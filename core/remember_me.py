"""Opaque browser handle; credentials remain in process memory, never in URLs/cookies.

Restarting the server invalidates remembered sessions. Multi-worker deployments need
an external session store before enabling cross-worker persistence.
"""
import hashlib
import secrets
import threading
import time
from datetime import datetime, timedelta

import streamlit as st

COOKIE = "nova_remember"
TTL = 7 * 24 * 60 * 60
_records = {}
_lock = threading.RLock()


def init_remember_me():
    import extra_streamlit_components as stx
    st.session_state["_remember_cookie_manager"] = stx.CookieManager(key="nova_cookies")


def _manager():
    return st.session_state.get("_remember_cookie_manager")


def _digest(handle):
    return hashlib.sha256(handle.encode()).hexdigest()


def _prune():
    now = time.time()
    for key, record in list(_records.items()):
        if record[0] <= now:
            del _records[key]


def recalled_tokens():
    manager = _manager()
    if manager is None:
        return {}
    handle = manager.get(COOKIE)
    if not isinstance(handle, str) or len(handle) != 64:
        return {}
    with _lock:
        _prune()
        record = _records.get(_digest(handle))
        if not record:
            return {}
        st.session_state["_remember_handle"] = handle
        st.session_state["_remember_enabled"] = True
        st.session_state["remember_me"] = True
        return dict(record[1])


def remember_session(session, enabled):
    manager = _manager()
    if manager is None or not enabled:
        forget_session()
        return
    def value(key):
        return session.get(key) if isinstance(session, dict) else getattr(session, key, None)
    tokens = {key: value(key) for key in ("access_token", "refresh_token")}
    if not all(tokens.values()):
        return
    st.session_state["_remember_enabled"] = True
    handle = st.session_state.get("_remember_handle")
    with _lock:
        _prune()
        if not handle or _digest(handle) not in _records:
            handle = secrets.token_hex(32)
            st.session_state["_remember_handle"] = handle
            expires = time.time() + TTL
            manager.set(COOKIE, handle, expires_at=datetime.now() + timedelta(seconds=TTL),
                        secure=True, same_site="strict", key="nova_cookie_set")
        else:
            expires = _records[_digest(handle)][0]
        _records[_digest(handle)] = (expires, tokens)


def forget_session():
    st.session_state.pop("_remember_enabled", None)
    manager = _manager()
    handle = st.session_state.pop("_remember_handle", None)
    if not handle and manager is not None:
        handle = manager.get(COOKIE)
    if isinstance(handle, str):
        with _lock:
            _records.pop(_digest(handle), None)
    if manager is not None and manager.get(COOKIE):
        manager.delete(COOKIE, key="nova_cookie_delete")
