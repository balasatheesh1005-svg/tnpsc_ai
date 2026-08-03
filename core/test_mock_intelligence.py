"""
Unit tests for Mock Exam Intelligence Engine V2 (core/mock_intelligence_ai.py).
Verifies observed behavioral mock analytics, attempt ratios, time management evaluation,
section & question type performance, mistake pattern detection, and JSON schema.
"""
import sys
import unittest
import json

from core.mock_intelligence_ai import get_mock_intelligence, _classify_mock_level


class TestMockIntelligenceEngineV2(unittest.TestCase):

    def test_mock_level_classification(self):
        """Test numeric mock accuracy level classification."""
        self.assertEqual(_classify_mock_level(90), "Exceptional")
        self.assertEqual(_classify_mock_level(78), "Good")
        self.assertEqual(_classify_mock_level(65), "Stable")
        self.assertEqual(_classify_mock_level(50), "Needs Focus")

    def test_master_mock_intelligence_schema(self):
        """Verify mock intelligence engine output conforms to master JSON schema."""
        mock_data = get_mock_intelligence("test_user")

        required_keys = [
            "overall_accuracy",
            "mock_level",
            "time_per_question",
            "attempt_rate",
            "correct_vs_wrong",
            "section_performance",
            "question_types",
            "mistakes",
            "strengths",
            "time_analysis",
            "summary",
            "slowest_section",
            "weakest_qtype",
        ]
        for key in required_keys:
            self.assertIn(key, mock_data, f"Missing required key in mock intelligence output: {key}")

    def test_accuracy_and_attempt_ratios(self):
        """Verify overall accuracy and attempt ratio percentages."""
        mock_data = get_mock_intelligence("test_user")

        acc = mock_data["overall_accuracy"]
        self.assertIsInstance(acc, int)
        self.assertGreaterEqual(acc, 0)
        self.assertLessEqual(acc, 100)

        ratio = mock_data["correct_vs_wrong"]
        self.assertIn("correct", ratio)
        self.assertIn("wrong", ratio)
        self.assertIn("skipped", ratio)

        total_pct = ratio["correct"] + ratio["wrong"] + ratio["skipped"]
        self.assertEqual(total_pct, 100, "Correct + Wrong + Skipped must sum to 100%")

    def test_time_management_analytics(self):
        """Verify overall and section-wise time per question analytics."""
        mock_data = get_mock_intelligence("test_user")

        avg_time = mock_data["time_per_question"]
        self.assertIsInstance(avg_time, int)
        self.assertGreater(avg_time, 0)
        self.assertIsInstance(mock_data["time_analysis"], str)

    def test_section_performance_list(self):
        """Verify section-wise performance items contain accuracy and time allocation."""
        mock_data = get_mock_intelligence("test_user")
        sections = mock_data["section_performance"]

        self.assertTrue(len(sections) >= 5)
        for s in sections:
            self.assertIn("subject", s)
            self.assertIn("accuracy", s)
            self.assertIn("avg_time_sec", s)
            self.assertGreaterEqual(s["accuracy"], 0)
            self.assertLessEqual(s["accuracy"], 100)
            self.assertGreater(s["avg_time_sec"], 0)

    def test_question_types_list(self):
        """Verify question type performance list contains accuracies."""
        mock_data = get_mock_intelligence("test_user")
        qtypes = mock_data["question_types"]

        self.assertTrue(len(qtypes) >= 4)
        for q in qtypes:
            self.assertIn("type", q)
            self.assertIn("accuracy", q)
            self.assertGreaterEqual(q["accuracy"], 0)
            self.assertLessEqual(q["accuracy"], 100)

    def test_mistakes_and_strengths_non_empty(self):
        """Verify mistake patterns and strengths are non-empty lists of strings."""
        mock_data = get_mock_intelligence("test_user")

        self.assertTrue(len(mock_data["mistakes"]) > 0)
        self.assertTrue(len(mock_data["strengths"]) > 0)
        self.assertIsInstance(mock_data["summary"], str)

    def test_json_serializability(self):
        """Verify engine output can be serialized to JSON cleanly."""
        mock_data = get_mock_intelligence("test_user")
        json_str = json.dumps(mock_data)
        self.assertTrue(len(json_str) > 0)


if __name__ == "__main__":
    unittest.main()
