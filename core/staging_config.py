"""Fail-closed configuration for the isolated staging branch only."""
import base64
import hashlib
import json
import re
from dataclasses import dataclass, field
from urllib.parse import urlsplit

import streamlit as st

# Fingerprint of the production project identifier, never a usable credential.
BLOCKED_PROJECT_HASHES = frozenset({"6d253d6c56925f75acaedb34f8afe3423651e29130b536fa12003a64e4938661"})


class StagingConfigurationError(ValueError):
    pass


@dataclass(frozen=True)
class StagingConfig:
    supabase_url: str
    supabase_key: str = field(repr=False)
    app_url: str
    project_ref: str


def get_staging_config():
    try:
        settings = st.secrets["staging"]
        database = st.secrets["supabase"]
        mode = settings["mode"]
        expected_ref = settings["expected_project_ref"]
        app_url = settings["app_url"]
        url = database["url"]
        key = database["publishable_key"]
    except Exception:
        raise StagingConfigurationError("Staging Secrets configuration is missing or incomplete.") from None
    if mode != "staging" or not all(isinstance(value, str) and value == value.strip()
                                    for value in (expected_ref, app_url, url, key)):
        raise StagingConfigurationError("Invalid staging configuration.")
    if not re.fullmatch(r"[a-z0-9]{20}", expected_ref):
        raise StagingConfigurationError("Invalid test project identifier.")
    if hashlib.sha256(expected_ref.encode()).hexdigest() in BLOCKED_PROJECT_HASHES:
        raise StagingConfigurationError("Production projects are forbidden in staging.")
    if url != f"https://{expected_ref}.supabase.co":
        raise StagingConfigurationError("Supabase URL does not match the pinned test project.")
    # A root HTTPS Community Cloud URL only; never accept a callback from query input.
    if not re.fullmatch(r"https://[a-z0-9]+(?:-[a-z0-9]+)*\.streamlit\.app", app_url):
        raise StagingConfigurationError("An exact HTTPS Test App root URL is required.")
    if "test" not in urlsplit(app_url).hostname.split(".")[0].split("-"):
        raise StagingConfigurationError("The isolated app hostname must include a test label.")
    if key.startswith("sb_publishable_"):
        if not re.fullmatch(r"sb_publishable_[A-Za-z0-9_-]{16,}", key):
            raise StagingConfigurationError("Invalid publishable key format.")
    else:
        try:
            parts = key.split(".")
            if len(parts) != 3:
                raise ValueError()
            claims = json.loads(base64.urlsafe_b64decode(parts[1] + "=" * (-len(parts[1]) % 4)))
            if claims.get("role") != "anon" or claims.get("ref") != expected_ref:
                raise ValueError()
        except Exception:
            raise StagingConfigurationError("Only a test-project publishable or anon key is allowed.") from None
    # This only validates configuration shape. Supabase still validates key authenticity.
    return StagingConfig(url, key, app_url, expected_ref)
