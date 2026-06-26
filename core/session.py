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

    user_id = getattr(user, "id", None)
    email = getattr(user, "email", None)
    if isinstance(user, dict):
        user_id = user_id or user.get("id")
        email = email or user.get("email")

    st.session_state["user_id"] = user_id
    st.session_state["email"] = (profile or {}).get("email") or email
    st.session_state["username"] = (profile or {}).get("username") or email
    st.session_state["full_name"] = (profile or {}).get("full_name") or ""


def is_authenticated():
    return bool(st.session_state.get("auth_session") and st.session_state.get("user_id"))


def current_user_id():
    return st.session_state.get("user_id")


def current_username():
    return st.session_state.get("username", "")


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
