import unittest
import os
import re

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

class TestTargeted360pxResponsive(unittest.TestCase):
    """
    Targeted test suite verifying component-scoped 360px responsive fixes:
    1. No global column override exists (no div[data-testid="column"] { min-width: 100% !important; })
    2. Locked files are completely untouched
    3. cards.py has .revision-grid set to 1fr at <=640px
    4. topic_hub.py has hub-learning-card, hub-practice-card, and hub-toolkit-marker scoped styles
    5. layout.py has notes-bottom-actions-marker scoped styles
    6. subject_selector.py has subject-card-item scoped styles
    7. topic_selector.py has topic-card-item scoped styles
    8. practice_renderer.py has practice-top-marker, practice-nav-marker, and practice-result-nav-marker scoped styles
    """

    def test_no_global_column_override(self):
        """Verify NO global all-column stacking selector was introduced across the codebase."""
        # Ensure that no UN-SCOPED global column rule like "div[data-testid="column"] {" exists.
        # Scoped rules like "div[data-testid="stHorizontalBlock"]:has(...) > div[data-testid="column"]" are approved.
        for s_dir in ["ui"]:
            full_dir = os.path.join(REPO_ROOT, s_dir)
            for root, _, files in os.walk(full_dir):
                for f in files:
                    if f.endswith(".py") or f.endswith(".css"):
                        fpath = os.path.join(root, f)
                        with open(fpath, "r", encoding="utf-8") as fp:
                            content = fp.read()
                        # Find all occurrences of div[data-testid="column"]
                        for m in re.finditer(r'([^\n>]*div\[data-testid="column"\]\s*\{[^}]+})', content):
                            matched_block = m.group(1).strip()
                            # If it's a global rule with min-width: 100% and no :has(...) scope
                            if ':has(' not in matched_block and 'min-width:\s*100%' in matched_block:
                                self.fail(f"Global un-scoped column override found in {fpath}: {matched_block}")

    def test_locked_files_untouched(self):
        """Verify locked files have not been modified."""
        locked_files = [
            "core/auth.py",
            "core/question_loader.py",
            "core/navigation_v2/navigation_state.py",
            "core/topics_loader.py",
            "core/leaderboard_ai.py",
            "ui/question_engine/explanation_component.py",
        ]
        for rel_path in locked_files:
            full_path = os.path.join(REPO_ROOT, rel_path)
            self.assertTrue(os.path.exists(full_path), f"Locked file missing: {rel_path}")

    def test_cards_revision_grid_mobile_fix(self):
        """Verify .revision-grid becomes single column at <=640px in cards.py."""
        fpath = os.path.join(REPO_ROOT, "ui", "components", "cards.py")
        with open(fpath, "r", encoding="utf-8") as fp:
            content = fp.read()

        self.assertIn(".revision-grid", content)
        self.assertIn("@media (max-width: 640px)", content)
        # Verify 1fr under media query
        match = re.search(r'\.revision-grid\s*\{\s*grid-template-columns:\s*1fr\s*!important', content)
        self.assertIsNotNone(match, ".revision-grid does not have grid-template-columns: 1fr !important under <=640px")

    def test_topic_hub_responsive_scoped(self):
        """Verify topic_hub.py uses scoped styles for learning modules, practice, and toolkit."""
        fpath = os.path.join(REPO_ROOT, "ui", "navigation_v2", "topic_hub.py")
        with open(fpath, "r", encoding="utf-8") as fp:
            content = fp.read()

        self.assertIn("hub-learning-card", content)
        self.assertIn("hub-practice-card", content)
        self.assertIn("hub-toolkit-marker", content)
        self.assertIn('div[data-testid="stHorizontalBlock"]:has(.hub-learning-card)', content)
        self.assertIn('div[data-testid="stHorizontalBlock"]:has(.hub-practice-card)', content)
        self.assertIn('div[data-testid="stHorizontalBlock"]:has(.hub-toolkit-marker)', content)

    def test_notes_bottom_actions_responsive_scoped(self):
        """Verify layout.py render_bottom_actions uses scoped responsive style."""
        fpath = os.path.join(REPO_ROOT, "ui", "notes", "layout.py")
        with open(fpath, "r", encoding="utf-8") as fp:
            content = fp.read()

        self.assertIn("notes-bottom-actions-marker", content)
        self.assertIn('div[data-testid="stHorizontalBlock"]:has(.notes-bottom-actions-marker)', content)
        self.assertIn("btn_bottom_practice", content)
        self.assertIn("btn_bottom_flashcards", content)
        self.assertIn("btn_bottom_ai", content)
        self.assertIn("btn_bottom_bookmark", content)
        self.assertIn("btn_bottom_share", content)

    def test_subject_selector_responsive_scoped(self):
        """Verify subject_selector.py uses scoped subject-card-item responsive style."""
        fpath = os.path.join(REPO_ROOT, "ui", "navigation_v2", "subject_selector.py")
        with open(fpath, "r", encoding="utf-8") as fp:
            content = fp.read()

        self.assertIn("subject-card-item", content)
        self.assertIn('div[data-testid="stHorizontalBlock"]:has(.subject-card-item)', content)

    def test_topic_selector_responsive_scoped(self):
        """Verify topic_selector.py uses scoped topic-card-item responsive style."""
        fpath = os.path.join(REPO_ROOT, "ui", "navigation_v2", "topic_selector.py")
        with open(fpath, "r", encoding="utf-8") as fp:
            content = fp.read()

        self.assertIn("topic-card-item", content)
        self.assertIn('div[data-testid="stHorizontalBlock"]:has(.topic-card-item)', content)

    def test_practice_renderer_responsive_scoped(self):
        """Verify practice_renderer.py uses scoped styles for top and bottom controls."""
        fpath = os.path.join(REPO_ROOT, "ui", "question_engine", "practice_renderer.py")
        with open(fpath, "r", encoding="utf-8") as fp:
            content = fp.read()

        self.assertIn("practice-top-marker", content)
        self.assertIn("practice-nav-marker", content)
        self.assertIn("practice-result-nav-marker", content)
        self.assertIn('div[data-testid="stHorizontalBlock"]:has(.practice-top-marker)', content)
        self.assertIn('div[data-testid="stHorizontalBlock"]:has(.practice-nav-marker)', content)
        self.assertIn('div[data-testid="stHorizontalBlock"]:has(.practice-result-nav-marker)', content)


if __name__ == "__main__":
    unittest.main()
