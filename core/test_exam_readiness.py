"""
Unit tests for Exam Readiness Engine V2 (core/exam_readiness_ai.py).
Verifies 5-dimension readiness evaluation, score classification levels,
subject readiness calculations, strength/improvement analysis, and JSON schema.
"""
import sys
import unittest
import json

from core.exam_readiness_ai import get_exam_readiness, _classify_readiness_level


class TestExamReadinessEngineV2(unittest.TestCase):

    def test_level_classification_mapping(self):
        """Test numeric readiness score classification levels."""
        self.assertEqual(_classify_readiness_level(15), "Beginning")
        self.assertEqual(_classify_readiness_level(35), "Developing")
        self.assertEqual(_classify_readiness_level(65), "Exam Ready")
        self.assertEqual(_classify_readiness_level(85), "Highly Ready")
        self.assertEqual(_classify_readiness_level(95), "Excellent Readiness")

    def test_master_readiness_schema(self):
        """Verify exam readiness engine output conforms to master JSON schema."""
        readiness = get_exam_readiness("test_user")

        required_keys = [
            "overall_readiness",
            "level",
            "readiness_dimensions",
            "subjects",
            "strengths",
            "improvements",
            "readiness_reason",
            "mentor_insight",
            "strongest_subject",
            "weakest_subject",
        ]
        for key in required_keys:
            self.assertIn(key, readiness, f"Missing required key in readiness output: {key}")

    def test_score_bounds(self):
        """Verify overall score is an integer bounded between 0 and 100."""
        readiness = get_exam_readiness("test_user")
        score = readiness["overall_readiness"]
        self.assertIsInstance(score, int)
        self.assertGreaterEqual(score, 0)
        self.assertLessEqual(score, 100)

    def test_dimensions_schema_and_bounds(self):
        """Verify 5 dimensions are present and bounded between 0 and 100."""
        readiness = get_exam_readiness("test_user")
        dims = readiness["readiness_dimensions"]

        required_dims = ["topic_mastery", "repository_completion", "revision_health", "consistency", "pyq_readiness"]
        for d_key in required_dims:
            self.assertIn(d_key, dims)
            d_val = dims[d_key]
            self.assertIsInstance(d_val, int)
            self.assertGreaterEqual(d_val, 0)
            self.assertLessEqual(d_val, 100)

    def test_subjects_readiness_list(self):
        """Verify subjects list contains standard subjects with valid scores."""
        readiness = get_exam_readiness("test_user")
        subjects = readiness["subjects"]

        self.assertTrue(len(subjects) >= 5)
        for s_item in subjects:
            self.assertIn("subject", s_item)
            self.assertIn("score", s_item)
            s_score = s_item["score"]
            self.assertIsInstance(s_score, int)
            self.assertGreaterEqual(s_score, 0)
            self.assertLessEqual(s_score, 100)

    def test_strengths_and_improvements_non_empty(self):
        """Verify strengths and improvement directives are non-empty lists."""
        readiness = get_exam_readiness("test_user")
        self.assertTrue(len(readiness["strengths"]) > 0)
        self.assertTrue(len(readiness["improvements"]) > 0)
        self.assertIsInstance(readiness["readiness_reason"], str)
        self.assertIsInstance(readiness["mentor_insight"], str)

    def test_json_serializability(self):
        """Verify engine output can be serialized to JSON without circular reference."""
        readiness = get_exam_readiness("test_user")
        json_str = json.dumps(readiness)
        self.assertTrue(len(json_str) > 0)


if __name__ == "__main__":
    unittest.main()
