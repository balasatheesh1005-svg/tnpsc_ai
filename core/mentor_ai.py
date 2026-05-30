from core.weakness_ai import get_weakness
from core.progress_ai import get_progress

# ====================================
# PERSONAL MENTOR
# ====================================


def mentor_advice(user):

    weak_data = get_weakness(user)

    progress = get_progress(user)

    # =========================
    # DEFAULT
    # =========================

    if not progress:

        return """

🚀 Welcome to Nova AI Mentor

Start practicing daily tests.

Consistency is the key to TNPSC success 🔥
"""

    # =========================
    # ACCURACY
    # =========================

    accuracies = []

    for row in progress:

        accuracy = row.get("accuracy")

        if accuracy is not None:

            accuracies.append(float(accuracy))

    if not accuracies:

        return """

ðŸš€ Welcome to Nova AI Mentor

Start practicing daily tests.

Consistency is the key to TNPSC success ðŸ”¥
"""

    avg_accuracy = sum(accuracies) / len(accuracies)

    # =========================
    # WEAK TOPIC
    # =========================

    if weak_data:

        weak_topic = max(weak_data, key=weak_data.get)

        weak_msg = f"⚠️ Focus more on:\n" f"{weak_topic.replace('-', ' → ')}"

    else:

        weak_msg = "🔥 No major weakness detected"

    # =========================
    # MOTIVATION
    # =========================

    if avg_accuracy >= 80:

        motivation = (
            "🚀 Excellent performance!\n" "You are progressing toward Top Rank."
        )

    elif avg_accuracy >= 60:

        motivation = "👍 Good improvement.\n" "Increase revision consistency."

    else:

        motivation = "⚠️ Need stronger preparation.\n" "Practice daily tests regularly."

    # =========================
    # FINAL RESPONSE
    # =========================

    return f"""

🧠 NOVA AI PERSONAL MENTOR

📊 Average Accuracy:
{round(avg_accuracy, 1)}%

{weak_msg}

{motivation}

📚 Suggested Action:
1. Practice Weak Topics
2. Complete Revisions
3. Maintain Daily Streak

🔥 Keep pushing toward your TNPSC goal
"""
