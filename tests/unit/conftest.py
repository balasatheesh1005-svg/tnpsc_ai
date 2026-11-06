"""Unit tests must never reach production services."""
import socket
import pytest


@pytest.fixture(autouse=True)
def block_network(monkeypatch):
    # Tests cannot use host proxies; constructors must work without proxy extras.
    for key in ("HTTP_PROXY", "HTTPS_PROXY", "ALL_PROXY", "http_proxy", "https_proxy", "all_proxy"):
        monkeypatch.delenv(key, raising=False)
    def denied(*args, **kwargs):
        raise RuntimeError('External services are disabled in unit tests; mock the service')
    monkeypatch.setattr(socket, 'getaddrinfo', denied)
    monkeypatch.setattr(socket.socket, 'connect', denied)
    monkeypatch.setattr(socket.socket, 'connect_ex', denied)
