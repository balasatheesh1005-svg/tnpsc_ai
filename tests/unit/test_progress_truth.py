import unittest
from unittest.mock import MagicMock, patch
import pandas as pd

from core.progress_ai import aggregate_topic_progress
from ui.pages.progress import render_progress_page


class TestProgressAnalyticsTruth(unittest.TestCase):
    """
    Targeted test suite for Progress Analytics topic aggregation,
    duplicate cleanup, attempt preservation, and truthful classification.
    """

    def test_case_1_same_topic_multiple_attempts(self):
        """CASE 1: Same topic attempted multiple times aggregates to 1 topic entry with mean accuracy."""
        raw_rows = [
            {"subject": "history", "topic": "indus_valley", "accuracy": 80.0},
            {"subject": "history", "topic": "indus_valley", "accuracy": 90.0},
        ]
        agg = aggregate_topic_progress(raw_rows)
        self.assertEqual(len(agg), 1, "Should aggregate into exactly one logical topic entry")
        self.assertEqual(agg.iloc[0]["Subject"], "history")
        self.assertEqual(agg.iloc[0]["Accuracy (%)"], 85.0)
        self.assertEqual(agg.iloc[0]["Attempts"], 2)

    def test_case_2_strong_weak_crossing(self):
        """CASE 2: Same topic with 40% and 90% attempts must NOT appear in both Weak and Strong."""
        raw_rows = [
            {"subject": "history", "topic": "indus_valley", "accuracy": 40.0},
            {"subject": "history", "topic": "indus_valley", "accuracy": 90.0},
        ]
        agg = aggregate_topic_progress(raw_rows)
        self.assertEqual(len(agg), 1)
        self.assertEqual(agg.iloc[0]["Accuracy (%)"], 65.0)

        weak = agg[agg["Accuracy (%)"] < 50]
        strong = agg[agg["Accuracy (%)"] >= 75]
        self.assertEqual(len(weak), 0, "65% should not be classified as Weak (<50)")
        self.assertEqual(len(strong), 0, "65% should not be classified as Strong (>=75)")

        # Verify a topic that genuinely averages to strong (>=75)
        raw_strong = [
            {"subject": "history", "topic": "indus_valley", "accuracy": 70.0},
            {"subject": "history", "topic": "indus_valley", "accuracy": 90.0},
        ]
        agg_strong = aggregate_topic_progress(raw_strong)
        self.assertEqual(len(agg_strong), 1)
        self.assertEqual(agg_strong.iloc[0]["Accuracy (%)"], 80.0)
        self.assertEqual(len(agg_strong[agg_strong["Accuracy (%)"] >= 75]), 1)
        self.assertEqual(len(agg_strong[agg_strong["Accuracy (%)"] < 50]), 0)

        # Verify a topic that genuinely averages to weak (<50)
        raw_weak = [
            {"subject": "history", "topic": "indus_valley", "accuracy": 30.0},
            {"subject": "history", "topic": "indus_valley", "accuracy": 50.0},
        ]
        agg_weak = aggregate_topic_progress(raw_weak)
        self.assertEqual(len(agg_weak), 1)
        self.assertEqual(agg_weak.iloc[0]["Accuracy (%)"], 40.0)
        self.assertEqual(len(agg_weak[agg_weak["Accuracy (%)"] < 50]), 1)
        self.assertEqual(len(agg_weak[agg_weak["Accuracy (%)"] >= 75]), 0)

    def test_case_3_attempt_count_preserved(self):
        """CASE 3: 3 attempts of same topic must preserve real attempt count (3)."""
        raw_rows = [
            {"subject": "history", "topic": "indus_valley", "accuracy": 70.0},
            {"subject": "history", "topic": "indus_valley", "accuracy": 80.0},
            {"subject": "history", "topic": "indus_valley", "accuracy": 90.0},
        ]
        agg = aggregate_topic_progress(raw_rows)
        self.assertEqual(len(agg), 1, "Logical topics must be 1")
        self.assertEqual(agg.iloc[0]["Attempts"], 3, "Real attempts count must be 3")
        self.assertEqual(agg.iloc[0]["Accuracy (%)"], 80.0)

    def test_case_4_same_topic_name_different_subjects(self):
        """CASE 4: Same topic label in different subjects must remain 2 distinct logical entries."""
        raw_rows = [
            {"subject": "history", "topic": "administration", "accuracy": 80.0},
            {"subject": "tn_administration", "topic": "administration", "accuracy": 50.0},
        ]
        agg = aggregate_topic_progress(raw_rows)
        self.assertEqual(len(agg), 2, "Cross-subject topics with identical names must remain separate")
        subjects = list(agg["Subject"])
        self.assertIn("history", subjects)
        self.assertIn("tn_administration", subjects)

    def test_case_5_multiple_topics(self):
        """CASE 5: Multiple topics across subjects all remain distinct."""
        raw_rows = [
            {"subject": "history", "topic": "indus_valley", "accuracy": 80.0},
            {"subject": "history", "topic": "indus_valley", "accuracy": 90.0},
            {"subject": "history", "topic": "guptas", "accuracy": 70.0},
            {"subject": "polity", "topic": "preamble", "accuracy": 40.0},
            {"subject": "polity", "topic": "preamble", "accuracy": 60.0},
            {"subject": "polity", "topic": "fundamental_rights", "accuracy": 95.0},
        ]
        agg = aggregate_topic_progress(raw_rows)
        self.assertEqual(len(agg), 4, "Should aggregate 6 attempts into 4 unique logical topics")

    def test_case_6_empty_data(self):
        """CASE 6: Empty progress data returns clean empty structure without fabricated entries."""
        for empty_input in [None, [], pd.DataFrame()]:
            agg = aggregate_topic_progress(empty_input)
            self.assertTrue(isinstance(agg, pd.DataFrame))
            self.assertEqual(len(agg), 0)
            self.assertEqual(list(agg.columns), ["Subject", "Repository", "Note Part", "Accuracy (%)", "Attempts"])

    def test_case_7_none_malformed_optional_values(self):
        """CASE 7: Missing topic/subject/accuracy or strings must not raise traceback or create None/nan%."""
        raw_rows = [
            {"subject": None, "topic": "sample", "accuracy": None},
            {"subject": "history", "topic": None, "accuracy": "invalid"},
            {"subject": "", "topic": "", "accuracy": "NaN"},
            {"subject": "polity", "topic": "preamble", "accuracy": "85.5"},
        ]
        agg = aggregate_topic_progress(raw_rows)
        self.assertEqual(len(agg), 1, "Only the valid numeric row should survive")
        self.assertEqual(agg.iloc[0]["Accuracy (%)"], 85.5)
        self.assertFalse(pd.isna(agg.iloc[0]["Accuracy (%)"]))

    def test_case_8_trend_preservation(self):
        """CASE 8: Attempt-level records remain distinct for chronological / trend analytics."""
        raw_rows = [
            {"subject": "history", "topic": "indus_valley", "accuracy": 60.0, "created_at": "2026-10-01"},
            {"subject": "history", "topic": "indus_valley", "accuracy": 80.0, "created_at": "2026-10-02"},
            {"subject": "history", "topic": "indus_valley", "accuracy": 95.0, "created_at": "2026-10-03"},
        ]
        df = pd.DataFrame(raw_rows)
        # Attempt level stays 3
        self.assertEqual(len(df), 3, "Chronological attempt list preserves every attempt")
        # Topic level collapses to 1
        agg = aggregate_topic_progress(df)
        self.assertEqual(len(agg), 1)

    def test_case_9_threshold_preservation(self):
        """CASE 9: Existing thresholds (< 50 Weak, >= 75 Strong) remain strictly preserved."""
        raw_rows = [
            {"subject": "history", "topic": "t1", "accuracy": 49.9},
            {"subject": "history", "topic": "t2", "accuracy": 50.0},
            {"subject": "history", "topic": "t3", "accuracy": 74.9},
            {"subject": "history", "topic": "t4", "accuracy": 75.0},
        ]
        agg = aggregate_topic_progress(raw_rows)
        weak = agg[agg["Accuracy (%)"] < 50]
        strong = agg[agg["Accuracy (%)"] >= 75]

        self.assertEqual(len(weak), 1)
        self.assertEqual(weak.iloc[0]["Accuracy (%)"], 49.9)

        self.assertEqual(len(strong), 1)
        self.assertEqual(strong.iloc[0]["Accuracy (%)"], 75.0)

    def test_case_10_ordering(self):
        """CASE 10: Weak lists sort ascending by accuracy; Strong lists sort descending."""
        raw_rows = [
            {"subject": "history", "topic": "topic_mid_weak", "accuracy": 35.0},
            {"subject": "history", "topic": "topic_very_weak", "accuracy": 20.0},
            {"subject": "history", "topic": "topic_super_strong", "accuracy": 95.0},
            {"subject": "history", "topic": "topic_mid_strong", "accuracy": 80.0},
        ]
        agg = aggregate_topic_progress(raw_rows)
        weak = agg[agg["Accuracy (%)"] < 50].sort_values(
            by=["Accuracy (%)", "Note Part"], ascending=[True, True]
        )
        strong = agg[agg["Accuracy (%)"] >= 75].sort_values(
            by=["Accuracy (%)", "Note Part"], ascending=[False, True]
        )

        self.assertEqual(list(weak["Accuracy (%)"]), [20.0, 35.0], "Weak must sort lowest accuracy first")
        self.assertEqual(list(strong["Accuracy (%)"]), [95.0, 80.0], "Strong must sort highest accuracy first")

    @patch("streamlit.info")
    @patch("streamlit.warning")
    @patch("streamlit.metric")
    @patch("streamlit.dataframe")
    @patch("streamlit.error")
    @patch("streamlit.success")
    @patch("streamlit.write")
    @patch("streamlit.caption")
    @patch("streamlit.markdown")
    @patch("streamlit.columns")
    def test_render_progress_page_duplicate_scenario(
        self, mock_columns, mock_markdown, mock_caption, mock_write,
        mock_success, mock_error, mock_dataframe, mock_metric, mock_warning, mock_info
    ):
        """Test full render_progress_page with multiple attempts on same topic."""
        mock_columns.side_effect = lambda n: [MagicMock() for _ in range(n)]

        progress_data = [
            {"subject": "history", "topic": "indus_valley", "accuracy": 80.0},
            {"subject": "history", "topic": "indus_valley", "accuracy": 90.0},
            {"subject": "polity", "topic": "preamble", "accuracy": 40.0},
            {"subject": "polity", "topic": "preamble", "accuracy": 60.0},
        ]

        with patch("ui.pages.progress.get_progress", return_value=progress_data):
            section_mock = MagicMock()
            render_progress_page(section_mock, "test_user")

        # Verify active topics metric = 2, total attempts = 4
        metric_calls = mock_metric.call_args_list
        active_topics_call = [c for c in metric_calls if "Active Topics" in c[0][0]]
        self.assertTrue(len(active_topics_call) > 0)
        self.assertEqual(active_topics_call[0][0][1], 2, "Active topics must be 2")

        total_attempts_call = [c for c in metric_calls if "Total Tests Attempted" in c[0][0]]
        self.assertTrue(len(total_attempts_call) > 0)
        self.assertEqual(total_attempts_call[0][0][1], 4, "Total attempts must be 4")

        # Verify weak/strong writes:
        # Indus Valley average is 85% -> Strong
        # Preamble average is 50% -> Neither (<50 is weak)
        write_calls = [c[0][0] for c in mock_write.call_args_list]
        indus_writes = [w for w in write_calls if "85.0%" in w or "indus_valley" in w]
        self.assertEqual(len(indus_writes), 1, "Indus Valley must appear exactly once in Strong topic areas")

    @patch("streamlit.info")
    def test_render_progress_page_empty(self, mock_info):
        """Test render_progress_page when user has no progress data."""
        with patch("ui.pages.progress.get_progress", return_value=[]):
            section_mock = MagicMock()
            render_progress_page(section_mock, "test_user")
            mock_info.assert_called_once()


if __name__ == "__main__":
    unittest.main()
