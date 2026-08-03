"""
TNPSC Nova AI - Smart Data Access & Engine Caching Layer
Phase 7 Performance Engineering - Sprint 2

Caches AI Engine outputs in Streamlit session_state to prevent duplicate calculations
and unnecessary database queries across page renders and navigation.
Integrates directly with Developer Performance Monitor (Sprint 1.5).
"""

from typing import Any, Callable, Dict, Optional
import streamlit as st

from core.performance import record_cache_hit, record_cache_miss
from core.user_context import UserContext


ENGINE_CACHE_KEY_PREFIX = "_engine_cache_"


def get_cached_engine_result(
    engine_name: str,
    user: Optional[str],
    compute_fn: Callable[[], Any],
    force_refresh: bool = False,
) -> Any:
    """
    Retrieves cached AI engine result from session_state or computes and caches it.
    
    :param engine_name: Human-readable engine name (e.g. 'Learning Intelligence Engine')
    :param user: Identifier for the current user
    :param compute_fn: Zero-argument function that computes the engine result if cache misses
    :param force_refresh: If True, bypasses cache and recomputes engine result
    :return: Engine output data structure
    """
    user_str = str(user or "Guest")
    cache_key = f"{ENGINE_CACHE_KEY_PREFIX}{engine_name}_{user_str}"

    if hasattr(st, "session_state"):
        if not force_refresh and cache_key in st.session_state:
            record_cache_hit(engine_name)
            return st.session_state[cache_key]

        record_cache_miss(engine_name)

    # Compute result if miss or no session_state
    result = compute_fn()

    if hasattr(st, "session_state"):
        st.session_state[cache_key] = result

    return result


def clear_engine_cache(user: Optional[str] = None) -> None:
    """
    Smart Cache Invalidation: Invalidates all cached AI Engine outputs in session_state.
    Also invalidates the cached UserContext so fresh database values are retrieved.
    
    Call this function whenever user state changes:
    - User completes Daily Test
    - User completes PYQ
    - User studies Notes / practices
    - User completes Revision
    - XP / Weakness / Progress changes
    """
    if hasattr(st, "session_state"):
        keys_to_delete = [
            k for k in st.session_state.keys() if k.startswith(ENGINE_CACHE_KEY_PREFIX)
        ]
        for k in keys_to_delete:
            del st.session_state[k]

        if "user_context" in st.session_state:
            del st.session_state["user_context"]
        if "dashboard_stats_cache" in st.session_state:
            del st.session_state["dashboard_stats_cache"]

    if user:
        UserContext.get_or_create(user, force_refresh=True)
