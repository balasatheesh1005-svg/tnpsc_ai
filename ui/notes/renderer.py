import re
import streamlit as st

from ui.notes.theme import inject_notes_theme_css
from ui.notes.animations import inject_animations_css
from ui.notes.navigation import render_sticky_toc
from ui.notes.layout import render_bottom_actions
from ui.notes.registry import GLOBAL_REGISTRY
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


def estimate_reading_time(content_dict):
    """Calculates approximate reading time based on JSON word count."""
    text_content = str(content_dict)
    word_count = len(re.findall(r"\w+", text_content))
    mins = max(1, round(word_count / 180))
    return f"{mins} min{'s' if mins > 1 else ''}"


def render_notes_engine(data: dict):
    """
    Production-Grade Generic Notes Rendering Engine for TNPSC Nova AI.
    Renders notes for EVERY subject automatically driven by JSON schema.
    No subject-specific code or hardcoded section conditionals.
    """
    if not data or not isinstance(data, dict):
        st.warning("📭 Invalid or empty note data.")
        return

    # Inject theme & CSS animations
    inject_notes_theme_css()
    inject_animations_css()

    # 1. Preserve original data & extract content payload
    full_data = data
    content = data.get("content", data)
    if not isinstance(content, dict):
        content = data

    # Combine content with top-level keys from full_data for section keys defined at top-level
    combined_content = dict(content)
    top_level_section_keys = [
        "revision_cards",
        "flashcards",
        "mind_map",
        "concept_map",
        "tables",
        "comparison",
        "comparison_tables",
        "comparison_table",
        "quick_revision",
        "fact_box",
        "important_facts",
        "timeline",
        "chronology",
        "memory_tricks",
        "mnemonics",
        "trap_points",
        "tnpsc_traps",
        "expected_questions",
        "pyq_references",
        "knowledge_graph",
        "relationships",
    ]
    for k in top_level_section_keys:
        if k in full_data and k not in combined_content:
            combined_content[k] = full_data[k]

    # Normalize revision_cards vs flashcards to ensure single authoritative deck
    if "revision_cards" in combined_content and combined_content["revision_cards"]:
        if "flashcards" in combined_content:
            del combined_content["flashcards"]

    subject = data.get("subject", "General Knowledge")
    topic = data.get("topic", "TNPSC Chapter")

    # Compute reading time dynamically if absent
    reading_time = data.get("reading_time", estimate_reading_time(combined_content))

    metadata = {
        "subject": subject,
        "topic": topic,
        "difficulty": data.get("difficulty", "Medium"),
        "reading_time": reading_time,
        "completion_pct": data.get("completion_pct", 80),
    }

    # Identify available sections in JSON and map to component registry
    registered_sections = []  # List of tuples: (order, key, value, spec)
    generic_topic_cards = []  # Fallback for dynamic topic sections
    seen_spec_orders = set()

    meta_skip_keys = {
        "subject",
        "topic",
        "language",
        "ui_type",
        "reading_time",
        "completion_pct",
        "difficulty",
        "content",
        "meta",
        "metadata",
        "keywords",
        "learning_outcomes",
        "constitutional_significance",
        "pyq_reference",
        "related_topics",
        "prerequisites",
        "next_topic",
        "references",
        "ai_metadata",
        "sections",
    }

    for key, value in combined_content.items():
        if key in meta_skip_keys or not value:
            continue

        spec = GLOBAL_REGISTRY.match_key(key)
        if spec:
            if spec.order not in seen_spec_orders:
                registered_sections.append((spec.order, key, value, spec))
                seen_spec_orders.add(spec.order)
        else:
            # Generic topic card section (e.g. constitutional_articles, powers_and_functions, etc.)
            generic_topic_cards.append((key, value))

    # Sort registered sections by strict priority order (1-22)
    registered_sections.sort(key=lambda x: x[0])

    # Build available sections list for Sticky Table of Contents
    toc_items = []
    for order, key, val, spec in registered_sections:
        toc_items.append((f"sec_{key}", spec.display_title or key.replace("_", " ").title(), spec.icon))

    if generic_topic_cards:
        toc_items.append(("sec_topic_cards", "Topic Breakdown", "📌"))

    # 1. RENDER HEADER
    render_header(metadata)

    # 5. RENDER STICKY TABLE OF CONTENTS (if multiple sections exist)
    if len(toc_items) >= 2:
        render_sticky_toc(toc_items)

    # Execute matched registry components in exact priority order
    for order, key, value, spec in registered_sections:
        # Check order breakpoints to insert intermediate components (e.g., Topic Cards at order 7)
        if order > 7 and generic_topic_cards:
            for g_key, g_val in generic_topic_cards:
                render_topic_cards(g_key, g_val)
            generic_topic_cards = []  # Rendered once

        # Execute registered component render function
        if spec.keys[0] in ["knowledge_graph", "relationships"]:
            spec.render_fn(value, topic)
        else:
            spec.render_fn(value)

    # Render remaining generic topic cards if not rendered yet
    if generic_topic_cards:
        for g_key, g_val in generic_topic_cards:
            render_topic_cards(g_key, g_val)

    # 16. RENDER AI TEACHER PANEL
    render_ai_teacher(topic)

    # 17. RENDER REVISION CARDS (only fallback if show_revision_cards is True and flashcards not already rendered)
    has_flashcards_rendered = "revision_cards" in combined_content or "flashcards" in combined_content
    if not has_flashcards_rendered and st.session_state.get("show_revision_cards", False):
        cards = full_data.get(
            "revision_cards",
            content.get(
                "flashcards",
                content.get(
                    "timeline",
                    content.get("important_facts", [topic])
                )
            )
        )
        render_revision_cards(cards if isinstance(cards, list) else [cards])

    # 20. RENDER BOOKMARKS, USER NOTES & HIGHLIGHTS
    render_bookmarks(topic)
    render_user_notes(topic)
    render_highlights(topic)

    # 21. RENDER BOTTOM ACTIONS BAR
    render_bottom_actions(subject, topic)

    # 22. RENDER ANALYTICS FOOTER
    render_footer(metadata)
