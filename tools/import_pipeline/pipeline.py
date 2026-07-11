"""Run the official TNPSC PYQ import pipeline.

Usage:
    python tools/import_pipeline/pipeline.py paper.pdf
"""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from tools.import_pipeline.ai_enrichment import enrich_placeholders
from tools.import_pipeline.answerkey_linker import link_answer_key
from tools.import_pipeline.pdf_extractor import extract_pdf
from tools.import_pipeline.question_normalizer import normalize_questions
from tools.import_pipeline.question_validator import validate_questions_file
from tools.import_pipeline.repository_import import import_to_repository


def run_pipeline(pdf_path, work_dir=None, exam="Group 1", year=2011, subject="General Knowledge") -> Dict[str, Any]:
    """Execute every pipeline stage and return a complete summary."""
    started_at = datetime.now().strftime("%Y%m%d_%H%M%S")
    workspace = Path(work_dir or Path("tools/import_pipeline/runs") / started_at)
    workspace.mkdir(parents=True, exist_ok=True)

    summary = {
        "input_pdf": str(pdf_path),
        "work_dir": str(workspace),
        "stages": {},
        "errors": [],
    }

    try:
        raw_path = workspace / "raw_questions.json"
        normalized_path = workspace / "normalized_questions.json"
        validated_path = workspace / "validated_questions.json"
        validation_report_path = workspace / "validation_report.json"
        verified_path = workspace / "verified_questions.json"
        enriched_path = workspace / "enriched_questions.json"
        pipeline_log_path = workspace / "pipeline_log.json"

        _print_stage("Extract")
        summary["stages"]["extract"] = extract_pdf(pdf_path, raw_path)

        _print_stage("Normalize")
        summary["stages"]["normalize"] = normalize_questions(
            raw_path,
            normalized_path,
            exam=exam,
            year=year,
            subject=subject,
        )

        _print_stage("Validate")
        summary["stages"]["validate"] = validate_questions_file(
            normalized_path,
            validated_path,
            validation_report_path,
        )

        _print_stage("Link Answer Key")
        summary["stages"]["answer_key"] = link_answer_key(validated_path, verified_path)

        _print_stage("AI Placeholder")
        summary["stages"]["ai_enrichment"] = enrich_placeholders(verified_path, enriched_path)

        _print_stage("Repository Import")
        summary["stages"]["repository_import"] = import_to_repository(enriched_path)

        _write_json(pipeline_log_path, summary)
        summary["log_path"] = str(pipeline_log_path)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return summary
    except Exception as exc:
        summary["errors"].append(f"unexpected pipeline error: {exc}")
        _write_json(workspace / "pipeline_log.json", summary)
        print(json.dumps(summary, ensure_ascii=False, indent=2))
        return summary


def _print_stage(name: str) -> None:
    print(f"[TNPSC Import Pipeline] {name}...")


def _write_json(path: Path, payload: Dict[str, Any]) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w", encoding="utf-8") as file:
            json.dump(payload, file, ensure_ascii=False, indent=2)
            file.write("\n")
    except Exception:
        return


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run the TNPSC official PYQ import pipeline.")
    parser.add_argument("pdf", help="Official TNPSC PDF path.")
    parser.add_argument("--work-dir", default=None, help="Optional pipeline output directory.")
    parser.add_argument("--exam", default="Group 1", help="Exam label used for generated records.")
    parser.add_argument("--year", type=int, default=2011, help="Question paper year used for generated IDs.")
    parser.add_argument("--subject", default="General Knowledge", help="Subject label used for generated records.")
    return parser


def main(argv=None) -> int:
    try:
        args = _build_parser().parse_args(argv)
        run_pipeline(args.pdf, work_dir=args.work_dir, exam=args.exam, year=args.year, subject=args.subject)
        return 0
    except SystemExit as exc:
        return int(exc.code or 0)
    except Exception as exc:
        print(json.dumps({"errors": [f"unexpected CLI error: {exc}"]}, indent=2))
        return 0


if __name__ == "__main__":
    raise SystemExit(main())
