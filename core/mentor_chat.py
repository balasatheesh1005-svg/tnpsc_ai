import pandas as pd
from core.dashboard_stats_ai import get_dashboard_stats
from core.weakness_ai import get_weakness
from core.revision_scheduler import (
    get_revision_overview,
)  # Using the scheduler's overview
from core.xp_ai import get_user_xp, get_level_progress
from core.daily_mission_ai import get_mission_progress
from core.progress_ai import get_progress  # For strong subject calculation


def mentor_reply(message, user):
    message_lower = message.lower()

    # Fetch all necessary data
    dashboard_stats = get_dashboard_stats(user)
    xp_data = get_user_xp(user)
    level_progress = get_level_progress(user)
    mission_progress = get_mission_progress(user)
    weak_data = get_weakness(user)
    revision_overview = get_revision_overview(user)
    user_progress_records = get_progress(user)  # For strong subject calculation

    # Extract data for responses
    accuracy = dashboard_stats.get("accuracy", 0)
    rank = dashboard_stats.get("rank", 0)
    current_xp = xp_data.get("xp", 0)
    current_level = xp_data.get("level", 1)
    xp_for_next_level = level_progress.get("xp_for_next", 0)
    next_level = level_progress.get("next_level", current_level)
    weak_subject_dashboard = dashboard_stats.get("weak_subject", "No Data")

    # Calculate strong_subject (replicate logic from ui/pages/mentor.py)
    strong_subject = "No Data"
    if user_progress_records:
        progress_df = pd.DataFrame(user_progress_records)
        if not progress_df.empty and "accuracy" in progress_df.columns:
            progress_df["accuracy"] = pd.to_numeric(
                progress_df["accuracy"], errors="coerce"
            ).fillna(0)
            progress_df["subject"] = (
                progress_df["subject"].fillna("Unknown").astype(str)
            )
            subject_avg = (
                progress_df.groupby("subject")["accuracy"]
                .mean()
                .sort_values(ascending=False)
            )
            if not subject_avg.empty:
                strong_subject = subject_avg.index[0].title()

    # --- Response Logic ---

    if "weak topic" in message_lower or "weakness" in message_lower:
        if weak_subject_dashboard != "No Data":
            return f"Your current weakest area is: **{weak_subject_dashboard}**. Focus on revising this topic."
        else:
            return "You don't have a clearly identified weak topic yet. Keep practicing to help me identify one!"

    elif "strong topic" in message_lower or "strength" in message_lower:
        if strong_subject != "No Data":
            return (
                f"Your strongest area is: **{strong_subject}**. Keep up the great work!"
            )
        else:
            return "I haven't identified a strong topic for you yet. Keep practicing to help me find your strengths!"

    elif "accuracy" in message_lower:
        return f"Your overall average accuracy is: **{accuracy}%**."

    elif "rank" in message_lower:
        if rank > 0:
            return f"You are currently ranked **#{rank}** on the leaderboard. Keep climbing!"
        else:
            return "You are not yet ranked on the leaderboard. Complete more tests to get a rank!"

    elif "xp" in message_lower:
        return f"You have **{current_xp} XP**."

    elif "level" in message_lower:
        return f"You are currently at **Level {current_level}**. You need **{xp_for_next_level} XP** to reach Level {next_level}."

    elif "revision" in message_lower:
        total_revisions = revision_overview.get("total", 0)
        overdue = len(revision_overview.get("overdue", []))
        due_today = len(revision_overview.get("due_today", []))
        upcoming = len(revision_overview.get("upcoming", []))

        if total_revisions > 0:
            response = f"You have **{total_revisions} revisions** in your queue. "
            if overdue > 0:
                response += f"**{overdue} are overdue!** "
            if due_today > 0:
                response += f"**{due_today} are due today.** "
            if upcoming > 0:
                response += f"{upcoming} are upcoming. "
            response += "Focus on clearing your overdue and today's revisions."
            return response
        else:
            return (
                "You have no revisions due. Great job staying on top of your studies!"
            )

    elif "mission" in message_lower or "daily mission" in message_lower:
        daily_test_completed = mission_progress.get("daily_test_completed")
        revision_count = mission_progress.get("revision_count", 0)
        questions_answered = mission_progress.get("questions_answered", 0)
        completed_count = mission_progress.get("completed_count", 0)

        response = f"Your daily mission progress: \n"
        response += f"- Daily Test: {'✅ Completed' if daily_test_completed else '⬜ Not Completed'}\n"
        response += f"- Revisions: {'✅ Completed' if revision_count >= 2 else f'⬜ {revision_count}/2 Completed'}\n"
        response += f"- Questions: {'✅ Completed' if questions_answered >= 20 else f'⬜ {questions_answered}/20 Answered'}\n"
        response += f"You have completed **{completed_count}/3** missions today."
        if completed_count == 3:
            response += " You can claim your 🎁 +100 XP reward!"
        else:
            response += " Keep going to complete all missions and earn your reward!"
        return response

    elif "study plan" in message_lower or "what next" in message_lower:
        # Simple rule-based study plan
        if weak_subject_dashboard != "No Data":
            return f"Your immediate next step should be to **revise {weak_subject_dashboard}**. After that, attempt a practice test."
        elif revision_overview.get("total", 0) > 0:
            return "You have pending revisions. Prioritize completing your **due revisions**."
        else:
            return "Keep up your daily practice! Focus on completing your daily test and maintaining your streak."

    else:
        return """I can help with:
• weak topic
• strong topic
• accuracy
• rank
• xp
• level
• revision
• mission
• study plan
"""
