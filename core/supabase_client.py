import time
import traceback
from types import SimpleNamespace

from supabase import create_client

SUPABASE_URL = "https://bexgmzfoxfpfysgpzbzc.supabase.co/"

SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJleGdtemZveGZwZnlzZ3B6YnpjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzk3MTA3MzUsImV4cCI6MjA5NTI4NjczNX0.-JFxsi353miLLteYNN8-oFjOQRoWnz2WOXfTlXR42zA"

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


supabase = _SafeSupabaseClient(create_client(SUPABASE_URL, SUPABASE_KEY))

