"""TNPSC Group 4 Free Mini Mock - Curated Gold 25 Questions Manifest.

IMPORTANT ARCHITECTURAL RULE:
This manifest contains ONLY deterministic composite references (source_file + question_id)
pointing to existing validated production questions under data/questions/.
NO question content, options, answers, or explanations are duplicated in this file.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from ui.question_engine.parser import NormalizedQuestion, UniversalQuestionAdapter


class CampaignManifestError(Exception):
    """Raised when the campaign manifest resolution or validation fails."""
    pass


# Deterministic 25 Gold references from the Phase 2 selection audit
GROUP4_GOLD_25: Tuple[Dict[str, str], ...] = (
    # General Tamil (12 questions)
    {
        "source_file": "data/questions/general_tamil/gt_u1_piritthu_serththu_ezhuthuthal_gold.json",
        "question_id": "GT_U1_PIRITTHU_001",
    },
    {
        "source_file": "data/questions/general_tamil/gt_u1_verchol_arithal_gold.json",
        "question_id": "GT_U1_VERCHOL_001",
    },
    {
        "source_file": "data/questions/general_tamil/gt_u2_orezhuthu_orumozhi_gold.json",
        "question_id": "GT_U2_OREZHUTHU_001",
    },
    {
        "source_file": "data/questions/general_tamil/gt_u1_santhi_pizhai_vallinam_gold.json",
        "question_id": "GT_U1_SANDHI_003",
    },
    {
        "source_file": "data/questions/general_tamil/gt_u1_ayarsol_tamilsol_ethirsol_gold.json",
        "question_id": "GT_U1_AYARSOL_001",
    },
    {
        "source_file": "data/questions/general_tamil/gt_u2_sollum_porulum_gold.json",
        "question_id": "GT_U2_SOLLUM_004",
    },
    {
        "source_file": "data/questions/general_tamil/gt_u2_marabuthtodar_uvamaithtodar_gold.json",
        "question_id": "GT_U2_UVAMAI_003",
    },
    {
        "source_file": "data/questions/general_tamil/gt_u3_todar_vagai_vinai_kootru_gold.json",
        "question_id": "GT_U3_TODAR_001",
    },
    {
        "source_file": "data/questions/general_tamil/gt_u1_piritthu_serththu_ezhuthuthal_gold.json",
        "question_id": "GT_U1_PIRITTHU_002",
    },
    {
        "source_file": "data/questions/general_tamil/gt_u2_orezhuthu_orumozhi_gold.json",
        "question_id": "GT_U2_OREZHUTHU_007",
    },
    {
        "source_file": "data/questions/general_tamil/gt_u1_ayarsol_tamilsol_ethirsol_gold.json",
        "question_id": "GT_U1_AYARSOL_003",
    },
    {
        "source_file": "data/questions/general_tamil/gt_u1_ezhuthu_pizhai_ottru_pizhai_gold.json",
        "question_id": "GT_U1_PIZHAI_001",
    },
    # General Studies - Polity (3 questions)
    {
        "source_file": "data/questions/polity/fundamental_rights_easy.json",
        "question_id": "FR_E_002",
    },
    {
        "source_file": "data/questions/polity/panchayati_raj_easy.json",
        "question_id": "PR_E_001",
    },
    {
        "source_file": "data/questions/polity/panchayati_raj_easy.json",
        "question_id": "PR_E_003",
    },
    # General Studies - INM (4 questions)
    {
        "source_file": "data/questions/inm/freedom_struggle_in_tamil_nadu_easy.json",
        "question_id": "INM_T13_E003",
    },
    {
        "source_file": "data/questions/inm/early_resistance_to_british_rule_easy.json",
        "question_id": "INM_T2_E002",
    },
    {
        "source_file": "data/questions/inm/indian_national_congress_easy.json",
        "question_id": "INM_T6_E001",
    },
    {
        "source_file": "data/questions/inm/early_resistance_to_british_rule_easy.json",
        "question_id": "INM_T2_E004",
    },
    # General Studies - Economy (2 questions)
    {
        "source_file": "data/questions/economy/five_year_plans_easy.json",
        "question_id": "FYP_E_001",
    },
    {
        "source_file": "data/questions/economy/niti_aayog_easy.json",
        "question_id": "NA_E_001",
    },
    # Aptitude & Mental Ability (4 questions)
    {
        "source_file": "data/questions/aptitude/aptitude_simplification_gold.json",
        "question_id": "SIMP_001",
    },
    {
        "source_file": "data/questions/aptitude/aptitude_percentage_gold.json",
        "question_id": "PERC_001",
    },
    {
        "source_file": "data/questions/aptitude/aptitude_ratio_proportion_gold.json",
        "question_id": "RATIO_002",
    },
    {
        "source_file": "data/questions/aptitude/aptitude_hcf_lcm_gold.json",
        "question_id": "HCF_002",
    },
)

# Truthful 3-Bucket Category Identifiers
BUCKET_GENERAL_TAMIL = "General Tamil"
BUCKET_GENERAL_STUDIES = "General Studies"
BUCKET_APTITUDE = "Aptitude & Mental Ability"

ANALYSIS_BUCKETS = (
    BUCKET_GENERAL_TAMIL,
    BUCKET_GENERAL_STUDIES,
    BUCKET_APTITUDE,
)


def get_bucket_for_source(source_file: str) -> str:
    """Deterministically map question source file path to one of the 3 analysis buckets."""
    norm_path = source_file.replace("\\", "/").lower()
    if "general_tamil" in norm_path:
        return BUCKET_GENERAL_TAMIL
    if "aptitude" in norm_path:
        return BUCKET_APTITUDE
    return BUCKET_GENERAL_STUDIES


def load_group4_campaign_questions(
    base_dir: Optional[Path] = None,
) -> List[NormalizedQuestion]:
    """Deterministically load and validate the exact 25 Gold questions from manifest.

    FAIL CLOSED:
    If any question cannot be resolved, verified, or normalized, raises CampaignManifestError.
    Never silently substitutes or falls back to any other question.
    """
    if base_dir is None:
        base_dir = Path(__file__).resolve().parent.parent.parent

    data_root = (base_dir / "data" / "questions").resolve()
    if not data_root.is_dir():
        raise CampaignManifestError(f"Question repository root not found: {data_root}")

    # Track seen composite identities to prevent any duplicate references
    seen_refs: set[Tuple[str, str]] = set()
    loaded_questions: List[NormalizedQuestion] = []
    file_cache: Dict[str, Any] = {}

    for idx, ref in enumerate(GROUP4_GOLD_25):
        source_rel = ref.get("source_file", "")
        q_id = ref.get("question_id", "")

        if not source_rel or not q_id:
            raise CampaignManifestError(f"Malformed manifest entry at index {idx}: {ref}")

        composite_key = (source_rel, q_id)
        if composite_key in seen_refs:
            raise CampaignManifestError(f"Duplicate composite reference in manifest: {composite_key}")
        seen_refs.add(composite_key)

        file_path = (base_dir / source_rel).resolve()

        # Strict security constraint: path must remain under data/questions/
        try:
            file_path.relative_to(data_root)
        except ValueError:
            raise CampaignManifestError(
                f"Path traversal detected or file outside questions root: {source_rel}"
            )

        if not file_path.is_file():
            raise CampaignManifestError(f"Manifest source file does not exist: {source_rel}")

        # Load JSON (cached across manifest references to the same file)
        if str(file_path) not in file_cache:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    file_cache[str(file_path)] = json.load(f)
            except Exception as e:
                raise CampaignManifestError(f"Failed to read JSON from {source_rel}: {e}")

        data = file_cache[str(file_path)]
        raw_items = data if isinstance(data, list) else data.get("questions", [])

        # Match exactly on question ID
        matches = [
            q for q in raw_items
            if str(q.get("id") or q.get("question_id")) == q_id
        ]
        if len(matches) != 1:
            raise CampaignManifestError(
                f"Expected exactly 1 match for {q_id} in {source_rel}, found {len(matches)}"
            )

        raw_q = matches[0]

        # Normalize via UniversalQuestionAdapter
        try:
            norm_q = UniversalQuestionAdapter.normalize(raw_q)
        except Exception as e:
            raise CampaignManifestError(f"Normalization failed for {q_id} in {source_rel}: {e}")

        # Strict validation
        if len(norm_q.options) != 4:
            raise CampaignManifestError(
                f"Question {q_id} has {len(norm_q.options)} options, expected exactly 4"
            )

        if norm_q.correct_answer not in ("A", "B", "C", "D"):
            raise CampaignManifestError(
                f"Question {q_id} has invalid correct_answer: {norm_q.correct_answer}"
            )

        has_explanation = bool(
            norm_q.explanation
            and (norm_q.explanation.en or norm_q.explanation.ta)
        )
        if not has_explanation:
            raise CampaignManifestError(f"Question {q_id} is missing explanation")

        # Assign bucket attribute for truthful 3-bucket analysis
        norm_q.campaign_bucket = get_bucket_for_source(source_rel)  # type: ignore[attr-defined]
        norm_q.campaign_source_file = source_rel  # type: ignore[attr-defined]

        loaded_questions.append(norm_q)

    if len(loaded_questions) != 25:
        raise CampaignManifestError(
            f"Expected exactly 25 questions loaded, got {len(loaded_questions)}"
        )

    return loaded_questions


def calculate_campaign_results(
    questions: List[NormalizedQuestion],
    answers: Dict[int, str],
    elapsed_time: int = 0,
) -> Dict[str, Any]:
    """Calculate 100% in-memory campaign test results with truthful 3-bucket analysis.

    Zero database writes.
    Zero XP / streak / progress calculation.
    """
    total = len(questions)
    valid_answers = {
        i: ans.upper()
        for i, ans in answers.items()
        if isinstance(ans, str) and ans.upper() in ("A", "B", "C", "D")
    }

    answered = len(valid_answers)
    unanswered = total - answered

    correct = 0
    wrong = 0

    # Bucket tracking
    bucket_stats: Dict[str, Dict[str, Any]] = {
        b: {"total": 0, "answered": 0, "correct": 0, "wrong": 0, "accuracy": 0.0}
        for b in ANALYSIS_BUCKETS
    }

    for idx, q in enumerate(questions):
        bucket = getattr(q, "campaign_bucket", get_bucket_for_source(getattr(q, "campaign_source_file", "")))
        if bucket not in bucket_stats:
            bucket = BUCKET_GENERAL_STUDIES
        bucket_stats[bucket]["total"] += 1

        chosen = valid_answers.get(idx)
        if chosen is not None:
            bucket_stats[bucket]["answered"] += 1
            if chosen == q.correct_answer:
                correct += 1
                bucket_stats[bucket]["correct"] += 1
            else:
                wrong += 1
                bucket_stats[bucket]["wrong"] += 1

    # Calculate overall accuracy
    overall_accuracy = round((correct / answered * 100), 1) if answered > 0 else 0.0

    # Calculate accuracy per bucket
    for b in ANALYSIS_BUCKETS:
        b_att = bucket_stats[b]["answered"]
        b_corr = bucket_stats[b]["correct"]
        bucket_stats[b]["accuracy"] = round((b_corr / b_att * 100), 1) if b_att > 0 else 0.0

    # Strongest area: highest accuracy among attempted buckets
    attempted_buckets = [b for b in ANALYSIS_BUCKETS if bucket_stats[b]["answered"] > 0]
    strongest_bucket: Optional[str] = None
    if attempted_buckets:
        # Sort descending by accuracy, tie-break by total answered
        sorted_strong = sorted(
            attempted_buckets,
            key=lambda b: (bucket_stats[b]["accuracy"], bucket_stats[b]["correct"]),
            reverse=True,
        )
        strongest_bucket = sorted_strong[0]

    # Improvement area: lowest accuracy among sufficiently represented buckets
    # Only claim improvement area if user answered at least 3 questions in the test
    # and at least 1 question in the bucket.
    improvement_bucket: Optional[str] = None
    sufficiently_represented = [b for b in ANALYSIS_BUCKETS if bucket_stats[b]["answered"] >= 1]
    if answered >= 3 and sufficiently_represented:
        sorted_weak = sorted(
            sufficiently_represented,
            key=lambda b: (bucket_stats[b]["accuracy"], -bucket_stats[b]["total"]),
        )
        # Only highlight if accuracy is below 100% or user has made mistakes
        if sorted_weak[0] and bucket_stats[sorted_weak[0]]["accuracy"] < 100.0:
            improvement_bucket = sorted_weak[0]

    return {
        "total_questions": total,
        "answered": answered,
        "unanswered": unanswered,
        "correct": correct,
        "wrong": wrong,
        "accuracy": overall_accuracy,
        "score_fraction": f"{correct} / {total}",
        "elapsed_time_sec": max(0, int(elapsed_time)),
        "bucket_breakdown": bucket_stats,
        "strongest_bucket": strongest_bucket,
        "improvement_bucket": improvement_bucket,
    }
