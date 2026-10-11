from unittest.mock import MagicMock, patch

FAKE_SESSION_STATE = {
    "auth_session": {"access_token": "fake-access-token", "refresh_token": "fake-refresh-token"},
    "auth_user": {"id": "00000000-0000-0000-0000-000000000001", "email": "test_p1@example.com"},
    "auth_profile": {
        "id": "00000000-0000-0000-0000-000000000001",
        "username": "test_p1_user",
        "full_name": "P1 Test User",
        "email": "test_p1@example.com",
        "xp": 100,
        "streak": 5,
        "level": 2,
    },
    "user_id": "00000000-0000-0000-0000-000000000001",
    "username": "test_p1_user",
    "email": "test_p1@example.com",
    "full_name": "P1 Test User",
    "authenticated": True,
    "selected_subject": "polity",
    "selected_topic_id": "polity_historical_background",
    "nav_view": "topic_hub",
    "score": 0,
    "correct_streak": 0,
    "wrong_count": 0,
    "level": 1,
    "answered": False,
}


def apply_fake_session_state(at=None):
    """Applies standard fake logged-in user state to Streamlit AppTest or st.session_state."""
    import streamlit as st

    for key, value in FAKE_SESSION_STATE.items():
        if at is not None:
            at.session_state[key] = value
        st.session_state[key] = value
    return at


def get_mock_dashboard_stats():
    return {
        "tests_attempted": 10,
        "accuracy": 85.0,
        "streak": 5,
        "rank": 1,
        "weak_subject": "Polity",
        "xp": 150,
        "level": 2,
        "level_progress": {"current_level": 2, "xp_in_level": 50, "xp_for_next": 100, "progress": 0.5},
    }


import copy
import datetime
import uuid
from types import SimpleNamespace
from unittest.mock import patch


class FakeDate(datetime.date):
    _current_today = datetime.date(2026, 10, 1)

    @classmethod
    def set_today(cls, d):
        cls._current_today = d

    @classmethod
    def today(cls):
        return cls._current_today or super().today()


class FakeSupabaseQuery:
    def __init__(self, store, table_name, stats):
        self.store = store
        self.table_name = table_name
        self.stats = stats
        self.filters = []
        self.limit_val = None
        self.operation = "select"
        self.payload = None

    def select(self, columns="*"):
        self.operation = "select"
        return self

    def eq(self, column, value):
        self.filters.append((column, value))
        return self

    def limit(self, count):
        self.limit_val = count
        return self

    def insert(self, data):
        self.operation = "insert"
        self.payload = data
        return self

    def update(self, data):
        self.operation = "update"
        self.payload = data
        return self

    def _matches_filters(self, row):
        for col, val in self.filters:
            if row.get(col) != val:
                return False
        return True

    def execute(self):
        table_rows = self.store.setdefault(self.table_name, [])

        if self.operation == "select":
            matching = [copy.deepcopy(r) for r in table_rows if self._matches_filters(r)]
            if self.limit_val is not None:
                matching = matching[: self.limit_val]
            return SimpleNamespace(data=matching, count=len(matching), error=None)

        elif self.operation == "insert":
            self.stats["writes"] += 1
            if isinstance(self.payload, dict):
                row = copy.deepcopy(self.payload)
                if "id" not in row:
                    row["id"] = str(uuid.uuid4())
                table_rows.append(row)
                return SimpleNamespace(data=[copy.deepcopy(row)], count=1, error=None)
            elif isinstance(self.payload, list):
                inserted = []
                for item in self.payload:
                    row = copy.deepcopy(item)
                    if "id" not in row:
                        row["id"] = str(uuid.uuid4())
                    table_rows.append(row)
                    inserted.append(row)
                return SimpleNamespace(data=[copy.deepcopy(r) for r in inserted], count=len(inserted), error=None)

        elif self.operation == "update":
            self.stats["writes"] += 1
            updated = []
            for row in table_rows:
                if self._matches_filters(row):
                    if isinstance(self.payload, dict):
                        row.update(copy.deepcopy(self.payload))
                    updated.append(copy.deepcopy(row))
            return SimpleNamespace(data=updated, count=len(updated), error=None)

        return SimpleNamespace(data=[], count=0, error=None)


class FakeSupabaseClient:
    def __init__(self):
        self.store = {}
        self.stats = {"network_calls": 0, "writes": 0, "rpc_calls": []}

    def table(self, table_name):
        return FakeSupabaseQuery(self.store, table_name, self.stats)

    def rpc(self, fn_name, params=None):
        self.stats["rpc_calls"].append((fn_name, params))

        class FakeRpcQuery:
            def __init__(self, client, fn):
                self.client = client
                self.fn = fn

            def execute(self):
                if self.fn == "get_global_leaderboard":
                    progress_rows = self.client.store.get("users_progress", [])
                    user_scores = {}
                    for row in progress_rows:
                        u = row.get("username")
                        if u:
                            try:
                                acc = float(row.get("accuracy", 0))
                                user_scores.setdefault(u, []).append(acc)
                            except (TypeError, ValueError):
                                pass
                    results = []
                    for u, scores in user_scores.items():
                        avg_acc = sum(scores) / len(scores)
                        results.append({"username": u, "accuracy": round(avg_acc, 2)})
                    results.sort(key=lambda x: x["accuracy"], reverse=True)
                    return SimpleNamespace(data=results[:10], count=len(results[:10]), error=None)
                return SimpleNamespace(data=[], count=0, error=None)

        return FakeRpcQuery(self, fn_name)

    def reset(self):
        self.store.clear()
        self.stats = {"network_calls": 0, "writes": 0, "rpc_calls": []}



