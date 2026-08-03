import datetime
from dataclasses import dataclass, field
import logging
from typing import Any, Dict, List, Optional
import streamlit as st

from core.session import current_user_id, current_username
from core.supabase_client import supabase
from core.user_identity import resolve_user_id

logger = logging.getLogger(__name__)


def _parse_due_date(value):
    if value is None:
        return None
    if isinstance(value, datetime.date):
        return value
    try:
        return datetime.date.fromisoformat(str(value))
    except ValueError:
        try:
            return datetime.datetime.fromisoformat(str(value)).date()
        except Exception:
            return None


@dataclass
class UserContext:
    user_id: Optional[str] = None
    username: str = "Guest"
    profile: Dict[str, Any] = field(default_factory=dict)
    progress: List[Dict[str, Any]] = field(default_factory=list)
    weakness: Dict[str, int] = field(default_factory=dict)
    xp: Dict[str, Any] = field(default_factory=lambda: {"xp": 0, "level": 1})
    streak: int = 0
    revisions: List[Dict[str, Any]] = field(default_factory=list)
    revision_overview: Dict[str, Any] = field(default_factory=dict)
    mission: Dict[str, Any] = field(default_factory=dict)
    memory: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def load(cls, user_identifier: Optional[str] = None) -> "UserContext":
        """
        Single-pass data loader for user data context.
        Executes minimal Supabase calls and returns a populated UserContext object.
        """
        user_id = resolve_user_id(user_identifier)
        if not user_id:
            logger.warning(f"UserContext.load called with unresolved user_identifier='{user_identifier}'")
            return cls(username="Guest")

        display_name = current_username() or (
            str(user_identifier)
            if user_identifier and not (len(str(user_identifier)) == 36 and str(user_identifier).count("-") == 4)
            else "Guest"
        )

        ctx = cls(user_id=user_id, username=display_name)

        # 1. Fetch Profile
        try:
            res = supabase.table("profiles").select("*").eq("id", user_id).limit(1).execute()
            if res.data:
                ctx.profile = res.data[0]
        except Exception as e:
            logger.warning(f"UserContext: profiles fetch error: {e}")

        # 2. Fetch Progress
        try:
            res = supabase.table("users_progress").select("*").eq("user_id", user_id).execute()
            ctx.progress = res.data or []
        except Exception as e:
            logger.warning(f"UserContext: users_progress fetch error: {e}")

        # 3. Fetch Weakness
        try:
            res = supabase.table("users_weakness").select("*").eq("user_id", user_id).execute()
            weak_map = {}
            for row in res.data or []:
                key = f"{row.get('subject')}-{row.get('topic')}"
                weak_map[key] = int(row.get("weakness") or 0)
            ctx.weakness = weak_map
        except Exception as e:
            logger.warning(f"UserContext: users_weakness fetch error: {e}")

        # 4. Fetch XP
        try:
            res = supabase.table("user_xp").select("xp, level").eq("user_id", user_id).limit(1).execute()
            if res.data:
                ctx.xp = {"xp": int(res.data[0].get("xp", 0)), "level": int(res.data[0].get("level", 1))}
            else:
                ctx.xp = {"xp": 0, "level": 1}
        except Exception as e:
            logger.warning(f"UserContext: user_xp fetch error: {e}")

        # 5. Fetch Streak
        try:
            res = supabase.table("user_streaks").select("*").eq("user_id", user_id).limit(1).execute()
            if res.data:
                ctx.streak = int(res.data[0].get("streak") or 0)
        except Exception as e:
            logger.warning(f"UserContext: user_streaks fetch error: {e}")

        # 6. Fetch Revisions
        try:
            res = supabase.table("user_revisions").select("*").eq("user_id", user_id).execute()
            ctx.revisions = res.data or []

            # Build revision overview
            today = datetime.date.today()
            overview = {
                "total": len(ctx.revisions),
                "overdue": [],
                "due_today": [],
                "upcoming": [],
                "queue": [],
            }
            for row in ctx.revisions:
                # Support both next_revision (schema) and next_due (legacy)
                due_val = row.get("next_revision") or row.get("next_due")
                due_date = _parse_due_date(due_val)
                level_val = int(row.get("interval") or row.get("level") or 1)

                item = {
                    "subject": row.get("subject") or "Unknown",
                    "topic": row.get("topic") or "Unknown",
                    "level": level_val,
                    "next_due": due_date,
                    "next_revision": due_date,
                }
                overview["queue"].append(item)
                if due_date:
                    if due_date < today:
                        overview["overdue"].append(item)
                    elif due_date == today:
                        overview["due_today"].append(item)
                    else:
                        overview["upcoming"].append(item)

            ctx.revision_overview = overview
        except Exception as e:
            logger.warning(f"UserContext: user_revisions fetch error: {e}")

        # 7. Fetch Daily Mission
        try:
            today_str = datetime.date.today().isoformat()
            res = (
                supabase.table("daily_missions")
                .select("*")
                .eq("user_id", user_id)
                .limit(1)
                .execute()
            )
            if res.data:
                ctx.mission = res.data[0]
            else:
                ctx.mission = {
                    "user_id": user_id,
                    "username": display_name,
                    "date": today_str,
                    "daily_test_completed": False,
                    "revision_completed": False,
                    "pyq_solved": 0,
                }
        except Exception as e:
            logger.warning(f"UserContext: daily_missions fetch error: {e}")

        # 8. Fetch Mentor Memory
        try:
            res = supabase.table("mentor_memory").select("*").eq("user_id", user_id).limit(1).execute()
            if res.data:
                row = res.data[0]
                mem_data = row.get("memory_data") or row.get("summary") or {}
                if isinstance(mem_data, dict):
                    ctx.memory = mem_data
                else:
                    ctx.memory = {}
        except Exception as e:
            logger.warning(f"UserContext: mentor_memory fetch error: {e}")

        return ctx

    @classmethod
    def get_or_create(cls, user_identifier: Optional[str] = None, force_refresh: bool = False) -> "UserContext":
        """
        Retrieves existing UserContext from Streamlit session state or loads a fresh one.
        """
        user_id = resolve_user_id(user_identifier)
        if hasattr(st, "session_state"):
            cached_ctx = st.session_state.get("user_context")
            if not force_refresh and cached_ctx and isinstance(cached_ctx, cls):
                if user_id and cached_ctx.user_id == user_id:
                    return cached_ctx
                if not user_id and cached_ctx.username == (user_identifier or "Guest"):
                    return cached_ctx

        fresh_ctx = cls.load(user_identifier)
        if hasattr(st, "session_state"):
            st.session_state["user_context"] = fresh_ctx
        return fresh_ctx

    def invalidate(self):
        """Invalidate the session cached user context."""
        if hasattr(st, "session_state") and "user_context" in st.session_state:
            del st.session_state["user_context"]
