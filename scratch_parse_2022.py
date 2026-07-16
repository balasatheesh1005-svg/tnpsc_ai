import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

file_path = Path("C:/Users/Home/Desktop/tnpsc_2022_q1_25.txt")
content = file_path.read_text(encoding="utf-8")

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

def parse_block(block, q_num):
    opt_matches = list(option_pattern.finditer(block))
    eq_text = block[:opt_matches[0].start()].strip()
    eq_text = re.sub(r"^(?:\-\-\-\s*)?\d+\.\s*", "", eq_text).strip()
    
    eo_a = clean_option(block[opt_matches[0].start() : opt_matches[1].start()], "A")
    eo_b = clean_option(block[opt_matches[1].start() : opt_matches[2].start()], "B")
    eo_c = clean_option(block[opt_matches[2].start() : opt_matches[3].start()], "C")
    eo_d = clean_option(block[opt_matches[3].start() : opt_matches[4].start()], "D")
    
    e_opt_text = block[opt_matches[4].start() : opt_matches[5].start()].strip()
    e_opt_cleaned = clean_option(e_opt_text, "E")
    lines = e_opt_cleaned.splitlines()
    tq_text = "\n".join(lines[1:]).strip()
    
    to_a = clean_option(block[opt_matches[5].start() : opt_matches[6].start()], "A")
    to_b = clean_option(block[opt_matches[6].start() : opt_matches[7].start()], "B")
    to_c = clean_option(block[opt_matches[7].start() : opt_matches[8].start()], "C")
    to_d = clean_option(block[opt_matches[8].start() : opt_matches[9].start()], "D")
    
    return {
        "q_num": q_num,
        "question_en": eq_text,
        "question_ta": tq_text,
        "options_en": {"A": eo_a, "B": eo_b, "C": eo_c, "D": eo_d},
        "options_ta": {"A": to_a, "B": to_b, "C": to_c, "D": to_d}
    }

parsed_questions = []
for idx, block in enumerate(blocks):
    parsed = parse_block(block, idx + 1)
    parsed_questions.append(parsed)

# Integrity checks
failures = []
for q in parsed_questions:
    if not q["question_en"]:
        failures.append(f"Q{q['q_num']}: Empty question_en")
    if not q["question_ta"]:
        failures.append(f"Q{q['q_num']}: Empty question_ta")
    for letter in ["A", "B", "C", "D"]:
        if not q["options_en"][letter]:
            failures.append(f"Q{q['q_num']}: Empty English option {letter}")
        if not q["options_ta"][letter]:
            failures.append(f"Q{q['q_num']}: Empty Tamil option {letter}")

print(f"Total validation failures: {len(failures)}")
for failure in failures[:10]:
    print(failure)
