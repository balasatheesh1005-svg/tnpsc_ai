import unittest
from unittest.mock import patch, MagicMock
from core.coach_maturity_ai import (
    get_coach_maturity,
    has_subject_evidence,
    get_subject_evidence,
    has_topic_evidence,
    normalize_subject_key,
)
from core.exam_readiness_ai import get_exam_readiness
from core.revision_engine import get_intelligent_revision_plan, _analyze_5_level_target
from core.predictive_performance_ai import get_predictive_performance
from core.adaptive_revision_ai import get_adaptive_final_revision
from core.exam_strategy_ai import get_exam_strategy


# ==============================================================================
# FIXTURES
# ==============================================================================

CASE_A_PROGRESS = []
CASE_A_WEAKNESS = {}
CASE_A_REVISIONS = {"total": 0, "due_today": [], "overdue": [], "progress": {"percentage": 0, "completed": 0}}

CASE_B_PROGRESS = [
    {
        "subject": "history",
        "topic": "indus_valley_civilization",
        "accuracy": 80.0,
        "score": 8,
        "total": 10,
    },
    {
        "subject": "history",
        "topic": "indus_valley_civilization",
        "accuracy": 80.0,
        "score": 8,
        "total": 10,
    },
]
CASE_B_WEAKNESS = {}
CASE_B_REVISIONS = {"total": 0, "due_today": [], "overdue": [], "progress": {"percentage": 0, "completed": 0}}

CASE_C_PROGRESS = [
    {"subject": "history", "topic": "indus_valley_civilization", "accuracy": 80.0},
    {"subject": "polity", "topic": "preamble", "accuracy": 70.0},
    {"subject": "geography", "topic": "rivers_of_india", "accuracy": 60.0},
]
CASE_C_WEAKNESS = {"geography-rivers_of_india": 2}
CASE_C_REVISIONS = {"total": 1, "due_today": [], "overdue": [], "progress": {"percentage": 100, "completed": 1}}

CASE_D_PROGRESS = []
for i in range(4):
    CASE_D_PROGRESS.append({"subject": "history", "topic": f"topic_{i}", "accuracy": 85.0})
    CASE_D_PROGRESS.append({"subject": "polity", "topic": f"topic_{i}", "accuracy": 78.0})
    CASE_D_PROGRESS.append({"subject": "geography", "topic": f"topic_{i}", "accuracy": 82.0})
    CASE_D_PROGRESS.append({"subject": "economy", "topic": f"topic_{i}", "accuracy": 74.0})
CASE_D_PROGRESS.append({"subject": "grand_test", "topic": "grand_mock_1", "accuracy": 82.0})
CASE_D_WEAKNESS = {"economy-fiscal_policy": 3}
CASE_D_REVISIONS = {"total": 5, "due_today": [{"subject": "polity", "topic": "preamble", "level": 2}], "overdue": [], "progress": {"percentage": 85, "completed": 4}}


# ==============================================================================
# PHASE 11 & 12: UNIT TESTS
# ==============================================================================

class TestIntelligenceTruthFoundation(unittest.TestCase):

    # --------------------------------------------------------------------------
    # CASE A: ZERO DATA USER
    # --------------------------------------------------------------------------
    @patch("core.coach_maturity_ai.get_progress", return_value=CASE_A_PROGRESS)
    @patch("core.coach_maturity_ai.get_weakness", return_value=CASE_A_WEAKNESS)
    @patch("core.coach_maturity_ai.get_streak", return_value=0)
    @patch("core.coach_maturity_ai.get_revision_overview", return_value=CASE_A_REVISIONS)
    def test_case_a_coach_maturity(self, _rev, _strk, _weak, _prog):
        maturity = get_coach_maturity(user="test_user_a")
        self.assertEqual(maturity["tier"], "TIER_0_NO_DATA")
        self.assertEqual(maturity["state"], "NO_DATA")
        self.assertEqual(maturity["attempt_count"], 0)
        self.assertEqual(maturity["observed_subjects"], [])
        self.assertFalse(maturity["readiness_eligible"])
        self.assertFalse(maturity["prediction_eligible"])
        self.assertFalse(maturity["mock_eligible"])

    @patch("core.exam_readiness_ai.get_progress", return_value=CASE_A_PROGRESS)
    @patch("core.exam_readiness_ai.get_weakness", return_value=CASE_A_WEAKNESS)
    @patch("core.exam_readiness_ai.get_streak", return_value=0)
    @patch("core.exam_readiness_ai.get_revision_analytics_v2", return_value=CASE_A_REVISIONS)
    def test_case_a_exam_readiness(self, _rev, _strk, _weak, _prog):
        readiness = get_exam_readiness(user="test_user_a", force_refresh=True)
        self.assertIsNone(readiness["overall_readiness"])
        self.assertFalse(readiness["is_eligible"])
        self.assertIn(readiness["level"], ["Not assessed", "No Test History"])
        for s in readiness["subjects"]:
            self.assertIsNone(s["score"])
            self.assertEqual(s["status"], "Not assessed")

    @patch("core.predictive_performance_ai.get_progress", return_value=CASE_A_PROGRESS)
    @patch("core.predictive_performance_ai.get_weakness", return_value=CASE_A_WEAKNESS)
    @patch("core.predictive_performance_ai.get_streak", return_value=0)
    @patch("core.predictive_performance_ai.get_revision_analytics_v2", return_value=CASE_A_REVISIONS)
    def test_case_a_predictive_performance(self, _rev, _strk, _weak, _prog):
        pred = get_predictive_performance(user="test_user_a", force_refresh=True)
        self.assertFalse(pred["is_eligible"])
        self.assertNotEqual(pred["confidence_reason"], "")
        self.assertEqual(pred["estimated_readiness"], "Unavailable")
        self.assertEqual(pred["estimated_mock_accuracy"], "Unavailable")

    @patch("core.revision_engine.get_progress", return_value=CASE_A_PROGRESS)
    @patch("core.revision_engine.get_weakness", return_value=CASE_A_WEAKNESS)
    @patch("core.revision_engine.get_revision_overview", return_value=CASE_A_REVISIONS)
    def test_case_a_smart_revision(self, _rev, _weak, _prog):
        plan = get_intelligent_revision_plan(user="test_user_a")
        self.assertIsNone(plan["accuracy"])
        self.assertEqual(plan["status"], "Coverage Recommendation")

    @patch("core.exam_strategy_ai.get_progress", return_value=CASE_A_PROGRESS)
    @patch("core.exam_strategy_ai.get_weakness", return_value=CASE_A_WEAKNESS)
    @patch("core.exam_strategy_ai.get_streak", return_value=0)
    def test_case_a_exam_strategy(self, _strk, _weak, _prog):
        strat = get_exam_strategy(user="test_user_a", force_refresh=True)
        self.assertFalse(strat["is_personalized"])
        self.assertEqual(strat["strategy_label"], "GENERAL TNPSC STRATEGY")

    # --------------------------------------------------------------------------
    # CASE B: CURRENT EARLY USER (History Indus Valley, 2 tests, 80% acc, 0 mocks)
    # --------------------------------------------------------------------------
    @patch("core.coach_maturity_ai.get_progress", return_value=CASE_B_PROGRESS)
    @patch("core.coach_maturity_ai.get_weakness", return_value=CASE_B_WEAKNESS)
    @patch("core.coach_maturity_ai.get_streak", return_value=0)
    @patch("core.coach_maturity_ai.get_revision_overview", return_value=CASE_B_REVISIONS)
    def test_case_b_coach_maturity(self, _rev, _strk, _weak, _prog):
        maturity = get_coach_maturity(user="test_user_b")
        self.assertEqual(maturity["tier"], "TIER_1_EARLY_SIGNAL")
        self.assertEqual(maturity["state"], "EARLY_INSIGHTS")
        self.assertEqual(maturity["attempt_count"], 2)
        self.assertEqual(maturity["observed_subjects"], ["History"])
        self.assertEqual(maturity["avg_accuracy"], 80.0)
        self.assertEqual(maturity["strong_subject"], "History")
        self.assertEqual(maturity["mock_count"], 0)
        self.assertFalse(maturity["readiness_eligible"])
        self.assertFalse(maturity["prediction_eligible"])
        self.assertFalse(maturity["mock_eligible"])

    @patch("core.exam_readiness_ai.get_progress", return_value=CASE_B_PROGRESS)
    @patch("core.exam_readiness_ai.get_weakness", return_value=CASE_B_WEAKNESS)
    @patch("core.exam_readiness_ai.get_streak", return_value=0)
    @patch("core.exam_readiness_ai.get_revision_analytics_v2", return_value=CASE_B_REVISIONS)
    def test_case_b_exam_readiness(self, _rev, _strk, _weak, _prog):
        readiness = get_exam_readiness(user="test_user_b", force_refresh=True)
        self.assertFalse(readiness["is_eligible"])
        self.assertIsNone(readiness["overall_readiness"])
        self.assertEqual(readiness["level"], "Early Assessment")

        subj_map = {s["subject"]: s for s in readiness["subjects"]}
        self.assertEqual(subj_map["History"]["score"], 80)
        self.assertEqual(subj_map["History"]["status"], "Assessed")

        # Unassessed subjects must have score=None
        for unassessed in ["Polity", "Geography", "Economy", "Science", "Current Affairs"]:
            self.assertIsNone(subj_map[unassessed]["score"], f"{unassessed} should not have synthetic score")
            self.assertEqual(subj_map[unassessed]["status"], "Not assessed")

    @patch("core.revision_engine.get_progress", return_value=CASE_B_PROGRESS)
    @patch("core.revision_engine.get_weakness", return_value=CASE_B_WEAKNESS)
    @patch("core.revision_engine.get_revision_overview", return_value=CASE_B_REVISIONS)
    def test_case_b_smart_revision(self, _rev, _weak, _prog):
        plan = get_intelligent_revision_plan(user="test_user_b")
        # History Indus Valley is observed, so it's prioritized
        self.assertEqual(plan["raw_subject"], "history")
        self.assertIn("indus", plan["raw_topic"])
        self.assertEqual(plan["accuracy"], 80.0)  # Real observed accuracy, not 55%

    @patch("core.predictive_performance_ai.get_progress", return_value=CASE_B_PROGRESS)
    @patch("core.predictive_performance_ai.get_weakness", return_value=CASE_B_WEAKNESS)
    @patch("core.predictive_performance_ai.get_streak", return_value=0)
    @patch("core.predictive_performance_ai.get_revision_analytics_v2", return_value=CASE_B_REVISIONS)
    def test_case_b_predictive_performance(self, _rev, _strk, _weak, _prog):
        pred = get_predictive_performance(user="test_user_b", force_refresh=True)
        self.assertFalse(pred["is_eligible"])
        self.assertIsNone(pred["current_mock_accuracy"])
        self.assertEqual(pred["estimated_mock_accuracy"], "Need Mock Data")
        self.assertEqual(pred["mock_accuracy_trend"], "Not assessed")
        self.assertEqual(pred["estimated_readiness"], "More practice data required")

    @patch("core.adaptive_revision_ai.get_progress", return_value=CASE_B_PROGRESS)
    @patch("core.adaptive_revision_ai.get_weakness", return_value=CASE_B_WEAKNESS)
    @patch("core.adaptive_revision_ai.get_streak", return_value=0)
    @patch("core.adaptive_revision_ai.get_revision_analytics_v2", return_value=CASE_B_REVISIONS)
    def test_case_b_adaptive_revision(self, _rev, _strk, _weak, _prog):
        adaptive = get_adaptive_final_revision(user="test_user_b", force_refresh=True)
        # History is genuine observed subject
        self.assertIn("History", adaptive["priority_subjects"])
        # Unobserved subjects must not be flagged as low readiness risks
        for r in adaptive["risk_analysis"]:
            self.assertNotIn("Low Polity readiness", r)
            self.assertNotIn("Low Geography readiness", r)
            self.assertNotIn("Low Economy readiness", r)
            self.assertNotIn("Hard topic repository completion at 65%", r)
            self.assertNotIn("Revision coverage at 70%", r)
        self.assertIsNone(adaptive["completion_percentage"])  # Not synthetic 95%

    @patch("core.exam_strategy_ai.get_progress", return_value=CASE_B_PROGRESS)
    @patch("core.exam_strategy_ai.get_weakness", return_value=CASE_B_WEAKNESS)
    @patch("core.exam_strategy_ai.get_streak", return_value=0)
    def test_case_b_exam_strategy(self, _strk, _weak, _prog):
        strat = get_exam_strategy(user="test_user_b", force_refresh=True)
        self.assertFalse(strat["is_personalized"])
        self.assertEqual(strat["strategy_label"], "GENERAL TNPSC STRATEGY")
        self.assertNotIn("Strength-First", strat["overall_strategy"])

    # --------------------------------------------------------------------------
    # PHASE 12: SYNTHETIC VALUE GUARDS FOR CASE B
    # --------------------------------------------------------------------------
    @patch("core.exam_readiness_ai.get_progress", return_value=CASE_B_PROGRESS)
    @patch("core.exam_readiness_ai.get_weakness", return_value=CASE_B_WEAKNESS)
    @patch("core.exam_readiness_ai.get_streak", return_value=0)
    @patch("core.exam_readiness_ai.get_revision_analytics_v2", return_value=CASE_B_REVISIONS)
    @patch("core.predictive_performance_ai.get_progress", return_value=CASE_B_PROGRESS)
    @patch("core.predictive_performance_ai.get_weakness", return_value=CASE_B_WEAKNESS)
    @patch("core.predictive_performance_ai.get_streak", return_value=0)
    @patch("core.predictive_performance_ai.get_revision_analytics_v2", return_value=CASE_B_REVISIONS)
    @patch("core.adaptive_revision_ai.get_progress", return_value=CASE_B_PROGRESS)
    @patch("core.adaptive_revision_ai.get_weakness", return_value=CASE_B_WEAKNESS)
    @patch("core.adaptive_revision_ai.get_streak", return_value=0)
    @patch("core.adaptive_revision_ai.get_revision_analytics_v2", return_value=CASE_B_REVISIONS)
    def test_synthetic_value_guards(self, *mocks):
        readiness = get_exam_readiness(user="test_user_b", force_refresh=True)
        pred = get_predictive_performance(user="test_user_b", force_refresh=True)
        adaptive = get_adaptive_final_revision(user="test_user_b", force_refresh=True)

        # 1. Unassessed subject scores must NOT be 73, 76, 79, 85
        unassessed_scores = [s["score"] for s in readiness["subjects"] if s["subject"] != "History"]
        for score in unassessed_scores:
            self.assertNotIn(score, [73, 76, 79, 85, 55, 65], f"Found synthetic subject score: {score}")

        # 2. Mock prediction must not be 10–12%
        self.assertNotEqual(pred["estimated_mock_accuracy"], "10–12%")
        self.assertNotEqual(pred["estimated_revision_health"], "10–12%")

        # 3. Adaptive completion must not be 95%
        self.assertNotEqual(adaptive["completion_percentage"], 95)

    # --------------------------------------------------------------------------
    # CASE C: MULTI-SUBJECT DEVELOPING USER (3 subjects, 0 mocks)
    # --------------------------------------------------------------------------
    @patch("core.coach_maturity_ai.get_progress", return_value=CASE_C_PROGRESS)
    @patch("core.coach_maturity_ai.get_weakness", return_value=CASE_C_WEAKNESS)
    @patch("core.coach_maturity_ai.get_streak", return_value=2)
    @patch("core.coach_maturity_ai.get_revision_overview", return_value=CASE_C_REVISIONS)
    def test_case_c_developing_user(self, _rev, _strk, _weak, _prog):
        maturity = get_coach_maturity(user="test_user_c")
        self.assertEqual(maturity["attempt_count"], 3)
        self.assertEqual(len(maturity["observed_subjects"]), 3)
        self.assertEqual(maturity["state"], "EARLY_INSIGHTS")

    @patch("core.exam_readiness_ai.get_progress", return_value=CASE_C_PROGRESS)
    @patch("core.exam_readiness_ai.get_weakness", return_value=CASE_C_WEAKNESS)
    @patch("core.exam_readiness_ai.get_streak", return_value=2)
    @patch("core.exam_readiness_ai.get_revision_analytics_v2", return_value=CASE_C_REVISIONS)
    def test_case_c_readiness_subjects(self, _rev, _strk, _weak, _prog):
        readiness = get_exam_readiness(user="test_user_c", force_refresh=True)
        subj_map = {s["subject"]: s for s in readiness["subjects"]}
        self.assertEqual(subj_map["History"]["score"], 80)
        self.assertEqual(subj_map["Polity"]["score"], 70)
        self.assertEqual(subj_map["Geography"]["score"], 60)
        # Unobserved subjects remain Not assessed
        self.assertIsNone(subj_map["Economy"]["score"])
        self.assertIsNone(subj_map["Science"]["score"])
        self.assertIsNone(subj_map["Current Affairs"]["score"])

    # --------------------------------------------------------------------------
    # CASE D: MATURE USER (17 tests, 4+ subjects, mocks, revisions)
    # --------------------------------------------------------------------------
    @patch("core.coach_maturity_ai.get_progress", return_value=CASE_D_PROGRESS)
    @patch("core.coach_maturity_ai.get_weakness", return_value=CASE_D_WEAKNESS)
    @patch("core.coach_maturity_ai.get_streak", return_value=5)
    @patch("core.coach_maturity_ai.get_revision_overview", return_value=CASE_D_REVISIONS)
    def test_case_d_mature_user(self, _rev, _strk, _weak, _prog):
        maturity = get_coach_maturity(user="test_user_d")
        self.assertEqual(maturity["tier"], "TIER_3_RELIABLE")
        self.assertEqual(maturity["state"], "PERSONALIZED_COACH")
        self.assertTrue(maturity["readiness_eligible"])
        self.assertTrue(maturity["prediction_eligible"])
        self.assertTrue(maturity["mock_eligible"])

    @patch("core.exam_readiness_ai.get_progress", return_value=CASE_D_PROGRESS)
    @patch("core.exam_readiness_ai.get_weakness", return_value=CASE_D_WEAKNESS)
    @patch("core.exam_readiness_ai.get_streak", return_value=5)
    @patch("core.exam_readiness_ai.get_revision_analytics_v2", return_value=CASE_D_REVISIONS)
    def test_case_d_mature_readiness(self, _rev, _strk, _weak, _prog):
        readiness = get_exam_readiness(user="test_user_d", force_refresh=True)
        self.assertTrue(readiness["is_eligible"])
        self.assertIsNotNone(readiness["overall_readiness"])
        self.assertGreater(readiness["overall_readiness"], 50)

    @patch("core.predictive_performance_ai.get_exam_readiness", return_value={"overall_score": 82, "overall_readiness_score": 82, "is_eligible": True, "readiness_dimensions": {"repository_completion": 80}})
    @patch("core.predictive_performance_ai.get_mock_intelligence", return_value={"overall_accuracy": 82})
    @patch("core.predictive_performance_ai.get_progress", return_value=CASE_D_PROGRESS)
    @patch("core.predictive_performance_ai.get_weakness", return_value=CASE_D_WEAKNESS)
    @patch("core.predictive_performance_ai.get_streak", return_value=5)
    @patch("core.predictive_performance_ai.get_revision_analytics_v2", return_value=CASE_D_REVISIONS)
    def test_case_d_mature_predictive(self, _rev, _strk, _weak, _prog, _mock, _read):
        pred = get_predictive_performance(user="test_user_d", force_refresh=True)
        self.assertTrue(pred["is_eligible"])
        self.assertGreaterEqual(pred["prediction_confidence"], 70)
        self.assertIn("–", pred["estimated_readiness"])
        self.assertIn("–", pred["estimated_mock_accuracy"])

    @patch("core.exam_strategy_ai.get_progress", return_value=CASE_D_PROGRESS)
    @patch("core.exam_strategy_ai.get_weakness", return_value=CASE_D_WEAKNESS)
    @patch("core.exam_strategy_ai.get_streak", return_value=5)
    def test_case_d_mature_strategy(self, _strk, _weak, _prog):
        strat = get_exam_strategy(user="test_user_d", force_refresh=True)
        self.assertTrue(strat["is_personalized"])
        self.assertEqual(strat["strategy_label"], "PERSONALIZED EXAM STRATEGY")

    # --------------------------------------------------------------------------
    # PHASE 13: CROSS-ENGINE CONSISTENCY TEST (CASE B)
    # --------------------------------------------------------------------------
    @patch("core.coach_maturity_ai.get_progress", return_value=CASE_B_PROGRESS)
    @patch("core.coach_maturity_ai.get_weakness", return_value=CASE_B_WEAKNESS)
    @patch("core.coach_maturity_ai.get_streak", return_value=0)
    @patch("core.coach_maturity_ai.get_revision_overview", return_value=CASE_B_REVISIONS)
    @patch("core.exam_readiness_ai.get_progress", return_value=CASE_B_PROGRESS)
    @patch("core.exam_readiness_ai.get_weakness", return_value=CASE_B_WEAKNESS)
    @patch("core.exam_readiness_ai.get_streak", return_value=0)
    @patch("core.exam_readiness_ai.get_revision_analytics_v2", return_value=CASE_B_REVISIONS)
    @patch("core.predictive_performance_ai.get_progress", return_value=CASE_B_PROGRESS)
    @patch("core.predictive_performance_ai.get_weakness", return_value=CASE_B_WEAKNESS)
    @patch("core.predictive_performance_ai.get_streak", return_value=0)
    @patch("core.predictive_performance_ai.get_revision_analytics_v2", return_value=CASE_B_REVISIONS)
    @patch("core.adaptive_revision_ai.get_progress", return_value=CASE_B_PROGRESS)
    @patch("core.adaptive_revision_ai.get_weakness", return_value=CASE_B_WEAKNESS)
    @patch("core.adaptive_revision_ai.get_streak", return_value=0)
    @patch("core.adaptive_revision_ai.get_revision_analytics_v2", return_value=CASE_B_REVISIONS)
    @patch("core.exam_strategy_ai.get_progress", return_value=CASE_B_PROGRESS)
    @patch("core.exam_strategy_ai.get_weakness", return_value=CASE_B_WEAKNESS)
    @patch("core.exam_strategy_ai.get_streak", return_value=0)
    @patch("core.revision_engine.get_progress", return_value=CASE_B_PROGRESS)
    @patch("core.revision_engine.get_weakness", return_value=CASE_B_WEAKNESS)
    @patch("core.revision_engine.get_revision_overview", return_value=CASE_B_REVISIONS)
    def test_phase13_cross_engine_consistency(self, *mocks):
        coach = get_coach_maturity(user="test_user_b")
        readiness = get_exam_readiness(user="test_user_b", force_refresh=True)
        pred = get_predictive_performance(user="test_user_b", force_refresh=True)
        adaptive = get_adaptive_final_revision(user="test_user_b", force_refresh=True)
        strat = get_exam_strategy(user="test_user_b", force_refresh=True)
        smart_rev = get_intelligent_revision_plan(user="test_user_b")

        # 1. Observed activity一致性
        self.assertEqual(coach["attempt_count"], 2)
        self.assertEqual(coach["avg_accuracy"], 80.0)
        self.assertEqual(coach["observed_subjects"], ["History"])
        self.assertEqual(coach["observed_topics"], ["indus_valley_civilization"])

        # 2. Exam Readiness一致性
        self.assertFalse(readiness["is_eligible"])
        self.assertIsNone(readiness["overall_readiness"])
        subj_map = {s["subject"]: s for s in readiness["subjects"]}
        self.assertEqual(subj_map["History"]["score"], 80)
        self.assertIsNone(subj_map["Polity"]["score"])
        self.assertIsNone(subj_map["Geography"]["score"])
        self.assertIsNone(subj_map["Economy"]["score"])

        # 3. Predictive一致性
        self.assertFalse(pred["is_eligible"])
        self.assertIsNone(pred["current_mock_accuracy"])
        self.assertEqual(pred["estimated_mock_accuracy"], "Need Mock Data")
        self.assertEqual(pred["estimated_readiness"], "More practice data required")

        # 4. Adaptive Revision一致性
        self.assertIn("History", adaptive["priority_subjects"])
        self.assertIsNone(adaptive["completion_percentage"])
        for r in adaptive["risk_analysis"]:
            self.assertNotIn("Low Polity", r)
            self.assertNotIn("Low Geography", r)

        # 5. Exam Strategy一致性
        self.assertFalse(strat["is_personalized"])
        self.assertEqual(strat["strategy_label"], "GENERAL TNPSC STRATEGY")

        # 6. Smart Revision一致性
        self.assertEqual(smart_rev["accuracy"], 80.0)
        self.assertNotEqual(smart_rev["accuracy"], 55.0)

    # --------------------------------------------------------------------------
    # SURGICAL NULL-SAFETY & RATIONALE TESTS
    # --------------------------------------------------------------------------
    @patch("core.exam_readiness_ai.get_progress", return_value=CASE_B_PROGRESS)
    @patch("core.exam_readiness_ai.get_weakness", return_value=CASE_B_WEAKNESS)
    @patch("core.exam_readiness_ai.get_streak", return_value=1)
    @patch("core.exam_readiness_ai.get_revision_analytics_v2", return_value=CASE_B_REVISIONS)
    def test_exam_readiness_none_never_produces_none_percent(self, _rev, _strk, _weak, _prog):
        """When overall_readiness is None, readiness_reason must never contain 'None%'."""
        readiness = get_exam_readiness("test_user_b", force_refresh=True)
        self.assertIsNone(readiness["overall_readiness"])
        self.assertNotIn("None%", readiness["readiness_reason"])
        self.assertIn("not assessed yet", readiness["readiness_reason"].lower())

    @patch("core.exam_readiness_ai.get_progress", return_value=CASE_D_PROGRESS)
    @patch("core.exam_readiness_ai.get_weakness", return_value=CASE_D_WEAKNESS)
    @patch("core.exam_readiness_ai.get_streak", return_value=5)
    @patch("core.exam_readiness_ai.get_revision_analytics_v2", return_value=CASE_D_REVISIONS)
    def test_exam_readiness_numeric_retains_percentage(self, _rev, _strk, _weak, _prog):
        """When overall_readiness is numeric, readiness_reason correctly includes the percentage."""
        readiness = get_exam_readiness("test_user_d", force_refresh=True)
        self.assertIsNotNone(readiness["overall_readiness"])
        self.assertIn(f"{readiness['overall_readiness']}%", readiness["readiness_reason"])

    @patch("ui.adaptive_revision.dashboard.get_adaptive_final_revision")
    def test_adaptive_revision_dashboard_render_null_safety(self, mock_get_adaptive):
        """Adaptive revision dashboard must safely render when completion_percentage is None."""
        from ui.adaptive_revision.dashboard import render_adaptive_revision_dashboard
        mock_get_adaptive.return_value = {
            "revision_phase": "Foundation Phase",
            "days_remaining": 30,
            "daily_target": "Revise 3 topics + 40 MCQs",
            "estimated_completion": "Projected revision completion unlocks after completing multi-subject practice baseline.",
            "priority_subjects": ["History"],
            "priority_topics": ["History: Indus Valley Civilization"],
            "revision_order": ["History"],
            "revision_cycles": ["Concept Reinforcement"],
            "risk_analysis": ["Expand practice across subjects."],
            "mentor_advice": "Maintain daily practice.",
            "dashboard_sections": {
                "completion_percentage": None,
            },
            "completion_percentage": None,
        }
        # Calling dashboard with completion_percentage=None must not raise TypeError
        try:
            render_adaptive_revision_dashboard("early_user_test")
        except TypeError as e:
            self.fail(f"render_adaptive_revision_dashboard crashed with TypeError on None: {e}")

    @patch("ui.adaptive_revision.dashboard.get_adaptive_final_revision")
    def test_adaptive_revision_dashboard_render_numeric_success(self, mock_get_adaptive):
        """Adaptive revision dashboard must safely render when completion_percentage is numeric."""
        from ui.adaptive_revision.dashboard import render_adaptive_revision_dashboard
        mock_get_adaptive.return_value = {
            "revision_phase": "30-Day Plan",
            "days_remaining": 30,
            "daily_target": "Revise 3 topics + 40 MCQs",
            "estimated_completion": "85% estimated revision completion in 24 days",
            "priority_subjects": ["History", "Polity"],
            "priority_topics": ["History: Indus Valley Civilization"],
            "revision_order": ["History", "Polity"],
            "revision_cycles": ["Concept Reinforcement"],
            "risk_analysis": ["Keep consistent."],
            "mentor_advice": "Focus on high yield topics.",
            "dashboard_sections": {
                "completion_percentage": 85,
            },
            "completion_percentage": 85,
        }
        try:
            render_adaptive_revision_dashboard("mature_user_test")
        except Exception as e:
            self.fail(f"render_adaptive_revision_dashboard crashed on numeric: {e}")


if __name__ == "__main__":
    unittest.main()

