def ai_coach(user, score, total, weak_data):

    percent = int((score / total) * 100) if total else 0

    weak_topics = list(weak_data.keys())[:2]

    message = f"""
🎯 Score: {percent}%

Hey {user}! 👋

"""

    if percent >= 80:
        message += "🔥 Excellent performance! You're exam ready.\n"
    elif percent >= 50:
        message += "👍 Good effort! Improve weak areas.\n"
    else:
        message += "⚠️ You need more practice. Don't worry.\n"

    if weak_topics:
        message += f"\n🧠 Focus: {', '.join(weak_topics)}\n"

    message += "\n📅 Today's Task:\n"
    message += "- Revise weak topic\n- Take 1 test\n- Study 20 mins\n"

    message += "\n🤖 I'm your personal AI mentor 💪"

    return message