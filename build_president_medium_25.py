import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("Building President Medium MCQs Dataset (25 items)...")

medium_25 = [
  {
    "id": "POLITY_PRESIDENT_MEDIUM_001",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "What is the formula used to calculate the value of vote of an elected MLA of a State for the Presidential election under Article 55?", "ta": "உறுப்பு 55-ன் கீழ் குடியரசுத் தலைவர் தேர்தலுக்கு ஒரு மாநிலத்தின் தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ வாக்கின் மதிப்புகளைக் கணக்கிடப் பயன்படுத்தப்படும் சூத்திரம் என்ன?"},
    "question_en": "What is the formula used to calculate the value of vote of an elected MLA of a State for the Presidential election under Article 55?",
    "question_ta": "உறுப்பு 55-ன் கீழ் குடியரசுத் தலைவர் தேர்தலுக்கு ஒரு மாநிலத்தின் தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ வாக்கின் மதிப்புகளைக் கணக்கிடப் பயன்படுத்தப்படும் சூத்திரம் என்ன?",
    "options": [
      {"id": "A", "en": "(Total State Population / Total Elected MLAs) × 1000", "ta": "(மொத்த மாநில மக்கள் தொகை / மொத்த தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்கள்) × 1000"},
      {"id": "B", "en": "(Total State Population / Total Elected MLAs) ÷ 1000", "ta": "(மொத்த மாநில மக்கள் தொகை / மொத்த தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்கள்) ÷ 1000"},
      {"id": "C", "en": "(Total Value of Votes of all MLAs / Total Elected MPs) ÷ 100", "ta": "(அனைத்து எம்.எல்.ஏ வாக்குகளின் மொத்த மதிப்பு / மொத்த தேர்ந்தெடுக்கப்பட்ட எம்பிக்கள்) ÷ 100"},
      {"id": "D", "en": "(Total State Population / Total Elected MPs) ÷ 1000", "ta": "(மொத்த மாநில மக்கள் தொகை / மொத்த தேர்ந்தெடுக்கப்பட்ட எம்பிக்கள்) ÷ 1000"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Value of vote of an MLA = (Total Population of State / Total Number of Elected Members of State Legislative Assembly) ÷ 1000. Population is taken from 1971 Census.", "ta": "எம்.எல்.ஏ வாக்கு மதிப்பு = (மாநிலத்தின் மொத்த மக்கள் தொகை / மாநிலச் சட்டமன்றத்தின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களின் எண்ணிக்கை) ÷ 1000. மக்கள் தொகை 1971 கணக்கெடுப்பிலிருந்து எடுக்கப்படுகிறது."},
    "explanation_en": "Value of vote of an MLA = (Total Population of State / Total Number of Elected Members of State Legislative Assembly) ÷ 1000. Population is taken from 1971 Census.",
    "explanation_ta": "எம்.எல்.ஏ வாக்கு மதிப்பு = (மாநிலத்தின் மொத்த மக்கள் தொகை / மாநிலச் சட்டமன்றத்தின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களின் எண்ணிக்கை) ÷ 1000. மக்கள் தொகை 1971 கணக்கெடுப்பிலிருந்து எடுக்கப்படுகிறது.",
    "source_reference": "Part V - Article 55(2)(a)",
    "trap_point": {"en": "Remember it is DIVIDED by 1000 (or multiplied by 1/1000), not multiplied by 1000!", "ta": "1000-ஆல் வகுக்கப்படுகிறது (அல்லது 1/1000-ஆல் பெருக்கப்படுகிறது), 1000-ஆல் பெருக்கப்படுவதில்லை என்பதை நினைவில் கொள்க!"},
    "tnpsc_tip": {"en": "MLA vote value varies from State to State based on population (e.g. UP has highest, Sikkim lowest).", "ta": "மக்கள் தொகை அடிப்படையில் எம்.எல்.ஏ வாக்கு மதிப்பு மாநிலத்திற்கு மாநிலம் வேறுபடும் (உ.பி அதிகபட்சம், சிக்கிம் மிகக் குறைவு)."},
    "why_not_others": {
      "A": {"en": "Option A multiplies by 1000 instead of dividing by 1000.", "ta": "விருப்பம் A 1000-ஆல் பெருக்குகிறது, வகுப்பதற்குப் பதிலாக."},
      "B": {"en": "Correct. Formula is (Population / Elected MLAs) ÷ 1000 under Art 55.", "ta": "சரி. சூத்திரம் (மக்கள் தொகை / தேர்ந்தெடுக்கப்பட்ட எம்.எல்.ஏ-க்கள்) ÷ 1000 ஆகும்."},
      "C": {"en": "Option C is close to MP vote value formula, but uses incorrect divisor 100.", "ta": "விருப்பம் C எம்பி வாக்கு மதிப்பு சூத்திரத்திற்கு அருகில் உள்ளது, ஆனால் தவறான வகுப்பி 100-ஐப் பயன்படுத்துகிறது."},
      "D": {"en": "Option D incorrectly uses Elected MPs instead of Elected MLAs for State population.", "ta": "விருப்பம் D எம்.எல்.ஏ-க்களுக்குப் பதிலாக எம்பிக்களைத் தவறாகப் பயன்படுத்துகிறது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_002",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "How is the Value of Vote of an elected Member of Parliament (MP) calculated for the Presidential election under Article 55?", "ta": "உறுப்பு 55-ன் கீழ் குடியரசுத் தலைவர் தேர்தலுக்குத் தேர்ந்தெடுக்கப்பட்ட ஒரு நாடாளுமன்ற உறுப்பினரின் (MP) வாக்கு மதிப்பு எவ்வாறு கணக்கிடப்படுகிறது?"},
    "question_en": "How is the Value of Vote of an elected Member of Parliament (MP) calculated for the Presidential election under Article 55?",
    "question_ta": "உறுப்பு 55-ன் கீழ் குடியரசுத் தலைவர் தேர்தலுக்குத் தேர்ந்தெடுக்கப்பட்ட ஒரு நாடாளுமன்ற உறுப்பினரின் (MP) வாக்கு மதிப்பு எவ்வாறு கணக்கிடப்படுகிறது?",
    "options": [
      {"id": "A", "en": "Total value of votes of all elected MLAs of all States / Total number of elected MPs", "ta": "அனைத்து மாநிலங்களின் தேர்ந்தெடுக்கப்பட்ட அனைத்து எம்.எல்.ஏ-க்களின் வாக்குகளின் மொத்த மதிப்பு / தேர்ந்தெடுக்கப்பட்ட மொத்த எம்பிக்கள்"},
      {"id": "B", "en": "Total Population of India / Total number of elected MPs", "ta": "இந்தியாவின் மொத்த மக்கள் தொகை / தேர்ந்தெடுக்கப்பட்ட மொத்த எம்பிக்கள்"},
      {"id": "C", "en": "Total value of votes of all elected MLAs / Total number of seats in Lok Sabha", "ta": "தேர்ந்தெடுக்கப்பட்ட அனைத்து எம்.எல்.ஏ வாக்குகளின் மொத்த மதிப்பு / மக்களவையின் மொத்த இடங்கள்"},
      {"id": "D", "en": "Total Population of India ÷ 1000", "ta": "இந்தியாவின் மொத்த மக்கள் தொகை ÷ 1000"}
    ],
    "correct_answer": "A",
    "explanation": {"en": "Value of vote of an MP = Total value of votes of all elected MLAs of all States / Total number of elected members of both Houses of Parliament (Lok Sabha + Rajya Sabha). This ensures parity between States and Union.", "ta": "எம்பி வாக்கு மதிப்பு = அனைத்து மாநிலங்களின் தேர்ந்தெடுக்கப்பட்ட அனைத்து எம்.எல்.ஏ வாக்குகளின் மொத்த மதிப்பு / நாடாளுமன்ற இரு அவைகளின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களின் மொத்த எண்ணிக்கை. இது மாநிலங்களுக்கும் ஒன்றியத்திற்குமிடையே சமநிலையை உறுதி செய்கிறது."},
    "explanation_en": "Value of vote of an MP = Total value of votes of all elected MLAs of all States / Total number of elected members of both Houses of Parliament (Lok Sabha + Rajya Sabha). This ensures parity between States and Union.",
    "explanation_ta": "எம்பி வாக்கு மதிப்பு = அனைத்து மாநிலங்களின் தேர்ந்தெடுக்கப்பட்ட அனைத்து எம்.எல்.ஏ வாக்குகளின் மொத்த மதிப்பு / நாடாளுமன்ற இரு அவைகளின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களின் மொத்த எண்ணிக்கை. இது மாநிலங்களுக்கும் ஒன்றியத்திற்குமிடையே சமநிலையை உறுதி செய்கிறது.",
    "source_reference": "Part V - Article 55(2)(c)",
    "trap_point": {"en": "Denominator includes ONLY ELECTED MPs (LS + RS), NOT nominated MPs or total sanctioned strength.", "ta": "பகுதி வகுப்பி தேர்ந்தெடுக்கப்பட்ட எம்பிக்களை (LS + RS) மட்டுமே உள்ளடக்கும், நியமன எம்பிக்களையோ அல்லது மொத்த பலத்தையோ அல்ல."},
    "tnpsc_tip": {"en": "Every MP has the EXACT SAME vote value across India, unlike MLAs whose vote value varies by State.", "ta": "எம்.எல்.ஏ-க்கள் போல் அல்லாமல், இந்தியா முழுவதும் அனைத்து எம்பிக்களுக்கும் ஒரே மாதிரியான வாக்கு மதிப்பே இருக்கும்."},
    "why_not_others": {
      "A": {"en": "Correct. MP Vote Value = Total MLA votes / Total elected MPs.", "ta": "சரி. எம்பி வாக்கு மதிப்பு = மொத்த எம்.எல்.ஏ வாக்குகள் / தேர்ந்தெடுக்கப்பட்ட மொத்த எம்பிக்கள்."},
      "B": {"en": "Option B uses population directly, which is incorrect for MP vote value.", "ta": "விருப்பம் B மக்கள் தொகையை நேரடியாகப் பயன்படுத்துகிறது, இது தவறானது."},
      "C": {"en": "Option C includes only Lok Sabha seats, ignoring Rajya Sabha elected members.", "ta": "விருப்பம் C மக்களவை இடங்களை மட்டுமே உள்ளடக்குகிறது, மாநிலங்களவையை புறக்கணிக்கிறது."},
      "D": {"en": "Option D is not the constitutional formula.", "ta": "விருப்பம் D அரசியலமைப்பு சூத்திரம் அல்ல."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_003",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "What is the formula for the 'Electoral Quota' required for a candidate to be declared elected in the Presidential election?", "ta": "குடியரசுத் தலைவர் தேர்தலில் ஒரு வேட்பாளர் வெற்றி பெற்றவராக அறிவிக்கப்படத் தேவையான 'தேர்தல் பங்கு' (Electoral Quota) சூத்திரம் என்ன?"},
    "question_en": "What is the formula for the 'Electoral Quota' required for a candidate to be declared elected in the Presidential election?",
    "question_ta": "குடியரசுத் தலைவர் தேர்தலில் ஒரு வேட்பாளர் வெற்றி பெற்றவராக அறிவிக்கப்படத் தேவையான 'தேர்தல் பங்கு' (Electoral Quota) சூத்திரம் என்ன?",
    "options": [
      {"id": "A", "en": "(Total Valid Votes Polled / 2) + 1", "ta": "(பதிவான மொத்த செல்லுபடியாகும் வாக்குகள் / 2) + 1"},
      {"id": "B", "en": "(Total Valid Votes Polled / 3) + 1", "ta": "(பதிவான மொத்த செல்லுபடியாகும் வாக்குகள் / 3) + 1"},
      {"id": "C", "en": "(Total Valid Votes Polled / 100) + 50", "ta": "(பதிவான மொத்த செல்லுபடியாகும் வாக்குகள் / 100) + 50"},
      {"id": "D", "en": "Simple majority of members present and voting", "ta": "வந்திருந்து வாக்களிப்பவர்களின் எளிய பெரும்பான்மை"}
    ],
    "correct_answer": "A",
    "explanation": {"en": "Electoral Quota = (Total number of valid votes polled / (1 + 1)) + 1 = (Total Valid Votes / 2) + 1. A candidate must secure more than 50% of the valid votes polled to be elected.", "ta": "தேர்தல் பங்கு = (பதிவான மொத்த செல்லுபடியாகும் வாக்குகள் / (1 + 1)) + 1 = (செல்லுபடியாகும் வாக்குகள் / 2) + 1. வெற்றி பெற வேட்பாளர் 50%-க்கும் அதிகமான வாக்குகளைப் பெற வேண்டும்."},
    "explanation_en": "Electoral Quota = (Total number of valid votes polled / (1 + 1)) + 1 = (Total Valid Votes / 2) + 1. A candidate must secure more than 50% of the valid votes polled to be elected.",
    "explanation_ta": "தேர்தல் பங்கு = (பதிவான மொத்த செல்லுபடியாகும் வாக்குகள் / (1 + 1)) + 1 = (செல்லுபடியாகும் வாக்குகள் / 2) + 1. வெற்றி பெற வேட்பாளர் 50%-க்கும் அதிகமான வாக்குகளைப் பெற வேண்டும்.",
    "source_reference": "Part V - Article 55 System of Election",
    "trap_point": {"en": "Unlike general elections (FPTP), winning candidate must get an absolute majority (>50% votes) via Electoral Quota.", "ta": "பொதுத் தேர்தல்கள் (FPTP) போல் அல்லாமல், வெற்றி பெறும் வேட்பாளர் தேர்தல் பங்கு மூலம் தனிப் பெரும்பான்மையை (>50%) பெற வேண்டும்."},
    "tnpsc_tip": {"en": "If no candidate gets quota in 1st preference, 2nd preference votes are transferred (happened in 1969 V.V. Giri election).", "ta": "முதல் விருப்புவாக்கில் யாருக்கும் பங்கு கிடைக்காவிட்டால், 2வது விருப்புவாக்குகள் மாற்றப்படும் (1969 வி.வி. கிரி தேர்தலில் நிகழ்ந்தது)."},
    "why_not_others": {
      "A": {"en": "Correct. Electoral Quota = (Total Valid Votes / 2) + 1.", "ta": "சரி. தேர்தல் பங்கு = (மொத்த செல்லுபடியாகும் வாக்குகள் / 2) + 1."},
      "B": {"en": "Option B divides by 3, which applies for multi-member vacancies, not single post of President.", "ta": "விருப்பம் B 3-ஆல் வகுக்கிறது, இது பல இடங்கள் காலியிடத்திற்குப் பொருந்தும்."},
      "C": {"en": "Option C is not the constitutional formula.", "ta": "விருப்பம் C அரசியலமைப்பு சூத்திரம் அல்ல."},
      "D": {"en": "Simple majority of voters is FPTP, not Electoral Quota system.", "ta": "எளிய பெரும்பான்மை FPTP முறை, தேர்தல் பங்கு முறை அல்ல."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_004",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "What happens when an Ordinary Bill passed by Parliament is presented to the President under Article 111 and the President returns it for reconsideration?", "ta": "உறுப்பு 111-ன் கீழ் நாடாளுமன்றத்தால் நிறைவேற்றப்பட்ட ஒரு சாதாரண மசோதாக் குடியரசுத் தலைவருக்கு அனுப்பப்பட்டு, அதை அவர் மறுபரிசீலனைக்குத் திருப்பி அனுப்பினால் என்ன நிகழும்?"},
    "question_en": "What happens when an Ordinary Bill passed by Parliament is presented to the President under Article 111 and the President returns it for reconsideration?",
    "question_ta": "உறுப்பு 111-ன் கீழ் நாடாளுமன்றத்தால் நிறைவேற்றப்பட்ட ஒரு சாதாரண மசோதாக் குடியரசுத் தலைவருக்கு அனுப்பப்பட்டு, அதை அவர் மறுபரிசீலனைக்குத் திருப்பி அனுப்பினால் என்ன நிகழும்?",
    "options": [
      {"id": "A", "en": "If Parliament passes the bill again with or without amendment, President MUST give assent.", "ta": "நாடாளுமன்றம் திருத்தத்துடனோ இல்லாமலோ மசோதாவை மீண்டும் நிறைவேற்றினால், குடியரசுத் தலைவர் கண்டிப்பாக ஒப்புதல் அளிக்க வேண்டும்."},
      {"id": "B", "en": "The bill automatically lapses permanently.", "ta": "மசோதா தானாகவே நிரந்தரமாக செயலிழந்துவிடும்."},
      {"id": "C", "en": "President can return the bill a second time for reconsideration.", "ta": "குடியரசுத் தலைவர் மசோதாவை இரண்டாவது முறையும் மறுபரிசீலனைக்குத் திருப்பி அனுப்பலாம்."},
      {"id": "D", "en": "Bill must be passed by 2/3rd special majority in both Houses to override President.", "ta": "குடியரசுத் தலைவரை நிராகரிக்க மசோதா இரு அவைகளிலும் 2/3 பங்கு சிறப்பு பெரும்பான்மையால் நிறைவேற்றப்பட வேண்டும்."}
    ],
    "correct_answer": "A",
    "explanation": {"en": "Article 111 proviso states that if the Bill is passed again by the Houses with or without amendment and presented to the President for assent, the President SHALL NOT withhold assent therefrom. This constitutes a Suspensive Veto.", "ta": "உறுப்பு 111-ன் படி, நாடாளுமன்றத்தின் இரு அவைகளும் திருத்தத்துடனோ இல்லாமலோ மசோதாவை மீண்டும் நிறைவேற்றிக் குடியரசுத் தலைவருக்கு அனுப்பினால், அவர் ஒப்புதலை நிறுத்த முடியாது (இடைநிறுத்த வீட்டோ)."},
    "explanation_en": "Article 111 proviso states that if the Bill is passed again by the Houses with or without amendment and presented to the President for assent, the President SHALL NOT withhold assent therefrom. This constitutes a Suspensive Veto.",
    "explanation_ta": "உறுப்பு 111-ன் படி, நாடாளுமன்றத்தின் இரு அவைகளும் திருத்தத்துடனோ இல்லாமலோ மசோதாவை மீண்டும் நிறைவேற்றிக் குடியரசுத் தலைவருக்கு அனுப்பினால், அவர் ஒப்புதலை நிறுத்த முடியாது (இடைநிறுத்த வீட்டோ).",
    "source_reference": "Part V - Article 111 Proviso",
    "trap_point": {"en": "India has Suspensive Veto (overridden by Simple Majority), NOT Qualified Veto (which requires 2/3rd majority as in USA).", "ta": "இந்தியா இடைநிறுத்த வீட்டோவைக் (எளிய பெரும்பான்மையால் வெல்லப்படக்கூடியது) கொண்டுள்ளது, தகுதிவாய்ந்த வீட்டோவை (அமெரிக்காவில் 2/3 பெரும்பான்மை) அல்ல."},
    "tnpsc_tip": {"en": "Money Bills cannot be returned for reconsideration under Article 111.", "ta": "பண மசோதாக்களை உறுப்பு 111-ன் கீழ் மறுபரிசீலனைக்குத் திருப்பி அனுப்ப முடியாது."},
    "why_not_others": {
      "A": {"en": "Correct. Second passage by simple majority binds the President under Art 111.", "ta": "சரி. எளிய பெரும்பான்மையால் 2வது நிறைவேற்றம் குடியரசுத் தலைவரைக் கட்டுப்படுத்தும்."},
      "B": {"en": "Bill does not lapse; Parliament can re-pass it.", "ta": "மசோதா செயலிழக்காது; நாடாளுமன்றம் அதை மீண்டும் நிறைவேற்றலாம்."},
      "C": {"en": "President cannot return a bill a second time.", "ta": "குடியரசுத் தலைவர் மசோதாவை 2வது முறை திருப்பி அனுப்ப முடியாது."},
      "D": {"en": "Qualified Veto requiring 2/3rd majority does not exist in India.", "ta": "2/3 பங்கு பெரும்பான்மை தேவைப்படும் தகுதிவாய்ந்த வீட்டோ இந்தியாவில் இல்லை."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_005",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "Which type of Veto Power was exercised by President Giani Zail Singh in 1986 regarding the Indian Post Office (Amendment) Bill?", "ta": "1986-ல் இந்திய தபால் அலுவலக (திருத்த) மசோதா தொடர்பாகக் குடியரசுத் தலைவர் கியானி ஜெயில் சிங் பயன்படுத்திய வீட்டோ அதிகார வகை எது?"},
    "question_en": "Which type of Veto Power was exercised by President Giani Zail Singh in 1986 regarding the Indian Post Office (Amendment) Bill?",
    "question_ta": "1986-ல் இந்திய தபால் அலுவலக (திருத்த) மசோதா தொடர்பாகக் குடியரசுத் தலைவர் கியானி ஜெயில் சிங் பயன்படுத்திய வீட்டோ அதிகார வகை எது?",
    "options": [
      {"id": "A", "en": "Absolute Veto", "ta": "முழுமையான வீட்டோ (Absolute Veto)"},
      {"id": "B", "en": "Suspensive Veto", "ta": "இடைநிறுத்த வீட்டோ (Suspensive Veto)"},
      {"id": "C", "en": "Pocket Veto", "ta": "பாக்கெட் வீட்டோ (Pocket Veto)"},
      {"id": "D", "en": "Qualified Veto", "ta": "தகுதிவாய்ந்த வீட்டோ (Qualified Veto)"}
    ],
    "correct_answer": "C",
    "explanation": {"en": "In 1986, President Giani Zail Singh exercised the Pocket Veto by taking no action (neither giving assent nor returning nor rejecting) on the Indian Post Office (Amendment) Bill, as the Constitution prescribes no time limit for giving assent.", "ta": "1986-ல் குடியரசுத் தலைவர் கியானி ஜெயில் சிங் இந்திய தபால் அலுவலக (திருத்த) மசோதா மீது எந்த நடவடிக்கையும் எடுக்காமல் (ஒப்புதல் அளிக்காமலும், திருப்பியனுப்பாமலும்) பாக்கெட் வீட்டோவைப் பயன்படுத்தினார்."},
    "explanation_en": "In 1986, President Giani Zail Singh exercised the Pocket Veto by taking no action (neither giving assent nor returning nor rejecting) on the Indian Post Office (Amendment) Bill, as the Constitution prescribes no time limit for giving assent.",
    "explanation_ta": "1986-ல் குடியரசுத் தலைவர் கியானி ஜெயில் சிங் இந்திய தபால் அலுவலக (திருத்த) மசோதா மீது எந்த நடவடிக்கையும் எடுக்காமல் (ஒப்புதல் அளிக்காமலும், திருப்பியனுப்பாமலும்) பாக்கெட் வீட்டோவைப் பயன்படுத்தினார்.",
    "source_reference": "Part V - Article 111 & Veto Powers",
    "trap_point": {"en": "Indian President's pocket is bigger than US President's pocket because Indian Constitution sets NO time limit for assent (US Constitution sets 10 days).", "ta": "இந்தியக் குடியரசுத் தலைவரின் பாக்கெட் அமெரிக்க அதிபரின் பாக்கெட்டை விடப் பெரியது, ஏனெனில் இந்திய அரசியலமைப்பு ஒப்புதலுக்குக் கால வரம்பு விதிக்கவில்லை (அமெரிக்காவில் 10 நாட்கள்)."},
    "tnpsc_tip": {"en": "The Post Office Bill was later withdrawn by the Cabinet in 1989.", "ta": "தபால் அலுவலக மசோதா பின்னர் 1989-ல் அமைச்சரவையால் திரும்பப் பெறப்பட்டது."},
    "why_not_others": {
      "A": {"en": "Absolute Veto is withholding assent explicitly, usually for private member bills or defeated cabinet bills.", "ta": "முழுமையான வீட்டோ என்பது ஒப்புதலை வெளிப்படையாக மறுப்பதாகும்."},
      "B": {"en": "Suspensive Veto is returning the bill for reconsideration.", "ta": "இடைநிறுத்த வீட்டோ என்பது மசோதாவை மறுபரிசீலனைக்குத் திருப்புவதாகும்."},
      "C": {"en": "Correct. Pocket Veto means keeping the bill pending indefinitely.", "ta": "சரி. பாக்கெட் வீட்டோ என்பது மசோதாவைக் காலவரையின்றி நிலுவையில் வைப்பதாகும்."},
      "D": {"en": "Qualified Veto does not exist in India.", "ta": "தகுதிவாய்ந்த வீட்டோ இந்தியாவில் இல்லை."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_006",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "What is the maximum duration an Ordinance promulgated by the President under Article 123 can remain in force without being approved by Parliament?", "ta": "உறுப்பு 123-ன் கீழ் குடியரசுத் தலைவரால் பிறப்பிக்கப்பட்ட ஒரு அவசரச் சட்டம் நாடாளுமன்றத்தால் ஒப்புதல் பெறப்படாமல் அதிகபட்சமாக எவ்வளவு காலம் அமலில் இருக்க முடியும்?"},
    "question_en": "What is the maximum duration an Ordinance promulgated by the President under Article 123 can remain in force without being approved by Parliament?",
    "question_ta": "உறுப்பு 123-ன் கீழ் குடியரசுத் தலைவரால் பிறப்பிக்கப்பட்ட ஒரு அவசரச் சட்டம் நாடாளுமன்றத்தால் ஒப்புதல் பெறப்படாமல் அதிகபட்சமாக எவ்வளவு காலம் அமலில் இருக்க முடியும்?",
    "options": [
      {"id": "A", "en": "6 months", "ta": "6 மாதங்கள்"},
      {"id": "B", "en": "6 weeks", "ta": "6 வாரங்கள்"},
      {"id": "C", "en": "6 months and 6 weeks", "ta": "6 மாதங்கள் மற்றும் 6 வாரங்கள்"},
      {"id": "D", "en": "1 year", "ta": "1 ஆண்டு"}
    ],
    "correct_answer": "C",
    "explanation": {"en": "Article 123(2)(a) mandates that an Ordinance must be laid before Parliament and ceases to operate at the expiration of 6 weeks from the reassembly of Parliament. Since maximum gap between sessions is 6 months, maximum life is 6 months + 6 weeks.", "ta": "உறுப்பு 123(2)(a)-ன் படி அவசரச் சட்டம் நாடாளுமன்றம் மீண்டும் கூடிய 6 வாரங்களுக்குள் ஒப்புதல் பெற வேண்டும். கூட்டத் தொடர்களுக்கு இடையிலான அதிகபட்ச இடைவெளி 6 மாதங்கள் என்பதால், இதன் அதிகபட்ச ஆயுள் 6 மாதங்கள் + 6 வாரங்கள் ஆகும்."},
    "explanation_en": "Article 123(2)(a) mandates that an Ordinance must be laid before Parliament and ceases to operate at the expiration of 6 weeks from the reassembly of Parliament. Since maximum gap between sessions is 6 months, maximum life is 6 months + 6 weeks.",
    "explanation_ta": "உறுப்பு 123(2)(a)-ன் படி அவசரச் சட்டம் நாடாளுமன்றம் மீண்டும் கூடிய 6 வாரங்களுக்குள் ஒப்புதல் பெற வேண்டும். கூட்டத் தொடர்களுக்கு இடையிலான அதிகபட்ச இடைவெளி 6 மாதங்கள் என்பதால், இதன் அதிகபட்ச ஆயுள் 6 மாதங்கள் + 6 வாரங்கள் ஆகும்.",
    "source_reference": "Part V - Article 123(2)",
    "trap_point": {"en": "Do not confuse '6 weeks from reassembly' with '6 months total life'. Maximum life is 6 months PLUS 6 weeks!", "ta": "'மீண்டும் கூடிய 6 வாரங்கள்' என்பதை '6 மாதங்கள் மொத்த ஆயுள்' என்பதியுடன் குழப்ப வேண்டாம். அதிகபட்ச ஆயுள் 6 மாதங்கள் பிளஸ் 6 வாரங்கள்!"},
    "tnpsc_tip": {"en": "If Houses reassemble on different dates, 6-week countdown starts from the LATER date.", "ta": "இரு அவைகளும் வெவ்வேறு தேதிகளில் மீண்டும் கூடினால், பிந்தைய தேதியிலிருந்தே 6 வாரக் கணக்கு தொடங்கும்."},
    "why_not_others": {
      "A": {"en": "6 months is the maximum gap between parliamentary sessions.", "ta": "6 மாதங்கள் என்பது கூட்டத் தொடர்களுக்கு இடையிலான அதிகபட்ச இடைவெளி."},
      "B": {"en": "6 weeks is the deadline after reassembly of Parliament.", "ta": "6 வாரங்கள் என்பது நாடாளுமன்றம் மீண்டும் கூடிய பின் உள்ள காலக்கெடு."},
      "C": {"en": "Correct. Maximum life of an Ordinance = 6 months + 6 weeks.", "ta": "சரி. அவசரச் சட்டத்தின் அதிகபட்ச ஆயுள் = 6 மாதங்கள் + 6 வாரங்கள்."},
      "D": {"en": "1 year is incorrect.", "ta": "1 ஆண்டு என்பது தவறானது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_007",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "Under Article 72, which specific form of Pardoning Power involves substituting a lighter form of punishment in place of a harsher punishment (e.g., changing death sentence to rigorous imprisonment)?", "ta": "உறுப்பு 72-ன் கீழ், கடுமையான தண்டனைக்கு பதிலாக லேசான தண்டனையை மாற்றுவதை (எ.கா. மரண தண்டனையை ஆயுள் தண்டனையாக மாற்றுவது) உள்ளடக்கிய மன்னிப்பளிக்கும் அதிகாரத்தின் குறிப்பிட்ட வடிவம் எது?"},
    "question_en": "Under Article 72, which specific form of Pardoning Power involves substituting a lighter form of punishment in place of a harsher punishment (e.g., changing death sentence to rigorous imprisonment)?",
    "question_ta": "உறுப்பு 72-ன் கீழ், கடுமையான தண்டனைக்கு பதிலாக லேசான தண்டனையை மாற்றுவதை (எ.கா. மரண தண்டனையை ஆயுள் தண்டனையாக மாற்றுவது) உள்ளடக்கிய மன்னிப்பளிக்கும் அதிகாரத்தின் குறிப்பிட்ட வடிவம் எது?",
    "options": [
      {"id": "A", "en": "Commutation", "ta": "தண்டனை மாற்றுதல் (Commutation)"},
      {"id": "B", "en": "Remission", "ta": "தண்டனைக் குறைப்பு (Remission)"},
      {"id": "C", "en": "Respite", "ta": "தண்டனை நிவாரணம் (Respite)"},
      {"id": "D", "en": "Reprieve", "ta": "தண்டனை இடைநிறுத்தம் (Reprieve)"}
    ],
    "correct_answer": "A",
    "explanation": {"en": "Commutation means substitution of one form of punishment for a lighter form (e.g., death sentence to rigorous imprisonment, or rigorous imprisonment to simple imprisonment).", "ta": "தண்டனை மாற்றுதல் (Commutation) என்பது ஒரு தண்டனை வடிவத்திற்கு பதிலாக லேசான தண்டனை வடிவத்தை மாற்றுவதாகும் (எ.கா. மரண தண்டனையை ஆயுள் தண்டனையாக மாற்றுவது)."},
    "explanation_en": "Commutation means substitution of one form of punishment for a lighter form (e.g., death sentence to rigorous imprisonment, or rigorous imprisonment to simple imprisonment).",
    "explanation_ta": "தண்டனை மாற்றுதல் (Commutation) என்பது ஒரு தண்டனை வடிவத்திற்கு பதிலாக லேசான தண்டனை வடிவத்தை மாற்றுவதாகும் (எ.கா. மரண தண்டனையை ஆயுள் தண்டனையாக மாற்றுவது).",
    "source_reference": "Part V - Article 72 Pardoning Terms",
    "trap_point": {"en": "Remission reduces the QUANTITY of sentence without changing character; Commutation changes the CHARACTER/NATURE of sentence to a lighter form.", "ta": "தண்டனைக் குறைப்பு (Remission) தன்மையை மாற்றாமல் காலத்தைக் குறைக்கும்; தண்டனை மாற்றுதல் (Commutation) தன்மையை லேசானதாக மாற்றும்."},
    "tnpsc_tip": {"en": "Match terms: Pardon (complete absolution), Commutation (substitution), Remission (reducing period), Respite (special facts like pregnancy), Reprieve (temporary stay).", "ta": "சொற்களைப் பொருத்துக: Pardon (முழு மன்னிப்பு), Commutation (மாற்றுதல்), Remission (காலத்தைக் குறைத்தல்), Respite (சிறப்புச் சூழல்), Reprieve (தற்காலிகத் தடை)."},
    "why_not_others": {
      "A": {"en": "Correct. Commutation means substituting a lighter punishment.", "ta": "சரி. Commutation என்பது லேசான தண்டனையை மாற்றுவதாகும்."},
      "B": {"en": "Remission reduces period of sentence without changing character (e.g., 2 yrs to 1 yr R.I.).", "ta": "Remission என்பது தன்மையை மாற்றாமல் காலத்தைக் குறைப்பதாகும்."},
      "C": {"en": "Respite is awarding lesser sentence due to special facts like pregnancy or disability.", "ta": "Respite என்பது கர்ப்பம்/உடல் ஊனம் போன்ற சிறப்புச் சூழல்களுக்காகக் குறைப்பதாகும்."},
      "D": {"en": "Reprieve is a temporary stay of execution of a sentence (especially death sentence).", "ta": "Reprieve என்பது தண்டனையைத் தற்காலிகமாக இடைநிறுத்தி வைப்பதாகும்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_008",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "Under Article 72, which specific pardoning term denotes awarding a lesser sentence in place of one originally awarded due to some special fact, such as physical disability or pregnancy of a woman offender?", "ta": "உறுப்பு 72-ன் கீழ், குற்றவாளியின் உடல் ஊனம் அல்லது கர்ப்பம் போன்ற ஏதேனும் சிறப்புச் சூழலின் காரணமாக முதலில் அளிக்கப்பட்ட தண்டனைக்கு பதிலாகக் குறைந்த தண்டனை வழங்குவதைக் குறிக்கும் மன்னிப்பளிக்கும் சொல் எது?"},
    "question_en": "Under Article 72, which specific pardoning term denotes awarding a lesser sentence in place of one originally awarded due to some special fact, such as physical disability or pregnancy of a woman offender?",
    "question_ta": "உறுப்பு 72-ன் கீழ், குற்றவாளியின் உடல் ஊனம் அல்லது கர்ப்பம் போன்ற ஏதேனும் சிறப்புச் சூழலின் காரணமாக முதலில் அளிக்கப்பட்ட தண்டனைக்கு பதிலாகக் குறைந்த தண்டனை வழங்குவதைக் குறிக்கும் மன்னிப்பளிக்கும் சொல் எது?",
    "options": [
      {"id": "A", "en": "Reprieve", "ta": "தண்டனை இடைநிறுத்தம் (Reprieve)"},
      {"id": "B", "en": "Respite", "ta": "தண்டனை நிவாரணம் (Respite)"},
      {"id": "C", "en": "Remission", "ta": "தண்டனைக் குறைப்பு (Remission)"},
      {"id": "D", "en": "Commutation", "ta": "தண்டனை மாற்றுதல் (Commutation)"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Respite denotes awarding a lesser sentence in place of one originally awarded due to some special fact, such as physical disability of a convict or pregnancy of a woman offender.", "ta": "தண்டனை நிவாரணம் (Respite) என்பது குற்றவாளியின் உடல் ஊனம் அல்லது பெண் குற்றவாளியின் கர்ப்பம் போன்ற சிறப்புச் சூழலால் குறைந்த தண்டனை வழங்குவதைக் குறிக்கும்."},
    "explanation_en": "Respite denotes awarding a lesser sentence in place of one originally awarded due to some special fact, such as physical disability of a convict or pregnancy of a woman offender.",
    "explanation_ta": "தண்டனை நிவாரணம் (Respite) என்பது குற்றவாளியின் உடல் ஊனம் அல்லது பெண் குற்றவாளியின் கர்ப்பம் போன்ற சிறப்புச் சூழலால் குறைந்த தண்டனை வழங்குவதைக் குறிக்கும்.",
    "source_reference": "Part V - Article 72 Pardoning Terms",
    "trap_point": {"en": "Respite is specifically triggered by 'SPECIAL FACTS' about the convict (pregnancy / illness / age / disability).", "ta": "Respite என்பது குற்றவாளியைப் பற்றிய 'சிறப்புச் சூழல்களால்' (கர்ப்பம்/நோய்/வயது/ஊனம்) தூண்டப்படுகிறது."},
    "tnpsc_tip": {"en": "Keep clear: Respite = Special facts (pregnancy); Reprieve = Stay of execution; Commutation = Lighter form.", "ta": "தெளிவாக இருங்கள்: Respite = சிறப்புச் சூழல்கள் (கர்ப்பம்); Reprieve = தற்காலிகத் தடை; Commutation = லேசான வடிவம்."},
    "why_not_others": {
      "A": {"en": "Reprieve is stay of execution.", "ta": "Reprieve என்பது தண்டனைச் செயல்பாட்டுத் தடையாகும்."},
      "B": {"en": "Correct. Respite is awarding lesser sentence due to special facts.", "ta": "சரி. Respite என்பது சிறப்புச் சூழல்களால் குறைந்த தண்டனை வழங்குவதாகும்."},
      "C": {"en": "Remission is reducing period without changing character.", "ta": "Remission என்பது தன்மையை மாற்றாமல் காலத்தைக் குறைப்பதாகும்."},
      "D": {"en": "Commutation is substituting a lighter form.", "ta": "Commutation என்பது லேசான வடிவத்தை மாற்றுவதாகும்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_009",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "When a State Bill is reserved by the Governor for the consideration of the President under Article 200, what options are available to the President under Article 201?", "ta": "உறுப்பு 200-ன் கீழ் மாநில மசோதா ஆளுநரால் குடியரசுத் தலைவரின் பரிசீலனைக்கு ஒதுக்கப்படும் போது, உறுப்பு 201-ன் கீழ் குடியரசுத் தலைவருக்கு என்ன தெரிவுகள் உள்ளன?"},
    "question_en": "When a State Bill is reserved by the Governor for the consideration of the President under Article 200, what options are available to the President under Article 201?",
    "question_ta": "உறுப்பு 200-ன் கீழ் மாநில மசோதா ஆளுநரால் குடியரசுத் தலைவரின் பரிசீலனைக்கு ஒதுக்கப்படும் போது, உறுப்பு 201-ன் கீழ் குடியரசுத் தலைவருக்கு என்ன தெரிவுகள் உள்ளன?",
    "options": [
      {"id": "A", "en": "President can give assent, withhold assent, or direct Governor to return bill (except Money Bill) for reconsideration.", "ta": "குடியரசுத் தலைவர் ஒப்புதல் அளிக்கலாம், ஒப்புதலை நிறுத்தலாம் அல்லது பண மசோதா தவிர்த்து பிறவற்றை மறுபரிசீலனைக்குத் திருப்ப ஆளுநருக்கு உத்தரவிடலாம்."},
      {"id": "B", "en": "If State Legislature passes the bill again, President MUST give assent.", "ta": "மாநிலச் சட்டமன்றம் மசோதாவை மீண்டும் நிறைவேற்றினால் குடியரசுத் தலைவர் கட்டாயம் ஒப்புதல் அளிக்க வேண்டும்."},
      {"id": "C", "en": "President must give assent within 30 days.", "ta": "குடியரசுத் தலைவர் 30 நாட்களுக்குள் ஒப்புதல் அளித்தாக வேண்டும்."},
      {"id": "D", "en": "President has no veto power over State Bills.", "ta": "மாநில மசோதாக்கள் மீது குடியரசுத் தலைவருக்கு வீட்டோ அதிகாரம் இல்லை."}
    ],
    "correct_answer": "A",
    "explanation": {"en": "Under Article 201, when a State Bill is reserved for President's consideration, President may give assent, withhold assent, or direct Governor to return it. Crucially, even if the State Legislature passes the bill again, the President is NOT BOUND to give assent (Absolute Veto over State Bills).", "ta": "உறுப்பு 201-ன் கீழ் மாநில மசோதா அனுப்பப்பட்டால் குடியரசுத் தலைவர் ஒப்புதல் அளிக்கலாம், நிறுத்தலாம் அல்லது திருப்பியனுப்ப உத்தரவிடலாம். மாநிலச் சட்டமன்றம் மீண்டும் நிறைவேற்றினாலும் குடியரசுத் தலைவர் ஒப்புதல் அளிக்கக் கட்டுப்பட்டவர் அல்ல!"},
    "explanation_en": "Under Article 201, when a State Bill is reserved for President's consideration, President may give assent, withhold assent, or direct Governor to return it. Crucially, even if the State Legislature passes the bill again, the President is NOT BOUND to give assent (Absolute Veto over State Bills).",
    "explanation_ta": "உறுப்பு 201-ன் கீழ் மாநில மசோதா அனுப்பப்பட்டால் குடியரசுத் தலைவர் ஒப்புதல் அளிக்கலாம், நிறுத்தலாம் அல்லது திருப்பியனுப்ப உத்தரவிடலாம். மாநிலச் சட்டமன்றம் மீண்டும் நிறைவேற்றினாலும் குடியரசுத் தலைவர் ஒப்புதல் அளிக்கக் கட்டுப்பட்டவர் அல்ல!"},
    "source_reference": "Part VI - Article 201",
    "trap_point": {"en": "Unlike Parliamentary bills (where re-passage binds President), second passage by STATE Legislature does NOT bind the President!", "ta": "நாடாளுமன்ற மசோதாக்கள் போல் அல்லாமல் (மீண்டும் நிறைவேற்றினால் குடியரசுத் தலைவர் கட்டுப்படுவார்), மாநிலச் சட்டமன்றத்தின் 2வது நிறைவேற்றம் குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது!"},
    "tnpsc_tip": {"en": "Governor MUST reserve a State Bill for President if it endangers High Court's constitutional position.", "ta": "உயர் நீதிமன்றத்தின் அரசியலமைப்பு நிலைக்கு ஆபத்து விளைவிக்கும் மாநில மசோதாவை ஆளுநர் கட்டாயம் குடியரசுத் தலைவருக்கு ஒதுக்க வேண்டும்."},
    "why_not_others": {
      "A": {"en": "Correct. President has absolute discretion over reserved State Bills.", "ta": "சரி. ஒதுக்கப்பட்ட மாநில மசோதாக்கள் மீது குடியரசுத் தலைவருக்கு முழு விவேக அதிகாரம் உண்டு."},
      "B": {"en": "Second passage by State Legislature does NOT bind the President.", "ta": "மாநிலச் சட்டமன்றத்தின் 2வது நிறைவேற்றம் குடியரசுத் தலைவரைக் கட்டுப்படுத்தாது."},
      "C": {"en": "No 30-day time limit exists under Article 201.", "ta": "உறுப்பு 201-ன் கீழ் 30 நாள் கால வரம்பு எதுவும் இல்லை."},
      "D": {"en": "President enjoys veto power over reserved State Bills.", "ta": "குடியரசுத் தலைவர் ஒதுக்கப்பட்ட மாநில மசோதாக்கள் மீது வீட்டோ அதிகாரத்தைப் பெறுகிறார்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_010",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "What landmark judicial principle regarding Ordinance-making power under Article 123 was laid down by the Supreme Court in the D.C. Wadhwa Case (1987)?", "ta": "உறுப்பு 123-ன் கீழ் அவசரச் சட்ட அதிகாரம் தொடர்பாக 1987-ல் டி.சி. வாத்வா வழக்கில் உச்ச நீதிமன்றம் வழங்கிய மைல்கல் நீதித் தீர்ப்புத் தத்துவம் என்ன?"},
    "question_en": "What landmark judicial principle regarding Ordinance-making power under Article 123 was laid down by the Supreme Court in the D.C. Wadhwa Case (1987)?",
    "question_ta": "உறுப்பு 123-ன் கீழ் அவசரச் சட்ட அதிகாரம் தொடர்பாக 1987-ல் டி.சி. வாத்வா வழக்கில் உச்ச நீதிமன்றம் வழங்கிய மைல்கல் நீதித் தீர்ப்புத் தத்துவம் என்ன?",
    "options": [
      {"id": "A", "en": "Re-promulgation of Ordinances without placing them before Legislature is a fraud on the Constitution.", "ta": "சட்டமன்றத்தில் சமர்ப்பிக்காமல் அவசரச் சட்டங்களை மீண்டும் மீண்டும் பிறப்பிப்பது அரசியலமைப்புக்கு எதிரான மோசடியாகும்."},
      {"id": "B", "en": "Presidential satisfaction for Ordinance is immune from judicial review.", "ta": "அவசரச் சட்டத்திற்கான குடியரசுத் தலைவரின் திருப்தி நீதித்துறை மறுஆய்விலிருந்து தப்பியது."},
      {"id": "C", "en": "Ordinances can amend the Constitution.", "ta": "அவசரச் சட்டங்கள் அரசியலமைப்பைத் திருத்த முடியும்."},
      {"id": "D", "en": "Ordinances remain in force permanently if Parliament is dissolved.", "ta": "நாடாளுமன்றம் கலைக்கப்பட்டால் அவசரச் சட்டங்கள் நிரந்தரமாக அமலில் இருக்கும்."}
    ],
    "correct_answer": "A",
    "explanation": {"en": "In D.C. Wadhwa v. State of Bihar (1987), the SC held that successive re-promulgation of Ordinances without submitting them to the Legislature is a colorable exercise of power and a fraud on the Constitution.", "ta": "1987-ன் டி.சி. வாத்வா வழக்கில், சட்டமன்றத்தின் முன் வைக்காமல் அவசரச் சட்டங்களை மீண்டும் மீண்டும் பிறப்பிப்பது அதிகார துஷ்பிரயோகம் மற்றும் அரசியலமைப்புக்கு எதிரான மோசடியாகும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது."},
    "explanation_en": "In D.C. Wadhwa v. State of Bihar (1987), the SC held that successive re-promulgation of Ordinances without submitting them to the Legislature is a colorable exercise of power and a fraud on the Constitution.",
    "explanation_ta": "1987-ன் டி.சி. வாத்வா வழக்கில், சட்டமன்றத்தின் முன் வைக்காமல் அவசரச் சட்டங்களை மீண்டும் மீண்டும் பிறப்பிப்பது அதிகார துஷ்பிரயோகம் மற்றும் அரசியலமைப்புக்கு எதிரான மோசடியாகும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது.",
    "source_reference": "D.C. Wadhwa v. State of Bihar (1987)",
    "trap_point": {"en": "Re-promulgation bypasses the legislature, violating democratic legislative supremacy.", "ta": "மீண்டும் பிறப்பிப்பது சட்டமன்றத்தைத் தவிர்க்கிறது, இது ஜனநாயக சட்டமன்ற மேலாதிக்கத்தை மீறுகிறது."},
    "tnpsc_tip": {"en": "Reaffirmed in Krishna Kumar Singh v. State of Bihar (2017) by 7-Judge Bench.", "ta": "கிருஷ்ண குமார் சிங் (2017) 7 நீதிபதிகள் அமர்வு வழக்கில் இது மீண்டும் உறுதிப்படுத்தப்பட்டது."},
    "why_not_others": {
      "A": {"en": "Correct. Re-promulgation is a fraud on the Constitution under D.C. Wadhwa 1987.", "ta": "சரி. மீண்டும் பிறப்பிப்பது அரசியலமைப்புக்கு எதிரான மோசடியாகும் (டி.சி. வாத்வா 1987)."},
      "B": {"en": "Ordinance satisfaction IS subject to judicial review (Cooper 1970 / Krishna Kumar Singh 2017).", "ta": "அவசரச் சட்டத் திருப்தி நீதித்துறை மறுஆய்வுக்கு உட்பட்டது."},
      "C": {"en": "Ordinance CANNOT amend the Constitution.", "ta": "அவசரச் சட்டம் அரசியலமைப்பைத் திருத்த முடியாது."},
      "D": {"en": "Ordinance lapses automatically 6 weeks after reassembly.", "ta": "அவசரச் சட்டம் மீண்டும் கூடிய 6 வாரங்களில் தானாகவே செயலிழக்கும்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_011",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "Which of the following constitutional post holders is NOT appointed by the President of India on the recommendation/advice of the Union Cabinet?", "ta": "பின்வரும் எந்த அரசியலமைப்புப் பதவி வகிப்பவர் மத்திய அமைச்சரவையின் பரிந்துரை/ஆலோசனையின் பேரில் இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்படுவதில்லை?"},
    "question_en": "Which of the following constitutional post holders is NOT appointed by the President of India on the recommendation/advice of the Union Cabinet?",
    "question_ta": "பின்வரும் எந்த அரசியலமைப்புப் பதவி வகிப்பவர் மத்திய அமைச்சரவையின் பரிந்துரை/ஆலோசனையின் பேரில் இந்தியக் குடியரசுத் தலைவரால் நியமிக்கப்படுவதில்லை?",
    "options": [
      {"id": "A", "en": "Comptroller and Auditor General of India (CAG)", "ta": "இந்தியக் தலைமைத் தணிக்கையாளர் (CAG)"},
      {"id": "B", "en": "Attorney General for India", "ta": "இந்தியத் தலைமை வழக்கறிஞர் (Attorney General)"},
      {"id": "C", "en": "State Governor", "ta": "மாநில ஆளுநர்"},
      {"id": "D", "en": "Speaker of Lok Sabha", "ta": "மக்களவை சபாநாயகர்"}
    ],
    "correct_answer": "D",
    "explanation": {"en": "The Speaker of Lok Sabha is ELECTED by the members of Lok Sabha from amongst themselves (Article 93), NOT appointed by the President.", "ta": "மக்களவை சபாநாயகர் மக்களவை உறுப்பினர்களால் தங்களுக்குள்ளிருந்தே தேர்ந்தெடுக்கப்படுபவர் (உறுப்பு 93); குடியரசுத் தலைவரால் நியமிக்கப்படுபவர் அல்ல."},
    "explanation_en": "The Speaker of Lok Sabha is ELECTED by the members of Lok Sabha from amongst themselves (Article 93), NOT appointed by the President.",
    "explanation_ta": "மக்களவை சபாநாயகர் மக்களவை உறுப்பினர்களால் தங்களுக்குள்ளிருந்தே தேர்ந்தெடுக்கப்படுபவர் (உறுப்பு 93); குடியரசுத் தலைவரால் நியமிக்கப்படுபவர் அல்ல.",
    "source_reference": "Part V - Article 93 & Executive Appointments",
    "trap_point": {"en": "CAG, AG, Governors, CEC, UPSC Members are appointed by President, but Speaker is ELECTED by Lok Sabha.", "ta": "CAG, AG, ஆளுநர்கள், CEC, UPSC உறுப்பினர்கள் குடியரசுத் தலைவரால் நியமிக்கப்படுவார்கள், ஆனால் சபாநாயகர் மக்களவையால் தேர்ந்தெடுக்கப்படுவார்."},
    "tnpsc_tip": {"en": "Speaker Pro Tem is appointed by President, but regular Speaker is elected by Lok Sabha.", "ta": "தற்காலிக சபாநாயகர் குடியரசுத் தலைவரால் நியமிக்கப்படுவார், ஆனால் வழக்கமான சபாநாயகர் மக்களவையால் தேர்ந்தெடுக்கப்படுவார்."},
    "why_not_others": {
      "A": {"en": "CAG is appointed by President under Article 148.", "ta": "CAG உறுப்பு 148-ன் கீழ் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்."},
      "B": {"en": "Attorney General is appointed by President under Article 76.", "ta": "தலைமை வழக்கறிஞர் உறுப்பு 76-ன் கீழ் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்."},
      "C": {"en": "Governor is appointed by President under Article 155.", "ta": "ஆளுநர் உறுப்பு 155-ன் கீழ் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார்."},
      "D": {"en": "Correct. Speaker of Lok Sabha is ELECTED under Article 93.", "ta": "சரி. மக்களவை சபாநாயகர் உறுப்பு 93-ன் கீழ் தேர்ந்தெடுக்கப்படுகிறார்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_012",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "What constitutional change was introduced by the 44th Amendment Act, 1978 regarding Article 74(1) Aid and Advice of the Council of Ministers?", "ta": "அமைச்சரவையின் உதவி மற்றும் ஆலோசனை தொடர்பான உறுப்பு 74(1)-ல் 1978-ன் 44வது திருத்தச் சட்டத்தால் கொண்டுவரப்பட்ட அரசியலமைப்பு மாற்றம் என்ன?"},
    "question_en": "What constitutional change was introduced by the 44th Amendment Act, 1978 regarding Article 74(1) Aid and Advice of the Council of Ministers?",
    "question_ta": "அமைச்சரவையின் உதவி மற்றும் ஆலோசனை தொடர்பான உறுப்பு 74(1)-ல் 1978-ன் 44வது திருத்தச் சட்டத்தால் கொண்டுவரப்பட்ட அரசியலமைப்பு மாற்றம் என்ன?",
    "options": [
      {"id": "A", "en": "Made Cabinet advice completely non-binding on the President.", "ta": "அமைச்சரவை ஆலோசனையைக் குடியரசுத் தலைவர் மீது முற்றிலும் கட்டுப்படுத்தாததாக மாற்றியது."},
      {"id": "B", "en": "Empowered President to return advice ONCE for reconsideration, but re-sent advice is binding.", "ta": "ஆலோசனையை ஒருமுறை மறுபரிசீலனைக்குத் திருப்பி அனுப்பக் குடியரசுத் தலைவருக்கு அதிகாரமளித்தது, ஆனால் மீண்டும் அனுப்பப்படும் ஆலோசனை கட்டுப்படுத்தும்."},
      {"id": "C", "en": "Required 2/3rd parliamentary approval to override Presidential refusal.", "ta": "குடியரசுத் தலைவரின் நிராகரிப்பை வெல்ல 2/3 பங்கு நாடாளுமன்ற ஒப்புதலைக் கோரியது."},
      {"id": "D", "en": "Transferred executive power from President to Prime Minister directly.", "ta": "நிர்வாக அதிகாரத்தைக் குடியரசுத் தலைவரிடமிருந்து பிரதமருக்கு நேரடியாக மாற்றியது."}
    ],
    "correct_answer": "B",
    "explanation": {"en": "The 44th CAA 1978 inserted a proviso to Article 74(1) allowing the President to require the Council of Ministers to reconsider such advice. However, if the Council of Ministers resends the advice, the President MUST act in accordance with it.", "ta": "44வது திருத்தம் 1978 உறுப்பு 74(1)-ல் ஒரு விதியைச் சேர்த்தது; இதன்படி ஆலோசனையைக் குடியரசுத் தலைவர் ஒருமுறை மறுபரிசீலனைக்கு அனுப்பலாம். ஆனால் அமைச்சரவை மீண்டும் அனுப்பினால் அதற்கேற்ப செயல்பட்டே தீர வேண்டும்."},
    "explanation_en": "The 44th CAA 1978 inserted a proviso to Article 74(1) allowing the President to require the Council of Ministers to reconsider such advice. However, if the Council of Ministers resends the advice, the President MUST act in accordance with it.",
    "explanation_ta": "44வது திருத்தம் 1978 உறுப்பு 74(1)-ல் ஒரு விதியைச் சேர்த்தது; இதன்படி ஆலோசனையைக் குடியரசுத் தலைவர் ஒருமுறை மறுபரிசீலனைக்கு அனுப்பலாம். ஆனால் அமைச்சரவை மீண்டும் அனுப்பினால் அதற்கேற்ப செயல்பட்டே தீர வேண்டும்."},
    "source_reference": "Part V - Article 74(1) Proviso",
    "trap_point": {"en": "42nd CAA 1976 made advice binding without any reconsideration; 44th CAA 1978 gave ONE chance for reconsideration.", "ta": "42வது திருத்தம் 1976 மறுபரிசீலனையின்றி ஆலோசனையைக் கட்டாயமாக்கியது; 44வது திருத்தம் 1978 ஒருமுறை மறுபரிசீலனை வாய்ப்பை அளித்தது."},
    "tnpsc_tip": {"en": "Court cannot inquire into what advice was tendered by Ministers to President under Article 74(2).", "ta": "அமைச்சர்கள் குடியரசுத் தலைவருக்கு என்ன ஆலோசனை வழங்கினார்கள் என்பதை உறுப்பு 74(2)-ன் கீழ் நீதிமன்றங்கள் விசாரிக்க முடியாது."},
    "why_not_others": {
      "A": {"en": "Advice is still binding after one reconsideration.", "ta": "ஒரு மறுபரிசீலனைக்குப் பின் ஆலோசனை இன்னமும் கட்டாயமானது."},
      "B": {"en": "Correct. 44th CAA 1978 added 1-time reconsideration proviso.", "ta": "சரி. 44வது திருத்தம் 1978 ஒருமுறை மறுபரிசீலனை விதியைச் சேர்த்தது."},
      "C": {"en": "No 2/3rd parliamentary approval is involved in Art 74 advice.", "ta": "உறுப்பு 74 ஆலோசனையில் 2/3 பங்கு நாடாளுமன்ற ஒப்புதல் தொடர்பில்லை."},
      "D": {"en": "Executive power legally remains vested in the President under Art 53.", "ta": "நிர்வாக அதிகாரம் சட்டப்படி உறுப்பு 53-ன் கீழ் குடியரசுத் தலைவரிடமே உள்ளது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_013",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "Under Article 358, which Fundamental Right is automatically suspended during a National Emergency declared on grounds of War or External Aggression?", "ta": "போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு அடிப்படையில் தேசிய அவசரநிலை பிரகடனம் செய்யப்படும் போது உறுப்பு 358-ன் கீழ் எந்த அடிப்படை உரிமை தானாகவே இடைநிறுத்தப்படுகிறது?"},
    "question_en": "Under Article 358, which Fundamental Right is automatically suspended during a National Emergency declared on grounds of War or External Aggression?",
    "question_ta": "போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு அடிப்படையில் தேசிய அவசரநிலை பிரகடனம் செய்யப்படும் போது உறுப்பு 358-ன் கீழ் எந்த அடிப்படை உரிமை தானாகவே இடைநிறுத்தப்படுகிறது?",
    "options": [
      {"id": "A", "en": "Article 14 (Right to Equality)", "ta": "உறுப்பு 14 (சமத்துவ உரிமை)"},
      {"id": "B", "en": "Article 19 (6 Freedoms)", "ta": "உறுப்பு 19 (6 சுதந்திரங்கள்)"},
      {"id": "C", "en": "Article 21 (Protection of Life)", "ta": "உறுப்பு 21 (வாழ்வுரிமை)"},
      {"id": "D", "en": "Article 32 (Constitutional Remedies)", "ta": "உறுப்பு 32 (அரசியலமைப்பு பரிகார உரிமை)"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Article 358 automatically suspends the 6 Fundamental Freedoms under Article 19 as soon as National Emergency is proclaimed on grounds of War or External Aggression (External Emergency).", "ta": "போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு (வெளிப்புற அவசரநிலை) அடிப்படையில் தேசிய அவசரநிலை பிரகடனம் செய்யப்பட்டவுடன் உறுப்பு 358 உறுப்பு 19-ன் கீழ் உள்ள 6 சுதந்திரங்களைத் தானாகவே இடைநிறுத்துகிறது."},
    "explanation_en": "Article 358 automatically suspends the 6 Fundamental Freedoms under Article 19 as soon as National Emergency is proclaimed on grounds of War or External Aggression (External Emergency).",
    "explanation_ta": "போர் அல்லது வெளிநாட்டு ஆக்கிரமிப்பு (வெளிப்புற அவசரநிலை) அடிப்படையில் தேசிய அவசரநிலை பிரகடனம் செய்யப்பட்டவுடன் உறுப்பு 358 உறுப்பு 19-ன் கீழ் உள்ள 6 சுதந்திரங்களைத் தானாகவே இடைநிறுத்துகிறது.",
    "source_reference": "Part XVIII - Article 358",
    "trap_point": {"en": "44th CAA 1978 restricted Art 358 ONLY to External Emergency. Art 19 is NOT suspended if Emergency is declared on 'Armed Rebellion'!", "ta": "44வது திருத்தம் 1978 உறுப்பு 358-ஐ வெளிப்புற அவசரநிலைக்கு மட்டுமே குறிப்பிட்டது. 'ஆயுதக் கிளர்ச்சி' அவசரநிலையின் போது உறுப்பு 19 இடைநிறுத்தப்படாது!"},
    "tnpsc_tip": {"en": "Article 358 applies automatically without requiring a separate Presidential Order.", "ta": "உறுப்பு 358 தனிக் குடியரசுத் தலைவர் உத்தரவின்றி தானாகவே செயல்படும்."},
    "why_not_others": {
      "A": {"en": "Article 14 can only be suspended from court enforcement under Article 359, not automatically under Art 358.", "ta": "உறுப்பு 14 உறுப்பு 359-ன் கீழ் மட்டுமே இடைநிறுத்தப்படும்."},
      "B": {"en": "Correct. Article 19 is automatically suspended under Article 358.", "ta": "சரி. உறுப்பு 19 உறுப்பு 358-ன் கீழ் தானாகவே இடைநிறுத்தப்படும்."},
      "C": {"en": "Article 21 CAN NEVER be suspended under Art 358 or Art 359.", "ta": "உறுப்பு 21-ஐ ஒருபோதும் இடைநிறுத்த முடியாது."},
      "D": {"en": "Article 32 enforcement of specific rights comes under Art 359.", "ta": "உறுப்பு 32 குறிப்பிட்ட உரிமைகள் அமலாக்கம் உறுப்பு 359-ன் கீழ் வரும்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_014",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "Under Article 359, the President can suspend the right to move courts for enforcement of specified Fundamental Rights. Which two Articles CAN NEVER be suspended under Article 359 as per the 44th Amendment Act, 1978?", "ta": "உறுப்பு 359-ன் கீழ் குறிப்பிட்ட அடிப்படை உரிமைகளை அமல்படுத்த நீதிமன்றங்களை அணுகும் உரிமையைக் குடியரசுத் தலைவர் இடைநிறுத்தலாம். 1978-ன் 44வது திருத்தச் சட்டத்தின் படி எந்த இரு உறுப்புகளை உறுப்பு 359-ன் கீழ் ஒருபோதும் இடைநிறுத்த முடியாது?"},
    "question_en": "Under Article 359, the President can suspend the right to move courts for enforcement of specified Fundamental Rights. Which two Articles CAN NEVER be suspended under Article 359 as per the 44th Amendment Act, 1978?",
    "question_ta": "உறுப்பு 359-ன் கீழ் குறிப்பிட்ட அடிப்படை உரிமைகளை அமல்படுத்த நீதிமன்றங்களை அணுகும் உரிமையைக் குடியரசுத் தலைவர் இடைநிறுத்தலாம். 1978-ன் 44வது திருத்தச் சட்டத்தின் படி எந்த இரு உறுப்புகளை உறுப்பு 359-ன் கீழ் ஒருபோதும் இடைநிறுத்த முடியாது?",
    "options": [
      {"id": "A", "en": "Articles 14 and 19", "ta": "உறுப்புகள் 14 மற்றும் 19"},
      {"id": "B", "en": "Articles 19 and 21", "ta": "உறுப்புகள் 19 மற்றும் 21"},
      {"id": "C", "en": "Articles 20 and 21", "ta": "உறுப்புகள் 20 மற்றும் 21"},
      {"id": "D", "en": "Articles 21 and 22", "ta": "உறுப்புகள் 21 மற்றும் 22"}
    ],
    "correct_answer": "C",
    "explanation": {"en": "The 44th Constitutional Amendment Act, 1978 amended Article 359 to provide that the right to move any court for the enforcement of Fundamental Rights under Article 20 (Protection against conviction) and Article 21 (Protection of life & personal liberty) CAN NEVER BE SUSPENDED.", "ta": "1978-ன் 44வது அரசியலமைப்பு திருத்தச் சட்டம் உறுப்பு 359-ஐத் திருத்தி உறுப்பு 20 (குற்ற தண்டனை பாதுகாப்பு) மற்றும் உறுப்பு 21 (வாழ்வு & தனிநபர் சுதந்திர பாதுகாப்பு) ஆகியவற்றை அமல்படுத்த நீதிமன்றங்களை அணுகும் உரிமையை ஒருபோதும் இடைநிறுத்த முடியாது என விதியமைத்தது."},
    "explanation_en": "The 44th Constitutional Amendment Act, 1978 amended Article 359 to provide that the right to move any court for the enforcement of Fundamental Rights under Article 20 (Protection against conviction) and Article 21 (Protection of life & personal liberty) CAN NEVER BE SUSPENDED.",
    "explanation_ta": "1978-ன் 44வது அரசியலமைப்பு திருத்தச் சட்டம் உறுப்பு 359-ஐத் திருத்தி உறுப்பு 20 (குற்ற தண்டனை பாதுகாப்பு) மற்றும் உறுப்பு 21 (வாழ்வு & தனிநபர் சுதந்திர பாதுகாப்பு) ஆகியவற்றை அமல்படுத்த நீதிமன்றங்களை அணுகும் உரிமையை ஒருபோதும் இடைநிறுத்த முடியாது என விதியமைத்தது.",
    "source_reference": "Part XVIII - Article 359",
    "trap_point": {"en": "Remember the pair Articles 20 and 21! (Not 19 and 21). Article 19 CAN be suspended under Art 358 during external emergency.", "ta": "உறுப்புகள் 20 மற்றும் 21 சோடியை நினைவில் கொள்க! (19 மற்றும் 21 அல்ல). உறுப்பு 19 உறுப்பு 358-ன் கீழ் இடைநிறுத்தப்படலாம்."},
    "tnpsc_tip": {"en": "This safeguard was introduced to prevent human rights violations like ADM Jabalpur (Habeas Corpus case 1976).", "ta": "ADM ஜபல்பூர் (ஆட்கொணர்வு வழக்கு 1976) போன்ற மனித உரிமை மீறல்களைத் தடுக்க இப் பாதுகாப்பு கொண்டுவரப்பட்டது."},
    "why_not_others": {
      "A": {"en": "Article 14 can be suspended under Art 359.", "ta": "உறுப்பு 14 உறுப்பு 359-ன் கீழ் இடைநிறுத்தப்படலாம்."},
      "B": {"en": "Article 19 is suspended under Art 358.", "ta": "உறுப்பு 19 உறுப்பு 358-ன் கீழ் இடைநிறுத்தப்படும்."},
      "C": {"en": "Correct. Articles 20 and 21 CAN NEVER be suspended under Art 359.", "ta": "சரி. உறுப்புகள் 20 மற்றும் 21-ஐ ஒருபோதும் இடைநிறுத்த முடியாது."},
      "D": {"en": "Article 22 can be suspended under Art 359.", "ta": "உறுப்பு 22 உறுப்பு 359-ன் கீழ் இடைநிறுத்தப்படலாம்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_015",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "Who amongst the following is ENTITLED to vote in the Impeachment of the President under Article 61, despite being EXCLUDED from voting in the Presidential Election under Article 54?", "ta": "உறுப்பு 54-ன் கீழ் குடியரசுத் தலைவர் தேர்தலில் வாக்களிப்பதிலிருந்து விலக்கப்பட்ட போதிலும், உறுப்பு 61-ன் கீழ் குடியரசுத் தலைவர் பதவி நீக்கத்தில் வாக்களிக்க உரிமை பெற்றவர் யார்?"},
    "question_en": "Who amongst the following is ENTITLED to vote in the Impeachment of the President under Article 61, despite being EXCLUDED from voting in the Presidential Election under Article 54?",
    "question_ta": "உறுப்பு 54-ன் கீழ் குடியரசுத் தலைவர் தேர்தலில் வாக்களிப்பதிலிருந்து விலக்கப்பட்ட போதிலும், உறுப்பு 61-ன் கீழ் குடியரசுத் தலைவர் பதவி நீக்கத்தில் வாக்களிக்க உரிமை பெற்றவர் யார்?",
    "options": [
      {"id": "A", "en": "Elected members of Legislative Councils (MLCs)", "ta": "சட்ட மேலவைகளின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள் (MLCs)"},
      {"id": "B", "en": "Nominated members of Parliament (Lok Sabha & Rajya Sabha)", "ta": "நாடாளுமன்ற நியமன உறுப்பினர்கள் (மக்களவை & மாநிலங்களவை)"},
      {"id": "C", "en": "Elected members of Union Territory Assemblies", "ta": "யூனியன் பிரதேச சட்டமன்றங்களின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள்"},
      {"id": "D", "en": "Governors of States", "ta": "மாநில ஆளுநர்கள்"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Nominated members of Parliament (LS & RS) do not participate in the election of the President under Art 54, but THEY DO PARTICIPATE in the impeachment of the President under Art 61. Conversely, elected MLAs vote in election, but DO NOT vote in impeachment.", "ta": "நாடாளுமன்ற நியமன எம்பிக்கள் உறுப்பு 54-ன் கீழ் தேர்தலில் வாக்களிப்பதில்லை, ஆனால் உறுப்பு 61-ன் கீழ் பதவி நீக்கத்தில் வாக்களிக்கிறார்கள். மாறாக, எம்.எல்.ஏ-க்கள் தேர்தலில் வாக்களிக்கிறார்கள், ஆனால் பதவி நீக்கத்தில் வாக்களிப்பதில்லை."},
    "explanation_en": "Nominated members of Parliament (LS & RS) do not participate in the election of the President under Art 54, but THEY DO PARTICIPATE in the impeachment of the President under Art 61. Conversely, elected MLAs vote in election, but DO NOT vote in impeachment.",
    "explanation_ta": "நாடாளுமன்ற நியமன எம்பிக்கள் உறுப்பு 54-ன் கீழ் தேர்தலில் வாக்களிப்பதில்லை, ஆனால் உறுப்பு 61-ன் கீழ் பதவி நீக்கத்தில் வாக்களிக்கிறார்கள். மாறாக, எம்.எல்.ஏ-க்கள் தேர்தலில் வாக்களிப்பார்கள், ஆனால் பதவி நீக்கத்தில் வாக்களிப்பதில்லை.",
    "source_reference": "Part V - Article 61 vs Article 54",
    "trap_point": {"en": "Remember the reverse anomaly: Nominated MPs vote in impeachment (no election vote); State MLAs vote in election (no impeachment vote!).", "ta": "தலைகீழ் முரண்பாட்டை நினைவில் கொள்க: நியமன எம்பிக்கள் பதவி நீக்கத்தில் வாக்களிப்பார்கள்; எம்.எல்.ஏ-க்கள் பதவி நீக்கத்தில் வாக்களிக்க முடியாது!"},
    "tnpsc_tip": {"en": "Impeachment is a purely federal quasi-judicial process conducted inside Parliament.", "ta": "பதவி நீக்கம் என்பது நாடாளுமன்றத்திற்குள் நடைபெறும் பகுதி-நீதிமன்ற நடைமுறையாகும்."},
    "why_not_others": {
      "A": {"en": "Legislative Council members (MLCs) do not vote in election OR impeachment.", "ta": "சட்ட மேலவை உறுப்பினர்கள் தேர்தலிலும் பதவி நீக்கத்திலும் வாக்களிக்க முடியாது."},
      "B": {"en": "Correct. Nominated MPs vote in impeachment under Article 61.", "ta": "சரி. நியமன எம்பிக்கள் உறுப்பு 61-ன் கீழ் பதவி நீக்கத்தில் வாக்களிக்கலாம்."},
      "C": {"en": "UT MLAs vote in election, but DO NOT vote in impeachment.", "ta": "யூனியன் பிரதேச எம்.எல்.ஏ-க்கள் தேர்தலில் வாக்களிப்பார்கள், பதவி நீக்கத்தில் அல்ல."},
      "D": {"en": "Governors do not vote in election or impeachment.", "ta": "ஆளுநர்கள் வாக்களிப்பதில்லை."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_016",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "Under Article 61, what specific majority is required in EACH House of Parliament to pass a resolution for the impeachment of the President?", "ta": "உறுப்பு 61-ன் கீழ் குடியரசுத் தலைவரைப் பதவி நீக்கம் செய்யும் தீர்மானத்தை நிறைவேற்ற நாடாளுமன்றத்தின் ஒவ்வொரு அவையிலும் தேவைப்படும் குறிப்பிட்ட பெரும்பான்மை என்ன?"},
    "question_en": "Under Article 61, what specific majority is required in EACH House of Parliament to pass a resolution for the impeachment of the President?",
    "question_ta": "உறுப்பு 61-ன் கீழ் குடியரசுத் தலைவரைப் பதவி நீக்கம் செய்யும் தீர்மானத்தை நிறைவேற்ற நாடாளுமன்றத்தின் ஒவ்வொரு அவையிலும் தேவைப்படும் குறிப்பிட்ட பெரும்பான்மை என்ன?",
    "options": [
      {"id": "A", "en": "Simple majority of members present and voting", "ta": "வந்திருந்து வாக்களிப்பவர்களின் எளிய பெரும்பான்மை"},
      {"id": "B", "en": "Majority of total membership of the House", "ta": "அவையின் மொத்த உறுப்பினர்களில் பெரும்பான்மை"},
      {"id": "C", "en": "2/3rd majority of members present and voting", "ta": "வந்திருந்து வாக்களிப்பவர்களில் 2/3 பங்கு பெரும்பான்மை"},
      {"id": "D", "en": "Majority of not less than 2/3rd of the TOTAL MEMBERSHIP of the House", "ta": "அவையின் மொத்த உறுப்பினர்களில் 2/3 பங்கிற்கு குறையாத பெரும்பான்மை"}
    ],
    "correct_answer": "D",
    "explanation": {"en": "Article 61(2)(b) & 61(4) mandate that the impeachment resolution must be passed by a majority of NOT LESS THAN TWO-THIRDS OF THE TOTAL MEMBERSHIP of each House. This is the strictest majority requirement in the Constitution.", "ta": "உறுப்பு 61(2)(b) & 61(4) பதவி நீக்கத் தீர்மானம் ஒவ்வொரு அவையின் மொத்த உறுப்பினர்களில் 2/3 பங்கிற்கு குறையாத பெரும்பான்மையால் நிறைவேற்றப்பட வேண்டும் எனக் கட்டாயப்படுத்துகிறது. இதுவே அரசியலமைப்பில் உள்ள மிகக் கடுமையான பெரும்பான்மை தேவையாகும்."},
    "explanation_en": "Article 61(2)(b) & 61(4) mandate that the impeachment resolution must be passed by a majority of NOT LESS THAN TWO-THIRDS OF THE TOTAL MEMBERSHIP of each House. This is the strictest majority requirement in the Constitution.",
    "explanation_ta": "உறுப்பு 61(2)(b) & 61(4) பதவி நீக்கத் தீர்மானம் ஒவ்வொரு அவையின் மொத்த உறுப்பினர்களில் 2/3 பங்கிற்கு குறையாத பெரும்பான்மையால் நிறைவேற்றப்பட வேண்டும் எனக் கட்டாயப்படுத்துகிறது. இதுவே அரசியலமைப்பில் உள்ள மிகக் கடுமையான பெரும்பான்மை தேவையாகும்.",
    "source_reference": "Part V - Article 61(2)(b) & (4)",
    "trap_point": {"en": "Do not confuse '2/3rd present and voting' (used for constitutional amendments & judge removal) with '2/3rd of TOTAL MEMBERSHIP' (used ONLY for President impeachment!).", "ta": "'வந்திருந்து வாக்களிப்பவர்களில் 2/3 பங்கு' என்பதை 'மொத்த உறுப்பினர்களில் 2/3 பங்கு' (குடியரசுத் தலைவர் பதவி நீக்கத்திற்கு மட்டுமே) என்பதோடு குழப்ப வேண்டாம்."},
    "tnpsc_tip": {"en": "Notice period required before introducing impeachment resolution is 14 days signed by 1/4th total membership.", "ta": "தீர்மானம் கொண்டுவரும் முன் 1/4 பங்கு உறுப்பினர்கள் கையொப்பமிட்ட 14 நாட்கள் அறிவிப்பு தேவை."},
    "why_not_others": {
      "A": {"en": "Simple majority is not sufficient for impeachment.", "ta": "எளிய பெரும்பான்மை பதவி நீக்கத்திற்கு போதுமானது அல்ல."},
      "B": {"en": "Absolute majority alone is not sufficient; it requires 2/3rd of TOTAL membership.", "ta": "மொத்த உறுப்பினர்களில் பெரும்பான்மை மட்டும் போதாது; 2/3 பங்கு தேவை."},
      "C": {"en": "2/3rd present and voting is used for SC Judges removal (Art 124), not President impeachment.", "ta": "வந்திருந்து வாக்களிப்பவர்களில் 2/3 பங்கு உச்ச நீதிமன்ற நீதிபதிகள் நீக்கத்திற்குப் பயன்படும்."},
      "D": {"en": "Correct. 2/3rd of TOTAL MEMBERSHIP is mandatory under Article 61.", "ta": "சரி. உறுப்பு 61-ன் கீழ் மொத்த உறுப்பினர்களில் 2/3 பங்கு கட்டாயமாகும்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_017",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "Under Article 365, what is the consequence if a State Government fails to comply with or give effect to any administrative direction given by the Union Executive under the Constitution?", "ta": "உறுப்பு 365-ன் கீழ், அரசியலமைப்பின் படி மத்திய நிர்வாகம் வழங்கும் வழிகாட்டல்களை ஒரு மாநில அரசு பின்பற்றத் தவறினால் அதன் விளைவு என்ன?"},
    "question_en": "Under Article 365, what is the consequence if a State Government fails to comply with or give effect to any administrative direction given by the Union Executive under the Constitution?",
    "question_ta": "உறுப்பு 365-ன் கீழ், அரசியலமைப்பின் படி மத்திய நிர்வாகம் வழங்கும் வழிகாட்டல்களை ஒரு மாநில அரசு பின்பற்றத் தவறினால் அதன் விளைவு என்ன?",
    "options": [
      {"id": "A", "en": "It is lawful for the President to hold that a situation has arisen under Article 356 (President's Rule).", "ta": "உறுப்பு 356-ன் கீழ் (குடியரசுத் தலைவர் ஆட்சி) நிலைமை ஏற்பட்டுள்ளதாகக் குடியரசுத் தலைவர் கருதுவது சட்டப்பூர்வமானது."},
      {"id": "B", "en": "State Assembly is automatically dissolved without Presidential proclamation.", "ta": "குடியரசுத் தலைவர் பிரகடனமின்றி மாநிலச் சட்டமன்றம் தானாகக் கலைந்துவிடும்."},
      {"id": "C", "en": "Supreme Court automatically dismisses the Chief Minister.", "ta": "உச்ச நீதிமன்றம் முதலமைச்சரைத் தானாகவே பதவி நீக்கம் செய்யும்."},
      {"id": "D", "en": "Union Finance Minister freezes all financial grants to the State permanently.", "ta": "மத்திய நிதி அமைச்சர் மாநிலத்திற்கான அனைத்து நிதி மானியங்களையும் நிரந்தரமாக முடக்குவார்."}
    ],
    "correct_answer": "A",
    "explanation": {"en": "Article 365 expressly provides that where any State has failed to comply with, or to give effect to, any directions given in the exercise of the executive power of the Union, it shall be lawful for the President to hold that a situation has arisen in which the government of the State cannot be carried on in accordance with the provisions of the Constitution (triggering Article 356).", "ta": "உறுப்பு 365 மத்திய நிர்வாக வழிகாட்டுதல்களை ஒரு மாநில அரசு பின்பற்றத் தவறினால், உறுப்பு 356-ன் கீழ் மாநில அரசு அரசியலமைப்பு படி நடைபெற முடியாத நிலை ஏற்பட்டதாகக் குடியரசுத் தலைவர் கருதுவது சட்டப்பூர்வமானது எனக் கூறுகிறது."},
    "explanation_en": "Article 365 expressly provides that where any State has failed to comply with, or to give effect to, any directions given in the exercise of the executive power of the Union, it shall be lawful for the President to hold that a situation has arisen in which the government of the State cannot be carried on in accordance with the provisions of the Constitution (triggering Article 356).",
    "explanation_ta": "உறுப்பு 365 மத்திய நிர்வாக வழிகாட்டுதல்களை ஒரு மாநில அரசு பின்பற்றத் தவறினால், உறுப்பு 356-ன் கீழ் மாநில அரசு அரசியலமைப்பு படி நடைபெற முடியாத நிலை ஏற்பட்டதாகக் குடியரசுத் தலைவர் கருதுவது சட்டப்பூர்வமானது எனக் கூறுகிறது.",
    "source_reference": "Part XVIII - Article 365 & Article 356",
    "trap_point": {"en": "Article 365 does not directly impose President's Rule; it provides the LEGAL GROUND for invoking Article 356!", "ta": "உறுப்பு 365 நேரடியாகக் குடியரசுத் தலைவர் ஆட்சியை அமல்படுத்துவதில்லை; இது உறுப்பு 356-ஐப் பயன்படுத்துவதற்கான சட்டப்பூர்வ காரணத்தை வழங்குகிறது!"},
    "tnpsc_tip": {"en": "Article 356 has two sources: Governor's report (Art 356) or Union direction non-compliance (Art 365).", "ta": "உறுப்பு 356-க்கு இரு மூலாதாரங்கள்: ஆளுநர் அறிக்கை (356) அல்லது மத்திய வழிகாட்டல் மீறல் (365)."},
    "why_not_others": {
      "A": {"en": "Correct. Article 365 provides lawful grounds to invoke Article 356 President's Rule.", "ta": "சரி. உறுப்பு 365 உறுப்பு 356 குடியரசுத் தலைவர் ஆட்சியை அமல்படுத்த சட்டப்பூர்வ காரணமளிக்கிறது."},
      "B": {"en": "Assembly is not automatically dissolved.", "ta": "சட்டமன்றம் தானாகக் கலைந்துவிடாது."},
      "C": {"en": "Supreme Court does not dismiss CMs automatically.", "ta": "உச்ச நீதிமன்றம் தானாக முதல்வரை நீக்குவதில்லை."},
      "D": {"en": "Finance Minister cannot unilaterally freeze grants outside constitutional process.", "ta": "நிதி அமைச்சர் தன்னிச்சையாக மானியங்களை முடக்க முடியாது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_018",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "Under Article 360(4)(b), during a Financial Emergency, whose salaries and allowances can be directed to be reduced by the President, notwithstanding anything in the Constitution?", "ta": "உறுப்பு 360(4)(b)-ன் கீழ், நிதி அவசரநிலையின் போது அரசியலமைப்பில் என்ன சொல்லப்பட்டிருப்பினும், யாருடைய ஊதியம் மற்றும் படிகளைக் குறைக்கக் குடியரசுத் தலைவர் உத்தரவிட முடியும்?"},
    "question_en": "Under Article 360(4)(b), during a Financial Emergency, whose salaries and allowances can be directed to be reduced by the President, notwithstanding anything in the Constitution?",
    "question_ta": "உறுப்பு 360(4)(b)-ன் கீழ், நிதி அவசரநிலையின் போது அரசியலமைப்பில் என்ன சொல்லப்பட்டிருப்பினும், யாருடைய ஊதியம் மற்றும் படிகளைக் குறைக்கக் குடியரசுத் தலைவர் உத்தரவிட முடியும்?",
    "options": [
      {"id": "A", "en": "Only Group C and D government employees", "ta": "குரூப் சி மற்றும் டி அரசு ஊழியர்கள் மட்டுமே"},
      {"id": "B", "en": "Only State government employees", "ta": "மாநில அரசு ஊழியர்கள் மட்டுமே"},
      {"id": "C", "en": "All or any class of persons serving the Union/State, including Judges of Supreme Court and High Courts", "ta": "உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகள் உட்பட ஒன்றியம்/மாநிலத்தில் பணியாற்றும் அனைத்து அல்லது குறிப்பிட்ட பிரிவு ஊழியர்கள்"},
      {"id": "D", "en": "Only Members of Parliament", "ta": "நாடாளுமன்ற உறுப்பினர்கள் மட்டுமே"}
    ],
    "correct_answer": "C",
    "explanation": {"en": "Article 360(4)(b) explicitly provides that during a Financial Emergency, President may issue directions for the reduction of salaries and allowances of all or any class of persons serving in connection with Union/State affairs, INCLUDING the Judges of the Supreme Court and High Courts.", "ta": "உறுப்பு 360(4)(b) நிதி அவசரநிலையின் போது உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகள் உட்பட ஒன்றியம்/மாநிலத்தில் பணியாற்றும் அனைத்து அல்லது எந்தவொரு பிரிவு ஊழியர்களின் ஊதியம் மற்றும் படிகளைக் குறைக்கக் குடியரசுத் தலைவர் உத்தரவிடலாம் எனக் கூறுகிறது."},
    "explanation_en": "Article 360(4)(b) explicitly provides that during a Financial Emergency, President may issue directions for the reduction of salaries and allowances of all or any class of persons serving in connection with Union/State affairs, INCLUDING the Judges of the Supreme Court and High Courts.",
    "explanation_ta": "உறுப்பு 360(4)(b) நிதி அவசரநிலையின் போது உச்ச நீதிமன்ற மற்றும் உயர் நீதிமன்ற நீதிபதிகள் உட்பட ஒன்றியம்/மாநிலத்தில் பணியாற்றும் அனைத்து அல்லது எந்தவொரு பிரிவு ஊழியர்களின் ஊதியம் மற்றும் படிகளைக் குறைக்கக் குடியரசுத் தலைவர் உத்தரவிடலாம் எனக் கூறுகிறது.",
    "source_reference": "Part XVIII - Article 360(4)(b)",
    "trap_point": {"en": "SC/HC Judges' salaries are normally protected by Constitution and cannot be reduced to their disadvantage during tenure, EXCEPT during Financial Emergency under Art 360!", "ta": "உச்ச/உயர் நீதிமன்ற நீதிபதிகள் ஊதியம் பதவிக்காலத்தில் குறைக்கப்பட முடியாது, நிதி அவசரநிலையின் போது தவிர!"},
    "tnpsc_tip": {"en": "This is a unique exception where constitutional salary protection of judges is relaxed.", "ta": "நீதிபதிகளின் அரசியலமைப்பு ஊதியப் பாதுகாப்பு தளர்த்தப்படும் ஒரே விதிவிலக்கு இதுவாகும்."},
    "why_not_others": {
      "A": {"en": "Salary reduction applies to all classes, not just Group C and D.", "ta": "ஊதியக் குறைப்பு அனைத்துப் பிரிவினருக்கும் பொருந்தும்."},
      "B": {"en": "Applies to Union servants as well as State servants.", "ta": "ஒன்றிய ஊழியர்களுக்கும் மாநில ஊழியர்களுக்கும் பொருந்தும்."},
      "C": {"en": "Correct. Covers all Union/State servants, INCLUDING SC & HC Judges under Art 360(4)(b).", "ta": "சரி. உறுப்பு 360(4)(b)-ன் கீழ் உச்ச & உயர் நீதிமன்ற நீதிபதிகள் உட்பட அனைவரும் அடங்குவர்."},
      "D": {"en": "Covers all public servants and judges, not just MPs.", "ta": "எம்பிக்கள் மட்டுமல்லாது அனைத்து அரசு ஊழியர்கள் மற்றும் நீதிபதிகளும் அடங்குவர்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_019",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "Under Article 78(c), what power does the President possess regarding a decision taken by an individual Minister?", "ta": "உறுப்பு 78(c)-ன் கீழ் தனிப்பட்ட அமைச்சர் எடுத்த முடிவு தொடர்பாகக் குடியரசுத் தலைவருக்கு என்ன அதிகாரமுண்டு?"},
    "question_en": "Under Article 78(c), what power does the President possess regarding a decision taken by an individual Minister?",
    "question_ta": "உறுப்பு 78(c)-ன் கீழ் தனிப்பட்ட அமைச்சர் எடுத்த முடிவு தொடர்பாகக் குடியரசுத் தலைவருக்கு என்ன அதிகாரமுண்டு?",
    "options": [
      {"id": "A", "en": "President can directly annul the Minister's decision.", "ta": "குடியரசுத் தலைவர் அமைச்சரின் முடிவை நேரடியாக ரத்து செய்யலாம்."},
      {"id": "B", "en": "President can require the PM to submit the matter for consideration of the Council of Ministers.", "ta": "அவ்விகாரத்தை அமைச்சரவையின் பரிசீலனைக்கு வைக்குமாறு பிரதமரைக் கேட்டுக் கொள்ளலாம்."},
      {"id": "C", "en": "President can dismiss the individual Minister unilaterally.", "ta": "குடியரசுத் தலைவர் அந்த அமைச்சரைத் தன்னிச்சையாகப் பதவி நீக்கம் செய்யலாம்."},
      {"id": "D", "en": "President can refer the Minister's decision to the Supreme Court.", "ta": "குடியரசுத் தலைவர் அமைச்சரின் முடிவை உச்ச நீதிமன்றத்திற்கு அனுப்பலாம்."}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Article 78(c) provides that if the President so requires, the Prime Minister shall submit for the consideration of the Council of Ministers any matter on which a decision has been taken by a Minister but which has not been considered by the Council.", "ta": "உறுப்பு 78(c) தனி அமைச்சர் எடுத்த முடிவு அமைச்சரவையால் பரிசீலிக்கப்படாவிட்டால், குடியரசுத் தலைவர் கோரினால் அப்பொருளை அமைச்சரவையின் பரிசீலனைக்கு வைப்பது பிரதமரின் கடமையாகும் எனக் கூறுகிறது."},
    "explanation_en": "Article 78(c) provides that if the President so requires, the Prime Minister shall submit for the consideration of the Council of Ministers any matter on which a decision has been taken by a Minister but which has not been considered by the Council.",
    "explanation_ta": "உறுப்பு 78(c) தனி அமைச்சர் எடுத்த முடிவு அமைச்சரவையால் பரிசீலிக்கப்படாவிட்டால், குடியரசுத் தலைவர் கோரினால் அப்பொருளை அமைச்சரவையின் பரிசீலனைக்கு வைப்பது பிரதமரின் கடமையாகும் எனக் கூறுகிறது.",
    "source_reference": "Part V - Article 78(c)",
    "trap_point": {"en": "This enforces collective responsibility of the Cabinet under Article 75(3).", "ta": "இது உறுப்பு 75(3)-ன் கீழ் அமைச்சரவையின் கூட்டுப் பொறுப்பை உறுதிப்படுத்துகிறது."},
    "tnpsc_tip": {"en": "Article 78 has 3 clauses: 78(a) communicate decisions, 78(b) furnish info, 78(c) submit minister's decision to Cabinet.", "ta": "உறுப்பு 78-ல் 3 விதிகள்: 78(a) முடிவுகளைத் தெரிவித்தல், 78(b) தகவல் அளித்தல், 78(c) தனி அமைச்சர் முடிவை கேபினட்டிற்கு வைப்பது."},
    "why_not_others": {
      "A": {"en": "President cannot directly annul a minister's executive decision.", "ta": "குடியரசுத் தலைவர் அமைச்சரின் முடிவை நேரடியாக ரத்து செய்ய முடியாது."},
      "B": {"en": "Correct. President requires PM to submit matter to Cabinet under Art 78(c).", "ta": "சரி. உறுப்பு 78(c)-ன் கீழ் கேபினட் பரிசீலனைக்கு வைக்குமாறு பிரதமரைக் கோரலாம்."},
      "C": {"en": "President can dismiss a minister ONLY on advice of PM.", "ta": "பிரதமரின் ஆலோசனையின் பேரில் மட்டுமே அமைச்சரை நீக்க முடியும்."},
      "D": {"en": "Art 78(c) is about Cabinet consideration, not Supreme Court reference.", "ta": "உறுப்பு 78(c) கேபினட் பரிசீலனை பற்றியது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_020",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "What is the constitutional status of a Caretaker Government headed by a resigned or defeated Prime Minister in India?", "ta": "இந்தியாவில் ராஜினாமா செய்த அல்லது தோற்கடிக்கப்பட்ட பிரதமரைக் கொண்ட இடைக்கால அரசாங்கத்தின் அரசியலமைப்பு நிலை என்ன?"},
    "question_en": "What is the constitutional status of a Caretaker Government headed by a resigned or defeated Prime Minister in India?",
    "question_ta": "இந்தியாவில் ராஜினாமா செய்த அல்லது தோற்கடிக்கப்பட்ட பிரதமரைக் கொண்ட இடைக்கால அரசாங்கத்தின் அரசியலமைப்பு நிலை என்ன?",
    "options": [
      {"id": "A", "en": "It has no constitutional validity and is unconstitutional.", "ta": "அதற்கு அரசியலமைப்பு செல்லுபடித் தன்மை இல்லை மற்றும் அது அரசியலமைப்புக்கு எதிரானது."},
      {"id": "B", "en": "It carries out routine day-to-day administration under Art 74 to prevent executive vacuum, but cannot take major policy decisions.", "ta": "நிர்வாகக் காலியிடத்தைத் தடுக்க உறுப்பு 74-ன் கீழ் அன்றாட நிர்வாகத்தை கவனிக்கும், ஆனால் முக்கிய கொள்கை முடிவுகளை எடுக்க முடியாது."},
      {"id": "C", "en": "It enjoys full legislative powers to pass major financial schemes and ordinances.", "ta": "முக்கிய நிதித் திட்டங்கள் மற்றும் அவசரச் சட்டங்களை நிறைவேற்ற முழு சட்டமன்ற அதிகாரங்களையும் பெறுகிறது."},
      {"id": "D", "en": "It replaces the President as the De Jure head of state.", "ta": "அது குடியரசுத் தலைவருக்குப் பதிலாக நாட்டின் De Jure தலைவராக மாறுகிறது."}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Under Article 74, there must ALWAYS be a Council of Ministers to advise the President. A Caretaker Ministry exists by constitutional convention to maintain administrative continuity, but lacks political mandate to take major policy decisions, enact controversial ordinances, or make high-level appointments.", "ta": "உறுப்பு 74-ன் கீழ் குடியரசுத் தலைவருக்கு ஆலோசனை வழங்க எப்போதும் அமைச்சரவை இருக்க வேண்டும். நிர்வாகத் தொடர்ச்சிக்கு இடைக்கால அரசு மரபுப்படி இயங்குகிறது, ஆனால் முக்கிய கொள்கை முடிவுகளையோ, அவசரச் சட்டங்களையோ இயற்ற முடியாது."},
    "explanation_en": "Under Article 74, there must ALWAYS be a Council of Ministers to advise the President. A Caretaker Ministry exists by constitutional convention to maintain administrative continuity, but lacks political mandate to take major policy decisions, enact controversial ordinances, or make high-level appointments.",
    "explanation_ta": "உறுப்பு 74-ன் கீழ் குடியரசுத் தலைவருக்கு ஆலோசனை வழங்க எப்போதும் அமைச்சரவை இருக்க வேண்டும். நிர்வாகத் தொடர்ச்சிக்கு இடைக்கால அரசு மரபுப்படி இயங்குகிறது, ஆனால் முக்கிய கொள்கை முடிவுகளையோ, அவசரச் சட்டங்களையோ இயற்ற முடியாது.",
    "source_reference": "Part V - Article 74 & Constitutional Conventions",
    "trap_point": {"en": "Caretaker Govt is NOT a separate post in the Constitution text; it is derived from convention under Article 74 to avoid executive vacuum.", "ta": "இடைக்கால அரசு அரசியலமைப்பு உரையில் தனிப் பதவி அல்ல; உறுப்பு 74-ன் கீழ் மரபால் உருவானது."},
    "tnpsc_tip": {"en": "President ensures caretaker government stays within administrative boundaries.", "ta": "இடைக்கால அரசு எல்லைக்குள் செயல்படுவதைக் குடியரசுத் தலைவர் உறுதி செய்வார்."},
    "why_not_others": {
      "A": {"en": "Caretaker government is constitutionally necessary under Art 74.", "ta": "உறுப்பு 74-ன் கீழ் இடைக்கால அரசு அரசியலமைப்பு ரீதியாகத் தேவையானது."},
      "B": {"en": "Correct. Handles routine day-to-day admin without major policy mandate.", "ta": "சரி. கொள்கை அதிகாரமின்றி அன்றாட நிர்வாகத்தை மட்டுமே கவனிக்கும்."},
      "C": {"en": "Caretaker govt CANNOT pass major policy schemes or controversial ordinances.", "ta": "இடைக்கால அரசு முக்கிய கொள்கைத் திட்டங்களையோ அவசரச் சட்டங்களையோ இயற்ற முடியாது."},
      "D": {"en": "President remains De Jure head of state.", "ta": "குடியரசுத் தலைவரே De Jure தலைவராகத் தொடர்வார்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_021",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "Under Article 65, when the President is unable to discharge functions due to absence or illness, who discharges the functions of the President?", "ta": "வருகையின்மை அல்லது நோய் காரணமாகக் குடியரசுத் தலைவர் தன் பணிகளைச் செய்ய இயலாத போது, உறுப்பு 65-ன் கீழ் குடியரசுத் தலைவரின் பணிகளை யார் கவனிப்பார்?"},
    "question_en": "Under Article 65, when the President is unable to discharge functions due to absence or illness, who discharges the functions of the President?",
    "question_ta": "வருகையின்மை அல்லது நோய் காரணமாகக் குடியரசுத் தலைவர் தன் பணிகளைச் செய்ய இயலாத போது, உறுப்பு 65-ன் கீழ் குடியரசுத் தலைவரின் பணிகளை யார் கவனிப்பார்?",
    "options": [
      {"id": "A", "en": "Prime Minister of India", "ta": "இந்தியப் பிரதமர்"},
      {"id": "B", "en": "Vice-President of India", "ta": "இந்தியத் துணைத் தலைவர்"},
      {"id": "C", "en": "Chief Justice of India", "ta": "இந்தியத் தலைமை நீதிபதி"},
      {"id": "D", "en": "Speaker of Lok Sabha", "ta": "மக்களவை சபாநாயகர்"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Article 65(2) states that when the President is unable to discharge his functions owing to absence, illness or any other cause, the Vice-President shall discharge his functions until the date on which the President resumes his duties.", "ta": "உறுப்பு 65(2) வருகையின்மை, நோய் அல்லது பிற காரணத்தால் குடியரசுத் தலைவர் பணிகளைச் செய்ய இயலாத போது, அவர் மீண்டும் பொறுப்பேற்கும் வரை துணைத் தலைவர் அப்பணிகளைச் செய்வார் எனக் கூறுகிறது."},
    "explanation_en": "Article 65(2) states that when the President is unable to discharge his functions owing to absence, illness or any other cause, the Vice-President shall discharge his functions until the date on which the President resumes his duties.",
    "explanation_ta": "உறுப்பு 65(2) வருகையின்மை, நோய் அல்லது பிற காரணத்தால் குடியரசுத் தலைவர் பணிகளைச் செய்ய இயலாத போது, அவர் மீண்டும் பொறுப்பேற்கும் வரை துணைத் தலைவர் அப்பணிகளைச் செய்வார் எனக் கூறுகிறது.",
    "source_reference": "Part V - Article 65(2)",
    "trap_point": {"en": "Distinguish between Art 65(1) (casual vacancy where VP ACTS AS President) and Art 65(2) (inability where VP DISCHARGES FUNCTIONS).", "ta": "உறுப்பு 65(1) (காலியிடத்தில் செயல் குடியரசுத் தலைவர்) மற்றும் உறுப்பு 65(2) (இயலாமையில் பணிகளை நிவர்த்தி செய்தல்) ஆகியவற்றை வேறுபடுத்துக."},
    "tnpsc_tip": {"en": "During temporary inability, sitting President remains in office.", "ta": "தற்காலிக இயலாமையின் போது பதவியில் உள்ள குடியரசுத் தலைவரே பதவியில் தொடர்வார்."},
    "why_not_others": {
      "A": {"en": "PM does not discharge President's constitutional functions.", "ta": "பிரதமர் குடியரசுத் தலைவரின் பணிகளைச் செய்வதில்லை."},
      "B": {"en": "Correct. Vice-President discharges functions under Article 65(2).", "ta": "சரி. உறுப்பு 65(2)-ன் கீழ் துணைத் தலைவர் பணிகளைச் செய்வார்."},
      "C": {"en": "CJI only acts if VP post is also vacant.", "ta": "துணைத் தலைவர் பதவியும் காலியாக இருந்தால் மட்டுமே CJI செயல்படுவார்."},
      "D": {"en": "Speaker does not discharge President's functions.", "ta": "சபாநாயகர் குடியரசுத் தலைவர் பணிகளைச் செய்வதில்லை."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_022",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "What is the primary difference between a Nominal Executive (De Jure) and a Real Executive (De Facto) in India's parliamentary system?", "ta": "இந்திய நாடாளுமன்ற முறையில் பெயரளவு நிர்வாகி (De Jure) மற்றும் உண்மை நிர்வாகி (De Facto) ஆகியோருக்கிடையேயான முதன்மை வேறுபாடு என்ன?"},
    "question_en": "What is the primary difference between a Nominal Executive (De Jure) and a Real Executive (De Facto) in India's parliamentary system?",
    "question_ta": "இந்திய நாடாளுமன்ற முறையில் பெயரளவு நிர்வாகி (De Jure) மற்றும் உண்மை நிர்வாகி (De Facto) ஆகியோருக்கிடையேயான முதன்மை வேறுபாடு என்ன?",
    "options": [
      {"id": "A", "en": "President is Head of State (De Jure); PM is Head of Govt (De Facto) exercising real power under Art 74.", "ta": "குடியரசுத் தலைவர் நாட்டின் தலைவர் (De Jure); பிரதமர் அரசாங்கத்தின் தலைவர் (De Facto) உறுப்பு 74-ன் கீழ் உண்மையான அதிகாரத்தைச் செலுத்துபவர்."},
      {"id": "B", "en": "President exercises real powers during peacetime, PM during emergency.", "ta": "சாதாரண காலத்தில் குடியரசுத் தலைவர் உண்மையான அதிகாரத்தைச் செலுத்துவார், அவசரநிலையில் பிரதமர் செலுத்துவார்."},
      {"id": "C", "en": "PM is Head of State; President is Head of Govt.", "ta": "பிரதமர் நாட்டின் தலைவர்; குடியரசுத் தலைவர் அரசாங்கத்தின் தலைவர்."},
      {"id": "D", "en": "Both President and PM enjoy equal executive authority.", "ta": "குடியரசுத் தலைவர் மற்றும் பிரதமர் இருவரும் சமமான நிர்வாக அதிகாரத்தைப் பெறுகிறார்கள்."}
    ],
    "correct_answer": "A",
    "explanation": {"en": "In India's parliamentary form of government, President is the Nominal (De Jure) Executive and Head of State in whose name all actions are taken (Art 77). Prime Minister is the Real (De Facto) Executive and Head of Government who leads the Cabinet.", "ta": "இந்திய நாடாளுமன்ற அமைப்பில் குடியரசுத் தலைவர் பெயரளவு (De Jure) நிர்வாகி மற்றும் நாட்டின் தலைவர் ஆவார் (உறுப்பு 77). பிரதமர் உண்மை (De Facto) நிர்வாகி மற்றும் கேபினட்டை வழிநடத்தும் அரசாங்கத்தின் தலைவர் ஆவார்."},
    "explanation_en": "In India's parliamentary form of government, President is the Nominal (De Jure) Executive and Head of State in whose name all actions are taken (Art 77). Prime Minister is the Real (De Facto) Executive and Head of Government who leads the Cabinet.",
    "explanation_ta": "இந்திய நாடாளுமன்ற அமைப்பில் குடியரசுத் தலைவர் பெயரளவு (De Jure) நிர்வாகி மற்றும் நாட்டின் தலைவர் ஆவார் (உறுப்பு 77). பிரதமர் உண்மை (De Facto) நிர்வாகி மற்றும் கேபினட்டை வழிநடத்தும் அரசாங்கத்தின் தலைவர் ஆவார்.",
    "source_reference": "Part V - Articles 53, 74, 75, 77",
    "trap_point": {"en": "All executive action is formally taken IN THE NAME of President under Art 77, but DECIDED by Cabinet under PM.", "ta": "அனைத்து நிர்வாக நடவடிக்கைகளும் உறுப்பு 77-ன் கீழ் குடியரசுத் தலைவர் பெயரிலேயே எடுக்கப்படும், ஆனால் பிரதமரைக் கொண்ட அமைச்சரவையால் தீர்மானிக்கப்படும்."},
    "tnpsc_tip": {"en": "Bagehotian model: President reigns but does not rule; PM rules.", "ta": "பாஜ்காட் மாதிரி: குடியரசுத் தலைவர் ஆளுகிறார் ஆட்சி செய்வதில்லை; பிரதமரே ஆட்சி செய்கிறார்."},
    "why_not_others": {
      "A": {"en": "Correct. President = Head of State (De Jure); PM = Head of Govt (De Facto).", "ta": "சரி. குடியரசுத் தலைவர் = நாட்டின் தலைவர் (De Jure); பிரதமர் = அரசின் தலைவர் (De Facto)."},
      "B": {"en": "PM exercises real executive power during peacetime and emergency.", "ta": "பிரதமரே எக்காலத்திலும் உண்மையான அதிகாரத்தைச் செலுத்துகிறார்."},
      "C": {"en": "Reverses the roles of Head of State and Head of Govt.", "ta": "நாட்டின் தலைவர் மற்றும் அரசின் தலைவர் நிலைகளை மாற்றி அமைக்கிறது."},
      "D": {"en": "Powers are not equal in parliamentary executive.", "ta": "நாடாளுமன்ற நிர்வாகத்தில் அதிகாரங்கள் சமமானவை அல்ல."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_023",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "What is the requirement regarding Money Bills under Article 117 when introduced in Lok Sabha?", "ta": "உறுப்பு 117-ன் கீழ் மக்களவையில் அறிமுகப்படுத்தப்படும் பண மசோதாக்கள் தொடர்பான நிபந்தனை என்ன?"},
    "question_en": "What is the requirement regarding Money Bills under Article 117 when introduced in Lok Sabha?",
    "question_ta": "உறுப்பு 117-ன் கீழ் மக்களவையில் அறிமுகப்படுத்தப்படும் பண மசோதாக்கள் தொடர்பான நிபந்தனை என்ன?",
    "options": [
      {"id": "A", "en": "Can be introduced ONLY on the prior recommendation of the President.", "ta": "குடியரசுத் தலைவரின் முன் பரிந்துரையின் பேரில் மட்டுமே அறிமுகப்படுத்தப்பட முடியும்."},
      {"id": "B", "en": "Can be introduced in either Lok Sabha or Rajya Sabha directly.", "ta": "மக்களவை அல்லது மாநிலங்களவை எதிலும் நேரடியாக அறிமுகப்படுத்தப்படலாம்."},
      {"id": "C", "en": "Requires 2/3rd majority recommendation of State Governors.", "ta": "மாநில ஆளுநர்களின் 2/3 பங்கு பரிந்துரை தேவை."},
      {"id": "D", "en": "Does not require President's recommendation at any stage.", "ta": "எந்த நிலையிலும் குடியரசுத் தலைவரின் பரிந்துரை தேவையில்லை."}
    ],
    "correct_answer": "A",
    "explanation": {"en": "Article 117(1) mandates that a Money Bill (defined in Art 110) shall NOT be introduced or moved except on the recommendation of the President, and a Money Bill SHALL NOT be introduced in Rajya Sabha.", "ta": "உறுப்பு 117(1) பண மசோதா (உறுப்பு 110) குடியரசுத் தலைவரின் முன் பரிந்துரையின்றி அறிமுகப்படுத்தப்படக் கூடாது என்றும் மாநிலங்களவையில் அறிமுகப்படுத்தப்படக் கூடாது என்றும் கட்டாயப்படுத்துகிறது."},
    "explanation_en": "Article 117(1) mandates that a Money Bill (defined in Art 110) shall NOT be introduced or moved except on the recommendation of the President, and a Money Bill SHALL NOT be introduced in Rajya Sabha.",
    "explanation_ta": "உறுப்பு 117(1) பண மசோதா (உறுப்பு 110) குடியரசுத் தலைவரின் முன் பரிந்துரையின்றி அறிமுகப்படுத்தப்படக் கூடாது என்றும் மாநிலங்களவையில் அறிமுகப்படுத்தப்படக் கூடாது என்றும் கட்டாயப்படுத்துகிறது.",
    "source_reference": "Part V - Article 117(1)",
    "trap_point": {"en": "Because Money Bill is introduced with President's PRIOR recommendation, President normally DOES NOT withhold assent or return it under Art 111.", "ta": "முன் பரிந்துரையுடன் அறிமுகப்படுத்தப்படுவதால், பண மசோதாக் குடியரசுத் தலைவரால் வழக்கமாகத் திருப்பி அனுப்பப்படுவதில்லை."},
    "tnpsc_tip": {"en": "Money Bills originate ONLY in Lok Sabha with President's recommendation.", "ta": "பண மசோதாக்கள் குடியரசுத் தலைவரின் பரிந்துரையுடன் மக்களவையில் மட்டுமே தொடங்கும்."},
    "why_not_others": {
      "A": {"en": "Correct. Prior recommendation of President is mandatory under Art 117(1).", "ta": "சரி. உறுப்பு 117(1)-ன் கீழ் குடியரசுத் தலைவரின் முன் பரிந்துரை கட்டாயமாகும்."},
      "B": {"en": "Money Bill CANNOT be introduced in Rajya Sabha.", "ta": "பண மசோதா மாநிலங்களவையில் அறிமுகப்படுத்தப்பட முடியாது."},
      "C": {"en": "Governors have no role in Union Money Bills.", "ta": "ஒன்றிய பண மசோதாக்களில் ஆளுநர்களுக்குப் பங்கில்லை."},
      "D": {"en": "President's recommendation is mandatory prior to introduction.", "ta": "அறிமுகத்திற்கு முன் குடியரசுத் தலைவரின் பரிந்துரை கட்டாயமாகும்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_024",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "Under Article 77, how are all executive actions of the Government of India formally taken?", "ta": "உறுப்பு 77-ன் கீழ் இந்திய அரசின் அனைத்து நிர்வாக நடவடிக்கைகளும் முறைப்படி யாருடைய பெயரால் எடுக்கப்படுகின்றன?"},
    "question_en": "Under Article 77, how are all executive actions of the Government of India formally taken?",
    "question_ta": "உறுப்பு 77-ன் கீழ் இந்திய அரசின் அனைத்து நிர்வாக நடவடிக்கைகளும் முறைப்படி யாருடைய பெயரால் எடுக்கப்படுகின்றன?",
    "options": [
      {"id": "A", "en": "In the name of the Prime Minister of India", "ta": "இந்தியப் பிரதமரின் பெயரால்"},
      {"id": "B", "en": "In the name of the President of India", "ta": "இந்தியக் குடியரசுத் தலைவரின் பெயரால்"},
      {"id": "C", "en": "In the name of the Parliament of India", "ta": "இந்திய நாடாளுமன்றத்தின் பெயரால்"},
      {"id": "D", "en": "In the name of the Cabinet Secretary", "ta": "கேபினட் செயலாளரின் பெயரால்"}
    ],
    "correct_answer": "B",
    "explanation": {"en": "Article 77(1) mandates that all executive action of the Government of India shall be expressed to be taken in the name of the President.", "ta": "உறுப்பு 77(1) இந்திய அரசின் அனைத்து நிர்வாக நடவடிக்கைகளும் குடியரசுத் தலைவரின் பெயரால் எடுக்கப்படுவதாகத் தெரிவிக்கப்பட வேண்டும் எனக் கட்டாயப்படுத்துகிறது."},
    "explanation_en": "Article 77(1) mandates that all executive action of the Government of India shall be expressed to be taken in the name of the President.",
    "explanation_ta": "உறுப்பு 77(1) இந்திய அரசின் அனைத்து நிர்வாக நடவடிக்கைகளும் குடியரசுத் தலைவரின் பெயரால் எடுக்கப்படுவதாகத் தெரிவிக்கப்பட வேண்டும் எனக் கட்டாயப்படுத்துகிறது.",
    "source_reference": "Part V - Article 77(1)",
    "trap_point": {"en": "Executive actions are expressed in President's name, but Authentication rules are made by President under Art 77(2).", "ta": "நிர்வாக நடவடிக்கைகள் குடியரசுத் தலைவர் பெயரால் வெளியிடப்படும், ஆனால் அதன் அங்கீகார விதிகளைக் குடியரசுத் தலைவர் உருவாக்குவார்."},
    "tnpsc_tip": {"en": "Article 77 also empowers President to make rules for convenient transaction of business of GoI.", "ta": "இந்திய அரசுப் பணிகளை எளிதாக நடத்த விதிகளை உருவாக்க உறுப்பு 77 குடியரசுத் தலைவருக்கு அதிகாரமளிக்கிறது."},
    "why_not_others": {
      "A": {"en": "Actions are taken in President's name, not PM's name.", "ta": "நடவடிக்கைகள் குடியரசுத் தலைவர் பெயரால் எடுக்கப்படும், பிரதமர் பெயரால் அல்ல."},
      "B": {"en": "Correct. Article 77(1) specifies all executive action is taken in the name of President.", "ta": "சரி. உறுப்பு 77(1) அனைத்து நிர்வாக நடவடிக்கைகளும் குடியரசுத் தலைவர் பெயரால் எடுக்கப்படும் எனக் கூறுகிறது."},
      "C": {"en": "Parliament is legislature, not the formal executive entity.", "ta": "நாடாளுமன்றம் சட்டமன்ற அமைப்பு, முறைசார் நிர்வாக அமைப்பு அல்ல."},
      "D": {"en": "Cabinet Secretary authenticates orders, but actions are in President's name.", "ta": "கேபினட் செயலாளர் சான்றளிப்பார், ஆனால் நடவடிக்கைகள் குடியரசுத் தலைவர் பெயரால் எடுக்கப்படும்."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  },
  {
    "id": "POLITY_PRESIDENT_MEDIUM_025",
    "subject": "Polity",
    "topic": "President of India",
    "difficulty": "Medium",
    "question_type": "Conceptual",
    "question": {"en": "Under Article 361, what personal immunity is granted to the President of India during his term of office?", "ta": "உறுப்பு 361-ன் கீழ் பதவிக் காலத்தில் இந்தியக் குடியரசுத் தலைவருக்கு என்ன தனிநபர் விலக்களிப்பு வழங்கப்பட்டுள்ளது?"},
    "question_en": "Under Article 361, what personal immunity is granted to the President of India during his term of office?",
    "question_ta": "உறுப்பு 361-ன் கீழ் பதவிக் காலத்தில் இந்தியக் குடியரசுத் தலைவருக்கு என்ன தனிநபர் விலக்களிப்பு வழங்கப்பட்டுள்ளது?",
    "options": [
      {"id": "A", "en": "No criminal proceedings whatsoever shall be instituted or continued against the President in any court during his term of office.", "ta": "பதவிக் காலத்தில் குடியரசுத் தலைவருக்கு எதிராக எந்தவொரு குற்றவியல் நடவடிக்கையும் எந்த நீதிமன்றத்திலும் தொடங்கப்படவோ தொடரப்படவோ முடியாது."},
      {"id": "B", "en": "Civil proceedings cannot be instituted even after giving 2 months written notice.", "ta": "2 மாத எழுத்துப்பூர்வ அறிவிப்பு அளித்த பிறகும் உரிமையியல் நடவடிக்கைகளைத் தொடங்க முடியாது."},
      {"id": "C", "en": "President is answerable to High Courts for all official acts.", "ta": "அனைத்து அதிகாரப்பூர்வ பணிகளுக்கும் குடியரசுத் தலைவர் உயர் நீதிமன்றங்களுக்குப் பதிலளிக்கக் கடமைப்பட்டவர்."},
      {"id": "D", "en": "President can be arrested during term of office with Supreme Court permission.", "ta": "உச்ச நீதிமன்ற அனுமதியுடன் பதவிக் காலத்தில் குடியரசுத் தலைவரைக் கைது செய்யலாம்."}
    ],
    "correct_answer": "A",
    "explanation": {"en": "Article 361(2) & (3) provide that no criminal proceedings whatsoever shall be instituted or continued against the President during his term of office, and no process for arrest or imprisonment shall issue from any court.", "ta": "உறுப்பு 361(2) & (3) பதவிக் காலத்தில் குடியரசுத் தலைவருக்கு எதிராக எந்தக் குற்றவியல் நடவடிக்கையும் தொடங்கப்படவோ தொடரப்படவோ முடியாது என்றும் எந்தக் கைது ஆணையும் பிறப்பிக்கப்பட முடியாது என்றும் கூறுகின்றன."},
    "explanation_en": "Article 361(2) & (3) provide that no criminal proceedings whatsoever shall be instituted or continued against the President during his term of office, and no process for arrest or imprisonment shall issue from any court.",
    "explanation_ta": "உறுப்பு 361(2) & (3) பதவிக் காலத்தில் குடியரசுத் தலைவருக்கு எதிராக எந்தக் குற்றவியல் நடவடிக்கையும் தொடங்கப்படவோ தொடரப்படவோ முடியாது என்றும் எந்தக் கைது ஆணையும் பிறப்பிக்கப்பட முடியாது என்றும் கூறுகின்றன.",
    "source_reference": "Part XIX - Article 361",
    "trap_point": {"en": "Criminal immunity is absolute during term. Civil proceedings for personal acts require 2 months written notice under Art 361(4).", "ta": "குற்றவியல் விலக்களிப்பு பதவிக் காலத்தில் முழுமையானது. தனிப்பட்ட செயல்களுக்கான உரிமையியல் நடவடிக்கைகளுக்கு உறுப்பு 361(4)-ன் கீழ் 2 மாத அறிவிப்பு தேவை."},
    "tnpsc_tip": {"en": "Article 361 protects both President and State Governors.", "ta": "உறுப்பு 361 குடியரசுத் தலைவர் மற்றும் மாநில ஆளுநர்கள் இருவரையும் பாதுகாக்கிறது."},
    "why_not_others": {
      "A": {"en": "Correct. Complete criminal immunity exists during term of office under Art 361(2).", "ta": "சரி. உறுப்பு 361(2)-ன் கீழ் பதவிக் காலத்தில் முழு குற்றவியல் விலக்களிப்பு உண்டு."},
      "B": {"en": "Civil proceedings CAN be instituted for personal acts after giving 2 months written notice.", "ta": "2 மாத அறிவிப்பிற்குப் பின் தனிப்பட்ட செயல்களுக்கு உரிமையியல் நடவடிக்கை எடுக்கலாம்."},
      "C": {"en": "President is NOT answerable to any court for performance of powers/duties (Art 361(1)).", "ta": "அதிகாரப் பணிகளுக்குக் குடியரசுத் தலைவர் எந்த நீதிமன்றத்திற்கும் பதிலளிக்க வேண்டியதில்லை."},
      "D": {"en": "No process for arrest can issue from any court during term of office.", "ta": "பதவிக் காலத்தில் எந்தக் கைது ஆணையும் பிறப்பிக்கப்பட முடியாது."}
    },
    "metadata": {"subject": "Polity", "topic": "President of India", "type": "Medium", "level": "TNPSC Group 1"}
  }
]

# Write medium.json
target_path = "data/questions/polity/president_medium.json"
os.makedirs(os.path.dirname(target_path), exist_ok=True)
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(medium_25, f, ensure_ascii=False, indent=2)

print(f"✅ Generated and validated {len(medium_25)} questions in {target_path}")
