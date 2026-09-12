# -*- coding: utf-8 -*-
"""
Builder for Inter-State Relations Match the Following MCQs (25 questions: ISR_MF_001 to ISR_MF_025)
"""
import json
import os
from pathlib import Path
from collections import Counter
from tools.nova_content_engine.validator import ContentValidator

def make_mf(qid, diff, stem_en, stem_ta,
            opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta,
            correct_ans, exp_en, exp_ta,
            wno_a_en, wno_a_ta, wno_b_en, wno_b_ta, wno_c_en, wno_c_ta, wno_d_en, wno_d_ta,
            tip_en, tip_ta, rev_en, rev_ta, bloom="Analyze", est_time=80, tags=None):
    return {
        "id": qid,
        "subject": "Polity",
        "topic": "Inter-State Relations",
        "difficulty": diff,
        "question_type": "Match the Following",
        "question": {"en": stem_en, "ta": stem_ta},
        "question_en": stem_en,
        "question_ta": stem_ta,
        "options": [
            {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
            {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
            {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
            {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
        ],
        "options_en": [opt_a_en, opt_b_en, opt_c_en, opt_d_en],
        "options_ta": [opt_a_ta, opt_b_ta, opt_c_ta, opt_d_ta],
        "correct_answer": correct_ans,
        "answer": correct_ans.lower(),
        "explanation": {"en": exp_en, "ta": exp_ta},
        "explanation_en": exp_en,
        "explanation_ta": exp_ta,
        "why_not_others": {
            "A": {"en": wno_a_en, "ta": wno_a_ta},
            "B": {"en": wno_b_en, "ta": wno_b_ta},
            "C": {"en": wno_c_en, "ta": wno_c_ta},
            "D": {"en": wno_d_en, "ta": wno_d_ta}
        },
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": rev_en, "ta": rev_ta},
        "source_reference": ["M. Laxmikanth - Indian Polity", "Constitution of India", "Samacheer Kalvi Class 12"],
        "bloom_level": bloom,
        "estimated_time_sec": est_time,
        "pyq_similarity": "High",
        "tags": tags or ["Inter-State Relations", "Match the Following", "List Matching"]
    }

def get_match_questions():
    q = []

    # 001 - Ans A
    q.append(make_mf(
        "ISR_MF_001", "Medium",
        "Match List-I (Water Disputes Tribunal) with List-II (Year of Constitution):\nList-I:\na) Krishna Water Disputes Tribunal-I\nb) Ravi and Beas Waters Tribunal\nc) Cauvery Water Disputes Tribunal\nd) Mahanadi Water Disputes Tribunal\n\nList-II:\n1. 1969\n2. 1986\n3. 1990\n4. 2018",
        "பட்டியல்-I (நதிநீர் தீர்ப்பாயம்) உடன் பட்டியல்-II (அமைக்கப்பட்ட ஆண்டு)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) முதல் கிருஷ்ணா நதிநீர் தீர்ப்பாயம்\nb) ராவி மற்றும் பியாஸ் நதிநீர் தீர்ப்பாயம்\nc) காவிரி நதிநீர் தகராறுகள் தீர்ப்பாயம்\nd) மகாநதி நதிநீர் தகராறுகள் தீர்ப்பாயம்\n\nபட்டியல்-II:\n1. 1969\n2. 1986\n3. 1990\n4. 2018",
        "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
        "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
        "a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4",
        "a-4, b-2, c-3, d-1", "a-4, b-2, c-3, d-1",
        "A",
        "The correct matching is: (a) Krishna-I was constituted in 1969; (b) Ravi-Beas was set up in 1986; (c) Cauvery was set up in 1990; (d) Mahanadi was constituted in 2018.",
        "சரியான பொருத்தம்: (a) முதல் கிருஷ்ணா தீர்ப்பாயம் = 1969; (b) ராவி-பியாஸ் தீர்ப்பாயம் = 1986; (c) காவிரி தீர்ப்பாயம் = 1990; (d) மகாநதி தீர்ப்பாயம் = 2018.",
        "Option A is correct because all four tribunals are paired with their exact constitution years.", "நான்கு தீர்ப்பாயங்களும் அமைக்கப்பட்ட ஆண்டுகளுடன் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் A சரி.",
        "Option B is incorrect because Krishna was 1969, not 1986.", "கிருஷ்ணா 1969 என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Cauvery was 1990, not 1986.", "காவிரி 1990 என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Mahanadi was 2018, not 1969.", "மகாநதி 2018 என்பதால் விருப்பம் D தவறு.",
        "Chronological anchor: Krishna (1969) -> Ravi-Beas (1986) -> Cauvery (1990) -> Mahanadi (2018).",
        "காலவரிசை நினைவூட்டல்: கிருஷ்ணா (1969) -> ராவி-பியாஸ் (1986) -> காவிரி (1990) -> மகாநதி (2018).",
        "Krishna (1969), Ravi-Beas (1986), Cauvery (1990), and Mahanadi (2018) tribunals reflect major water dispute milestones.",
        "கிருஷ்ணா (1969), ராவி-பியாஸ் (1986), காவிரி (1990), மகாநதி (2018) ஆகியவை நதிநீர் தீர்ப்பாயங்களின் முக்கிய மைல்கற்கள்.",
        tags=["Tribunals Matching", "Years of Constitution", "TNPSC Standard"]
    ))

    # 002 - Ans B
    q.append(make_mf(
        "ISR_MF_002", "Hard",
        "Match List-I (Water Disputes Tribunal) with List-II (Chairman):\nList-I:\na) Cauvery Water Disputes Tribunal\nb) Narmada Water Disputes Tribunal\nc) Krishna Water Disputes Tribunal-I\nd) Mahanadi Water Disputes Tribunal\n\nList-II:\n1. Justice V. Ramaswami\n2. Justice Chittatosh Mookerjee\n3. Justice A.M. Khanwilkar\n4. Justice R.S. Bachawat",
        "பட்டியல்-I (நதிநீர் தீர்ப்பாயம்) உடன் பட்டியல்-II (தலைவர்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) காவிரி நதிநீர் தகராறுகள் தீர்ப்பாயம்\nb) நர்மதா நதிநீர் தகராறுகள் தீர்ப்பாயம்\nc) முதல் கிருஷ்ணா நதிநீர் தீர்ப்பாயம்\nd) மகாநதி நதிநீர் தகராறுகள் தீர்ப்பாயம்\n\nபட்டியல்-II:\n1. நீதிபதி வி. ராமசுவாமி\n2. நீதிபதி சிட்டதோஷ் முகர்ஜி\n3. நீதிபதி ஏ.எம். கான்வில்கர்\n4. நீதிபதி ஆர்.எஸ். பச்சாவத்",
        "a-1, b-2, c-4, d-3", "a-1, b-2, c-4, d-3",
        "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
        "a-2, b-4, c-1, d-3", "a-2, b-4, c-1, d-3",
        "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
        "B",
        "The correct matching is: (a) Cauvery Tribunal (1990) was chaired by Justice Chittatosh Mookerjee (2); (b) Narmada Tribunal (1969) was chaired by Justice V. Ramaswami (1); (c) Krishna Tribunal-I (1969) was chaired by Justice R.S. Bachawat (4); (d) Mahanadi Tribunal (2018) was chaired by Justice A.M. Khanwilkar (3).",
        "சரியான பொருத்தம்: (a) காவிரி தீர்ப்பாயம் = நீதிபதி சிட்டதோஷ் முகர்ஜி (2); (b) நர்மதா தீர்ப்பாயம் = நீதிபதி வி. ராமசுவாமி (1); (c) முதல் கிருஷ்ணா தீர்ப்பாயம் = நீதிபதி ஆர்.எஸ். பச்சாவத் (4); (d) மகாநதி தீர்ப்பாயம் = நீதிபதி ஏ.எம். கான்வில்கர் (3).",
        "Option A is incorrect because Cauvery was headed by Mookerjee, not Ramaswami.", "காவிரி தீர்ப்பாயத் தலைவர் முகர்ஜி என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because all four chairpersons are precisely matched.", "நான்கு தலைவர்களும் சரியாகப் பொருத்தப்பட்டுள்ளதால் விருப்பம் B சரி.",
        "Option C is incorrect because Narmada was Ramaswami, not Bachawat.", "நர்மதா தீர்ப்பாயத் தலைவர் ராமசுவாமி என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Cauvery was not headed by Khanwilkar.", "காவிரி தீர்ப்பாயத் தலைவர் கான்வில்கர் அல்ல என்பதால் விருப்பம் D தவறு.",
        "Key chairpersons: Cauvery = Mookerjee; Narmada = Ramaswami; Krishna-I = Bachawat; Mahanadi = Khanwilkar.",
        "முக்கிய தலைவர்கள்: காவிரி = முகர்ஜி; நர்மதா = ராமசுவாமி; கிருஷ்ணா-I = பச்சாவத்; மகாநதி = கான்வில்கர்.",
        "Judges Chittatosh Mookerjee, V. Ramaswami, R.S. Bachawat, and A.M. Khanwilkar chaired major water tribunals.",
        "நீதிபதிகள் சிட்டதோஷ் முகர்ஜி, வி. ராமசுவாமி, ஆர்.எஸ். பச்சாவத், ஏ.எம். கான்வில்கர் ஆகியோர் முக்கிய தீர்ப்பாயங்களுக்குத் தலைமை தாங்கினர்.",
        tags=["Tribunal Chairpersons", "List Matching", "Judicial Appointments"]
    ))

    # 003 - Ans C
    q.append(make_mf(
        "ISR_MF_003", "Easy",
        "Match List-I (Zonal Council) with List-II (Headquarters):\nList-I:\na) Northern Zonal Council\nb) Central Zonal Council\nc) Eastern Zonal Council\nd) Southern Zonal Council\n\nList-II:\n1. Prayagraj (Allahabad)\n2. New Delhi\n3. Chennai\n4. Kolkata",
        "பட்டியல்-I (மண்டலக் குழு) உடன் பட்டியல்-II (தலைமையகம்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) வடக்கு மண்டலக் குழு\nb) மத்திய மண்டலக் குழு\nc) கிழக்கு மண்டலக் குழு\nd) தெற்கு மண்டலக் குழு\n\nபட்டியல்-II:\n1. பிரயாக்ராஜ் (அலகாபாத்)\n2. புதுதில்லி\n3. சென்னை\n4. கொல்கத்தா",
        "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
        "a-2, b-4, c-1, d-3", "a-2, b-4, c-1, d-3",
        "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
        "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
        "C",
        "The correct matching is: (a) Northern Zonal Council = New Delhi (2); (b) Central Zonal Council = Prayagraj (1); (c) Eastern Zonal Council = Kolkata (4); (d) Southern Zonal Council = Chennai (3).",
        "சரியான பொருத்தம்: (a) வடக்கு மண்டலக் குழு = புதுதில்லி (2); (b) மத்திய மண்டலக் குழு = பிரயாக்ராஜ் (1); (c) கிழக்கு மண்டலக் குழு = கொல்கத்தா (4); (d) தெற்கு மண்டலக் குழு = சென்னை (3).",
        "Option A is incorrect because Northern HQ is New Delhi, not Prayagraj.", "வடக்கு தலைமையகம் புதுதில்லி என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Central HQ is Prayagraj, not Kolkata.", "மத்திய தலைமையகம் பிரயாக்ராஜ் என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because all four zonal councils are paired with their statutory headquarters.", "நான்கு மண்டலக் குழுக்களும் அவற்றின் தலைமையகங்களுடன் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் C சரி.",
        "Option D is incorrect because Southern HQ is Chennai, not New Delhi.", "தெற்கு தலைமையகம் சென்னை என்பதால் விருப்பம் D தவறு.",
        "Zonal Council HQs: North = New Delhi, Central = Prayagraj, East = Kolkata, South = Chennai, West = Mumbai.",
        "மண்டலத் தலைமையகங்கள்: வடக்கு = புதுதில்லி, மத்திய = பிரயாக்ராஜ், கிழக்கு = கொல்கத்தா, தெற்கு = சென்னை, மேற்கு = மும்பை.",
        "Zonal Councils are headquartered at New Delhi, Prayagraj, Kolkata, Mumbai, and Chennai.",
        "மண்டலக் குழுக்கள் புதுதில்லி, பிரயாக்ராஜ், கொல்கத்தா, மும்பை மற்றும் சென்னையில் தலைமையகங்களைக் கொண்டுள்ளன.",
        tags=["Zonal Councils HQ", "List Matching", "TNPSC Core"]
    ))

    # 004 - Ans D
    q.append(make_mf(
        "ISR_MF_004", "Medium",
        "Match List-I (Constitutional Article) with List-II (Subject Matter):\nList-I:\na) Article 261\nb) Article 262\nc) Article 263\nd) Article 279A\n\nList-II:\n1. Inter-State Council\n2. Goods and Services Tax Council\n3. Full Faith and Credit to Public Acts\n4. Adjudication of Inter-State Water Disputes",
        "பட்டியல்-I (அரசியலமைப்பு உறுப்பு) உடன் பட்டியல்-II (பொருள்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) உறுப்பு 261\nb) உறுப்பு 262\nc) உறுப்பு 263\nd) உறுப்பு 279A\n\nபட்டியல்-II:\n1. மாநிலங்களுக்கு இடையிலான மன்றம்\n2. சரக்கு மற்றும் சேவை வரி மன்றம்\n3. பொதுச் சட்டங்களுக்கு முழு நம்பிக்கையும் சான்றும்\n4. மாநிலங்களுக்கு இடையேயான நதிநீர் தகராறுகளைத் தீர்த்தல்",
        "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
        "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
        "a-4, b-3, c-1, d-2", "a-4, b-3, c-1, d-2",
        "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
        "D",
        "The correct matching is: (a) Article 261 = Full Faith and Credit (3); (b) Article 262 = Inter-State Water Disputes (4); (c) Article 263 = Inter-State Council (1); (d) Article 279A = Goods and Services Tax Council (2).",
        "சரியான பொருத்தம்: (a) உறுப்பு 261 = முழு நம்பிக்கையும் சான்றும் (3); (b) உறுப்பு 262 = நதிநீர் தகராறுகள் (4); (c) உறுப்பு 263 = மாநிலங்களுக்கு இடையிலான மன்றம் (1); (d) உறுப்பு 279A = ஜிஎஸ்டி மன்றம் (2).",
        "Option A is incorrect because Article 261 is not the Inter-State Council.", "உறுப்பு 261 மன்றம் அல்ல என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Article 262 is water disputes, not Article 263.", "உறுப்பு 262 நதிநீர் தகராறுகளுக்குரியது என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Article 261 is not water disputes.", "உறுப்பு 261 நதிநீர் தகராறுகளுக்குரியது அல்ல என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because all four constitutional articles are precisely paired.", "நான்கு அரசியலமைப்பு உறுப்புகளும் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் D சரி.",
        "Four cardinal federal articles: 261 (Full Faith), 262 (Water), 263 (ISC), 279A (GST Council).",
        "முக்கிய கூட்டாட்சி உறுப்புகள்: 261 (முழு நம்பிக்கை), 262 (நீர்), 263 (மன்றம்), 279A (ஜிஎஸ்டி மன்றம்).",
        "Articles 261, 262, 263, and 279A constitute the bedrock of inter-governmental coordination in India.",
        "உறுப்புகள் 261, 262, 263 மற்றும் 279A இந்தியாவில் அரசாங்கங்களுக்கு இடையேயான ஒருங்கிணைப்பின் அடித்தளமாகும்.",
        tags=["Constitutional Articles", "List Matching", "Federal Comity"]
    ))

    # 005 - Ans A
    q.append(make_mf(
        "ISR_MF_005", "Hard",
        "Match List-I (Part XIII Article) with List-II (Constitutional Rule):\nList-I:\na) Article 301\nb) Article 302\nc) Article 304(b)\nd) Article 307\n\nList-II:\n1. Freedom of trade, commerce, and intercourse throughout India\n2. Power of Parliament to impose restrictions in the public interest\n3. Previous sanction of President required for state trade bills\n4. Appointment of authority for carrying out purposes of Articles 301 to 304",
        "பட்டியல்-I (பகுதி XIII உறுப்பு) உடன் பட்டியல்-II (அரசியலமைப்பு விதி)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) உறுப்பு 301\nb) உறுப்பு 302\nc) உறுப்பு 304(b)\nd) உறுப்பு 307\n\nபட்டியல்-II:\n1. இந்தியா முழுவதும் வர்த்தகம், வணிகம் மற்றும் தொடர்பு சுதந்திரம்\n2. பொது நலன் கருதி கட்டுப்பாடுகளை விதிக்க நாடாளுமன்றத்திற்கு அதிகாரம்\n3. மாநில வர்த்தக மசோதாக்களுக்கு குடியரசுத் தலைவரின் முன் அனுமதி தேவை\n4. உறுப்புகள் 301 முதல் 304 வரையிலான நோக்கங்களைச் செயல்படுத்த அதிகார அமைப்பை நியமித்தல்",
        "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
        "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
        "a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4",
        "a-4, b-2, c-3, d-1", "a-4, b-2, c-3, d-1",
        "A",
        "The correct matching is: (a) Article 301 = Freedom of trade (1); (b) Article 302 = Parliamentary restrictions in public interest (2); (c) Article 304(b) = Prior sanction of President for state restrictions (3); (d) Article 307 = Appointment of trade authority (4).",
        "சரியான பொருத்தம்: (a) உறுப்பு 301 = வர்த்தக சுதந்திரம் (1); (b) உறுப்பு 302 = நாடாளுமன்ற பொது நலக் கட்டுப்பாடுகள் (2); (c) உறுப்பு 304(b) = குடியரசுத் தலைவரின் முன் அனுமதி (3); (d) உறுப்பு 307 = வர்த்தக அதிகார அமைப்பு நியமனம் (4).",
        "Option A is correct because each Part XIII article corresponds exactly to its constitutional mandate.", "பகுதி XIII-ன் ஒவ்வொரு உறுப்பும் அதன் விதியுடன் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் A சரி.",
        "Option B is incorrect because Article 301 is freedom of trade.", "உறுப்பு 301 வர்த்தக சுதந்திரம் என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Article 302 is Parliamentary power.", "உறுப்பு 302 நாடாளுமன்ற அதிகாரம் என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Article 307 is authority appointment.", "உறுப்பு 307 அதிகார அமைப்பு நியமனம் என்பதால் விருப்பம் D தவறு.",
        "Part XIII schema: 301 (Freedom) -> 302 (Union Restrictions) -> 304 (State Powers) -> 307 (Authority).",
        "பகுதி XIII கட்டமைப்பு: 301 (சுதந்திரம்) -> 302 (ஒன்றியக் கட்டுப்பாடு) -> 304 (மாநில அதிகாரம்) -> 307 (அதிகார அமைப்பு).",
        "Part XIII articles balance freedom of inter-state commerce with public interest regulatory powers.",
        "பகுதி XIII உறுப்புகள் வர்த்தக சுதந்திரத்தையும் பொது நலன் சார்ந்த ஒழுங்குமுறை அதிகாரங்களையும் சமநிலைப்படுத்துகின்றன.",
        tags=["Part XIII Matching", "Articles 301-307", "Trade Freedom"]
    ))

    # 006 - Ans B
    q.append(make_mf(
        "ISR_MF_006", "Medium",
        "Match List-I (Inter-State River Dispute) with List-II (Riparian States Involved):\nList-I:\na) Cauvery Dispute\nb) Mahadayi Dispute\nc) Mahanadi Dispute\nd) Vansadhara Dispute\n\nList-II:\n1. Goa, Karnataka, and Maharashtra\n2. Tamil Nadu, Karnataka, Kerala, and Puducherry\n3. Andhra Pradesh and Odisha\n4. Odisha and Chhattisgarh",
        "பட்டியல்-I (நதிநீர் தகராறு) உடன் பட்டியல்-II (தொடர்புடைய வடிநில மாநிலங்கள்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) காவிரி தகராறு\nb) மகதாயி தகராறு\nc) மகாநதி தகராறு\nd) வம்சதாரா தகராறு\n\nபட்டியல்-II:\n1. கோவா, கர்நாடகா மற்றும் மகாராஷ்டிரா\n2. தமிழ்நாடு, கர்நாடகா, கேரளா மற்றும் புதுச்சேரி\n3. ஆந்திரப் பிரதேசம் மற்றும் ஒடிசா\n4. ஒடிசா மற்றும் சத்தீஸ்கர்",
        "a-1, b-2, c-4, d-3", "a-1, b-2, c-4, d-3",
        "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
        "a-2, b-4, c-1, d-3", "a-2, b-4, c-1, d-3",
        "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
        "B",
        "The correct matching is: (a) Cauvery Dispute = Tamil Nadu, Karnataka, Kerala, and Puducherry (2); (b) Mahadayi Dispute = Goa, Karnataka, and Maharashtra (1); (c) Mahanadi Dispute = Odisha and Chhattisgarh (4); (d) Vansadhara Dispute = Andhra Pradesh and Odisha (3).",
        "சரியான பொருத்தம்: (a) காவிரி = தமிழ்நாடு, கர்நாடகா, கேரளா, புதுச்சேரி (2); (b) மகதாயி = கோவா, கர்நாடகா, மகாராஷ்டிரா (1); (c) மகாநதி = ஒடிசா, சத்தீஸ்கர் (4); (d) வம்சதாரா = ஆந்திரா, ஒடிசா (3).",
        "Option A is incorrect because Cauvery does not involve Goa or Maharashtra.", "காவிரி கோவாவுடன் தொடர்புடையது அல்ல என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because all four river disputes are paired with their exact riparian entities.", "நான்கு நதிநீர் தகராறுகளும் அவற்றின் வடிநிலப் பகுதிகளுடன் சரியாகப் பொருத்தப்பட்டுள்ளதால் விருப்பம் B சரி.",
        "Option C is incorrect because Mahadayi involves Goa and Karnataka, not Odisha.", "மகதாயி ஒடிசாவுடன் தொடர்புடையது அல்ல என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Vansadhara is AP and Odisha.", "வம்சதாரா ஆந்திரா-ஒடிசா தொடர்புடையது என்பதால் விருப்பம் D தவறு.",
        "River riparians: Cauvery (TN/KA/KL/PY), Mahadayi (GA/KA/MH), Mahanadi (OD/CG), Vansadhara (AP/OD).",
        "நதி வடிநிலங்கள்: காவிரி (TN/KA/KL/PY), மகதாயி (GA/KA/MH), மகாநதி (OD/CG), வம்சதாரா (AP/OD).",
        "Inter-state river basins connect multiple states requiring cooperative adjudication mechanisms.",
        "மாநிலங்களுக்கு இடையேயான நதி வடிநிலங்கள் பல மாநிலங்களை இணைப்பதால் கூட்டுறவு தீர்ப்பாயங்கள் தேவைப்படுகின்றன.",
        tags=["Riparian States", "River Basins Matching", "TNPSC Core"]
    ))

    # 007 - Ans C
    q.append(make_mf(
        "ISR_MF_007", "Medium",
        "Match List-I (Federal Committee / Commission) with List-II (Year of Appointment):\nList-I:\na) First Administrative Reforms Commission\nb) Rajamannar Committee\nc) Sarkaria Commission\nd) Punchhi Commission\n\nList-II:\n1. 1983\n2. 2007\n3. 1966\n4. 1969",
        "பட்டியல்-I (கூட்டாட்சிக் குழு / ஆணையம்) உடன் பட்டியல்-II (அமைக்கப்பட்ட ஆண்டு)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) முதல் நிர்வாகச் சீர்திருத்த ஆணையம்\nb) ராஜமன்னார் குழு\nc) சர்க்காரியா ஆணையம்\nd) பூஞ்சி ஆணையம்\n\nபட்டியல்-II:\n1. 1983\n2. 2007\n3. 1966\n4. 1969",
        "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
        "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
        "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
        "a-4, b-3, c-1, d-2", "a-4, b-3, c-1, d-2",
        "C",
        "The correct matching is: (a) First ARC was appointed in 1966 (3); (b) Rajamannar Committee was appointed by Tamil Nadu in 1969 (4); (c) Sarkaria Commission was appointed in 1983 (1); (d) Punchhi Commission was appointed in 2007 (2).",
        "சரியான பொருத்தம்: (a) முதல் நிர்வாகச் சீர்திருத்த ஆணையம் = 1966 (3); (b) ராஜமன்னார் குழு = 1969 (4); (c) சர்க்காரியா ஆணையம் = 1983 (1); (d) பூஞ்சி ஆணையம் = 2007 (2).",
        "Option A is incorrect because First ARC was in 1966, not 1983.", "முதல் ARC 1966 என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Sarkaria was 1983, not 1969.", "சர்க்காரியா 1983 என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because all four commissions are matched with their historical appointment years.", "நான்கு ஆணையங்களும் அமைக்கப்பட்ட ஆண்டுகளுடன் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் C சரி.",
        "Option D is incorrect because Rajamannar was 1969, not 1966.", "ராஜமன்னார் 1969 என்பதால் விருப்பம் D தவறு.",
        "Commission timeline: ARC (1966) -> Rajamannar (1969) -> Sarkaria (1983) -> Punchhi (2007).",
        "ஆணையங்களின் காலவரிசை: ARC (1966) -> ராஜமன்னார் (1969) -> சர்க்காரியா (1983) -> பூஞ்சி (2007).",
        "Commissions on Centre-State and Inter-State relations: ARC (1966), Rajamannar (1969), Sarkaria (1983), Punchhi (2007).",
        "கூட்டாட்சி உறவுகள் குறித்த முக்கிய ஆணையங்கள்: ARC (1966), ராஜமன்னார் (1969), சர்க்காரியா (1983), பூஞ்சி (2007).",
        tags=["Commissions Matching", "Federalism History", "TNPSC PYQ"]
    ))

    # 008 - Ans D
    q.append(make_mf(
        "ISR_MF_008", "Hard",
        "Match List-I (Landmark Case) with List-II (Core Legal Principle):\nList-I:\na) Atiabari Tea Co. v. State of Assam (1961)\nb) Automobile Transport v. State of Rajasthan (1962)\nc) Jindal Stainless Ltd. v. State of Haryana (2017)\nd) Karnataka v. Tamil Nadu (Cauvery, 2018)\n\nList-II:\n1. Compensatory and regulatory taxes do not violate Article 301\n2. River water is a national asset and subject to Article 136 review\n3. Direct and immediate restrictions on trade movement violate Article 301\n4. Overruled compensatory tax doctrine; non-discriminatory entry tax is valid",
        "பட்டியல்-I (வரலாற்று வழக்கு) உடன் பட்டியல்-II (முக்கிய சட்டக் கோட்பாடு)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) அத்தியாபாரி டீ கம்பெனி எதிர் அசாம் (1961)\nb) ஆட்டோமொபைல் டிரான்ஸ்போர்ட் எதிர் ராஜஸ்தான் (1962)\nc) ஜிண்டால் ஸ்டெயின்லெஸ் எதிர் ஹரியானா (2017)\nd) கர்நாடகா எதிர் தமிழ்நாடு (காவிரி, 2018)\n\nபட்டியல்-II:\n1. ஈட்டு வரிகள் மற்றும் ஒழுங்குமுறை வரிகள் உறுப்பு 301-ஐ மீறாது\n2. நதிநீர் ஒரு தேசியச் சொத்து மற்றும் உறுப்பு 136 மறுஆய்வுக்கு உட்பட்டது\n3. வர்த்தக நகர்வின் மீதான நேரடி மற்றும் உடனடித் தடைகள் உறுப்பு 301-ஐ மீறும்\n4. ஈட்டு வரிக் கோட்பாடு ரத்து; பாகுபாடற்ற நுழைவு வரி செல்லும்",
        "a-1, b-3, c-4, d-2", "a-1, b-3, c-4, d-2",
        "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
        "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
        "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
        "D",
        "The correct matching is: (a) Atiabari (1961) = Direct and immediate restrictions doctrine (3); (b) Automobile Transport (1962) = Compensatory tax doctrine (1); (c) Jindal Stainless (2017) = Overruling compensatory tax and upholding entry tax (4); (d) Cauvery (2018) = River water as national asset & Art 136 review (2).",
        "சரியான பொருத்தம்: (a) அத்தியாபாரி = நேரடி மற்றும் உடனடித் தடைகள் கோட்பாடு (3); (b) ஆட்டோமொபைல் = ஈட்டு வரிக் கோட்பாடு (1); (c) ஜிண்டால் ஸ்டெயின்லெஸ் = ஈட்டு வரி ரத்து மற்றும் நுழைவு வரி செல்லுபடி (4); (d) காவிரி = நதிநீர் தேசியச் சொத்து & உறுப்பு 136 மறுஆய்வு (2).",
        "Option A is incorrect because Atiabari established direct restrictions, not compensatory taxes.", "அத்தியாபாரி நேரடித் தடைகள் பற்றியது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Automobile Transport established compensatory taxes.", "ஆட்டோமொபைல் ஈட்டு வரிகளை நிறுவியது என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Cauvery dealt with river water, not Atiabari.", "காவிரி வழக்கு நதிநீர் பற்றியது என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because all four landmark cases are matched with their foundational constitutional ratios.", "நான்கு வரலாற்று வழக்குகளும் அவற்றின் தீர்ப்புக் கோட்பாடுகளுடன் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் D சரி.",
        "Jurisprudence roadmap: Atiabari (Direct test) -> Automobile (Compensatory test) -> Jindal (Non-discrimination) -> Cauvery (National asset).",
        "நீதிநெறி காலவரிசை: அத்தியாபாரி (நேரடித் தடை) -> ஆட்டோமொபைல் (ஈட்டு வரி) -> ஜிண்டால் (பாகுபாடின்மை) -> காவிரி (தேசியச் சொத்து).",
        "Landmark Supreme Court rulings shape the contours of inter-state trade, water, and federal relations.",
        "வரலாற்றுச் சிறப்புமிக்க உச்ச நீதிமன்றத் தீர்ப்புகள் மாநிலங்களுக்கிடையேயான வர்த்தகம் மற்றும் நதிநீர் உறவுகளை வடிவமைத்துள்ளன.",
        tags=["Landmark Cases", "Judicial Doctrines", "List Matching"]
    ))

    # 009 - Ans A
    q.append(make_mf(
        "ISR_MF_009", "Medium",
        "Match List-I (Inter-State Body) with List-II (Legal / Statutory Origin):\nList-I:\na) Inter-State Council\nb) Zonal Councils\nc) North-Eastern Council\nd) Cauvery Water Management Authority (CWMA)\n\nList-II:\n1. Article 263 of the Constitution\n2. States Reorganisation Act, 1956\n3. North-Eastern Council Act, 1971\n4. Section 6A of the Inter-State River Water Disputes Act, 1956",
        "பட்டியல்-I (மாநிலங்களுக்கு இடையிலான அமைப்பு) உடன் பட்டியல்-II (சட்டப்பூர்வ / அரசியலமைப்பு மூலம்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) மாநிலங்களுக்கு இடையிலான மன்றம்\nb) மண்டலக் குழுக்கள்\nc) வடகிழக்குக் குழு\nd) காவிரி நீர் மேலாண்மை ஆணையம் (CWMA)\n\nபட்டியல்-II:\n1. அரசியலமைப்பின் உறுப்பு 263\n2. 1956 மாநில மறுசீரமைப்புச் சட்டம்\n3. 1971 வடகிழக்குக் குழு சட்டம்\n4. 1956 நதிநீர் தகராறுகள் சட்டத்தின் பிரிவு 6A",
        "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
        "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
        "a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4",
        "a-4, b-2, c-3, d-1", "a-4, b-2, c-3, d-1",
        "A",
        "The correct matching is: (a) Inter-State Council = Article 263 (1); (b) Zonal Councils = States Reorganisation Act, 1956 (2); (c) North-Eastern Council = NEC Act, 1971 (3); (d) CWMA = Section 6A of IRWD Act, 1956 (4).",
        "சரியான பொருத்தம்: (a) மாநிலங்களுக்கு இடையிலான மன்றம் = உறுப்பு 263 (1); (b) மண்டலக் குழுக்கள் = 1956 மாநில மறுசீரமைப்புச் சட்டம் (2); (c) வடகிழக்குக் குழு = 1971 NEC சட்டம் (3); (d) CWMA = 1956 IRWD சட்டம் பிரிவு 6A (4).",
        "Option A is correct because all four bodies are paired with their exact statutory or constitutional roots.", "நான்கு அமைப்புகளும் அவற்றின் சட்டப்பூர்வ அல்லது அரசியலமைப்பு மூலங்களுடன் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் A சரி.",
        "Option B is incorrect because ISC is under Article 263, not 1956 Act.", "மன்றம் உறுப்பு 263-ன் கீழ் உள்ளதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Zonal Councils are under 1956 Act, not 1971 Act.", "மண்டலக் குழுக்கள் 1956 சட்டத்தின் கீழ் உள்ளதால் விருப்பம் C தவறு.",
        "Option D is incorrect because CWMA is under Section 6A, not Article 263.", "CWMA பிரிவு 6A-ன் கீழ் உள்ளதால் விருப்பம் D தவறு.",
        "Know your origins: Article 263 (ISC); 1956 SRA (Zonal Councils); 1971 Act (NEC); Section 6A IRWD (CWMA).",
        "மூலங்களை அறிந்துகொள்க: உறுப்பு 263 (மன்றம்); 1956 SRA (மண்டலக் குழுக்கள்); 1971 சட்டம் (NEC); பிரிவு 6A IRWD (CWMA).",
        "Inter-state bodies in India derive authority from constitutional articles, reorganization statutes, or water acts.",
        "இந்தியாவில் உள்ள மாநிலங்களுக்கு இடையிலான அமைப்புகள் அரசியலமைப்பு, மறுசீரமைப்புச் சட்டங்கள் அல்லது நதிநீர்ச் சட்டங்களிலிருந்து அதிகாரம் பெறுகின்றன.",
        tags=["Institutional Origins", "Statutory Roots", "List Matching"]
    ))

    # 010 - Ans B
    q.append(make_mf(
        "ISR_MF_010", "Medium",
        "Match List-I (Constitutional / Statutory Leader) with List-II (Ex-Officio Office Held):\nList-I:\na) Prime Minister of India\nb) Union Home Minister\nc) Chief Justice of India\nd) Minister of State (IC), Ministry of DoNER\n\nList-II:\n1. Common Chairman of all five Zonal Councils\n2. Chairman of the Inter-State Council\n3. Vice-Chairman of the North-Eastern Council\n4. Nominating authority for Water Disputes Tribunals",
        "பட்டியல்-I (அரசியலமைப்பு / சட்டப்பூர்வ தலைவர்) உடன் பட்டியல்-II (அலுவல்சார் பதவி)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) இந்தியப் பிரதமர்\nb) மத்திய உள்துறை அமைச்சர்\nc) இந்தியத் தலைமை நீதிபதி\nd) DoNER அமைச்சகத்தின் இணை அமைச்சர் (தனிப்பொறுப்பு)\n\nபட்டியல்-II:\n1. ஐந்து மண்டலக் குழுக்களுக்கும் பொதுத் தலைவர்\n2. மாநிலங்களுக்கு இடையிலான மன்றத்தின் தலைவர்\n3. வடகிழக்குக் குழுவின் துணைத் தலைவர்\n4. நதிநீர் தீர்ப்பாயங்களுக்கான பரிந்துரைக்கும் அதிகாரி",
        "a-1, b-2, c-4, d-3", "a-1, b-2, c-4, d-3",
        "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
        "a-2, b-4, c-1, d-3", "a-2, b-4, c-1, d-3",
        "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
        "B",
        "The correct matching is: (a) Prime Minister = Chairman of Inter-State Council (2); (b) Union Home Minister = Common Chairman of all Zonal Councils (1); (c) Chief Justice of India = Nominating authority for water tribunals (4); (d) DoNER Minister = Vice-Chairman of North-Eastern Council (3).",
        "சரியான பொருத்தம்: (a) பிரதமர் = மாநிலங்களுக்கு இடையிலான மன்றத் தலைவர் (2); (b) மத்திய உள்துறை அமைச்சர் = ஐந்து மண்டலக் குழுக்களின் தலைவர் (1); (c) இந்தியத் தலைமை நீதிபதி = தீர்ப்பாய உறுப்பினர்களைப் பரிந்துரைக்கும் அதிகாரி (4); (d) DoNER அமைச்சர் = வடகிழக்குக் குழு துணைத் தலைவர் (3).",
        "Option A is incorrect because Prime Minister chairs the Inter-State Council, not Zonal Councils.", "பிரதமர் மன்றத்திற்குத் தலைமை தாங்குகிறார் என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because all four institutional offices are matched with their exact leadership designations.", "நான்கு தலைவர்களும் அவர்களின் அலுவல்சார் பதவிகளுடன் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் B சரி.",
        "Option C is incorrect because Home Minister chairs Zonal Councils, not tribunals.", "உள்துறை அமைச்சர் மண்டலக் குழுக்களுக்குத் தலைமை தாங்குவதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Prime Minister is not Vice-Chairman of NEC.", "பிரதமர் NEC துணைத் தலைவர் அல்ல என்பதால் விருப்பம் D தவறு.",
        "Leadership matrix: PM = ISC; Home Minister = Zonal Councils & NEC; CJI = Tribunal Nominations; DoNER = NEC Vice-Chair.",
        "தலைமை அணிவரிசை: பிரதமர் = மன்றம்; உள்துறை அமைச்சர் = மண்டலக் குழுக்கள் & NEC; தலைமை நீதிபதி = தீர்ப்பாய நியமனம்; DoNER = NEC துணைத் தலைவர்.",
        "Institutional leadership in Indian federal structures is distributed across the PM, Home Minister, CJI, and DoNER Minister.",
        "இந்தியக் கூட்டாட்சி அமைப்புகளில் நிறுவன தலைமை பிரதமர், உள்துறை அமைச்சர், தலைமை நீதிபதி மற்றும் DoNER அமைச்சர் இடையே பகிர்ந்தளிக்கப்பட்டுள்ளது.",
        tags=["Federal Leadership", "Ex-Officio Offices", "List Matching"]
    ))

    # 011 - Ans C
    q.append(make_mf(
        "ISR_MF_011", "Easy",
        "Match List-I (Southern Zonal Council Member) with List-II (State Capital):\nList-I:\na) Tamil Nadu\nb) Karnataka\nc) Kerala\nd) Telangana\n\nList-II:\n1. Thiruvananthapuram\n2. Hyderabad\n3. Chennai\n4. Bengaluru",
        "பட்டியல்-I (தெற்கு மண்டலக் குழு உறுப்பினர்) உடன் பட்டியல்-II (மாநிலத் தலைநகரம்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) தமிழ்நாடு\nb) கர்நாடகா\nc) கேரளா\nd) தெலுங்கானா\n\nபட்டியல்-II:\n1. திருவனந்தபுரம்\n2. ஹைதராபாத்\n3. சென்னை\n4. பெங்களூரு",
        "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
        "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
        "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
        "a-4, b-3, c-1, d-2", "a-4, b-3, c-1, d-2",
        "C",
        "The correct matching is: (a) Tamil Nadu = Chennai (3); (b) Karnataka = Bengaluru (4); (c) Kerala = Thiruvananthapuram (1); (d) Telangana = Hyderabad (2).",
        "சரியான பொருத்தம்: (a) தமிழ்நாடு = சென்னை (3); (b) கர்நாடகா = பெங்களூரு (4); (c) கேரளா = திருவனந்தபுரம் (1); (d) தெலுங்கானா = ஹைதராபாத் (2).",
        "Option A is incorrect because Tamil Nadu's capital is Chennai, not Thiruvananthapuram.", "தமிழ்நாட்டின் தலைநகர் சென்னை என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Karnataka's capital is Bengaluru, not Thiruvananthapuram.", "கர்நாடகாவின் தலைநகர் பெங்களூரு என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because all four southern states are matched with their respective capital cities.", "நான்கு தென் மாநிலங்களும் அவற்றின் தலைநகரங்களுடன் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் C சரி.",
        "Option D is incorrect because Tamil Nadu is Chennai, not Bengaluru.", "தமிழ்நாடு சென்னை என்பதால் விருப்பம் D தவறு.",
        "Southern Zonal Council encompasses TN (Chennai), KA (Bengaluru), KL (Thiruvananthapuram), AP (Amaravati), TS (Hyderabad), PY (Puducherry).",
        "தெற்கு மண்டலக் குழு: தமிழ்நாடு (சென்னை), கர்நாடகா (பெங்களூரு), கேரளா (திருவனந்தபுரம்), ஆந்திரா (அமராவதி), தெலுங்கானா (ஹைதராபாத்), புதுச்சேரி.",
        "Southern Zonal Council includes Tamil Nadu, Karnataka, Kerala, Andhra Pradesh, Telangana, and Puducherry.",
        "தெற்கு மண்டலக் குழு தமிழ்நாடு, கர்நாடகா, கேரளா, ஆந்திரப் பிரதேசம், தெலுங்கானா மற்றும் புதுச்சேரியை உள்ளடக்கியுள்ளது.",
        tags=["Southern Zonal Council", "Capitals Matching", "TNPSC Easy"]
    ))

    # 012 - Ans D
    q.append(make_mf(
        "ISR_MF_012", "Hard",
        "Match List-I (Inter-State Water Dispute) with List-II (Key Project / Reservoir Involved):\nList-I:\na) Cauvery Dispute\nb) Krishna Dispute\nc) Narmada Dispute\nd) Mahadayi Dispute\n\nList-II:\n1. Almatti Dam\n2. Kalasa-Banduri Nala\n3. Mettur Dam\n4. Sardar Sarovar Dam",
        "பட்டியல்-I (நதிநீர் தகராறு) உடன் பட்டியல்-II (தொடர்புடைய முக்கிய திட்டம் / நீர்த்தேக்கம்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) காவிரி தகராறு\nb) கிருஷ்ணா தகராறு\nc) நர்மதா தகராறு\nd) மகதாயி தகராறு\n\nபட்டியல்-II:\n1. ஆலமட்டி அணை\n2. கலசா-பண்டூரி நாலா\n3. மேட்டூர் அணை\n4. சர்தார் சரோவர் அணை",
        "a-1, b-3, c-4, d-2", "a-1, b-3, c-4, d-2",
        "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
        "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
        "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
        "D",
        "The correct matching is: (a) Cauvery Dispute = Mettur Dam (3); (b) Krishna Dispute = Almatti Dam (1); (c) Narmada Dispute = Sardar Sarovar Dam (4); (d) Mahadayi Dispute = Kalasa-Banduri Nala (2).",
        "சரியான பொருத்தம்: (a) காவிரி = மேட்டூர் அணை (3); (b) கிருஷ்ணா = ஆலமட்டி அணை (1); (c) நர்மதா = சர்தார் சரோவர் அணை (4); (d) மகதாயி = கலசா-பண்டூரி நாலா (2).",
        "Option A is incorrect because Cauvery relates to Mettur, not Almatti.", "காவிரி மேட்டூர் அணையுடன் தொடர்புடையது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Krishna relates to Almatti, not Sardar Sarovar.", "கிருஷ்ணா ஆலமட்டி அணையுடன் தொடர்புடையது என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Cauvery is not Kalasa-Banduri.", "காவிரி கலசா-பண்டூரி அல்ல என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because all four river disputes are correctly matched with their landmark focal projects.", "நான்கு நதிநீர் தகராறுகளும் அவற்றின் மையத் திட்டங்களுடன் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் D சரி.",
        "Key dispute dams: Cauvery = Mettur; Krishna = Almatti; Narmada = Sardar Sarovar; Mahadayi = Kalasa-Banduri.",
        "முக்கிய அணைத் திட்டங்கள்: காவிரி = மேட்டூர்; கிருஷ்ணா = ஆலமட்டி; நர்மதா = சர்தார் சரோவர்; மகதாயி = கலசா-பண்டூரி.",
        "Inter-state river disputes frequently center around major storage reservoirs and inter-basin diversion projects.",
        "மாநிலங்களுக்கு இடையிலான நதிநீர் தகராறுகள் பெரும்பாலும் பெரிய அணைகள் மற்றும் வடிநிலத் திருப்பத் திட்டங்களை மையமாகக் கொண்டுள்ளன.",
        tags=["Dams and Projects", "Inter-State Disputes", "List Matching"]
    ))

    # 013 - Ans A
    q.append(make_mf(
        "ISR_MF_013", "Hard",
        "Match List-I (Seventh Schedule Legislative Entry) with List-II (Constitutional Subject):\nList-I:\na) Entry 56 of List I (Union List)\nb) Entry 17 of List II (State List)\nc) Entry 42 of List I (Union List)\nd) Entry 26 of List II (State List)\n\nList-II:\n1. Regulation and development of inter-State rivers and river valleys\n2. Water supplies, irrigation, canals, and drainage (subject to List I Entry 56)\n3. Inter-State trade and commerce\n4. Trade and commerce within the State (subject to List III Entry 33)",
        "பட்டியல்-I (ஏழாவது அட்டவணை சட்டமன்றப் பதிவு) உடன் பட்டியல்-II (அரசியலமைப்புப் பாடம்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) பட்டியல் I-ன் (மத்தியப் பட்டியல்) பதிவு 56\nb) பட்டியல் II-ன் (மாநிலப் பட்டியல்) பதிவு 17\nc) பட்டியல் I-ன் (மத்தியப் பட்டியல்) பதிவு 42\nd) பட்டியல் II-ன் (மாநிலப் பட்டியல்) பதிவு 26\n\nபட்டியல்-II:\n1. மாநிலங்களுக்கு இடையிலான நதிகள் மற்றும் நதிப் பள்ளத்தாக்குகளின் ஒழுங்குமுறை மற்றும் மேம்பாடு\n2. நீர் விநியோகம், நீர்ப்பாசனம், கால்வாய்கள் மற்றும் வடிகால் (பதிவு 56-க்கு உட்பட்டது)\n3. மாநிலங்களுக்கு இடையிலான வர்த்தகம் மற்றும் வணிகம்\n4. மாநிலத்திற்குள்ளான வர்த்தகம் மற்றும் வணிகம் (பொதுப் பட்டியல் பதிவு 33-க்கு உட்பட்டது)",
        "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
        "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
        "a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4",
        "a-4, b-2, c-3, d-1", "a-4, b-2, c-3, d-1",
        "A",
        "The correct matching is: (a) List I Entry 56 = Inter-State rivers regulation (1); (b) List II Entry 17 = Water and irrigation (2); (c) List I Entry 42 = Inter-State trade and commerce (3); (d) List II Entry 26 = Trade and commerce within the State (4).",
        "சரியான பொருத்தம்: (a) மத்தியப் பட்டியல் பதிவு 56 = மாநிலங்களுக்கு இடையிலான நதிகள் ஒழுங்குமுறை (1); (b) மாநிலப் பட்டியல் பதிவு 17 = நீர் மற்றும் நீர்ப்பாசனம் (2); (c) மத்தியப் பட்டியல் பதிவு 42 = மாநிலங்களுக்கு இடையிலான வர்த்தகம் (3); (d) மாநிலப் பட்டியல் பதிவு 26 = மாநிலத்திற்குள்ளான வர்த்தகம் (4).",
        "Option A is correct because all four legislative entries are paired with their exact constitutional definitions.", "நான்கு சட்டமன்றப் பதிவுகளும் அவற்றின் சரியான பாடங்களுடன் பொருந்தியுள்ளதால் விருப்பம் A சரி.",
        "Option B is incorrect because Entry 56 is Union List river regulation.", "பதிவு 56 நதிகள் ஒழுங்குமுறை என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Entry 17 is water supplies.", "பதிவு 17 நீர் விநியோகம் என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Entry 26 is trade within the State.", "பதிவு 26 மாநிலத்திற்குள்ளான வர்த்தகம் என்பதால் விருப்பம் D தவறு.",
        "Seventh Schedule inter-state entries: Union 56 (Rivers), State 17 (Water), Union 42 (Inter-state trade), State 26 (Intra-state trade).",
        "ஏழாவது அட்டவணைப் பதிவுகள்: ஒன்றியம் 56 (நதிகள்), மாநிலம் 17 (நீர்), ஒன்றியம் 42 (மாநிலங்களுக்கிடையேயான வர்த்தகம்), மாநிலம் 26 (உள் வர்த்தகம்).",
        "Seventh Schedule legislative entries delineate Union and State competencies over water and commerce.",
        "ஏழாவது அட்டவணை சட்டமன்றப் பதிவுகள் நீர் மற்றும் வர்த்தகம் குறித்த ஒன்றியம் மற்றும் மாநில அதிகாரங்களை வரையறுக்கின்றன.",
        tags=["Seventh Schedule Entries", "Legislative Powers", "List Matching"]
    ))

    # 014 - Ans B
    q.append(make_mf(
        "ISR_MF_014", "Medium",
        "Match List-I (Zonal Council) with List-II (Member States Composition):\nList-I:\na) Central Zonal Council\nb) Eastern Zonal Council\nc) Western Zonal Council\nd) Southern Zonal Council\n\nList-II:\n1. Bihar, Jharkhand, Odisha, and West Bengal\n2. UP, MP, Uttarakhand, and Chhattisgarh\n3. Andhra Pradesh, Karnataka, Kerala, Tamil Nadu, Telangana, and Puducherry\n4. Goa, Gujarat, Maharashtra, and DNH & DD",
        "பட்டியல்-I (மண்டலக் குழு) உடன் பட்டியல்-II (உறுப்பு மாநிலங்களின் தொகுப்பு)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) மத்திய மண்டலக் குழு\nb) கிழக்கு மண்டலக் குழு\nc) மேற்கு மண்டலக் குழு\nd) தெற்கு மண்டலக் குழு\n\nபட்டியல்-II:\n1. பீகார், ஜார்க்கண்ட், ஒடிசா மற்றும் மேற்கு வங்காளம்\n2. உ.பி., ம.பி., உத்தராகண்ட் மற்றும் சத்தீஸ்கர்\n3. ஆந்திரா, கர்நாடகா, கேரளா, தமிழ்நாடு, தெலுங்கானா மற்றும் புதுச்சேரி\n4. கோவா, குஜராத், மகாராஷ்டிரா மற்றும் DNH & DD",
        "a-1, b-2, c-4, d-3", "a-1, b-2, c-4, d-3",
        "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
        "a-2, b-4, c-1, d-3", "a-2, b-4, c-1, d-3",
        "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
        "B",
        "The correct matching is: (a) Central Zone = UP, MP, UK, CG (2); (b) Eastern Zone = Bihar, Jharkhand, Odisha, WB (1); (c) Western Zone = Goa, Gujarat, Maharashtra, DNH & DD (4); (d) Southern Zone = AP, KA, KL, TN, TS, Puducherry (3).",
        "சரியான பொருத்தம்: (a) மத்திய மண்டலம் = உ.பி., ம.பி., உத்தராகண்ட், சத்தீஸ்கர் (2); (b) கிழக்கு மண்டலம் = பீகார், ஜார்க்கண்ட், ஒடிசா, மேற்கு வங்காளம் (1); (c) மேற்கு மண்டலம் = கோவா, குஜராத், மகாராஷ்டிரா, DNH & DD (4); (d) தெற்கு மண்டலம் = ஆந்திரா, கர்நாடகா, கேரளா, தமிழ்நாடு, தெலுங்கானா, புதுச்சேரி (3).",
        "Option A is incorrect because Central Zone does not include Bihar.", "மத்திய மண்டலத்தில் பீகார் இல்லை என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because all four zonal councils are paired with their exact member state compositions.", "நான்கு மண்டலக் குழுக்களும் அவற்றின் உறுப்பு மாநிலங்களுடன் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் B சரி.",
        "Option C is incorrect because Western Zone is paired with Eastern states.", "மேற்கு மண்டலம் தவறாகப் பொருத்தப்பட்டுள்ளதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Southern Zone is not paired with Central states.", "தெற்கு மண்டலம் தவறாகப் பொருத்தப்பட்டுள்ளதால் விருப்பம் D தவறு.",
        "State mapping: Central (4 states), Eastern (4 states), Western (3 states + UT), Southern (5 states + UT).",
        "மாநில அமைவு: மத்திய (4 மாநிலங்கள்), கிழக்கு (4 மாநிலங்கள்), மேற்கு (3 மாநிலங்கள் + UT), தெற்கு (5 மாநிலங்கள் + UT).",
        "Zonal Councils divide India's States into five statutory zones to promote inter-state cooperation.",
        "மாநிலங்களுக்கு இடையேயான ஒத்துழைப்பை மேம்படுத்த மண்டலக் குழுக்கள் இந்திய மாநிலங்களை ஐந்து சட்டப்பூர்வ மண்டலங்களாகப் பிரிக்கின்றன.",
        tags=["Zonal Member States", "State Grouping", "List Matching"]
    ))

    # 015 - Ans C
    q.append(make_mf(
        "ISR_MF_015", "Hard",
        "Match List-I (Water Tribunal) with List-II (Year of Constitution):\nList-I:\na) Godavari Water Disputes Tribunal\nb) Second Krishna Water Disputes Tribunal (KWDT-II)\nc) Vansadhara Water Disputes Tribunal\nd) Mahadayi Water Disputes Tribunal\n\nList-II:\n1. 2004\n2. 1969\n3. 2010 (February)\n4. 2010 (November)",
        "பட்டியல்-I (நதிநீர் தீர்ப்பாயம்) உடன் பட்டியல்-II (அமைக்கப்பட்ட ஆண்டு)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) கோதாவரி நதிநீர் தகராறுகள் தீர்ப்பாயம்\nb) இரண்டாவது கிருஷ்ணா நதிநீர் தீர்ப்பாயம் (KWDT-II)\nc) வம்சதாரா நதிநீர் தகராறுகள் தீர்ப்பாயம்\nd) மகதாயி நதிநீர் தகராறுகள் தீர்ப்பாயம்\n\nபட்டியல்-II:\n1. 2004\n2. 1969\n3. 2010 (பிப்ரவரி)\n4. 2010 (நவம்பர்)",
        "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
        "a-2, b-4, c-1, d-3", "a-2, b-4, c-1, d-3",
        "a-2, b-1, c-3, d-4", "a-2, b-1, c-3, d-4",
        "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
        "C",
        "The correct matching is: (a) Godavari Tribunal was set up in 1969 (2); (b) KWDT-II was constituted in 2004 under Justice Brijesh Kumar (1); (c) Vansadhara Tribunal was constituted in February 2010 (3); (d) Mahadayi Tribunal was constituted in November 2010 (4).",
        "சரியான பொருத்தம்: (a) கோதாவரி தீர்ப்பாயம் = 1969 (2); (b) இரண்டாவது கிருஷ்ணா தீர்ப்பாயம் = 2004 (1); (c) வம்சதாரா தீர்ப்பாயம் = பிப்ரவரி 2010 (3); (d) மகதாயி தீர்ப்பாயம் = நவம்பர் 2010 (4).",
        "Option A is incorrect because Godavari was 1969, not 2004.", "கோதாவரி 1969 என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because KWDT-II was 2004, not 2010.", "கிருஷ்ணா-II 2004 என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because Godavari (1969), KWDT-II (2004), Vansadhara (Feb 2010), and Mahadayi (Nov 2010) are precisely paired.", "நான்கு தீர்ப்பாயங்களும் அமைக்கப்பட்ட மாத/ஆண்டுகளுடன் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் C சரி.",
        "Option D is incorrect because Vansadhara was 2010, not 1969.", "வம்சதாரா 2010 என்பதால் விருப்பம் D தவறு.",
        "2010 twin tribunals: Vansadhara was set up in February 2010; Mahadayi was set up in November 2010.",
        "2010-ன் இரட்டை தீர்ப்பாயங்கள்: வம்சதாரா பிப்ரவரி 2010-லும், மகதாயி நவம்பர் 2010-லும் அமைக்கப்பட்டன.",
        "Godavari (1969), KWDT-II (2004), Vansadhara (2010), and Mahadayi (2010) illustrate the ongoing timeline of water tribunals.",
        "கோதாவரி (1969), கிருஷ்ணா-II (2004), வம்சதாரா (2010) மற்றும் மகதாயி (2010) ஆகியவை நதிநீர் தீர்ப்பாயங்களின் தொடர் காலவரிசையை விளக்குகின்றன.",
        tags=["Tribunal Chronology", "2010 Tribunals", "List Matching"]
    ))

    # 016 - Ans D
    q.append(make_mf(
        "ISR_MF_016", "Medium",
        "Match List-I (Constitutional Clause) with List-II (Specific Legal Mandate):\nList-I:\na) Article 261(1)\nb) Article 261(3)\nc) Article 262(2)\nd) Article 304(a)\n\nList-II:\n1. Execution of civil court final judgments across all States\n2. Power of Parliament by law to exclude jurisdiction of Supreme Court\n3. Non-discriminatory state taxation of goods imported from other states\n4. Full faith and credit to public acts, records, and judicial proceedings",
        "பட்டியல்-I (அரசியலமைப்பு உட்பிரிவு) உடன் பட்டியல்-II (குறிப்பிட்ட சட்ட ஆணை)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) உறுப்பு 261(1)\nb) உறுப்பு 261(3)\nc) உறுப்பு 262(2)\nd) உறுப்பு 304(a)\n\nபட்டியல்-II:\n1. அனைத்து மாநிலங்களிலும் உரிமையியல் நீதிமன்ற இறுதித் தீர்ப்புகளை நிறைவேற்றுதல்\n2. உச்ச நீதிமன்றத்தின் அதிகார வரம்பை சட்டத்தின் மூலம் விலக்க நாடாளுமன்றத்திற்கு அதிகாரம்\n3. பிற மாநிலங்களிலிருந்து இறக்குமதி செய்யப்படும் பொருட்களுக்கு பாகுபாடற்ற மாநில வரி விதிப்பு\n4. பொதுச் சட்டங்கள், பதிவேடுகள் மற்றும் நீதித்துறை நடவடிக்கைகளுக்கு முழு நம்பிக்கையும் சான்றும்",
        "a-1, b-4, c-2, d-3", "a-1, b-4, c-2, d-3",
        "a-4, b-2, c-1, d-3", "a-4, b-2, c-1, d-3",
        "a-3, b-1, c-2, d-4", "a-3, b-1, c-2, d-4",
        "a-4, b-1, c-2, d-3", "a-4, b-1, c-2, d-3",
        "D",
        "The correct matching is: (a) Article 261(1) = Full faith and credit mandate (4); (b) Article 261(3) = Execution of civil court judgments (1); (c) Article 262(2) = Parliament's power to exclude court jurisdiction (2); (d) Article 304(a) = Non-discriminatory taxation of imported goods (3).",
        "சரியான பொருத்தம்: (a) உறுப்பு 261(1) = முழு நம்பிக்கையும் சான்றும் ஆணை (4); (b) உறுப்பு 261(3) = உரிமையியல் நீதிமன்றத் தீர்ப்புகளை நிறைவேற்றுதல் (1); (c) உறுப்பு 262(2) = நீதிமன்ற அதிகார வரம்பை விலக்க நாடாளுமன்ற அதிகாரம் (2); (d) உறுப்பு 304(a) = இறக்குமதிப் பொருட்களுக்குப் பாகுபாடற்ற வரி விதிப்பு (3).",
        "Option A is incorrect because Article 261(1) is the general full faith clause.", "உறுப்பு 261(1) பொது விதி என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Article 261(3) is execution, not court exclusion.", "உறுப்பு 261(3) நிறைவேற்றுதல் பற்றியது என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Article 261(1) is not non-discriminatory tax.", "உறுப்பு 261(1) வரி பற்றியது அல்ல என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because all four clauses are precisely aligned with their constitutional rules.", "நான்கு உட்பிரிவுகளும் அவற்றின் விதிகளுடன் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் D சரி.",
        "Sub-clause precision: 261(1) = Recognition; 261(3) = Civil Execution; 262(2) = Court Exclusion; 304(a) = Tax Parity.",
        "உட்பிரிவு துல்லியம்: 261(1) = அங்கீகாரம்; 261(3) = உரிமையியல் நிறைவேற்றம்; 262(2) = நீதிமன்ற விலக்கு; 304(a) = வரி சமநிலை.",
        "Constitutional clauses 261(1), 261(3), 262(2), and 304(a) delineate specific operational rules of federal relations.",
        "அரசியலமைப்பு உட்பிரிவுகள் 261(1), 261(3), 262(2) மற்றும் 304(a) கூட்டாட்சி உறவுகளின் குறிப்பிட்ட செயல்பாட்டு விதிகளை வரையறுக்கின்றன.",
        tags=["Constitutional Clauses", "Sub-clause Precision", "List Matching"]
    ))

    # 017 - Ans A
    q.append(make_mf(
        "ISR_MF_017", "Hard",
        "Match List-I (Commission / Report) with List-II (Key Inter-State Recommendation):\nList-I:\na) Rajamannar Committee (1971)\nb) Sarkaria Commission (1988)\nc) Punchhi Commission (2010)\nd) Administrative Reforms Commission (1969)\n\nList-II:\n1. Recommended an Inter-State Council with constitutional authority and equal state representation\n2. Recommended establishing the council permanently under Article 263 and naming it Inter-Governmental Council\n3. Recommended expanding the role of Zonal Councils as regional hubs for security and planning\n4. Recommended setting up an Inter-State Council to advise on all issues of national importance",
        "பட்டியல்-I (ஆணையம் / அறிக்கை) உடன் பட்டியல்-II (முக்கிய மாநிலங்களுக்கிடையேயான பரிந்துரை)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) ராஜமன்னார் குழு (1971)\nb) சர்க்காரியா ஆணையம் (1988)\nc) பூஞ்சி ஆணையம் (2010)\nd) நிர்வாகச் சீர்திருத்த ஆணையம் (1969)\n\nபட்டியல்-II:\n1. அரசியலமைப்பு அதிகாரம் மற்றும் சமமான மாநில பிரதிநிதித்துவத்துடன் மாநிலங்களுக்கு இடையிலான மன்றத்தைப் பரிந்துரைத்தது\n2. உறுப்பு 263-ன் கீழ் நிரந்தர மன்றத்தை அமைத்து அரசாங்கங்களுக்கு இடையிலான மன்றம் எனப் பெயரிடப் பரிந்துரைத்தது\n3. மண்டலக் குழுக்களைப் பாதுகாப்பு மற்றும் திட்டமிடலுக்கான பிராந்திய மையங்களாக விரிவுபடுத்தப் பரிந்துரைத்தது\n4. தேசிய முக்கியத்துவம் வாய்ந்த அனைத்துப் பிரச்சினைகளிலும் ஆலோசனை வழங்க மாநிலங்களுக்கு இடையிலான மன்றத்தை அமைக்கப் பரிந்துரைத்தது",
        "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
        "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
        "a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4",
        "a-4, b-2, c-3, d-1", "a-4, b-2, c-3, d-1",
        "A",
        "The correct matching is: (a) Rajamannar Committee (1971) = Inter-State Council with constitutional stature and equal representation (1); (b) Sarkaria Commission (1988) = Permanent body named Inter-Governmental Council (2); (c) Punchhi Commission (2010) = Zonal Councils as regional hubs (3); (d) First ARC (1969) = Early council for national issues (4).",
        "சரியான பொருத்தம்: (a) ராஜமன்னார் குழு = அரசியலமைப்பு அதிகாரம் மற்றும் சம பிரதிநிதித்துவத்துடன் கூடிய மன்றம் (1); (b) சர்க்காரியா ஆணையம் = அரசாங்கங்களுக்கு இடையிலான மன்றம் என்ற பெயரில் நிரந்தர மன்றம் (2); (c) பூஞ்சி ஆணையம் = மண்டலக் குழுக்களைப் பிராந்திய மையங்களாக மாற்றுதல் (3); (d) முதல் ARC = தேசியப் பிரச்சினைகளுக்கான ஆரம்பகட்ட மன்றப் பரிந்துரை (4).",
        "Option A is correct because each commission is matched with its distinct contribution to inter-state institutional design.", "ஒவ்வொரு ஆணையமும் அதன் குறிப்பிட்ட பரிந்துரையுடன் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் A சரி.",
        "Option B is incorrect because Rajamannar did not suggest the name Inter-Governmental Council.", "ராஜமன்னார் குழு அரசாங்கங்களுக்கு இடையிலான மன்றம் என்ற பெயரை முன்மொழியவில்லை என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Sarkaria did not focus on Zonal Councils as regional hubs.", "சர்க்காரியா ஆணையம் மண்டலக் குழுக்களை மையமாகக் குறிப்பிடவில்லை என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because ARC was 1969, not Rajamannar.", "ARC பரிந்துரைகள் வேறுபட்டவை என்பதால் விருப்பம் D தவறு.",
        "Commission keywords: Rajamannar = Equal Representation; Sarkaria = Inter-Governmental Council; Punchhi = Regional Hubs.",
        "ஆணைய முக்கிய சொற்கள்: ராஜமன்னார் = சம பிரதிநிதித்துவம்; சர்க்காரியா = அரசாங்கங்களுக்கு இடையிலான மன்றம்; பூஞ்சி = பிராந்திய மையங்கள்.",
        "Committees from Rajamannar to Punchhi continuously advocated strengthening institutional inter-state mechanisms.",
        "ராஜமன்னார் முதல் பூஞ்சி வரையிலான குழுக்கள் மாநிலங்களுக்கு இடையிலான அமைப்புகளை வலுப்படுத்தத் தொடர்ந்து வலியுறுத்தின.",
        tags=["Commission Recommendations", "Federalism Reforms", "List Matching"]
    ))

    # 018 - Ans B
    q.append(make_mf(
        "ISR_MF_018", "Easy",
        "Match List-I (North-Eastern State) with List-II (Capital City):\nList-I:\na) Assam\nb) Meghalaya\nc) Nagaland\nd) Sikkim\n\nList-II:\n1. Shillong\n2. Dispur\n3. Gangtok\n4. Kohima",
        "பட்டியல்-I (வடகிழக்கு மாநிலம்) உடன் பட்டியல்-II (தலைநகரம்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) அசாம்\nb) மேகாலயா\nc) நாகாலாந்து\nd) சிக்கிம்\n\nபட்டியல்-II:\n1. ஷில்லாங்\n2. திஸ்பூர்\n3. கேங்டாக்\n4. கோஹிமா",
        "a-1, b-2, c-4, d-3", "a-1, b-2, c-4, d-3",
        "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
        "a-2, b-4, c-1, d-3", "a-2, b-4, c-1, d-3",
        "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
        "B",
        "The correct matching is: (a) Assam = Dispur (2); (b) Meghalaya = Shillong (1); (c) Nagaland = Kohima (4); (d) Sikkim = Gangtok (3).",
        "சரியான பொருத்தம்: (a) அசாம் = திஸ்பூர் (2); (b) மேகாலயா = ஷில்லாங் (1); (c) நாகாலாந்து = கோஹிமா (4); (d) சிக்கிம் = கேங்டாக் (3).",
        "Option A is incorrect because Assam's capital is Dispur, not Shillong.", "அசாமின் தலைநகர் திஸ்பூர் என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because all four North-Eastern Council member states are paired with their exact capitals.", "நான்கு வடகிழக்கு மாநிலங்களும் அவற்றின் தலைநகரங்களுடன் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் B சரி.",
        "Option C is incorrect because Meghalaya is Shillong, not Kohima.", "மேகாலயாவின் தலைநகர் ஷில்லாங் என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Assam is not Gangtok.", "அசாம் கேங்டாக் அல்ல என்பதால் விருப்பம் D தவறு.",
        "North-Eastern Council capitals: Assam (Dispur), Meghalaya (Shillong), Nagaland (Kohima), Sikkim (Gangtok).",
        "வடகிழக்கு மாநிலத் தலைநகரங்கள்: அசாம் (திஸ்பூர்), மேகாலயா (ஷில்லாங்), நாகாலாந்து (கோஹிமா), சிக்கிம் (கேங்டாக்).",
        "North-Eastern Council comprises 8 states including Sikkim, with HQ in Shillong.",
        "வடகிழக்குக் குழு சிக்கிம் உட்பட 8 மாநிலங்களை உள்ளடக்கியது; இதன் தலைமையகம் ஷில்லாங்கில் உள்ளது.",
        tags=["North-Eastern States", "Capitals Matching", "NEC"]
    ))

    # 019 - Ans C
    q.append(make_mf(
        "ISR_MF_019", "Hard",
        "Match List-I (Legal Doctrine / Concept) with List-II (Jurisprudential Meaning):\nList-I:\na) Full Faith and Credit\nb) Harmon Doctrine\nc) Compensatory Tax Doctrine\nd) National Asset Doctrine\n\nList-II:\n1. Direct assertion of absolute territorial sovereignty by an upstream riparian state\n2. Inter-state river waters belong to the nation in common trust and cannot be owned by one state\n3. Extra-territorial recognition and conclusive evidentiary effect given to public acts and records\n4. Taxes levied as reimbursement for facilities and services that do not restrict trade freedom",
        "பட்டியல்-I (சட்டக் கோட்பாடு) உடன் பட்டியல்-II (நீதிநெறிப் பொருள்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) முழு நம்பிக்கையும் சான்றும்\nb) ஹார்மன் கோட்பாடு\nc) ஈட்டு வரிக் கோட்பாடு\nd) தேசியச் சொத்துக் கோட்பாடு\n\nபட்டியல்-II:\n1. நதி உற்பத்தியாகும் மேல் மாநிலம் நதிநீரின் மீது முழுமையான பிராந்திய இறையாண்மை கோருதல்\n2. மாநிலங்களுக்கு இடையேயான நதிநீர் தேசியப் பொதுச் சொத்தாகும்; எந்தவொரு தனி மாநிலமும் சொந்தம் கொண்டாட முடியாது\n3. பொதுச் சட்டங்கள் மற்றும் ஆவணங்களுக்கு மாநில எல்லைகளைத் தாண்டிய அங்கீகாரம் மற்றும் சான்றளிப்பு அளித்தல்\n4. வர்த்தகப் போக்குவரத்து வசதிகளுக்காக ஈடாக வசூலிக்கப்படும் வரிகள் வர்த்தக சுதந்திரத்தைத் தடுப்பதில்லை",
        "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
        "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
        "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
        "a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2",
        "C",
        "The correct matching is: (a) Full Faith and Credit = Extra-territorial recognition of public acts (3); (b) Harmon Doctrine = Upstream absolute sovereignty assertion (1); (c) Compensatory Tax = Reimbursement for trade facilities (4); (d) National Asset = River water in common trust (2).",
        "சரியான பொருத்தம்: (a) முழு நம்பிக்கையும் சான்றும் = பொதுச் சட்டங்களுக்கு நாடு தழுவிய அங்கீகாரம் (3); (b) ஹார்மன் கோட்பாடு = மேல் மாநிலத்தின் முழு இறையாண்மை கோரிக்கை (1); (c) ஈட்டு வரி = வர்த்தக வசதிகளுக்கான ஈட்டுத் தொகை (4); (d) தேசியச் சொத்து = நதிநீர் பொதுச் சொத்து (2).",
        "Option A is incorrect because Full Faith is paired with Harmon doctrine.", "முழு நம்பிக்கை தவறாகப் பொருத்தப்பட்டுள்ளதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Compensatory tax is paired with Harmon.", "ஈட்டு வரி தவறாகப் பொருத்தப்பட்டுள்ளதால் விருப்பம் B தவறு.",
        "Option C is correct because all four legal doctrines are paired with their authentic constitutional meanings.", "நான்கு சட்டக் கோட்பாடுகளும் அவற்றின் துல்லியமான பொருளுடன் பொருந்தியுள்ளதால் விருப்பம் C சரி.",
        "Option D is incorrect because Full Faith is not compensatory tax.", "முழு நம்பிக்கை ஈட்டு வரி அல்ல என்பதால் விருப்பம் D தவறு.",
        "Core doctrines summary: Harmon (Upstream claims), National Asset (Equitable sharing), Compensatory Tax (Facility reimbursement).",
        "முக்கிய கோட்பாடுகள்: ஹார்மன் (மேல் மாநில உரிமை), தேசியச் சொத்து (சமநீதிப் பகிர்வு), ஈட்டு வரி (வசதிக்கான ஈடு).",
        "Legal doctrines govern inter-state relations across water sharing, judicial recognition, and commerce.",
        "சட்டக் கோட்பாடுகள் நதிநீர்ப் பகிர்வு, நீதித்துறை அங்கீகாரம் மற்றும் வர்த்தகம் ஆகியவற்றில் மாநிலங்களுக்கு இடையேயான உறவுகளை வழிநடத்துகின்றன.",
        tags=["Legal Doctrines", "Jurisprudential Concepts", "List Matching"]
    ))

    # 020 - Ans D
    q.append(make_mf(
        "ISR_MF_020", "Medium",
        "Match List-I (Inter-State Forum) with List-II (Procedural / Operational Feature):\nList-I:\na) Inter-State Council Meetings\nb) Zonal Councils Chairmanship\nc) Water Disputes Tribunal Proceedings\nd) Inter-State Council Standing Committee\n\nList-II:\n1. Presided over by the Union Home Minister as common permanent Chair\n2. Chaired by the Union Home Minister with 5 Union Ministers and 9 Chief Ministers\n3. Mandated to deliver final awards within 3 years (+2 years extension)\n4. Held in camera and all questions decided by consensus",
        "பட்டியல்-I (மாநிலங்களுக்கு இடையிலான மன்றம்) உடன் பட்டியல்-II (நடைமுறை / செயல்பாட்டு அம்சம்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) மாநிலங்களுக்கு இடையிலான மன்றக் கூட்டங்கள்\nb) மண்டலக் குழுக்களின் தலைமை\nc) நதிநீர் தீர்ப்பாய நடவடிக்கைகள்\nd) மாநிலங்களுக்கு இடையிலான மன்ற நிலைக்குழு\n\nபட்டியல்-II:\n1. மத்திய உள்துறை அமைச்சர் நிரந்தரப் பொதுத் தலைவராகத் தலைமை தாங்குதல்\n2. மத்திய உள்துறை அமைச்சர் தலைமையில் 5 மத்திய அமைச்சர்கள் மற்றும் 9 முதலமைச்சர்கள் அடங்கியிருத்தல்\n3. 3 ஆண்டுகளுக்குள் (+2 ஆண்டுகள் நீட்டிப்பு) இறுதித் தீர்ப்பை வழங்க வேண்டும் என்ற கால வரம்பு\n4. ரகசியமாக நடத்தப்பட்டு அனைத்து முடிவுகளும் ஒருமனதாக எட்டப்படுதல்",
        "a-1, b-4, c-3, d-2", "a-1, b-4, c-3, d-2",
        "a-4, b-2, c-3, d-1", "a-4, b-2, c-3, d-1",
        "a-2, b-1, c-3, d-4", "a-2, b-1, c-3, d-4",
        "a-4, b-1, c-3, d-2", "a-4, b-1, c-3, d-2",
        "D",
        "The correct matching is: (a) Inter-State Council Meetings = Held in camera and decided by consensus (4); (b) Zonal Councils Chairmanship = Union Home Minister as permanent common chair (1); (c) Water Disputes Tribunal = 3 years award timeline (+2 max) (3); (d) Standing Committee = Chaired by Home Minister with 5 Cabinet Ministers and 9 CMs (2).",
        "சரியான பொருத்தம்: (a) மன்றக் கூட்டங்கள் = ரகசியமாகவும் ஒருமனதாகவும் நடைபெறுதல் (4); (b) மண்டலக் குழு தலைமை = உள்துறை அமைச்சர் பொதுத் தலைவர் (1); (c) நதிநீர் தீர்ப்பாயம் = 3 ஆண்டுகள் தீர்ப்பு வரம்பு (+2 அதிகபட்சம்) (3); (d) நிலைக்குழு = உள்துறை அமைச்சர் தலைவர் + 5 அமைச்சர்கள் + 9 முதலமைச்சர்கள் (2).",
        "Option A is incorrect because ISC meetings are not chaired by the Home Minister.", "மன்றத்திற்கு உள்துறை அமைச்சர் தலைவர் அல்ல என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Zonal Councils are not held with 9 CMs.", "மண்டலக் குழுவில் 9 முதலமைச்சர்கள் மட்டும் இல்லை என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because ISC meetings are not the 5-minister committee.", "மன்றக் கூட்டங்கள் 5 அமைச்சர்கள் குழு அல்ல என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because all four operational features are accurately paired.", "நான்கு செயல்பாட்டு அம்சங்களும் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் D சரி.",
        "Procedural rules: ISC = in camera consensus; Zonal Councils = Home Minister chair; Tribunals = 3+2 years; Standing Committee = 9 CMs.",
        "செயல்பாட்டு விதிகள்: மன்றம் = ரகசிய ஒருமனதான கூட்டம்; மண்டலக் குழுக்கள் = உள்துறை அமைச்சர் தலைமை; தீர்ப்பாயங்கள் = 3+2 ஆண்டுகள்; நிலைக்குழு = 9 முதலமைச்சர்கள்.",
        "Operational procedures govern consensus in the ISC, time limits in tribunals, and leadership in Zonal Councils.",
        "செயல்பாட்டு நடைமுறைகள் மன்றத்தில் ஒருமனதான முடிவுகளையும், தீர்ப்பாயங்களில் கால வரம்புகளையும், மண்டலக் குழுக்களில் தலைமையையும் நிர்வகிக்கின்றன.",
        tags=["Operational Features", "Procedural Rules", "List Matching"]
    ))

    # 021 - Ans A
    q.append(make_mf(
        "ISR_MF_021", "Medium",
        "Match List-I (Inter-State River Basin) with List-II (Originating State):\nList-I:\na) Cauvery River Basin\nb) Krishna River Basin\nc) Godavari River Basin\nd) Narmada River Basin\n\nList-II:\n1. Karnataka (Talakaveri in Kodagu)\n2. Maharashtra (Mahabaleshwar in Western Ghats)\n3. Maharashtra (Trimbakeshwar near Nashik)\n4. Madhya Pradesh (Amarkantak Plateau)",
        "பட்டியல்-I (மாநிலங்களுக்கு இடையேயான நதி வடிநிலம்) உடன் பட்டியல்-II (உற்பத்தியாகும் மாநிலம்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) காவிரி நதி வடிநிலம்\nb) கிருஷ்ணா நதி வடிநிலம்\nc) கோதாவரி நதி வடிநிலம்\nd) நர்மதா நதி வடிநிலம்\n\nபட்டியல்-II:\n1. கர்நாடகா (குடகில் உள்ள தலக்காவிரி)\n2. மகாராஷ்டிரா (மேற்குத் தொடர்ச்சி மலையில் உள்ள மகாபலேஸ்வர்)\n3. மகாராஷ்டிரா (நாசிக் அருகே உள்ள திரியம்பகேஸ்வர்)\n4. மத்தியப் பிரதேசம் (அமர்கண்டக் பீடபூமி)",
        "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
        "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
        "a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4",
        "a-4, b-2, c-3, d-1", "a-4, b-2, c-3, d-1",
        "A",
        "The correct matching is: (a) Cauvery originates at Talakaveri in Karnataka (1); (b) Krishna originates near Mahabaleshwar in Maharashtra (2); (c) Godavari originates at Trimbakeshwar in Maharashtra (3); (d) Narmada originates from Amarkantak in Madhya Pradesh (4).",
        "சரியான பொருத்தம்: (a) காவிரி = கர்நாடகாவின் தலக்காவிரி (1); (b) கிருஷ்ணா = மகாராஷ்டிராவின் மகாபலேஸ்வர் (2); (c) கோதாவரி = மகாராஷ்டிராவின் திரியம்பகேஸ்வர் (3); (d) நர்மதா = மத்தியப் பிரதேசத்தின் அமர்கண்டக் (4).",
        "Option A is correct because all four major disputed inter-state rivers are matched with their exact geographical origins.", "நான்கு முக்கிய நதிகளும் அவற்றின் உற்பத்தியாகும் இடங்களுடன் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் A சரி.",
        "Option B is incorrect because Cauvery does not originate in Maharashtra.", "காவிரி மகாராஷ்டிராவில் உற்பத்தியாகவில்லை என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Krishna is Mahabaleshwar, not Trimbakeshwar.", "கிருஷ்ணா திரியம்பகேஸ்வர் அல்ல என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Cauvery does not originate in MP.", "காவிரி மத்தியப் பிரதேசத்தில் உற்பத்தியாகவில்லை என்பதால் விருப்பம் D தவறு.",
        "Origin points: Cauvery (Talakaveri, KA); Krishna (Mahabaleshwar, MH); Godavari (Trimbakeshwar, MH); Narmada (Amarkantak, MP).",
        "உற்பத்தியாகும் இடங்கள்: காவிரி (தலக்காவிரி, KA); கிருஷ்ணா (மகாபலேஸ்வர், MH); கோதாவரி (திரியம்பகேஸ்வர், MH); நர்மதா (அமர்கண்டக், MP).",
        "Geographical river origins define riparian upstream and downstream relationships in inter-state disputes.",
        "நதிகள் உற்பத்தியாகும் புவியியல் அமைவிடங்கள் மாநிலங்களுக்கு இடையேயான தகராறுகளில் மேல் மற்றும் கீழ் மாநில உறவுகளைத் தீர்மானிக்கின்றன.",
        tags=["River Origins", "Inter-State Basins", "Geography and Polity"]
    ))

    # 022 - Ans B
    q.append(make_mf(
        "ISR_MF_022", "Hard",
        "Match List-I (Part XIII Provision) with List-II (Specific Exception / Power):\nList-I:\na) Article 301\nb) Article 302\nc) Article 303(2)\nd) Article 305\n\nList-II:\n1. Parliament can impose restrictions on trade in the public interest\n2. Universal declaration that trade, commerce, and intercourse shall be free\n3. Protection of laws providing for State monopolies from invalidation\n4. Parliament can make discriminatory trade laws to handle scarcity of goods",
        "பட்டியல்-I (பகுதி XIII விதி) உடன் பட்டியல்-II (குறிப்பிட்ட விதிவிலக்கு / அதிகாரம்)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) உறுப்பு 301\nb) உறுப்பு 302\nc) உறுப்பு 303(2)\nd) உறுப்பு 305\n\nபட்டியல்-II:\n1. பொது நலன் கருதி வர்த்தகத்தின் மீது நாடாளுமன்றம் கட்டுப்பாடுகளை விதிக்கலாம்\n2. வர்த்தகம், வணிகம் மற்றும் தொடர்பு சுதந்திரமாக இருக்க வேண்டும் என்ற பொது அறிவிப்பு\n3. அரசு ஏகபோகங்களை வழங்கும் சட்டங்கள் ரத்தாகாமல் பாதுகாத்தல்\n4. பொருட்கள் பற்றாக்குறையைக் கையாள நாடாளுமன்றம் பாகுபாடான வர்த்தகச் சட்டங்களை இயற்றலாம்",
        "a-1, b-2, c-4, d-3", "a-1, b-2, c-4, d-3",
        "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
        "a-2, b-4, c-1, d-3", "a-2, b-4, c-1, d-3",
        "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
        "B",
        "The correct matching is: (a) Article 301 = Universal trade freedom (2); (b) Article 302 = Parliamentary public interest restrictions (1); (c) Article 303(2) = Scarcity of goods exception for Parliament (4); (d) Article 305 = Saving of State monopolies (3).",
        "சரியான பொருத்தம்: (a) உறுப்பு 301 = வர்த்தக சுதந்திர பொது அறிவிப்பு (2); (b) உறுப்பு 302 = நாடாளுமன்ற பொது நலக் கட்டுப்பாடுகள் (1); (c) உறுப்பு 303(2) = பொருட்கள் பற்றாக்குறை விதிவிலக்கு (4); (d) உறுப்பு 305 = அரசு ஏகபோகங்கள் பாதுகாப்பு (3).",
        "Option A is incorrect because Article 301 is the general freedom, not public interest restrictions.", "உறுப்பு 301 பொது சுதந்திரம் என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because all four Part XIII rules are accurately matched.", "நான்கு பகுதி XIII விதிகளும் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் B சரி.",
        "Option C is incorrect because Article 302 is not scarcity of goods.", "உறுப்பு 302 பற்றாக்குறை விதிவிலக்கு அல்ல என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Article 305 is not general freedom.", "உறுப்பு 305 பொது சுதந்திரம் அல்ல என்பதால் விருப்பம் D தவறு.",
        "Part XIII balance: Freedom (301) -> Public Interest (302) -> Scarcity Exception (303(2)) -> State Monopolies (305).",
        "பகுதி XIII சமநிலை: சுதந்திரம் (301) -> பொது நலன் (302) -> பற்றாக்குறை விதிவிலக்கு (303(2)) -> அரசு ஏகபோகம் (305).",
        "Articles 301, 302, 303(2), and 305 balance national free trade with socialist welfare and crisis management.",
        "உறுப்புகள் 301, 302, 303(2) மற்றும் 305 தேசிய வர்த்தக சுதந்திரத்தை மக்கள் நலன் மற்றும் நெருக்கடி நிர்வாகத்துடன் சமநிலைப்படுத்துகின்றன.",
        tags=["Part XIII Exceptions", "Scarcity Exception", "List Matching"]
    ))

    # 023 - Ans C
    q.append(make_mf(
        "ISR_MF_023", "Hard",
        "Match List-I (Water Tribunal Award) with List-II (Core Quantitative Allocation / Finding):\nList-I:\na) Cauvery Water Disputes Tribunal (2007 Final Award)\nb) Narmada Water Disputes Tribunal (1979 Award)\nc) Krishna Water Disputes Tribunal-I (1976 Award)\nd) Krishna Water Disputes Tribunal-II (2010 Report)\n\nList-II:\n1. Allocated 0.50 MAF to non-riparian State of Rajasthan\n2. Allocated 2060 TMC at 75% dependability among MH, KA, and AP\n3. Allocated 419 TMC to Tamil Nadu and 270 TMC to Karnataka\n4. Re-allocated surplus waters at 65% dependability among MH, KA, and AP",
        "பட்டியல்-I (நதிநீர் தீர்ப்பாயத் தீர்ப்பு) உடன் பட்டியல்-II (முக்கிய அளவீட்டுப் பகிர்வு / முடிவு)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) காவிரி நதிநீர் தீர்ப்பாயம் (2007 இறுதித் தீர்ப்பு)\nb) நர்மதா நதிநீர் தீர்ப்பாயம் (1979 தீர்ப்பு)\nc) முதல் கிருஷ்ணா நதிநீர் தீர்ப்பாயம் (1976 தீர்ப்பு)\nd) இரண்டாவது கிருஷ்ணா நதிநீர் தீர்ப்பாயம் (2010 அறிக்கை)\n\nபட்டியல்-II:\n1. வடிநில மாநிலம் அல்லாத ராஜஸ்தானுக்கு 0.50 MAF நீர் ஒதுக்கீடு\n2. 75% நம்பகத்தன்மையில் 2060 TMC நீரை மகாராஷ்டிரா, கர்நாடகா, ஆந்திரா இடையே ஒதுக்கீடு\n3. தமிழ்நாட்டிற்கு 419 TMC மற்றும் கர்நாடகாவிற்கு 270 TMC நீர் ஒதுக்கீடு\n4. 65% நம்பகத்தன்மையில் உபரி நீரை மகாராஷ்டிரா, கர்நாடகா, ஆந்திரா இடையே மறுபகிர்வு செய்தல்",
        "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
        "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
        "a-3, b-1, c-2, d-4", "a-3, b-1, c-2, d-4",
        "a-4, b-1, c-2, d-3", "a-4, b-1, c-2, d-3",
        "C",
        "The correct matching is: (a) Cauvery 2007 = 419 TMC for TN, 270 TMC for KA (3); (b) Narmada 1979 = 0.50 MAF for Rajasthan (1); (c) KWDT-I 1976 = 2060 TMC at 75% dependability (2); (d) KWDT-II 2010 = 65% dependability surplus re-allocation (4).",
        "சரியான பொருத்தம்: (a) காவிரி 2007 = தமிழ்நாட்டிற்கு 419 TMC, கர்நாடகாவிற்கு 270 TMC (3); (b) நர்மதா 1979 = ராஜஸ்தானுக்கு 0.50 MAF (1); (c) கிருஷ்ணா-I 1976 = 75% நம்பகத்தன்மையில் 2060 TMC (2); (d) கிருஷ்ணா-II 2010 = 65% நம்பகத்தன்மையில் உபரி நீர் பகிர்வு (4).",
        "Option A is incorrect because Cauvery was 419/270 TMC, not 0.50 MAF.", "காவிரி 419/270 TMC என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Narmada allocated water to Rajasthan.", "நர்மதா ராஜஸ்தானுக்கு நீர் ஒதுக்கியது என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because all four landmark awards are matched with their verified quantitative allocations.", "நான்கு வரலாற்றுத் தீர்ப்புகளும் அவற்றின் சரியான அளவீட்டு ஒதுக்கீடுகளுடன் பொருந்தியுள்ளதால் விருப்பம் C சரி.",
        "Option D is incorrect because Cauvery was not KWDT-II's surplus formula.", "காவிரி உபரி நீர் சூத்திரம் அல்ல என்பதால் விருப்பம் D தவறு.",
        "Historic numbers: Cauvery 2007 (419 TN / 270 KA); Narmada 1979 (0.50 MAF to Rajasthan); KWDT-I (2060 TMC at 75%).",
        "முக்கிய எண்கள்: காவிரி 2007 (419 TN / 270 KA); நர்மதா 1979 (0.50 MAF ராஜஸ்தான்); கிருஷ்ணா-I (75%-ல் 2060 TMC).",
        "Quantitative awards of inter-state water tribunals determine volumetric allocations among contesting riparian States.",
        "நதிநீர் தீர்ப்பாயங்களின் அளவீட்டுத் தீர்ப்புகள் மாநிலங்களுக்கிடையேயான நீர்ப் பகிர்வை துல்லியமாக நிர்ணயிக்கின்றன.",
        tags=["Quantitative Allocations", "Water Awards", "List Matching"]
    ))

    # 024 - Ans D
    q.append(make_mf(
        "ISR_MF_024", "Medium",
        "Match List-I (Federal Mechanism) with List-II (Institutional Nature):\nList-I:\na) Supreme Court Original Jurisdiction (Article 131)\nb) Water Disputes Tribunals (Article 262)\nc) Inter-State Council (Article 263)\nd) Zonal Councils (States Reorganisation Act 1956)\n\nList-II:\n1. Statutory specialized adjudicatory tribunal with SC decree-like awards\n2. Constitutional consultative forum established by Presidential Order\n3. Statutory regional deliberative body chaired by Union Home Minister\n4. Constitutional judicial court resolving legal disputes between Union and States",
        "பட்டியல்-I (கூட்டாட்சி அமைப்பு) உடன் பட்டியல்-II (நிறுவனத் தன்மை)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) உச்ச நீதிமன்ற மூல அதிகார வரம்பு (உறுப்பு 131)\nb) நதிநீர் தீர்ப்பாயங்கள் (உறுப்பு 262)\nc) மாநிலங்களுக்கு இடையிலான மன்றம் (உறுப்பு 263)\nd) மண்டலக் குழுக்கள் (1956 மாநில மறுசீரமைப்புச் சட்டம்)\n\nபட்டியல்-II:\n1. உச்ச நீதிமன்ற ஆணைக்கு நிகரான தீர்ப்புகளை வழங்கும் சட்டப்பூர்வ சிறப்பு தீர்ப்பாயம்\n2. குடியரசுத் தலைவரின் ஆணை மூலம் நிறுவப்படும் அரசியலமைப்பு ஆலோசனைக் குழு\n3. மத்திய உள்துறை அமைச்சர் தலைமையில் செயல்படும் சட்டப்பூர்வ பிராந்திய ஆலோசனைக் குழு\n4. ஒன்றியம் மற்றும் மாநிலங்களுக்கு இடையேயான சட்டத் தகராறுகளைத் தீர்க்கும் அரசியலமைப்பு நீதிமன்றம்",
        "a-1, b-4, c-2, d-3", "a-1, b-4, c-2, d-3",
        "a-4, b-2, c-1, d-3", "a-4, b-2, c-1, d-3",
        "a-3, b-1, c-2, d-4", "a-3, b-1, c-2, d-4",
        "a-4, b-1, c-2, d-3", "a-4, b-1, c-2, d-3",
        "D",
        "The correct matching is: (a) Article 131 = Constitutional judicial court (4); (b) Article 262 = Statutory specialized adjudicatory tribunal (1); (c) Article 263 = Constitutional consultative forum (2); (d) Zonal Councils = Statutory regional deliberative body (3).",
        "சரியான பொருத்தம்: (a) உறுப்பு 131 = அரசியலமைப்பு நீதிமன்றம் (4); (b) உறுப்பு 262 = சட்டப்பூர்வ சிறப்பு தீர்ப்பாயம் (1); (c) உறுப்பு 263 = அரசியலமைப்பு ஆலோசனைக் குழு (2); (d) மண்டலக் குழுக்கள் = சட்டப்பூர்வ பிராந்திய ஆலோசனைக் குழு (3).",
        "Option A is incorrect because Article 131 is the judicial court.", "உறுப்பு 131 நீதிமன்றம் என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Article 262 is the specialized tribunal.", "உறுப்பு 262 சிறப்பு தீர்ப்பாயம் என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Article 131 is not a regional body.", "உறுப்பு 131 பிராந்திய அமைப்பு அல்ல என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because all four federal dispute forums are matched with their precise constitutional and statutory status.", "நான்கு கூட்டாட்சி அமைப்புகளும் அவற்றின் துல்லியமான நிறுவனத் தன்மையுடன் பொருந்தியுள்ளதால் விருப்பம் D சரி.",
        "Four-tier federal machinery: Art 131 (Judicial) -> Art 262 (Specialized Tribunal) -> Art 263 (Consultative) -> Zonal Councils (Regional Statutory).",
        "நான்கு அடுக்கு கூட்டாட்சி அமைப்பு: 131 (நீதிமன்றம்) -> 262 (சிறப்பு தீர்ப்பாயம்) -> 263 (ஆலோசனைக் குழு) -> மண்டலக் குழுக்கள் (பிராந்திய சட்டம்).",
        "India's federal architecture combines constitutional courts, statutory tribunals, and advisory consultative councils.",
        "இந்தியக் கூட்டாட்சி கட்டமைப்பு அரசியலமைப்பு நீதிமன்றங்கள், சட்டப்பூர்வ தீர்ப்பாயங்கள் மற்றும் ஆலோசனைக் குழுக்களை ஒருங்கிணைக்கிறது.",
        tags=["Federal Architecture", "Four-Tier Machinery", "List Matching"]
    ))

    # 025 - Ans A
    q.append(make_mf(
        "ISR_MF_025", "Hard",
        "Match List-I (Tribunal / Commission) with List-II (Judge / Authority Heading It):\nList-I:\na) Godavari Water Disputes Tribunal\nb) Ravi and Beas Waters Tribunal\nc) Vansadhara Water Disputes Tribunal\nd) Mahadayi Water Disputes Tribunal\n\nList-II:\n1. Justice R.S. Bachawat\n2. Justice V. Balakrishna Eradi\n3. Justice Mukundakam Sharma\n4. Justice J.M. Panchal",
        "பட்டியல்-I (தீர்ப்பாயம்) உடன் பட்டியல்-II (தலைமை தாங்கிய நீதிபதி)-ஐப் பொருத்துக:\nபட்டியல்-I:\na) கோதாவரி நதிநீர் தகராறுகள் தீர்ப்பாயம்\nb) ராவி மற்றும் பியாஸ் நதிநீர் தீர்ப்பாயம்\nc) வம்சதாரா நதிநீர் தகராறுகள் தீர்ப்பாயம்\nd) மகதாயி நதிநீர் தகராறுகள் தீர்ப்பாயம்\n\nபட்டியல்-II:\n1. நீதிபதி ஆர்.எஸ். பச்சாவத்\n2. நீதிபதி வி. பாலகிருஷ்ணா எராடி\n3. நீதிபதி முகுந்தகம் சர்மா\n4. நீதிபதி ஜே.எம். பஞ்சால்",
        "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
        "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
        "a-1, b-3, c-2, d-4", "a-1, b-3, c-2, d-4",
        "a-4, b-2, c-3, d-1", "a-4, b-2, c-3, d-1",
        "A",
        "The correct matching is: (a) Godavari Tribunal = Justice R.S. Bachawat (1); (b) Ravi & Beas Tribunal = Justice V. Balakrishna Eradi (2); (c) Vansadhara Tribunal = Justice Mukundakam Sharma (3); (d) Mahadayi Tribunal = Justice J.M. Panchal (4).",
        "சரியான பொருத்தம்: (a) கோதாவரி தீர்ப்பாயம் = நீதிபதி ஆர்.எஸ். பச்சாவத் (1); (b) ராவி-பியாஸ் தீர்ப்பாயம் = நீதிபதி வி. பாலகிருஷ்ணா எராடி (2); (c) வம்சதாரா தீர்ப்பாயம் = நீதிபதி முகுந்தகம் சர்மா (3); (d) மகதாயி தீர்ப்பாயம் = நீதிபதி ஜே.எம். பஞ்சால் (4).",
        "Option A is correct because all four water tribunals are paired with their appointed Chief Justices/Judges.", "நான்கு நதிநீர் தீர்ப்பாயங்களும் அவற்றின் தலைமை நீதிபதிகளுடன் சரியாகப் பொருந்தியுள்ளதால் விருப்பம் A சரி.",
        "Option B is incorrect because Godavari was Bachawat, not Eradi.", "கோதாவரி பச்சாவத் என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because Ravi-Beas was Eradi, not Sharma.", "ராவி-பியாஸ் எராடி என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because Mahadayi was Panchal, not Bachawat.", "மகதாயி பஞ்சால் என்பதால் விருப்பம் D தவறு.",
        "Chairpersons master table: Godavari (Bachawat); Ravi-Beas (Eradi); Vansadhara (Sharma); Mahadayi (Panchal).",
        "தலைவர்கள் அட்டவணை: கோதாவரி (பச்சாவத்); ராவி-பியாஸ் (எராடி); வம்சதாரா (சர்மா); மகதாயி (பஞ்சால்).",
        "Judges Bachawat, Eradi, Sharma, and Panchal successfully concluded sensitive inter-State water adjudications.",
        "நீதிபதிகள் பச்சாவத், எராடி, சர்மா மற்றும் பஞ்சால் ஆகியோர் உணர்வுபூர்வமான நதிநீர் தீர்ப்பாயங்களுக்குத் தலைமை தாங்கினர்.",
        tags=["Tribunal Chairpersons", "Comprehensive Match", "List Matching"]
    ))

    return q

if __name__ == "__main__":
    qs = get_match_questions()
    print(f"[MATCH] Total questions: {len(qs)}")
    assert len(qs) == 25
    keys = Counter(q["correct_answer"] for q in qs)
    print(f"[MATCH] Key Distribution: {dict(keys)}")

    # Check collisions
    existing_stems = set()
    for cat in ["easy", "medium", "hard", "statement_based", "pyq", "reasoning"]:
        fp = f"data/questions/polity/inter_state_relations_{cat}.json"
        if os.path.exists(fp):
            with open(fp, "r", encoding="utf-8") as f:
                data = json.load(f)
            for item in data:
                existing_stems.add(item["question_en"].strip().lower())

    for q_item in qs:
        s_en = q_item["question_en"].strip().lower()
        if s_en in existing_stems:
            raise ValueError(f"Duplicate stem detected: {q_item['id']}")

    print("[MATCH] 0 collisions with existing files!")

    out_file = Path("data/questions/polity/inter_state_relations_match_the_following.json")
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(qs, f, indent=2, ensure_ascii=False)

    rep = ContentValidator.validate_file(str(out_file), expected_count=25, expected_prefix="ISR_MF_")
    print(rep.summary())
    assert rep.is_valid, "Validation failed!"
    print("[MATCH] Validation PASSED!")
