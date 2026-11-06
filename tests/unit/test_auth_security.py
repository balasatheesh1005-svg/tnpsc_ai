"""Network-free regression tests. No claim of live Supabase validation."""
from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest
import streamlit as st
from core import auth, session, remember_me as remember, supabase_client as clients


@pytest.fixture(autouse=True)
def isolated_state():
    with patch.object(st, 'session_state', {}), patch.object(st, 'query_params', {}):
        remember._records.clear()
        yield
        remember._records.clear()


def cookie_manager():
    cookies = {}
    manager = MagicMock()
    manager.get.side_effect = cookies.get
    manager.set.side_effect = lambda name, value, **kw: cookies.update({name: value})
    manager.delete.side_effect = lambda name, **kw: cookies.pop(name, None)
    st.session_state['_remember_cookie_manager'] = manager
    return manager, cookies


def test_legacy_urls_are_scrubbed_without_authentication():
    st.query_params.update(tnpsc_at='injected', tnpsc_rt='injected', campaign='group4')
    with patch.object(auth, 'supabase') as client:
        assert not auth.restore_auth_session()
        client.auth.set_session.assert_not_called()
    assert st.query_params == {'campaign': 'group4'}


def test_save_does_not_write_tokens_to_url_or_cookie_when_disabled():
    manager, cookies = cookie_manager()
    session.persist_auth_session({'access_token': 'private-at', 'refresh_token': 'private-rt'})
    assert not st.query_params
    assert not cookies
    assert not remember._records
    manager.set.assert_not_called()


def test_remember_restore_and_logout_revocation():
    manager, cookies = cookie_manager()
    st.session_state['remember_me'] = True
    tokens = {'access_token': 'private-at', 'refresh_token': 'private-rt'}
    session.persist_auth_session(tokens)
    handle = cookies[remember.COOKIE]
    assert len(handle) == 64 and 'private' not in handle
    kwargs = manager.set.call_args.kwargs
    assert kwargs['secure'] and kwargs['same_site'] == 'strict'
    st.session_state.pop('_remember_handle')
    assert remember.recalled_tokens() == tokens
    session.clear_auth_session()
    assert not remember._records and not cookies
    cookies[remember.COOKIE] = handle
    assert remember.recalled_tokens() == {}


def test_remember_expiry_and_unknown_handle_fail_closed():
    _, cookies = cookie_manager()
    st.session_state['remember_me'] = True
    with patch.object(remember.time, 'time', return_value=100):
        session.persist_auth_session({'access_token': 'at', 'refresh_token': 'rt'})
    with patch.object(remember.time, 'time', return_value=100 + remember.TTL + 1):
        assert remember.recalled_tokens() == {}
    cookies[remember.COOKIE] = 'a' * 64
    assert remember.recalled_tokens() == {}


def test_refresh_keeps_handle_and_absolute_expiry():
    _, cookies = cookie_manager()
    st.session_state['remember_me'] = True
    session.persist_auth_session({'access_token': 'old', 'refresh_token': 'old'})
    handle = cookies[remember.COOKIE]
    expiry = remember._records[remember._digest(handle)][0]
    session.persist_auth_session({'access_token': 'new', 'refresh_token': 'new'})
    assert cookies[remember.COOKIE] == handle
    assert remember.recalled_tokens()['refresh_token'] == 'new'
    assert remember._records[remember._digest(handle)][0] == expiry


def test_client_proxy_isolates_auth_and_table_requests_across_users():
    first, second = {}, {}
    with patch.object(clients, 'create_client', side_effect=lambda *a, **kw: MagicMock()) as factory:
        with patch.object(st, 'session_state', first):
            a = clients.get_supabase_client()
            clients.supabase.auth.set_session('a', 'a-refresh')
            assert clients.get_supabase_client() is a
        with patch.object(st, 'session_state', second):
            b = clients.get_supabase_client()
            clients.supabase.auth.set_session('b', 'b-refresh')
            clients.supabase.table('profiles')
            b._client.table.assert_called_once_with('profiles')
        assert a is not b
        a.auth.set_session.assert_called_once_with('a', 'a-refresh')
        b.auth.set_session.assert_called_once_with('b', 'b-refresh')
        assert factory.call_count == 2
        assert factory.call_args.kwargs['options'].auto_refresh_token is False
        with patch.object(st, 'session_state', first):
            session.clear_auth_session()
            assert clients.get_supabase_client() is not a


def test_expired_active_session_refreshes_and_rotates_saved_tokens():
    st.session_state.update(auth_session=SimpleNamespace(expires_at=1), user_id='a', auth_profile={'id': 'a'})
    refreshed = SimpleNamespace(expires_at=9999999999, access_token='new', refresh_token='new')
    with patch.object(auth, 'supabase') as client, patch.object(auth, 'save_auth_session') as save:
        client.auth.refresh_session.return_value = SimpleNamespace(session=refreshed, user=SimpleNamespace(id='a'))
        assert auth.restore_auth_session()
        save.assert_called_once()
        client.auth.refresh_session.assert_called_once()


def test_failed_restore_revokes_handle_and_discards_client():
    _, cookies = cookie_manager()
    st.session_state['remember_me'] = True
    session.persist_auth_session({'access_token': 'at', 'refresh_token': 'rt'})
    st.session_state['_nova_supabase_client'] = object()
    with patch.object(auth, 'supabase') as client:
        client.auth.set_session.side_effect = ValueError('expired')
        assert not auth.restore_auth_session()
    assert not cookies and not remember._records
    assert '_nova_supabase_client' not in st.session_state


def test_new_failed_recovery_cannot_reuse_previous_recovery_tokens():
    st.session_state.update(recovery_session_active=True, recovery_tokens={'access_token': 'old', 'refresh_token': 'old'})
    st.query_params.update(token_hash='expired', type='recovery')
    with patch.object(auth, 'supabase') as client:
        client.auth.verify_otp.side_effect = ValueError('expired')
        assert not auth.handle_recovery_callback()
    assert 'recovery_tokens' not in st.session_state
    assert not st.session_state.get('recovery_session_active')
    assert not st.query_params


def test_remember_choice_survives_login_widget_cleanup():
    _, cookies = cookie_manager()
    st.session_state['remember_me'] = True
    session.persist_auth_session({'access_token': 'old', 'refresh_token': 'old'})
    del st.session_state['remember_me']  # Streamlit removes widgets on another page.
    session.persist_auth_session({'access_token': 'new', 'refresh_token': 'new'})
    assert cookies and remember.recalled_tokens()['access_token'] == 'new'


@pytest.mark.parametrize('identifier', ['learner', 'learner@example.com'])
def test_login_and_remember_reload_preserve_identity(identifier):
    _, cookies = cookie_manager()
    st.session_state['remember_me'] = True
    profile = {'id': 'uuid-a', 'username': 'learner', 'email': 'learner@example.com'}
    tokens = SimpleNamespace(access_token='at', refresh_token='rt')
    response = SimpleNamespace(session=tokens, user=SimpleNamespace(id='uuid-a', email=profile['email']))
    with patch.object(auth, 'supabase') as client, \
         patch.object(auth, 'get_profile_by_username', return_value=profile), \
         patch.object(auth, 'get_profile_by_email', return_value=profile), \
         patch.object(auth, 'get_profile_by_user_id', return_value=profile):
        client.auth.sign_in_with_password.return_value = response
        client.auth.set_session.return_value = response
        assert auth.login(identifier, 'synthetic-password')[0]
        assert session.current_user_id() == 'uuid-a'
        for key in session.AUTH_KEYS:
            st.session_state.pop(key, None)
        assert auth.restore_auth_session()
        assert session.current_user_id() == 'uuid-a'
        assert cookies and not st.query_params


def test_pkce_callback_preserves_session_local_verifier_client():
    sdk = MagicMock()
    sdk.auth.exchange_code_for_session.return_value = SimpleNamespace(session=object())
    st.session_state['_nova_supabase_client'] = clients._SafeSupabaseClient(sdk)
    st.query_params.update(code='synthetic-pkce', type='recovery')
    assert auth.handle_recovery_callback()
    sdk.auth.exchange_code_for_session.assert_called_once_with({'auth_code': 'synthetic-pkce'})
    assert clients.get_supabase_client()._client is sdk
