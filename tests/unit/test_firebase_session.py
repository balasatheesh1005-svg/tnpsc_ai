import time
from types import SimpleNamespace
from unittest.mock import Mock
from uuid import uuid4

import pytest

from core import firebase_session as google


@pytest.fixture
def session(monkeypatch):
    state = {}
    bind = Mock()
    monkeypatch.setattr(google, "bind_firebase_profile", bind)
    monkeypatch.setattr(google, "is_authenticated", lambda: bool(state.get("auth_session")))
    monkeypatch.setattr(google, "clear_auth_session", state.clear)

    def save(auth_session, user, profile, *, persist):
        assert not persist
        state["auth_session"] = auth_session

    monkeypatch.setattr(google, "save_auth_session", save)
    return state, bind


def test_foreign_session_challenge_is_rejected(session):
    state, bind = session
    google.login_challenge(state)
    foreign_nonce = google.login_challenge({})
    assert not google.accept_google_login(state, {"nonce": foreign_nonce, "token": "opaque"})
    bind.assert_not_called()


def test_expired_challenge_is_rejected(session):
    state, bind = session
    nonce = google.login_challenge(state)
    state[google.CHALLENGE_KEY] = (nonce, time.monotonic() - 1)
    assert not google.accept_google_login(state, {"nonce": nonce, "token": "opaque"})
    bind.assert_not_called()


def test_failed_binding_consumes_challenge(session):
    state, bind = session
    bind.side_effect = ValueError
    payload = {"nonce": google.login_challenge(state), "token": "opaque"}
    with pytest.raises(ValueError):
        google.accept_google_login(state, payload)
    assert not google.accept_google_login(state, payload)
    bind.assert_called_once_with("opaque")


def test_login_uses_bound_profile_and_session_client(session):
    state, bind = session
    profile_id = uuid4()
    client = Mock()
    client.table.return_value.select.return_value.eq.return_value.limit.return_value.execute.return_value.data = [
        {"id": str(profile_id)}
    ]
    bind.return_value = SimpleNamespace(client=client, profile_id=profile_id, expires_at=int(time.time()) + 60)
    payload = {"nonce": google.login_challenge(state), "token": "opaque"}
    assert google.accept_google_login(state, payload)
    assert google.is_firebase_session(state)
    assert google.firebase_session_valid(state)
    assert state[google.CLIENT_KEY]._client is client
    assert "opaque" not in repr(state["auth_session"])
    assert not google.accept_google_login(state, payload)
    state["auth_session"]["expires_at"] = int(time.time()) - 1
    assert not google.firebase_session_valid(state)


def test_firebase_logout_uses_local_session_cleanup(monkeypatch):
    from core import auth

    state = {"auth_session": {"provider": "firebase"}, google.CLIENT_KEY: object()}
    monkeypatch.setattr(auth, "st", SimpleNamespace(session_state=state))
    clear = Mock(side_effect=state.clear)
    supabase = Mock()
    monkeypatch.setattr(auth, "clear_auth_session", clear)
    monkeypatch.setattr(auth, "supabase", supabase)
    auth.logout()
    clear.assert_called_once()
    assert not state
    supabase.auth.sign_out.assert_not_called()
