from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass(frozen=True)
class Question:
    id: str
    question_en: str
    options: Dict[str, str]
    correct_answer: str
    question_ta: str = ""
    exam: str = ""
    year: Optional[int] = None
    subject: str = ""
    topic: str = ""
    subtopic: str = ""
    difficulty: str = ""
    explanation: Dict[str, str] = field(default_factory=dict)
    related_note: str = ""
    tags: List[str] = field(default_factory=list)
    repeat_years: List[int] = field(default_factory=list)
    ai_trick: str = ""
    source: str = ""
    practice_set: str = ""
    raw: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_dict(cls, data):
        row = dict(data or {})
        
        # Safely extract related_note / related_notes
        related_note_val = ""
        raw_val = row.get("related_note")
        if raw_val is None or raw_val == "":
            raw_val = row.get("related_notes")
        
        if isinstance(raw_val, list):
            valid_items = [item for item in raw_val if isinstance(item, str) and item.strip()]
            related_note_val = valid_items[0] if valid_items else ""
        elif isinstance(raw_val, str):
            related_note_val = raw_val.strip()
            
        return cls(
            id=str(row.get("id", "")),
            question_en=str(row.get("question_en") or row.get("question") or ""),
            question_ta=str(row.get("question_ta") or ""),
            options=dict(row.get("options") or {}),
            correct_answer=str(
                row.get("correct_answer")
                or row.get("answer")
                or (row.get("correct_answers")[0] if isinstance(row.get("correct_answers"), (list, tuple, set)) and row.get("correct_answers") else "")
                or ""
            ),
            exam=str(row.get("exam") or ""),
            year=_safe_int(row.get("year")),
            subject=str(row.get("subject") or ""),
            topic=str(row.get("topic") or ""),
            subtopic=str(row.get("subtopic") or ""),
            difficulty=str(row.get("difficulty") or ""),
            explanation=dict(row.get("explanation") or {}),
            related_note=related_note_val,
            tags=list(row.get("tags") or []),
            repeat_years=list(row.get("repeat_years") or []),
            ai_trick=str(row.get("ai_trick") or ""),
            source=str(row.get("source") or ""),
            practice_set=str(row.get("practice_set") or ""),
            raw=row,
        )

    def to_dict(self):
        row = dict(self.raw)
        row.update(
            {
                "id": self.id,
                "exam": self.exam,
                "year": self.year,
                "subject": self.subject,
                "topic": self.topic,
                "subtopic": self.subtopic,
                "difficulty": self.difficulty,
                "question_en": self.question_en,
                "question_ta": self.question_ta,
                "options": dict(self.options),
                "correct_answer": self.correct_answer,
                "explanation": dict(self.explanation),
                "related_note": self.related_note,
                "related_notes": self.related_note,
                "tags": list(self.tags),
                "repeat_years": list(self.repeat_years),
                "ai_trick": self.ai_trick,
                "source": self.source,
                "practice_set": self.practice_set,
            }
        )
        return row


@dataclass
class ValidationResult:
    valid: bool
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)


@dataclass
class QuestionProgress:
    user_id: str
    mode: str
    question_id: str
    selected_answer: str = ""
    is_correct: bool = False
    attempts: int = 0
    updated_at: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "mode": self.mode,
            "question_id": self.question_id,
            "selected_answer": self.selected_answer,
            "is_correct": self.is_correct,
            "attempts": self.attempts,
            "updated_at": self.updated_at,
            "metadata": dict(self.metadata),
        }


@dataclass
class QuestionStatistics:
    total_questions: int = 0
    by_exam: Dict[str, int] = field(default_factory=dict)
    by_year: Dict[str, int] = field(default_factory=dict)
    by_subject: Dict[str, int] = field(default_factory=dict)
    by_difficulty: Dict[str, int] = field(default_factory=dict)
    invalid_questions: int = 0

    def to_dict(self):
        return {
            "total_questions": self.total_questions,
            "by_exam": dict(self.by_exam),
            "by_year": dict(self.by_year),
            "by_subject": dict(self.by_subject),
            "by_difficulty": dict(self.by_difficulty),
            "invalid_questions": self.invalid_questions,
        }


def _safe_int(value):
    try:
        return int(value)
    except (TypeError, ValueError):
        return None

