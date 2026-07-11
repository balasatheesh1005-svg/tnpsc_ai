import json
from datetime import datetime, timezone
from pathlib import Path

from core.question_engine.constants import (
    DEFAULT_BOOKMARK_PATH,
    DEFAULT_PROGRESS_PATH,
    DEFAULT_QUESTION_ROOT,
    DEFAULT_SOURCE,
    SOURCE_API,
    SOURCE_JSON,
    SOURCE_SUPABASE,
)
from core.question_engine.filters import filter_questions
from core.question_engine.loader import load_questions_from_path
from core.question_engine.models import QuestionStatistics
from core.question_engine.stats import count_by_field
from core.question_engine.validators import validate_questions


def _safe_read_store(path, default):
    try:
        store_path = Path(path)
        if not store_path.exists():
            return default
        with store_path.open("r", encoding="utf-8") as file:
            data = json.load(file)
        return data if isinstance(data, type(default)) else default
    except (FileNotFoundError, PermissionError, json.JSONDecodeError, OSError):
        return default


def _safe_write_store(path, data):
    try:
        store_path = Path(path)
        store_path.parent.mkdir(parents=True, exist_ok=True)
        with store_path.open("w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=2)
        return True
    except (PermissionError, TypeError, OSError):
        return False


def _load_from_json(root):
    return load_questions_from_path(root)


def _load_from_supabase(**_kwargs):
    return []


def _load_from_api(**_kwargs):
    return []


def get_questions(
    source=DEFAULT_SOURCE,
    root=DEFAULT_QUESTION_ROOT,
    filters=None,
    keyword=None,
    validate=False,
    **kwargs,
):
    """Return questions from the active backend using safe defaults."""
    try:
        if source == SOURCE_JSON:
            questions = _load_from_json(root)
        elif source == SOURCE_SUPABASE:
            questions = _load_from_supabase(**kwargs)
        elif source == SOURCE_API:
            questions = _load_from_api(**kwargs)
        else:
            questions = []

        if validate:
            result = validate_questions(questions)
            if not result.valid:
                return []

        return filter_questions(questions, criteria=filters, keyword=keyword)
    except Exception:
        return []


def get_question_by_id(question_id, source=DEFAULT_SOURCE, root=DEFAULT_QUESTION_ROOT, **kwargs):
    try:
        target = str(question_id or "")
        if not target:
            return None
        for question in get_questions(source=source, root=root, **kwargs):
            if str(question.get("id") or "") == target:
                return question
    except Exception:
        return None
    return None


def save_progress(user_id, progress, path=DEFAULT_PROGRESS_PATH):
    try:
        user_key = str(user_id or "anonymous")
        store = _safe_read_store(path, {})
        records = list(store.get(user_key, []))
        record = dict(progress or {})
        record["updated_at"] = record.get("updated_at") or datetime.now(timezone.utc).isoformat()
        records.append(record)
        store[user_key] = records
        return _safe_write_store(path, store)
    except Exception:
        return False


def load_progress(user_id, path=DEFAULT_PROGRESS_PATH):
    try:
        user_key = str(user_id or "anonymous")
        store = _safe_read_store(path, {})
        records = store.get(user_key, [])
        return records if isinstance(records, list) else []
    except Exception:
        return []


def get_bookmarks(user_id, path=DEFAULT_BOOKMARK_PATH):
    try:
        user_key = str(user_id or "anonymous")
        store = _safe_read_store(path, {})
        bookmarks = store.get(user_key, [])
        return bookmarks if isinstance(bookmarks, list) else []
    except Exception:
        return []


def save_bookmark(user_id, question_id, path=DEFAULT_BOOKMARK_PATH):
    try:
        question_key = str(question_id or "").strip()
        if not question_key:
            return False
        user_key = str(user_id or "anonymous")
        store = _safe_read_store(path, {})
        bookmarks = list(store.get(user_key, []))
        if question_key not in bookmarks:
            bookmarks.append(question_key)
        store[user_key] = bookmarks
        return _safe_write_store(path, store)
    except Exception:
        return False


def remove_bookmark(user_id, question_id, path=DEFAULT_BOOKMARK_PATH):
    try:
        question_key = str(question_id or "").strip()
        user_key = str(user_id or "anonymous")
        store = _safe_read_store(path, {})
        bookmarks = [item for item in store.get(user_key, []) if str(item) != question_key]
        store[user_key] = bookmarks
        return _safe_write_store(path, store)
    except Exception:
        return False


def get_statistics(source=DEFAULT_SOURCE, root=DEFAULT_QUESTION_ROOT, **kwargs):
    try:
        questions = get_questions(source=source, root=root, **kwargs)
        validation = validate_questions(questions)
        stats = QuestionStatistics(
            total_questions=len(questions),
            by_exam=dict(count_by_field(questions, "exam")),
            by_year=dict(count_by_field(questions, "year")),
            by_subject=dict(count_by_field(questions, "subject")),
            by_difficulty=dict(count_by_field(questions, "difficulty")),
            invalid_questions=len(validation.errors),
        )
        return stats.to_dict()
    except Exception:
        return QuestionStatistics().to_dict()

