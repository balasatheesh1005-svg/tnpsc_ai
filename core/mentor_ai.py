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


def mentor_insights(
    accuracy,
    streak,
    weak_subject,
    strong_subject,
    tests_attempted,
    due_revisions=0,
):
    """Generate structured mentor guidance using rule-based logic."""

    def _normalize_value(value, default=0.0):
        try:
            return float(value)
        except (TypeError, ValueError):
            return float(default)

    accuracy_value = max(0.0, min(100.0, _normalize_value(accuracy, 0.0)))
    streak_value = int(max(0, _normalize_value(streak, 0)))
    tests_value = int(max(0, _normalize_value(tests_attempted, 0)))

    if not weak_subject or weak_subject == "No Data":
        weak_label = "your current focus area"
    else:
        weak_label = weak_subject

    if not strong_subject or strong_subject == "No Data":
        strong_label = "your strongest area"
    else:
        strong_label = strong_subject

    if accuracy_value < 50:
        message = (
            f"Your foundation needs reinforcement. Start with quick revision in {weak_label} "
            "and build confidence through short, focused practice sessions."
        )
        revision = f"Review fundamentals in {weak_label}."
        practice = f"Attempt 5 practice questions focused on {weak_label}."
        goal = "Reach 50% accuracy over the next two tests."
        time = "30 minutes"
    elif accuracy_value < 70:
        message = (
            f"Nice progress — keep the momentum going. Continue revising {weak_label} "
            "and use timed practice to improve consistency."
        )
        revision = f"Revise key concepts in {weak_label}."
        practice = "Complete one targeted practice set and review each mistake."
        goal = "Push accuracy above 70%."
        time = "45 minutes"
    elif accuracy_value < 85:
        message = f"Strong performance. Polish {weak_label} and reinforce your strength in {strong_label}."
        revision = f"Review challenging points in {weak_label}."
        practice = "Take a mixed-topic timed test and analyze errors."
        goal = "Maintain accuracy above 80%."
        time = "50 minutes"
    else:
        message = f"Excellent work. Keep your streak alive with focused revision and high-quality practice."
        revision = f"Fine-tune {weak_label} and revisit high-value concepts."
        practice = "Attempt one full timed set with review."
        goal = "Sustain 85%+ accuracy."
        time = "40 minutes"

    if streak_value < 3:
        message += " Keep a running streak by practicing on consecutive days."

    if tests_value < 5:
        practice = "Build confidence with 3 short quizzes this week."

    if due_revisions > 0:
        message += f" 📚 You have {due_revisions} pending revisions today."

    return {
        "message": message,
        "revision": revision,
        "practice": practice,
        "goal": goal,
        "time": time,
    }
