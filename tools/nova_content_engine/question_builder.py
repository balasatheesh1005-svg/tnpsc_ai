# -*- coding: utf-8 -*-
"""
Canonical 24-Field MCQ Builder and Atomic File Writer for TNPSC Nova AI.
Enforces the frozen 24-field schema, deterministic IDs, bilingual parity,
pedagogical structure, and strict legacy file protection.
"""

import json
import os
import re
from typing import Any, Dict, List, Optional, Set, Tuple, Union

from .economy_mcq_config import CATEGORY_CODE_MAP, ECONOMY_LEGACY_FILES

# Canonical 24 Fields
REQUIRED_24_FIELDS: List[str] = [
    "id",
    "subject",
    "topic",
    "difficulty",
    "question_type",
    "question",
    "question_en",
    "question_ta",
    "options",
    "options_en",
    "options_ta",
    "correct_answer",
    "answer",
    "explanation",
    "explanation_en",
    "explanation_ta",
    "why_not_others",
    "tnpsc_tip",
    "revision_fact",
    "source_reference",
    "bloom_level",
    "estimated_time_sec",
    "pyq_similarity",
    "tags",
]

VALID_DIFFICULTIES: Set[str] = {"Easy", "Medium", "Hard"}

VALID_BLOOM_LEVELS: Set[str] = {
    "Remember",
    "Understand",
    "Apply",
    "Analyze",
    "Evaluate",
    "Create",
}

PLACEHOLDER_SUBSTRINGS: List[str] = [
    "placeholder",
    "lorem ipsum",
    "todo",
    "tbd",
    "sample text",
    "temp text",
    "dummy text",
]


class LegacyCollisionError(RuntimeError):
    """Raised when an operation attempts to overwrite or modify protected legacy question files."""
    pass


class QuestionValidationError(ValueError):
    """Raised when question data fails canonical 24-field validation."""
    pass


def build_deterministic_question_id(prefix: str, category: str, seq: int) -> str:
    """
    Builds deterministic, collision-free question IDs.
    Format: <PREFIX>_<CATEGORY_CODE>_<SEQ_3_DIGITS>
    Example: NI_E_001, NI_SB_001, NI_AR_001, NI_CHRONO_001, NI_GT_001.
    """
    clean_pfx = prefix.strip().upper()
    cat_clean = category.strip().lower()
    code = CATEGORY_CODE_MAP.get(cat_clean, cat_clean.upper())
    return f"{clean_pfx}_{code}_{seq:03d}"


def is_legacy_question_file(filepath: str) -> bool:
    """
    Detects whether a file is an Economy legacy question file that must not be overwritten.
    Checks filename match and inspects content structure (e.g. 30 questions, missing 'id').
    """
    fname = os.path.basename(filepath)
    if fname in ECONOMY_LEGACY_FILES:
        return True

    if os.path.exists(filepath):
        try:
            with open(filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
            if isinstance(data, list) and len(data) > 0:
                # Legacy economy files have 30 questions and lack 'id'
                first = data[0]
                if isinstance(first, dict) and "id" not in first:
                    return True
        except Exception:
            pass
    return False


class MCQQuestionBuilder:
    """
    Deterministic Builder for canonical 24-field TNPSC MCQs.
    Enforces bilingual completeness, pedagogical rationale, and strict validation.
    """

    @staticmethod
    def build_question(
        qid: str,
        subject: str,
        topic: str,
        difficulty: str,
        question_type: str,
        question_en: str,
        question_ta: str,
        options_en: List[str],
        options_ta: List[str],
        correct_answer: str,
        explanation_en: str,
        explanation_ta: str,
        why_not_others: Dict[str, Dict[str, str]],
        tnpsc_tip: Dict[str, str],
        revision_fact: Dict[str, str],
        source_reference: List[str],
        bloom_level: str = "Understand",
        estimated_time_sec: int = 60,
        pyq_similarity: str = "Standard",
        tags: Optional[List[str]] = None,
    ) -> Dict[str, Any]:
        """
        Builds and strictly validates a canonical 24-field MCQ object.
        Rejects placeholder text, incomplete bilingual content, and mismatched options.
        """
        # 1. Basic string hygiene and validation
        if not qid or not str(qid).strip():
            raise QuestionValidationError("Question ID cannot be empty.")
        clean_qid = str(qid).strip()

        if not subject or not str(subject).strip():
            raise QuestionValidationError(f"{clean_qid}: Subject cannot be empty.")
        clean_subj = str(subject).strip()

        if not topic or not str(topic).strip():
            raise QuestionValidationError(f"{clean_qid}: Topic cannot be empty.")
        clean_topic = str(topic).strip()

        # Difficulty check
        norm_diff = str(difficulty).strip().capitalize()
        if norm_diff not in VALID_DIFFICULTIES:
            raise QuestionValidationError(
                f"{clean_qid}: Invalid difficulty '{difficulty}'. Must be one of {VALID_DIFFICULTIES}"
            )

        # Question Type check
        if not question_type or not str(question_type).strip():
            raise QuestionValidationError(f"{clean_qid}: question_type cannot be empty.")
        clean_qtype = str(question_type).strip()

        # Bloom level check
        norm_bloom = str(bloom_level).strip().capitalize()
        if norm_bloom not in VALID_BLOOM_LEVELS:
            norm_bloom = "Understand"

        # 2. Bilingual question text check
        clean_q_en = str(question_en).strip()
        clean_q_ta = str(question_ta).strip()
        if len(clean_q_en) < 5:
            raise QuestionValidationError(f"{clean_qid}: question_en too short ({len(clean_q_en)} chars).")
        if len(clean_q_ta) < 5:
            raise QuestionValidationError(f"{clean_qid}: question_ta too short ({len(clean_q_ta)} chars).")

        # Placeholder checks
        for txt, field_name in [(clean_q_en, "question_en"), (clean_q_ta, "question_ta")]:
            txt_lower = txt.lower()
            for ph in PLACEHOLDER_SUBSTRINGS:
                if ph in txt_lower:
                    raise QuestionValidationError(f"{clean_qid}: Placeholder '{ph}' detected in {field_name}.")

        # Script checks: Tamil must have Tamil characters
        if not re.search(r"[\u0B80-\u0BFF]", clean_q_ta):
            raise QuestionValidationError(
                f"{clean_qid}: question_ta contains no Tamil Unicode characters."
            )

        # 3. Options validation (exactly 4 options A, B, C, D)
        if not isinstance(options_en, list) or len(options_en) != 4:
            raise QuestionValidationError(
                f"{clean_qid}: options_en must have exactly 4 items, got {len(options_en) if isinstance(options_en, list) else 'non-list'}"
            )
        if not isinstance(options_ta, list) or len(options_ta) != 4:
            raise QuestionValidationError(
                f"{clean_qid}: options_ta must have exactly 4 items, got {len(options_ta) if isinstance(options_ta, list) else 'non-list'}"
            )

        clean_opt_en = [str(o).strip() for o in options_en]
        clean_opt_ta = [str(o).strip() for o in options_ta]

        for idx, (oe, ot) in enumerate(zip(clean_opt_en, clean_opt_ta)):
            opt_letter = ["A", "B", "C", "D"][idx]
            if not oe:
                raise QuestionValidationError(f"{clean_qid}: Option {opt_letter} English text is empty.")
            if not ot:
                raise QuestionValidationError(f"{clean_qid}: Option {opt_letter} Tamil text is empty.")
            for ph in PLACEHOLDER_SUBSTRINGS:
                if ph in oe.lower() or ph in ot.lower():
                    raise QuestionValidationError(f"{clean_qid}: Placeholder detected in Option {opt_letter}.")

        # Check for duplicate options within question
        if len(set(clean_opt_en)) != 4:
            raise QuestionValidationError(f"{clean_qid}: Duplicate option text in options_en.")
        if len(set(clean_opt_ta)) != 4:
            raise QuestionValidationError(f"{clean_qid}: Duplicate option text in options_ta.")

        # Build options structure
        options_struct = [
            {"id": "A", "en": clean_opt_en[0], "ta": clean_opt_ta[0]},
            {"id": "B", "en": clean_opt_en[1], "ta": clean_opt_ta[1]},
            {"id": "C", "en": clean_opt_en[2], "ta": clean_opt_ta[2]},
            {"id": "D", "en": clean_opt_en[3], "ta": clean_opt_ta[3]},
        ]

        # 4. Correct answer validation
        ca = str(correct_answer).strip().upper()
        if ca not in ["A", "B", "C", "D"]:
            raise QuestionValidationError(f"{clean_qid}: correct_answer must be A/B/C/D, got '{correct_answer}'.")
        ans = ca.lower()

        # 5. Explanations validation
        clean_exp_en = str(explanation_en).strip()
        clean_exp_ta = str(explanation_ta).strip()
        if len(clean_exp_en) < 5:
            raise QuestionValidationError(f"{clean_qid}: explanation_en too short.")
        if len(clean_exp_ta) < 5:
            raise QuestionValidationError(f"{clean_qid}: explanation_ta too short.")

        # 6. why_not_others validation
        if not isinstance(why_not_others, dict) or set(why_not_others.keys()) != {"A", "B", "C", "D"}:
            raise QuestionValidationError(f"{clean_qid}: why_not_others must contain keys A, B, C, D.")

        clean_wno: Dict[str, Dict[str, str]] = {}
        for k in ["A", "B", "C", "D"]:
            v = why_not_others[k]
            if not isinstance(v, dict) or "en" not in v or "ta" not in v:
                raise QuestionValidationError(f"{clean_qid}: why_not_others[{k}] must be a dict with 'en' and 'ta'.")
            clean_wno[k] = {
                "en": str(v["en"]).strip(),
                "ta": str(v["ta"]).strip(),
            }
            if not clean_wno[k]["en"] or not clean_wno[k]["ta"]:
                raise QuestionValidationError(f"{clean_qid}: why_not_others[{k}] has empty en or ta text.")

        # 7. Pedagogical fields validation
        if not isinstance(tnpsc_tip, dict) or "en" not in tnpsc_tip or "ta" not in tnpsc_tip:
            raise QuestionValidationError(f"{clean_qid}: tnpsc_tip must be a dict with 'en' and 'ta'.")
        clean_tip = {"en": str(tnpsc_tip["en"]).strip(), "ta": str(tnpsc_tip["ta"]).strip()}
        if not clean_tip["en"] or not clean_tip["ta"]:
            raise QuestionValidationError(f"{clean_qid}: Incomplete bilingual tnpsc_tip.")

        if not isinstance(revision_fact, dict) or "en" not in revision_fact or "ta" not in revision_fact:
            raise QuestionValidationError(f"{clean_qid}: revision_fact must be a dict with 'en' and 'ta'.")
        clean_rf = {"en": str(revision_fact["en"]).strip(), "ta": str(revision_fact["ta"]).strip()}
        if not clean_rf["en"] or not clean_rf["ta"]:
            raise QuestionValidationError(f"{clean_qid}: Incomplete bilingual revision_fact.")

        # 8. Source references validation
        if not isinstance(source_reference, list) or len(source_reference) == 0:
            raise QuestionValidationError(f"{clean_qid}: source_reference must be a non-empty list of sources.")
        clean_sources = [str(s).strip() for s in source_reference if str(s).strip()]
        if not clean_sources:
            raise QuestionValidationError(f"{clean_qid}: source_reference contains only empty entries.")

        # 9. Time and Tags
        time_sec = int(estimated_time_sec) if estimated_time_sec else 60
        if time_sec <= 0:
            time_sec = 60

        clean_tags = [str(t).strip() for t in (tags or []) if str(t).strip()]
        if not clean_tags:
            clean_tags = [clean_subj, clean_topic]

        # 10. Assemble canonical 24-field dictionary
        question_obj: Dict[str, Any] = {
            "id": clean_qid,
            "subject": clean_subj,
            "topic": clean_topic,
            "difficulty": norm_diff,
            "question_type": clean_qtype,
            "question": {
                "en": clean_q_en,
                "ta": clean_q_ta,
            },
            "question_en": clean_q_en,
            "question_ta": clean_q_ta,
            "options": options_struct,
            "options_en": clean_opt_en,
            "options_ta": clean_opt_ta,
            "correct_answer": ca,
            "answer": ans,
            "explanation": {
                "en": clean_exp_en,
                "ta": clean_exp_ta,
            },
            "explanation_en": clean_exp_en,
            "explanation_ta": clean_exp_ta,
            "why_not_others": clean_wno,
            "tnpsc_tip": clean_tip,
            "revision_fact": clean_rf,
            "source_reference": clean_sources,
            "bloom_level": norm_bloom,
            "estimated_time_sec": time_sec,
            "pyq_similarity": str(pyq_similarity).strip() if pyq_similarity else "Standard",
            "tags": clean_tags,
        }

        # Verify all 24 fields present and non-empty
        for f in REQUIRED_24_FIELDS:
            if f not in question_obj or question_obj[f] is None:
                raise QuestionValidationError(f"{clean_qid}: Missing canonical field '{f}'.")

        return question_obj


def write_question_file_atomically(
    filepath: str,
    questions: List[Dict[str, Any]],
    allow_legacy_overwrite: bool = False,
) -> None:
    """
    Safely and atomically writes a list of validated questions to disk.
    - Prevents overwriting protected legacy question files.
    - Validates 24-field schema before writing.
    - Writes to .tmp file first, loads to verify integrity, then atomic os.replace.
    """
    norm_path = os.path.normpath(filepath).replace("\\", "/")

    # Check legacy collision guard
    if not allow_legacy_overwrite and is_legacy_question_file(norm_path):
        raise LegacyCollisionError(
            f"LEGACY PROTECTION VIOLATION: Refusing to overwrite protected legacy question file '{norm_path}'. "
            "Legacy files must be preserved untouched."
        )

    if not isinstance(questions, list):
        raise ValueError(f"Questions to write must be a list, got {type(questions).__name__}")

    # Validate all questions contain 24 required fields
    for idx, q in enumerate(questions):
        qid = q.get("id", f"idx_{idx}")
        for rf in REQUIRED_24_FIELDS:
            if rf not in q:
                raise QuestionValidationError(f"Question {qid} missing required field '{rf}'")

    # Atomic write pattern
    os.makedirs(os.path.dirname(os.path.abspath(filepath)), exist_ok=True)
    tmp_path = f"{filepath}.tmp"

    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)

    # Verification read back
    with open(tmp_path, "r", encoding="utf-8") as f:
        verified_data = json.load(f)

    if len(verified_data) != len(questions):
        if os.path.exists(tmp_path):
            os.remove(tmp_path)
        raise IOError(f"Verification read back failed: expected {len(questions)} items, read {len(verified_data)}")

    # Atomic replacement
    os.replace(tmp_path, filepath)
