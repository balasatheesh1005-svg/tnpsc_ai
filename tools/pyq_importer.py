"""Production-safe PYQ import utility for TNPSC Nova AI.

The importer is intentionally independent from the UI. It reads one or more
JSON files/directories, validates each question with the question engine
validators, skips invalid or duplicate rows, and appends accepted rows to the
JSON-backed question repository.
"""

import argparse
import json
import sys
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Sequence, Tuple

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from core.question_engine.constants import DEFAULT_QUESTION_ROOT, PYQ_REQUIRED_FIELDS, SOURCE_JSON
from core.question_engine.loader import iter_json_files, refresh_question_cache
from core.question_engine.models import Question
from core.question_engine.repository import get_questions
from core.question_engine.stats import count_by_field
from core.question_engine.validators import validate_question_schema


DEFAULT_IMPORT_FILE = "imported_pyq.json"


@dataclass
class ImportErrorDetail:
    file: str
    message: str
    question_id: str = ""
    index: Optional[int] = None
    level: str = "error"

    def to_dict(self) -> Dict[str, Any]:
        row = {
            "file": self.file,
            "message": self.message,
            "level": self.level,
        }
        if self.question_id:
            row["question_id"] = self.question_id
        if self.index is not None:
            row["index"] = self.index
        return row


@dataclass
class ImportSummary:
    imported_count: int = 0
    skipped_count: int = 0
    duplicate_count: int = 0
    invalid_count: int = 0
    subject_counts: Dict[str, int] = field(default_factory=dict)
    topic_counts: Dict[str, int] = field(default_factory=dict)
    year_counts: Dict[str, int] = field(default_factory=dict)
    errors: List[ImportErrorDetail] = field(default_factory=list)
    output_file: str = ""

    def to_dict(self) -> Dict[str, Any]:
        return {
            "imported_count": self.imported_count,
            "skipped_count": self.skipped_count,
            "duplicate_count": self.duplicate_count,
            "invalid_count": self.invalid_count,
            "subject_counts": dict(self.subject_counts),
            "topic_counts": dict(self.topic_counts),
            "year_counts": dict(self.year_counts),
            "errors": [error.to_dict() for error in self.errors],
            "output_file": self.output_file,
        }


def import_pyq_files(
    sources: Sequence[Path],
    destination_root: Path = DEFAULT_QUESTION_ROOT,
    output_file: Optional[Path] = None,
    error_log_path: Optional[Path] = None,
) -> Dict[str, Any]:
    """Import PYQ JSON files and return a crash-safe summary dictionary."""
    summary = ImportSummary()

    try:
        source_paths = [Path(source) for source in sources or []]
        destination_root = Path(destination_root)
        output_path = _resolve_output_path(destination_root, output_file)
        summary.output_file = str(output_path)

        imported_rows = _load_import_candidates(source_paths, summary)
        existing_ids = _load_existing_ids(destination_root, summary)
        duplicate_ids = _find_duplicate_import_ids(imported_rows)

        valid_questions = []
        for source_file, index, row in imported_rows:
            question_id = _question_id(row)

            if not question_id:
                _mark_invalid(summary, source_file, index, question_id, ["missing required field: id"])
                continue

            if question_id in existing_ids or question_id in duplicate_ids:
                summary.duplicate_count += 1
                summary.errors.append(
                    ImportErrorDetail(
                        file=str(source_file),
                        index=index,
                        question_id=question_id,
                        message="duplicate question id",
                    )
                )
                continue

            validation = validate_question_schema(row, required_fields=PYQ_REQUIRED_FIELDS)
            if not validation.valid:
                _mark_invalid(summary, source_file, index, question_id, validation.errors)
                continue

            valid_questions.append(Question.from_dict(row).to_dict())
            existing_ids.add(question_id)

            for warning in validation.warnings:
                summary.errors.append(
                    ImportErrorDetail(
                        file=str(source_file),
                        index=index,
                        question_id=question_id,
                        message=warning,
                        level="warning",
                    )
                )

        if valid_questions:
            saved = _append_questions(output_path, valid_questions, summary)
            if saved:
                summary.imported_count = len(valid_questions)
                _populate_counts(summary, valid_questions)
                refresh_question_cache()
            else:
                summary.invalid_count += len(valid_questions)
                summary.errors.append(
                    ImportErrorDetail(file=str(output_path), message="valid questions could not be saved")
                )

        summary.skipped_count = summary.duplicate_count + summary.invalid_count

        if error_log_path:
            _write_error_log(Path(error_log_path), summary)

        return summary.to_dict()
    except Exception as exc:
        summary.errors.append(ImportErrorDetail(file="", message=f"unexpected importer error: {exc}"))
        summary.skipped_count = summary.duplicate_count + summary.invalid_count
        return summary.to_dict()


def _load_import_candidates(
    sources: Sequence[Path],
    summary: ImportSummary,
) -> List[Tuple[Path, int, Dict[str, Any]]]:
    candidates = []

    for file_path in _iter_source_files(sources, summary):
        for index, row in _read_questions_from_file(file_path, summary):
            candidates.append((file_path, index, row))

    return candidates


def _iter_source_files(sources: Sequence[Path], summary: ImportSummary) -> Iterable[Path]:
    seen = set()

    if not sources:
        summary.errors.append(ImportErrorDetail(file="", message="no import source provided"))
        return []

    files = []
    for source in sources:
        try:
            if source.is_file() and source.suffix.lower() == ".json":
                files.append(source)
            elif source.is_dir():
                files.extend(iter_json_files(source))
            else:
                summary.errors.append(ImportErrorDetail(file=str(source), message="source is not a JSON file or directory"))
        except OSError as exc:
            summary.errors.append(ImportErrorDetail(file=str(source), message=f"source could not be inspected: {exc}"))

    unique_files = []
    for file_path in files:
        resolved = str(file_path.resolve()) if file_path.exists() else str(file_path)
        if resolved not in seen:
            unique_files.append(file_path)
            seen.add(resolved)
    return unique_files


def _read_questions_from_file(path: Path, summary: ImportSummary) -> List[Tuple[int, Dict[str, Any]]]:
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except json.JSONDecodeError as exc:
        summary.errors.append(ImportErrorDetail(file=str(path), message=f"invalid JSON: {exc}"))
        return []
    except (FileNotFoundError, PermissionError, OSError) as exc:
        summary.errors.append(ImportErrorDetail(file=str(path), message=f"file could not be read: {exc}"))
        return []
    except Exception as exc:
        summary.errors.append(ImportErrorDetail(file=str(path), message=f"unexpected read error: {exc}"))
        return []

    rows = _extract_question_rows(data)
    if rows is None:
        summary.errors.append(ImportErrorDetail(file=str(path), message="JSON must be a question object, a list, or an object with a questions list"))
        return []

    questions = []
    for index, item in enumerate(rows, start=1):
        if isinstance(item, dict):
            questions.append((index, item))
        else:
            summary.invalid_count += 1
            summary.errors.append(
                ImportErrorDetail(file=str(path), index=index, message="invalid schema: question must be a dictionary")
            )
    return questions


def _extract_question_rows(data: Any) -> Optional[List[Any]]:
    if isinstance(data, list):
        return data
    if isinstance(data, dict):
        if isinstance(data.get("questions"), list):
            return data["questions"]
        if "id" in data or "question_en" in data or "question_ta" in data:
            return [data]
    return None


def _load_existing_ids(destination_root: Path, summary: ImportSummary) -> set:
    try:
        questions = get_questions(source=SOURCE_JSON, root=destination_root)
        return {_question_id(question) for question in questions if _question_id(question)}
    except Exception as exc:
        summary.errors.append(
            ImportErrorDetail(file=str(destination_root), message=f"existing repository ids could not be loaded: {exc}")
        )
        return set()


def _find_duplicate_import_ids(rows: Sequence[Tuple[Path, int, Dict[str, Any]]]) -> set:
    counts = Counter(_question_id(row) for _, _, row in rows if _question_id(row))
    return {question_id for question_id, count in counts.items() if count > 1}


def _question_id(question: Dict[str, Any]) -> str:
    try:
        return str((question or {}).get("id") or "").strip()
    except Exception:
        return ""


def _mark_invalid(
    summary: ImportSummary,
    source_file: Path,
    index: int,
    question_id: str,
    messages: Sequence[str],
) -> None:
    summary.invalid_count += 1
    for message in messages or ["invalid question"]:
        summary.errors.append(
            ImportErrorDetail(
                file=str(source_file),
                index=index,
                question_id=question_id,
                message=message,
            )
        )


def _resolve_output_path(destination_root: Path, output_file: Optional[Path]) -> Path:
    if output_file:
        output_path = Path(output_file)
        return output_path if output_path.is_absolute() else destination_root / output_path
    return destination_root / DEFAULT_IMPORT_FILE


def _append_questions(output_path: Path, questions: Sequence[Dict[str, Any]], summary: ImportSummary) -> bool:
    try:
        existing = []
        if output_path.exists():
            with output_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            if isinstance(data, list):
                existing = [item for item in data if isinstance(item, dict)]
            elif isinstance(data, dict) and isinstance(data.get("questions"), list):
                existing = [item for item in data["questions"] if isinstance(item, dict)]
            else:
                summary.errors.append(
                    ImportErrorDetail(file=str(output_path), message="output file has unsupported JSON shape")
                )
                return False

        output_path.parent.mkdir(parents=True, exist_ok=True)
        with output_path.open("w", encoding="utf-8") as file:
            json.dump(existing + list(questions), file, ensure_ascii=False, indent=2)
            file.write("\n")
        return True
    except (PermissionError, TypeError, json.JSONDecodeError, OSError) as exc:
        summary.errors.append(ImportErrorDetail(file=str(output_path), message=f"save failed: {exc}"))
        return False
    except Exception as exc:
        summary.errors.append(ImportErrorDetail(file=str(output_path), message=f"unexpected save error: {exc}"))
        return False


def _populate_counts(summary: ImportSummary, questions: Sequence[Dict[str, Any]]) -> None:
    summary.subject_counts = dict(count_by_field(questions, "subject"))
    summary.topic_counts = dict(count_by_field(questions, "topic"))
    summary.year_counts = dict(count_by_field(questions, "year"))


def _write_error_log(path: Path, summary: ImportSummary) -> bool:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        payload = {
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "summary": summary.to_dict(),
        }
        with path.open("w", encoding="utf-8") as file:
            json.dump(payload, file, ensure_ascii=False, indent=2)
            file.write("\n")
        return True
    except Exception:
        return False


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Import TNPSC PYQ JSON files safely.")
    parser.add_argument("sources", nargs="+", help="JSON files or directories to import.")
    parser.add_argument("--destination-root", default=str(DEFAULT_QUESTION_ROOT), help="Question repository root.")
    parser.add_argument("--output-file", default=None, help="Output JSON file name/path. Relative paths live under destination root.")
    parser.add_argument("--error-log", default=None, help="Optional detailed error log JSON path.")
    return parser


def main(argv: Optional[Sequence[str]] = None) -> int:
    try:
        args = _build_parser().parse_args(argv)
        summary = import_pyq_files(
            sources=[Path(source) for source in args.sources],
            destination_root=Path(args.destination_root),
            output_file=Path(args.output_file) if args.output_file else None,
            error_log_path=Path(args.error_log) if args.error_log else None,
        )
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return 0
    except SystemExit as exc:
        return int(exc.code or 0)
    except Exception as exc:
        payload = ImportSummary(
            errors=[ImportErrorDetail(file="", message=f"unexpected CLI error: {exc}")]
        ).to_dict()
        print(json.dumps(payload, ensure_ascii=False, indent=2))
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
