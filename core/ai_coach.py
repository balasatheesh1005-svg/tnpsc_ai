from core.mentor_memory import get_memory
from core.streak_ai import get_streak

def ai_coach(user, score, total, weak_data):

    memory = get_memory(user)

    percent = int((score / total) * 100) if total else 0

    last_score = memory.get("last_score")
    weak_topics = memory.get("weak_topics", [])

    message = f"Hey {user}! 👋\n\n"

    # 🎯 Score
    message += f"🎯 You scored {percent}% this time.\n"

    # 📈 Improvement
    if last_score is not None:
        if percent > last_score:
            message += "🔥 Much better than your last attempt. You're improving fast!\n"
        elif percent < last_score:
            message += "⚠️ Slight drop from last test. Let's get back on track.\n"
        else:
            message += "👍 Same as last time. Let's push further!\n"

    # 🧠 Weak topics clean
    clean_topics = []
    for t in weak_topics:
        try:
            topic_name = t.split("-")[1].replace("_", " ").title()
            clean_topics.append(topic_name)
        except:
            clean_topics.append(t)

    if clean_topics:
        message += f"\n🧠 Focus on: {', '.join(clean_topics)}\n"
        message += f"👉 Spend extra time on {clean_topics[0]} today.\n"

    # 🔥 Streak
    streak = get_streak(user)
    if streak >= 3:
        message += f"\n🔥 You're on a {streak}-day streak. Keep it going!\n"

    # 📅 Plan
    message += "\n📅 Today's Plan:\n"
    message += "- Revise weak topic\n- Take 1 test\n- Study 20 mins\n"

    # 💪 Closing
    message += "\n💪 Stay consistent. I'm with you every day."

    return message