import json
import re
import sys
from pathlib import Path

# Add project root to sys.path so we can import modules
ROOT = Path("c:/Users/Home/Desktop/tnpsc_ai")
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

sys.stdout.reconfigure(encoding='utf-8')

from tools.import_pipeline_v2 import subject_classifier, topic_classifier, difficulty_classifier
from core.question_engine.validators import validate_questions

# Raw official answer keys
official_keys = {
    1: "C", 2: "A", 3: "B", 4: "B", 5: "ALL", 6: "D", 7: "D", 8: "B", 9: "D", 10: "C",
    11: "B", 12: "B", 13: "ALL", 14: "C", 15: "B", 16: "D", 17: "C", 18: "B", 19: "C", 20: "C",
    21: "C", 22: "D", 23: "A", 24: "B", 25: "B", 26: "A", 27: "B", 28: "C", 29: "ALL", 30: "B",
    31: "B", 32: "B", 33: "A", 34: "D", 35: "C", 36: "A", 37: "A", 38: "A", 39: "C", 40: "D",
    41: "C", 42: "B", 43: "A", 44: "C", 45: "A", 46: "D", 47: "A", 48: "B", 49: "C", 50: "B",
    51: "B/D", 52: "A/B/C/D", 53: "C", 54: "C", 55: "A", 56: "C", 57: "B", 58: "A", 59: "C", 60: "A",
    61: "A", 62: "A", 63: "C", 64: "B", 65: "B", 66: "C", 67: "C", 68: "C", 69: "B/C", 70: "B",
    71: "D", 72: "B", 73: "C", 74: "ALL", 75: "A", 76: "C", 77: "C", 78: "D", 79: "C", 80: "C",
    81: "B", 82: "C", 83: "C", 84: "B", 85: "B", 86: "A", 87: "B", 88: "A", 89: "C", 90: "D",
    91: "C", 92: "ALL", 93: "A", 94: "C", 95: "B", 96: "C", 97: "B", 98: "C", 99: "B", 100: "D",
    101: "D", 102: "D", 103: "D", 104: "B", 105: "A", 106: "C", 107: "D", 108: "B", 109: "B", 110: "C",
    111: "B", 112: "A", 113: "ALL", 114: "B", 115: "A", 116: "B", 117: "A", 118: "C", 119: "B", 120: "D",
    121: "C", 122: "C", 123: "B", 124: "A", 125: "C", 126: "C", 127: "C", 128: "D", 129: "B", 130: "A",
    131: "D", 132: "B", 133: "D", 134: "D", 135: "B", 136: "C", 137: "A", 138: "D", 139: "D", 140: "C",
    141: "B", 142: "B", 143: "B", 144: "A", 145: "D", 146: "B", 147: "A", 148: "A", 149: "C", 150: "B",
    151: "C", 152: "A/C", 153: "C", 154: "C", 155: "C", 156: "A", 157: "ALL", 158: "ALL", 159: "A", 160: "D",
    161: "C", 162: "C", 163: "B", 164: "C", 165: "D", 166: "C", 167: "B", 168: "C", 169: "D", 170: "D",
    171: "C", 172: "C", 173: "D", 174: "C", 175: "C", 176: "A", 177: "C", 178: "A", 179: "A", 180: "A",
    181: "B", 182: "A", 183: "ALL", 184: "B", 185: "ALL", 186: "A", 187: "D", 188: "B", 189: "D", 190: "C",
    191: "B", 192: "B", 193: "B", 194: "B", 195: "B", 196: "A", 197: "B/C", 198: "B", 199: "D", 200: "C"
}

def convert_key(key_str):
    key_str = key_str.strip().upper()
    if key_str == "ALL" or key_str == "A/B/C/D":
        return ["A", "B", "C", "D"]
    if "/" in key_str:
        return [part.strip() for part in key_str.split("/") if part.strip()]
    return [key_str]

# Read OCR file
file_path = Path("C:/Users/Home/Desktop/tnpsc_2022_q1_25.txt")
content = file_path.read_text(encoding="utf-8")

# Split blocks
pattern = re.compile(r"(?i)Correct\s+Answer\s*:\s*\([A-E]\)")
matches = list(pattern.finditer(content))

blocks = []
last_end = 0
for match in matches:
    end = match.end()
    blocks.append(content[last_end:end].strip())
    last_end = end

option_pattern = re.compile(r"^\s*\(([A-E])\)\s*", re.MULTILINE)

def clean_option(text, letter):
    prefix_pattern = re.compile(rf"^\s*\({letter}\)\s*", re.IGNORECASE)
    return prefix_pattern.sub("", text).strip()

questions_list = []
answer_key_list = []

for idx, block in enumerate(blocks):
    q_num = idx + 1
    opt_matches = list(option_pattern.finditer(block))
    
    # Question text EN
    eq_text = block[:opt_matches[0].start()].strip()
    eq_text = re.sub(r"^(?:\-\-\-\s*)?\d+\.\s*", "", eq_text).strip()
    
    # Options A-D EN
    eo_a = clean_option(block[opt_matches[0].start() : opt_matches[1].start()], "A")
    eo_b = clean_option(block[opt_matches[1].start() : opt_matches[2].start()], "B")
    eo_c = clean_option(block[opt_matches[2].start() : opt_matches[3].start()], "C")
    eo_d = clean_option(block[opt_matches[3].start() : opt_matches[4].start()], "D")
    
    # Question text TA
    e_opt_text = block[opt_matches[4].start() : opt_matches[5].start()].strip()
    e_opt_cleaned = clean_option(e_opt_text, "E")
    lines = e_opt_cleaned.splitlines()
    tq_text = "\n".join(lines[1:]).strip()
    
    # Options A-D TA
    to_a = clean_option(block[opt_matches[5].start() : opt_matches[6].start()], "A")
    to_b = clean_option(block[opt_matches[6].start() : opt_matches[7].start()], "B")
    to_c = clean_option(block[opt_matches[7].start() : opt_matches[8].start()], "C")
    to_d = clean_option(block[opt_matches[8].start() : opt_matches[9].start()], "D")
    
    # Official Answers
    ans_key_raw = official_keys[q_num]
    correct_answers = convert_key(ans_key_raw)
    correct_answer = correct_answers[0]
    
    # Create question dict structure
    q_dict = {
        "id": f"PYQ_G1_2022_{q_num:03d}",
        "exam": "Group 1",
        "year": 2022,
        "question_en": eq_text,
        "question_ta": tq_text,
        "options": {
            "A": f"{eo_a} / {to_a}",
            "B": f"{eo_b} / {to_b}",
            "C": f"{eo_c} / {to_c}",
            "D": f"{eo_d} / {to_d}"
        },
        "correct_answers": correct_answers,
        "correct_answer": correct_answer,
        "explanation": {"en": "", "ta": ""},
        "related_note": "",
        "tags": ["group-1", "2022"],
        "repeat_years": [],
        "ai_trick": "",
        "source": "Official TNPSC Group-I 2022 Question Paper",
        "source_page": None,
        "question_number": q_num
    }
    
    # Run classifiers
    subject = subject_classifier.classify(q_dict)
    topic = topic_classifier.classify(q_dict)
    difficulty = difficulty_classifier.classify(q_dict)
    
    q_dict["subject"] = subject
    q_dict["topic"] = topic
    q_dict["difficulty"] = difficulty
    q_dict["tags"].append(subject.lower().replace(" & ", "-").replace(" ", "-"))
    
    questions_list.append(q_dict)
    
    # Collect answer key record
    answer_key_list.append({
        "id": q_dict["id"],
        "correct_answers": correct_answers
    })

# Validate the generated questions
validation_result = validate_questions(questions_list)
print(f"Validation Valid: {validation_result.valid}")
print(f"Validation Errors Count: {len(validation_result.errors)}")
for error in validation_result.errors[:10]:
    print(error)

# Save files if valid
if validation_result.valid:
    repo_file = ROOT / "data" / "pyq" / "group1" / "group1_2022_official.json"
    repo_file.parent.mkdir(parents=True, exist_ok=True)
    with repo_file.open("w", encoding="utf-8") as f:
        json.dump(questions_list, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Successfully saved repository file: {repo_file}")
    
    ans_file = ROOT / "data" / "official" / "answer_keys" / "group1" / "group1_2022_answer_key.json"
    ans_file.parent.mkdir(parents=True, exist_ok=True)
    with ans_file.open("w", encoding="utf-8") as f:
        # Wrap answers map
        ans_payload = {
            "exam": "Group 1",
            "year": 2022,
            "answers": {item["id"]: {"correct_answers": item["correct_answers"]} for item in answer_key_list}
        }
        json.dump(ans_payload, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Successfully saved answer key file: {ans_file}")
else:
    print("SAVING SKIPPED DUE TO VALIDATION ERRORS.")
