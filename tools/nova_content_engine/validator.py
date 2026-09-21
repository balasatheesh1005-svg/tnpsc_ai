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
    def validate_question(
        q: dict,
        expected_prefix: str = "",
        expected_difficulty: Optional[str] = None,
        expected_type: Optional[str] = None,
    ) -> List[ValidationIssue]:
        issues = []
        qid = q.get("id", "UNKNOWN")

        # 1. Check ID format and prefix
        if not q.get("id"):
            issues.append(ValidationIssue("CRITICAL", qid, "id", "Missing question ID"))
        elif expected_prefix:
            root_pfx = expected_prefix.rstrip("_")
            if not (str(q["id"]).startswith(expected_prefix) or str(q["id"]).startswith(root_pfx)):
                issues.append(ValidationIssue("MAJOR", qid, "id", f"ID does not start with expected prefix {expected_prefix}"))

        # 2. Check 24 required fields
        for f in REQUIRED_FIELDS:
            if f not in q or q[f] is None:
                issues.append(ValidationIssue("CRITICAL", qid, f, f"Missing required field '{f}'"))

        # 3. Bilingual content checks
        q_en = q.get("question_en") or q.get("question", "")
        q_ta = q.get("question_ta", "")
        if not q_en or len(str(q_en).strip()) < 5:
            issues.append(ValidationIssue("CRITICAL", qid, "question_en", "English question text is missing or too short"))
        if not q_ta or len(str(q_ta).strip()) < 5:
            issues.append(ValidationIssue("CRITICAL", qid, "question_ta", "Tamil question text is missing or too short"))

        # Tamil Unicode script check: question_ta must contain Tamil characters
        if q_ta and not re.search(r"[\u0B80-\u0BFF]", str(q_ta)):
            issues.append(ValidationIssue("CRITICAL", qid, "question_ta", "Tamil question text contains no Tamil Unicode characters"))

        # Accidental Tamil in English question text check
        if q_en and len(re.findall(r"[\u0B80-\u0BFF]", str(q_en))) > len(str(q_en)) * 0.3:
            issues.append(ValidationIssue("CRITICAL", qid, "question_en", "English question text contains excessive Tamil characters"))

        # Placeholder checks
        for text_val, name in [(q_en, "question_en"), (q_ta, "question_ta")]:
            if any(p in str(text_val).lower() for p in ["placeholder", "lorem ipsum", "todo", "tbd", "dummy text"]):
                issues.append(ValidationIssue("CRITICAL", qid, name, "Detected placeholder text"))

        # 4. Options check
        options = q.get("options", [])
        if not isinstance(options, list) or len(options) != 4:
            issues.append(ValidationIssue("CRITICAL", qid, "options", f"Expected exactly 4 options, got {len(options) if isinstance(options, list) else 'non-list'}"))
        else:
            opt_ids = [opt.get("id") for opt in options if isinstance(opt, dict)]
            if opt_ids != ["A", "B", "C", "D"]:
                issues.append(ValidationIssue("CRITICAL", qid, "options", f"Option IDs must be ['A', 'B', 'C', 'D'], got {opt_ids}"))

            en_texts = []
            ta_texts = []
            for opt in options:
                opt_id = opt.get("id", "")
                en_t = str(opt.get("en", "")).strip()
                ta_t = str(opt.get("ta", "")).strip()
                en_texts.append(en_t)
                ta_texts.append(ta_t)
                if not en_t:
                    issues.append(ValidationIssue("CRITICAL", qid, f"options[{opt_id}].en", "Empty English option text"))
                if not ta_t:
                    issues.append(ValidationIssue("CRITICAL", qid, f"options[{opt_id}].ta", "Empty Tamil option text"))

            # Duplicate options check
            if len(set(en_texts)) != 4 and all(en_texts):
                issues.append(ValidationIssue("CRITICAL", qid, "options", "Duplicate English option texts within question"))
            if len(set(ta_texts)) != 4 and all(ta_texts):
                issues.append(ValidationIssue("CRITICAL", qid, "options", "Duplicate Tamil option texts within question"))

            # Parity with options_en and options_ta
            opts_en_field = q.get("options_en")
            if isinstance(opts_en_field, list) and len(opts_en_field) == 4:
                if [str(x).strip() for x in opts_en_field] != en_texts:
                    issues.append(ValidationIssue("MAJOR", qid, "options_en", "options_en does not match options[].en"))

            opts_ta_field = q.get("options_ta")
            if isinstance(opts_ta_field, list) and len(opts_ta_field) == 4:
                if [str(x).strip() for x in opts_ta_field] != ta_texts:
                    issues.append(ValidationIssue("MAJOR", qid, "options_ta", "options_ta does not match options[].ta"))

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

        # 7. Source reference validation
        src = q.get("source_reference")
        if not isinstance(src, list) or len(src) == 0:
            issues.append(ValidationIssue("MINOR", qid, "source_reference", "Missing or empty source_reference list"))

        # 8. Difficulty check & consistency
        diff = q.get("difficulty")
        if diff not in ["Easy", "Medium", "Hard"]:
            issues.append(ValidationIssue("MAJOR", qid, "difficulty", f"Invalid difficulty: '{diff}'"))
        elif expected_difficulty and diff != expected_difficulty:
            issues.append(ValidationIssue("CRITICAL", qid, "difficulty", f"Difficulty mismatch: expected '{expected_difficulty}', got '{diff}'"))

        # 9. Question type consistency check
        qtype = str(q.get("question_type", "")).strip()
        if expected_type:
            if expected_type == "Statement" and "statement" not in qtype.lower():
                issues.append(ValidationIssue("MAJOR", qid, "question_type", f"Expected Statement-type, got '{qtype}'"))
            elif expected_type == "Assertion & Reason" and "reason" not in qtype.lower() and "assertion" not in qtype.lower():
                issues.append(ValidationIssue("MAJOR", qid, "question_type", f"Expected Assertion & Reason type, got '{qtype}'"))
            elif expected_type == "Chronology" and "chrono" not in qtype.lower():
                issues.append(ValidationIssue("MAJOR", qid, "question_type", f"Expected Chronology type, got '{qtype}'"))
            elif expected_type == "Match the Following" and "match" not in qtype.lower():
                issues.append(ValidationIssue("MAJOR", qid, "question_type", f"Expected Match the Following type, got '{qtype}'"))

        # Structural event validation for Chronology questions
        if expected_type == "Chronology" or "chrono" in qtype.lower():
            chrono_events = [l for l in str(q_en).split("\n") if re.match(r"^\s*[1-4]\.\s+", l.strip())]
            if len(chrono_events) != 4:
                issues.append(ValidationIssue("MAJOR", qid, "question_type", f"Chronology question stem must contain 4 numbered events, found {len(chrono_events)}"))

        return issues

    @classmethod
    def validate_file(
        cls,
        filepath: str,
        expected_count: Optional[int] = None,
        expected_prefix: str = "",
        expected_difficulty: Optional[str] = None,
        expected_type: Optional[str] = None,
    ) -> ValidationReport:
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
        fname = os.path.basename(filepath).lower()

        # Check for legacy files
        if fname in ["nature_and_structure_of_indian_economy_easy.json",
                     "nature_and_structure_of_indian_economy_medium.json",
                     "nature_and_structure_of_indian_economy_hard.json"]:
            all_issues.append(ValidationIssue("MAJOR", "FILE", "legacy", f"File '{fname}' is an existing Economy legacy file."))

        # Infer expected difficulty and type from filename if not explicitly provided
        exp_diff = expected_difficulty
        if not exp_diff:
            if "_easy." in fname:
                exp_diff = "Easy"
            elif "_medium." in fname:
                exp_diff = "Medium"
            elif "_hard." in fname:
                exp_diff = "Hard"

        exp_type = expected_type
        if not exp_type:
            if "_statement" in fname:
                exp_type = "Statement"
            elif "_reasoning" in fname or "_assertion" in fname:
                exp_type = "Assertion & Reason"
            elif "_match" in fname:
                exp_type = "Match the Following"
            elif "_chronology" in fname:
                exp_type = "Chronology"

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

            q_issues = cls.validate_question(
                q,
                expected_prefix=expected_prefix,
                expected_difficulty=exp_diff,
                expected_type=exp_type,
            )
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
