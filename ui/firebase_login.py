"""Optional Google Login UI for the feature preview."""
from pathlib import Path
import re

import streamlit as st
import streamlit.components.v1 as components

from core.firebase_session import CHALLENGE_KEY, accept_google_login, login_challenge
from core.firebase_supabase import FIREBASE_PROJECT, SUPABASE_PROJECT
from core.staging_config import get_staging_config

_google = components.declare_component("nova_google_login", path=str(Path(__file__).with_name("firebase_google")))
LIVE_STAGING_URL = "https://tnpsc-nova-ai-p0-test.streamlit.app"


def render_firebase_login():
    try:
        settings = st.secrets["firebase_google"]
        if settings.get("enabled") is not True:
            return
        staging = get_staging_config()
        if staging.project_ref != SUPABASE_PROJECT or staging.app_url == LIVE_STAGING_URL:
            raise ValueError()
        api_key = settings["web_api_key"]
        app_id = settings["web_app_id"]
        if not re.fullmatch(r"AIza[A-Za-z0-9_-]{35}", api_key) or not re.fullmatch(
            r"1:[0-9]+:web:[a-f0-9]+", app_id
        ):
            raise ValueError()
    except (KeyError, FileNotFoundError):
        return
    except Exception:
        st.error("Google உள்நுழைவு அமைப்புகளைச் சரிபார்க்கவும்.")
        return

    state = st.session_state
    if state.pop("_nova_firebase_login_failed", False):
        st.error("Google உள்நுழைவு முடியவில்லை. சரிபார்க்கப்பட்ட சோதனைக் கணக்கைப் பயன்படுத்தவும்.")
    nonce = login_challenge(state)
    payload = _google(
        config={"projectId": FIREBASE_PROJECT, "authDomain": f"{FIREBASE_PROJECT}.firebaseapp.com",
                "apiKey": api_key, "appId": app_id},
        challenge=nonce,
        key=f"nova_google_{nonce}",
        default=None,
    )
    if payload is None:
        return
    try:
        accepted = accept_google_login(state, payload)
    except Exception:
        accepted = False
    if not accepted:
        state.pop(CHALLENGE_KEY, None)
        state["_nova_firebase_login_failed"] = True
    st.rerun()
