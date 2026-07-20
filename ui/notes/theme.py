import streamlit as st

# Design System Color Palette as per TNPSC Nova AI Specifications
SECTION_THEMES = {
    "header": {"bg": "linear-gradient(135deg, #0F172A 0%, #1E293B 50%, #1E40AF 100%)", "border": "#3B82F6", "text": "#F8FAFC"},
    "definition": {"bg": "#EFF6FF", "dark_bg": "#1E293B", "border": "#2563EB", "accent": "#2563EB", "icon": "📘"},
    "objectives": {"bg": "#F0F9FF", "dark_bg": "#0F172A", "border": "#0284C7", "accent": "#0284C7", "icon": "🎯"},
    "introduction": {"bg": "#F8FAFC", "dark_bg": "#1E293B", "border": "#64748B", "accent": "#475569", "icon": "📖"},
    "timeline": {"bg": "#EEF2FF", "dark_bg": "#1E1B4B", "border": "#4F46E5", "accent": "#4F46E5", "icon": "⏳"},
    "topic_card": {"bg": "#FFFFFF", "dark_bg": "#0F172A", "border": "#CBD5E1", "accent": "#3B82F6", "icon": "📌"},
    "comparison": {"bg": "#ECFEFF", "dark_bg": "#164E63", "border": "#0891B2", "accent": "#0891B2", "icon": "⚖️"},
    "fact_box": {"bg": "#FFFBEB", "dark_bg": "#451A03", "border": "#D97706", "accent": "#D97706", "icon": "💡"},
    "memory": {"bg": "#F3E8FF", "dark_bg": "#3B0764", "border": "#9333EA", "accent": "#9333EA", "icon": "🧠"},
    "revision": {"bg": "#F0FDF4", "dark_bg": "#052E16", "border": "#16A34A", "accent": "#16A34A", "icon": "⚡"},
    "trap_points": {"bg": "#FEF2F2", "dark_bg": "#450A0A", "border": "#DC2626", "accent": "#DC2626", "icon": "⚠️"},
    "expected_questions": {"bg": "#FFF7ED", "dark_bg": "#431407", "border": "#EA580C", "accent": "#EA580C", "icon": "🎯"},
    "pyq_reference": {"bg": "#ECFDF5", "dark_bg": "#064E3B", "border": "#059669", "accent": "#059669", "icon": "📜"},
    "related_topics": {"bg": "#F5F3FF", "dark_bg": "#2E1065", "border": "#7C3AED", "accent": "#7C3AED", "icon": "🔗"},
    "ai_teacher": {"bg": "linear-gradient(135deg, #1E40AF 0%, #3B82F6 100%)", "border": "#60A5FA", "accent": "#60A5FA", "text": "#FFFFFF", "icon": "🤖"},
    "revision_cards": {"bg": "#FAFAF9", "dark_bg": "#1C1917", "border": "#78716C", "accent": "#0284C7", "icon": "🎴"},
    "mind_map": {"bg": "#F0FDFA", "dark_bg": "#042F2E", "border": "#0D9488", "accent": "#0D9488", "icon": "🗺️"},
    "knowledge_graph": {"bg": "#F5F3FF", "dark_bg": "#2E1065", "border": "#7C3AED", "accent": "#7C3AED", "icon": "🕸️"},
    "bookmarks": {"bg": "#F8FAFC", "dark_bg": "#0F172A", "border": "#64748B", "accent": "#64748B", "icon": "🔖"},
    "notes": {"bg": "#FEFCE8", "dark_bg": "#422006", "border": "#EAB308", "accent": "#CA8A04", "icon": "✏️"},
    "highlights": {"bg": "#FEF08A", "dark_bg": "#713F12", "border": "#EAB308", "accent": "#A16207", "icon": "🖍️"},
    "footer": {"bg": "#0F172A", "dark_bg": "#020617", "border": "#334155", "accent": "#38BDF8", "text": "#94A3B8", "icon": "📊"}
}


def inject_notes_theme_css():
    """Injects high-performance CSS tokens for Nova AI Notes Engine."""
    st.markdown(
        """
        <style>
        /* Nova Notes Engine Modern Global Styles */
        .nova-card {
            border-radius: 16px;
            padding: 1.5rem;
            margin-bottom: 1.25rem;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            border-left: 5px solid transparent;
        }

        .nova-card:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 30px rgba(0, 0, 0, 0.08);
        }

        /* Specific Component Card Theme Classes */
        .nova-definition-card {
            background-color: rgba(37, 99, 235, 0.04);
            border-left-color: #2563EB;
            border-top: 1px solid rgba(37, 99, 235, 0.15);
            border-right: 1px solid rgba(37, 99, 235, 0.15);
            border-bottom: 1px solid rgba(37, 99, 235, 0.15);
        }

        .nova-fact-card {
            background-color: rgba(217, 119, 6, 0.06);
            border-left-color: #D97706;
            border-top: 1px solid rgba(217, 119, 6, 0.2);
            border-right: 1px solid rgba(217, 119, 6, 0.2);
            border-bottom: 1px solid rgba(217, 119, 6, 0.2);
        }

        .nova-memory-card {
            background-color: rgba(147, 51, 234, 0.06);
            border-left-color: #9333EA;
            border-top: 1px solid rgba(147, 51, 234, 0.2);
            border-right: 1px solid rgba(147, 51, 234, 0.2);
            border-bottom: 1px solid rgba(147, 51, 234, 0.2);
        }

        .nova-revision-card {
            background-color: rgba(22, 163, 74, 0.06);
            border-left-color: #16A34A;
            border-top: 1px solid rgba(22, 163, 74, 0.2);
            border-right: 1px solid rgba(22, 163, 74, 0.2);
            border-bottom: 1px solid rgba(22, 163, 74, 0.2);
        }

        .nova-trap-card {
            background-color: rgba(220, 38, 38, 0.06);
            border-left-color: #DC2626;
            border-top: 1px solid rgba(220, 38, 38, 0.2);
            border-right: 1px solid rgba(220, 38, 38, 0.2);
            border-bottom: 1px solid rgba(220, 38, 38, 0.2);
        }

        .nova-expected-card {
            background-color: rgba(234, 88, 12, 0.06);
            border-left-color: #EA580C;
            border-top: 1px solid rgba(234, 88, 12, 0.2);
            border-right: 1px solid rgba(234, 88, 12, 0.2);
            border-bottom: 1px solid rgba(234, 88, 12, 0.2);
        }

        .nova-ai-card {
            background: linear-gradient(135deg, #1E3A8A 0%, #2563EB 100%);
            color: #FFFFFF !important;
            border-radius: 18px;
            padding: 1.75rem;
            box-shadow: 0 10px 25px rgba(37, 99, 235, 0.25);
        }

        .nova-ai-card h3, .nova-ai-card p, .nova-ai-card span {
            color: #FFFFFF !important;
        }

        .nova-badge {
            display: inline-flex;
            align-items: center;
            padding: 0.35rem 0.85rem;
            border-radius: 9999px;
            font-size: 0.78rem;
            font-weight: 700;
            letter-spacing: 0.03em;
            text-transform: uppercase;
        }

        .nova-chip {
            display: inline-block;
            padding: 0.25rem 0.65rem;
            border-radius: 8px;
            font-size: 0.82rem;
            font-weight: 600;
            margin-right: 0.4rem;
            margin-bottom: 0.4rem;
            background-color: rgba(37, 99, 235, 0.1);
            color: #2563EB;
            border: 1px solid rgba(37, 99, 235, 0.2);
        }

        /* Timeline vertical line */
        .nova-timeline-container {
            position: relative;
            padding-left: 2rem;
            margin: 1.25rem 0;
            border-left: 3px solid #4F46E5;
        }

        .nova-timeline-item {
            position: relative;
            margin-bottom: 1.25rem;
            padding-left: 1rem;
        }

        .nova-timeline-item::before {
            content: '';
            position: absolute;
            left: -2.6rem;
            top: 0.35rem;
            width: 14px;
            height: 14px;
            border-radius: 50%;
            background-color: #4F46E5;
            border: 3px solid #FFFFFF;
            box-shadow: 0 0 0 2px #4F46E5;
        }

        /* Sticky TOC */
        .nova-toc-sticky {
            position: sticky;
            top: 1rem;
            z-index: 100;
            background: rgba(255, 255, 255, 0.95);
            backdrop-filter: blur(10px);
            border-radius: 14px;
            padding: 0.75rem 1rem;
            border: 1px solid #E2E8F0;
            box-shadow: 0 4px 15px rgba(0,0,0,0.05);
            margin-bottom: 1.5rem;
        }

        /* Dark mode overrides for TOC */
        @media (prefers-color-scheme: dark) {
            .nova-toc-sticky {
                background: rgba(15, 23, 42, 0.92);
                border-color: #334155;
            }
        }

        /* Custom Flashcard UI */
        .nova-flashcard {
            background: linear-gradient(145deg, #ffffff, #f1f5f9);
            border: 2px solid #cbd5e1;
            border-radius: 16px;
            padding: 2rem;
            text-align: center;
            min-height: 180px;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            box-shadow: 0 10px 25px rgba(0,0,0,0.06);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
