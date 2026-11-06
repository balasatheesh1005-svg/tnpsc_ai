"""Offline staging guards; no real project credentials or schema access."""
import base64
import hashlib
import json
from unittest.mock import MagicMock, patch

import pytest
import streamlit as st
from core import auth, staging_config as config, supabase_client as clients


def test_valid_publishable_config_keeps_key_out_of_repr():
    settings = config.get_staging_config()
    assert settings.project_ref == 't' * 20
    assert settings.app_url == 'https://nova-staging-test.streamlit.app'
    assert settings.supabase_key not in repr(settings)


@pytest.mark.parametrize('secrets', [{}, {'staging': {}}, {'staging': {'mode': 'production'}}])
def test_missing_secrets_fail_before_sdk_initialization(monkeypatch, secrets):
    monkeypatch.setattr(st, 'secrets', secrets)
    with patch.object(clients, 'create_client') as factory:
        with pytest.raises(config.StagingConfigurationError):
            clients.get_supabase_client()
        factory.assert_not_called()


def test_blocked_production_project_fingerprint(monkeypatch):
    monkeypatch.setattr(config, 'BLOCKED_PROJECT_HASHES', {hashlib.sha256(('t' * 20).encode()).hexdigest()})
    with pytest.raises(config.StagingConfigurationError, match='Production'):
        config.get_staging_config()


@pytest.mark.parametrize('section,key,value', [
    ('staging', 'mode', 'production'),
    ('staging', 'expected_project_ref', 'wrong-project'),
    ('supabase', 'url', 'https://' + 'x' * 20 + '.supabase.co'),
    ('supabase', 'url', 'http://' + 't' * 20 + '.supabase.co'),
    ('supabase', 'url', 'https://attacker.invalid'),
    ('supabase', 'url', 'https://' + 't' * 20 + '.supabase.co?key=leak'),
    ('supabase', 'publishable_key', 'sb_secret_synthetic_rejected'),
    ('supabase', 'publishable_key', 'not-a-key'),
    ('staging', 'app_url', 'https://production.streamlit.app'),
    ('staging', 'app_url', 'http://nova-test.streamlit.app'),
    ('staging', 'app_url', 'https://nova-test.streamlit.app.evil.invalid'),
    ('staging', 'app_url', 'https://user:password@nova-test.streamlit.app'),
    ('staging', 'app_url', 'https://nova-test.streamlit.app/?redirect=evil'),
    ('staging', 'app_url', 'https://nova-test.streamlit.app/#token'),
])
def test_unsafe_configuration_rejected_without_echoing_values(section, key, value):
    st.secrets[section][key] = value
    with pytest.raises(config.StagingConfigurationError) as error:
        config.get_staging_config()
    assert value not in str(error.value)


def anon_key(role='anon', ref='t' * 20):
    claims = base64.urlsafe_b64encode(json.dumps({'role': role, 'ref': ref}).encode()).decode().rstrip('=')
    return f'header.{claims}.synthetic-signature'


def test_legacy_anon_key_must_belong_to_test_project():
    st.secrets['supabase']['publishable_key'] = anon_key()
    assert config.get_staging_config().supabase_key == anon_key()


@pytest.mark.parametrize('key', [anon_key(role='service_role'), anon_key(ref='x' * 20)])
def test_legacy_privileged_or_wrong_project_key_rejected(key):
    st.secrets['supabase']['publishable_key'] = key
    with pytest.raises(config.StagingConfigurationError):
        config.get_staging_config()


def test_reset_redirect_is_from_secrets_not_query_parameters():
    with patch.object(st, 'query_params', {'redirect_to': 'https://attacker.invalid'}), \
         patch.object(auth, 'supabase') as sdk:
        assert auth.send_password_reset('learner@example.test')[0]
        sdk.auth.reset_password_for_email.assert_called_once_with(
            'learner@example.test', options={'redirect_to': 'https://nova-staging-test.streamlit.app'})


def test_reset_never_uses_sdk_without_valid_staging_configuration(monkeypatch):
    monkeypatch.setattr(st, 'secrets', {})
    with patch.object(auth, 'supabase') as sdk:
        assert not auth.send_password_reset('learner@example.test')[0]
        sdk.auth.reset_password_for_email.assert_not_called()
        sdk.auth.reset_password_email.assert_not_called()
