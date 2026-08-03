"""
Unit tests for AI Recommendation Engine V2 (core/recommendation_ai.py).
Verifies single primary recommendation cascade, risk detection logic,
confidence calculation, benefit estimation, and JSON schema conformance.
"""
import sys
import unittest
import json

from core.recommendation_ai import get_ai_recommendation


class TestRecommendationEngineV2(unittest.TestCase):

    def test_master_recommendation_schema(self):
        """Verify recommendation engine output conforms to master JSON schema."""
        rec = get_ai_recommendation("test_user")

        required_keys = [
            "current_action",
            "next_action",
            "recommendation",
            "recommendation_type",
            "priority",
            "subject",
            "topic",
            "repository",
            "question_type",
            "risk",
            "risk_level",
            "risk_description",
            "estimated_benefit",
            "confidence",
            "confidence_reason",
            "explanation",
            "mentor_message",
            "learning_bottleneck",
        ]
        for key in required_keys:
            self.assertIn(key, rec, f"Missing required key in recommendation output: {key}")

    def test_single_primary_recommendation(self):
        """Verify engine returns exactly one unambiguous primary recommendation."""
        rec = get_ai_recommendation("test_user")
        self.assertIsInstance(rec["recommendation"], str)
        self.assertTrue(len(rec["recommendation"]) > 0)
        self.assertIn(rec["priority"], ["Critical", "High", "Medium-High", "Medium", "Standard"])

    def test_risk_detection_level(self):
        """Verify risk level is categorized into standard levels."""
        rec = get_ai_recommendation("test_user")
        self.assertIn(rec["risk_level"], ["Critical", "High", "Medium", "Low"])
        self.assertIsInstance(rec["risk"], str)
        self.assertIsInstance(rec["risk_description"], str)

    def test_confidence_score_range(self):
        """Verify recommendation confidence score is an integer bounded between 70% and 98%."""
        rec = get_ai_recommendation("test_user")
        conf = rec["confidence"]
        self.assertIsInstance(conf, int)
        self.assertGreaterEqual(conf, 70)
        self.assertLessEqual(conf, 98)

    def test_estimated_benefit_structure(self):
        """Verify estimated benefit contains required fields."""
        rec = get_ai_recommendation("test_user")
        benefit = rec["estimated_benefit"]
        self.assertIn("mastery", benefit)
        self.assertIn("xp", benefit)
        self.assertIn("confidence", benefit)
        self.assertIn("completion_progress", benefit)

    def test_json_serializability(self):
        """Verify output can be serialized to JSON cleanly."""
        rec = get_ai_recommendation("test_user")
        json_str = json.dumps(rec)
        self.assertTrue(len(json_str) > 0)


if __name__ == "__main__":
    unittest.main()
