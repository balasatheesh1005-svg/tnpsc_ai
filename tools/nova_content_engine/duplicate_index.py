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
    Compact in-memory metadata index of questions supporting 7-level duplicate detection.
    Avoids repeatedly loading massive JSON payloads into generation contexts.

    Levels:
      Level 1: Exact stem duplicate (English & Tamil)
      Level 2: Normalized stem duplicate
      Level 3: Concept + answer collision
      Level 4: Near duplicate / high Jaccard token overlap (> 0.85)
      Level 5: Cross-topic duplicate
      Level 6: Cross-difficulty duplicate
      Level 7: Grand Test vs Core collision
    """

    def __init__(self, topic_id: str):
        self.topic_id = topic_id
        self.exact_stems_en: Set[str] = set()
        self.exact_stems_ta: Set[str] = set()
        self.normalized_stems_en: Set[str] = set()
        self.question_ids: Set[str] = set()
        self.learning_targets: Dict[str, str] = {}  # target -> question_id
        self.concept_answers: Set[Tuple[str, str]] = set()  # (norm_concept, norm_answer_text)
        self.stems_by_difficulty: Dict[str, Set[str]] = {}
        self.stems_by_category: Dict[str, Set[str]] = {}
        self.stems_by_topic: Dict[str, Set[str]] = {}
        self.compact_records: List[Dict[str, str]] = []

    def add_question(self, q: dict, topic_id: Optional[str] = None, category: Optional[str] = None) -> None:
        qid = q.get("id", "")
        q_en = q.get("question_en") or q.get("question", "")
        q_ta = q.get("question_ta", "")
        diff = str(q.get("difficulty", "")).capitalize()
        cat = category or ("grand_test" if "_gt_" in qid.lower() or "_grand" in qid.lower() else "core")
        t_id = topic_id or q.get("topic", self.topic_id)

        self.question_ids.add(qid)
        norm_en = ""
        if q_en:
            self.exact_stems_en.add(q_en.strip())
            norm_en = normalize_text(q_en)
            self.normalized_stems_en.add(norm_en)
        if q_ta:
            self.exact_stems_ta.add(q_ta.strip())

        # Category and Difficulty tracking
        if norm_en:
            if diff:
                if diff not in self.stems_by_difficulty:
                    self.stems_by_difficulty[diff] = set()
                self.stems_by_difficulty[diff].add(norm_en)

            if cat:
                if cat not in self.stems_by_category:
                    self.stems_by_category[cat] = set()
                self.stems_by_category[cat].add(norm_en)

            if t_id:
                if t_id not in self.stems_by_topic:
                    self.stems_by_topic[t_id] = set()
                self.stems_by_topic[t_id].add(norm_en)

        # Concept + answer tracking (Level 3)
        rf = q.get("revision_fact", {})
        rf_en = rf.get("en", "") if isinstance(rf, dict) else str(rf)
        if rf_en:
            norm_target = normalize_text(rf_en)
            self.learning_targets[norm_target] = qid

            # Extract correct answer text
            ans_key = q.get("correct_answer", "A")
            opts = q.get("options", [])
            ans_text = ""
            for o in opts:
                if isinstance(o, dict) and o.get("id") == ans_key:
                    ans_text = o.get("en", "")
                    break
            if ans_text:
                self.concept_answers.add((norm_target, normalize_text(ans_text)))

        self.compact_records.append({
            "id": qid,
            "stem_en": q_en.strip()[:100] if q_en else "",
            "norm_en": norm_en,
            "target": rf_en[:80] if rf_en else "",
            "difficulty": diff,
            "category": cat,
            "topic_id": t_id,
        })

    def load_from_files(self, file_paths: List[str]) -> int:
        """Load questions from existing file paths into the compact index."""
        loaded = 0
        for fp in file_paths:
            if not os.path.exists(fp):
                continue
            cat = "grand_test" if "grand_test" in fp.lower() or "_grand." in fp.lower() else "core"
            try:
                with open(fp, "r", encoding="utf-8") as f:
                    data = json.load(f)
                if isinstance(data, list):
                    for item in data:
                        if isinstance(item, dict):
                            self.add_question(item, category=cat)
                            loaded += 1
            except Exception as e:
                print(f"Warning: Failed to index {fp}: {e}")
        return loaded

    def check_duplicate(
        self,
        question_en: str,
        question_ta: str = "",
        correct_answer_text: str = "",
        revision_fact: str = "",
        difficulty: str = "",
        category: str = "",
        topic_id: str = "",
    ) -> Tuple[bool, str]:
        """
        7-Level Duplicate Check.
        Returns (is_duplicate, reason).
        """
        if not question_en:
            return False, ""

        q_en_clean = question_en.strip()
        norm_en = normalize_text(q_en_clean)

        # Level 7: Grand Test vs Core collision (evaluated first when category is specified)
        if category and norm_en in self.normalized_stems_en:
            is_gt = category in ["grand_test", "grand"]
            opp_cat = "core" if is_gt else "grand_test"
            if norm_en in self.stems_by_category.get(opp_cat, set()):
                return True, f"LEVEL 7: Grand Test vs Core stem collision ({category} vs {opp_cat})"

        # Level 6: Cross-difficulty duplicate (evaluated when difficulty is specified)
        if difficulty and norm_en in self.normalized_stems_en:
            diff_cap = difficulty.capitalize()
            for other_diff, stems in self.stems_by_difficulty.items():
                if other_diff != diff_cap and norm_en in stems:
                    return True, f"LEVEL 6: Cross-difficulty stem collision between {diff_cap} and {other_diff}"

        # Level 5: Cross-topic duplicate (evaluated when topic_id is specified)
        if topic_id and norm_en in self.normalized_stems_en:
            for other_tid, stems in self.stems_by_topic.items():
                if other_tid != topic_id and norm_en in stems:
                    return True, f"LEVEL 5: Cross-topic stem collision with topic '{other_tid}'"

        # Level 1: Exact stem duplicate
        if q_en_clean in self.exact_stems_en:
            return True, "LEVEL 1: Exact English stem already exists in index"
        if question_ta and question_ta.strip() in self.exact_stems_ta:
            return True, "LEVEL 1: Exact Tamil stem already exists in index"

        # Level 2: Normalized stem duplicate
        if norm_en in self.normalized_stems_en:
            return True, "LEVEL 2: Normalized English stem collision detected"

        # Level 3: Concept + answer collision
        if revision_fact and correct_answer_text:
            pair = (normalize_text(revision_fact), normalize_text(correct_answer_text))
            if pair in self.concept_answers:
                return True, "LEVEL 3: Identical learning target and correct answer collision detected"

        # Level 4: Near duplicate / high Jaccard token overlap (> 0.85)
        words_new = set(norm_en.split())
        if len(words_new) >= 8:
            for rec in self.compact_records:
                words_existing = set(rec["norm_en"].split())
                if len(words_existing) >= 8:
                    intersection = len(words_new & words_existing)
                    union = len(words_new | words_existing)
                    sim = intersection / union if union > 0 else 0
                    if sim > 0.85:
                        return True, f"LEVEL 4: High token similarity ({sim:.2f}) with existing question {rec['id']}"

        return False, ""

    def count(self) -> int:
        return len(self.question_ids)
