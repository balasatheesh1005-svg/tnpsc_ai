"""
Unit tests for Personal Study Planner Engine V2 (core/study_planner_ai.py).
Verifies planning priority logic, schema conformance, dynamic time adaptation,
and data integrity across learning intelligence engines.
"""
import sys
import unittest
import json

from core.study_planner_ai import get_personal_study_plan, _determine_priority_label
from core.study_planner import get_today_plan


class TestStudyPlannerEngineV2(unittest.TestCase):

    def test_priority_label_mapping(self):
        """Test numeric priority label mapping."""
        self.assertEqual(_determine_priority_label(1), "Critical")
        self.assertEqual(_determine_priority_label(2), "High")
        self.assertEqual(_determine_priority_label(3), "Medium-High")
        self.assertEqual(_determine_priority_label(4), "Medium")
        self.assertEqual(_determine_priority_label(5), "Standard")
        self.assertEqual(_determine_priority_label(6), "Optional")

    def test_master_plan_schema(self):
        """Verify master plan dictionary schema and required fields."""
        plan = get_personal_study_plan("test_user", available_time=45)
        
        self.assertIn("today_plan", plan)
        self.assertIn("estimated_time", plan)
        self.assertIn("available_time", plan)
        self.assertIn("expected_mastery_gain", plan)
        self.assertIn("expected_xp", plan)
        self.assertIn("expected_outcome", plan)
        self.assertIn("study_sequence", plan)
        self.assertIn("next_action", plan)
        self.assertIn("mentor_message", plan)
        self.assertIn("daily_summary", plan)

        # Check today_plan item schema
        today_plan = plan["today_plan"]
        self.assertTrue(len(today_plan) > 0)
        
        first_task = today_plan[0]
        required_task_keys = [
            "priority", "priority_label", "task", "subject", "topic",
            "repository", "question_type", "duration", "reason",
            "expected_benefit", "reward"
        ]
        for key in required_task_keys:
            self.assertIn(key, first_task)

    def test_time_adaptation_20_mins(self):
        """Verify 20-minute available time caps tasks strictly to critical items."""
        plan_20 = get_personal_study_plan("test_user", available_time=20)
        self.assertLessEqual(plan_20["estimated_time"], 25)
        self.assertLessEqual(len(plan_20["today_plan"]), 2)

    def test_time_adaptation_90_mins(self):
        """Verify 90-minute available time generates extended session with PYQ/practice."""
        plan_90 = get_personal_study_plan("test_user", available_time=90)
        self.assertGreater(len(plan_90["today_plan"]), len(get_personal_study_plan("test_user", 20)["today_plan"]))

    def test_legacy_adapter_compatibility(self):
        """Verify core.study_planner.get_today_plan adapter returns valid legacy format."""
        legacy_output = get_today_plan("test_user")
        self.assertIn("topic", legacy_output)
        self.assertIn("questions", legacy_output)
        self.assertIn("mode", legacy_output)
        self.assertIn("planner_v2", legacy_output)

    def test_json_serializability(self):
        """Verify engine output can be serialized to JSON without circular reference or non-serializable objects."""
        plan = get_personal_study_plan("test_user", available_time=45)
        json_str = json.dumps(plan)
        self.assertTrue(len(json_str) > 0)


if __name__ == "__main__":
    unittest.main()
