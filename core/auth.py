import re

from core.session import (
    clear_auth_session,
    get_persisted_auth_tokens,
    is_authenticated,
    save_auth_session,
)
from core.supabase_client import supabase


USERNAME_PATTERN = re.compile(r"^[a-zA-Z0-9_]{3,30}$")


def normalize_email(email):
    return (email or "").strip().lower()


def normalize_username(username):
    return (username or "").strip().lower()


def _first_row(response):
    rows = getattr(response, "data", None) or []
    return rows[0] if rows else None


def _auth_user(response):
    return getattr(response, "user", None) or getattr(getattr(response, "session", None), "user", None)


def _auth_session(response):
    return getattr(response, "session", None)


def _user_id(user):
    if isinstance(user, dict):
        return user.get("id")
    return getattr(user, "id", None)


def _user_email(user):
    if isinstance(user, dict):
        return user.get("email")
    return getattr(user, "email", None)


def _looks_like_network_error(error):
    lower = str(error).lower()
    markers = (
        "connection",
        "timeout",
        "timed out",
        "network",
        "dns",
        "name resolution",
        "temporary failure",
        "max retries",
        "remote end closed",
    )
    return any(marker in lower for marker in markers)


def validate_signup(full_name, username, email, password, confirm_password):
    full_name = (full_name or "").strip()
    username = normalize_username(username)
    email = normalize_email(email)

    if not full_name:
        return False, "Full name is required."
    if not USERNAME_PATTERN.match(username):
        return False, "Username must be 3-30 characters and use only letters, numbers, or underscores."
    if not email or "@" not in email:
        return False, "Enter a valid email address."
    if len(password or "") < 8:
        return False, "Password must contain at least 8 characters."
    if password != confirm_password:
        return False, "Passwords do not match."

    return True, None


def get_profile_by_user_id(user_id):
    if not user_id:
        return None
    response = supabase.table("profiles").select("*").eq("id", user_id).limit(1).execute()
    return _first_row(response)


def get_profile_by_username(username):
    username = normalize_username(username)
    if not username:
        return None
    response = supabase.table("profiles").select("*").eq("username", username).limit(1).execute()
    return _first_row(response)


def get_profile_by_email(email):
    email = normalize_email(email)
    if not email:
        return None
    response = supabase.table("profiles").select("*").eq("email", email).limit(1).execute()
    return _first_row(response)


def username_exists(username):
    return get_profile_by_username(username) is not None


def email_exists(email):
    return get_profile_by_email(email) is not None


def restore_auth_session():
    if is_authenticated():
        return True

    tokens = get_persisted_auth_tokens()
    access_token = tokens.get("access_token")
    refresh_token = tokens.get("refresh_token")
    if not access_token or not refresh_token:
        return False

    try:
        response = supabase.auth.set_session(access_token, refresh_token)
    except Exception:
        clear_auth_session()
        return False

    session = _auth_session(response)
    user = _auth_user(response)
    if not session or not user:
        clear_auth_session()
        return False

    email = _user_email(user)
    profile = get_profile_by_user_id(_user_id(user)) or get_profile_by_email(email) or {}
    if not profile:
        profile = {
            "id": _user_id(user),
            "username": email,
            "full_name": "",
            "email": email,
            "xp": 0,
            "streak": 0,
            "level": 1,
            "profile_photo": None,
        }

    save_auth_session(session, user, profile)
    return True


def sign_up(full_name, username, email, password, confirm_password):
    valid, message = validate_signup(full_name, username, email, password, confirm_password)
    if not valid:
        return False, message

    username = normalize_username(username)
    email = normalize_email(email)
    full_name = full_name.strip()

    if username_exists(username):
        return False, "This username is already taken."
    if email_exists(email):
        return False, "This email is already registered."

    try:
        response = supabase.auth.sign_up(
            {
                "email": email,
                "password": password,
                "options": {
                    "data": {
                        "full_name": full_name,
                        "username": username,
                    }
                },
            }
        )
    except Exception as error:
        return False, _friendly_auth_error(error, context="signup")

    user = _auth_user(response)
    session = _auth_session(response)
    if not user:
        return False, "Something went wrong. Please try again."

    profile = {
        "id": _user_id(user),
        "username": username,
        "full_name": full_name,
        "email": email,
    }

    profile_response = supabase.table("profiles").upsert(profile, on_conflict="id").execute()
    saved_profile = _first_row(profile_response) or profile

    if session:
        save_auth_session(session, user, saved_profile)
        return True, "Account created successfully."

    return True, "Account created. Please check your email if confirmation is enabled, then login."


def login(identifier, password):
    identifier = (identifier or "").strip()
    if not identifier or not password:
        return False, "Enter your email or username and password."

    email = normalize_email(identifier)
    if "@" not in identifier:
        profile = get_profile_by_username(identifier)
        if not profile:
            return False, "Username does not exist."
        email = profile.get("email")
    else:
        profile = get_profile_by_email(email)

    try:
        response = supabase.auth.sign_in_with_password(
            {"email": email, "password": password}
        )
    except Exception as error:
        if "@" in identifier and not profile and "invalid" in str(error).lower():
            return False, "No account found with this email."
        return False, _friendly_auth_error(error, context="login")

    session = _auth_session(response)
    user = _auth_user(response)
    if not session or not user:
        return False, "Incorrect password."

    profile = get_profile_by_user_id(_user_id(user)) or get_profile_by_email(email) or {}
    if not profile:
        profile = {
            "id": _user_id(user),
            "username": email,
            "full_name": "",
            "email": email,
        }
        supabase.table("profiles").upsert(profile, on_conflict="id").execute()

    save_auth_session(session, user, profile)
    return True, "Logged in successfully."



def send_password_reset(email):
    email = normalize_email(email)
    if not email or "@" not in email:
        return False, "Enter a valid email address."

    try:
        supabase.auth.reset_password_for_email(email)
    except AttributeError:
        try:
            supabase.auth.reset_password_email(email)
        except Exception as error:
            return False, _friendly_auth_error(error, context="reset")
    except Exception as error:
        return False, _friendly_auth_error(error, context="reset")

    return True, "Password reset link has been sent to your email."


def logout():
    try:
        supabase.auth.sign_out()
    except Exception:
        pass
    clear_auth_session()


def _friendly_auth_error(error, context=None):
    text = str(error)
    lower = text.lower()
    if _looks_like_network_error(error):
        return "Unable to connect. Please check your internet connection."
    if "invalid login" in lower or "invalid credentials" in lower:
        return "Incorrect password."
    if "user not found" in lower or "not found" in lower:
        return "No account found with this email."
    if "already registered" in lower or "already exists" in lower:
        return "This email is already registered."
    if ("password" in lower and "weak" in lower) or "at least 8" in lower:
        return "Password must contain at least 8 characters."
    if "email" in lower and "confirm" in lower:
        return "Please confirm your email before logging in."
    if context == "reset" and ("invalid" in lower or "email" in lower):
        return "Enter a valid email address."
    return "Something went wrong. Please try again."
