import json
import os
import re
from typing import Dict, List, Optional, Set, Tuple
import streamlit as st

from core.topics_loader import get_topic_metadata_by_id
from core.weakness_ai import get_weakness

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BASE_PATH = os.path.join(os.path.dirname(CURRENT_DIR), "data", "notes")

# Conservative stop words (English interrogatives, prepositions, articles, copulas)
STOP_WORDS: Set[str] = {
    "the", "a", "an", "is", "are", "was", "were", "on", "in", "of", "to", "for",
    "when", "what", "which", "who", "whom", "whose", "how", "why", "where",
    "did", "does", "do", "and", "or", "at", "by", "from", "with", "as", "into",
    "about", "any", "all", "some", "it", "its", "their", "this", "that", "these",
    "those", "be", "been", "being", "have", "has", "had", "having", "will", "would",
    "shall", "should", "can", "could", "may", "might", "must", "then", "than",
    "so", "tell", "me", "give", "know", "want", "please", "i"
}

# Generic internal metadata keys to strictly exclude from learner-facing text
EXCLUDED_METADATA_KEYS: Set[str] = {
    "id", "slug", "key", "type", "ui_type", "status", "version", "schema_version",
    "hash", "source", "source_hash", "builder_version", "file_path", "filename",
    "meta", "metadata", "builder_metadata", "validation", "category_id"
}

# Canonical TNPSC topic alias mapping for high-signal conceptual synonyms
CANONICAL_ALIASES: Dict[str, List[str]] = {
    "gst": ["goods and services tax", "goods and service tax", "gst council"],
    "goods and services tax": ["gst", "goods and service tax"],
    "gst council": ["goods and services tax council", "article 279a"],
    "ivc": ["indus valley civilization"],
    "indus valley": ["indus valley civilization"],
    "dpsp": ["directive principles of state policy"],
    "fr": ["fundamental rights"],
    "niti aayog": ["national institution for transforming india"],
    "finance commission": ["finance commission of india"],
    "pyq": ["previous year questions"],
    "upsc": ["union public service commission"],
    "tnpsc": ["tamil nadu public service commission"],
}


def is_internal_metadata_key(key: str) -> bool:
    """Checks whether a dictionary key is internal metadata that should not be learner prose."""
    k = str(key).lower().strip()
    if k in EXCLUDED_METADATA_KEYS:
        return True
    if k.endswith("_id") or k.endswith("_ids") or k.startswith("meta_"):
        return True
    return False


def extract_learner_safe_blocks(obj) -> List[str]:
    """
    Recursively extracts learner-facing text blocks while strictly excluding
    internal IDs (e.g. trap_id, table_id, node_id, file paths, builder metadata).
    Handles comparison tables, revision cards, definitions, and trap explanations.
    """
    blocks = []
    if isinstance(obj, str):
        s = obj.strip()
        if s:
            blocks.append(s)
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, list):
                # Structured comparison table row
                row_str = " | ".join(str(cell).strip() for cell in item if str(cell).strip())
                if row_str:
                    blocks.append(row_str)
            else:
                blocks.extend(extract_learner_safe_blocks(item))
    elif isinstance(obj, dict):
        for k, v in obj.items():
            if is_internal_metadata_key(k):
                continue
            blocks.extend(extract_learner_safe_blocks(v))
    return blocks


def tokenize_text(text: str) -> List[str]:
    """Tokenizes text using word boundaries, fully supporting English, alphanumeric, and Tamil script."""
    return re.findall(r"[a-zA-Z0-9_\u0B80-\u0BFF]+", str(text).lower())


def normalize_query_terms(query: str) -> Tuple[str, List[str], List[str]]:
    """
    Normalizes query string and separates raw tokens from meaningful syllabus terms.
    Returns: (cleaned_query, all_tokens, meaningful_tokens).
    """
    q_clean = str(query).lower().strip()
    all_tokens = tokenize_text(q_clean)
    meaningful_tokens = [t for t in all_tokens if t not in STOP_WORDS]
    return q_clean, all_tokens, meaningful_tokens


@st.cache_data
def load_notes() -> List[Dict]:
    """
    Loads all verified TNPSC Nova notes with learner-safe text extraction,
    canonical syllabus metadata, and official keywords.
    """
    notes_data = []

    if not os.path.exists(BASE_PATH):
        return notes_data

    for subject in sorted(os.listdir(BASE_PATH)):
        subject_path = os.path.join(BASE_PATH, subject)
        if not os.path.isdir(subject_path):
            continue

        for file in sorted(os.listdir(subject_path)):
            if file.endswith(".json"):
                file_path = os.path.join(subject_path, file)
                try:
                    if os.path.getsize(file_path) == 0:
                        continue

                    with open(file_path, "r", encoding="utf-8") as f:
                        data = json.load(f)

                        blocks = extract_learner_safe_blocks(data.get("content", {}))
                        note_file_stem = file.replace(".json", "")
                        meta = get_topic_metadata_by_id(subject, note_file_stem)

                        topic = data.get("topic") or meta.get("display_title") or note_file_stem.replace("_", " ").title()
                        keywords = data.get("keywords", [])
                        if not isinstance(keywords, list):
                            keywords = []

                        notes_data.append(
                            {
                                "subject": subject,
                                "topic_id": meta.get("topic_id", note_file_stem),
                                "repository_id": meta.get("repository_id", note_file_stem),
                                "display_title": meta.get("display_title", topic),
                                "topic": topic,
                                "keywords": [str(k) for k in keywords if k],
                                "blocks": blocks,
                                "searchable_text": " ".join(blocks).lower(),
                            }
                        )
                except Exception as e:
                    print(f"⚠️ Warning: Skipping invalid note {file_path}. Error: {e}")
                    continue

    return notes_data


def score_note_evidence(note: Dict, q_clean: str, meaningful_tokens: List[str]) -> Tuple[int, List[str]]:
    """
    Scores note evidence relevance using a deterministic hierarchy:
    1. Multi-word phrase match in topic title or keywords (+50)
    2. Canonical alias match in topic title or keywords (+40)
    3. Topic title token boundary match (+20 per token)
    4. Keyword token boundary match (+15 per token)
    5. Learner-safe content token match (+3 per token, capped)
    6. Subject agreement bonus (+10 if topic/keywords also agree)
    """
    if not meaningful_tokens:
        return 0, []

    score = 0
    matched_reasons = []

    topic_lower = str(note["topic"]).lower()
    display_lower = str(note["display_title"]).lower()
    subject_lower = str(note["subject"]).lower()
    keywords_lower = [str(k).lower() for k in note["keywords"]]

    # 1. Exact canonical phrase matching (multi-word)
    m_phrase = " ".join(meaningful_tokens)
    if len(meaningful_tokens) >= 2 and (
        m_phrase in topic_lower or m_phrase in display_lower or any(m_phrase in kw for kw in keywords_lower)
    ):
        score += 50
        matched_reasons.append(f"phrase_match({m_phrase})")

    # 2. Canonical topic aliases
    for alias_key, alias_targets in CANONICAL_ALIASES.items():
        if alias_key in q_clean:
            for tgt in alias_targets:
                if tgt in topic_lower or tgt in display_lower or any(tgt in kw for kw in keywords_lower):
                    score += 40
                    matched_reasons.append(f"alias_topic_kw({tgt})")
                elif tgt in note["searchable_text"]:
                    score += 15
                    matched_reasons.append(f"alias_content({tgt})")

    # 3. Token-level matching with token boundary isolation
    topic_tokens = set(tokenize_text(topic_lower)).union(tokenize_text(display_lower))
    kw_tokens = set()
    for kw in keywords_lower:
        kw_tokens.update(tokenize_text(kw))
    content_tokens = set(tokenize_text(note["searchable_text"]))

    for t in meaningful_tokens:
        if t in topic_tokens:
            score += 20
            matched_reasons.append(f"topic_token({t})")
        elif t in kw_tokens:
            score += 15
            matched_reasons.append(f"kw_token({t})")
        elif t in content_tokens:
            score += 3
            matched_reasons.append(f"content_token({t})")

    # 4. Subject agreement bonus (only if topic, alias, or keyword also matched)
    if any(r.startswith(("phrase", "alias", "topic_token", "kw_token")) for r in matched_reasons):
        if subject_lower in q_clean or any(t == subject_lower for t in meaningful_tokens):
            score += 10
            matched_reasons.append(f"subject_bonus({subject_lower})")

    return score, matched_reasons


def classify_evidence_confidence(score: int, matched_reasons: List[str]) -> str:
    """
    Maps deterministic evidence score to semantic confidence states.
    Prevents arbitrary numeric probability fabrication.
    """
    if score >= 50 or any(r.startswith(("phrase", "alias_topic_kw")) for r in matched_reasons):
        return "STRONG MATCH"
    elif score >= 25:
        return "GOOD MATCH"
    elif score >= 10:
        return "LIMITED EVIDENCE"
    return "INSUFFICIENT EVIDENCE"


def extract_best_evidence_sentences(note: Dict, q_clean: str, meaningful_tokens: List[str]) -> List[str]:
    """
    Selects top 2-3 most relevant, learner-facing sentences from the verified note evidence.
    Ranks by query token overlap and specific factual indicators.
    """
    scored_sentences = []
    m_set = set(meaningful_tokens)
    m_phrase = " ".join(meaningful_tokens)

    for block in note.get("blocks", []):
        b_clean = block.strip()
        if len(b_clean) < 15:
            continue

        # Split block into distinct sentences or keep concise bullet items
        sentences = re.split(r"(?<=[.!?])\s+|\n+", b_clean)
        for sent in sentences:
            s_stripped = sent.strip()
            if len(s_stripped) < 15:
                continue

            s_tokens = set(tokenize_text(s_stripped))
            overlap = len(m_set.intersection(s_tokens))
            s_score = overlap * 5

            if len(meaningful_tokens) >= 2 and m_phrase in s_stripped.lower():
                s_score += 25

            # Factual query intent bonus (date, year, article, amendment)
            if any(t in ["date", "when", "year", "article", "amendment", "rollout"] for t in tokenize_text(q_clean)):
                if re.search(r"\b(19\d\d|20\d\d|article\s*\d+[a-z]?|amendment)\b", s_stripped, re.I):
                    s_score += 10

            if s_score > 0:
                scored_sentences.append((s_score, s_stripped))

    scored_sentences.sort(key=lambda x: x[0], reverse=True)

    # Deduplicate sentences by normalized prefix
    seen = set()
    unique_top = []
    for sc, txt in scored_sentences:
        key = txt[:60].lower()
        if key not in seen:
            seen.add(key)
            unique_top.append(txt)
            if len(unique_top) == 3:
                break

    if not unique_top:
        for b in note.get("blocks", []):
            if len(b.strip()) >= 25:
                unique_top = [b.strip()[:250]]
                break

    return unique_top


def ai_teacher(question: str, user: Optional[str] = None) -> str:
    """
    Core AI Teacher retrieval engine.
    Follows: User Question -> Safe Normalization -> Note Retrieval ->
             Deterministic Evidence Ranking -> Semantic Confidence -> Conservative Answer.
    """
    q_clean, all_tokens, meaningful_tokens = normalize_query_terms(question)

    # Abstention Gate 1: No meaningful syllabus tokens remain
    if not meaningful_tokens:
        return (
            "📘 Answer கிடைக்கவில்லை.\n\n"
            "I couldn't find enough reliable evidence in the current TNPSC Nova AI notes for this question.\n"
            "Try asking with specific TNPSC syllabus terms or topic keywords (e.g., GST, Preamble, Indus Valley)."
        )

    notes = load_notes()
    if not notes:
        return (
            "📘 Answer கிடைக்கவில்லை.\n\n"
            "Notes corpus is currently unavailable. Please try again shortly."
        )

    scored_notes = []
    for note in notes:
        score, reasons = score_note_evidence(note, q_clean, meaningful_tokens)
        if score > 0:
            scored_notes.append((score, note, reasons))

    scored_notes.sort(key=lambda x: x[0], reverse=True)

    # Abstention Gate 2: Insufficient evidence score
    if not scored_notes or scored_notes[0][0] < 10:
        return (
            "📘 Answer கிடைக்கவில்லை.\n\n"
            "I couldn't find enough reliable evidence in the current TNPSC Nova AI notes for this question.\n"
            "Try asking with specific TNPSC syllabus terms or topic keywords (e.g., GST, Preamble, Indus Valley)."
        )

    top_score, best_match, top_reasons = scored_notes[0]
    confidence_tier = classify_evidence_confidence(top_score, top_reasons)
    best_sentences = extract_best_evidence_sentences(best_match, q_clean, meaningful_tokens)

    answer_points = "\n\n".join([f"{i}. {line}" for i, line in enumerate(best_sentences, start=1)])

    memory_note = ""
    if user:
        weak_data = get_weakness(user)
        repo_key = f"{best_match['subject']}-{best_match['repository_id']}"
        topic_key = f"{best_match['subject']}-{best_match['topic_id']}"

        if weak_data and (repo_key in weak_data or topic_key in weak_data):
            memory_note = "\n\n⚠️ You have a weak accuracy score in this topic area.\nRevise properly!"

    return f"""📘 {best_match['subject'].upper()}
- {best_match['topic']}

🎯 Evidence Confidence: {confidence_tier}

🧠 Key Notes Evidence:
{answer_points}{memory_note}

🚀 Powered by Nova AI Teacher"""


def explain_answer(question: str, correct: str, user_ans: str) -> str:
    """Preserved legacy diagnostic explanation helper."""
    return f"""
❌ Your Answer:
{user_ans.upper()}

✅ Correct Answer:
{correct.upper()}

📘 Explanation:
This question is important for TNPSC exams.
Focus on key facts and revise this topic properly.

🚀 Nova AI Analysis Complete
"""
