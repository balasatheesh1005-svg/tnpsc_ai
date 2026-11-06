import time
import traceback
from types import SimpleNamespace

import streamlit as st
from supabase import ClientOptions, create_client

from core.staging_config import get_staging_config

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 0.35

_last_error = {"message": None, "type": None, "time": 0.0}


def _is_network_error(error):
    text = str(error).lower()
    network_markers = (
        "connection",
        "timeout",
        "timed out",
        "network",
        "dns",
        "name resolution",
        "temporary failure",
        "max retries",
        "remote end closed",
    )
    return any(marker in text for marker in network_markers)


def _record_error(error):
    error_type = "network" if _is_network_error(error) else "database"
    _last_error.update(
        {
            "message": str(error),
            "type": error_type,
            "time": time.time(),
        }
    )
    print(f"[Supabase {error_type} error] {error}")
    traceback.print_exc()


def get_recent_error_message(max_age_seconds=5):
    if not _last_error["message"]:
        return None
    if time.time() - _last_error["time"] > max_age_seconds:
        return None
    if _last_error["type"] == "network":
        return "Network issue. Please retry."
    return "Something went wrong. Please try again."


from core.performance import record_query


class _RetryQuery:
    def __init__(self, query, table_name: str = "unknown"):
        self._query = query
        self.table_name = table_name

    def __getattr__(self, name):
        attr = getattr(self._query, name)

        if name == "execute":

            def execute_with_retry(*args, **kwargs):
                last_error = None
                start_t = time.perf_counter()

                for attempt in range(MAX_RETRIES):
                    try:
                        res = attr(*args, **kwargs)
                        dur = time.perf_counter() - start_t
                        record_query(self.table_name, dur, success=True)
                        return res
                    except Exception as error:
                        last_error = error
                        if _is_network_error(error) and attempt < MAX_RETRIES - 1:
                            time.sleep(RETRY_DELAY_SECONDS)
                        else:
                            break

                dur = time.perf_counter() - start_t
                record_query(self.table_name, dur, success=False)
                _record_error(last_error)
                return SimpleNamespace(data=[], count=0, error=last_error)

            return execute_with_retry

        if not callable(attr):
            return attr

        def chained(*args, **kwargs):
            result = attr(*args, **kwargs)
            if result is self._query:
                return self
            return _RetryQuery(result, table_name=self.table_name)

        return chained


class _SafeSupabaseClient:
    def __init__(self, client):
        self._client = client

    def table(self, name):
        return _RetryQuery(self._client.table(name), table_name=name)

    def __getattr__(self, name):
        return getattr(self._client, name)


def get_supabase_client():
    # Never cache an authenticated SDK client across Streamlit sessions.
    config = get_staging_config()
    key = "_nova_supabase_client"
    if key not in st.session_state:
        st.session_state[key] = _SafeSupabaseClient(create_client(
            config.supabase_url, config.supabase_key,
            # Public ClientOptions is SyncClientOptions, including per-client memory storage.
            options=ClientOptions(auto_refresh_token=False, persist_session=False),
        ))
    return st.session_state[key]


class _SessionClientProxy:
    def __getattr__(self, name):
        # Introspection must not allocate an authenticated client as a side effect.
        if name.startswith("_"):
            raise AttributeError(name)
        return getattr(get_supabase_client(), name)


supabase = _SessionClientProxy()

