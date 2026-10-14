"""
Unit tests for Study Planner Truth & Safety (tests/unit/test_study_planner_truth.py).
Validates evidence gating, observed performance semantics, non-fabrication of future
mastery, task/time consistency, zero-data beginner handling, and absence of guarantee language.
"""
import unittest
from unittest.mock import patch, MagicMock

from core.study_planner_ai import get_personal_study_plan
from ui.planner.dashboard import render_study_planner_dashboard


class TestStudyPlannerTruth(unittest.TestCase):
    """Test matrix verifying truth contract across all 8 required cases."""

    def test_case_1_zero_attempts(self):
        """CASE 1 - ZERO ATTEMPTS: useful beginner plan, no fake metrics or projections."""
        with patch("core.study_planner_ai.get_progress", return_value=[]), \
             patch("core.learning_intelligence_ai.get_progress", return_value=[]), \
             patch("core.coach_maturity_ai.get_progress", return_value=[]), \
             patch("core.study_planner_ai.get_weakness", return_value={}), \
             patch("core.learning_intelligence_ai.get_weakness", return_value={}), \
             patch("core.coach_maturity_ai.get_weakness", return_value={}), \
             patch("core.study_planner_ai.get_streak", return_value=0), \
             patch("core.study_planner_ai.get_revision_analytics_v2", return_value={"overdue": [], "due_today": []}):

            plan = get_personal_study_plan(user="zero_user", available_time=45, force_refresh=True)

            self.assertIsInstance(plan, dict)
            self.assertTrue(len(plan["today_plan"]) >= 1)
            # Subject and topic must not be placeholder strings like 'Not enough data yet'
            self.assertNotIn("Not enough data yet", plan["subject"])
            self.assertNotIn("Not enough data yet", plan["topic"])

            outcome = plan["expected_outcome"]
            # No fake observed accuracy or mastery percentage
            self.assertIsNone(outcome["observed_accuracy"])
            self.assertEqual(outcome["current_mastery"], "No Data")
            self.assertFalse(outcome["projection_available"])

            # Check no arbitrary percentage strings in outcome
            self.assertNotIn("%", str(outcome["expected_mastery"]))
            self.assertNotIn("%", str(outcome["expected_mastery_gain"]))
            self.assertNotIn("%", str(plan["expected_mastery_gain"]))

    def test_case_2_two_attempts_80_accuracy(self):
        """CASE 2 - TWO ATTEMPTS / 80% ACCURACY: shows 80% as observed accuracy, never arbitrary 98%."""
        sample_progress = [
            {"subject": "History", "topic": "indus_valley", "accuracy": 80.0, "completed_at": "2026-03-01T10:00:00"},
            {"subject": "History", "topic": "indus_valley", "accuracy": 80.0, "completed_at": "2026-03-02T10:00:00"}
        ]
        with patch("core.study_planner_ai.get_progress", return_value=sample_progress), \
             patch("core.learning_intelligence_ai.get_progress", return_value=sample_progress), \
             patch("core.coach_maturity_ai.get_progress", return_value=sample_progress), \
             patch("core.study_planner_ai.get_weakness", return_value={}), \
             patch("core.learning_intelligence_ai.get_weakness", return_value={}), \
             patch("core.coach_maturity_ai.get_weakness", return_value={}), \
             patch("core.study_planner_ai.get_streak", return_value=0), \
             patch("core.study_planner_ai.get_revision_analytics_v2", return_value={"overdue": [], "due_today": []}):

            plan = get_personal_study_plan(user="user_80", available_time=45, force_refresh=True)

            outcome = plan["expected_outcome"]
            self.assertEqual(outcome["observed_accuracy"], 80.0)
            self.assertEqual(outcome["observed_accuracy_str"], "80.0%")
            # Must NOT claim arbitrary 98% or +18.8%
            self.assertNotEqual(outcome["expected_mastery"], "98%")
            self.assertNotEqual(outcome["expected_mastery"], "98.0%")
            self.assertNotEqual(outcome["expected_mastery_gain"], "+18.8%")
            self.assertNotIn("%", str(outcome["expected_mastery"]))
            self.assertFalse(outcome["projection_available"])

    def test_case_3_low_evidence(self):
        """CASE 3 - LOW EVIDENCE (2 attempts, 1 subject, 0 mocks, 0 revisions): recommendations allowed, projections blocked."""
        sample_progress = [
            {"subject": "History", "topic": "indus_valley", "accuracy": 75.0, "completed_at": "2026-03-01T10:00:00"},
            {"subject": "History", "topic": "indus_valley", "accuracy": 85.0, "completed_at": "2026-03-02T10:00:00"}
        ]
        with patch("core.study_planner_ai.get_progress", return_value=sample_progress), \
             patch("core.learning_intelligence_ai.get_progress", return_value=sample_progress), \
             patch("core.coach_maturity_ai.get_progress", return_value=sample_progress), \
             patch("core.study_planner_ai.get_weakness", return_value={}), \
             patch("core.coach_maturity_ai.get_weakness", return_value={}), \
             patch("core.study_planner_ai.get_streak", return_value=0), \
             patch("core.study_planner_ai.get_revision_analytics_v2", return_value={"overdue": [], "due_today": []}):

            plan = get_personal_study_plan(user="low_data_user", available_time=45, force_refresh=True)

            # Recommendations allowed
            self.assertTrue(len(plan["today_plan"]) >= 1)
            # Tier correctly reflects early signal
            self.assertEqual(plan["expected_outcome"]["evidence_tier_label"], "Early Signal")
            # Precise unsupported prediction blocked
            self.assertFalse(plan["expected_outcome"]["projection_available"])
            self.assertNotIn("%", str(plan["expected_outcome"]["expected_mastery"]))

    def test_case_4_more_learner_data(self):
        """CASE 4 - MORE LEARNER DATA (>=5 attempts, multiple subjects): planner remains functional without fake precise projection."""
        rich_progress = [
            {"subject": "History", "topic": "indus_valley", "accuracy": 80.0, "completed_at": "2026-03-01T10:00:00"},
            {"subject": "History", "topic": "delhi_sultanate", "accuracy": 85.0, "completed_at": "2026-03-02T10:00:00"},
            {"subject": "Polity", "topic": "preamble", "accuracy": 90.0, "completed_at": "2026-03-03T10:00:00"},
            {"subject": "Polity", "topic": "fundamental_rights", "accuracy": 70.0, "completed_at": "2026-03-04T10:00:00"},
            {"subject": "Economy", "topic": "five_year_plans", "accuracy": 75.0, "completed_at": "2026-03-05T10:00:00"},
            {"subject": "Economy", "topic": "rbi", "accuracy": 80.0, "completed_at": "2026-03-06T10:00:00"},
        ]
        with patch("core.study_planner_ai.get_progress", return_value=rich_progress), \
             patch("core.learning_intelligence_ai.get_progress", return_value=rich_progress), \
             patch("core.coach_maturity_ai.get_progress", return_value=rich_progress), \
             patch("core.study_planner_ai.get_weakness", return_value={"Polity-fundamental_rights": 3}), \
             patch("core.coach_maturity_ai.get_weakness", return_value={"Polity-fundamental_rights": 3}), \
             patch("core.study_planner_ai.get_streak", return_value=4), \
             patch("core.study_planner_ai.get_revision_analytics_v2", return_value={"overdue": [], "due_today": []}):

            plan = get_personal_study_plan(user="rich_user", available_time=45, force_refresh=True)

            self.assertTrue(len(plan["today_plan"]) >= 1)
            outcome = plan["expected_outcome"]
            self.assertEqual(outcome["observed_accuracy"], 80.0)
            # Still no arbitrary future percentage
            self.assertNotIn("%", str(outcome["expected_mastery"]))
            self.assertFalse(outcome["projection_available"])

    def test_case_5_none_and_missing_values(self):
        """CASE 5 - NONE / MISSING VALUES: guarded against None%, float(None), tracebacks, fallback to safe values."""
        corrupt_progress = [
            {"subject": None, "topic": None, "accuracy": None},
            {"subject": "History", "accuracy": None},
        ]
        with patch("core.study_planner_ai.get_progress", return_value=corrupt_progress), \
             patch("core.learning_intelligence_ai.get_progress", return_value=corrupt_progress), \
             patch("core.coach_maturity_ai.get_progress", return_value=corrupt_progress), \
             patch("core.study_planner_ai.get_weakness", return_value={}), \
             patch("core.coach_maturity_ai.get_weakness", return_value={}), \
             patch("core.study_planner_ai.get_streak", return_value=0), \
             patch("core.study_planner_ai.get_revision_analytics_v2", return_value={"overdue": [], "due_today": []}):

            plan = get_personal_study_plan(user="corrupt_user", available_time=None, force_refresh=True)

            self.assertIsInstance(plan, dict)
            self.assertNotIn("None%", str(plan))
            self.assertIsInstance(plan["estimated_time"], int)
            self.assertIsInstance(plan["available_time"], int)
            outcome = plan["expected_outcome"]
            self.assertNotIn("None%", str(outcome))
            self.assertIsNone(outcome["observed_accuracy"])
            self.assertEqual(outcome["current_mastery"], "No Data")

    def test_case_6_task_and_time_consistency(self):
        """CASE 6 - TASK TIME: internal consistency between task durations and total planned minutes."""
        sample_progress = [
            {"subject": "History", "topic": "indus_valley", "accuracy": 80.0}
        ]
        with patch("core.study_planner_ai.get_progress", return_value=sample_progress), \
             patch("core.learning_intelligence_ai.get_progress", return_value=sample_progress), \
             patch("core.coach_maturity_ai.get_progress", return_value=sample_progress), \
             patch("core.study_planner_ai.get_weakness", return_value={}), \
             patch("core.coach_maturity_ai.get_weakness", return_value={}), \
             patch("core.study_planner_ai.get_streak", return_value=0), \
             patch("core.study_planner_ai.get_revision_analytics_v2", return_value={"overdue": [], "due_today": []}):

            for time_budget in [20, 45, 90]:
                plan = get_personal_study_plan(user="time_user", available_time=time_budget, force_refresh=True)
                tasks = plan["today_plan"]
                summed_duration = sum(t["duration"] for t in tasks)
                self.assertEqual(summed_duration, plan["estimated_time"])
                self.assertEqual(summed_duration, plan["daily_summary"]["estimated_time"])
                self.assertEqual(len(tasks), plan["daily_summary"]["total_tasks"])
                self.assertLessEqual(plan["estimated_time"], time_budget + 5)

    def test_case_7_label_truth(self):
        """CASE 7 - LABEL TRUTH: underlying accuracy is labelled Observed Accuracy, not Mastery."""
        sample_progress = [
            {"subject": "History", "topic": "indus_valley", "accuracy": 80.0}
        ]
        with patch("core.study_planner_ai.get_progress", return_value=sample_progress), \
             patch("core.learning_intelligence_ai.get_progress", return_value=sample_progress), \
             patch("core.coach_maturity_ai.get_progress", return_value=sample_progress), \
             patch("core.study_planner_ai.get_weakness", return_value={}), \
             patch("core.coach_maturity_ai.get_weakness", return_value={}), \
             patch("core.study_planner_ai.get_streak", return_value=0), \
             patch("core.study_planner_ai.get_revision_analytics_v2", return_value={"overdue": [], "due_today": []}):

            plan = get_personal_study_plan(user="truth_user", available_time=45, force_refresh=True)

            outcome = plan["expected_outcome"]
            self.assertIn("observed_accuracy", outcome)
            self.assertIn("observed_accuracy_str", outcome)
            self.assertEqual(outcome["observed_accuracy"], 80.0)

    def test_case_8_no_guarantee_language(self):
        """CASE 8 - NO GUARANTEE LANGUAGE: neither plan data nor rendered UI contains unsupported promises."""
        sample_progress = [
            {"subject": "History", "topic": "indus_valley", "accuracy": 80.0}
        ]
        with patch("core.study_planner_ai.get_progress", return_value=sample_progress), \
             patch("core.learning_intelligence_ai.get_progress", return_value=sample_progress), \
             patch("core.coach_maturity_ai.get_progress", return_value=sample_progress), \
             patch("core.study_planner_ai.get_weakness", return_value={}), \
             patch("core.coach_maturity_ai.get_weakness", return_value={}), \
             patch("core.study_planner_ai.get_streak", return_value=0), \
             patch("core.study_planner_ai.get_revision_analytics_v2", return_value={"overdue": [], "due_today": []}):

            plan = get_personal_study_plan(user="guarantee_check", available_time=45, force_refresh=True)
            plan_str = str(plan).lower()

            prohibited_terms = [
                "guaranteed",
                "will reach",
                "will improve by",
                "expected mastery 98%",
                "expected mastery: 98%",
                "+18.8%",
                "+12.9%",
            ]
            for term in prohibited_terms:
                self.assertNotIn(term, plan_str)

            # Check today_plan benefits
            for task in plan["today_plan"]:
                self.assertNotIn("elevate mastery from", task["expected_benefit"].lower())


if __name__ == "__main__":
    unittest.main()
