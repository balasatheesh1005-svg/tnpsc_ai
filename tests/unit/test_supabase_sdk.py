"""Real SDK constructors and auth state; synthetic HTTP responses, never live Supabase."""
import base64
import json
import time
from unittest.mock import MagicMock, patch

import httpx
import pytest
import streamlit as st
from supabase import Client

from core import auth, remember_me, session, supabase_client as clients


USERS = {
    'alice': {'id': '00000000-0000-0000-0000-000000000001', 'username': 'alice', 'email': 'alice@example.test'},
    'bob': {'id': '00000000-0000-0000-0000-000000000002', 'username': 'bob', 'email': 'bob@example.test'},
}


def user_data(name):
    return {
        **USERS[name], 'aud': 'authenticated', 'role': 'authenticated',
        'app_metadata': {}, 'user_metadata': {}, 'created_at': '2026-01-01T00:00:00Z',
    }


def token_data(name):
    def encode(value):
        return base64.urlsafe_b64encode(json.dumps(value).encode()).decode().rstrip('=')
    expires = int(time.time()) + 3600
    token = '.'.join((encode({'alg': 'HS256', 'typ': 'JWT'}),
                      encode({'exp': expires, 'sub': USERS[name]['id']}),
                      'synthetic-signature'))
    return {'access_token': token, 'refresh_token': f'synthetic-refresh-{name}',
            'token_type': 'bearer', 'expires_in': 3600, 'expires_at': expires,
            'user': user_data(name)}


@pytest.fixture(autouse=True)
def sdk_environment(monkeypatch):
    # Test the application's real create_client call, with no production config.
    monkeypatch.setattr(clients, 'SUPABASE_URL', 'https://unit-test.invalid')
    monkeypatch.setattr(clients, 'SUPABASE_KEY', 'synthetic-sdk-test-key')
    # Host proxy settings are unrelated to SDK initialization and may require extras.
    for key in ('HTTP_PROXY', 'HTTPS_PROXY', 'ALL_PROXY', 'http_proxy', 'https_proxy', 'all_proxy'):
        monkeypatch.delenv(key, raising=False)
    with patch.object(st, 'session_state', {}), patch.object(st, 'query_params', {}):
        remember_me._records.clear()
        yield
        remember_me._records.clear()


@pytest.fixture
def synthetic_http(monkeypatch):
    requests = []

    def send(http_client, request, **kwargs):
        assert request.url.host == 'unit-test.invalid'
        requests.append(request)
        path = request.url.path
        payload = json.loads(request.content) if request.content else {}
        if path == '/rest/v1/profiles':
            data = list(USERS.values())
            for key in ('id', 'username', 'email'):
                match = request.url.params.get(key)
                if match:
                    data = [row for row in data if row[key] == match.removeprefix('eq.')]
        elif path in ('/auth/v1/token', '/auth/v1/verify'):
            name = payload.get('email', 'alice').split('@')[0]
            data = token_data(name)
        elif path == '/auth/v1/user':
            bearer = request.headers.get('authorization', '')
            payload_segment = bearer.removeprefix('Bearer ').split('.')[1]
            claims = json.loads(base64.urlsafe_b64decode(payload_segment + '=' * (-len(payload_segment) % 4)))
            name = next(name for name, row in USERS.items() if row['id'] == claims['sub'])
            data = user_data(name)
        elif path in ('/auth/v1/recover', '/auth/v1/logout'):
            data = {}
        else:
            pytest.fail(f'Unexpected synthetic SDK request: {request.method} {path}')
        return httpx.Response(200, json=data, request=request)

    # The SDK builds and parses real HTTP messages, but send never opens a socket.
    monkeypatch.setattr(httpx.Client, 'send', send)
    return requests


def install_cookie_manager():
    cookies = {}
    manager = MagicMock()
    manager.get.side_effect = cookies.get
    manager.set.side_effect = lambda cookie, value, **kwargs: cookies.update({cookie: value})
    manager.delete.side_effect = lambda cookie, **kwargs: cookies.pop(cookie, None)
    st.session_state['_remember_cookie_manager'] = manager
    return cookies


def test_real_sdk_initialization_has_storage_and_isolates_clients():
    first_state, second_state = {}, {}
    with patch.object(st, 'session_state', first_state):
        first = clients.get_supabase_client()
        assert isinstance(first._client, Client)
        assert clients.get_supabase_client() is first
        assert first.auth.get_session() is None
        assert first._client.options.auto_refresh_token is False
        assert first._client.options.persist_session is False
        first._client.options.storage.set_item('isolation-marker', 'alice')
        first.table('profiles').select('*')  # Construct only; no execute/network.
        first.storage.from_('synthetic-bucket')
    with patch.object(st, 'session_state', second_state):
        second = clients.get_supabase_client()
        assert isinstance(second._client, Client)
        assert first is not second
        assert first.auth is not second.auth
        assert first._client.options.storage is not second._client.options.storage
        assert second._client.options.storage.get_item('isolation-marker') is None
        assert second.auth.get_session() is None


@pytest.mark.parametrize('remember', [False, True])
def test_real_sdk_login_remember_restore_logout(synthetic_http, remember):
    cookies = install_cookie_manager()
    st.session_state['_remember_enabled'] = remember
    assert auth.login('alice@example.test', 'synthetic-password')[0]
    sdk = clients.get_supabase_client()
    assert sdk.auth.get_session().user.id == USERS['alice']['id']
    assert session.current_user_id() == USERS['alice']['id']
    assert not st.query_params
    assert bool(cookies) == remember
    if remember:
        # Simulate a new Streamlit session with the same browser cookie.
        manager = st.session_state['_remember_cookie_manager']
        st.session_state.clear()
        st.session_state['_remember_cookie_manager'] = manager
        assert auth.restore_auth_session()
        restored = clients.get_supabase_client()
        assert restored is not sdk
        assert restored.auth.get_session().user.id == USERS['alice']['id']
        sdk = restored
    auth.logout()
    assert sdk.auth.get_session() is None
    assert not session.is_authenticated()
    assert '_nova_supabase_client' not in st.session_state
    assert not cookies and not remember_me._records
    assert not auth.restore_auth_session()


def test_real_sdk_logout_does_not_change_other_user(synthetic_http):
    alice_state, bob_state = {}, {}
    with patch.object(st, 'session_state', alice_state):
        assert auth.login('alice', 'synthetic-password')[0]
        alice_client = clients.get_supabase_client()
    with patch.object(st, 'session_state', bob_state):
        assert auth.login('bob', 'synthetic-password')[0]
        bob_client = clients.get_supabase_client()
        bob_session = bob_client.auth.get_session()
        assert bob_session.user.id == USERS['bob']['id']
    with patch.object(st, 'session_state', alice_state):
        auth.logout()
        assert alice_client.auth.get_session() is None
    with patch.object(st, 'session_state', bob_state):
        assert clients.get_supabase_client() is bob_client
        assert bob_client.auth.get_session() is bob_session
        assert session.current_user_id() == USERS['bob']['id']


def test_real_sdk_password_reset_callback_update_and_cleanup(synthetic_http):
    assert auth.send_password_reset('alice@example.test')[0]
    st.query_params.update(token_hash='synthetic-recovery-hash', type='recovery')
    assert auth.handle_recovery_callback()
    assert not st.query_params
    assert st.session_state['recovery_session_active']
    sdk = clients.get_supabase_client()
    assert sdk.auth.get_session().user.id == USERS['alice']['id']
    assert auth.update_password('SyntheticNewPassword123', 'SyntheticNewPassword123')[0]
    assert sdk.auth.get_session() is None
    assert not st.session_state.get('recovery_session_active')
    assert '_nova_supabase_client' not in st.session_state
    assert not session.is_authenticated()
    assert any(request.url.path == '/auth/v1/recover' for request in synthetic_http)
    assert any(request.method == 'PUT' and request.url.path == '/auth/v1/user' for request in synthetic_http)


def test_proxy_introspection_does_not_initialize_a_client():
    assert not hasattr(clients.supabase, '__func__')
    assert '_nova_supabase_client' not in st.session_state
