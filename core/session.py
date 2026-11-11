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


def persist_auth_session(session):
    clear_legacy_url_tokens()
    from core.remember_me import remember_session
    remember_session(session, enabled=st.session_state.get("_remember_enabled", st.session_state.get("remember_me", False)))


def get_persisted_auth_tokens():
    # Legacy URL credentials are untrusted and must never establish identity.
    clear_legacy_url_tokens()
    from core.remember_me import recalled_tokens
    return recalled_tokens()


def clear_legacy_url_tokens():
    for key in PERSISTED_SESSION_KEYS.values():
        if key in st.query_params:
            del st.query_params[key]


def clear_persisted_auth_session():
    clear_legacy_url_tokens()
    from core.remember_me import forget_session
    forget_session()


def save_auth_session(session, user, profile, *, persist=True):
    st.session_state["auth_session"] = session
    st.session_state["auth_user"] = user
    st.session_state["auth_profile"] = profile or {}
    if persist:
        persist_auth_session(session)

    profile_dict = profile or {}

    # Extract user_id UUID from profiles.id first, falling back to auth user object
    user_id = profile_dict.get("id") or getattr(user, "id", None)
    if isinstance(user, dict) and not user_id:
        user_id = user.get("id")

    email = profile_dict.get("email") or getattr(user, "email", None)
    if isinstance(user, dict) and not email:
        email = user.get("email")

    raw_username = profile_dict.get("username")
    raw_full_name = profile_dict.get("full_name")

    from core.user_identity import get_safe_public_identity

    username = get_safe_public_identity(
        raw_identifier=raw_username,
        full_name=raw_full_name,
        seed=str(user_id) if user_id else (email or "learner"),
    )

    st.session_state["user_id"] = str(user_id) if user_id else None
    st.session_state["username"] = username
    st.session_state["email"] = email
    st.session_state["full_name"] = raw_full_name or ""


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


def clear_auth_session(discard_client=True):
    for key in AUTH_KEYS:
        st.session_state.pop(key, None)
    st.session_state.pop("_nova_firebase_challenge", None)
    clear_persisted_auth_session()
    if discard_client:
        st.session_state.pop("_nova_supabase_client", None)


def reset_app_state_for_logout():
    clear_auth_session()
    for key in list(st.session_state.keys()):
        st.session_state.pop(key, None)
