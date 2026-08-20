from typing import Callable, Dict, List, Optional, Tuple

from ui.notes.components.header import render_header
from ui.notes.components.definition import render_definition
from ui.notes.components.objectives import render_objectives
from ui.notes.components.introduction import render_introduction
from ui.notes.components.timeline import render_timeline
from ui.notes.components.topic_card import render_topic_cards
from ui.notes.components.comparison import render_comparison
from ui.notes.components.fact_box import render_fact_box
from ui.notes.components.memory import render_memory_tricks
from ui.notes.components.revision import render_revision
from ui.notes.components.trap_points import render_trap_points
from ui.notes.components.expected_questions import render_expected_questions
from ui.notes.components.pyq_reference import render_pyq_reference
from ui.notes.components.related_topics import render_related_topics
from ui.notes.components.ai_teacher import render_ai_teacher
from ui.notes.components.revision_cards import render_revision_cards
from ui.notes.components.mind_map import render_mind_map
from ui.notes.components.knowledge_graph import render_knowledge_graph
from ui.notes.components.bookmarks import render_bookmarks
from ui.notes.components.notes import render_user_notes
from ui.notes.components.highlights import render_highlights
from ui.notes.components.footer import render_footer


class ComponentSpec:

    def __init__(self, order: int, keys: List[str], render_fn: Callable, icon: str = "📌", display_title: str = ""):
        self.order = order
        self.keys = [k.lower() for k in keys]
        self.render_fn = render_fn
        self.icon = icon
        self.display_title = display_title


class ComponentRegistry:
    """
    Component Registry for TNPSC Nova AI Notes Engine.
    Maps JSON keys to reusable components dynamically.
    No hardcoded subject conditionals.
    """

    def __init__(self):
        self._specs: List[ComponentSpec] = []
        self._register_default_components()

    def register(self, spec: ComponentSpec):
        self._specs.append(spec)
        self._specs.sort(key=lambda s: s.order)

    def _register_default_components(self):
        # 1. Header handled directly in layout pipeline
        # 2. Definition
        self.register(ComponentSpec(2, ["definition"], render_definition, icon="📘", display_title="Definition"))
        # 3. Learning Objectives
        self.register(ComponentSpec(3, ["learning_objectives", "objectives", "exam_importance"], render_objectives, icon="🎯", display_title="Objectives"))
        # 4. Introduction
        self.register(ComponentSpec(4, ["introduction", "overview", "origin_and_extent", "discovery"], render_introduction, icon="📖", display_title="Introduction"))
        # 6. Timeline
        self.register(ComponentSpec(6, ["timeline", "chronology"], render_timeline, icon="⏳", display_title="Timeline"))
        # 8. Comparison
        self.register(ComponentSpec(8, ["comparison", "comparison_sg_ag", "tables"], render_comparison, icon="⚖️", display_title="Comparison"))
        # 9. Fact Box
        self.register(ComponentSpec(9, ["important_facts", "facts", "fact_box"], render_fact_box, icon="💡", display_title="Fact Box"))
        # 10. Memory Tricks
        self.register(ComponentSpec(10, ["memory_tricks", "mnemonics", "exam_tricks"], render_memory_tricks, icon="🧠", display_title="Memory Tricks"))
        # 11. Quick Revision
        self.register(ComponentSpec(11, ["quick_revision", "revision_summary"], render_revision, icon="⚡", display_title="Quick Revision"))
        # 12. Trap Points
        self.register(ComponentSpec(12, ["exam_trap", "trap_points", "traps", "tnpsc_traps"], render_trap_points, icon="⚠️", display_title="Trap Points"))
        # 13. Expected Questions
        self.register(ComponentSpec(13, ["expected_questions", "question_areas"], render_expected_questions, icon="🎯", display_title="Expected Questions"))
        # 14. PYQ References
        self.register(ComponentSpec(14, ["pyq_references", "pyqs", "pyq_reference"], render_pyq_reference, icon="📜", display_title="PYQ References"))
        # 15. Related Topics
        self.register(ComponentSpec(15, ["related_topics", "connected_topics"], render_related_topics, icon="🔗", display_title="Related Topics"))
        # 17. Revision Cards
        self.register(ComponentSpec(17, ["revision_cards", "flashcards"], render_revision_cards, icon="🎴", display_title="Revision Cards"))
        # 18. Mind Map
        self.register(ComponentSpec(18, ["mind_map", "concept_map"], render_mind_map, icon="🗺️", display_title="Mind Map"))
        # 19. Knowledge Graph
        self.register(ComponentSpec(19, ["knowledge_graph", "relationships"], render_knowledge_graph, icon="🕸️", display_title="Knowledge Graph"))

    def match_key(self, key: str) -> Optional[ComponentSpec]:
        key_lower = key.lower()
        for spec in self._specs:
            if key_lower in spec.keys:
                return spec
        return None


# Global registry singleton instance
GLOBAL_REGISTRY = ComponentRegistry()
