import json
import os
import re
from collections import Counter
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Set, Tuple


REQUIRED_FIELDS = [
    "id", "subject", "topic", "difficulty", "question_type",
    "question", "question_en", "question_ta",
    "options", "options_en", "options_ta",
    "correct_answer", "answer",
    "explanation", "explanation_en", "explanation_ta",
    "why_not_others", "tnpsc_tip", "revision_fact",
    "source_reference", "bloom_level", "estimated_time_sec",
    "pyq_similarity", "tags"
]


@dataclass
class ValidationIssue:
    severity: str  # "CRITICAL", "MAJOR", "MINOR"
    question_id: str
    field_name: str
    message: str


@dataclass
class ValidationReport:
    is_valid: bool
    total_audited: int
    issues: List[ValidationIssue] = field(default_factory=list)
    key_distribution: Dict[str, int] = field(default_factory=dict)
    difficulty_distribution: Dict[str, int] = field(default_factory=dict)
    metadata: Dict[str, Any] = field(default_factory=dict)

    def critical_issues(self) -> List[ValidationIssue]:
        return [i for i in self.issues if i.severity == "CRITICAL"]

    def major_issues(self) -> List[ValidationIssue]:
        return [i for i in self.issues if i.severity == "MAJOR"]

    def summary(self) -> str:
        res = f"Validation Report: {'PASS' if self.is_valid else 'FAIL'} | Total: {self.total_audited}\n"
        res += f"Key Distribution: {self.key_distribution}\n"
        res += f"Difficulty: {self.difficulty_distribution}\n"
        if self.issues:
            res += f"Total Issues: {len(self.issues)} (Critical: {len(self.critical_issues())}, Major: {len(self.major_issues())})\n"
            for iss in self.issues[:10]:
                res += f"  - [{iss.severity}] {iss.question_id}: {iss.message}\n"
        else:
            res += "No issues found."
        return res


class ContentValidator:
    """
    Deterministic validator enforcing TNPSC Nova AI standards.
    Can validate a single question, a list of questions, a specific file, or a complete topic suite.
    """

    @staticmethod
    def validate_question(q: dict, expected_prefix: str = "") -> List[ValidationIssue]:
        issues = []
        qid = q.get("id", "UNKNOWN")

        # 1. Check ID format and prefix
        if not q.get("id"):
            issues.append(ValidationIssue("CRITICAL", qid, "id", "Missing question ID"))
        elif expected_prefix and not str(q["id"]).startswith(expected_prefix):
            issues.append(ValidationIssue("MAJOR", qid, "id", f"ID does not start with expected prefix {expected_prefix}"))

        # 2. Check 24 required fields
        for f in REQUIRED_FIELDS:
            if f not in q:
                issues.append(ValidationIssue("CRITICAL", qid, f, f"Missing required field '{f}'"))

        # 3. Bilingual content checks
        q_en = q.get("question_en") or q.get("question", "")
        q_ta = q.get("question_ta", "")
        if not q_en or len(str(q_en).strip()) < 5:
            issues.append(ValidationIssue("CRITICAL", qid, "question_en", "English question text is missing or too short"))
        if not q_ta or len(str(q_ta).strip()) < 5:
            issues.append(ValidationIssue("CRITICAL", qid, "question_ta", "Tamil question text is missing or too short"))

        # Placeholder checks
        for text_val, name in [(q_en, "question_en"), (q_ta, "question_ta")]:
            if any(p in str(text_val).lower() for p in ["placeholder", "lorem ipsum", "todo", "tbd"]):
                issues.append(ValidationIssue("CRITICAL", qid, name, "Detected placeholder text"))

        # 4. Options check
        options = q.get("options", [])
        if not isinstance(options, list) or len(options) != 4:
            issues.append(ValidationIssue("CRITICAL", qid, "options", f"Expected exactly 4 options, got {len(options) if isinstance(options, list) else 'non-list'}"))
        else:
            opt_ids = [opt.get("id") for opt in options if isinstance(opt, dict)]
            if opt_ids != ["A", "B", "C", "D"]:
                issues.append(ValidationIssue("CRITICAL", qid, "options", f"Option IDs must be ['A', 'B', 'C', 'D'], got {opt_ids}"))
            for opt in options:
                opt_id = opt.get("id", "")
                if not opt.get("en") or len(str(opt["en"]).strip()) == 0:
                    issues.append(ValidationIssue("CRITICAL", qid, f"options[{opt_id}].en", "Empty English option text"))
                if not opt.get("ta") or len(str(opt["ta"]).strip()) == 0:
                    issues.append(ValidationIssue("CRITICAL", qid, f"options[{opt_id}].ta", "Empty Tamil option text"))

        # 5. Answer integrity
        correct = q.get("correct_answer")
        ans = q.get("answer")
        if correct not in ["A", "B", "C", "D"]:
            issues.append(ValidationIssue("CRITICAL", qid, "correct_answer", f"correct_answer must be A/B/C/D, got '{correct}'"))
        if ans != str(correct).lower():
            issues.append(ValidationIssue("CRITICAL", qid, "answer", f"answer '{ans}' != correct_answer.lower() '{str(correct).lower()}'"))

        # 6. Explanation and pedagogical fields
        exp = q.get("explanation", {})
        exp_en = exp.get("en") if isinstance(exp, dict) else q.get("explanation_en", "")
        exp_ta = exp.get("ta") if isinstance(exp, dict) else q.get("explanation_ta", "")
        if not exp_en or len(str(exp_en).strip()) < 5:
            issues.append(ValidationIssue("MAJOR", qid, "explanation.en", "English explanation missing or too short"))
        if not exp_ta or len(str(exp_ta).strip()) < 5:
            issues.append(ValidationIssue("MAJOR", qid, "explanation.ta", "Tamil explanation missing or too short"))

        wno = q.get("why_not_others", {})
        if not isinstance(wno, dict) or not all(k in wno for k in ["A", "B", "C", "D"]):
            issues.append(ValidationIssue("MAJOR", qid, "why_not_others", "why_not_others must contain keys A, B, C, D"))

        tip = q.get("tnpsc_tip", {})
        if not tip or (isinstance(tip, dict) and (not tip.get("en") or not tip.get("ta"))):
            issues.append(ValidationIssue("MINOR", qid, "tnpsc_tip", "Incomplete bilingual tnpsc_tip"))

        rf = q.get("revision_fact", {})
        if not rf or (isinstance(rf, dict) and (not rf.get("en") or not rf.get("ta"))):
            issues.append(ValidationIssue("MINOR", qid, "revision_fact", "Incomplete bilingual revision_fact"))

        # 7. Difficulty check
        diff = q.get("difficulty")
        if diff not in ["Easy", "Medium", "Hard"]:
            issues.append(ValidationIssue("MAJOR", qid, "difficulty", f"Invalid difficulty: '{diff}'"))

        return issues

    @classmethod
    def validate_file(cls, filepath: str, expected_count: Optional[int] = None, expected_prefix: str = "") -> ValidationReport:
        if not os.path.exists(filepath):
            return ValidationReport(
                is_valid=False,
                total_audited=0,
                issues=[ValidationIssue("CRITICAL", "FILE", "filepath", f"File does not exist: {filepath}")]
            )

        try:
            with open(filepath, "r", encoding="utf-8") as f:
                questions = json.load(f)
        except Exception as e:
            return ValidationReport(
                is_valid=False,
                total_audited=0,
                issues=[ValidationIssue("CRITICAL", "FILE", "json", f"JSON parsing failed: {e}")]
            )

        if not isinstance(questions, list):
            return ValidationReport(
                is_valid=False,
                total_audited=0,
                issues=[ValidationIssue("CRITICAL", "FILE", "root", "File root must be a JSON array")]
            )

        all_issues = []
        if expected_count is not None and len(questions) != expected_count:
            all_issues.append(ValidationIssue("CRITICAL", "COUNT", "length", f"Expected {expected_count} questions, got {len(questions)}"))

        seen_ids = set()
        seen_stems = set()
        key_counter = Counter()
        diff_counter = Counter()

        for idx, q in enumerate(questions, start=1):
            qid = q.get("id", f"INDEX_{idx}")
            if qid in seen_ids:
                all_issues.append(ValidationIssue("CRITICAL", qid, "id", f"Duplicate question ID: {qid}"))
            seen_ids.add(qid)

            stem_en = (q.get("question_en") or q.get("question", "")).strip().lower()
            if stem_en:
                if stem_en in seen_stems:
                    all_issues.append(ValidationIssue("CRITICAL", qid, "question_en", "Duplicate English stem within file"))
                seen_stems.add(stem_en)

            q_issues = cls.validate_question(q, expected_prefix=expected_prefix)
            all_issues.extend(q_issues)

            if q.get("correct_answer"):
                key_counter[q["correct_answer"]] += 1
            if q.get("difficulty"):
                diff_counter[q["difficulty"]] += 1

        is_valid = len([i for i in all_issues if i.severity in ["CRITICAL", "MAJOR"]]) == 0
        return ValidationReport(
            is_valid=is_valid,
            total_audited=len(questions),
            issues=all_issues,
            key_distribution=dict(key_counter),
            difficulty_distribution=dict(diff_counter)
        )

    @classmethod
    def validate_topic_suite(cls, files_map: Dict[str, Tuple[str, int, str]]) -> ValidationReport:
        """
        Validate all 9 files of a topic.
        files_map: category -> (filepath, expected_count, id_prefix)
        """
        all_issues = []
        total_questions = 0
        all_ids = set()
        all_stems_en = set()
        core_stems = set()
        gt_stems = set()
        overall_keys = Counter()
        overall_diffs = Counter()

        for cat, (filepath, expected_count, prefix) in files_map.items():
            rep = cls.validate_file(filepath, expected_count=expected_count, expected_prefix=prefix)
            all_issues.extend(rep.issues)
            total_questions += rep.total_audited

            if os.path.exists(filepath):
                try:
                    with open(filepath, "r", encoding="utf-8") as f:
                        qs = json.load(f)
                    for q in qs:
                        qid = q.get("id")
                        if qid in all_ids:
                            all_issues.append(ValidationIssue("CRITICAL", qid, "id", f"Cross-file duplicate ID {qid}"))
                        all_ids.add(qid)

                        s_en = (q.get("question_en") or q.get("question", "")).strip().lower()
                        if s_en in all_stems_en:
                            all_issues.append(ValidationIssue("CRITICAL", qid, "question_en", f"Cross-file duplicate stem in {cat}"))
                        all_stems_en.add(s_en)

                        if cat == "grand_test":
                            gt_stems.add(s_en)
                        else:
                            core_stems.add(s_en)

                        overall_keys[q.get("correct_answer")] += 1
                        overall_diffs[q.get("difficulty")] += 1
                except Exception:
                    pass

        # Check Grand Test independence
        gt_collisions = core_stems & gt_stems
        if gt_collisions:
            all_issues.append(ValidationIssue(
                "CRITICAL", "GRAND_TEST", "independence",
                f"Found {len(gt_collisions)} duplicate stems between Core and Grand Test"
            ))

        # Check Grand Test key balance if grand_test exists in files_map
        if "grand_test" in files_map:
            gt_path, _, _ = files_map["grand_test"]
            if os.path.exists(gt_path):
                with open(gt_path, "r", encoding="utf-8") as f:
                    gt_qs = json.load(f)
                gt_keys = Counter([q.get("correct_answer") for q in gt_qs])
                for opt in ["A", "B", "C", "D"]:
                    count = gt_keys.get(opt, 0)
                    if not (22 <= count <= 28):
                        all_issues.append(ValidationIssue(
                            "MAJOR", "GT_KEY_BALANCE", "correct_answer",
                            f"Grand Test option '{opt}' count is {count} (must be 22-28)"
                        ))

        is_valid = len([i for i in all_issues if i.severity in ["CRITICAL", "MAJOR"]]) == 0
        return ValidationReport(
            is_valid=is_valid,
            total_audited=total_questions,
            issues=all_issues,
            key_distribution=dict(overall_keys),
            difficulty_distribution=dict(overall_diffs)
        )
