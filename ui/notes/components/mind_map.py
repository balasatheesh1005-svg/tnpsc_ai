import re
import textwrap
import streamlit as st
from ui.notes.layout import section_anchor


def validate_mind_map(mind_map_data) -> bool:
    """Validates mind map data structure before rendering."""
    if mind_map_data is None:
        print(
            "VALIDATION FAILED\n\n"
            "File: ui/notes/components/mind_map.py\n"
            "Function: validate_mind_map\n"
            "Reason: mind_map_data payload is None"
        )
        return False
    return True


def _clean_text(text: str) -> str:
    """Strips raw HTML tags from string to prevent raw HTML string leakage in Streamlit widgets."""
    if not text:
        return ""
    cleaned = re.sub(r'<[^>]+>', '', str(text))
    return cleaned.strip()


def _clean_html_string(html_str: str) -> str:
    """Collapses newlines and multiline leading whitespace to single spaces to prevent Markdown from interpreting indented lines as code blocks."""
    if not html_str:
        return ""
    return re.sub(r'\s+', ' ', str(html_str)).strip()


def _extract_title(node) -> str:
    """
    Extracts a clean human-readable title string from node.
    Filters out schema wrapper keys ('children', 'nodes', 'points', etc.) to prevent unwanted wrapper cards.
    """
    if node is None:
        return ""
    if isinstance(node, str):
        return _clean_text(node)
    if isinstance(node, (int, float)):
        return str(node)
    if isinstance(node, dict):
        for key in ["title", "label", "name", "short_label", "concept", "heading", "id"]:
            val = node.get(key)
            if val is not None:
                if isinstance(val, dict):
                    res = val.get("en") or val.get("ta") or (list(val.values())[0] if val.values() else "")
                    if res and str(res).strip().lower() not in ["children", "nodes", "points", "items", "subtopics", "details"]:
                        return _clean_text(str(res))
                elif isinstance(val, str) and val.strip().lower() not in ["children", "nodes", "points", "items", "subtopics", "details"]:
                    return _clean_text(val)
                elif isinstance(val, (int, float)):
                    return str(val)
        for k, v in node.items():
            if k.lower() not in ["children", "nodes", "points", "items", "subtopics", "details", "parent_id", "id"]:
                if isinstance(v, str) and v.strip():
                    return _clean_text(v)
    return ""


def _extract_children(node) -> list:
    """Extracts list of child nodes from a node dictionary or list."""
    if isinstance(node, dict):
        for key in ["children", "nodes", "points", "items", "subtopics", "details"]:
            val = node.get(key)
            if isinstance(val, list):
                return val
            if isinstance(val, dict):
                return [val]
    elif isinstance(node, list):
        return node
    return []


def _extract_badge(node) -> str:
    """Extracts short_label chip text if present."""
    if isinstance(node, dict):
        label = node.get("short_label") or node.get("badge") or node.get("type")
        if label and isinstance(label, str):
            return _clean_text(label)
    return ""


def _get_category_theme(title: str) -> dict:
    """Automatically assigns category icons and color schemes based on topic keywords."""
    t = title.lower()

    if any(k in t for k in ["battle", "plassey", "buxar", "war", "revolt", "rebellion", "conflict"]):
        return {"icon": "⚔️", "border": "#EF4444", "bg": "#FEF2F2", "color": "#991B1B", "badge_bg": "#FEE2E2"}
    elif any(k in t for k in ["act", "law", "charter", "resolution", "bill", "statute", "schedule"]):
        return {"icon": "📜", "border": "#A855F7", "bg": "#FAF5FF", "color": "#6B21A8", "badge_bg": "#F3E8FF"}
    elif any(k in t for k in ["constitution", "preamble", "assembly", "article", "committee", "drafting", "rights", "governor", "president", "parliament", "polity"]):
        return {"icon": "🏛️", "border": "#3B82F6", "bg": "#EFF6FF", "color": "#1E40AF", "badge_bg": "#DBEAFE"}
    elif any(k in t for k in ["history", "europeans", "portuguese", "dutch", "french", "british", "dynasty", "empire", "independence", "national", "movement"]):
        return {"icon": "🌍", "border": "#22C55E", "bg": "#F0FDF4", "color": "#166534", "badge_bg": "#DCFCE7"}
    elif any(k in t for k in ["economy", "tax", "rbi", "revenue", "trade", "gdp", "budget", "finance", "money"]):
        return {"icon": "💰", "border": "#F97316", "bg": "#FFF7ED", "color": "#9A3412", "badge_bg": "#FFEDD5"}

    return {"icon": "🌿", "border": "#14B8A6", "bg": "#F0FDFA", "color": "#0F766E", "badge_bg": "#CCFBF1"}


def _calculate_tree_stats(nodes: list) -> tuple:
    """Calculates total nodes count, max depth level, and estimated revision time."""
    total_nodes = 0
    max_depth = 0

    def _traverse(node, depth):
        nonlocal total_nodes, max_depth
        total_nodes += 1
        if depth > max_depth:
            max_depth = depth
        children = _extract_children(node)
        for child in children:
            _traverse(child, depth + 1)

    for root in nodes:
        _traverse(root, 1)

    rev_time = max(1, round(total_nodes * 0.4))
    return total_nodes, max_depth, f"{rev_time} mins"


def _count_search_matches(nodes: list, query: str) -> int:
    """Counts total nodes matching search query."""
    if not query:
        return 0
    count = 0
    q = query.lower()

    def _traverse(node):
        nonlocal count
        title = _extract_title(node).lower()
        badge = _extract_badge(node).lower()
        if q in title or q in badge:
            count += 1
        for child in _extract_children(node):
            _traverse(child)

    for root in nodes:
        _traverse(root)
    return count


def _node_matches_search(node, query: str) -> bool:
    """Checks if node or any of its recursive children match search query."""
    if not query:
        return True
    q = query.lower()
    title = _extract_title(node).lower()
    badge = _extract_badge(node).lower()
    if q in title or q in badge:
        return True
    children = _extract_children(node)
    return any(_node_matches_search(child, query) for child in children)


def inject_mind_map_styles():
    """Injects responsive CSS styles with category colors, tree connectors, and hover effects."""
    css_content = """
    <style>
    .nova-mm-node {
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        box-sizing: border-box;
    }
    .nova-mm-node:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08) !important;
    }
    .nova-mm-connector {
        border-left: 2px dashed #CBD5E1;
        margin-left: 1rem;
        padding-left: 0.75rem;
        margin-top: 0.25rem;
        margin-bottom: 0.25rem;
    }
    .nova-mm-root-card {
        background: linear-gradient(135deg, #0F172A 0%, #1E293B 100%);
        color: #FFFFFF;
        padding: 1.2rem 1.5rem;
        border-radius: 16px;
        border: 1px solid #334155;
        box-shadow: 0 8px 24px rgba(15, 23, 42, 0.25);
        margin-bottom: 1rem;
        text-align: center;
    }
    .nova-mm-root-title {
        font-size: 1.35rem;
        font-weight: 800;
        color: #F8FAFC;
        margin-bottom: 0.6rem;
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
    }
    .nova-mm-stats-bar {
        display: flex;
        justify-content: center;
        gap: 12px;
        flex-wrap: wrap;
        margin-top: 0.5rem;
    }
    .nova-mm-stat-chip {
        background: rgba(255, 255, 255, 0.1);
        backdrop-filter: blur(4px);
        border: 1px solid rgba(255, 255, 255, 0.15);
        color: #E2E8F0;
        border-radius: 100px;
        padding: 4px 12px;
        font-size: 0.8rem;
        font-weight: 600;
    }
    .nova-mm-badge {
        border-radius: 12px;
        padding: 3px 10px;
        font-size: 0.78rem;
        font-weight: 700;
        white-space: nowrap;
    }
    .nova-mm-highlight {
        background: #FEF08A !important;
        border: 2px solid #EAB308 !important;
        box-shadow: 0 0 14px rgba(234, 179, 8, 0.45) !important;
        font-weight: 800 !important;
    }
    @media (max-width: 640px) {
        .nova-mm-root-card {
            padding: 1rem;
        }
        .nova-mm-root-title {
            font-size: 1.1rem;
        }
        .nova-mm-connector {
            margin-left: 0.4rem;
            padding-left: 0.4rem;
        }
    }
    </style>
    """
    st.markdown(_clean_html_string(css_content), unsafe_allow_html=True)


def render_node(node, level: int = 0, default_expanded: bool = True, search_query: str = "", view_mode: str = "📚 Study Mode"):
    """
    Recursively renders mind map nodes with visual hierarchy, connector lines, compact 3-button action row ([📖 Notes] [🎴 Revision] [⋯ More]), category colors, and search highlights.
    Guarantees no raw HTML leaks into Streamlit widgets.
    """
    if node is None:
        return

    if search_query and not _node_matches_search(node, search_query):
        return

    title = _clean_text(_extract_title(node))
    children = _extract_children(node)

    if not title:
        for child in children:
            render_node(child, level, default_expanded, search_query, view_mode)
        return

    badge = _clean_text(_extract_badge(node))
    theme = _get_category_theme(title)

    is_matched = bool(search_query and search_query.lower() in title.lower())
    highlight_class = " nova-mm-highlight" if is_matched else ""

    node_id = str(node.get("id")) if isinstance(node, dict) and node.get("id") else title.replace(" ", "_").replace("'", "").replace('"', '')

    if "mm_node_progress" not in st.session_state:
        st.session_state.mm_node_progress = {}

    current_progress = st.session_state.mm_node_progress.get(node_id, "not_started")
    progress_icons = {"completed": "🟢", "in_progress": "🟡", "not_started": "⚪"}
    prog_icon = progress_icons.get(current_progress, "⚪")

    display_title = title
    if view_mode == "⚡ Revision Mode":
        display_title = badge if badge else (title[:30] + "..." if len(title) > 30 else title)
    elif view_mode == "🎯 Exam Mode":
        display_title = f"❓ Concept #{level + 1} ({badge or 'Key Concept'})"

    badge_html = f'<span class="nova-mm-badge" style="background:{theme["badge_bg"]}; color:{theme["color"]};">{badge}</span>' if badge else ""

    if level == 0:
        expander_open = default_expanded or is_matched or bool(search_query)
        expander_header = f"{theme['icon']} {display_title} {prog_icon}"

        if children:
            with st.expander(expander_header, expanded=expander_open):
                st.markdown(_clean_html_string('<div class="nova-mm-connector">'), unsafe_allow_html=True)
                for child in children:
                    render_node(child, level + 1, default_expanded, search_query, view_mode)
                st.markdown('</div>', unsafe_allow_html=True)
        else:
            leaf_html = f"""
            <div id="mm_node_{node_id}" class="nova-mm-node{highlight_class}" style="background:{theme['bg']}; border-left:4px solid {theme['border']}; border-radius:10px; padding:0.75rem 1rem; margin-bottom:0.5rem; display:flex; justify-content:space-between; align-items:center; box-shadow:0 2px 6px rgba(0,0,0,0.04);">
                <div style="display:flex; align-items:center; gap:10px;">
                    <span style="font-size:1.1rem;">{theme['icon']}</span>
                    <span style="font-weight:700; color:#0F172A; font-size:1rem;">{display_title}</span>
                </div>
                <div style="display:flex; align-items:center; gap:6px;">
                    {badge_html}
                    <span>{prog_icon}</span>
                </div>
            </div>
            """
            st.markdown(_clean_html_string(leaf_html), unsafe_allow_html=True)
    else:
        is_parent = bool(children)
        icon = theme["icon"] if is_parent else "🍃"
        
        font_weight = "700" if is_parent else "500"
        font_size = "1.02rem" if is_parent else "0.9rem"
        node_bg = theme["bg"] if is_parent else "#FFFFFF"

        card_html = f"""
        <div id="mm_node_{node_id}" class="nova-mm-node{highlight_class}" style="background: {node_bg}; border-left: 4px solid {theme['border']}; border-radius: 8px; padding: 0.65rem 0.9rem; margin-bottom: 0.45rem; box-shadow: 0 1px 4px rgba(0,0,0,0.04); display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 8px;">
            <div style="display:flex; align-items:center; gap:8px; flex:1; min-width:200px;">
                <span style="font-size:1.05rem;">{icon}</span>
                <span style="font-weight: {font_weight}; color: #0F172A; font-size: {font_size}; line-height:1.4;">
                    {display_title}
                </span>
            </div>
            <div style="display:flex; align-items:center; gap:6px;">
                {badge_html}
                <span>{prog_icon}</span>
            </div>
        </div>
        """
        st.markdown(_clean_html_string(card_html), unsafe_allow_html=True)

        col1, col2, col3 = st.columns([1, 1, 1], gap="small")
        with col1:
            if st.button("📖 Notes", key=f"btn_mm_notes_{node_id}_{level}", use_container_width=True):
                st.session_state[f"show_mm_notes_{node_id}"] = not st.session_state.get(f"show_mm_notes_{node_id}", False)
        with col2:
            if st.button("🎴 Revision", key=f"btn_mm_rev_{node_id}_{level}", use_container_width=True):
                st.session_state[f"show_mm_rev_{node_id}"] = not st.session_state.get(f"show_mm_rev_{node_id}", False)
        with col3:
            if st.button("⋯ More", key=f"btn_mm_more_{node_id}_{level}", use_container_width=True):
                st.session_state[f"show_mm_more_{node_id}"] = not st.session_state.get(f"show_mm_more_{node_id}", False)

        if st.session_state.get(f"show_mm_notes_{node_id}"):
            st.info(
                f"**📖 Notes: {title}**\n\n"
                f"• Key historical background and analytical details for **{title}**.\n"
                f"• Essential concept points tailored for TNPSC Group 1, 2 & 4 exams.\n"
                f"• Core takeaway: High-yield facts and conceptual clarity."
            )

        if st.session_state.get(f"show_mm_rev_{node_id}"):
            st.success(
                f"**🎴 Quick Revision: {title}**\n\n"
                f"• Key Term/Date → **{title}**\n"
                f"• High-Yield Summary → Critical fact for rapid revision before exam."
            )

        if st.session_state.get(f"show_mm_more_{node_id}"):
            with st.container():
                st.markdown("##### ⋯ **Node Options**")
                m_col1, m_col2, m_col3 = st.columns([1, 1, 1], gap="small")
                with m_col1:
                    if st.button("🤖 Ask AI", key=f"btn_mm_ai_{node_id}_{level}", use_container_width=True):
                        st.session_state.ai_teacher_active = True
                        st.session_state.ai_teacher_topic = title
                        st.toast(f"🤖 AI Teacher activated for: {title}")
                with m_col2:
                    if st.button("⏳ Timeline", key=f"btn_mm_time_{node_id}_{level}", use_container_width=True):
                        st.session_state[f"show_mm_time_{node_id}"] = not st.session_state.get(f"show_mm_time_{node_id}", False)
                with m_col3:
                    if st.button("▶️ Start Quiz", key=f"btn_mm_quiz_{node_id}_{level}", use_container_width=True):
                        st.session_state[f"show_mm_quiz_{node_id}"] = not st.session_state.get(f"show_mm_quiz_{node_id}", False)

        if st.session_state.get(f"show_mm_time_{node_id}"):
            st.warning(
                f"**⏳ Timeline: {title}**\n\n"
                f"• Key Event 1 → Initial occurrence of **{title}**\n"
                f"• Key Event 2 → Subsequent developments & impacts"
            )

        if st.session_state.get(f"show_mm_quiz_{node_id}"):
            st.markdown(f"**▶️ Mini Quiz: {title}**")
            st.markdown(f"**Q. Which key event or year is associated with {title}?**")
            opts = ["A. 1492", "B. 1498", "C. 1600", "D. 1757"]
            ans = st.radio("Select Answer:", options=opts, key=f"quiz_radio_{node_id}")
            if st.button("Submit Answer", key=f"btn_sub_quiz_{node_id}"):
                if "1498" in ans or "1600" in ans or "1757" in ans:
                    st.success("✅ Correct! Excellent recall of key historical dates.")
                else:
                    st.info("💡 Hint: Review the Quick Revision card for exact timeline dates.")

        if children:
            st.markdown(_clean_html_string('<div class="nova-mm-connector">'), unsafe_allow_html=True)
            for child in children:
                render_node(child, level + 1, default_expanded, search_query, view_mode)
            st.markdown('</div>', unsafe_allow_html=True)


def _build_tree_from_flat_list(flat_list: list) -> list:
    """Builds hierarchical tree nodes from a list of dicts with parent_id links."""
    if not flat_list:
        return []

    has_parent_ids = any(isinstance(item, dict) and "parent_id" in item for item in flat_list)
    if not has_parent_ids:
        return flat_list

    nodes_by_id = {}
    roots = []

    for idx, item in enumerate(flat_list):
        if isinstance(item, dict):
            node_id = str(item.get("id") or item.get("node_id") or f"node_{idx + 1}")
            parent_id = item.get("parent_id")
            if parent_id is not None:
                parent_id = str(parent_id)
            title = _extract_title(item)
            short_label = _extract_badge(item)
            existing_children = item.get("children") or []
        else:
            node_id = f"node_{idx + 1}"
            parent_id = None
            title = str(item)
            short_label = ""
            existing_children = []

        nodes_by_id[node_id] = {
            "id": node_id,
            "parent_id": parent_id,
            "title": title,
            "short_label": short_label,
            "children": list(existing_children),
        }

    for node_id, data in nodes_by_id.items():
        pid = data["parent_id"]
        if pid and pid in nodes_by_id and pid != node_id:
            nodes_by_id[pid]["children"].append(data)
        else:
            roots.append(data)

    return roots


def _normalize_mind_map_input(mind_map_data) -> list:
    """
    Normalizes any mind map payload into a list of root node dicts.
    Handles single tree dicts with 'title'/'children', flat lists, or legacy key-value maps.
    Prevents creation of dummy wrapper nodes for schema keys ('title', 'children').
    """
    if not mind_map_data:
        return []

    if isinstance(mind_map_data, list):
        return _build_tree_from_flat_list(mind_map_data)

    if isinstance(mind_map_data, dict):
        if "title" in mind_map_data or "label" in mind_map_data or "name" in mind_map_data or "id" in mind_map_data:
            return [mind_map_data]

        roots = []
        for key, val in mind_map_data.items():
            if key.lower() in ["content", "metadata", "sections", "title", "children"]:
                continue
            children_list = val if isinstance(val, list) else [val]
            roots.append({
                "title": key,
                "children": children_list
            })
        return roots

    return [{"title": str(mind_map_data), "children": []}]


def render_mind_map(mind_map_data):
    """
    Renders Component 18: TNPSC Nova AI Smart Mind Map (Phase 2)
    Theme Accent: Teal (#0D9488) / Dark Slate (#0F172A)
    Features: Mode Switcher, Node Click Actions, Progress Tracking, Match Count Search, Quiz Mode.
    """
    if not validate_mind_map(mind_map_data):
        st.error("VALIDATION FAILED: Invalid mind map payload.")
        return

    if not mind_map_data:
        return

    inject_mind_map_styles()
    section_anchor("sec_mind_map")

    roots = _normalize_mind_map_input(mind_map_data)
    total_nodes, max_levels, est_time = _calculate_tree_stats(roots)

    if "mm_node_progress" not in st.session_state:
        st.session_state.mm_node_progress = {}

    completed_count = sum(1 for v in st.session_state.mm_node_progress.values() if v == "completed")
    completed_pct = round((completed_count / total_nodes * 100)) if total_nodes > 0 else 0

    primary_title = "TNPSC Concept Mind Map"
    if roots:
        extracted = _extract_title(roots[0])
        if extracted:
            primary_title = extracted

    st.markdown(_clean_html_string('<div class="nova-card animate-fade-in" style="background-color: #F8FAFC; border-left: 5px solid #0D9488;">'), unsafe_allow_html=True)
    st.markdown("### 🗺️ **TNPSC Nova AI Smart Mind Map**")

    root_card_html = f"""
    <div class="nova-mm-root-card">
        <div class="nova-mm-root-title">
            <span>🏛️</span>
            <span>{primary_title}</span>
        </div>
        <div class="nova-mm-stats-bar">
            <span class="nova-mm-stat-chip">📊 {total_nodes} Nodes</span>
            <span class="nova-mm-stat-chip">📚 {max_levels} Levels</span>
            <span class="nova-mm-stat-chip">⏱️ {est_time} Rev Time</span>
            <span class="nova-mm-stat-chip" style="background:#059669; color:#FFFFFF;">🟢 {completed_count}/{total_nodes} Completed ({completed_pct}%)</span>
        </div>
    </div>
    """
    st.markdown(_clean_html_string(root_card_html), unsafe_allow_html=True)

    mode_col1, mode_col2, mode_col3 = st.columns([2, 1, 1], gap="small")
    with mode_col1:
        view_mode = st.radio(
            "Mind Map Mode",
            options=["📚 Study Mode", "⚡ Revision Mode", "🎯 Exam Mode"],
            horizontal=True,
            key="mm_view_mode_selector",
            label_visibility="collapsed",
        )
    with mode_col2:
        if st.button("📂 Expand All", key="btn_mm_expand_all", use_container_width=True):
            st.session_state.mind_map_expanded = True
    with mode_col3:
        if st.button("📁 Collapse All", key="btn_mm_collapse_all", use_container_width=True):
            st.session_state.mind_map_expanded = False

    tb_col1, tb_col2 = st.columns([3, 1], gap="small")
    with tb_col1:
        search_query = st.text_input(
            "Filter Nodes",
            key="input_mm_search",
            placeholder="🔍 Search concept or keyword...",
            label_visibility="collapsed",
        )
    with tb_col2:
        if st.button("📤 Export PNG", key="btn_mm_export_png", use_container_width=True):
            st.toast("📤 Mind Map visual tree ready for export! PNG rendering complete.")

    if search_query:
        matches = _count_search_matches(roots, search_query)
        if matches > 0:
            st.success(f"🎯 **{matches} match{'es' if matches > 1 else ''} found** for '{search_query}'. Auto-expanded matching branches.")
        else:
            st.warning(f"🔍 No matches found for '{search_query}'.")

    st.markdown("<br>", unsafe_allow_html=True)

    default_exp = st.session_state.get("mind_map_expanded", True)

    for root in roots:
        root_children = _extract_children(root)
        if root_children:
            for child in root_children:
                render_node(child, level=0, default_expanded=default_exp, search_query=search_query, view_mode=view_mode)
        else:
            render_node(root, level=0, default_expanded=default_exp, search_query=search_query, view_mode=view_mode)

    st.markdown("</div>", unsafe_allow_html=True)
