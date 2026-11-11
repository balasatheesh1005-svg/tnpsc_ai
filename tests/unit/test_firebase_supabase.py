from types import SimpleNamespace
from unittest.mock import Mock
from uuid import uuid4

import pytest

from core import firebase_supabase as binding
from core.staging_config import StagingConfig


@pytest.fixture
def setup(monkeypatch):
    project = binding.SUPABASE_PROJECT
    config = StagingConfig(f"https://{project}.supabase.co", "sb_publishable_test",
                           "https://nova-test.streamlit.app", project)
    validator = Mock()
    validator.return_value.validate.return_value = SimpleNamespace(expires_at=12345)
    factory = Mock(side_effect=lambda *args, **kwargs: Mock())
    monkeypatch.setattr(binding, "FirebaseGoogleTokenValidator", validator)
    monkeypatch.setattr(binding, "create_client", factory)
    config_loader = Mock(return_value=config)
    monkeypatch.setattr(binding, "get_staging_config", config_loader)
    return config_loader, validator, factory


def test_verifies_token_before_using_database(setup):
    _, validator, factory = setup
    validator.return_value.validate.side_effect = ValueError()
    with pytest.raises(ValueError):
        binding.bind_firebase_profile("invalid")
    factory.assert_not_called()


def test_wrong_database_fails_before_verification(setup):
    config_loader, validator, factory = setup
    config_loader.return_value = StagingConfig("https://wrong.supabase.co", "unused", "unused", binding.SUPABASE_PROJECT)
    with pytest.raises(binding.FirebaseProfileBindingError):
        binding.bind_firebase_profile("token")
    validator.assert_not_called()
    factory.assert_not_called()


def test_clients_and_bearers_are_separate(setup):
    _, _, factory = setup
    clients = [Mock(), Mock()]
    ids = [uuid4(), uuid4()]
    factory.side_effect = clients
    for client, profile_id in zip(clients, ids):
        client.rpc.return_value.execute.return_value.data = str(profile_id)
        client.table.return_value.select.return_value.limit.return_value.execute.return_value.data = [
            {"id": str(profile_id)}
        ]
    for client, profile_id, token in zip(clients, ids, ("first", "second")):
        result = binding.bind_firebase_profile(token)
        assert result.client is client
        assert result.profile_id == profile_id
        assert result.expires_at == 12345
        client.postgrest.auth.assert_called_once_with(token)
        client.auth.set_session.assert_not_called()


@pytest.mark.parametrize("profiles", [[], [{"id": "bad"}], [{"id": "first"}, {"id": "second"}]])
def test_no_valid_unique_profile_denies_binding(setup, profiles):
    _, _, factory = setup
    client = Mock()
    factory.side_effect = [client]
    client.rpc.return_value.execute.return_value.data = str(uuid4())
    client.table.return_value.select.return_value.limit.return_value.execute.return_value.data = profiles
    with pytest.raises(binding.FirebaseProfileBindingError, match="linked staging profile"):
        binding.bind_firebase_profile("token")


def test_real_sdk_sends_firebase_bearer_and_publishable_key(setup):
    import httpx
    from supabase import create_client

    _, _, factory = setup
    profile_id = str(uuid4())
    paths = []

    def respond(request):
        assert request.headers["Authorization"] == "Bearer verified-test-token"
        assert request.headers["apikey"] == "sb_publishable_test"
        paths.append(request.url.path)
        if request.url.path.endswith("/get_linked_firebase_profile_id"):
            return httpx.Response(200, json=profile_id)
        return httpx.Response(200, json=[{"id": profile_id}])

    with httpx.Client(transport=httpx.MockTransport(respond)) as transport:
        def create(url, key, *, options):
            options.httpx_client = transport
            return create_client(url, key, options=options)

        factory.side_effect = create
        assert str(binding.bind_firebase_profile("verified-test-token").profile_id) == profile_id

    assert paths == ["/rest/v1/rpc/get_linked_firebase_profile_id", "/rest/v1/profiles"]


def test_missing_mapping_rpc_denies_binding_before_profile_query(setup):
    _, _, factory = setup
    client = Mock()
    factory.side_effect = [client]
    client.rpc.return_value.execute.return_value.data = None
    with pytest.raises(binding.FirebaseProfileBindingError):
        binding.bind_firebase_profile("token")
    client.table.assert_not_called()
