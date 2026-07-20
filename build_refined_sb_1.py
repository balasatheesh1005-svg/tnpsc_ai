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

# =========================================================
# 10 TWO STATEMENT QUESTIONS (HB_SB_001 to HB_SB_010)
# =========================================================

# HB_SB_001
questions.append(make_q(
    "HB_SB_001", "Statement Based",
    "With reference to the Regulating Act of 1773 and the Amending Act of 1781, consider the following statements:\n1. The Regulating Act 1773 established an Executive Council of four members to assist the Governor-General of Bengal, with decisions taken by majority vote.\n2. The Amending Act 1781 expanded the jurisdiction of the Supreme Court at Calcutta to include all revenue collection matters across Bengal, Bihar, and Orissa.\nWhich of the statements given above is/are correct?",
    "1773 ஒழுங்குமுறைச் சட்டம் மற்றும் 1781 திருத்தச் சட்டம் ஆகியவற்றைக் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1773 ஒழுங்குமுறைச் சட்டம் வங்காள கவர்னர் ஜெனரலுக்கு உதவ நான்கு உறுப்பினர்களைக் கொண்ட நிர்வாகக் குழுவை அமைத்தது, முடிவுகள் பெரும்பான்மை வாக்களிப்பால் எடுக்கப்பட்டன.\n2. 1781 திருத்தச் சட்டம் கொல்கத்தா உச்ச நீதிமன்றத்தின் அதிகார வரம்பை விரிவுபடுத்தி வங்காளம், பீகார், ஒரிசா முழுவதிலும் உள்ள அனைத்து வருவாய் வசூல் விவகாரங்களையும் அதில் சேர்த்தது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "A",
    "Statement 1 is correct (1773 Act created 4-member council with majority voting). Statement 2 is INCORRECT because the Amending Act 1781 (Act of Settlement) EXEMPTED revenue matters and revenue collection acts from Supreme Court jurisdiction.",
    "கூற்று 1 சரி (4 உறுப்பினர்கள் கொண்ட நிர்வாகக் குழு, பெரும்பான்மை முடிவுகள்). கூற்று 2 தவறு, ஏனெனில் 1781 திருத்தச் சட்டம் வருவாய் விவகாரங்களை உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து விலக்கியது (விரிவுபடுத்தவில்லை).",
    "Correct. Statement 1 is true; Statement 2 is false.",
    "சரி. கூற்று 1 சரி; கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is correct.",
    "தவறு. கூற்று 1 சரியானது.",
    "TNPSC Trap: Amending Act 1781 EXEMPTED revenue collection from Supreme Court jurisdiction (did not expand it).",
    "TNPSC பொறி: 1781 திருத்தச் சட்டம் வருவாய் வசூலை உச்ச நீதிமன்ற அதிகார வரம்பிலிருந்து விலக்கியது (விரிவுபடுத்தவில்லை).",
    "Warren Hastings was the first Governor-General of Bengal under the 1773 Regulating Act.",
    "1773 ஒழுங்குமுறைச் சட்டப்படி வாரன் ஹேஸ்டிங்ஸ் வங்காளத்தின் முதல் கவர்னர் ஜெனரலானார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Regulating Act 1773", "Amending Act 1781"]
))

# HB_SB_002
questions.append(make_q(
    "HB_SB_002", "Statement Based",
    "With reference to Pitt's India Act of 1784 and Charter Act of 1793, consider the following statements:\n1. Pitt's India Act 1784 established a Board of Control of six Privy Councillors to superintend political and military affairs of British possessions in India.\n2. The Charter Act 1793 mandated that the Commander-in-Chief was automatically an ex-officio member of the Governor-General's Council in all circumstances.\nWhich of the statements given above is/are correct?",
    "1784 பிட் இந்தியச் சட்டம் மற்றும் 1793 சாசனச் சட்டம் ஆகியவற்றைக் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1784 பிட் இந்தியச் சட்டம் இந்தியாவில் உள்ள பிரிட்டிஷ் உடமைகளின் அரசியல், இராணுவ விவகாரங்களைக் கண்காணிக்க 6 உறுப்பினர்கள் கொண்ட கட்டுப்பாட்டு வாரியத்தை நிறுவியது.\n2. 1793 சாசனச் சட்டம் அனைத்து சூழ்நிலைகளிலும் தளபதியை (Commander-in-Chief) கவர்னர் ஜெனரல் கவுன்சிலின் இயல்பான உறுப்பினராகத் தானாகவே கட்டாயப்படுத்தியது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "A",
    "Statement 1 is correct (Board of Control created with 6 members). Statement 2 is INCORRECT because the 1793 Act laid down that the Commander-in-Chief was NOT to be a member of GG Council unless specifically appointed by Court of Directors.",
    "கூற்று 1 சரி (6 உறுப்பினர்கள் கட்டுப்பாட்டு வாரியம்). கூற்று 2 தவறு, ஏனெனில் 1793 சட்டம் இயக்குநர்கள் அவையால் சிறப்பாக நியமிக்கப்பட்டால் ஒழிய தளபதி தானாக கவுன்சில் உறுப்பினராக முடியாது எனக் கூறியது.",
    "Correct. Statement 1 is true; Statement 2 is false.",
    "சரி. கூற்று 1 சரி; கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is correct.",
    "தவறு. கூற்று 1 சரியானது.",
    "TNPSC Trap: 1793 Act explicitly barred Commander-in-Chief from being ex-officio member of GG Council unless specifically nominated.",
    "TNPSC பொறி: 1793 சட்டம் தளபதி தானாகவே கவுன்சில் உறுப்பினராக இருப்பதைத் தடுத்தது.",
    "Pitt's India Act 1784 referred to EIC territories as 'British Possessions in India' for the first time.",
    "1784 பிட் இந்தியச் சட்டம் முதன்முறையாக கம்பெனி நிலப்பரப்புகளை 'இந்தியாவில் உள்ள பிரிட்டிஷ் உடமைகள்' எனக் குறிப்பிட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Pitt's India Act 1784", "Charter Act 1793"]
))

# HB_SB_003
questions.append(make_q(
    "HB_SB_003", "Statement Based",
    "With reference to the trade monopoly of the East India Company, consider the following statements:\n1. The Charter Act of 1813 abolished the Company's trade monopoly in India, but retained its monopoly in Tea trade and trade with China.\n2. The Charter Act of 1833 ended all commercial trading activities of the East India Company without exception, making it a purely administrative body.\nWhich of the statements given above is/are correct?",
    "கிழக்கிந்தியக் கம்பெனியின் வர்த்தக ஏகபோகம் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1813 சாசனச் சட்டம் தேயிலை வர்த்தகம் மற்றும் சீனாவுடனான வர்த்தகம் தவிர இந்தியாவில் கம்பெனியின் வர்த்தக ஏகபோகத்தை ஒழித்தது.\n2. 1833 சாசனச் சட்டம் எந்தவிலக்கும் இன்றி கம்பெனியின் அனைத்து வர்த்தக நடவடிக்கைகளையும் முடிவுக்குக் கொண்டுவந்து அதைத் தூய நிர்வாக அமைப்பாக மாற்றியது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "C",
    "Both statements are correct. 1813 Charter Act ended Indian trade monopoly except Tea and China trade; 1833 Charter Act ended ALL commercial activities completely, making EIC a purely administrative trustee.",
    "இரண்டு கூற்றுகளும் சரியானவை. 1813 சட்டம் தேயிலை/சீனா தவிர ஏகபோகத்தை ஒழித்தது; 1833 சட்டம் அனைத்து வர்த்தகத்தையும் ஒழித்து கம்பெனியைத் தூய நிர்வாக அமைப்பாக்கியது.",
    "Incorrect. Statement 2 is also correct.",
    "தவறு. கூற்று 2-ம் சரியானது.",
    "Incorrect. Statement 1 is also correct.",
    "தவறு. கூற்று 1-ம் சரியானது.",
    "Correct. Both Statements 1 and 2 are historically true.",
    "சரி. கூற்றுகள் 1 மற்றும் 2 இரண்டும் உண்மை.",
    "Incorrect. Both statements are correct.",
    "தவறு. இரண்டு கூற்றுகளும் சரியானவை.",
    "1833 Act stated that Company's territorial holdings were held 'in trust for His Majesty, His Heirs and Successors'.",
    "1833 சட்டம் கம்பெனியின் பகுதிகள் 'மன்னரின் நம்பிக்கைப் பொறுப்பில் (trust)' வைக்கப்பட்டுள்ளதாக அறிவித்தது.",
    "Charter Act 1813 allocated Rs 1 Lakh annually for education in India.",
    "1813 சாசனச் சட்டம் இந்தியாவில் கல்விக்காக ஆண்டிற்கு ரூ. 1 லட்சம் ஒதுக்கியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Charter Act 1813", "Charter Act 1833"]
))

# HB_SB_004
questions.append(make_q(
    "HB_SB_004", "Statement Based",
    "With reference to law-making members in the Governor-General's Council, consider the following statements:\n1. The Charter Act of 1833 introduced Lord Macaulay as a full executive member of the Governor-General's Council with voting rights on all administrative matters.\n2. The Charter Act of 1853 introduced an open competitive examination system for Indian Civil Services recruitment based on the Macaulay Committee report (1854).\nWhich of the statements given above is/are correct?",
    "கவர்னர் ஜெனரல் கவுன்சிலில் சட்ட உறுப்பினர்கள் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1833 சாசனச் சட்டம் லார்ட் மெக்காலேயை கவர்னர் ஜெனரல் கவுன்சிலின் அனைத்து நிர்வாக விவகாரங்களிலும் வாக்களிக்கும் அதிகாரம் கொண்ட முழு நிர்வாக உறுப்பினராகச் சேர்த்தது.\n2. 1853 சாசனச் சட்டம் மெக்காலே குழு அறிக்கையின் (1854) அடிப்படையில் இந்திய குடிமைப் பணி ஆட்சேர்ப்புக்கு திறந்தவெளிப் போட்டித் தேர்வு முறையை அறிமுகப்படுத்தியது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "B",
    "Statement 1 is INCORRECT because in 1833 Lord Macaulay was added as a Law Member WITHOUT full executive voting rights (he voted only on law-making). Statement 2 is correct (open competition instituted in 1853, Macaulay Comm 1854).",
    "கூற்று 1 தவறு, ஏனெனில் 1833 இல் மெக்காலே சட்ட உறுப்பினராக மட்டுமே சேர்க்கப்பட்டார், அவருக்கு முழு நிர்வாக வாக்களிப்பு உரிமை இல்லை. கூற்று 2 சரி (1853 போட்டித் தேர்வு, 1854 மெக்காலே குழு).",
    "Incorrect. Statement 1 is false.",
    "தவறு. கூற்று 1 தவறானது.",
    "Correct. Statement 2 is true; Statement 1 is false.",
    "சரி. கூற்று 2 சரி; கூற்று 1 தவறானது.",
    "Incorrect. Statement 1 is false.",
    "தவறு. கூற்று 1 தவறானது.",
    "Incorrect. Statement 2 is correct.",
    "தவறு. கூற்று 2 சரியானது.",
    "TNPSC Trap: 1833 Law Member (Macaulay) did NOT have voting rights on general executive business; he only sat during law framing.",
    "TNPSC பொறி: 1833 சட்ட உறுப்பினருக்கு பொது நிர்வாக விவகாரங்களில் வாக்களிக்கும் உரிமை இல்லை.",
    "1853 Act separated legislative and executive functions of GG Council by creating 6-member Indian Legislative Council.",
    "1853 சட்டம் 6 உறுப்பினர்கள் கொண்ட சட்டமன்ற கவுன்சிலை உருவாக்கி சட்டமன்ற/நிர்வாகப் பணிகளைப் பிரித்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Charter Act 1833", "Charter Act 1853"]
))

# HB_SB_005
questions.append(make_q(
    "HB_SB_005", "Statement Based",
    "With reference to the Government of India Act 1858 and Indian Councils Act 1861, consider the following statements:\n1. The Government of India Act 1858 created the office of Secretary of State for India assisted by a 15-member advisory Council of India based in London.\n2. The Indian Councils Act 1861 empowered the Viceroy to issue Ordinances during emergencies with a validity period of one year.\nWhich of the statements given above is/are correct?",
    "1858 இந்திய அரசுச் சட்டம் மற்றும் 1861 இந்தியக் கவுன்சில்கள் சட்டம் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1858 இந்திய அரசுச் சட்டம் லண்டனைத் தலைமையகமாகக் கொண்டு 15 உறுப்பினர்கள் கொண்ட ஆலோசனைக் குழுவுடன் கூடிய இந்திய அரசுச் செயலாளர் பதவியை உருவாக்கியது.\n2. 1861 இந்தியக் கவுன்சில்கள் சட்டம் அவசரகாலத்தில் ஒரு வருடம் செல்லுபடியாகும் அவசரச்சட்டங்களை பிறப்பிக்க வைஸ்ராய்க்கு அதிகாரமளித்தது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "A",
    "Statement 1 is correct (1858 Act created Secretary of State with 15-member Council of India). Statement 2 is INCORRECT because Ordinance validity under 1861 Act was SIX MONTHS, not one year.",
    "கூற்று 1 சரி (1858 சட்டம் 15 உறுப்பினர்கள் கொண்ட கவுன்சிலுடன் அரசுச் செயலாளரை உருவாக்கியது). கூற்று 2 தவறு, ஏனெனில் 1861 சட்டப்படி வைஸ்ராய் அவசரச்சட்டம் 6 மாதங்கள் மட்டுமே செல்லுபடியாகும்.",
    "Correct. Statement 1 is true; Statement 2 is false.",
    "சரி. கூற்று 1 சரி; கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is correct.",
    "தவறு. கூற்று 1 சரியானது.",
    "TNPSC Trap: Ordinance validity under 1861 Act was 6 MONTHS (not 1 year).",
    "TNPSC பொறி: 1861 சட்டப்படி வைஸ்ராய் அவசரச்சட்டத்தின் செல்லுபடியாகும் காலம் 6 மாதங்கள் (1 வருடம் அல்ல).",
    "Lord Canning was the first Viceroy under 1858 Act and legalized Portfolio system in 1861 Act.",
    "கேனிங் பிரபு 1858 சட்டப்படி முதல் வைஸ்ராயானார்; 1861 சட்டத்தில் துறை ஒதுக்கீடு முறையை சட்டப்பூர்வமாக்கினார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1858", "Indian Councils Act 1861"]
))

# HB_SB_006
questions.append(make_q(
    "HB_SB_006", "Statement Based",
    "With reference to electoral representation in British India, consider the following statements:\n1. The Indian Councils Act 1892 explicitly introduced the word 'ELECTION' for the first time in the statutory text.\n2. The Indian Councils Act 1909 introduced separate electorates for Muslims, where Muslim members were elected exclusively by Muslim voters.\nWhich of the statements given above is/are correct?",
    "பிரிட்டிஷ் இந்தியாவில் தேர்தல் பிரதிநிதித்துவம் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1892 இந்தியக் கவுன்சில்கள் சட்டம் முதன்முறையாக 'தேர்தல்' என்ற சொல்லை சட்ட உரையில் வெளிப்படையாக அறிமுகப்படுத்தியது.\n2. 1909 இந்தியக் கவுன்சில்கள் சட்டம் முஸ்லிம்களுக்குத் தனித் தொகுதிகளை அறிமுகப்படுத்தியது, அங்கு முஸ்லிம் உறுப்பினர்கள் முஸ்லிம் வாக்காளர்களால் மட்டுமே தேர்ந்தெடுக்கப்பட்டனர்.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "B",
    "Statement 1 is INCORRECT because the word 'election' was carefully avoided in 1892 Act text (described as recommendation). Statement 2 is correct (Morley-Minto reforms established Muslim separate electorates).",
    "கூற்று 1 தவறு, ஏனெனில் 1892 சட்ட உரையில் 'தேர்தல்' என்ற சொல் தவிர்க்கப்பட்டது (பரிந்துரை என்றே கூறப்பட்டது). கூற்று 2 சரி (1909 மோர்லே-மிண்டோ சட்டம் முஸ்லிம் தனித் தொகுதியை அமைத்தது).",
    "Incorrect. Statement 1 is false.",
    "தவறு. கூற்று 1 தவறானது.",
    "Correct. Statement 2 is true; Statement 1 is false.",
    "சரி. கூற்று 2 சரி; கூற்று 1 தவறானது.",
    "Incorrect. Statement 1 is false.",
    "தவறு. கூற்று 1 தவறானது.",
    "Incorrect. Statement 2 is correct.",
    "தவறு. கூற்று 2 சரியானது.",
    "TNPSC Trap: 1892 Act introduced an indirect recommendation element, but the word 'ELECTION' was avoided.",
    "TNPSC பொறி: 1892 சட்டம் மறைமுகத் தேர்தல் கூறைக் கொண்டு வந்தாலும் 'தேர்தல்' என்ற சொல் தவிர்க்கப்பட்டது.",
    "Lord Minto came to be known as the 'Father of Communal Electorate'.",
    "லார்ட் மிண்டோ 'வகுப்புவாதத் தொகுதிகளின் தந்தை' என அழைக்கப்பட்டார்.",
    "Analyze", 75, ["Polity", "Historical Background", "Indian Councils Act 1892", "Indian Councils Act 1909"]
))

# HB_SB_007
questions.append(make_q(
    "HB_SB_007", "Statement Based",
    "With reference to the constitutional structure under Government of India Acts 1919 and 1935, consider the following statements:\n1. The Government of India Act 1919 introduced Dyarchy at the Central level, leaving provincial administration unified.\n2. The Government of India Act 1935 introduced Provincial Autonomy in place of Provincial Dyarchy.\nWhich of the statements given above is/are correct?",
    "1919 மற்றும் 1935 இந்திய அரசுச் சட்டங்களின் கீழ் அரசியலமைப்பு கட்டமைப்பு குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1919 இந்திய அரசுச் சட்டம் மத்திய மட்டத்தில் இரட்டை ஆட்சியை அறிமுகப்படுத்தி மாகாண நிர்வாகத்தை ஒருங்கிணைத்து வைத்தது.\n2. 1935 இந்திய அரசுச் சட்டம் மாகாண இரட்டை ஆட்சிக்கு பதிலாக மாகாண தன்னாட்சியை அறிமுகப்படுத்தியது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "B",
    "Statement 1 is INCORRECT because GOI Act 1919 introduced Dyarchy in PROVINCES (not Centre). Statement 2 is correct (1935 Act replaced Provincial Dyarchy with Provincial Autonomy).",
    "கூற்று 1 தவறு, ஏனெனில் 1919 சட்டம் மாகாணங்களில்தான் இரட்டை ஆட்சியை கொண்டு வந்தது (மத்தியில் அல்ல). கூற்று 2 சரி (1935 சட்டம் மாகாண இரட்டை ஆட்சியை ஒழித்து மாகாண தன்னாட்சியை கொண்டு வந்தது).",
    "Incorrect. Statement 1 is false.",
    "தவறு. கூற்று 1 தவறானது.",
    "Correct. Statement 2 is true; Statement 1 is false.",
    "சரி. கூற்று 2 சரி; கூற்று 1 தவறானது.",
    "Incorrect. Statement 1 is false.",
    "தவறு. கூற்று 1 தவறானது.",
    "Incorrect. Statement 2 is correct.",
    "தவறு. கூற்று 2 சரியானது.",
    "TNPSC Trap: 1919 Act = Dyarchy in PROVINCES; 1935 Act = Dyarchy proposed at CENTRE (and Provincial Autonomy implemented).",
    "TNPSC பொறி: 1919 சட்டம் = மாகாணங்களில் இரட்டை ஆட்சி; 1935 சட்டம் = மத்தியில் இரட்டை ஆட்சி உத்தேசம் & மாகாண தன்னாட்சி அமல்.",
    "Provincial Autonomy came into operation in April 1937 under the 1935 Act.",
    "மாகாண தன்னாட்சி 1935 சட்டப்படி 1937 ஏப்ரலில் அமலுக்கு வந்தது.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1919", "Government of India Act 1935"]
))

# HB_SB_008
questions.append(make_q(
    "HB_SB_008", "Statement Based",
    "With reference to legislative powers under Government of India Act 1935 and Indian Independence Act 1947, consider the following statements:\n1. The Government of India Act 1935 assigned Residuary legislative powers exclusively to the Federal Legislature.\n2. Section 6 of the Indian Independence Act 1947 empowered the Constituent Assembly to alter or repeal any Act of British Parliament applying to India.\nWhich of the statements given above is/are correct?",
    "1935 இந்திய அரசுச் சட்டம் மற்றும் 1947 சுதந்திரச் சட்டத்தின் கீழ் சட்ட அதிகாரங்கள் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1935 இந்திய அரசுச் சட்டம் எஞ்சிய சட்ட அதிகாரங்களை கூட்டாட்சி சட்டமன்றத்திற்கு மட்டுமே ஒப்படைத்தது.\n2. 1947 இந்திய சுதந்திரச் சட்டத்தின் பிரிவு 6 இந்தியாவில் பொருந்தும் எந்தவொரு பிரிட்டிஷ் பாராளுமன்ற சட்டத்தையும் மாற்ற அல்லது ரத்து செய்ய அரசியலமைப்பு சபைக்கு அதிகாரமளித்தது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "B",
    "Statement 1 is INCORRECT because Residuary legislative powers under 1935 Act were given to the Governor-General (Viceroy), NOT to the Federal Legislature. Statement 2 is correct (Section 6 granted Assembly full repeal power).",
    "கூற்று 1 தவறு, ஏனெனில் 1935 சட்டத்தில் எஞ்சிய அதிகாரங்கள் வைஸ்ராயிடம் இருந்தன (கூட்டாட்சி சட்டமன்றத்திடம் அல்ல). கூற்று 2 சரி (பிரிவு 6 அரசியலமைப்பு சபைக்கு ரத்து செய்யும் அதிகாரம் அளித்தது).",
    "Incorrect. Statement 1 is false.",
    "தவறு. கூற்று 1 தவறானது.",
    "Correct. Statement 2 is true; Statement 1 is false.",
    "சரி. கூற்று 2 சரி; கூற்று 1 தவறானது.",
    "Incorrect. Statement 1 is false.",
    "தவறு. கூற்று 1 தவறானது.",
    "Incorrect. Statement 2 is correct.",
    "தவறு. கூற்று 2 சரியானது.",
    "TNPSC Trap: In 1935 Act, Residuary powers = Governor-General. In 1950 Constitution, Residuary powers = Parliament (Article 248).",
    "TNPSC பொறி: 1935 சட்டத்தில் எஞ்சிய அதிகாரங்கள் = கவர்னர் ஜெனரல். 1950 அரசியலமைப்பில் எஞ்சிய அதிகாரங்கள் = பாராளுமன்றம் (பிரிவு 248).",
    "Indian Independence Act 1947 received Royal Assent on July 18, 1947.",
    "1947 இந்திய சுதந்திரச் சட்டம் 1947 ஜூலை 18 அன்று அரச ஒப்புதலைப் பெற்றது.",
    "Analyze", 75, ["Polity", "Historical Background", "Government of India Act 1935", "Indian Independence Act 1947"]
))

# HB_SB_009
questions.append(make_q(
    "HB_SB_009", "Statement Based",
    "With reference to the administrative transition from Company Rule to Crown Rule, consider the following statements:\n1. Company Rule (1773-1858) was characterized by parliamentary regulation through 20-year Charter Acts.\n2. Crown Rule (1858-1947) mandated that the salary and expenses of the Secretary of State for India be paid out of the British Home Treasury right from 1858.\nWhich of the statements given above is/are correct?",
    "கம்பெனி ஆட்சியிலிருந்து முடிஅரசு ஆட்சிக்கு ஏற்பட்ட நிர்வாக மாற்றம் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. கம்பெனி ஆட்சி (1773-1858) 20 ஆண்டு சாசனச் சட்டங்கள் மூலம் பாராளுமன்ற ஒழுங்குமுறையால் வகைப்படுத்தப்பட்டது.\n2. முடிஅரசு ஆட்சி (1858-1947) 1858 முதலே இந்திய அரசுச் செயலாளரின் சம்பளம் மற்றும் செலவுகள் பிரிட்டிஷ் கருவூலத்திலிருந்து வழங்கப்பட வேண்டும் எனக் கட்டாயப்படுத்தியது.\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "A",
    "Statement 1 is correct (Company Rule renewed via 20-year Charters). Statement 2 is INCORRECT because Secretary of State salaries were charged on INDIAN REVENUES from 1858 until the Government of India Act 1919 shifted it to British Treasury.",
    "கூற்று 1 சரி (20 ஆண்டு சாசனச் சட்டங்கள் புதுப்பிப்பு). கூற்று 2 தவறு, ஏனெனில் அரசுச் செயலாளர் சம்பளம் 1858 முதல் 1919 வரை இந்திய வருவாயிலிருந்தே வழங்கப்பட்டது (பிரிட்டிஷ் கருவூலத்திலிருந்து அல்ல).",
    "Correct. Statement 1 is true; Statement 2 is false.",
    "சரி. கூற்று 1 சரி; கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 2 is false.",
    "தவறு. கூற்று 2 தவறானது.",
    "Incorrect. Statement 1 is correct.",
    "தவறு. கூற்று 1 சரியானது.",
    "TNPSC Trap: Secretary of State salaries were charged on Indian Revenues from 1858 to 1919 (shifted to British Treasury by 1919 Act).",
    "TNPSC பொறி: அரசுச் செயலாளர் சம்பளம் 1858 முதல் 1919 வரை இந்திய வருவாயில் சுமத்தப்பட்டது (1919 இல் பிரிட்டிஷ் கருவூலத்திற்கு மாற்றப்பட்டது).",
    "Government of India Act 1858 was called the 'Act for Good Government of India'.",
    "1858 இந்திய அரசுச் சட்டம் 'இந்தியாவின் நல்லாட்சிக்கான சட்டம்' எனப்பட்டது.",
    "Analyze", 75, ["Polity", "Historical Background", "Company Rule vs Crown Rule", "Drain of Wealth"]
))

# HB_SB_010
questions.append(make_q(
    "HB_SB_010", "Statement Based",
    "With reference to the Constituent Assembly background and Indian Independence Act 1947, consider the following statements:\n1. All 389 members of the Constituent Assembly formed in November 1946 were directly elected by universal adult franchise.\n2. Under the Indian Independence Act 1947, the Constituent Assembly performed dual functions: a Constitution-making body (headed by Dr. Rajendra Prasad) and an ordinary legislative body (headed by G.V. Mavlankar).\nWhich of the statements given above is/are correct?",
    "அரசியலமைப்பு சபையின் பின்னணி மற்றும் 1947 இந்திய சுதந்திரச் சட்டம் குறித்து பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. நவம்பர் 1946 இல் அமைக்கப்பட்ட அரசியலமைப்பு சபையின் 389 உறுப்பினர்களும் உலகளாவிய வயதுவந்தோர் வாக்குரிமை மூலம் நேரடியாகத் தேர்ந்தெடுக்கப்பட்டனர்.\n2. 1947 இந்திய சுதந்திரச் சட்டத்தின் கீழ் அரசியலமைப்பு சபை இரு பணிகளைச் செய்தது: அரசியலமைப்பு உருவாக்கம் (தலைவர்: ராஜேந்திர பிரசாத்) மற்றும் சாதாரண சட்டமன்ற பணி (தலைவர்: ஜி.வி. மாவ்லங்கர்).\nஎது சரி?",
    "1 only", "1 மட்டும்",
    "2 only", "2 மட்டும்",
    "Both 1 and 2", "1 மற்றும் 2 இரண்டும்",
    "Neither 1 nor 2", "1 மற்றும் 2 இரண்டும் இல்லை",
    "B",
    "Statement 1 is INCORRECT because Constituent Assembly members were NOT directly elected by adult franchise (British Indian seats were indirectly elected by provincial assemblies, and Princely State seats were nominated). Statement 2 is correct (dual roles under 1947 Act).",
    "கூற்று 1 தவறு, ஏனெனில் சபை உறுப்பினர்கள் நேரடி வாக்குரிமையால் தேர்ந்தெடுக்கப்படவில்லை (மறைமுகத் தேர்தல் & நியமனம்). கூற்று 2 சரி (1947 சட்டப்படி இரு பணிகள்).",
    "Incorrect. Statement 1 is false.",
    "தவறு. கூற்று 1 தவறானது.",
    "Correct. Statement 2 is true; Statement 1 is false.",
    "சரி. கூற்று 2 சரி; கூற்று 1 தவறானது.",
    "Incorrect. Statement 1 is false.",
    "தவறு. கூற்று 1 தவறானது.",
    "Incorrect. Statement 2 is correct.",
    "தவறு. கூற்று 2 சரியானது.",
    "TNPSC Trap: Constituent Assembly was a partly elected and partly nominated body.",
    "TNPSC பொறி: அரசியலமைப்பு சபை பகுதி அளவு தேர்ந்தெடுக்கப்பட்ட மற்றும் பகுதி அளவு நியமிக்கப்பட்ட அமைப்பாகும்.",
    "Constituent Assembly held its first meeting on December 9, 1946.",
    "அரசியலமைப்பு சபை தனது முதல் கூட்டத்தை 1946 டிசம்பர் 9 அன்று நடத்தியது.",
    "Analyze", 75, ["Polity", "Historical Background", "Constituent Assembly Background", "Indian Independence Act 1947"]
))

# Save part 1
with open(target_path, "w", encoding="utf-8") as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Refined Part 1 complete: {len(questions)} Two-Statement questions saved.")
