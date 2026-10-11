import re
import streamlit as st


def format_hero_display_title(raw_topic: str, subject: str = "") -> str:
    """Formats raw topic keys or slugs into clean learner-facing titles."""
    if not raw_topic:
        return "TNPSC Topic"

    t = str(raw_topic).strip()

    # Extract part number if present (_part_1, _part1, _Part_1, etc.)
    part_num = ""
    m = re.search(r"_part_?(\d+)$", t, flags=re.IGNORECASE)
    if m:
        part_num = m.group(1)
        t = re.sub(r"_part_?\d+$", "", t, flags=re.IGNORECASE)

    # Strip subject prefix if present (e.g. polity_, economy_, gt_)
    s_lower = subject.lower().strip() if subject else ""
    if s_lower and t.lower().startswith(f"{s_lower}_"):
        t = t[len(s_lower) + 1 :]
    elif t.lower().startswith("gt_") or t.lower().startswith("tna_") or t.lower().startswith("ts_"):
        t = re.sub(r"^(gt|tna|ts)_", "", t, flags=re.IGNORECASE)

    replacements = {
        "hcf_lcm": "HCF & LCM",
        "ratio_proportion": "Ratio & Proportion",
        "simple_interest": "Simple Interest",
        "compound_interest": "Compound Interest",
        "time_work": "Time & Work",
        "logical_reasoning": "Logical Reasoning",
        "puzzles": "Puzzles",
        "dice": "Dice",
        "visual_reasoning": "Visual Reasoning",
        "alpha_numeric_reasoning": "Alpha-Numeric Reasoning",
        "number_series": "Number Series",
        "percentage": "Percentage",
        "simplification": "Simplification",
        "area": "Area",
        "volume": "Volume",
    }

    clean_base = replacements.get(t.lower(), t.replace("_", " ").title())

    if part_num:
        return f"{clean_base} – Part {part_num}"
    return clean_base


def render_header(metadata):
    """
    Renders Component 1: Hero Header Card
    Displays Subject, Topic, Difficulty Badge, Reading Time, Progress %, Completion Status.
    """
    subject = metadata.get("subject", "General Knowledge").title()
    raw_topic = metadata.get("topic", "TNPSC Topic")
    display_title = metadata.get("display_title") or format_hero_display_title(raw_topic, subject)
    difficulty = metadata.get("difficulty", "Medium").title()
    reading_time = metadata.get("reading_time", "5 mins")
    completion_pct = metadata.get("completion_pct", 85)

    # Color badge mapping
    diff_color = "#22C55E" if difficulty.lower() == "easy" else "#F59E0B" if difficulty.lower() == "medium" else "#EF4444"

    st.markdown(
        f"""
        <div class="nova-card animate-fade-in" style="background: linear-gradient(135deg, #0F172A 0%, #1E293B 60%, #1E40AF 100%); color: white; padding: 2rem; border-radius: 20px; box-shadow: 0 12px 30px rgba(15, 23, 42, 0.3);">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.75rem;">
                <span class="nova-badge" style="background-color: rgba(59, 130, 246, 0.25); color: #93C5FD; border: 1px solid rgba(147, 197, 253, 0.3);">
                    📘 {subject}
                </span>
                <span class="nova-badge" style="background-color: {diff_color}22; color: {diff_color}; border: 1px solid {diff_color}55;">
                    ⚡ {difficulty}
                </span>
            </div>
            <h1 style="color: #FFFFFF; font-size: 2.1rem; font-weight: 800; margin-bottom: 0.5rem; line-height: 1.2;">
                {display_title}
            </h1>
            <div style="display: flex; gap: 1.5rem; align-items: center; font-size: 0.9rem; color: #CBD5E1; margin-top: 1rem;">
                <span>⏱️ Reading Time: <strong>{reading_time}</strong></span>
                <span>📊 Estimated Completion: <strong>{completion_pct}%</strong></span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.progress(completion_pct / 100.0)

