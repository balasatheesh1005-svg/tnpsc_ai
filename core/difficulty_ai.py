from core.progress_ai import get_progress

def get_user_level(user, last_score=0):

    if last_score >= 80:
        return "hard"
    elif last_score >= 50:
        return "medium"
    else:
        return "easy"