"""
Unit tests for Mock Intelligence UI Truth and Rendering (P0 Batch 4).
Verifies:
1. Zero-mock intentional empty / Not Assessed presentation
2. Raw Python dict protection in time_analysis and mistake/strength rendering
3. Section-wise HTML structural integrity (no literal </div> or markdown codeblock bleed)
4. Valid single and multi-mock data rendering
5. Partial / missing optional field resilience
6. None-value resilience (no None%, int(None), float(None))
7. UI safety (no internal IDs, file paths, raw dict/list representations)
"""
import html
import re
import unittest
from unittest.mock import MagicMock, patch

from ui.components.cards import (
    mock_hero_card_html,
    mock_mistakes_strengths_html,
    mock_qtype_performance_html,
    mock_time_analysis_card_html,
)
from ui.mock_intelligence.dashboard import render_mock_intelligence_dashboard


class TestMockIntelligenceUITruth(unittest.TestCase):

    # =========================================================================
    # CASE 1: ZERO MOCKS (mock_count = 0 / empty mock history)
    # =========================================================================
    def test_case_1_zero_mock_intentional_empty_state(self):
        """Zero mocks must show intentional Not Assessed state without fake accuracy or raw dict."""
        zero_mock_data = {
            "overall_accuracy": None,
            "mock_level": "No Mock History",
            "has_mock_history": False,
            "is_eligible": False,
            "time_per_question": None,
            "attempt_rate": 0,
            "correct_vs_wrong": {"correct": 0, "wrong": 0},
            "section_performance": [],
            "question_types": [],
            "mistakes": [],
            "strengths": [],
            "mistake_breakdown": {},
            "time_analysis": {
                "fastest_section": "N/A",
                "fastest_time": "N/A",
                "slowest_section": "N/A",
                "slowest_time": "N/A",
                "recommendation": "Complete a Mock or Grand Test to generate behavioral analysis.",
            },
            "summary": "No mock test history available. Complete a Mock or Grand Test to generate behavioral analysis.",
            "slowest_section": "N/A",
            "weakest_qtype": "N/A",
        }

        # 1. Hero Card
        hero = mock_hero_card_html(zero_mock_data).markup
        self.assertIn("--", hero)
        self.assertIn("Not assessed", hero)
        self.assertNotIn("0% Attempt Rate", hero)
        self.assertNotIn("{'", hero)
        self.assertNotIn("</div>\n```", hero)

        # Must not fabricate a mock score
        self.assertNotIn(">0%<", hero)
        self.assertNotIn(">65%<", hero)
        self.assertNotIn(">85%<", hero)

        # 2. Time Analysis Card
        time_card = mock_time_analysis_card_html(zero_mock_data).markup
        self.assertIn("Not assessed", time_card)
        self.assertIn("No mock tests attempted yet", time_card)
        self.assertNotIn("{'", time_card)
        self.assertNotIn("fastest_section", time_card)

        # 3. QTypes Card
        qtype_card = mock_qtype_performance_html(zero_mock_data["question_types"]).markup
        self.assertIn("Not assessed", qtype_card)
        self.assertIn("No question type behavioral data recorded yet", qtype_card)

        # 4. Mistakes & Strengths Card
        ms_card = mock_mistakes_strengths_html(zero_mock_data["mistakes"], zero_mock_data["strengths"]).markup
        self.assertIn("No mistake patterns detected yet", ms_card)
        self.assertIn("No observed exam strengths yet", ms_card)
        self.assertNotIn("{'", ms_card)

    # =========================================================================
    # CASE 2: RAW DICT PROTECTION
    # =========================================================================
    def test_case_2_raw_dict_protection_in_time_analysis(self):
        """Structured dictionary in time_analysis must never be rendered via str(dict)."""
        engine_dict_data = {
            "has_mock_history": False,
            "time_per_question": None,
            "time_analysis": {
                "fastest_section": "N/A",
                "fastest_time": "N/A",
                "slowest_section": "N/A",
                "slowest_time": "N/A",
                "recommendation": "Complete a Mock or Grand Test to generate behavioral analysis.",
            },
        }

        rendered = mock_time_analysis_card_html(engine_dict_data).markup

        # Check for dict string patterns
        self.assertNotIn("{'", rendered)
        self.assertNotIn("'recommendation':", rendered)
        self.assertNotIn("'fastest_section':", rendered)
        self.assertNotIn("{}", rendered)
        # Check clean learner-facing advice
        self.assertIn("No mock tests attempted yet", rendered)

    def test_case_2_raw_dict_protection_with_non_zero_mock_dict(self):
        """Structured dictionary for non-zero mock must be parsed into clean text."""
        engine_dict_data = {
            "has_mock_history": True,
            "time_per_question": 55,
            "time_analysis": {
                "fastest_section": "Aptitude",
                "fastest_time": "45s / question",
                "slowest_section": "History",
                "slowest_time": "65s / question",
                "recommendation": "Maintain steady pace on Aptitude.",
            },
        }

        rendered = mock_time_analysis_card_html(engine_dict_data).markup

        self.assertNotIn("{'", rendered)
        self.assertNotIn("'fastest_section':", rendered)
        self.assertIn("Fastest: Aptitude (45s / question)", rendered)
        self.assertIn("Slowest: History (65s / question)", rendered)
        self.assertIn("Maintain steady pace on Aptitude.", rendered)

    # =========================================================================
    # CASE 3: EMPTY SECTION DATA & HTML STRUCTURAL INTEGRITY
    # =========================================================================
    def test_case_3_empty_section_data_no_literal_html(self):
        """Empty section performance must render clean empty state without literal </div>."""
        mock_data = {
            "overall_accuracy": None,
            "mock_level": "No Mock History",
            "has_mock_history": False,
            "section_performance": [],
            "question_types": [],
            "mistakes": [],
            "strengths": [],
            "summary": "No mock test history available.",
        }

        with patch("streamlit.html") as mock_html, \
             patch("streamlit.columns", return_value=(MagicMock(), MagicMock())), \
             patch("streamlit.write"), \
             patch("core.user_context.UserContext.get_or_create", return_value=MagicMock()), \
             patch("ui.mock_intelligence.dashboard.get_mock_intelligence", return_value=mock_data):
            render_mock_intelligence_dashboard(user="test_fresh_user")

            # Collect all html calls
            html_calls = [call[0][0] for call in mock_html.call_args_list if call[0]]
            all_rendered_html = "\n".join(html_calls)

            # Assert intentional empty state for section performance
            self.assertIn("Section Performance: Not assessed", all_rendered_html)
            self.assertIn("No mock tests attempted yet", all_rendered_html)

            # Assert no markdown codeblock indentation artifact
            self.assertNotIn("```", all_rendered_html)
            self.assertNotIn("&lt;/div&gt;", all_rendered_html)

            # Ensure all <div> tags are balanced
            div_open_count = all_rendered_html.count("<div")
            div_close_count = all_rendered_html.count("</div>")
            self.assertEqual(div_open_count, div_close_count, "All <div> tags must be properly closed")

    # =========================================================================
    # CASE 4: ONE VALID MOCK
    # =========================================================================
    def test_case_4_one_valid_mock_renders_correctly(self):
        """Single completed mock test renders real metrics and section analytics."""
        valid_mock_data = {
            "overall_accuracy": 72,
            "mock_level": "Stable",
            "has_mock_history": True,
            "is_eligible": True,
            "time_per_question": 55,
            "attempt_rate": 82,
            "correct_vs_wrong": {"correct": 72, "wrong": 28, "skipped": 0},
            "section_performance": [
                {"subject": "Polity", "accuracy": 72, "avg_time_sec": 55, "status": "Stable"}
            ],
            "question_types": [
                {"type": "Direct Concept", "accuracy": 75}
            ],
            "mistakes": [
                {"pattern": "Time Management Under Timed Conditions", "frequency": "Medium", "impact": "-5 Marks"}
            ],
            "strengths": [
                {"behavior": "Consistent Question Selection Flow", "advantage": "+5 Mins Saved"}
            ],
            "time_analysis": {
                "fastest_section": "Polity",
                "fastest_time": "55s / question",
                "slowest_section": "Polity",
                "slowest_time": "55s / question",
                "recommendation": "Maintain steady pace on Polity.",
            },
            "summary": "Mock performance is stable (72% accuracy, 82% attempt rate).",
        }

        # Hero
        hero = mock_hero_card_html(valid_mock_data).markup
        self.assertIn("72%", hero)
        self.assertIn("82% Attempt Rate", hero)
        self.assertIn("Stable", hero)
        self.assertIn("Correct: 72%", hero)

        # Time
        time_card = mock_time_analysis_card_html(valid_mock_data).markup
        self.assertIn("Avg 55 sec / Question", time_card)
        self.assertIn("Maintain steady pace on Polity.", time_card)

        # Mistakes & Strengths
        ms_card = mock_mistakes_strengths_html(valid_mock_data["mistakes"], valid_mock_data["strengths"]).markup
        self.assertIn("Time Management Under Timed Conditions", ms_card)
        self.assertIn("-5 Marks", ms_card)
        self.assertIn("Consistent Question Selection Flow", ms_card)
        self.assertIn("+5 Mins Saved", ms_card)
        self.assertNotIn("{'", ms_card)

        # Dashboard rendering with mock data
        with patch("streamlit.html") as mock_html, \
             patch("streamlit.columns", return_value=(MagicMock(), MagicMock())), \
             patch("streamlit.write"), \
             patch("core.user_context.UserContext.get_or_create", return_value=MagicMock()), \
             patch("ui.mock_intelligence.dashboard.get_mock_intelligence", return_value=valid_mock_data):
            render_mock_intelligence_dashboard(user="learner_with_1_mock")

            html_calls = [call[0][0] for call in mock_html.call_args_list if call[0]]
            all_html = "\n".join(html_calls)
            self.assertIn("Polity", all_html)
            self.assertIn("72%", all_html)
            self.assertIn("55s/Q", all_html)
            self.assertIn("Direct Concept", all_html)

    # =========================================================================
    # CASE 5: MULTIPLE VALID MOCKS
    # =========================================================================
    def test_case_5_multiple_valid_mocks(self):
        """Multiple mock exams preserve subject breakdown and comparative pace analysis."""
        multi_mock_data = {
            "overall_accuracy": 84,
            "mock_level": "Exceptional",
            "has_mock_history": True,
            "is_eligible": True,
            "time_per_question": 48,
            "attempt_rate": 94,
            "correct_vs_wrong": {"correct": 84, "wrong": 12, "skipped": 4},
            "section_performance": [
                {"subject": "History", "accuracy": 90, "avg_time_sec": 42, "status": "Strong"},
                {"subject": "Polity", "accuracy": 85, "avg_time_sec": 46, "status": "Strong"},
                {"subject": "Geography", "accuracy": 78, "avg_time_sec": 52, "status": "Strong"},
                {"subject": "Aptitude", "accuracy": 82, "avg_time_sec": 54, "status": "Strong"},
            ],
            "question_types": [
                {"type": "Direct Concept", "accuracy": 92},
                {"type": "Chronology", "accuracy": 80},
                {"type": "Match the Following", "accuracy": 85},
            ],
            "mistakes": [
                {"pattern": "Calculation Check in Aptitude", "impact": "-2 Marks"}
            ],
            "strengths": [
                {"behavior": "High Speed in History and Polity", "advantage": "+8 Mins Saved"},
                {"behavior": "High Elimination Precision", "advantage": "+10 Marks"}
            ],
            "time_analysis": {
                "fastest_section": "History",
                "fastest_time": "42s / question",
                "slowest_section": "Aptitude",
                "slowest_time": "54s / question",
                "recommendation": "Maintain exceptional speed on History while securing Aptitude precision.",
            },
            "summary": "Mock performance is exceptional (84% accuracy, 94% attempt rate).",
        }

        with patch("streamlit.html") as mock_html, \
             patch("streamlit.columns", return_value=(MagicMock(), MagicMock())), \
             patch("streamlit.write"), \
             patch("core.user_context.UserContext.get_or_create", return_value=MagicMock()), \
             patch("ui.mock_intelligence.dashboard.get_mock_intelligence", return_value=multi_mock_data):
            render_mock_intelligence_dashboard(user="pro_learner")

            html_calls = [call[0][0] for call in mock_html.call_args_list if call[0]]
            all_html = "\n".join(html_calls)

            # All subjects visible
            self.assertIn("History", all_html)
            self.assertIn("Polity", all_html)
            self.assertIn("Geography", all_html)
            self.assertIn("Aptitude", all_html)

            # Accuracy and pace visible
            self.assertIn("90%", all_html)
            self.assertIn("42s/Q", all_html)

            # No raw dicts anywhere
            self.assertNotIn("{'", all_html)
            self.assertNotIn("<div>\n    \n</div>", all_html)

    # =========================================================================
    # CASE 6: PARTIAL / MISSING OPTIONAL FIELDS
    # =========================================================================
    def test_case_6_partial_missing_optional_fields_no_traceback(self):
        """Missing optional fields must render gracefully without traceback or fake numeric fallback."""
        sparse_data = {
            # overall_accuracy missing
            # attempt_rate missing
            # time_per_question missing
            "has_mock_history": False,
        }

        # Cards must render safely without crashing
        hero = mock_hero_card_html(sparse_data).markup
        self.assertIn("--", hero)
        self.assertIn("Not assessed", hero)

        time_card = mock_time_analysis_card_html(sparse_data).markup
        self.assertIn("Not assessed", time_card)

        qtype = mock_qtype_performance_html([]).markup
        self.assertIn("Not assessed", qtype)

        ms = mock_mistakes_strengths_html([], []).markup
        self.assertIn("No mistake patterns", ms)

        # Empty dict should also work
        empty_hero = mock_hero_card_html({}).markup
        self.assertIn("--", empty_hero)
        empty_time = mock_time_analysis_card_html({}).markup
        self.assertIn("Not assessed", empty_time)

    # =========================================================================
    # CASE 7: NONE VALUES RESILIENCE
    # =========================================================================
    def test_case_7_none_values_resilience(self):
        """Explicit None values must not render None%, int(None) crash, or raw 'None' text."""
        none_data = {
            "overall_accuracy": None,
            "mock_level": None,
            "has_mock_history": False,
            "time_per_question": None,
            "attempt_rate": None,
            "correct_vs_wrong": {"correct": None, "wrong": None, "skipped": None},
            "section_performance": [
                {"subject": "Tamil", "accuracy": None, "avg_time_sec": None}
            ],
            "question_types": [
                {"type": "Assertion", "accuracy": None}
            ],
            "mistakes": [None],
            "strengths": [None],
            "time_analysis": None,
            "summary": None,
        }

        hero = mock_hero_card_html(none_data).markup
        self.assertNotIn("None%", hero)
        self.assertNotIn("None Attempt Rate", hero)
        self.assertIn("--", hero)

        time_card = mock_time_analysis_card_html(none_data).markup
        self.assertNotIn("None sec", time_card)
        self.assertIn("Not assessed", time_card)

        qtype = mock_qtype_performance_html(none_data["question_types"]).markup
        self.assertNotIn("None%", qtype)
        self.assertIn("Not assessed", qtype)

        # Render full dashboard with None values
        with patch("streamlit.html") as mock_html, \
             patch("streamlit.columns", return_value=(MagicMock(), MagicMock())), \
             patch("streamlit.write"), \
             patch("core.user_context.UserContext.get_or_create", return_value=MagicMock()), \
             patch("ui.mock_intelligence.dashboard.get_mock_intelligence", return_value=none_data):
            render_mock_intelligence_dashboard(user="none_user")

            html_calls = [call[0][0] for call in mock_html.call_args_list if call[0]]
            all_html = "\n".join(html_calls)
            self.assertNotIn("None%", all_html)
            self.assertNotIn("None/Q", all_html)
            self.assertNotIn("{'", all_html)

    # =========================================================================
    # CASE 8: UI SAFETY (NO INTERNAL IDS, PATHS, RAW DICT/LIST)
    # =========================================================================
    def test_case_8_ui_safety_no_leakage(self):
        """Rendered output must not expose raw Python dicts, raw lists, internal IDs, or file paths."""
        test_payloads = [
            # Zero mock payload
            {
                "overall_accuracy": None,
                "has_mock_history": False,
                "section_performance": [],
                "question_types": [],
                "mistakes": [],
                "strengths": [],
                "time_analysis": {"fastest_section": "N/A", "recommendation": "Test rec"},
                "summary": "No mocks attempted.",
            },
            # Non-zero mock payload with nested structures
            {
                "overall_accuracy": 75,
                "has_mock_history": True,
                "time_per_question": 60,
                "attempt_rate": 85,
                "correct_vs_wrong": {"correct": 75, "wrong": 25},
                "section_performance": [{"subject": "Science", "accuracy": 75, "avg_time_sec": 60}],
                "question_types": [{"type": "Numerical", "accuracy": 70}],
                "mistakes": [{"pattern": "Formula recall", "frequency": "Low"}],
                "strengths": [{"behavior": "Quick reading", "advantage": "+3 mins"}],
                "time_analysis": {"fastest_section": "Science", "recommendation": "Good pace"},
                "summary": "Solid mock performance.",
            },
        ]

        for payload in test_payloads:
            with patch("streamlit.html") as mock_html, \
                 patch("streamlit.columns", return_value=(MagicMock(), MagicMock())), \
                 patch("streamlit.write"), \
                 patch("core.user_context.UserContext.get_or_create", return_value=MagicMock()), \
                 patch("ui.mock_intelligence.dashboard.get_mock_intelligence", return_value=payload):
                render_mock_intelligence_dashboard(user="safety_user")

                html_calls = [call[0][0] for call in mock_html.call_args_list if call[0]]
                combined = "\n".join(html_calls)

                # No raw Python dicts
                self.assertIsNone(re.search(r"\{'[a-zA-Z0-9_]+':", combined), "Raw Python dict must not be rendered")

                # No raw Python lists
                self.assertIsNone(re.search(r"\['[a-zA-Z0-9_]+'\]", combined), "Raw Python list must not be rendered")

                # No file paths
                self.assertNotIn("c:\\", combined.lower())
                self.assertNotIn("/home/", combined.lower())
                self.assertNotIn(".py", combined.lower())

                # No internal IDs
                self.assertNotIn("node_id", combined)
                self.assertNotIn("builder_metadata", combined)
                self.assertNotIn("trap_id", combined)


if __name__ == "__main__":
    unittest.main()
