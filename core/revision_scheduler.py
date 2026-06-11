from core.revision_ai import (
    get_due_revisions as _get_due_revisions,
    get_revision_overview as _get_revision_overview,
)


def get_due_revisions(username):
    """Return a list of due revision topic keys and their due dates."""
    return _get_due_revisions(username)


def get_revision_count(username):
    """Return the count of revisions due for the user."""
    return len(_get_due_revisions(username))


def get_top_due_revisions(username, limit=3):
    """Return the top N due revision topic keys for the user."""
    return [topic for topic, _due in _get_due_revisions(username)[:limit]]


def get_revision_overview(username):
    """Return a full revision queue overview grouped by overdue, due today, and upcoming."""
    return _get_revision_overview(username)


def get_revision_queue(username, limit=8):
    overview = _get_revision_overview(username)
    return overview["queue"][:limit]
