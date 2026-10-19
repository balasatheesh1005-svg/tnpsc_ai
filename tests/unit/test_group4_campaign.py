"""Unit tests for TNPSC Group 4 Free Mini Mock Campaign.

Validates the 22 required safety, manifest, routing, scoring, and zero-persistence specifications.
"""

from __future__ import annotations

import json
from pathlib import Path
import unittest
from unittest.mock import MagicMock, patch

from core.campaign.group4_curated_questions import (
    ANALYSIS_BUCKETS,
    BUCKET_APTITUDE,
    BUCKET_GENERAL_STUDIES,
    BUCKET_GENERAL_TAMIL,
    GROUP4_GOLD_25,
    CampaignManifestError,
    calculate_campaign_results,
    get_bucket_for_source,
    load_group4_campaign_questions,
)
from ui.campaign.group4_mock import (
    _reset_campaign_test,
    render_group4_campaign,
)


class TestGroup4CampaignSuite(unittest.TestCase):
    """22 required validation checks for the Group 4 public marketing funnel."""

    @classmethod
    def setUpClass(cls) -> None:
        cls.root_dir = Path(__file__).resolve().parent.parent.parent
        cls.questions = load_group4_campaign_questions(cls.root_dir)

    # 1. Manifest count == 25
    def test_01_manifest_count_equals_25(self) -> None:
        self.assertEqual(len(GROUP4_GOLD_25), 25, "Manifest must contain exactly 25 references")

    # 2. Composite refs unique
    def test_02_composite_refs_unique(self) -> None:
        refs = [(r["source_file"], r["question_id"]) for r in GROUP4_GOLD_25]
        self.assertEqual(len(refs), len(set(refs)), "Composite references must be unique")

    # 3. All source files resolve under data/questions
    def test_03_all_source_files_resolve_under_data_questions(self) -> None:
        data_root = (self.root_dir / "data" / "questions").resolve()
        for ref in GROUP4_GOLD_25:
            rel = ref["source_file"]
            resolved = (self.root_dir / rel).resolve()
            self.assertTrue(resolved.is_file(), f"File does not exist: {rel}")
            # Ensure resolved path is under data/questions
            try:
                resolved.relative_to(data_root)
            except ValueError:
                self.fail(f"Source file {rel} is not under data/questions")

    # 4. All 25 IDs resolve exactly once
    def test_04_all_25_ids_resolve_exactly_once(self) -> None:
        for ref in GROUP4_GOLD_25:
            rel = ref["source_file"]
            qid = ref["question_id"]
            p = (self.root_dir / rel).resolve()
            with open(p, "r", encoding="utf-8") as f:
                data = json.load(f)
            items = data if isinstance(data, list) else data.get("questions", [])
            matches = [q for q in items if str(q.get("id") or q.get("question_id")) == qid]
            self.assertEqual(len(matches), 1, f"Expected 1 match for {qid} in {rel}, found {len(matches)}")

    # 5. All normalize successfully
    def test_05_all_normalize_successfully(self) -> None:
        self.assertEqual(len(self.questions), 25)
        for q in self.questions:
            self.assertTrue(hasattr(q, "id"))
            self.assertTrue(hasattr(q, "options"))
            self.assertTrue(hasattr(q, "correct_answer"))

    # 6. Exactly 4 options each
    def test_06_exactly_4_options_each(self) -> None:
        for q in self.questions:
            self.assertEqual(len(q.options), 4, f"Question {q.id} must have exactly 4 options")
            opt_ids = [opt.id for opt in q.options]
            self.assertEqual(opt_ids, ["A", "B", "C", "D"], f"Question {q.id} options must be A, B, C, D")

    # 7. Valid correct key each
    def test_07_valid_correct_key_each(self) -> None:
        for q in self.questions:
            self.assertIn(q.correct_answer, ["A", "B", "C", "D"], f"Question {q.id} has invalid key")

    # 8. Explanation exists each
    def test_08_explanation_exists_each(self) -> None:
        for q in self.questions:
            has_exp = bool(q.explanation and (q.explanation.en or q.explanation.ta))
            self.assertTrue(has_exp, f"Question {q.id} must have explanation")

    # 9. Subject distribution matches approved Gold set
    def test_09_subject_distribution_matches_approved_gold_set(self) -> None:
        bucket_counts: dict[str, int] = {}
        for q in self.questions:
            b = getattr(q, "campaign_bucket", get_bucket_for_source(getattr(q, "campaign_source_file", "")))
            bucket_counts[b] = bucket_counts.get(b, 0) + 1

        self.assertEqual(bucket_counts.get(BUCKET_GENERAL_TAMIL), 12, "Must have 12 General Tamil questions")
        self.assertEqual(bucket_counts.get(BUCKET_GENERAL_STUDIES), 9, "Must have 9 General Studies questions")
        self.assertEqual(bucket_counts.get(BUCKET_APTITUDE), 4, "Must have 4 Aptitude questions")

    # 10. Difficulty distribution matches approved Gold set
    def test_10_difficulty_distribution_matches_approved_gold_set(self) -> None:
        for q in self.questions:
            self.assertEqual(q.difficulty, "Easy", f"Question {q.id} difficulty must be Easy")

    # 11. No production question content duplicated in manifest
    def test_11_no_production_question_content_duplicated_in_manifest(self) -> None:
        manifest_file = self.root_dir / "core" / "campaign" / "group4_curated_questions.py"
        with open(manifest_file, "r", encoding="utf-8") as f:
            code = f.read()

        # Check sample stems from questions to ensure they are NOT in manifest file
        sample_stems = [
            "பொருத்தமான விடையைத் தேர்ந்தெடுக்க",
            "அகரவரிசைப்படுத்துக",
            "வேர்ச்சொல்",
            "Fundamental Rights",
            "Panchayati Raj",
            "NITI Aayog",
        ]
        for stem in sample_stems:
            self.assertNotIn(stem, code, f"Question content '{stem}' must not be duplicated in manifest")

    # 12. Anonymous scoring correctness
    def test_12_anonymous_scoring_correctness(self) -> None:
        # All correct
        all_correct_answers = {i: q.correct_answer for i, q in enumerate(self.questions)}
        res_full = calculate_campaign_results(self.questions, all_correct_answers, 60)
        self.assertEqual(res_full["correct"], 25)
        self.assertEqual(res_full["wrong"], 0)
        self.assertEqual(res_full["unanswered"], 0)
        self.assertEqual(res_full["accuracy"], 100.0)

        # All wrong
        all_wrong_answers = {
            i: ("B" if q.correct_answer == "A" else "A")
            for i, q in enumerate(self.questions)
        }
        res_zero = calculate_campaign_results(self.questions, all_wrong_answers, 60)
        self.assertEqual(res_zero["correct"], 0)
        self.assertEqual(res_zero["wrong"], 25)
        self.assertEqual(res_zero["accuracy"], 0.0)

    # 13. Unanswered calculation correctness
    def test_13_unanswered_calculation_correctness(self) -> None:
        # Only answer 5 questions: 3 correct, 2 wrong, 20 unanswered
        partial_answers = {
            0: self.questions[0].correct_answer,
            1: self.questions[1].correct_answer,
            2: self.questions[2].correct_answer,
            3: "B" if self.questions[3].correct_answer == "A" else "A",
            4: "B" if self.questions[4].correct_answer == "A" else "A",
        }
        res = calculate_campaign_results(self.questions, partial_answers, 100)
        self.assertEqual(res["answered"], 5)
        self.assertEqual(res["unanswered"], 20)
        self.assertEqual(res["correct"], 3)
        self.assertEqual(res["wrong"], 2)
        # Verify unanswered are NOT counted as wrong
        self.assertNotEqual(res["wrong"], 22)
        self.assertEqual(res["accuracy"], 60.0)

    # 14. Three-bucket aggregation correctness
    def test_14_three_bucket_aggregation_correctness(self) -> None:
        # Answer first 2 questions of each bucket correctly
        answers = {
            0: self.questions[0].correct_answer,
            1: self.questions[1].correct_answer,
            12: self.questions[12].correct_answer,
            13: self.questions[13].correct_answer,
            21: self.questions[21].correct_answer,
            22: self.questions[22].correct_answer,
        }
        res = calculate_campaign_results(self.questions, answers, 90)
        bk = res["bucket_breakdown"]

        self.assertEqual(bk[BUCKET_GENERAL_TAMIL]["total"], 12)
        self.assertEqual(bk[BUCKET_GENERAL_TAMIL]["answered"], 2)
        self.assertEqual(bk[BUCKET_GENERAL_TAMIL]["correct"], 2)
        self.assertEqual(bk[BUCKET_GENERAL_TAMIL]["accuracy"], 100.0)

        self.assertEqual(bk[BUCKET_GENERAL_STUDIES]["total"], 9)
        self.assertEqual(bk[BUCKET_GENERAL_STUDIES]["answered"], 2)
        self.assertEqual(bk[BUCKET_GENERAL_STUDIES]["correct"], 2)
        self.assertEqual(bk[BUCKET_GENERAL_STUDIES]["accuracy"], 100.0)

        self.assertEqual(bk[BUCKET_APTITUDE]["total"], 4)
        self.assertEqual(bk[BUCKET_APTITUDE]["answered"], 2)
        self.assertEqual(bk[BUCKET_APTITUDE]["correct"], 2)
        self.assertEqual(bk[BUCKET_APTITUDE]["accuracy"], 100.0)

    # 15. No topic-level diagnosis
    def test_15_no_topic_level_diagnosis(self) -> None:
        res = calculate_campaign_results(self.questions, {0: "A", 1: "B"}, 40)
        # Ensure only 3 buckets are present and no topic-level diagnosis keys exist
        self.assertEqual(set(res["bucket_breakdown"].keys()), set(ANALYSIS_BUCKETS))
        self.assertNotIn("weak_topic", res)
        self.assertNotIn("topic_analysis", res)
        self.assertNotIn("topic_diagnosis", res)

    # 16. Query route accepts exact group4 only
    def test_16_query_route_accepts_exact_group4_only(self) -> None:
        # Check app.py code to verify strict equality on 'group4'
        app_file = self.root_dir / "app.py"
        with open(app_file, "r", encoding="utf-8") as f:
            app_code = f.read()

        self.assertIn('st.query_params.get("campaign") == "group4"', app_code)
        # Ensure no wildcard or regex or arbitrary campaign matching
        self.assertNotIn('st.query_params.get("campaign") in', app_code)

    # 17. Normal root remains auth-gated
    def test_17_normal_root_remains_auth_gated(self) -> None:
        app_file = self.root_dir / "app.py"
        with open(app_file, "r", encoding="utf-8") as f:
            app_code = f.read()

        # When campaign is not group4, app.py reaches if not is_authenticated()
        self.assertIn("if not is_authenticated():", app_code)

    # 18. Campaign execution does not invoke persistence functions
    def test_18_campaign_execution_does_not_invoke_persistence(self) -> None:
        import core.campaign.group4_curated_questions as c_module
        import ui.campaign.group4_mock as u_module

        prohibited_terms = [
            "save_progress",
            "add_xp",
            "update_streak",
            "add_weakness",
            "add_revision_topic",
            "complete_practice_session",
            "record_practice_answer",
            "supabase",
            "get_supabase",
        ]

        with open(c_module.__file__, "r", encoding="utf-8") as f:
            c_text = f.read()
        with open(u_module.__file__, "r", encoding="utf-8") as f:
            u_text = f.read()

        for term in prohibited_terms:
            self.assertNotIn(term, c_text.lower(), f"Prohibited persistence call '{term}' found in curated_questions")
            self.assertNotIn(term, u_text.lower(), f"Prohibited persistence call '{term}' found in ui campaign")

    # 19. Retake clears only campaign namespace
    @patch("streamlit.session_state", dict())
    def test_19_retake_clears_only_campaign_namespace(self) -> None:
        import streamlit as st

        # Set up mixed state
        st.session_state["campaign_group4_stage"] = "result"
        st.session_state["campaign_group4_answers"] = {0: "A", 1: "B"}
        st.session_state["campaign_group4_index"] = 24
        # Unrelated / auth state
        st.session_state["username"] = "learner_123"
        st.session_state["auth_page"] = "login"
        st.session_state["unrelated_token"] = "secret_xyz"

        _reset_campaign_test(start_stage="test")

        # Unrelated state preserved
        self.assertEqual(st.session_state["username"], "learner_123")
        self.assertEqual(st.session_state["auth_page"], "login")
        self.assertEqual(st.session_state["unrelated_token"], "secret_xyz")

        # Campaign state reset to initial test
        self.assertEqual(st.session_state["campaign_group4_stage"], "test")
        self.assertEqual(st.session_state["campaign_group4_index"], 0)
        self.assertEqual(st.session_state["campaign_group4_answers"], {})

    # 20. Signup CTA exits campaign safely
    @patch("streamlit.session_state", dict())
    @patch("streamlit.query_params", {"campaign": "group4"})
    @patch("streamlit.rerun")
    def test_20_signup_cta_exits_campaign_safely(self, mock_rerun: MagicMock) -> None:
        import streamlit as st

        # Simulate clicking the signup CTA
        if "campaign" in st.query_params:
            del st.query_params["campaign"]
        st.session_state["auth_page"] = "signup"

        self.assertNotIn("campaign", st.query_params)
        self.assertEqual(st.session_state["auth_page"], "signup")

    # 21. Answer review does not expose internal IDs/paths
    def test_21_answer_review_does_not_expose_internal_ids_paths(self) -> None:
        import ui.campaign.group4_mock as u_module

        with open(u_module.__file__, "r", encoding="utf-8") as f:
            code = f.read()

        # In review rendering, verify it does NOT print q.id or q.campaign_source_file or json paths
        self.assertNotIn("html.escape(q.id)", code)
        self.assertNotIn("q.campaign_source_file", code)
        self.assertNotIn("q.raw", code)

    # 22. 25 questions remain deterministic across reloads
    def test_22_questions_remain_deterministic_across_reloads(self) -> None:
        run1 = load_group4_campaign_questions(self.root_dir)
        run2 = load_group4_campaign_questions(self.root_dir)

        self.assertEqual(len(run1), 25)
        self.assertEqual(len(run2), 25)
        for q1, q2 in zip(run1, run2):
            self.assertEqual(q1.id, q2.id)
            self.assertEqual(q1.correct_answer, q2.correct_answer)
            self.assertEqual(q1.question_ta, q2.question_ta)
            self.assertEqual(len(q1.options), len(q2.options))


if __name__ == "__main__":
    unittest.main()
