import os
import re
import json
from typing import Dict, List, Optional, Set, Tuple


def normalize_text(text: str) -> str:
    """Normalize text for strict duplicate checks."""
    if not text:
        return ""
    # Lowercase, strip punctuation and whitespace
    t = text.lower().strip()
    t = re.sub(r"[^\w\s]", "", t)
    t = re.sub(r"\s+", " ", t)
    return t


class TopicDuplicateIndex:
    """
    Compact in-memory metadata index of questions for a topic.
    Avoids repeatedly loading massive JSON payloads into generation contexts.
    """

    def __init__(self, topic_id: str):
        self.topic_id = topic_id
        self.exact_stems_en: Set[str] = set()
        self.exact_stems_ta: Set[str] = set()
        self.normalized_stems_en: Set[str] = set()
        self.question_ids: Set[str] = set()
        self.learning_targets: Dict[str, str] = {}  # target -> question_id
        self.compact_records: List[Dict[str, str]] = []

    def add_question(self, q: dict) -> None:
        qid = q.get("id", "")
        q_en = q.get("question_en") or q.get("question", "")
        q_ta = q.get("question_ta", "")

        self.question_ids.add(qid)
        if q_en:
            self.exact_stems_en.add(q_en.strip())
            norm_en = normalize_text(q_en)
            self.normalized_stems_en.add(norm_en)
        if q_ta:
            self.exact_stems_ta.add(q_ta.strip())

        # Extract target from revision_fact or tnpsc_tip if available
        rf = q.get("revision_fact", {})
        rf_en = rf.get("en", "") if isinstance(rf, dict) else str(rf)
        if rf_en:
            self.learning_targets[normalize_text(rf_en)] = qid

        self.compact_records.append({
            "id": qid,
            "stem_en": q_en.strip()[:100],
            "norm_en": normalize_text(q_en),
            "target": rf_en[:80] if rf_en else ""
        })

    def load_from_files(self, file_paths: List[str]) -> int:
        """Load questions from existing file paths into the compact index."""
        loaded = 0
        for fp in file_paths:
            if not os.path.exists(fp):
                continue
            try:
                with open(fp, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict):
                            self.add_question(item)
                            loaded += 1
            except Exception as e:
                print(f"Warning: Failed to index {fp}: {e}")
        return loaded

    def check_duplicate(self, question_en: str, question_ta: str = "") -> Tuple[bool, str]:
        """
        Returns (is_duplicate, reason).
        """
        if not question_en:
            return False, ""

        q_en_clean = question_en.strip()
        if q_en_clean in self.exact_stems_en:
            return True, "Exact English stem already exists in index"

        norm_en = normalize_text(q_en_clean)
        if norm_en in self.normalized_stems_en:
            return True, "Normalized English stem collision detected"

        if question_ta and question_ta.strip() in self.exact_stems_ta:
            return True, "Exact Tamil stem already exists in index"

        # Check high token overlap (Jaccard similarity > 0.85)
        words_new = set(norm_en.split())
        if len(words_new) >= 8:
            for rec in self.compact_records:
                words_existing = set(rec["norm_en"].split())
                if len(words_existing) >= 8:
                    intersection = len(words_new & words_existing)
                    union = len(words_new | words_existing)
                    sim = intersection / union if union > 0 else 0
                    if sim > 0.85:
                        return True, f"High semantic/token similarity ({sim:.2f}) with existing question {rec['id']}"

        return False, ""

    def count(self) -> int:
        return len(self.question_ids)
