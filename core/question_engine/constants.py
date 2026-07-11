from pathlib import Path


DEFAULT_QUESTION_ROOT = Path("data/pyq")
DEFAULT_PROGRESS_PATH = Path("data/question_engine_progress.json")
DEFAULT_BOOKMARK_PATH = Path("data/question_engine_bookmarks.json")

SOURCE_JSON = "json"
SOURCE_SUPABASE = "supabase"
SOURCE_API = "api"

DEFAULT_SOURCE = SOURCE_JSON

OPTION_KEYS = ("A", "B", "C", "D")

REQUIRED_QUESTION_FIELDS = (
    "id",
    "question_en",
    "options",
    "correct_answer",
)

PYQ_REQUIRED_FIELDS = (
    "id",
    "exam",
    "year",
    "subject",
    "topic",
    "difficulty",
    "question_en",
    "question_ta",
    "options",
    "correct_answer",
    "explanation",
)

