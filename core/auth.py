import re

from core.session import (
    clear_auth_session,
    get_persisted_auth_tokens,
    is_authenticated,
    save_auth_session,
)
from core.supabase_client import supabase


USERNAME_PATTERN = re.compile(r"^[a-zA-Z0-9_]{3,30}$")
MOBILE_PATTERN = re.compile(r"^[6-9]\d{9}$")


def normalize_email(email):
    return (email or "").strip().lower()


def normalize_username(username):
    return (username or "").strip().lower()


def normalize_mobile(mobile):
    if not mobile:
        return ""
    return str(mobile).replace(" ", "").replace("-", "").strip()


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


def validate_signup(full_name, username, email, mobile_number, password, confirm_password):
    full_name = (full_name or "").strip()
    username = normalize_username(username)
    email = normalize_email(email)
    mobile = normalize_mobile(mobile_number)

    if not full_name:
        return False, "Full name is required."
    if not USERNAME_PATTERN.match(username):
        return False, "Username must be 3-30 characters and use only letters, numbers, or underscores."
    if not email or "@" not in email:
        return False, "Enter a valid email address."
    if not MOBILE_PATTERN.match(mobile):
        return False, "Please enter a valid 10-digit mobile number."
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


def sign_up(full_name, username, email, mobile_number, password, confirm_password):
    valid, message = validate_signup(full_name, username, email, mobile_number, password, confirm_password)
    if not valid:
        return False, message

    username = normalize_username(username)
    email = normalize_email(email)
    mobile = normalize_mobile(mobile_number)
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
                        "mobile_number": mobile,
                    }
                },
            }
        )
    except Exception as error:
        return False, _friendly_auth_error(error, context="signup")

    user = _auth_user(response)
    session = _auth_session(response)
    if not user:
        print(f"[TNPSC Nova Auth][Signup] Auth API returned no user object for '{username}'.")
        return False, "Something went wrong. Please try again."

    # Database trigger on_auth_user_created atomically inserts public.profiles row.
    # Client-side unauthenticated upsert is omitted here to prevent RLS policy errors.
    profile = {
        "id": _user_id(user),
        "username": username,
        "full_name": full_name,
        "email": email,
        "mobile_number": mobile,
    }

    if session:
        save_auth_session(session, user, profile)
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
        try:
            supabase.table("profiles").upsert(profile, on_conflict="id").execute()
        except Exception as pe:
            print(f"[TNPSC Nova Auth][Login] Login profile upsert fallback failed: {_sanitize_log_message(pe)}")

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


def validate_password_reset(password, confirm_password):
    if not password or len(password) < 8:
        return False, "Password must contain at least 8 characters."
    if password != confirm_password:
        return False, "Passwords do not match."
    return True, None


def update_password(new_password, confirm_password=None):
    if confirm_password is not None:
        valid, msg = validate_password_reset(new_password, confirm_password)
        if not valid:
            return False, msg
    elif not new_password or len(new_password) < 8:
        return False, "Password must contain at least 8 characters."

    try:
        session = supabase.auth.get_session()
    except Exception:
        session = None
    if not session:
        try:
            import streamlit as st

            tokens = st.session_state.get("recovery_tokens")
            if tokens and tokens.get("access_token") and tokens.get("refresh_token"):
                response = supabase.auth.set_session(tokens["access_token"], tokens["refresh_token"])
                session = _auth_session(response)
        except Exception:
            session = None
    if not session:
        return False, "This password reset link is invalid or has expired. Please request a new reset link."

    try:
        response = supabase.auth.update_user({"password": new_password})
    except Exception as error:
        return False, _friendly_auth_error(error, context="update_password")

    try:
        supabase.auth.sign_out()
    except Exception:
        pass
    try:
        import streamlit as st

        st.session_state.pop("recovery_tokens", None)
    except Exception:
        pass
    clear_auth_session()

    return True, "Password has been updated successfully. Please log in with your new password."


def handle_recovery_callback():
    """Detects and processes Supabase password recovery tokens from Streamlit URL query parameters."""
    try:
        import streamlit as st
    except ImportError:
        return False

    if not hasattr(st, "query_params"):
        return False

    query_params = dict(st.query_params)
    if not query_params:
        return False

    error = query_params.get("error")
    error_desc = query_params.get("error_description") or query_params.get("error_code")
    if error or error_desc:
        st.query_params.clear()
        st.session_state["recovery_error"] = "This password reset link is invalid or has expired. Please request a new reset link."
        st.session_state["auth_page"] = "reset_password"
        return True

    token_hash = query_params.get("token_hash")
    recovery_type = query_params.get("type")
    code = query_params.get("code")
    access_token = query_params.get("access_token")
    refresh_token = query_params.get("refresh_token")

    # Non-recovery auth callbacks (e.g. type="signup", type="invite") must never enter recovery
    if recovery_type and recovery_type != "recovery":
        return False

    if token_hash:
        if recovery_type != "recovery":
            return False
        st.query_params.clear()
        clear_auth_session()
        try:
            response = supabase.auth.verify_otp({"token_hash": token_hash, "type": "recovery"})
            session = _auth_session(response)
            if session or getattr(response, "user", None):
                st.session_state["recovery_session_active"] = True
                st.session_state["auth_page"] = "reset_password"
                return True
            st.session_state["recovery_error"] = "This password reset link is invalid or has expired. Please request a new reset link."
            st.session_state["auth_page"] = "reset_password"
            return False
        except Exception:
            st.session_state["recovery_error"] = "This password reset link is invalid or has expired. Please request a new reset link."
            st.session_state["auth_page"] = "reset_password"
            return False

    if code:
        st.query_params.clear()
        clear_auth_session()
        try:
            response = supabase.auth.exchange_code_for_session({"auth_code": code})
            session = _auth_session(response)
            if session:
                st.session_state["recovery_session_active"] = True
                st.session_state["auth_page"] = "reset_password"
                return True
            st.session_state["recovery_error"] = "This password reset link is invalid or has expired. Please request a new reset link."
            st.session_state["auth_page"] = "reset_password"
            return False
        except Exception:
            st.session_state["recovery_error"] = "This password reset link is invalid or has expired. Please request a new reset link."
            st.session_state["auth_page"] = "reset_password"
            return False

    if access_token or refresh_token:
        if recovery_type != "recovery" or not access_token or not refresh_token:
            if recovery_type == "recovery":
                st.query_params.clear()
                st.session_state["recovery_error"] = "This password reset link is invalid or has expired. Please request a new reset link."
                st.session_state["auth_page"] = "reset_password"
            return False
        st.query_params.clear()
        clear_auth_session()
        try:
            response = supabase.auth.set_session(access_token, refresh_token)
            session = _auth_session(response)
            if session or getattr(response, "user", None):
                st.session_state["recovery_session_active"] = True
                st.session_state["recovery_tokens"] = {
                    "access_token": access_token,
                    "refresh_token": refresh_token,
                }
                st.session_state["auth_page"] = "reset_password"
                return True
            st.session_state["recovery_error"] = "This password reset link is invalid or has expired. Please request a new reset link."
            st.session_state["auth_page"] = "reset_password"
            return False
        except Exception:
            st.session_state["recovery_error"] = "This password reset link is invalid or has expired. Please request a new reset link."
            st.session_state["auth_page"] = "reset_password"
            return False

    if recovery_type == "recovery":
        st.query_params.clear()
        st.session_state["recovery_error"] = "This password reset link is invalid or has expired. Please request a new reset link."
        st.session_state["auth_page"] = "reset_password"
        return False

    return False


def logout():
    try:
        import streamlit as st

        st.session_state.pop("recovery_tokens", None)
        st.session_state.pop("recovery_session_active", None)
        st.session_state.pop("recovery_error", None)
    except Exception:
        pass
    try:
        supabase.auth.sign_out()
    except Exception:
        pass
    clear_auth_session()


def _sanitize_log_message(msg):
    if not msg:
        return ""
    text = str(msg)
    text = re.sub(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", "[REDACTED_EMAIL]", text)
    text = re.sub(r"\b[6-9]\d{9}\b", "[REDACTED_MOBILE]", text)
    text = re.sub(r"eyJ[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+\.[a-zA-Z0-9_-]+", "[REDACTED_TOKEN]", text)
    return text


def _friendly_auth_error(error, context=None):
    text = str(error)
    lower = text.lower()
    context_label = (context or "auth").capitalize()
    sanitized_text = _sanitize_log_message(text)
    print(f"[TNPSC Nova Auth][{context_label}] Error: {sanitized_text}")

    if _looks_like_network_error(error):
        return "Unable to connect. Please check your internet connection."
    if (
        "rate limit" in lower
        or "too many requests" in lower
        or "429" in lower
        or "over_email_send_rate_limit" in lower
    ):
        return "Too many attempts. Please try again later."
    if "invalid login" in lower or "invalid credentials" in lower:
        return "Incorrect password."
    if "user not found" in lower or "not found" in lower:
        return "No account found with this email."
    if (
        "already registered" in lower
        or "already exists" in lower
        or "user_already_exists" in lower
        or "already been registered" in lower
    ):
        return "This email is already registered."
    if (
        ("password" in lower and ("weak" in lower or "short" in lower))
        or "at least 8" in lower
        or "should be at least" in lower
    ):
        return "Password must contain at least 8 characters."
    if (
        "invalid email" in lower
        or "email_invalid" in lower
        or "unable to validate email" in lower
    ):
        return "Enter a valid email address."
    if "email" in lower and "confirm" in lower:
        return "Please confirm your email before logging in."
    if context in ("reset", "recovery", "update_password") and (
        "token" in lower
        or "expired" in lower
        or "invalid" in lower
        or "otp" in lower
        or "session" in lower
    ):
        return "This password reset link is invalid or has expired. Please request a new reset link."
    if context == "reset" and ("invalid" in lower or "email" in lower):
        return "Enter a valid email address."
    return "Something went wrong. Please try again."

