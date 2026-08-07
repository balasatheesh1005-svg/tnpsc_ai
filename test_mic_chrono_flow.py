import sys
import json

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from core.topics_loader import get_topic_metadata_by_id
from core.question_loader import load_questions

print("=== VERIFYING MAKING OF INDIAN CONSTITUTION CHRONOLOGY FLOW ===")

mic_parts = [
    "polity_making_of_indian_constitution_part_1",
    "polity_making_of_indian_constitution_part_2",
    "polity_making_of_indian_constitution_part_3"
]

print("\n--- 1. Metadata Mappings Check ---")
for mic in mic_parts:
    meta = get_topic_metadata_by_id("polity", mic)
    print(f"Topic ID: {meta['topic_id']} -> Repository ID: {meta['repository_id']} (Display: {meta['display_title']})")
    assert meta["repository_id"] == "polity_making_of_indian_constitution", f"MIC Mismatch for {mic}"

print("\n--- 2. Chronology Question Loading Verification for All 3 Notes Parts ---")
for idx, mic in enumerate(mic_parts, 1):
    meta = get_topic_metadata_by_id("polity", mic)
    qs = load_questions(meta["repository_id"], "chronology")
    print(f"Part {idx} ({meta['display_title']}) -> Loaded {len(qs)} chronology questions from '{meta['repository_id']}_chronology.json'")
    assert len(qs) == 25, f"Expected 25 chronology questions for {mic}, got {len(qs)}"

print("\n--- 3. Checking Question Fields & Syntax for all 25 Questions ---")
with open("data/questions/polity/making_of_indian_constitution_chronology.json", encoding="utf-8") as f:
    questions = json.load(f)

assert len(questions) == 25, "Total count is not 25"

required_fields = [
    "id", "subject", "topic", "difficulty", "question_type",
    "question", "events", "options", "correct_answer",
    "explanation", "why_not_others", "tnpsc_tip", "revision_fact",
    "source_reference", "bloom_level", "estimated_time_sec", "pyq_similarity",
    "tags", "question_en", "question_ta", "options_en", "options_ta", "answer",
    "explanation_en", "explanation_ta"
]

for idx, q in enumerate(questions, 1):
    for field in required_fields:
        assert field in q, f"Question {idx} ({q.get('id')}) missing field: {field}"
    assert len(q["options"]) == 4, f"Question {idx} does not have 4 options"
    assert q["correct_answer"] in ["A", "B", "C", "D"], f"Question {idx} invalid correct_answer"
    assert q["answer"] in ["a", "b", "c", "d"], f"Question {idx} invalid answer"

print(f"[OK] ALL 25 CHRONOLOGY QUESTIONS VALIDATED SUCCESSFULLY! Sequential IDs: {questions[0]['id']} to {questions[-1]['id']}")
