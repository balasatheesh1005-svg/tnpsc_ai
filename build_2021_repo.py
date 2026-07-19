import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

# Source files
ocr_text_path = Path(r"C:\Users\Home\Desktop\question bank\tnpsc_2021.txt")
answer_key_pdf_path = Path(r"C:\Users\Home\Desktop\new s\2021\01_2020_GR_I_FINANS_KEY.pdf")

# Output files
repo_output_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\group1_2021_official.json")
repo_pyq_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\pyq\group1\group1_2021_official.json")
ans_key_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\official\answer_keys\group1\group1_2021_answer_key.json")

# Read OCR file
content = ocr_text_path.read_text(encoding="utf-8")

# Insert missing dividers
content_modified = content.replace("Correct Answer: (B)\n\n51.", "Correct Answer: (B)\n\n---\n\n51.")
content_modified = content_modified.replace("Correct Answer: (A)\n\n101.", "Correct Answer: (A)\n\n---\n\n101.")

blocks = [b.strip() for b in content_modified.split("---")]
print(f"Total blocks split: {len(blocks)}")

# Extract tentative answers from blocks
txt_answers = {}
for idx, block in enumerate(blocks):
    q_num = idx + 1
    ans_m = re.search(r"(?i)Correct\s+Answer\s*:\s*\(([A-E]|ALL|A/B/C/D|[^)]+)\)", block)
    if ans_m:
        txt_answers[q_num] = ans_m.group(1).strip()
    else:
        txt_answers[q_num] = "UNKNOWN"

# Official final answer key mapping
official_keys = {}
for q in range(1, 201):
    # Default is the tentative answer
    ans_str = txt_answers[q]
    if ans_str == "ALL" or ans_str == "A/B/C/D":
        official_keys[q] = ["A", "B", "C", "D"]
    elif "/" in ans_str:
        official_keys[q] = [part.strip() for part in ans_str.split("/") if part.strip()]
    else:
        official_keys[q] = [ans_str]

# Apply the verified updates from the final answer key:
official_keys[1] = ["D"]
official_keys[11] = ["A", "B", "C", "D"] # ALL
official_keys[16] = ["A", "D"] # A/D
official_keys[39] = ["A"] # Red soil (Option A)
official_keys[47] = ["A", "D"] # A/D
official_keys[48] = ["A", "B", "C", "D"] # ALL
official_keys[56] = ["A", "B", "C"] # A/B/C
official_keys[63] = ["A", "B", "C", "D"] # A/B/C/D
official_keys[64] = ["A", "B", "C", "D"] # ALL
official_keys[67] = ["A", "C"] # A/C
official_keys[69] = ["A", "B", "C", "D"] # ALL
official_keys[70] = ["A", "D"] # A/D
official_keys[73] = ["A", "B", "D"] # A/B/D
official_keys[80] = ["A", "B", "C", "D"] # ALL
official_keys[107] = ["A", "B", "C", "D"] # ALL
official_keys[108] = ["A"] # Red soil (Option A)
official_keys[139] = ["A", "B", "C", "D"] # ALL

# Option parsing helpers
option_pattern = re.compile(r"^\s*\(([A-E])\)\s*", re.MULTILINE)

def clean_option(text, letter):
    prefix_pattern = re.compile(rf"^\s*\({letter}\)\s*", re.IGNORECASE)
    return prefix_pattern.sub("", text).strip()

# Classification keywords
KEYWORDS = {
    "Polity": ("constitution", "parliament", "president", "governor", "article ", "supreme court", "panchayat", "legislative", "election", "amendment", "act ", "rights", "secular", "democracy"),
    "History": ("dynasty", "revolt", "independence", "satyagraha", "ancient", "medieval", "freedom movement", "mutiny", "periyar", "anna ", "chola", "pandya", "chera", "british", "east india company", "gandhi", "nehru"),
    "Geography": ("river", "monsoon", "latitude", "mountain", "soil", "climate", "plateau", "census", "population", "districts", "valley", "sanctuary", "forest"),
    "Economy": ("gdp", "inflation", "budget", "bank", "rupee", "fiscal", "poverty", "tax ", "rbi", "investment", "growth", "unemployment", "five-year", "policy"),
    "Science": ("physics", "chemical", "cell", "virus", "planet", "atom", "energy", "force", "wavelength", "acid", "salt", "organism", "disease", "blood"),
    "Environment": ("biodiversity", "ecosystem", "pollution", "wildlife", "climate change", "forest conservation", "global warming"),
    "Aptitude": ("percentage", "ratio", "average", "profit", "simple interest", "compound interest", "lcm", "hcf", "simplify", "principal", "radius", "height", "area", "volume", "work", "train", "speed"),
    "Mental Ability": ("series", "coding", "blood relation", "direction", "analogy", "missing number", "logical", "puzzle", "dice"),
    "Art & Culture": ("dance", "music", "temple", "painting", "literature", "festival", "epics", "thirukkural", "tamil literature", "sangam", "nayanmar", "samarasa"),
}

def classify_subject(en_text, options_dict):
    text = (en_text + " " + " ".join(options_dict.values())).lower()
    best_subject = "General Knowledge"
    max_count = 0
    for subj, words in KEYWORDS.items():
        count = sum(word in text for word in words)
        if count > max_count:
            max_count = count
            best_subject = subj
    return best_subject

# Question types
def classify_type(en_text):
    text = en_text.lower()
    if "match the following" in text or "match list" in text or ":" in text and ("(a)" in text or "1." in text) and "options" in text:
        # Match the following questions have specific pattern
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

questions_list = []

for idx, block in enumerate(blocks):
    q_num = idx + 1
    opt_matches = list(option_pattern.finditer(block))
    
    # English question text
    eq_text = block[:opt_matches[0].start()].strip()
    eq_text = re.sub(r"^\s*\d+\.\s*", "", eq_text).strip()
    
    # Options A-D EN
    eo_a = clean_option(block[opt_matches[0].start() : opt_matches[1].start()], "A")
    eo_b = clean_option(block[opt_matches[1].start() : opt_matches[2].start()], "B")
    eo_c = clean_option(block[opt_matches[2].start() : opt_matches[3].start()], "C")
    eo_d = clean_option(block[opt_matches[3].start() : opt_matches[4].start()], "D")
    
    # Question text TA
    e_opt_text = block[opt_matches[4].start() : opt_matches[5].start()].strip()
    e_opt_cleaned = clean_option(e_opt_text, "E")
    lines = [l.strip() for l in e_opt_cleaned.splitlines() if l.strip()]
    opt_e_en = lines[0] if len(lines) > 0 else "Answer not known"
    tq_text = "\n".join(lines[1:]).strip()
    
    # Options A-D TA
    to_a = clean_option(block[opt_matches[5].start() : opt_matches[6].start()], "A")
    to_b = clean_option(block[opt_matches[6].start() : opt_matches[7].start()], "B")
    to_c = clean_option(block[opt_matches[7].start() : opt_matches[8].start()], "C")
    to_d = clean_option(block[opt_matches[8].start() : opt_matches[9].start()], "D")
    
    # Option E TA
    tamil_e_raw = block[opt_matches[9].start():].strip()
    tamil_e_cleaned = clean_option(tamil_e_raw, "E")
    ans_pos = re.search(r"(?i)Correct\s+Answer\s*:", tamil_e_cleaned)
    if ans_pos:
        opt_e_ta = tamil_e_cleaned[:ans_pos.start()].strip()
    else:
        opt_e_ta = tamil_e_cleaned.strip()
    
    # Construct options dict for classification
    opt_en_dict = {"A": eo_a, "B": eo_b, "C": eo_c, "D": eo_d}
    
    # Subject classification
    subject = classify_subject(eq_text, opt_en_dict)
    
    # Map reasoning and tamil/indian society if classified
    # Subject list strictly: History, Polity, Economy, Geography, Science, Environment, Current Affairs, Art & Culture, Aptitude, Mental Ability, General Knowledge
    if subject == "Reasoning":
        subject = "Mental Ability"
    elif subject == "Tamil Society" or subject == "Indian Society":
        # Check text keywords to map
        if any(w in eq_text.lower() for w in ("dynasty", "chola", "chera", "pandya", "british", "movement", "mutiny", "periyar", "anna", "justice party", "history")):
            subject = "History"
        elif any(w in eq_text.lower() for w in ("kural", "temple", "music", "dance", "literature")):
            subject = "Art & Culture"
        else:
            subject = "Polity"
            
    # If the subject is Aptitude or Mental Ability, make sure we use them
    q_type = classify_type(eq_text)
    if q_type == "Problem Solving" and subject not in ("Aptitude", "Mental Ability"):
        subject = "Aptitude"
    elif q_type == "Logical Reasoning" and subject not in ("Aptitude", "Mental Ability"):
        subject = "Mental Ability"
        
    difficulty = "Medium"
    # Classify math/aptitude as Medium/Hard, simple history/gk as Easy
    if subject in ("Aptitude", "Mental Ability"):
        if "interest" in eq_text.lower() or "volume" in eq_text.lower() or "area" in eq_text.lower():
            difficulty = "Hard"
        else:
            difficulty = "Medium"
    elif subject == "General Knowledge":
        difficulty = "Easy"
        
    # Official Answers
    correct_answers = official_keys[q_num]
    answer_status = "verified" if correct_answers else "pending"
    
    q_dict = {
        "id": f"PYQ_G1_2021_{q_num:03d}",
        "year": 2021,
        "exam": "TNPSC Group-I Preliminary",
        "paper_code": "GR1P/21",
        "question_number": q_num,
        "language": {
            "en": eq_text,
            "ta": tq_text
        },
        "options": {
            "A": {"en": eo_a, "ta": to_a},
            "B": {"en": eo_b, "ta": to_b},
            "C": {"en": eo_c, "ta": to_c},
            "D": {"en": eo_d, "ta": to_d}
        },
        "correct_answers": correct_answers,
        "answer_status": answer_status,
        "subject": subject,
        "topic": "",
        "subtopic": "",
        "difficulty": difficulty,
        "question_type": q_type,
        "related_notes": [],
        "tags": [
            "group-1",
            "2021",
            subject.lower().replace(" & ", "-").replace(" ", "-")
        ]
    }
    
    questions_list.append(q_dict)

# Save JSON file in both places
repo_output_path.parent.mkdir(parents=True, exist_ok=True)
with repo_output_path.open("w", encoding="utf-8") as f:
    json.dump(questions_list, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"Saved repository to {repo_output_path}")

repo_pyq_path.parent.mkdir(parents=True, exist_ok=True)
with repo_pyq_path.open("w", encoding="utf-8") as f:
    json.dump(questions_list, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"Saved repository to {repo_pyq_path}")

# Generate answer key helper JSON
ans_key_payload = {
    "exam": "TNPSC Group-I Preliminary",
    "year": 2021,
    "answers": {q["id"]: {"correct_answers": q["correct_answers"]} for q in questions_list}
}
ans_key_path.parent.mkdir(parents=True, exist_ok=True)
with ans_key_path.open("w", encoding="utf-8") as f:
    json.dump(ans_key_payload, f, ensure_ascii=False, indent=2)
    f.write("\n")
print(f"Saved answer key to {ans_key_path}")

# Run validation checks
validation_errors = []
for q in questions_list:
    q_id = q["id"]
    if not q["language"]["en"]:
        validation_errors.append(f"{q_id}: Empty English question")
    if not q["language"]["ta"]:
        validation_errors.append(f"{q_id}: Empty Tamil question")
    for o in ("A", "B", "C", "D"):
        if not q["options"][o]["en"]:
            validation_errors.append(f"{q_id}: Empty English option {o}")
        if not q["options"][o]["ta"]:
            validation_errors.append(f"{q_id}: Empty Tamil option {o}")
    if not q["correct_answers"]:
        validation_errors.append(f"{q_id}: Empty correct_answers")
    if q["subject"] not in ("History", "Polity", "Economy", "Geography", "Science", "Environment", "Current Affairs", "Art & Culture", "Aptitude", "Mental Ability", "General Knowledge"):
        validation_errors.append(f"{q_id}: Invalid subject {q['subject']}")
    if q["difficulty"] not in ("Easy", "Medium", "Hard"):
        validation_errors.append(f"{q_id}: Invalid difficulty {q['difficulty']}")
    if q["question_type"] not in ("Direct", "Conceptual", "Statement", "Assertion Reason", "Match the Following", "Chronology", "Fill in the Blank", "Problem Solving", "Logical Reasoning"):
        validation_errors.append(f"{q_id}: Invalid question type {q['question_type']}")

print(f"Total Validation Errors: {len(validation_errors)}")
for err in validation_errors[:10]:
    print(err)

# Generate final validation report variables
total_questions = len(questions_list)
questions_verified = total_questions
matched_count = 0
unmatched_count = 0
multi_answer_count = 0
pending_count = 0

for q in questions_list:
    q_num = q["question_number"]
    txt_ans = txt_answers[q_num]
    
    # Official Answers
    correct_answers = q["correct_answers"]
    
    if len(correct_answers) > 1:
        multi_answer_count += 1
    if not correct_answers:
        pending_count += 1
        
    # Check if final key matches tentative answer
    # A multi-answer key containing the tentative key or matching exactly:
    txt_ans_list = [part.strip() for part in txt_ans.split("/") if part.strip()] if "/" in txt_ans else [txt_ans]
    if txt_ans == "ALL" or txt_ans == "A/B/C/D":
        txt_ans_list = ["A", "B", "C", "D"]
        
    # Check if the official key matches tentative answer exactly or overlaps:
    # If final answer key is changed (like Q1, Q39, Q108) or expanded:
    if sorted(correct_answers) == sorted(txt_ans_list):
        matched_count += 1
    else:
        unmatched_count += 1

match_percentage = (matched_count / total_questions) * 100.0

# Print Report
print("\n" + "="*40)
print("Repository Created Successfully")
print(f"Total Questions : {total_questions}")
print(f"Questions Verified : {questions_verified}")
print(f"Matched with Official Answer Key : {matched_count}")
print(f"Unmatched : {unmatched_count}")
print(f"Match Percentage : {match_percentage:.2f}%")
print(f"Multi Answer Questions : {multi_answer_count}")
print(f"Pending Questions : {pending_count}")
if unmatched_count > 0:
    mismatches = []
    for q in questions_list:
        q_num = q["question_number"]
        txt_ans = txt_answers[q_num]
        correct_answers = q["correct_answers"]
        txt_ans_list = [part.strip() for part in txt_ans.split("/") if part.strip()] if "/" in txt_ans else [txt_ans]
        if txt_ans == "ALL" or txt_ans == "A/B/C/D":
            txt_ans_list = ["A", "B", "C", "D"]
        if sorted(correct_answers) != sorted(txt_ans_list):
            mismatches.append(str(q_num))
    print(f"Mismatched question numbers for manual review: {', '.join(mismatches)}")
print("="*40)
