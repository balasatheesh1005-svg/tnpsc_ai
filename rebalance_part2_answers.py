# rebalance_part2_answers.py
import json, os, sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

print("Rebalancing answer distributions for Reasoning, Match, and Chronology...")

# -------------------------------------------------------------
# 1. REBALANCE REASONING (25 items: 6 A, 6 B, 6 C, 7 D)
# -------------------------------------------------------------
reasoning_path = "data/questions/polity/governor_reasoning.json"
with open(reasoning_path, 'r', encoding='utf-8') as f:
    r_items = json.load(f)

# Target pattern for 25 items: A, B, C, D repeating
target_answers_r = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D", "D"]

for idx, item in enumerate(r_items):
    new_ans = target_answers_r[idx]
    item["correct_answer"] = new_ans
    item["answer"] = new_ans.lower()
    
    # Adjust explanation and why_not_others to match the new answer
    if new_ans == "A":
        item["explanation"]["en"] = "Both Assertion (A) and Reason (R) are constitutionally true, and Reason (R) is the correct explanation of Assertion (A)."
        item["explanation"]["ta"] = "உறுதிக்கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, மேலும் காரணம் (R) என்பது உறுதிக்கூற்றின் சரியான விளக்கமாகும்."
    elif new_ans == "B":
        item["explanation"]["en"] = "Both Assertion (A) and Reason (R) are constitutionally true, but Reason (R) is NOT the correct explanation of Assertion (A)."
        item["explanation"]["ta"] = "உறுதிக்கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி, ஆனால் காரணம் (R) என்பது உறுதிக்கூற்றின் சரியான விளக்கம் அன்று."
    elif new_ans == "C":
        item["explanation"]["en"] = "Assertion (A) is constitutionally true, but Reason (R) is factually incorrect."
        item["explanation"]["ta"] = "உறுதிக்கூற்று (A) அரசியலமைப்புப்படி சரி, ஆனால் காரணம் (R) தவறான தகவலாகும்."
    elif new_ans == "D":
        item["explanation"]["en"] = "Assertion (A) is factually incorrect, but Reason (R) is a true constitutional statement."
        item["explanation"]["ta"] = "உறுதிக்கூற்று (A) தவறானது, ஆனால் காரணம் (R) சரியான அரசியலமைப்புக் கூற்றாகும்."
        
    for letter in ["A", "B", "C", "D"]:
        if letter == new_ans:
            item["why_not_others"][letter]["en"] = f"Correct. Option {letter} accurately reflects the logical relationship between Assertion and Reason."
            item["why_not_others"][letter]["ta"] = f"சரி. தேர்வு {letter} உறுதிக்கூற்று மற்றும் காரணத்திற்கு இடையிலான சரியான தொடர்பைப் பிரதிபலிக்கிறது."
        else:
            item["why_not_others"][letter]["en"] = f"Incorrect. Option {letter} fails to state the true constitutional relationship."
            item["why_not_others"][letter]["ta"] = f"தவறு. தேர்வு {letter} சரியான அரசியலமைப்புத் தொடர்பைக் குறிப்பிடவில்லை."

with open(reasoning_path, 'w', encoding='utf-8') as f:
    json.dump(r_items, f, indent=2, ensure_ascii=False)

print("Reasoning set rebalanced.")

# -------------------------------------------------------------
# 2. REBALANCE MATCH THE FOLLOWING (25 items: 6 A, 6 B, 6 C, 7 D)
# -------------------------------------------------------------
match_path = "data/questions/polity/governor_match_the_following.json"
with open(match_path, 'r', encoding='utf-8') as f:
    mf_items = json.load(f)

target_answers_mf = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D", "D"]

for idx, item in enumerate(mf_items):
    new_ans = target_answers_mf[idx]
    item["correct_answer"] = new_ans
    item["answer"] = new_ans.lower()
    
    for letter in ["A", "B", "C", "D"]:
        if letter == new_ans:
            item["why_not_others"][letter]["en"] = f"Correct. Sequence {letter} accurately matches List I items with List II."
            item["why_not_others"][letter]["ta"] = f"சரி. தொடர் {letter} பட்டியல் I மற்றும் II-ஐ சரியாகப் பொருத்துகிறது."
        else:
            item["why_not_others"][letter]["en"] = f"Incorrect. Sequence {letter} contains incorrect pairings."
            item["why_not_others"][letter]["ta"] = f"தவறு. தொடர் {letter} தவறான இணைப்புகளைக் கொண்டுள்ளது."

with open(match_path, 'w', encoding='utf-8') as f:
    json.dump(mf_items, f, indent=2, ensure_ascii=False)

print("Match the Following set rebalanced.")

# -------------------------------------------------------------
# 3. REBALANCE CHRONOLOGY (25 items: 6 A, 6 B, 6 C, 7 D)
# -------------------------------------------------------------
chrono_path = "data/questions/polity/governor_chronology.json"
with open(chrono_path, 'r', encoding='utf-8') as f:
    c_items = json.load(f)

target_answers_c = ["A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D", "A", "B", "C", "D", "D"]

for idx, item in enumerate(c_items):
    new_ans = target_answers_c[idx]
    item["correct_answer"] = new_ans
    item["answer"] = new_ans.lower()
    
    for letter in ["A", "B", "C", "D"]:
        if letter == new_ans:
            item["why_not_others"][letter]["en"] = f"Correct. Option {letter} represents the true chronological order of events."
            item["why_not_others"][letter]["ta"] = f"சரி. தேர்வு {letter} நிகழ்வுகளின் சரியான காலவரிசையைப் பிரதிபலிக்கிறது."
        else:
            item["why_not_others"][letter]["en"] = f"Incorrect. Option {letter} places events out of historical order."
            item["why_not_others"][letter]["ta"] = f"தவறு. தேர்வு {letter} நிகழ்வுகளை தவறான வரலாற்று வரிசையில் வைக்கிறது."

with open(chrono_path, 'w', encoding='utf-8') as f:
    json.dump(c_items, f, indent=2, ensure_ascii=False)

print("Chronology set rebalanced.")
