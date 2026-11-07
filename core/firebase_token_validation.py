"""Staging foundation only: cryptographic validation, not an app login/session grant.

Not wired into Login. Trusted Supabase third-party auth and UUID mapping must be
configured before a validated Firebase identity can access application data.
"""
import os
import re
import time
from dataclasses import dataclass, field

from google.auth import jwt
from google.auth.transport.requests import Request
from google.oauth2 import id_token

CERTIFICATES_URL = 'https://www.googleapis.com/robot/v1/metadata/x509/securetoken@system.gserviceaccount.com'


class FirebaseTokenValidationError(ValueError):
    """A safe error that never includes the token or provider response."""


@dataclass(frozen=True)
class ValidatedFirebaseIdentity:
    issuer: str
    subject: str = field(repr=False)
    email: str = field(repr=False)
    expires_at: int
    authenticated_at: int

    @property
    def identity_key(self):
        # Namespaced identity; never reinterpret a Firebase subject as an app UUID.
        return self.issuer, self.subject


class _CertificateRequest:
    def __init__(self, request=None):
        self.request = request if request is not None else Request()

    def __call__(self, url, method='GET', **kwargs):
        if url != CERTIFICATES_URL or method != 'GET':
            raise FirebaseTokenValidationError('Unexpected certificate source.')
        return self.request(url=url, method='GET', timeout=5)


class FirebaseGoogleTokenValidator:
    """Verify signed claims for one pinned Test Firebase project.

    This does not check online revocation/disabled-user status, set custom claims,
    create/link profiles, install database trust or establish a Streamlit session.
    """
    def __init__(self, project_id, certificate_request=None, max_auth_age_seconds=300):
        if not isinstance(project_id, str) or not re.fullmatch(r'[a-z][a-z0-9-]{4,28}[a-z0-9]', project_id):
            raise FirebaseTokenValidationError('A pinned Firebase test project ID is required.')
        if os.environ.get('FIREBASE_AUTH_EMULATOR_HOST'):
            raise FirebaseTokenValidationError('Emulator authentication is forbidden in hosted staging.')
        if type(max_auth_age_seconds) is not int or not 1 <= max_auth_age_seconds <= 3600:
            raise FirebaseTokenValidationError('Invalid recent-authentication window.')
        self.project_id = project_id
        self.issuer = f'https://securetoken.google.com/{project_id}'
        self.request = _CertificateRequest(certificate_request)
        self.max_auth_age_seconds = max_auth_age_seconds

    def validate(self, token):
        try:
            if not isinstance(token, str) or len(token) > 16384 or token.count('.') != 2:
                raise ValueError()
            header = jwt.decode_header(token)
            if (header.get('alg') != 'RS256' or not isinstance(header.get('kid'), str)
                    or not re.fullmatch(r'[A-Za-z0-9_-]{1,128}', header['kid'])
                    or any(key in header for key in ('jku', 'jwk', 'x5u'))):
                raise ValueError()
            # Real Google library verifies signature, audience, iat and exp.
            claims = id_token.verify_firebase_token(
                token, self.request, audience=self.project_id, clock_skew_in_seconds=0)
            now = int(time.time())
            subject = claims.get('sub')
            email = claims.get('email')
            if claims.get('iss') != self.issuer or claims.get('aud') != self.project_id:
                raise ValueError()
            if not isinstance(subject, str) or not 1 <= len(subject) <= 128:
                raise ValueError()
            if 'user_id' in claims and claims['user_id'] != subject:
                raise ValueError()
            if (claims.get('email_verified') is not True or not isinstance(email, str)
                    or not email or '@' not in email or len(email) > 320):
                raise ValueError()
            if claims.get('role') != 'authenticated':
                raise ValueError()
            if claims.get('firebase', {}).get('sign_in_provider') != 'google.com':
                raise ValueError()
            if any(type(claims.get(key)) is not int for key in ('iat', 'exp', 'auth_time')):
                raise ValueError()
            if not (0 < claims['auth_time'] <= claims['iat'] <= now < claims['exp']):
                raise ValueError()
            if now - claims['auth_time'] > self.max_auth_age_seconds:
                raise ValueError()
            return ValidatedFirebaseIdentity(
                self.issuer, subject, email, claims['exp'], claims['auth_time'])
        except Exception:
            raise FirebaseTokenValidationError('Firebase Google token validation failed.') from None
