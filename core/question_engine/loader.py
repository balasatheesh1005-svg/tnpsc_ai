import json
from functools import lru_cache
from pathlib import Path


def safe_read_json(path):
    """Read a question JSON file and return a list of question dictionaries."""
    try:
        with Path(path).open("r", encoding="utf-8") as file:
            data = json.load(file)
    except (FileNotFoundError, PermissionError, json.JSONDecodeError, OSError):
        return []

    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]

    if isinstance(data, dict):
        questions = data.get("questions")
        if isinstance(questions, list):
            return [item for item in questions if isinstance(item, dict)]
        if "id" in data or "question_en" in data or "question_ta" in data:
            return [data]

    return []


def iter_json_files(root, recursive=True):
    """Safely list JSON files below a root path."""
    root_path = Path(root)
    if not root_path.exists() or not root_path.is_dir():
        return []

    try:
        pattern = "**/*.json" if recursive else "*.json"
        return sorted(path for path in root_path.glob(pattern) if path.is_file())
    except OSError:
        return []


@lru_cache(maxsize=64)
def _load_questions_cached(root, recursive=True):
    questions = []
    for file_path in iter_json_files(root, recursive=recursive):
        questions.extend(safe_read_json(file_path))
    return tuple(questions)


def load_questions_from_path(root, recursive=True):
    """Load all question dictionaries under a root path without crashing."""
    return list(_load_questions_cached(str(root), recursive))


def refresh_question_cache():
    """Clear cached question JSON data after files are changed."""
    _load_questions_cached.cache_clear()

