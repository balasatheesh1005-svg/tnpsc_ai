import streamlit as st


AUTH_KEYS = (
    "auth_session",
    "auth_user",
    "auth_profile",
    "user_id",
    "username",
    "full_name",
    "email",
)

PERSISTED_SESSION_KEYS = {
    "access_token": "tnpsc_at",
    "refresh_token": "tnpsc_rt",
}


def _session_value(session, key):
    if isinstance(session, dict):
        return session.get(key)
    return getattr(session, key, None)


def _query_value(key):
    value = st.query_params.get(key)
    if isinstance(value, list):
        return value[0] if value else None
    return value


def persist_auth_session(session):
    access_token = _session_value(session, "access_token")
    refresh_token = _session_value(session, "refresh_token")
    if not access_token or not refresh_token:
        return

    st.query_params[PERSISTED_SESSION_KEYS["access_token"]] = access_token
    st.query_params[PERSISTED_SESSION_KEYS["refresh_token"]] = refresh_token


def get_persisted_auth_tokens():
    return {
        "access_token": _query_value(PERSISTED_SESSION_KEYS["access_token"]),
        "refresh_token": _query_value(PERSISTED_SESSION_KEYS["refresh_token"]),
    }


def clear_persisted_auth_session():
    for key in PERSISTED_SESSION_KEYS.values():
        if key in st.query_params:
            del st.query_params[key]


def save_auth_session(session, user, profile):
    st.session_state["auth_session"] = session
    st.session_state["auth_user"] = user
    st.session_state["auth_profile"] = profile or {}
    persist_auth_session(session)

    profile_dict = profile or {}

    # Extract user_id UUID from profiles.id first, falling back to auth user object
    user_id = profile_dict.get("id") or getattr(user, "id", None)
    if isinstance(user, dict) and not user_id:
        user_id = user.get("id")

    email = profile_dict.get("email") or getattr(user, "email", None)
    if isinstance(user, dict) and not email:
        email = user.get("email")

    username = profile_dict.get("username") or email or ""

    st.session_state["user_id"] = str(user_id) if user_id else None
    st.session_state["username"] = username
    st.session_state["email"] = email
    st.session_state["full_name"] = profile_dict.get("full_name") or ""


def is_authenticated():
    return bool(st.session_state.get("auth_session") and st.session_state.get("user_id"))


def current_user_id():
    """Returns the current logged in user's profiles.id UUID."""
    return st.session_state.get("user_id")


def current_username():
    """Returns the current logged in username for display and legacy lookups."""
    return st.session_state.get("username", "")


def current_user_email():
    """Returns the current logged in user email."""
    return st.session_state.get("email", "")


def get_session_identity():
    """Returns dual-identity dictionary for the current session state."""
    return {
        "user_id": st.session_state.get("user_id"),
        "username": st.session_state.get("username", ""),
        "email": st.session_state.get("email", ""),
    }


def clear_auth_session():
    for key in AUTH_KEYS:
        st.session_state.pop(key, None)
    clear_persisted_auth_session()


def reset_app_state_for_logout():
    preserved = set(AUTH_KEYS)
    for key in list(st.session_state.keys()):
        if key not in preserved:
            st.session_state.pop(key, None)
    clear_auth_session()

