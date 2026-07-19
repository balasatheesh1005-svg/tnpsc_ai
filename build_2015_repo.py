import json
import re
import sys
from pathlib import Path

# Add project root to sys.path
ROOT = Path(r"c:\Users\Home\Desktop\tnpsc_ai")
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

sys.stdout.reconfigure(encoding='utf-8')

from tools.import_pipeline_v2 import subject_classifier, topic_classifier, difficulty_classifier
from core.question_engine.validators import validate_questions

# Paths
txt_path = Path(r"C:\Users\Home\.gemini\antigravity\scratch\tnpsc_2015_q1_100.txt")
md_path = Path(r"C:\Users\Home\.gemini\antigravity\scratch\tnpsc_2015_answer_key_comparison.md")

# Outputs
repo_output_root = ROOT / "group1_2015_official.json"
repo_output_pyq = ROOT / "data" / "pyq" / "group1" / "group1_2015_official.json"
ans_key_output = ROOT / "data" / "official" / "answer_keys" / "group1" / "group1_2015_answer_key.json"

def clean_option(text, letter):
    prefix_pattern = re.compile(rf"^\s*\({letter}\)\s*", re.IGNORECASE)
    return prefix_pattern.sub("", text).strip()

def classify_type(en_text):
    text = en_text.lower()
    if "match the following" in text or "match list" in text or ":" in text and ("(a)" in text or "1." in text) and "options" in text:
        if "match" in text or "porutha" in text:
            return "Match the Following"
    if "chronology" in text or "chronological" in text or "arrange the following events in order" in text:
        return "Chronology"
    if "assertion" in text or "reason" in text or "assertion (a)" in text:
        return "Assertion Reason"
    if "statement 1" in text or "statement i" in text or "which of the statements" in text or "correct statements" in text:
        return "Statement"
    if "fill in the blank" in text or "____" in text:
        return "Fill in the Blank"
    if any(k in text for k in ("lcm", "hcf", "simplify", "interest", "find the", "evaluate", "solve", "ratio", "average", "percentage")):
        return "Problem Solving"
    if "missing number" in text or "series" in text:
        return "Logical Reasoning"
    if "concept" in text or "define" in text or "meaning" in text:
        return "Conceptual"
    return "Direct"

# Read inputs
print("Reading inputs...")
content = txt_path.read_text(encoding="utf-8")
blocks = [b.strip() for b in content.split("---") if b.strip()]

md_content = md_path.read_text(encoding="utf-8")

# Parse official answer keys
official_keys = {}
for line in md_content.splitlines():
    if not line.strip() or "|" not in line or "Q.No" in line or "---" in line:
        continue
    parts = [p.strip() for p in line.split("|") if p.strip()]
    if len(parts) >= 2:
        try:
            q_num = int(parts[0])
            key_str = parts[1]
            official_keys[q_num] = key_str
        except ValueError:
            pass

def convert_key(key_str):
    key_str = key_str.strip().upper()
    if key_str == "ALL" or key_str == "A/B/C/D":
        return ["A", "B", "C", "D"]
    if "/" in key_str:
        return [part.strip() for part in key_str.split("/") if part.strip()]
    return [key_str]

option_pattern = re.compile(r"^\s*\(([A-D])\)\s*", re.MULTILINE)

questions_list = []
answer_key_list = []

for idx, block in enumerate(blocks):
    q_num = idx + 1
    opt_matches = list(option_pattern.finditer(block))
    
    # English question text
    eq_text = block[:opt_matches[0].start()].strip()
    eq_text = re.sub(r"^\s*\d+\.\s*", "", eq_text).strip()
    
    # English options A, B, C
    eo_a = clean_option(block[opt_matches[0].start() : opt_matches[1].start()], "A")
    eo_b = clean_option(block[opt_matches[1].start() : opt_matches[2].start()], "B")
    eo_c = clean_option(block[opt_matches[2].start() : opt_matches[3].start()], "C")
    
    # Separation of English Option D and Tamil Question
    rest_en_d_ta_q = block[opt_matches[3].end() : opt_matches[4].start()].strip()
    parts = re.split(r'\n\s*\n', rest_en_d_ta_q, maxsplit=1)
    eo_d = parts[0].strip()
    tq_text = parts[1].strip() if len(parts) > 1 else ""
    
    # Tamil options A, B, C
    to_a = clean_option(block[opt_matches[4].start() : opt_matches[5].start()], "A")
    to_b = clean_option(block[opt_matches[5].start() : opt_matches[6].start()], "B")
    to_c = clean_option(block[opt_matches[6].start() : opt_matches[7].start()], "C")
    
    # Tamil Option D
    d_part = block[opt_matches[7].start():].strip()
    ans_match = re.search(r"(?i)Correct\s+Answer\s*:", d_part)
    to_d = clean_option(d_part[:ans_match.start()], "D") if ans_match else clean_option(d_part, "D")
    
    # Get official answer
    ans_raw = official_keys[q_num]
    correct_answers = convert_key(ans_raw)
    
    # Initial question structure for classification
    q_dict = {
        "id": f"PYQ_G1_2015_{q_num:03d}",
        "year": 2015,
        "exam": "TNPSC Group-I Preliminary",
        "paper_code": "GR1P/15",
        "question_number": q_num,
        "question_en": eq_text,
        "question_ta": tq_text,
        "options": {
            "A": f"{eo_a}\n{to_a}",
            "B": f"{eo_b}\n{to_b}",
            "C": f"{eo_c}\n{to_c}",
            "D": f"{eo_d}\n{to_d}"
        },
        "correct_answers": correct_answers,
        "answer_status": "verified",
        "subject": "",
        "topic": "",
        "subtopic": "",
        "difficulty": "",
        "question_type": classify_type(eq_text),
        "related_notes": [],
        "tags": ["group-1", "2015"]
    }
    
    # Run classifiers
    subject = subject_classifier.classify(q_dict)
    topic = topic_classifier.classify(q_dict)
    difficulty = difficulty_classifier.classify(q_dict)
    
    q_dict["subject"] = subject
    q_dict["topic"] = topic
    q_dict["difficulty"] = difficulty
    
    # Add subject tag
    subj_tag = subject.lower().replace(" & ", "-").replace(" ", "-")
    q_dict["tags"].append(subj_tag)
    
    questions_list.append(q_dict)
    answer_key_list.append({
        "id": q_dict["id"],
        "correct_answers": correct_answers
    })

# Validate
print(f"Validating {len(questions_list)} questions...")
validation_result = validate_questions(questions_list)

print(f"Validation result: Valid={validation_result.valid}")
if not validation_result.valid:
    print("Errors:")
    for err in validation_result.errors:
        print("  -", err)
    print("Warnings:")
    for warn in validation_result.warnings:
        print("  -", warn)
    sys.exit(1)

# Write output files
print("Saving output files...")
for out_path in (repo_output_root, repo_output_pyq):
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf-8") as f:
        json.dump(questions_list, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Saved: {out_path}")

# Write answer key file
ans_key_output.parent.mkdir(parents=True, exist_ok=True)
with ans_key_output.open("w", encoding="utf-8") as f:
    ans_payload = {
        "exam": "TNPSC Group-I Preliminary",
        "year": 2015,
        "answers": {item["id"]: {"correct_answers": item["correct_answers"]} for item in answer_key_list}
    }
    json.dump(ans_payload, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"Saved: {ans_key_output}")

print("Done! All files built and validated successfully.")
