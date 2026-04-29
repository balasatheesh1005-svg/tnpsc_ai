from core.mentor_memory import get_memory

def ai_coach(user, score, total, weak_data):

    memory = get_memory(user)

    percent = int((score / total) * 100) if total else 0

    last_score = memory.get("last_score")
    weak_topics = memory.get("weak_topics", [])

    message = f"Hey {user}! 👋\n\n"

    message += f"🎯 Current Score: {percent}%\n"

    if last_score is not None:
        if percent > last_score:
            message += "📈 Improvement from last test! Great job 🔥\n"
        elif percent < last_score:
            message += "📉 Score dropped. Let's focus more 💪\n"

    if weak_topics:
        message += f"\n🧠 Your weak areas: {', '.join(weak_topics)}\n"

    message += "\n📅 Today's Plan:\n"
    message += "- Revise weak topic\n- Take 1 test\n- Study 20 mins\n"

    return message