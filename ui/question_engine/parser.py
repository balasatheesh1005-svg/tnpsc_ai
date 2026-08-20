import html
import re
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple


@dataclass
class OptionItem:
    id: str  # "A", "B", "C", "D"
    en: str
    ta: str = ""

    def get_display_text(self, lang_mode: str = "BOTH") -> str:
        en_text = self.en.strip()
        ta_text = self.ta.strip()
        
        if lang_mode == "EN" or not ta_text:
            return en_text
        if lang_mode == "TA" or not en_text:
            return ta_text
        if en_text == ta_text:
            return en_text
        return f"{en_text} / {ta_text}"


@dataclass
class ExplanationDetails:
    en: str = "No explanation available."
    ta: str = ""
    historical_context: str = ""
    reason: str = ""
    constitutional_impact: str = ""
    exam_trap: str = ""
    memory_trick: str = ""
    why_not_others: Dict[str, Dict[str, str]] = field(default_factory=dict)
    tnpsc_tip: Dict[str, str] = field(default_factory=dict)
    revision_fact: Dict[str, str] = field(default_factory=dict)
    source_reference: List[str] = field(default_factory=list)


@dataclass
class NormalizedQuestion:
    id: str
    subject: str
    topic: str
    subtopic: str
    difficulty: str
    question_type: str
    question_en: str
    question_ta: str
    options: List[OptionItem]
    correct_answer: str  # Uppercase "A", "B", "C", or "D"
    explanation: ExplanationDetails
    exam: str = "TNPSC Group I"
    year: Optional[int] = None
    bloom_level: str = "Understand"
    estimated_time_sec: int = 60
    pyq_similarity: str = "Standard"
    tags: List[str] = field(default_factory=list)
    raw: Dict[str, Any] = field(default_factory=dict)


class UniversalQuestionAdapter:
    """Universal parser & normalizer for any TNPSC question JSON format."""

    @staticmethod
    def normalize(data: Any) -> NormalizedQuestion:
        if isinstance(data, NormalizedQuestion):
            return data
            
        row = dict(data or {}) if isinstance(data, dict) else {}

        q_id = str(row.get("id") or row.get("question_id") or row.get("_id") or "q_unknown")
        subject = str(row.get("subject") or row.get("subject_name") or "General").strip().title()
        
        raw_topic = str(row.get("topic") or row.get("topic_name") or "General").strip()
        topic = raw_topic.replace("_", " ").title()
        
        subtopic = str(row.get("subtopic") or row.get("sub_topic") or "").strip()
        
        difficulty = str(row.get("difficulty") or row.get("level") or "Medium").strip().title()
        if difficulty == "Easy":
            difficulty = "Easy"
        elif difficulty in ["Hard", "High"]:
            difficulty = "Hard"
        elif "Exceptional" in difficulty:
            difficulty = "Exceptional Difficult"
        else:
            difficulty = "Medium"

        # Extract Question Text
        question_en = UniversalQuestionAdapter._extract_string(
            row, ["question_en", "question", "stem_en"], "Question text not available."
        )
        
        # Handle dict format for question {"en": "...", "ta": "..."}
        if isinstance(row.get("question"), dict):
            q_dict = row["question"]
            question_en = str(q_dict.get("en") or question_en)
            question_ta = str(q_dict.get("ta") or "")
        else:
            question_ta = UniversalQuestionAdapter._extract_string(row, ["question_ta", "stem_ta"], "")

        # Options Normalization
        options_list = UniversalQuestionAdapter._normalize_options(row)

        # Correct Answer Normalization
        correct_ans = UniversalQuestionAdapter._extract_correct_answer(row)

        # Question Type Detection
        qtype = str(row.get("question_type") or row.get("type") or "").strip()
        if not qtype:
            qtype = UniversalQuestionAdapter._detect_question_type(question_en, row.get("tags", []))

        # Explanation Normalization
        explanation_obj = UniversalQuestionAdapter._normalize_explanation(row)

        # Metadata
        exam = str(row.get("exam") or "TNPSC Group I").strip()
        year = None
        try:
            if row.get("year"):
                year = int(row["year"])
        except (TypeError, ValueError):
            year = None

        bloom_level = str(row.get("bloom_level") or row.get("bloom") or "Understand").strip().title()
        
        est_time = 60
        try:
            if row.get("estimated_time_sec"):
                est_time = int(row["estimated_time_sec"])
        except (TypeError, ValueError):
            est_time = 60

        pyq_sim = str(row.get("pyq_similarity") or row.get("pyq_trend") or "Standard").strip().title()
        tags = list(row.get("tags") or [])

        return NormalizedQuestion(
            id=q_id,
            subject=subject,
            topic=topic,
            subtopic=subtopic,
            difficulty=difficulty,
            question_type=qtype,
            question_en=question_en,
            question_ta=question_ta,
            options=options_list,
            correct_answer=correct_ans,
            explanation=explanation_obj,
            exam=exam,
            year=year,
            bloom_level=bloom_level,
            estimated_time_sec=est_time,
            pyq_similarity=pyq_sim,
            tags=tags,
            raw=row,
        )

    @staticmethod
    def _extract_string(row: dict, keys: List[str], default: str) -> str:
        for k in keys:
            val = row.get(k)
            if isinstance(val, str) and val.strip():
                return val.strip()
        return default

    @staticmethod
    def _normalize_options(row: dict) -> List[OptionItem]:
        keys = ["A", "B", "C", "D"]
        result = []

        # Case 1: options is a list of dicts [{"id": "A", "en": "...", "ta": "..."}]
        raw_options = row.get("options")
        if isinstance(raw_options, list):
            for idx, item in enumerate(raw_options):
                opt_key = keys[idx] if idx < len(keys) else str(idx + 1)
                if isinstance(item, dict):
                    opt_id = str(item.get("id") or opt_key).upper()
                    o_en = str(item.get("en") or item.get("text") or item.get("english") or "")
                    o_ta = str(item.get("ta") or item.get("tamil") or "")
                    result.append(OptionItem(id=opt_id, en=o_en, ta=o_ta))
                elif isinstance(item, str):
                    result.append(OptionItem(id=opt_key, en=item, ta=""))
            return result

        # Case 2: options is a dict {"A": "Text", "B": "Text"} or {"A": {"en": "..", "ta": ".."}}
        if isinstance(raw_options, dict):
            for k in keys:
                if k in raw_options:
                    val = raw_options[k]
                    if isinstance(val, dict):
                        o_en = str(val.get("en") or val.get("english") or "")
                        o_ta = str(val.get("ta") or val.get("tamil") or "")
                        result.append(OptionItem(id=k, en=o_en, ta=o_ta))
                    else:
                        result.append(OptionItem(id=k, en=str(val), ta=""))
            if result:
                return result

        # Case 3: Parallel lists options_en and options_ta
        opts_en = row.get("options_en")
        opts_ta = row.get("options_ta")
        if isinstance(opts_en, list):
            for idx, val in enumerate(opts_en):
                opt_key = keys[idx] if idx < len(keys) else str(idx + 1)
                t_val = ""
                if isinstance(opts_ta, list) and idx < len(opts_ta):
                    t_val = str(opts_ta[idx])
                result.append(OptionItem(id=opt_key, en=str(val), ta=t_val))
            return result

        return result

    @staticmethod
    def _extract_correct_answer(row: dict) -> str:
        candidates = [
            row.get("correct_answer"),
            row.get("answer"),
            row.get("correct"),
        ]
        if isinstance(row.get("correct_answers"), (list, tuple, set)) and row.get("correct_answers"):
            candidates.insert(0, row["correct_answers"][0])
            
        for cand in candidates:
            if cand is not None and str(cand).strip():
                ans_str = str(cand).strip().upper()
                if ans_str in ["A", "B", "C", "D"]:
                    return ans_str
                # Handles index 0, 1, 2, 3
                if ans_str in ["0", "1", "2", "3"]:
                    return ["A", "B", "C", "D"][int(ans_str)]
        return "A"

    @staticmethod
    def _detect_question_type(text: str, tags: List[str]) -> str:
        tag_str = " ".join(tags).lower()
        if "statement" in tag_str or "statement based" in tag_str:
            return "Statement Based"
        if "assertion" in tag_str or "reason" in tag_str:
            return "Assertion & Reason"
        if "match" in tag_str or "following" in tag_str:
            return "Match the Following"
        if "chronology" in tag_str or "timeline" in tag_str:
            return "Chronology"
        if "multi-act" in tag_str or "comparative" in tag_str:
            return "Multi-Act Comparative"

        text_lower = text.lower()
        if "statement" in text_lower or "consider the following" in text_lower or re.search(r"\n\s*1\.\s+", text):
            return "Statement Based"
        if "assertion (a)" in text_lower or "reason (r)" in text_lower:
            return "Assertion & Reason"
        if "match list" in text_lower or "match the following" in text_lower:
            return "Match the Following"
        if "chronological" in text_lower or "arrange the following" in text_lower:
            return "Chronology"

        return "Direct MCQ"

    @staticmethod
    def _normalize_explanation(row: dict) -> ExplanationDetails:
        exp_raw = row.get("explanation")
        en_str = ""
        ta_str = ""
        
        if isinstance(exp_raw, dict):
            en_str = str(exp_raw.get("en") or exp_raw.get("english") or "")
            ta_str = str(exp_raw.get("ta") or exp_raw.get("tamil") or "")
        elif isinstance(exp_raw, str):
            en_str = exp_raw

        en_str = en_str or str(row.get("explanation_en") or "Explanation details available upon review.")
        ta_str = ta_str or str(row.get("explanation_ta") or "விளக்கம் விரைவில் புதுப்பிக்கப்படும்.")

        # Structured sections
        hist_ctx = ""
        reason = ""
        const_imp = ""
        exam_trap = ""
        mem_trick = ""

        # Parse from explanation text if structured tags exist
        if "Historical Context:" in en_str:
            parts = re.split(r"(Historical Context:|Reason:|Constitutional Impact:|Exam Trap:|Memory Trick:)", en_str)
            for i in range(1, len(parts), 2):
                header = parts[i].strip()
                content = parts[i+1].strip() if i+1 < len(parts) else ""
                if header == "Historical Context:":
                    hist_ctx = content
                elif header == "Reason:":
                    reason = content
                elif header == "Constitutional Impact:":
                    const_imp = content
                elif header == "Exam Trap:":
                    exam_trap = content
                elif header == "Memory Trick:":
                    mem_trick = content

        # Extract why_not_others, tnpsc_tip, revision_fact, source_reference
        wno = row.get("why_not_others")
        wno_dict = {}
        if isinstance(wno, dict):
            for k, v in wno.items():
                if isinstance(v, dict):
                    wno_dict[str(k).upper()] = {
                        "en": str(v.get("en") or ""),
                        "ta": str(v.get("ta") or "")
                    }
                elif isinstance(v, str):
                    wno_dict[str(k).upper()] = {"en": v, "ta": ""}

        tip_dict = {}
        raw_tip = row.get("tnpsc_tip")
        if isinstance(raw_tip, dict):
            tip_dict = {"en": str(raw_tip.get("en") or ""), "ta": str(raw_tip.get("ta") or "")}
        elif isinstance(raw_tip, str):
            tip_dict = {"en": raw_tip, "ta": ""}

        rf_dict = {}
        raw_rf = row.get("revision_fact")
        if isinstance(raw_rf, dict):
            rf_dict = {"en": str(raw_rf.get("en") or ""), "ta": str(raw_rf.get("ta") or "")}
        elif isinstance(raw_rf, str):
            rf_dict = {"en": raw_rf, "ta": ""}

        sources = []
        raw_src = row.get("source_reference") or row.get("source") or row.get("sources")
        if isinstance(raw_src, list):
            sources = [str(s) for s in raw_src if s]
        elif isinstance(raw_src, str) and raw_src.strip():
            sources = [raw_src.strip()]

        return ExplanationDetails(
            en=en_str,
            ta=ta_str,
            historical_context=hist_ctx,
            reason=reason,
            constitutional_impact=const_imp,
            exam_trap=exam_trap,
            memory_trick=mem_trick,
            why_not_others=wno_dict,
            tnpsc_tip=tip_dict,
            revision_fact=rf_dict,
            source_reference=sources,
        )
