import datetime
import logging
from typing import Dict, List, Any, Optional
import streamlit as st

from core.mentor_memory import get_memory
from core.progress_ai import get_progress
from core.revision_engine import (
    get_intelligent_revision_plan,
    get_revision_analytics_v2,
)
from core.streak_ai import get_streak
from core.weakness_ai import get_weakness
from core.xp_ai import get_level_progress, get_user_xp

logger = logging.getLogger(__name__)


def format_subject_name(subject: str) -> str:
    """Helper to format subject name cleanly."""
    if not subject:
        return "General"
    return str(subject).replace("_", " ").replace("-", " ").title()


def format_topic_name(topic: str) -> str:
    """Helper to format topic name cleanly."""
    if not topic:
        return "General"
    return str(topic).replace("_", " ").replace("-", " ").title()



def _calculate_star_rating(value: float, min_val: float = 0, max_val: float = 100) -> int:
    """Helper to convert continuous metric to 1-5 star integer rating."""
    if value <= min_val:
        return 1
    pct = (value - min_val) / (max_val - min_val)
    if pct < 0.2:
        return 1
    elif pct < 0.4:
        return 2
    elif pct < 0.6:
        return 3
    elif pct < 0.8:
        return 4
    else:
        return 5


from core.performance import measure_time, record_cache_hit, record_cache_miss
from core.engine_cache import ENGINE_CACHE_KEY_PREFIX


@measure_time("Learning Intelligence Engine")
def get_learning_intelligence(
    user: str = None, context: Optional[Any] = None, force_refresh: bool = False
) -> Dict[str, Any]:
    """
    Learning Intelligence Engine V2 - Single Source of Truth.
    Synthesizes data across Progress, Weakness, Revision V2, XP, Streak, and Memory engines
    to determine WHY the student is weak and generate actionable recovery intelligence.
    """
    user_str = str(user or "Guest")
    cache_key = f"{ENGINE_CACHE_KEY_PREFIX}Learning Intelligence Engine_{user_str}"
    if hasattr(st, "session_state") and not force_refresh and cache_key in st.session_state:
        record_cache_hit("Learning Intelligence Engine")
        return st.session_state[cache_key]
    record_cache_miss("Learning Intelligence Engine")

    from core.user_context import UserContext
    ctx = context or UserContext.get_or_create(user)

    # 1. Fetch Engine Data using shared context
    progress_rows = get_progress(user, context=ctx)
    weakness_data = get_weakness(user, context=ctx)
    revision_plan = get_intelligent_revision_plan(user, context=ctx)
    revision_analytics = get_revision_analytics_v2(user, context=ctx)
    streak = get_streak(user, context=ctx)
    xp_data = get_user_xp(user, context=ctx)
    memory = get_memory(user, context=ctx)

    # 2. Analyze Subject & Topic Performance Breakdowns
    all_accuracies = [float(r.get("accuracy", 0)) for r in progress_rows if r.get("accuracy") is not None]
    overall_acc = sum(all_accuracies) / len(all_accuracies) if all_accuracies else 0.0

    # Categorize accuracies by sub-repository pattern
    foundation_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "easy" in str(r.get("topic", "")).lower() or "notes" in str(r.get("topic", "")).lower()]
    medium_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "medium" in str(r.get("topic", "")).lower()]
    hard_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "hard" in str(r.get("topic", "")).lower()]
    assertion_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "assertion" in str(r.get("topic", "")).lower()]
    statement_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "statement" in str(r.get("topic", "")).lower()]
    chronology_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "chronology" in str(r.get("topic", "")).lower()]
    pyq_accs = [float(r.get("accuracy", 0)) for r in progress_rows if "pyq" in str(r.get("topic", "")).lower()]

    avg_foundation = sum(foundation_accs) / len(foundation_accs) if foundation_accs else (overall_acc if overall_acc else 75.0)
    avg_hard = sum(hard_accs) / len(hard_accs) if hard_accs else (overall_acc * 0.75 if overall_acc else 45.0)
    avg_assertion = sum(assertion_accs) / len(assertion_accs) if assertion_accs else (avg_hard * 0.85 if avg_hard else 38.0)
    avg_statement = sum(statement_accs) / len(statement_accs) if statement_accs else (avg_hard * 0.9 if avg_hard else 48.0)
    avg_chronology = sum(chronology_accs) / len(chronology_accs) if chronology_accs else 50.0

    # 3. Determine Root Cause
    if avg_assertion < 55:
        root_cause = "Concept Application"
        root_explanation = "Foundational knowledge is intact, but higher-order logical linking in Assertion & Reason requires practice."
    elif avg_chronology < 55:
        root_cause = "Chronological Recall"
        root_explanation = "Historical event sequences and timeline dates require spaced chronological ordering revision."
    elif avg_statement < 55:
        root_cause = "Multi-Statement Analysis"
        root_explanation = "Evaluating multiple statement combinations (1, 2 only vs All correct) requires process-of-elimination techniques."
    elif avg_hard < 55:
        root_cause = "Application Skills"
        root_explanation = "Difficulty spikes in Hard repository questions reveal a need for deeper concept integration."
    elif overall_acc < 50:
        root_cause = "Foundational Knowledge Gap"
        root_explanation = "Key terms and definitions require initial study notes review before attempting mock tests."
    else:
        root_cause = "Timed Performance Stress"
        root_explanation = "Accuracy drops slightly under test conditions. Practice consistent timed sets to solidify recall."

    # 4. Determine Learning Bottleneck
    subj = revision_plan.get("level1_subject", "History")
    topic = revision_plan.get("level2_topic", "Modern India")
    repo = revision_plan.get("level3_repository", "Hard Repository")
    qtype = revision_plan.get("level4_question_type", "Assertion & Reason")
    bottleneck_acc = revision_plan.get("accuracy", 38.0)

    learning_bottleneck = f"{subj} ↓ {topic} ↓ {repo} ↓ {qtype}"

    # 5. Determine Learning Strength & Weakness
    if avg_foundation >= 75:
        learning_strength = "Foundational Knowledge & Key Terms"
    elif streak >= 5:
        learning_strength = "Daily Consistency & Study Habit"
    else:
        learning_strength = "Topic Familiarity"

    learning_weakness = f"{qtype} ({bottleneck_acc}% Accuracy)"

    # 6. Generate Rule-Based 4-Step Recovery Plan
    recovery_plan = [
        f"Step 1: Revise {qtype} notes & key concepts",
        f"Step 2: Practice targeted {repo} practice set",
        f"Step 3: Attempt {subj} PYQ Repository questions",
        f"Step 4: Take full Grand Test to verify topic mastery",
    ]

    # 7. Calculate Estimated Recovery Sessions & Time
    if bottleneck_acc < 45:
        estimated_recovery = "3 Sessions (2 Revision Cycles)"
        rec_sessions_count = 3
    elif bottleneck_acc < 65:
        estimated_recovery = "2 Sessions (1 Revision Cycle)"
        rec_sessions_count = 2
    else:
        estimated_recovery = "1 Focused Session"
        rec_sessions_count = 1

    # 8. Calculate Topic Mastery Probability
    current_mastery = round(bottleneck_acc, 1)
    projected_mastery = min(95.0, round(current_mastery + (15.0 * rec_sessions_count), 1))

    # 9. Calculate 8-Dimension Learning DNA (1 to 5 Stars)
    revision_prog = revision_analytics.get("progress", {})
    rev_pct = revision_prog.get("percentage", 80)

    learning_dna = {
        "knowledge": _calculate_star_rating(avg_foundation, 40, 100),
        "memory": _calculate_star_rating(overall_acc, 30, 95),
        "application": _calculate_star_rating(avg_hard, 30, 95),
        "analysis": _calculate_star_rating(avg_assertion, 30, 95),
        "speed": _calculate_star_rating(min(100, len(progress_rows) * 10), 10, 100),
        "accuracy": _calculate_star_rating(overall_acc, 30, 95),
        "consistency": _calculate_star_rating(streak, 0, 7),
        "revision": _calculate_star_rating(rev_pct, 20, 100),
    }

    # 10. Generate Current Recommendation & Mentor Insight (Rule-Based Templates, NO LLM)
    recommendation = (
        f"Focus {rec_sessions_count} focused sessions on {qtype} in {topic} "
        f"to elevate Topic Mastery from {current_mastery}% to {projected_mastery}%."
    )

    if learning_dna["application"] <= 2:
        mentor_insight = "Your conceptual knowledge is strong. Focus on concept application to push your score higher."
    elif "Assertion" in qtype:
        mentor_insight = "Your biggest improvement opportunity is Assertion & Reason. Master this pattern to secure top rank."
    elif projected_mastery >= 85:
        mentor_insight = f"One more revision cycle will likely push {topic} above 90% topic mastery."
    elif overall_acc >= 80:
        mentor_insight = "Grand Test revision is now highly recommended."
    else:
        mentor_insight = "Executing your recovery plan consistently will build solid topic mastery."

    # 11. Final Engine Output JSON Schema
    result = {
        "subject": subj,
        "topic": topic,
        "repository": repo,
        "question_type": qtype,
        "difficulty": revision_plan.get("level5_difficulty", "Hard"),
        "learning_strength": learning_strength,
        "learning_weakness": learning_weakness,
        "root_cause": root_cause,
        "root_explanation": root_explanation,
        "learning_bottleneck": learning_bottleneck,
        "recovery_plan": recovery_plan,
        "estimated_recovery": estimated_recovery,
        "current_mastery": current_mastery,
        "mastery_probability": projected_mastery,
        "learning_dna": learning_dna,
        "recommendation": recommendation,
        "mentor_insight": mentor_insight,
    }

    if hasattr(st, "session_state"):
        st.session_state[cache_key] = result

    return result
