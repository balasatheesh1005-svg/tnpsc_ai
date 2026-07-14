"""Standalone TNPSC Nova AI Import Pipeline V2 CLI."""
import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from tools.import_pipeline.question_validator import validate_questions_file
from tools.import_pipeline_v2 import pdf_reader, ocr_engine, question_splitter, option_parser
from tools.import_pipeline_v2 import subject_classifier, topic_classifier, difficulty_classifier
from tools.import_pipeline_v2 import duplicate_checker, answer_key_matcher, explanation_generator, notes_linker, repository_writer, report_generator


def run(pdf, exam="Group 1", year=None, work_dir=None, output=None):
    pdf = Path(pdf)
    year = int(year or _infer_year(pdf.name))
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    work = Path(work_dir or ROOT / "tools" / "import_pipeline_v2" / "runs" / stamp)
    source = pdf_reader.read_pdf(pdf)
    cleaned = ocr_engine.cleanup_pages(source["pages"], pdf)
    split = question_splitter.split_questions(cleaned["pages"])
    parsed = option_parser.parse_options(split["question_blocks"])
    normalized = [_normalize(row, exam, year, pdf) for row in parsed["questions"]]
    normalized_path = work / "normalized_questions.json"
    normalized_path.parent.mkdir(parents=True, exist_ok=True)
    normalized_path.write_text(json.dumps({"questions": normalized}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    validation = validate_questions_file(normalized_path, work / "validated_questions.json", work / "validation_report.json")
    validated = json.loads((work / "validated_questions.json").read_text(encoding="utf-8")).get("questions", [])
    duplicate = duplicate_checker.check(validated, ROOT / "data" / "pyq")
    classified = []
    for row in duplicate["unique_questions"]:
        row = dict(row); row["subject"] = subject_classifier.classify(row); row["topic"] = topic_classifier.classify(row); row["difficulty"] = difficulty_classifier.classify(row); classified.append(row)
    keyed = answer_key_matcher.match(classified, exam, year)
    enriched = notes_linker.link_notes(explanation_generator.add_placeholders(keyed["questions"]))
    target = Path(output or ROOT / "data" / "pyq" / "group1" / f"group1_{year}_import_pipeline_v2.json")
    repository = {"output_file": str(target), "written_count": 0, "status": "not_written"}
    status = "blocked"
    if keyed["answer_key_found"] and not keyed["missing_ids"] and enriched["questions"] and not source["errors"]:
        repository = repository_writer.write(enriched["questions"], target); repository["status"] = "written"; status = "production_ready"
    summary = {"input_pdf": str(pdf), "status": status, "questions": enriched["questions"], "extracted_blocks": len(split["question_blocks"]), "parsed_questions": len(parsed["questions"]), "validation": validation, "duplicate": {"duplicate_count": len(duplicate["duplicates"]), "duplicates": duplicate["duplicates"]}, "answer_key": {"answer_key_found": keyed["answer_key_found"], "matched_count": keyed["matched_count"], "missing_ids": keyed["missing_ids"]}, "repository": repository, "warnings": source["warnings"] + cleaned["warnings"] + split["warnings"], "rejected": parsed["rejected"]}
    summary["reports"] = report_generator.generate(work, summary)
    (work / "pipeline_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return summary


def _normalize(raw, exam, year, pdf):
    number = int(raw["question_number"])
    return {"id": f"PYQ_G1_{year}_{number:03d}", "exam": exam, "year": year, "subject": "General Knowledge", "topic": "", "subtopic": "", "difficulty": "", "question_en": raw["question_text"], "question_ta": "", "options": raw["options"], "correct_answer": "", "explanation": {"en": "", "ta": ""}, "related_note": "", "tags": [], "repeat_years": [], "ai_trick": "", "source": str(pdf), "source_page": raw.get("page_number"), "question_number": number}


def _infer_year(name):
    match = re.search(r"(?:19|20)\d{2}", name)
    if not match: raise ValueError("Year could not be inferred from filename; pass --year YYYY.")
    return match.group(0)


def main():
    parser = argparse.ArgumentParser(description="TNPSC Nova AI Import Pipeline V2")
    parser.add_argument("pdf"); parser.add_argument("--exam", default="Group 1"); parser.add_argument("--year", type=int); parser.add_argument("--work-dir"); parser.add_argument("--output")
    args = parser.parse_args()
    try: print(json.dumps(run(args.pdf, args.exam, args.year, args.work_dir, args.output), ensure_ascii=False, indent=2))
    except Exception as exc: print(json.dumps({"status": "failed", "error": str(exc)}, indent=2)); return 1
    return 0


if __name__ == "__main__": raise SystemExit(main())
