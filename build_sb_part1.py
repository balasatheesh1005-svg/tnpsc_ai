import json
import sys
from pathlib import Path

target_path = Path(r"c:\Users\Home\Desktop\tnpsc_ai\data\questions\polity\historical_background_statement_based.json")

def make_q(q_id, q_type, q_en, q_ta, opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta,
           correct_ans, exp_en, exp_ta, wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta,
           tip_en, tip_ta, rev_en, rev_ta, bloom, est_time, tags):
    opts = [
        {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
        {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
        {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
        {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
    ]
    opts_en = [opt_a_en, opt_b_en, opt_c_en, opt_d_en]
    opts_ta = [opt_a_ta, opt_b_ta, opt_c_ta, opt_d_ta]
    
    return {
        "id": q_id,
        "subject": "Polity",
        "topic": "Historical Background",
        "difficulty": "Hard",
        "question_type": "Statement Based",
        "question": {"en": q_en, "ta": q_ta},
        "options": opts,
        "correct_answer": correct_ans,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": {
            "A": {"en": wno_a_en, "ta": wno_a_ta},
            "B": {"en": wno_b_en, "ta": wno_b_ta},
            "C": {"en": wno_c_en, "ta": wno_c_ta},
            "D": {"en": wno_d_en, "ta": wno_d_ta}
        },
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": ["M. Laxmikanth - Indian Polity", "NCERT", "Samacheer Kalvi"],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": "High",
        "tags": tags,
        "question_en": q_en,
        "question_ta": q_ta,
        "options_en": opts_en,
        "options_ta": opts_ta,
        "answer": correct_ans.lower(),
        "explanation_en": exp_en,
        "explanation_ta": exp_ta
    }

questions = []

# HB_SB_001 to HB_SB_010 already defined, let's load or define Q11-Q15 in Part 1 script:

# HB_SB_011
questions.append(make_q(
    "HB_SB_011", "Statement Based",
    "Consider the following statements regarding the Government of India Act of 1919:\n1. It introduced Dyarchy in the provinces by dividing provincial subjects into Reserved and Transferred.\n2. It introduced Bicameralism at the Centre consisting of a Council of State and a Legislative Assembly.\nWhich of the statements given above is/are correct?",
    "1919 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது மாகாணத் துறைகளை ஒதுக்கப்பட்டவை மற்றும் மாற்றப்பட்டவை எனப் பிரித்து மாகாணங்களில் இரட்டை ஆட்சியை அறிமுகப்படுத்தியது.\n2. இது மாநிலங்களவை (Council of State) மற்றும் சட்டமன்றப் பேரவை (Legislative Assembly) கொண்ட ஈரவை முறையை மத்தியில் அறிமுகப்படுத்தியது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. GOI Act 1919 (Montagu-Chelmsford Reforms) introduced Dyarchy in 8 provinces and established bicameral central legislature (Council of State and Legislative Assembly).",
    "இரண்டு கூற்றுகளும் சரியானவை. 1919 சட்டம் மாகாணங்களில் இரட்டை ஆட்சியையும் மத்தியில் ஈரவை முறையையும் (மாநிலங்களவை, சட்டமன்ற பேரவை) கொண்டு வந்தது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are historically true.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் உண்மை.",
    "Incorrect. Both statements are correct.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "GOI Act 1919 separated Provincial Budgets from the Central Budget for the first time.",
    "1919 சட்டம் முதன்முறையாக மாகாண வரவு செலவுத் திட்டத்தை மத்திய வரவு செலவுத் திட்டத்திலிருந்து பிரித்தது.",
    "Central Public Service Commission was set up in 1926 under provisions of the 1919 Act.",
    "1919 சட்ட விதிகளின்படி 1926 இல் மத்திய பொதுச் சேவை ஆணையம் அமைக்கப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1919", "Two Statement"]
))

# HB_SB_012
questions.append(make_q(
    "HB_SB_012", "Statement Based",
    "Consider the following statements regarding the Government of India Act of 1935:\n1. It provided for the establishment of an All-India Federation consisting of Provinces and Princely States as units.\n2. It abolished Dyarchy in the provinces and introduced Provincial Autonomy in its place.\nWhich of the statements given above is/are correct?",
    "1935 ஆம் ஆண்டின் இந்திய அரசுச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது மாகாணங்கள் மற்றும் சுதேச சமஸ்தானங்களை அலகுகளாகக் கொண்ட அகில இந்திய கூட்டாட்சியை நிறுவ வழிவகை செய்தது.\n2. இது மாகாணங்களில் இரட்டை ஆட்சியை ஒழித்து அதற்குப் பதிலாக மாகாண தன்னாட்சியை அறிமுகப்படுத்தியது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. GOI Act 1935 proposed All-India Federation (which never materialized) and replaced Provincial Dyarchy with Provincial Autonomy (operationalized in 1937).",
    "இரண்டு கூற்றுகளும் சரியானவை. 1935 சட்டம் அகில இந்திய கூட்டாட்சியை உத்தேசித்ததுடன் மாகாண இரட்டை ஆட்சியை ஒழித்து மாகாண தன்னாட்சியை கொண்டு வந்தது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are historically true.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் உண்மை.",
    "Incorrect. Both statements are correct.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "The All-India Federation proposed in 1935 Act never came into being because Princely States refused to join.",
    "சுதேச சமஸ்தானங்கள் இணைய மறுத்ததால் 1935 சட்டத்தில் உத்தேசிக்கப்பட்ட கூட்டாட்சி அமையவே இல்லை.",
    "Federal Court established under 1935 Act began functioning in 1937.",
    "1935 சட்டத்தில் அமைக்கப்பட்ட கூட்டாட்சி நீதிமன்றம் 1937 இல் செயல்படத் தொடங்கியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1935", "Two Statement"]
))

# HB_SB_013
questions.append(make_q(
    "HB_SB_013", "Statement Based",
    "Consider the following statements regarding the Indian Independence Act of 1947:\n1. It declared India as an independent and sovereign state from August 15, 1947.\n2. It abolished the office of Viceroy and provided for a Governor-General for each dominion appointed by the British King on the advice of the dominion cabinet.\nWhich of the statements given above is/are correct?",
    "1947 ஆம் ஆண்டின் இந்திய சுதந்திரச் சட்டம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இது ஆகஸ்ட் 15, 1947 முதல் இந்தியாவை ஒரு சுதந்திர மற்றும் இறையாண்மை கொண்ட நாடாக அறிவித்தது.\n2. இது வைஸ்ராய் பதவியை ஒழித்து, டொமினியன் அமைச்சரவையின் ஆலோசனையின் பேரில் பிரிட்டிஷ் மன்னரால் நியமிக்கப்படும் கவர்னர் ஜெனரல் பதவியை ஒவ்வொரு டொமினியனுக்கும் வழங்கியது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. Indian Independence Act 1947 ended British rule on August 15, 1947, abolished Viceroy office, and designated Governor-General as constitutional head appointed on cabinet advice.",
    "இரண்டு கூற்றுகளும் சரியானவை. 1947 சுதந்திரச் சட்டம் ஆகஸ்ட் 15, 1947 இல் பிரிட்டிஷ் ஆட்சியை முடித்து வைஸ்ராய் பதவியை ஒழித்தது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are historically true.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் உண்மை.",
    "Incorrect. Both statements are correct.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "Indian Independence Act 1947 abolished the office of Secretary of State for India and transferred functions to Secretary of State for Commonwealth Affairs.",
    "1947 சுதந்திரச் சட்டம் இந்திய அரசுச் செயலாளர் பதவியை ஒழித்து காமன்வெல்த் விவகாரச் செயலாளரிடம் பொறுப்புகளை மாற்றியது.",
    "Lord Mountbatten became the first Governor-General of independent Dominion of India.",
    "மவுண்ட்பேட்டன் பிரபு சுதந்திர இந்திய டொமினியனின் முதல் கவர்னர் ஜெனரலானார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Independence Act 1947", "Two Statement"]
))

# HB_SB_014
questions.append(make_q(
    "HB_SB_014", "Statement Based",
    "Consider the following statements regarding the constitutional transition from Company Rule (1773-1858) to Crown Rule (1858-1947):\n1. Company Rule was characterized by administrative regulation through 20-year Charter Acts.\n2. Crown Rule replaced Charter Acts with Government of India Acts and Indian Councils Acts passed directly by British Parliament.\nWhich of the statements given above is/are correct?",
    "கம்பெனி ஆட்சியிலிருந்து (1773-1858) முடிஅரசு ஆட்சிக்கு (1858-1947) ஏற்பட்ட அரசியலமைப்பு மாற்றம் பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. கம்பெனி ஆட்சி 20 ஆண்டு சாசனச் சட்டங்கள் மூலம் நிர்வாக ஒழுங்குமுறையால் வகைப்படுத்தப்பட்டது.\n2. முடிஅரசு ஆட்சி சாசனச் சட்டங்களுக்குப் பதிலாக பிரிட்டிஷ் பாராளுமன்றத்தால் நேரடியாக நிறைவேற்றப்பட்ட இந்திய அரசுச் சட்டங்கள் மற்றும் கவுன்சில்கள் சட்டங்களைக் கொண்டு வந்தது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. 1793-1853 were 20-year Charters renewing EIC powers, whereas post-1858 enactments were direct Parliamentary Acts for Crown governance.",
    "இரண்டு கூற்றுகளும் சரியானவை. 1793-1853 சாசனச் சட்டங்கள் கம்பெனி அதிகாரத்தைப் புதுப்பித்தன; 1858க்குப் பிந்தைய சட்டங்கள் நேரடி பிரிட்டிஷ் அரசுச் சட்டங்களாகும்.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 accurately synthesize the structural distinction.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் கட்டமைப்பு வேறுபாட்டைச் சரியாக விவரிக்கின்றன.",
    "Incorrect. Both statements are correct.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "Charter Acts were enacted in 1793, 1813, 1833, and 1853 at 20-year intervals.",
    "சாசனச் சட்டங்கள் 1793, 1813, 1833, மற்றும் 1853 ஆகிய ஆண்டுகளில் 20 ஆண்டு இடைவெளியில் இயற்றப்பட்டன.",
    "Government of India Act 1858 marked the formal boundary line between Company Rule and Crown Rule.",
    "1858 இந்திய அரசுச் சட்டம் கம்பெனி ஆட்சிக்கும் முடிஅரசு ஆட்சிக்கும் இடையிலான அதிகாரப்பூர்வ எல்லைக்கடவையாக அமைந்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Company Rule vs Crown Rule", "Two Statement"]
))

# HB_SB_015
questions.append(make_q(
    "HB_SB_015", "Statement Based",
    "Consider the following statements regarding the Constituent Assembly background:\n1. The Constituent Assembly of India was constituted in November 1946 under the scheme formulated by the Cabinet Mission Plan.\n2. Under the Indian Independence Act 1947, the Constituent Assembly was made a fully sovereign body and performed dual functions as a constitution-making body and ordinary legislature.\nWhich of the statements given above is/are correct?",
    "அரசியலமைப்பு சபையின் பின்னணி பற்றிய பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்திய அரசியலமைப்பு சபை நவம்பர் 1946 இல் கேபினட் மிஷன் திட்டத்தால் உருவாக்கப்பட்ட திட்டத்தின் கீழ் அமைக்கப்பட்டது.\n2. 1947 இந்திய சுதந்திரச் சட்டத்தின் கீழ், அரசியலமைப்பு சபை முழு இறையாண்மை கொண்ட அமைப்பாக மாற்றப்பட்டு அரசியலமைப்பு உருவாக்கம் மற்றும் சாதாரண சட்டமன்றம் ஆகிய இரு பணிகளைச் செய்தது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. Constituent Assembly was formed in Nov 1946 per Cabinet Mission Plan and gained total sovereignty under 1947 Independence Act, performing dual constituent and legislative roles.",
    "இரண்டு கூற்றுகளும் சரியானவை. அரசியலமைப்பு சபை நவம்பர் 1946 இல் கேபினட் மிஷன் திட்டப்படி அமைந்ததுடன் 1947 சட்டப்படி முழு இறையாண்மை பெற்று இரு பணிகளைச் செய்தது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are historically true.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் உண்மை.",
    "Incorrect. Both statements are correct.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "Dr. Rajendra Prasad chaired the Constituent Assembly when it met as a Constitution-making body, while G.V. Mavlankar chaired when it met as a Legislative body.",
    "அரசியலமைப்பு அமைப்பாகக் கூடிய போது ராஜேந்திர பிரசாத்தும், சட்டமன்றமாகக் கூடிய போது ஜி.வி. மாவ்லங்கரும் தலைமை தாங்கினர்.",
    "The total strength of the Constituent Assembly was 389 prior to partition, reduced to 299 after partition.",
    "பிரிவினைக்கு முன் சபையின் மொத்த உறுப்பினர்கள் 389, பிரிவினைக்குப் பின் 299 ஆகக் குறைந்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Constituent Assembly Background", "Two Statement"]
))

# Combine Q1-Q10 from previous build script
with open(target_path, "r", encoding="utf-8") as f:
    existing_q = json.load(f)

# Append Q11-Q15 to existing Q1-Q10
existing_q.extend(questions)
existing_q.sort(key=lambda x: x["id"])

with open(target_path, "w", encoding="utf-8") as f:
    json.dump(existing_q, f, ensure_ascii=False, indent=2)

print(f"Part 1 complete: {len(existing_q)} Two-Statement questions saved.")
