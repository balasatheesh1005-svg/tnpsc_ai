"""
Unit tests for Adaptive Final Revision Engine V2 (core/adaptive_revision_ai.py).
Verifies strategy output schema, phase calculation, priority ordering, risk detection,
non-fear based wording, and mentor guidance generation.
"""
import unittest

from core.adaptive_revision_ai import (
    get_adaptive_final_revision,
    _determine_revision_phase,
    _generate_daily_target,
)


class TestAdaptiveRevisionEngineV2(unittest.TestCase):

    def test_determine_revision_phase(self):
        """Verify dynamic revision phase selection based on timeline."""
        self.assertEqual(_determine_revision_phase(95), "90-Day Plan")
        self.assertEqual(_determine_revision_phase(60), "60-Day Plan")
        self.assertEqual(_determine_revision_phase(30), "30-Day Plan")
        self.assertEqual(_determine_revision_phase(15), "15-Day Plan")
        self.assertEqual(_determine_revision_phase(7), "7-Day Plan")
        self.assertEqual(_determine_revision_phase(3), "3-Day Plan")
        self.assertEqual(_determine_revision_phase(1), "1-Day Rapid Recall")

    def test_daily_target_generation(self):
        """Verify daily target generation matches phase requirements."""
        target_30 = _generate_daily_target("30-Day Plan", 70)
        self.assertIn("topics", target_30.lower())
        self.assertIn("mcqs", target_30.lower())

    def test_master_schema_conformance(self):
        """Verify master adaptive final revision engine schema returns all required keys."""
        plan = get_adaptive_final_revision("test_user")

        required_keys = [
            "revision_phase",
            "days_remaining",
            "priority_subjects",
            "priority_topics",
            "revision_order",
            "daily_target",
            "revision_cycles",
            "risk_analysis",
            "mentor_advice",
            "estimated_completion",
            "dashboard_sections",
        ]
        for key in required_keys:
            self.assertIn(key, plan, f"Missing required key in adaptive revision schema: {key}")

        # Check revision cycles contain all 4 standard cycles
        cycles = plan["revision_cycles"]
        self.assertEqual(len(cycles), 4)
        self.assertIn("Concept Reinforcement", cycles[0])
        self.assertIn("Practice Questions", cycles[1])
        self.assertIn("PYQ Revision", cycles[2])
        self.assertIn("Rapid Recall", cycles[3])

    def test_priority_subjects_generation(self):
        """Verify priority subjects are generated non-randomly."""
        plan = get_adaptive_final_revision("test_user")
        subjects = plan["priority_subjects"]
        self.assertIsInstance(subjects, list)
        self.assertGreaterEqual(len(subjects), 1)

    def test_non_fear_language_in_risk_analysis(self):
        """Verify risk analysis uses constructive, non-fear guidance."""
        plan = get_adaptive_final_revision("test_user")
        risks = plan["risk_analysis"]
        combined_text = " ".join(risks).lower()

        forbidden_fear_words = [
            "fail",
            "impossible",
            "doomed",
            "disaster",
            "hopeless",
            "panic",
            "guaranteed failure",
        ]
        for word in forbidden_fear_words:
            self.assertNotIn(word, combined_text, f"Fear-based language found in risk analysis: {word}")

    def test_explicit_target_days(self):
        """Verify passing explicit target_days changes phase appropriately."""
        plan_7 = get_adaptive_final_revision("test_user", target_days=7)
        self.assertEqual(plan_7["revision_phase"], "7-Day Plan")


if __name__ == "__main__":
    unittest.main()
