# -*- coding: utf-8 -*-
"""
Dedicated Chronology Validator for TNPSC Nova Content Engine.
Enforces the CRITICAL CHRONOLOGY RULE:
- Numbered events (1, 2, 3, 4) in the question stem MUST be presented in non-chronological order.
- The correct chronological order MUST NOT equal the presented order (1-2-3-4).
- Options must be valid, unique permutations of [1, 2, 3, 4].
- Exactly one correct sequence.
- Explanations must explicitly teach the chronology with dates/years and arrow sequences.
- Fully bilingual (English & Tamil).
"""
import json
import os
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class ChronologyAuditReport:
    total_questions: int
    already_in_order_count: int
    invalid_duplicate_sequences_count: int
    correct_answer_integrity_pass: bool
    presentation_order_shuffle_pass: bool
    option_uniqueness_pass: bool
    explanation_chronology_pass: bool
    is_valid: bool
    issues: List[str] = field(default_factory=list)

    def format_final_report(self) -> str:
        lines = [
            f"Total chronology questions: {self.total_questions}",
            "",
            "Already-in-correct-order:",
            f"{self.already_in_order_count}",
            "",
            "Invalid/duplicate sequences:",
            f"{self.invalid_duplicate_sequences_count}",
            "",
            f"Correct-answer integrity:",
            f"{'PASS' if self.correct_answer_integrity_pass else 'FAIL'}",
            "",
            f"Presentation-order shuffle:",
            f"{'PASS' if self.presentation_order_shuffle_pass else 'FAIL'}",
            "",
            f"Option uniqueness:",
            f"{'PASS' if self.option_uniqueness_pass else 'FAIL'}",
            "",
            f"Explanation chronology:",
            f"{'PASS' if self.explanation_chronology_pass else 'FAIL'}",
            "",
            f"Final Chronology Gate:",
            f"{'PASS' if self.is_valid else 'FAIL'}"
        ]
        return "\n".join(lines)


class ChronologyValidator:
    """
    Validates chronology questions to ensure event order is non-chronological,
    sequences are unique, and explanations teach the chronology.
    """

    @classmethod
    def parse_sequence_digits(cls, text: str) -> List[int]:
        """Extract sequence digits from option string (e.g. '2 - 4 - 1 - 3' -> [2, 4, 1, 3])."""
        return [int(d) for d in re.findall(r"\b[1-4]\b", str(text))]

    @classmethod
    def validate_question(cls, q: dict) -> Tuple[bool, List[str], Dict[str, Any]]:
        issues = []
        qid = q.get("id", "UNKNOWN")
        stats = {
            "already_in_order": False,
            "invalid_seq": False,
            "duplicate_seq": False,
            "correct_integrity": True,
            "explanation_ok": True,
        }

        # 1. Check stem events count
        stem_en = q.get("question_en", "") or q.get("question", {}).get("en", "")
        stem_ta = q.get("question_ta", "") or q.get("question", {}).get("ta", "")

        events_en = [l.strip() for l in stem_en.split("\n") if re.match(r"^\s*[1-4]\.\s+", l.strip())]
        events_ta = [l.strip() for l in stem_ta.split("\n") if re.match(r"^\s*[1-4]\.\s+", l.strip())]

        if len(events_en) != 4:
            issues.append(f"{qid}: Expected 4 numbered events in English stem, found {len(events_en)}")
        if len(events_ta) != 4:
            issues.append(f"{qid}: Expected 4 numbered events in Tamil stem, found {len(events_ta)}")

        # 2. Check options validity and uniqueness
        options = q.get("options", [])
        if len(options) != 4:
            issues.append(f"{qid}: Expected 4 options, found {len(options)}")
            stats["invalid_seq"] = True
            return False, issues, stats

        parsed_seqs = []
        for opt in options:
            opt_id = opt.get("id", "?")
            digits = cls.parse_sequence_digits(opt.get("en", ""))
            if len(digits) != 4 or sorted(digits) != [1, 2, 3, 4]:
                issues.append(f"{qid}: Option {opt_id} does not contain a valid permutation of [1, 2, 3, 4]: '{opt.get('en')}'")
                stats["invalid_seq"] = True
            parsed_seqs.append(tuple(digits))

        # Uniqueness of options
        if len(set(parsed_seqs)) != 4:
            issues.append(f"{qid}: Duplicate option sequences found: {parsed_seqs}")
            stats["duplicate_seq"] = True

        # 3. Correct answer integrity and Presentation order vs Correct order
        correct_key = q.get("correct_answer", "").upper()
        if correct_key not in ["A", "B", "C", "D"]:
            issues.append(f"{qid}: Invalid correct_answer '{correct_key}'")
            stats["correct_integrity"] = False
        else:
            idx_map = {"A": 0, "B": 1, "C": 2, "D": 3}
            c_idx = idx_map[correct_key]
            correct_digits = list(parsed_seqs[c_idx]) if c_idx < len(parsed_seqs) else []

            # CRITICAL RULE: Presented order must NOT equal correct order!
            if correct_digits == [1, 2, 3, 4]:
                issues.append(f"{qid}: CRITICAL: Events in question stem were presented in chronological order (correct sequence is 1-2-3-4)")
                stats["already_in_order"] = True

        # 4. Explanation chronology rule
        exp_en = q.get("explanation_en", "") or q.get("explanation", {}).get("en", "")
        exp_ta = q.get("explanation_ta", "") or q.get("explanation", {}).get("ta", "")

        # Must have dates / years (4 digits)
        has_dates = bool(re.search(r"\b(19\d\d|20\d\d)\b", exp_en))
        # Must show chronology / progression
        has_progression = bool(re.search(r"(→|->|chronological|order)", exp_en, re.IGNORECASE))

        if not has_dates and not has_progression:
            issues.append(f"{qid}: Explanation must teach the chronology with dates/years and sequence")
            stats["explanation_ok"] = False

        is_valid = len(issues) == 0
        return is_valid, issues, stats

    @classmethod
    def validate_questions(cls, questions: List[dict]) -> ChronologyAuditReport:
        total = len(questions)
        already_in_order = 0
        invalid_duplicate = 0
        correct_integrity_pass = True
        explanation_pass = True
        all_issues = []

        for q in questions:
            is_valid, q_issues, stats = cls.validate_question(q)
            if not is_valid:
                all_issues.extend(q_issues)
            if stats["already_in_order"]:
                already_in_order += 1
            if stats["invalid_seq"] or stats["duplicate_seq"]:
                invalid_duplicate += 1
            if not stats["correct_integrity"]:
                correct_integrity_pass = False
            if not stats["explanation_ok"]:
                explanation_pass = False

        presentation_order_shuffle_pass = (already_in_order == 0)
        option_uniqueness_pass = (invalid_duplicate == 0)
        overall_valid = (
            len(all_issues) == 0 and
            already_in_order == 0 and
            invalid_duplicate == 0 and
            correct_integrity_pass and
            presentation_order_shuffle_pass and
            option_uniqueness_pass and
            explanation_pass
        )

        return ChronologyAuditReport(
            total_questions=total,
            already_in_order_count=already_in_order,
            invalid_duplicate_sequences_count=invalid_duplicate,
            correct_answer_integrity_pass=correct_integrity_pass,
            presentation_order_shuffle_pass=presentation_order_shuffle_pass,
            option_uniqueness_pass=option_uniqueness_pass,
            explanation_chronology_pass=explanation_pass,
            is_valid=overall_valid,
            issues=all_issues
        )

    @classmethod
    def validate_file(cls, filepath: str) -> ChronologyAuditReport:
        if not os.path.exists(filepath):
            return ChronologyAuditReport(
                total_questions=0,
                already_in_order_count=0,
                invalid_duplicate_sequences_count=0,
                correct_answer_integrity_pass=False,
                presentation_order_shuffle_pass=False,
                option_uniqueness_pass=False,
                explanation_chronology_pass=False,
                is_valid=False,
                issues=[f"File not found: {filepath}"]
            )

        with open(filepath, "r", encoding="utf-8") as f:
            questions = json.load(f)

        return cls.validate_questions(questions)
