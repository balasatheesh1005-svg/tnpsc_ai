"""
Unit tests for Predictive Performance Engine V2 (core/predictive_performance_ai.py).
Verifies rule-based deterministic output, estimated metric ranges, confidence calculation,
prohibition of guaranteed claims, and JSON schema conformance.
"""
import unittest

from core.predictive_performance_ai import (
    get_predictive_performance,
    _classify_trend,
    _format_range,
)


class TestPredictivePerformanceEngineV2(unittest.TestCase):

    def test_trend_classification(self):
        """Test numeric delta trend classification."""
        self.assertEqual(_classify_trend(70, 4.0), "Improving")
        self.assertEqual(_classify_trend(70, 1.5), "Stable")
        self.assertEqual(_classify_trend(70, 0.5), "Needs Attention")

    def test_range_formatting(self):
        """Test formatted estimation ranges."""
        res = _format_range(72, 3.0, 7.0)
        self.assertTrue("–" in res or "-" in res)
        self.assertTrue(res.endswith("%"))

        # Verify low < high
        parts = res.replace("%", "").split("–")
        if len(parts) == 2:
            low_val, high_val = int(parts[0]), int(parts[1])
            self.assertLess(low_val, high_val)
            self.assertLessEqual(high_val, 99)

    def test_master_schema_conformance(self):
        """Verify master predictive performance schema returns all required keys."""
        pred = get_predictive_performance("test_user")

        required_keys = [
            "current_readiness",
            "estimated_readiness",
            "readiness_trend",
            "current_mock_accuracy",
            "estimated_mock_accuracy",
            "mock_accuracy_trend",
            "current_topic_mastery",
            "estimated_topic_mastery",
            "topic_mastery_trend",
            "current_revision_health",
            "estimated_revision_health",
            "revision_trend",
            "current_consistency",
            "estimated_consistency",
            "consistency_trend",
            "current_repo_completion",
            "estimated_repo_completion",
            "repo_completion_trend",
            "prediction_confidence",
            "confidence_reason",
            "prediction_reason",
            "mentor_projection",
            "explanation_bullets",
            "dimensions",
            "disclaimer",
        ]
        for key in required_keys:
            self.assertIn(key, pred, f"Missing required key in predictive performance schema: {key}")

    def test_prohibited_guarantee_claims(self):
        """Verify that output NEVER claims absolute guarantees or pass/fail predictions."""
        pred = get_predictive_performance("test_user")

        combined_text = (
            str(pred.get("prediction_reason", "")) +
            str(pred.get("mentor_projection", "")) +
            str(pred.get("confidence_reason", ""))
        ).lower()

        forbidden_phrases = [
            "you will pass",
            "you will clear",
            "you will get rank",
            "guaranteed",
            "pass/fail",
            "100% pass",
        ]
        for phrase in forbidden_phrases:
            self.assertNotIn(phrase, combined_text, f"Forbidden guarantee phrase found: {phrase}")

    def test_confidence_range(self):
        """Verify prediction confidence score is between 0 and 100."""
        pred = get_predictive_performance("test_user")
        conf = pred["prediction_confidence"]
        self.assertIsInstance(conf, int)
        self.assertGreaterEqual(conf, 50)
        self.assertLessEqual(conf, 100)


if __name__ == "__main__":
    unittest.main()
