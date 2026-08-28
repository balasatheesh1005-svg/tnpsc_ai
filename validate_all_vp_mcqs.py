import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

def validate_all_vp_mcqs():
    print("================================================================================")
    print("🧪 CROSS-DATASET VALIDATION & ENGINE SIMULATION: VICE-PRESIDENT MCQs")
    print("================================================================================")

    datasets = [
        ("easy.json", "data/questions/polity/vice_president_easy.json", 50),
        ("medium.json", "data/questions/polity/vice_president_medium.json", 50),
        ("hard.json", "data/questions/polity/vice_president_hard.json", 50),
        ("statement.json", "data/questions/polity/vice_president_statement.json", 50),
        ("reasoning.json", "data/questions/polity/vice_president_reasoning.json", 25),
        ("chronology.json", "data/questions/polity/vice_president_chronology.json", 25),
        ("match.json", "data/questions/polity/vice_president_match.json", 25),
        ("grand_test.json", "data/questions/polity/vice_president_grand_test.json", 100)
    ]

    all_ids = set()
    total_q_count = 0
    all_stems = {}

    for name, path, expected_count in datasets:
        assert os.path.exists(path), f"❌ File missing: {path}"
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        assert len(data) == expected_count, f"{name}: Expected {expected_count} questions, got {len(data)}"
        print(f"  ✅ {name}: {len(data)} questions (Matches expected {expected_count})")
        
        for q in data:
            qid = q.get("id") or q.get("question_id")
            assert qid not in all_ids, f"Duplicate Question ID found: {qid}"
            all_ids.add(qid)
            
            # Check options
            opts = q.get("options", [])
            assert len(opts) == 4, f"{qid}: Expected 4 options, got {len(opts)}"
            
            corr = q.get("correct_answer")
            assert corr in ["A", "B", "C", "D"], f"{qid}: Invalid correct_answer '{corr}'"
            
            # Check why_not_others
            wno = q.get("why_not_others", {})
            assert isinstance(wno, dict) and len(wno) == 4, f"{qid}: Invalid why_not_others dict"
            for opt_key in ["A", "B", "C", "D"]:
                val = wno.get(opt_key, {})
                en_txt = val.get("en", "") if isinstance(val, dict) else str(val)
                assert len(en_txt.split()) > 3, f"{qid}: Distractor explanation too short/generic for option {opt_key}"
                
            # Check tnpsc_tip
            tip = q.get("tnpsc_tip", {})
            tip_en = tip.get("en", "") if isinstance(tip, dict) else str(tip)
            assert len(tip_en.split()) > 3, f"{qid}: TNPSC tip too short/generic"
            
            # Check stems for duplicates
            q_stem = q.get("question_en", "").strip().lower()
            if q_stem in all_stems:
                print(f"  ⚠️ Warning: Duplicate question stem between {qid} and {all_stems[q_stem]}")
            else:
                all_stems[q_stem] = qid
                
            total_q_count += 1

    print("\n--------------------------------------------------")
    print(f"Total Questions Verified: {total_q_count} / 375")
    print(f"Total Unique IDs Verified: {len(all_ids)}")
    print("SUCCESS: ALL 8 DATASETS PASSED STATIC & EXPLANATION QUALITY VALIDATION!")
    print("--------------------------------------------------")

if __name__ == "__main__":
    validate_all_vp_mcqs()
