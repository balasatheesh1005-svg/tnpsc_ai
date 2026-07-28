import streamlit as st
import random, time
import traceback

from ui.components.header import render_sidebar_branding
from ui.components.cards import (
    glass_card,
    glass_card_html,
    analytics_grid,
    html_fragment,
    render_card_styles,
)
from ui.theme import render_theme_css
from core.auth import logout, restore_auth_session
from core.session import is_authenticated, reset_app_state_for_logout
from core.supabase_client import get_recent_error_message
from ui.login import render_login_page
from ui.signup import render_signup_page


# ---------------- UI HELPERS ----------------
def section(title):
    st.markdown(
        f"""
    <div style="
    background:#ffffff;
    padding:15px;
    border-radius:12px;
    box-shadow:0 2px 8px rgba(0,0,0,0.1);
    margin-bottom:15px;">
    <h3>{title}</h3>
    </div>
    """,
        unsafe_allow_html=True,
    )


def show_friendly_error(message=None):
    st.warning(message or "Something went wrong. Please try again.")


def safe_call(callback, fallback=None, message=None):
    try:
        return callback()
    except Exception as e:
        import traceback

        st.code(traceback.format_exc())
        return fallback


def default_dashboard_stats():
    return {
        "tests_attempted": 0,
        "accuracy": 0,
        "streak": 0,
        "rank": 0,
        "weak_subject": "No Data",
        "xp": 0,
        "level": 1,
        "level_progress": {},
    }


# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="TNPSC Nova AI", page_icon="assets/app_icon.png", layout="wide"
)
# ---------------- STYLE ----------------
render_theme_css()

# ---------------- IMPORTS ----------------
from core.question_loader import load_questions
from core.daily_mission_ai import (
    update_daily_test,
    update_revision as update_daily_mission_revision,
)
from core.test_completion import complete_test
from core.test_evaluator import evaluate_answer
from core.test_revision import handle_correct_revision, handle_wrong_revision
from core.progress_ai import get_progress
from core.test_topic_selector import get_test_config
from core.test_weakness import handle_correct_answer, handle_wrong_answer
from ui.dashboard import render_dashboard
from ui.revision.dashboard import render_revision_dashboard
from ui.intelligence.dashboard import render_learning_intelligence_dashboard
from streamlit_option_menu import option_menu
from core.dashboard_stats_ai import get_dashboard_stats
from ui.pages.daily_test_renderer import render_explanation_next, render_question
from ui.pages.leaderboard import render_leaderboard
from ui.pages.mentor import render_mentor
from ui.pages.notes import render_notes_page


# ---------------- UI HELPERS ----------------
def section(title):
    st.markdown(
        f"""
    <div style="
    background:#ffffff;
    padding:15px;
    border-radius:12px;
    box-shadow:0 2px 8px rgba(0,0,0,0.1);
    margin-bottom:15px;">
    <h3>{title}</h3>
    </div>
    """,
        unsafe_allow_html=True,
    )


def show_friendly_error(message=None):
    st.warning(message or "Something went wrong. Please try again.")


def safe_call(callback, fallback=None, message=None):
    try:
        return callback()
    except Exception as e:
        import traceback

        st.code(traceback.format_exc())
        return fallback


def default_dashboard_stats():
    return {
        "tests_attempted": 0,
        "accuracy": 0,
        "streak": 0,
        "rank": 0,
        "weak_subject": "No Data",
        "xp": 0,
        "level": 1,
        "level_progress": {},
    }


# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="TNPSC Nova AI", page_icon="assets/app_icon.png", layout="wide"
)
# ---------------- STYLE ----------------
render_theme_css()

# ---------------- IMPORTS ----------------
from core.question_loader import load_questions
from core.daily_mission_ai import (
    update_daily_test,
    update_revision as update_daily_mission_revision,
)
from core.test_completion import complete_test
from core.test_evaluator import evaluate_answer
from core.test_revision import handle_correct_revision, handle_wrong_revision
from core.progress_ai import get_progress
from core.test_topic_selector import get_test_config
from core.test_weakness import handle_correct_answer, handle_wrong_answer
from ui.dashboard import render_dashboard
from streamlit_option_menu import option_menu
from core.dashboard_stats_ai import get_dashboard_stats
from ui.pages.daily_test_renderer import render_explanation_next, render_question
from ui.pages.leaderboard import render_leaderboard
from ui.pages.mentor import render_mentor
from ui.pages.notes import render_notes_page
from ui.pages.about import render_about_page
from ui.pages.contact import render_contact_page
from ui.pages.progress import render_progress_page
from ui.pages.teacher import render_teacher
from ui.pages.weakness import render_weakness_page
from ui.pyq.dashboard import render_pyq_dashboard
from core.navigation_v2.navigation_state import (
    init_navigation_state,
    get_selected_subject,
    get_selected_topic,
    get_selected_topic_key,
    set_global_topic,
    clear_selected_subject,
    clear_selected_topic,
)
from ui.navigation_v2.subject_selector import render_subject_selector
from ui.navigation_v2.topic_selector import render_topic_selector
from ui.navigation_v2.topic_hub import render_topic_hub

# ---------------- AUTHENTICATION ----------------
restore_auth_session()


if not is_authenticated():
    st.markdown(
        """
        <style>
            .stApp {
                background: linear-gradient(135deg, #0f172a, #1e3a8a, #2563eb);
                background-attachment: fixed;
            }
            [data-testid="stHeader"], [data-testid="stSidebar"] { display: none; }
            .login-container { max-width: 450px; margin: auto; padding: 10px; }
            .glass-card {
                background: rgba(255, 255, 255, 0.08);
                backdrop-filter: blur(12px);
                border-radius: 20px;
                border: 1px solid rgba(255, 255, 255, 0.1);
                padding: 20px;
                box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.3);
                margin-bottom: 15px;
                text-align: center;
            }
            .chip-container { display: flex; flex-wrap: wrap; justify-content: center; gap: 8px; margin: 15px 0; }
            .chip {
                padding: 6px 14px; border-radius: 100px; font-size: 0.85em; font-weight: 600;
                display: inline-flex; align-items: center; gap: 6px;
                backdrop-filter: blur(4px); border: 1px solid rgba(255, 255, 255, 0.1);
            }
            .chip-blue { background: rgba(59, 130, 246, 0.2); color: #93c5fd; }
            .chip-green { background: rgba(34, 197, 94, 0.2); color: #86efac; }
            .chip-purple { background: rgba(168, 85, 247, 0.2); color: #d8b4fe; }
            .chip-orange { background: rgba(249, 115, 22, 0.2); color: #fdba74; }
            .badge-container { display: flex; justify-content: space-around; margin-top: 15px; }
            .badge { text-align: center; font-size: 0.7em; color: #cbd5e1; }
            .badge span { display: block; font-size: 1.6em; margin-bottom: 4px; }
            [data-testid="stTextInput"] label,
            [data-testid="stTextInput"] label p {
                color: #FFFFFF !important;
                font-weight: 800 !important;
            }
            [data-testid="stTextInput"] div[data-baseweb="input"] {
                background-color: #FFFFFF !important;
                border: 1px solid #2563EB !important;
                border-radius: 10px !important;
                box-shadow: none !important;
            }
            [data-testid="stTextInput"] div[data-baseweb="input"]:focus-within {
                border-color: #2563EB !important;
                box-shadow: 0 0 0 2px rgba(147, 197, 253, 0.45) !important;
            }
            [data-testid="stTextInput"] input,
            [data-testid="stTextInput"] input[type="password"],
            [data-testid="stTextInput"] input[type="text"],
            [data-testid="stTextInput"] input[type="email"] {
                background-color: #FFFFFF !important;
                color: #111827 !important;
                -webkit-text-fill-color: #111827 !important;
                caret-color: #111827 !important;
            }
            [data-testid="stTextInput"] input::placeholder {
                color: #6B7280 !important;
                -webkit-text-fill-color: #6B7280 !important;
                opacity: 1 !important;
            }
            [data-testid="stTextInput"] svg {
                color: #111827 !important;
                fill: #111827 !important;
            }
            div.stButton > button,
            div.stFormSubmitButton > button {
                border-radius: 10px !important;
                font-weight: 800 !important;
            }
            div.stButton > button[kind="primary"],
            div.stFormSubmitButton > button[kind="primary"] {
                background: #2563EB !important;
                border: 1px solid #2563EB !important;
                color: #FFFFFF !important;
                box-shadow: 0 4px 14px rgba(37, 99, 235, 0.32) !important;
            }
            div.stButton > button[kind="primary"]:hover,
            div.stFormSubmitButton > button[kind="primary"]:hover {
                background: #1D4ED8 !important;
                border-color: #1D4ED8 !important;
                color: #FFFFFF !important;
            }
            div.stButton > button[kind="tertiary"] {
                min-height: 2rem !important;
                background: transparent !important;
                border: 0 !important;
                color: #93C5FD !important;
                box-shadow: none !important;
                text-decoration: none !important;
            }
            div.stButton > button[kind="tertiary"]:hover {
                background: transparent !important;
                color: #93C5FD !important;
                text-decoration: underline !important;
                box-shadow: none !important;
                transform: none !important;
            }
            div.stButton > button:disabled,
            div.stFormSubmitButton > button:disabled {
                background: #9CA3AF !important;
                border-color: #9CA3AF !important;
                color: #FFFFFF !important;
                opacity: 1 !important;
                box-shadow: none !important;
            }
            div[data-testid="stCaptionContainer"],
            div[data-testid="stCaptionContainer"] p {
                color: #E5E7EB !important;
            }
            div[data-testid="stMarkdownContainer"] h3 {
                color: #FFFFFF !important;
            }
            div[data-testid="stAlert"] [data-testid="stAlertContainer"],
            div[data-testid="stAlert"] [data-testid="stAlertContainer"] * {
                color: #FFFFFF !important;
            }
            div[data-testid="stAlert"] [data-testid="stAlertContainer"] svg {
                fill: currentColor !important;
            }
            div[data-testid="stAlert"]:has([data-testid="stAlertContentSuccess"])
            [data-testid="stAlertContainer"] {
                background: #16A34A !important;
            }
            div[data-testid="stAlert"]:has([data-testid="stAlertContentError"])
            [data-testid="stAlertContainer"] {
                background: #DC2626 !important;
            }
            div[data-testid="stAlert"]:has([data-testid="stAlertContentInfo"])
            [data-testid="stAlertContainer"] {
                background: #2563EB !important;
            }
            div[data-testid="stAlert"]:has([data-testid="stAlertContentWarning"])
            [data-testid="stAlertContainer"] {
                background: #F97316 !important;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    with st.container():
        st.markdown('<div class="login-container">', unsafe_allow_html=True)

        # SECTION 1 – LOGO & BRANDING
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            st.image("assets/app_icon.png", use_container_width=True)

        st.markdown(
            """
            <div style="text-align: center; margin-bottom: 20px;">
                <h1 style="color: white; margin-bottom: 0;">TNPSC Nova AI</h1>
                <p style="color: #94a3b8; font-size: 0.9em;">India's AI Powered TNPSC Preparation Platform</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # SECTION 2 – FEATURE CHIPS
        st.markdown(
            """
            <div class="chip-container">
                <div class="chip chip-blue">📘 Daily Tests</div>
                <div class="chip chip-green">🤖 AI Teacher</div>
                <div class="chip chip-purple">👨‍🏫 Personal Mentor</div>
                <div class="chip chip-orange">📚 Smart Revision</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        # SECTION 3 – WELCOME CARD
        st.markdown(
            """
            <div class="glass-card">
                <h3 style="color: white; margin-bottom: 5px;">👋 Welcome Back</h3>
                <p style="color: #cbd5e1; font-size: 0.95em; margin: 0;">Learn. Practice. Revise. Succeed.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        if "auth_page" not in st.session_state:
            st.session_state["auth_page"] = "login"

        login_tab, signup_tab = st.columns(2)
        with login_tab:
            if st.button(
                "Login",
                use_container_width=True,
                disabled=st.session_state["auth_page"] == "login",
            ):
                st.session_state["auth_page"] = "login"
                st.rerun()
        with signup_tab:
            if st.button(
                "Sign Up",
                use_container_width=True,
                disabled=st.session_state["auth_page"] == "signup",
            ):
                st.session_state["auth_page"] = "signup"
                st.rerun()

        if st.session_state["auth_page"] == "signup":
            render_signup_page()
        else:
            render_login_page()

        st.markdown("</div>", unsafe_allow_html=True)

    st.stop()
else:
    # ---------------- USER ----------------
    username = st.session_state["username"]
    user = username
    dashboard_stats = safe_call(
        lambda: get_dashboard_stats(username),
        fallback=default_dashboard_stats()
    )

    st.session_state["tests_attempted"] = dashboard_stats.get("tests_attempted", 0)

    st.session_state["accuracy"] = dashboard_stats.get("accuracy", 0)

    st.session_state["streak"] = dashboard_stats.get("streak", 0)
    st.session_state["rank"] = dashboard_stats.get("rank", 0)
    st.session_state["weak_subject"] = dashboard_stats.get("weak_subject", "No Data")

    fetched_lv = dashboard_stats.get("level", 1)
    if "xp_level" in st.session_state and fetched_lv > st.session_state["xp_level"]:
        st.session_state["xp_level_up"] = True
    st.session_state["xp_level"] = fetched_lv


# ---------------- SESSION INIT ----------------


def initialize_session_state():
    defaults = {
        "correct_streak": 0,
        "wrong_count": 0,
        "level": "easy",
        "exam": "group1",
        "test_active": False,
        "score": 0,
        "q_index": 0,
        "mentor_chat": [],
        "test_qs": [],
        "answered": False,
        "test_results_processed": False,
        "test_mode": None,
        "test_subject": None,
        "test_topic": None,
        "start_time": 0,
        "mentor_notification": False,
        "notes_practice_trigger": False,
        "xp_level": 1,
        "xp_level_up": False,
        "test_start_xp": 0,
        "study_stage": "notes",
    }
    for key, val in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = val
    init_navigation_state()


initialize_session_state()

MENU_OPTIONS = [
    "🏠 Home",
    "📘 Daily Test",
    "PYQ",
    "📚 Notes",
    "🧠 Weakness",
    "🔄 Smart Revision",
    "🧬 Learning Intelligence",
    "📊 Progress",
    "🏆 Leaderboard",
    "🤖 AI Teacher",
    "👨‍🏫 Personal Mentor",
    "ℹ️ About",
    "📞 Contact",
]

if "main_menu" not in st.session_state:
    st.session_state["main_menu"] = MENU_OPTIONS[0]

if "navigate_to" in st.session_state:
    nav_target = st.session_state.get("navigate_to")
    if nav_target in MENU_OPTIONS:
        st.session_state["main_menu"] = nav_target
    st.session_state.pop("navigate_to", None)

current_menu = st.session_state["main_menu"]
current_index = MENU_OPTIONS.index(current_menu)

# ---------------- MENU ----------------
with st.sidebar:
    render_sidebar_branding(
        username,
        st.session_state.get("rank", 0),
        st.session_state.get("accuracy", 0),
        st.session_state.get("streak", 0),
    )

    if st.button("Logout", use_container_width=True):
        logout()
        reset_app_state_for_logout()
        st.rerun()

    selected = option_menu(
        menu_title="📂 Menu",
        options=MENU_OPTIONS,
        icons=[
            "house",
            "clipboard-check",
            "journal-text",
            "book",
            "brain",
            "arrow-repeat",
            "cpu",
            "bar-chart",
            "trophy",
            "robot",
            "person",
            "info-circle",
            "envelope",
        ],
        menu_icon="cast",
        default_index=current_index,
        key="sidebar_main_menu",
        styles={
            "container": {
                "padding": "0",
                "background-color": "transparent",
            },
            "icon": {
                "color": "inherit",
                "font-size": "17px",
            },
            "nav-link": {
                "font-size": "15px",
                "text-align": "left",
                "margin": "4px 0",
                "--hover-color": "#EFF6FF",
            },
            "nav-link-selected": {
                "background": "linear-gradient(135deg, #0F172A, #2563EB)",
                "color": "#FFFFFF",
            },
            "menu-title": {
                "font-size": "16px",
                "font-weight": "800",
                "color": "#0F172A",
                "padding": "0.4rem 0.2rem 0.75rem",
            },
        },
    )

    st.session_state["main_menu"] = selected


def render_today_topic_card(user):
    """Display the daily recommended topic card before the test starts."""
    if "daily_test_config" not in st.session_state:
        st.session_state.daily_test_config = get_test_config(user)

    daily_config = st.session_state.daily_test_config
    topic_display = daily_config["topic"].replace("_", " ").title()
    subject_display = daily_config["subject"].title()

    subj_lower = daily_config["subject"].lower()
    subj_icon = (
        "🏛️"
        if subj_lower in ["polity", "history"]
        else "💰" if subj_lower == "economy" else "📚"
    )

    card_html = glass_card_html(
        "📘 Today's Recommended Topic",
        value=topic_display,
        body="",
        extra_html=analytics_grid(
            [
                (f"{subj_icon} Subject", subject_display),
                ("📖 Topic", topic_display),
                ("❓ Questions", "10"),
            ]
        ),
    )
    st.html(card_html)


# ================= MENU ROUTING =================

# ---------------- HOME ----------------
if selected == "🏠 Home":
    nav_view = st.session_state.get("nav_view", "topic_hub")
    render_card_styles()
    
    if nav_view == "subject_select":
        render_subject_selector()
    elif nav_view == "topic_select":
        render_topic_selector()
    else:
        t_hub, t_dash = st.tabs(["📚 Study Hub", "📊 Performance Dashboard"])
        with t_hub:
            render_topic_hub(user)
        with t_dash:
            safe_call(render_dashboard)


# ---------------- DAILY TEST ----------------
elif selected == "📘 Daily Test":
    section("📘 Daily Test")
    render_card_styles()
    is_active = st.session_state.test_active

    if not is_active:
        render_today_topic_card(user)
        st.write("")

    # 🚀 AUTO-LOAD FROM NOTES
    if st.session_state.get("notes_practice_trigger") and not is_active:
        with st.spinner("⏳ Loading Practice Session..."):
            st.session_state.update(
                {
                    "q_index": 0,
                    "score": 0,
                    "answered": False,
                    "test_active": True,
                    "test_mode": "daily",
                    "test_mode": "notes_practice",
                    "test_results_processed": False,
                    "notes_practice_trigger": False,
                    "test_start_xp": st.session_state.get("xp", 0),
                }
            )
            questions = load_questions(
                st.session_state.test_subject,
                st.session_state.test_topic,
                st.session_state.level,
            )
            if not questions:
                st.error("No questions found for this topic.")
                st.session_state.test_active = False
            else:
                st.session_state.test_qs = random.sample(
                    questions, min(10, len(questions))
                )
                st.rerun()

    col1, col2, col3 = st.columns(3)
    # 🚀 START TEST
    with col1:
        if st.button("🚀 Start Daily Test", disabled=is_active):
            with st.spinner("⏳ Generating Test..."):
                st.session_state.update(
                    {
                        "q_index": 0,
                        "score": 0,
                        "answered": False,
                        "test_active": True,
                        "test_mode": "daily",
                        "test_results_processed": False,
                        "test_start_xp": st.session_state.get("xp", 0),
                    }
                )
            if "daily_test_config" in st.session_state:
                test_config = st.session_state.daily_test_config
            else:
                test_config = get_test_config(user)

            st.session_state.test_subject, st.session_state.test_topic = (
                test_config["subject"],
                test_config["topic"],
            )
            questions = load_questions(
                test_config["subject"], test_config["topic"], test_config["level"]
            )
            if not questions:
                st.error("No questions found")
                st.stop()
            st.session_state.test_qs = random.sample(questions, min(10, len(questions)))
            st.rerun()

    # 🔥 WEAK TEST
    with col2:
        if st.button("🔥 Practice Weak Topics", disabled=is_active):
            with st.spinner("⏳ Loading Weak Topics..."):
                st.session_state.update(
                    {
                        "test_active": True,
                        "test_mode": "weak",
                        "test_results_processed": False,
                        "test_start_xp": st.session_state.get("xp", 0),
                    }
                )
            test_config = get_test_config(user, mode="weak")
            st.session_state.test_subject, st.session_state.test_topic = (
                test_config["subject"],
                test_config["topic"],
            )
            questions = load_questions(
                test_config["subject"], test_config["topic"], test_config["level"]
            )
            if not questions:
                st.error("No questions found")
                st.stop()
            st.session_state.test_qs = random.sample(questions, min(5, len(questions)))
            st.rerun()

    with col3:
        if st.button("📚 Start Revision Test", disabled=is_active):
            with st.spinner("⏳ Fetching Revision Queue..."):
                st.session_state.update(
                    {
                        "test_active": True,
                        "test_mode": "revision",
                        "test_results_processed": False,
                        "test_start_xp": st.session_state.get("xp", 0),
                    }
                )
            test_config = get_test_config(user, mode="revision")
            st.session_state.test_subject, st.session_state.test_topic = (
                test_config["subject"],
                test_config["topic"],
            )
            questions = load_questions(
                test_config["subject"], test_config["topic"], test_config["level"]
            )
            if not questions:
                st.error("❌ No revision questions found")
                st.stop()
            st.session_state.test_qs = random.sample(questions, min(5, len(questions)))
            st.rerun()

    # ---------------- SAFETY ----------------
    if not st.session_state.test_active:
        st.info("👉 Please select a test mode above to begin your session.")
        st.stop()

    # ---------------- QUESTIONS ----------------
    if not st.session_state.test_qs:
        st.warning("No questions loaded")
        st.stop()

    total_q = len(st.session_state.get("test_qs", []))
    if st.session_state.q_index < total_q:
        q = st.session_state.test_qs[st.session_state.q_index]
        selected_ans, options = render_question(q)

        # ---------------- SUBMIT ----------------
        if not st.session_state.answered:
            if st.button("Submit Answer", type="primary", use_container_width=True):
                selected_key = selected_ans.split(".", 1)[0] if selected_ans else ""
                st.session_state["last_selected_option"] = selected_key

                result = evaluate_answer(
                    selected_ans,
                    options,
                    q,
                    user,
                    st.session_state.test_subject,
                    st.session_state.test_topic,
                )

                if result["processed"]:
                    subject = st.session_state.test_subject
                    topic = st.session_state.test_topic
                    if result["is_correct"]:
                        handle_correct_answer(user, subject, topic)
                        if st.session_state.test_mode == "revision":
                            handle_correct_revision(user, subject, topic)
                    else:
                        handle_wrong_answer(user, subject, topic)
                        if st.session_state.test_mode == "revision":
                            handle_wrong_revision(user, subject, topic)
                    st.rerun()

        # ---------------- NEXT ----------------
        if st.session_state.answered:
            render_explanation_next(q)

    elif total_q > 0:
        total = st.session_state.get("score", 0)
        percent = int((total / total_q) * 100)

        if not st.session_state.get("test_results_processed", False):
            complete_test(
                user,
                st.session_state.get("test_subject", "polity"),
                st.session_state.get("test_topic", "general"),
                percent,
            )
            if st.session_state.test_mode in ["daily", "notes_practice"]:
                update_daily_test(user)
            elif st.session_state.test_mode == "revision":
                update_daily_mission_revision(user)

            # Refresh Dashboard Stats
            old_level = st.session_state.get("xp_level", 1)
            dashboard_stats = safe_call(
                lambda: get_dashboard_stats(username),
                fallback=default_dashboard_stats(),
            )
            if dashboard_stats:
                st.session_state["tests_attempted"] = dashboard_stats.get("tests_attempted", 0)
                st.session_state["accuracy"] = dashboard_stats.get("accuracy", 0)
                st.session_state["streak"] = dashboard_stats.get("streak", 0)
                st.session_state["rank"] = dashboard_stats.get("rank", 0)
                st.session_state["weak_subject"] = dashboard_stats.get("weak_subject", "No Data")
                st.session_state["xp"] = dashboard_stats.get("xp", 0)
                new_level = dashboard_stats.get("level", 1)
                if new_level > old_level:
                    st.session_state["xp_level_up"] = True
                st.session_state["xp_level"] = new_level

            if st.session_state.get("xp_level_up"):
                st.balloons()
                st.success(f"🎉 LEVEL UP!\n\n🏆 Reached Level {st.session_state['xp_level']}")
                st.session_state["xp_level_up"] = False

            st.session_state.test_results_processed = True
            st.session_state.test_active = False
        st.session_state.pop("daily_test_config", None)

        st.session_state.test_qs = []

# =====================================================
# 📘 NOTES
# =====================================================

elif selected == "PYQ":

    safe_call(lambda: render_pyq_dashboard(section))


# =====================================================
# 📘 NOTES
# =====================================================

elif selected == "📚 Notes":

    safe_call(lambda: render_notes_page(section))


# =====================================================
# 🧠 WEAKNESS
# =====================================================

elif selected == "🧠 Weakness":

    safe_call(lambda: render_weakness_page(section, user))


# =====================================================
# 🔄 SMART REVISION
# =====================================================

elif selected == "🔄 Smart Revision":

    safe_call(lambda: render_revision_dashboard(user))


# =====================================================
# 🧬 LEARNING INTELLIGENCE
# =====================================================

elif selected == "🧬 Learning Intelligence":

    safe_call(lambda: render_learning_intelligence_dashboard(user))




# =====================================================
# 📊 PROGRESS
# =====================================================

elif selected == "📊 Progress":

    safe_call(lambda: render_progress_page(section, user))

# ---------------- LEADERBOARD ----------------
elif selected == "🏆 Leaderboard":

    safe_call(lambda: render_leaderboard(section))

# ---------------- AI TEACHER ----------------
elif selected == "🤖 AI Teacher":

    safe_call(lambda: render_teacher(section, user))

elif selected == "👨‍🏫 Personal Mentor":

    safe_call(lambda: render_mentor(section, typing_effect, user))

elif selected == "ℹ️ About":

    safe_call(lambda: render_about_page(section))

elif selected == "📞 Contact":

    safe_call(lambda: render_contact_page(section))

st.markdown("---")

st.caption("🚀 TNPSC AI • AI Powered TNPSC Preparation Platform")
