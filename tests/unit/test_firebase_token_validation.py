"""Real RSA/signature checks against synthetic certificates; no Google or Firebase calls."""
import base64
import json
import time
from types import SimpleNamespace
from unittest.mock import Mock

import pytest
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from google.auth import crypt, jwt

from core.firebase_token_validation import (
    CERTIFICATES_URL, FirebaseGoogleTokenValidator, FirebaseTokenValidationError,
)

PROJECT = 'nova-firebase-test'


@pytest.fixture(scope='module')
def keys():
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    private = key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
                               serialization.NoEncryption())
    public = key.public_key().public_bytes(serialization.Encoding.PEM,
                                          serialization.PublicFormat.SubjectPublicKeyInfo).decode()
    return crypt.RSASigner.from_string(private, key_id='synthetic-key'), public


@pytest.fixture
def claims():
    now = int(time.time())
    return {'iss': f'https://securetoken.google.com/{PROJECT}', 'aud': PROJECT,
            'sub': 'firebase-subject-A', 'iat': now - 1, 'exp': now + 3500,
            'auth_time': now - 2, 'email': 'synthetic@example.invalid',
            'email_verified': True, 'role': 'authenticated',
            'firebase': {'sign_in_provider': 'google.com'}}


def validator(keys, project=PROJECT):
    request = Mock(return_value=SimpleNamespace(status=200, data=json.dumps({'synthetic-key': keys[1]}).encode()))
    return FirebaseGoogleTokenValidator(project, certificate_request=request), request


def sign(keys, claims, header=None):
    return jwt.encode(keys[0], claims, header=header).decode()


def test_valid_google_token_uses_real_signature_and_pinned_public_certificates(keys, claims):
    verifier, request = validator(keys)
    token = sign(keys, claims)
    identity = verifier.validate(token)
    assert identity.identity_key == (claims['iss'], claims['sub'])
    assert identity.email == claims['email']
    assert token not in repr(identity) and claims['email'] not in repr(identity)
    request.assert_called_once_with(url=CERTIFICATES_URL, method='GET', timeout=5)


@pytest.mark.parametrize('changes', [
    {'aud': 'different-test-project'},
    {'aud': [PROJECT, 'other-project']},
    {'iss': 'https://accounts.google.com'},
    {'iss': 'https://securetoken.google.com/other-project'},
    {'sub': ''}, {'sub': 'x' * 129}, {'sub': 7},
    {'email_verified': False}, {'email_verified': 'true'},
    {'email': ''}, {'role': 'anon'}, {'role': 'service_role'},
    {'firebase': {'sign_in_provider': 'password'}},
    {'firebase': {'sign_in_provider': 'anonymous'}}, {'firebase': None},
    {'exp': 1}, {'exp': True}, {'iat': 9999999999},
    {'auth_time': 1}, {'auth_time': True}, {'user_id': 'subject-B'},
])
def test_rejects_invalid_signed_claims(keys, claims, changes):
    claims.update(changes)
    token = sign(keys, claims)
    with pytest.raises(FirebaseTokenValidationError) as error:
        validator(keys)[0].validate(token)
    assert token not in str(error.value)


def test_rejects_signature_tampering(keys, claims):
    parts = sign(keys, claims).split('.')
    claims['sub'] = 'attacker'
    parts[1] = base64.urlsafe_b64encode(json.dumps(claims).encode()).decode().rstrip('=')
    with pytest.raises(FirebaseTokenValidationError):
        validator(keys)[0].validate('.'.join(parts))


@pytest.mark.parametrize('header', [{'alg': 'none'}, {'alg': 'HS256'},
    {'jku': 'https://attacker.invalid'}, {'jwk': {}}, {'x5u': 'https://attacker.invalid'}])
def test_rejects_algorithm_confusion_and_untrusted_key_sources_before_network(keys, claims, header):
    token = sign(keys, claims, header)
    verifier, request = validator(keys)
    with pytest.raises(FirebaseTokenValidationError):
        verifier.validate(token)
    request.assert_not_called()


def test_certificate_failure_fails_closed_without_disclosing_token(keys, claims):
    request = Mock(side_effect=RuntimeError('private backend diagnostics'))
    token = sign(keys, claims)
    with pytest.raises(FirebaseTokenValidationError) as error:
        FirebaseGoogleTokenValidator(PROJECT, certificate_request=request).validate(token)
    assert 'diagnostics' not in str(error.value) and token not in str(error.value)


def test_project_contexts_and_subjects_are_isolated(keys, claims):
    first = validator(keys)[0].validate(sign(keys, claims))
    claims['sub'] = 'firebase-subject-B'
    second = validator(keys)[0].validate(sign(keys, claims))
    assert first.identity_key != second.identity_key
    with pytest.raises(FirebaseTokenValidationError):
        validator(keys, project='different-test-project')[0].validate(sign(keys, claims))


def test_emulator_authentication_is_never_accepted_in_hosted_staging(monkeypatch):
    monkeypatch.setenv('FIREBASE_AUTH_EMULATOR_HOST', 'localhost:9099')
    with pytest.raises(FirebaseTokenValidationError):
        FirebaseGoogleTokenValidator(PROJECT)


@pytest.mark.parametrize('token', ['', None, 'malformed', 'a' * 16385])
def test_malformed_tokens_fail_closed(token):
    with pytest.raises(FirebaseTokenValidationError):
        FirebaseGoogleTokenValidator(PROJECT).validate(token)
