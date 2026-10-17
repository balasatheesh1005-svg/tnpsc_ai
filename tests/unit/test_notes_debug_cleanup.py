import unittest
from unittest.mock import MagicMock, patch
import streamlit as st

from ui.pages.notes import render_notes_page


class TestNotesDebugCleanup(unittest.TestCase):
    """
    Targeted test suite verifying that learner-facing debug metadata
    (CURRENT TOPIC, CURRENT PART, LOADED FILE, internal filesystem paths)
    is never emitted by the Study Notes page.
    """

    def _render_and_capture(self, subject, topic_id, repo_id, display_title, part_num=1, lang_mode="English"):
        st.session_state.clear()
        st.session_state["selected_subject"] = subject
        st.session_state["selected_topic_id"] = topic_id
        st.session_state["selected_repository_id"] = repo_id
        st.session_state["selected_display_title"] = display_title
        st.session_state[f"selected_part_{topic_id}"] = part_num
        st.session_state["notes_language_mode"] = lang_mode

        captions = []
        markdowns = []
        writes = []
        errors = []
        warnings = []

        with patch("streamlit.caption", side_effect=lambda t, *a, **kw: captions.append(str(t))), \
             patch("streamlit.markdown", side_effect=lambda t, *a, **kw: markdowns.append(str(t))), \
             patch("streamlit.write", side_effect=lambda t, *a, **kw: writes.append(str(t))), \
             patch("streamlit.error", side_effect=lambda t, *a, **kw: errors.append(str(t))), \
             patch("streamlit.warning", side_effect=lambda t, *a, **kw: warnings.append(str(t))), \
             patch("streamlit.info"), \
             patch("streamlit.button", return_value=False), \
             patch("streamlit.columns", side_effect=lambda n, **kw: [MagicMock() for _ in range(n if isinstance(n, int) else len(n))]), \
             patch("ui.pages.notes.render_notes") as mock_render:

            section = MagicMock()
            render_notes_page(section)

        all_rendered = " ".join(captions + markdowns + writes)
        return {
            "captions": captions,
            "markdowns": markdowns,
            "writes": writes,
            "errors": errors,
            "warnings": warnings,
            "all_text": all_rendered,
            "mock_render_called": mock_render.called,
        }

    def test_polity_historical_background_parts_1_to_4(self):
        """Verify Polity Historical Background parts 1-4 load properly and emit no debug strings."""
        for part in [1, 2, 3, 4]:
            res = self._render_and_capture(
                subject="polity",
                topic_id="historical_background",
                repo_id="historical_background",
                display_title="Historical Background",
                part_num=part,
            )
            self.assertTrue(res["mock_render_called"], f"Part {part} must invoke render_notes")
            self.assertEqual(len(res["errors"]), 0, f"Part {part} must render without error")

            # Check that none of the debug strings or paths appear anywhere in learner-facing UI
            self.assertNotIn("CURRENT TOPIC", res["all_text"])
            self.assertNotIn("CURRENT PART", res["all_text"])
            self.assertNotIn("LOADED FILE", res["all_text"])
            self.assertNotIn("data/notes/", res["all_text"])
            self.assertNotIn(".json", res["all_text"])

            # Verify specifically that captions do not include the old pin emoji debug line
            for cap in res["captions"]:
                self.assertNotIn("📌", cap)
                self.assertNotIn("CURRENT TOPIC", cap)

    def test_multi_subject_history(self):
        """Verify History notes render without debug metadata."""
        res = self._render_and_capture(
            subject="history",
            topic_id="history_indus_valley_civilization",
            repo_id="history_indus_valley_civilization",
            display_title="Indus Valley Civilization",
            part_num=1,
        )
        self.assertTrue(res["mock_render_called"])
        self.assertEqual(len(res["errors"]), 0)
        self.assertNotIn("CURRENT TOPIC", res["all_text"])
        self.assertNotIn("CURRENT PART", res["all_text"])
        self.assertNotIn("LOADED FILE", res["all_text"])
        self.assertNotIn("data/notes/", res["all_text"])

    def test_multi_subject_tamil_society(self):
        """Verify Tamil Society notes render without debug metadata."""
        res = self._render_and_capture(
            subject="tamil_society",
            topic_id="ts_archaeological_excavations_in_tamil_nadu",
            repo_id="ts_archaeological_excavations_in_tamil_nadu",
            display_title="Archaeological Excavations in Tamil Nadu",
            part_num=1,
        )
        self.assertTrue(res["mock_render_called"])
        self.assertEqual(len(res["errors"]), 0)
        self.assertNotIn("CURRENT TOPIC", res["all_text"])
        self.assertNotIn("CURRENT PART", res["all_text"])
        self.assertNotIn("LOADED FILE", res["all_text"])
        self.assertNotIn("data/notes/", res["all_text"])

    def test_language_modes_preserved(self):
        """Verify language modes (English, Tamil, Both) function without debug emissions."""
        for mode in ["English", "தமிழ்", "Both"]:
            res = self._render_and_capture(
                subject="polity",
                topic_id="historical_background",
                repo_id="historical_background",
                display_title="Historical Background",
                part_num=1,
                lang_mode=mode,
            )
            self.assertTrue(res["mock_render_called"])
            self.assertNotIn("CURRENT TOPIC", res["all_text"])
            self.assertNotIn("LOADED FILE", res["all_text"])

    def test_missing_topic_error_state(self):
        """Verify that missing topics display user-friendly warning without path leaks."""
        res = self._render_and_capture(
            subject="polity",
            topic_id="non_existent_topic",
            repo_id="non_existent_topic",
            display_title="Non Existent Topic",
        )
        self.assertFalse(res["mock_render_called"])
        self.assertTrue(len(res["warnings"]) > 0)
        self.assertIn("coming soon", res["warnings"][0])
        self.assertNotIn("data/notes/", res["all_text"])
        self.assertNotIn(".json", res["all_text"])


if __name__ == "__main__":
    unittest.main()
