"""Session-bound Firebase login for the isolated staging app."""
import hmac
import secrets
import time

from core.firebase_supabase import bind_firebase_profile
from core.session import clear_auth_session, is_authenticated, save_auth_session
from core.supabase_client import _SafeSupabaseClient

CHALLENGE_KEY = "_nova_firebase_challenge"
CLIENT_KEY = "_nova_supabase_client"
PROVIDER = "firebase"
CHALLENGE_SECONDS = 300


def login_challenge(state):
    challenge = state.get(CHALLENGE_KEY)
    if challenge is None or challenge[1] <= time.monotonic():
        challenge = (secrets.token_urlsafe(32), time.monotonic() + CHALLENGE_SECONDS)
        state[CHALLENGE_KEY] = challenge
    return challenge[0]


def accept_google_login(state, payload):
    if is_authenticated() or not isinstance(payload, dict):
        return False
    challenge = state.get(CHALLENGE_KEY)
    nonce = payload.get("nonce")
    token = payload.get("token")
    if (challenge is None or challenge[1] <= time.monotonic()
            or not isinstance(nonce, str) or not nonce.isascii()
            or not hmac.compare_digest(nonce, challenge[0])
            or not isinstance(token, str)):
        return False
    del state[CHALLENGE_KEY]

    binding = bind_firebase_profile(token)
    if binding.expires_at <= time.time():
        return False
    profile_id = str(binding.profile_id)
    profiles = (binding.client.table("profiles").select("id,username,full_name,email")
                .eq("id", profile_id).limit(2).execute().data)
    if len(profiles) != 1 or profiles[0].get("id") != profile_id:
        return False

    clear_auth_session()
    try:
        state[CLIENT_KEY] = _SafeSupabaseClient(binding.client)
        save_auth_session(
            {"provider": PROVIDER, "expires_at": binding.expires_at},
            {"id": profile_id}, profiles[0], persist=False,
        )
    except Exception:
        clear_auth_session()
        raise
    return True


def is_firebase_session(state):
    session = state.get("auth_session")
    return isinstance(session, dict) and session.get("provider") == PROVIDER


def firebase_session_valid(state):
    session = state["auth_session"]
    return (
        type(session.get("expires_at")) is int
        and session["expires_at"] > time.time()
        and CLIENT_KEY in state
        and is_authenticated()
    )
