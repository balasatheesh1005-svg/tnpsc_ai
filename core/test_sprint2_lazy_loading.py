"""
TNPSC Nova AI - Phase 7 Sprint 2 Smart Data Access & Lazy Loading Unit Test Suite
Verifies session engine caching, performance monitor hit/miss metrics,
smart cache invalidation, and zero regression across AI Engine outputs.
"""

import unittest
from unittest.mock import MagicMock, patch
import streamlit as st

from core.engine_cache import (
    ENGINE_CACHE_KEY_PREFIX,
    clear_engine_cache,
    get_cached_engine_result,
)
from core.performance import perf_monitor, reset_metrics
from core.user_context import UserContext
from core.learning_intelligence_ai import get_learning_intelligence
from core.study_planner_ai import get_personal_study_plan
from core.recommendation_ai import get_ai_recommendation
from core.exam_readiness_ai import get_exam_readiness
from core.mock_intelligence_ai import get_mock_intelligence
from core.predictive_performance_ai import get_predictive_performance
from core.adaptive_revision_ai import get_adaptive_final_revision
from core.exam_strategy_ai import get_exam_strategy


class TestSprint2LazyLoading(unittest.TestCase):

    def setUp(self):
        reset_metrics()
        # Ensure session state exists mock
        if not hasattr(st, "session_state"):
            st.session_state = {}
        clear_engine_cache("test_user")

    def tearDown(self):
        clear_engine_cache("test_user")

    def test_cache_hit_and_miss_recording(self):
        """Verify that get_cached_engine_result records miss on 1st call and hit on 2nd call."""
        call_count = 0

        def sample_compute():
            nonlocal call_count
            call_count += 1
            return {"status": "ok", "value": 42}

        # First call -> Miss
        res1 = get_cached_engine_result("Test Engine", "user1", sample_compute)
        self.assertEqual(res1["value"], 42)
        self.assertEqual(call_count, 1)

        c_sum = perf_monitor.get_cache_summary()
        self.assertIn("Test Engine", c_sum["miss_details"])

        # Second call -> Hit
        res2 = get_cached_engine_result("Test Engine", "user1", sample_compute)
        self.assertEqual(res2["value"], 42)
        self.assertEqual(call_count, 1)  # Compute NOT called again!

        c_sum2 = perf_monitor.get_cache_summary()
        self.assertIn("Test Engine", c_sum2["hit_details"])
        self.assertGreaterEqual(c_sum2["hit_ratio"], 50.0)

    def test_cache_invalidation(self):
        """Verify that clear_engine_cache removes cached engine results and UserContext."""
        compute_fn = lambda: {"data": "test_data"}

        get_cached_engine_result("Test Engine 2", "user2", compute_fn)
        key = f"{ENGINE_CACHE_KEY_PREFIX}Test Engine 2_user2"
        self.assertIn(key, st.session_state)

        # Clear cache
        clear_engine_cache("user2")
        self.assertNotIn(key, st.session_state)

    @patch("core.user_context.supabase")
    def test_ai_engines_reuse_cached_learning_intelligence(self, mock_supabase):
        """Verify AI engines execute without error and reuse cached engine outputs."""
        # Setup mock return data for UserContext load
        mock_supabase.table().select().eq().execute().data = []
        mock_supabase.table().select().eq().limit().execute().data = []

        ctx = UserContext(username="test_user")
        st.session_state["user_context"] = ctx

        # Execute Learning Intelligence once
        intel1 = get_learning_intelligence("test_user", context=ctx)
        self.assertIsInstance(intel1, dict)
        self.assertIn("root_cause", intel1)

        # Second call should hit cache
        intel2 = get_learning_intelligence("test_user", context=ctx)
        self.assertEqual(intel1, intel2)

        # Execute dependent engines
        rec = get_ai_recommendation("test_user", context=ctx)
        self.assertIn("recommendation", rec)

        readiness = get_exam_readiness("test_user", context=ctx)
        self.assertIn("overall_readiness_score", readiness)

        mock_intel = get_mock_intelligence("test_user", context=ctx)
        self.assertIn("overall_accuracy", mock_intel)

        predictive = get_predictive_performance("test_user", context=ctx)
        self.assertIn("prediction_confidence", predictive)

        adaptive = get_adaptive_final_revision("test_user", context=ctx)
        self.assertIn("revision_phase", adaptive)

        strategy = get_exam_strategy("test_user", context=ctx)
        self.assertIn("overall_strategy", strategy)

        # Cache Summary check
        c_sum = perf_monitor.get_cache_summary()
        self.assertGreater(c_sum["hits"], 0)


if __name__ == "__main__":
    unittest.main()
