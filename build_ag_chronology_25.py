# -*- coding: utf-8 -*-
"""
Generator for Attorney General of India Chronology MCQs (25 Questions: AG_C_001 to AG_C_025).
Strictly adheres to:
- Numbered events (1, 2, 3, 4) presented in NON-CHRONOLOGICAL order.
- Correct sequence is NOT 1-2-3-4.
- 4 unique permutations of [1, 2, 3, 4].
- Explanation includes 4-digit years and sequence arrows '->'.
- Full 24-field TNPSC Nova AI schema.
- Balanced answer keys (approx 6-7 each of A, B, C, D).
"""

import json
import os
import shutil
import random
from ag_mcq_helper import make_ag_q
from rebalance_er_helper import balance_question_keys
from tools.nova_content_engine.validator import ContentValidator
from tools.nova_content_engine.chronology_validator import ChronologyValidator

# Raw data: each item has:
# - stem_prefix_en, stem_prefix_ta
# - 4 events with (label_en, label_ta, year_val)
# We will explicitly shuffle the presentation order so that presented order != chronological order!

raw_chronology_items = [
    # 1: Early Attorneys General
    {
        "subtopic": "Tenures of Early Attorneys General",
        "title_en": "Arrange the following early Attorneys General of India in chronological order of their assumption of office:",
        "title_ta": "இந்தியாவின் பின்வரும் ஆரம்பகால தலைமை வழக்கறிஞர்களை அவர்கள் பதவியேற்ற காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("M.C. Setalvad appointed as first Attorney General", "எம்.சி. செடல்வாட் முதல் தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1950),
            ("C.K. Daphtary appointed as second Attorney General", "சி.கே. தப்தாரி இரண்டாவது தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1963),
            ("Niren De appointed as third Attorney General", "நீரேன் டே மூன்றாவது தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1968),
            ("S.V. Gupte appointed as fourth Attorney General", "எஸ்.வி. குப்தே நான்காவது தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1977)
        ],
        "shuffle_order": [3, 1, 4, 2] # 1968, 1950, 1977, 1963 -> sorted is 1950(2), 1963(4), 1968(1), 1977(3) -> 2 - 4 - 1 - 3
    },
    # 2: 1980s & 1990s AGs
    {
        "subtopic": "Tenures of 1980s and 1990s AGs",
        "title_en": "Arrange the following Attorneys General of India in chronological order of their assumption of office:",
        "title_ta": "பின்வரும் இந்திய தலைமை வழக்கறிஞர்களை அவர்கள் பதவியேற்ற காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("L.N. Sinha appointed as Attorney General", "எல்.என். சின்ஹா தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1979),
            ("K. Parasaran appointed as Attorney General", "கே. பராசரன் தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1983),
            ("Soli Sorabjee appointed as Attorney General for his first term", "சோலி சொராப்ஜி தனது முதல் பதவிக்காலத்திற்கு நியமிக்கப்படுதல்", 1989),
            ("G. Ramaswamy appointed as Attorney General", "ஜி. ராமசுவாமி தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1990)
        ],
        "shuffle_order": [2, 4, 1, 3] # 1983, 1990, 1979, 1989 -> sorted is 1979(3), 1983(1), 1989(4), 1990(2) -> 3 - 1 - 4 - 2
    },
    # 3: 1990s AGs
    {
        "subtopic": "Tenures of 1990s AGs",
        "title_en": "Arrange the following tenures of Attorneys General of India in chronological order:",
        "title_ta": "இந்திய தலைமை வழக்கறிஞர்களின் பின்வரும் பதவிக்காலங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("Milon K. Banerjee (first tenure as AG)", "மிலன் கே. பானர்ஜி (தலைமை வழக்கறிஞராக முதல் பதவிக்காலம்)", 1992),
            ("Ashok Desai appointed as Attorney General", "அசோக் தேசாய் தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1996),
            ("Soli Sorabjee (second tenure as AG)", "சோலி சொராப்ஜி (தலைமை வழக்கறிஞராக இரண்டாவது பதவிக்காலம்)", 1998),
            ("Milon K. Banerjee (second tenure as AG)", "மிலன் கே. பானர்ஜி (தலைமை வழக்கறிஞராக இரண்டாவது பதவிக்காலம்)", 2004)
        ],
        "shuffle_order": [4, 2, 1, 3] # 2004, 1996, 1992, 1998 -> sorted is 1992(3), 1996(2), 1998(4), 2004(1) -> 3 - 2 - 4 - 1
    },
    # 4: Modern AGs (2009–present)
    {
        "subtopic": "Tenures of Modern AGs",
        "title_en": "Arrange the following modern Attorneys General of India in chronological order of their appointment:",
        "title_ta": "பின்வரும் நவீன இந்திய தலைமை வழக்கறிஞர்களை அவர்கள் நியமிக்கப்பட்ட காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("G.E. Vahanvati appointed as Attorney General", "ஜி.இ. வாகனவதி தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 2009),
            ("Mukul Rohatgi appointed as Attorney General", "முகுல் ரோஹத்கி தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 2014),
            ("K.K. Venugopal appointed as Attorney General", "கே.கே. வேணுகோபால் தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 2017),
            ("R. Venkataramani appointed as Attorney General", "ஆர். வெங்கடரமணி தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 2022)
        ],
        "shuffle_order": [3, 1, 4, 2] # 2017, 2009, 2022, 2014 -> sorted is 2009(2), 2014(4), 2017(1), 2022(3) -> 2 - 4 - 1 - 3
    },
    # 5: Landmark Cases (Early Era)
    {
        "subtopic": "Landmark Constitutional Cases (1950-1967)",
        "title_en": "Arrange the following landmark constitutional cases argued by early Attorneys General in chronological order:",
        "title_ta": "ஆரம்பகால தலைமை வழக்கறிஞர்களால் வாதிடப்பட்ட பின்வரும் வரலாற்றுச் சிறப்புமிக்க அரசியலமைப்பு வழக்குகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("A.K. Gopalan v. State of Madras (Preventive Detention)", "ஏ.கே. கோபாலன் எதிர் மதராஸ் மாகாணம் (தடுப்புக் காவல் வழக்கு)", 1950),
            ("Shankari Prasad v. Union of India (1st Amendment validity)", "சங்கரி பிரசாத் எதிர் இந்திய ஒன்றியம் (1-வது திருத்தச் செல்லுபடி)", 1951),
            ("In re Berubari Union Reference under Article 143", "சரத்து 143-ன் கீழ் பெருபாரி யூனியன் குறிப்புரை", 1960),
            ("Golaknath v. State of Punjab (Fundamental rights non-amendability)", "கோலாக்நாத் எதிர் பஞ்சாப் அரசு (அடிப்படை உரிமைகள் திருத்த இயலாமை)", 1967)
        ],
        "shuffle_order": [4, 1, 3, 2] # 1967, 1950, 1960, 1951 -> sorted is 1950(2), 1951(4), 1960(3), 1967(1) -> 2 - 4 - 3 - 1
    },
    # 6: Landmark Cases (1970s)
    {
        "subtopic": "Landmark Constitutional Cases (1970-1976)",
        "title_en": "Arrange the following historic cases involving the Attorney General of India in chronological order:",
        "title_ta": "இந்திய தலைமை வழக்கறிஞர் ஆஜரான பின்வரும் வரலாற்று முக்கியத்துவம் வாய்ந்த வழக்குகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("R.C. Cooper v. Union of India (Bank Nationalization case)", "ஆர்.சி. கூப்பர் எதிர் இந்திய ஒன்றியம் (வங்கி தேசியமயமாக்கல் வழக்கு)", 1970),
            ("Kesavananda Bharati v. State of Kerala (Basic Structure Doctrine)", "கேசவானந்த பாரதி எதிர் கேரள அரசு (அடிப்படை கட்டமைப்பு கோட்பாடு)", 1973),
            ("Indira Nehru Gandhi v. Raj Narain (Election case)", "இந்திரா நேரு காந்தி எதிர் ராஜ் நாராயணன் (தேர்தல் வழக்கு)", 1975),
            ("ADM Jabalpur v. Shivkant Shukla (Habeas Corpus case)", "ஏ.டி.எம். ஜபல்பூர் எதிர் சிவகாந்த் சுக்லா (ஆட்கொணர்வு வழக்கு)", 1976)
        ],
        "shuffle_order": [2, 4, 1, 3] # 1973, 1976, 1970, 1975 -> sorted is 1970(3), 1973(1), 1975(4), 1976(2) -> 3 - 1 - 4 - 2
    },
    # 7: Landmark Cases (Late 1970s to 1990s)
    {
        "subtopic": "Landmark Constitutional Cases (1978-1997)",
        "title_en": "Arrange the following landmark Supreme Court judgments in chronological order:",
        "title_ta": "பின்வரும் வரலாற்றுச் சிறப்புமிக்க உச்ச நீதிமன்றத் தீர்ப்புகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("Maneka Gandhi v. Union of India (Article 21 expansion)", "மேனகா காந்தி எதிர் இந்திய ஒன்றியம் (சரத்து 21 விரிவாக்கம்)", 1978),
            ("Minerva Mills v. Union of India (Harmonious balance)", "மினர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (இணக்கமான சமநிலை)", 1980),
            ("S.R. Bommai v. Union of India (Article 356 guidelines)", "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (சரத்து 356 வழிகாட்டுதல்கள்)", 1994),
            ("L. Chandra Kumar v. Union of India (Tribunals power)", "எல். சந்திர குமார் எதிர் இந்திய ஒன்றியம் (தீர்ப்பாயங்கள் அதிகாரம்)", 1997)
        ],
        "shuffle_order": [3, 1, 4, 2] # 1994, 1978, 1997, 1980 -> sorted is 1978(2), 1980(4), 1994(1), 1997(3) -> 2 - 4 - 1 - 3
    },
    # 8: Landmark Cases (2010s to present)
    {
        "subtopic": "Landmark Cases (2012-2023)",
        "title_en": "Arrange the following landmark Constitution Bench matters argued by the Attorney General in chronological order:",
        "title_ta": "தலைமை வழக்கறிஞரால் வாதிடப்பட்ட பின்வரும் முக்கிய அரசியலமைப்பு அமர்வு வழக்குகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("Natural Resources Allocation Presidential Reference (Art 143)", "இயற்கை வளங்கள் ஒதுக்கீடு தொடர்பான சரத்து 143 குறிப்புரை", 2012),
            ("Supreme Court Advocates-on-Record Association (NJAC case)", "சுப்ரீம் கோர்ட் அட்வகேட்ஸ்-ஆன்-ரெக்கார்ட் சங்கம் (NJAC வழக்கு)", 2015),
            ("K.S. Puttaswamy v. Union of India (Right to Privacy)", "கே.எஸ். புட்டசாமி எதிர் இந்திய ஒன்றியம் (தனிநபர் அந்தரங்க உரிமை)", 2017),
            ("In re Article 370 Abrogation Verdict", "சரத்து 370 ரத்து தொடர்பான உச்ச நீதிமன்ற இறுதித் தீர்ப்பு", 2023)
        ],
        "shuffle_order": [4, 2, 1, 3] # 2023, 2015, 2012, 2017 -> sorted is 2012(3), 2015(2), 2017(4), 2023(1) -> 3 - 2 - 4 - 1
    },
    # 9: Institutional History of Law Officers
    {
        "subtopic": "Historical Milestones of Law Officers",
        "title_en": "Arrange the following institutional milestones in the evolution of law officers in India in chronological order:",
        "title_ta": "இந்தியாவில் சட்ட அதிகாரிகள் அலுவலகத்தின் பரிணாம வளர்ச்சியில் பின்வரும் வரலாற்று மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("Charter Act of 1833 creating Law Member in Governor-General's Council", "1833 பட்டயச் சட்டம் கவர்னர்-ஜெனரல் கவுன்சிலில் சட்ட உறுப்பினரை உருவாக்குதல்", 1833),
            ("Government of India Act 1935 providing for Advocate-General for Federation", "1935 இந்திய அரசுச் சட்டம் கூட்டாட்சி அட்வகேட்-ஜெனரல் பதவியை வழங்குதல்", 1935),
            ("Adoption of Article 76 creating Attorney General of India", "சரத்து 76-ன் கீழ் இந்திய தலைமை வழக்கறிஞர் பதவி உருவாக்கப்படுதல்", 1950),
            ("Enactment of Section 23 of Advocates Act granting pre-audience", "முதன்மை வாதாடும் உரிமை வழங்கும் வழக்கறிஞர்கள் சட்டம் பிரிவு 23 இயற்றப்படுதல்", 1961)
        ],
        "shuffle_order": [3, 4, 1, 2] # 1950, 1961, 1833, 1935 -> sorted is 1833(3), 1935(4), 1950(1), 1961(2) -> 3 - 4 - 1 - 2
    },
    # 10: Statutory Milestones
    {
        "subtopic": "Statutory & Administrative Milestones",
        "title_en": "Arrange the following statutory and administrative milestones relating to the office of Attorney General in chronological order:",
        "title_ta": "தலைமை வழக்கறிஞர் அலுவலகம் தொடர்பான பின்வரும் சட்டரீதியான மற்றும் நிர்வாக மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("Establishment of the First Law Commission of independent India", "சுதந்திர இந்தியாவின் முதலாவது சட்ட ஆணையம் அமைக்கப்படுதல்", 1955),
            ("Enactment of the Advocates Act defining Bar hierarchy", "வழக்கறிஞர்கள் படிநிலையை வரையறுக்கும் வழக்கறிஞர்கள் சட்டம் இயற்றப்படுதல்", 1961),
            ("Enactment of Section 15 of Contempt of Courts Act requiring AG consent", "AG ஒப்புதலைக் கட்டாயமாக்கும் நீதிமன்ற அவமதிப்புச் சட்டம் பிரிவு 15 இயற்றப்படுதல்", 1971),
            ("Promulgation of the Law Officers (Conditions of Service) Rules", "சட்ட அதிகாரிகள் (பணி நிபந்தனைகள்) விதிகள் பிறப்பிக்கப்படுதல்", 1987)
        ],
        "shuffle_order": [4, 1, 3, 2] # 1987, 1955, 1971, 1961 -> sorted is 1955(2), 1961(4), 1971(3), 1987(1) -> 2 - 4 - 3 - 1
    },
    # 11: Soli Sorabjee's Career Milestones
    {
        "subtopic": "Soli Sorabjee's Career Milestones",
        "title_en": "Arrange the following career milestones of eminent jurist Soli Sorabjee in chronological order:",
        "title_ta": "புகழ்பெற்ற சட்ட வல்லுநர் சோலி சொராப்ஜியின் பின்வரும் தொழில்முறை மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("Appointed as Additional Solicitor General of India", "இந்தியாவின் கூடுதல் சொலிசிட்டர் ஜெனரலாக நியமிக்கப்படுதல்", 1977),
            ("Appointed as Solicitor General of India", "இந்தியாவின் சொலிசிட்டர் ஜெனரலாக நியமிக்கப்படுதல்", 1979),
            ("Appointed as Attorney General of India for his first term", "தனது முதல் பதவிக்காலத்திற்கு இந்திய தலைமை வழக்கறிஞராக நியமிக்கப்படுதல்", 1989),
            ("Conferred with the Padma Vibhushan", "பத்ம விபூஷண் விருது வழங்கி கௌரவிக்கப்படுதல்", 2002)
        ],
        "shuffle_order": [3, 1, 4, 2] # 1989, 1977, 2002, 1979 -> sorted is 1977(2), 1979(4), 1989(1), 2002(3) -> 2 - 4 - 1 - 3
    },
    # 12: Historic Article 143 References (Early)
    {
        "subtopic": "Historic Article 143 References (1951-1978)",
        "title_en": "Arrange the following Presidential references under Article 143 argued by the Attorney General in chronological order:",
        "title_ta": "தலைமை வழக்கறிஞரால் வாதிடப்பட்ட பின்வரும் சரத்து 143 குடியரசுத் தலைவர் குறிப்புரைகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("In re Delhi Laws Act Reference (Delegated Legislation)", "தில்லி சட்டங்கள் சட்டம் குறிப்புரை (அதிகாரப் பகிர்வு சட்டம்)", 1951),
            ("In re Berubari Union Reference (Cession of Territory)", "பெருபாரி யூனியன் குறிப்புரை (நிலப்பரப்பை விட்டுக்கொடுத்தல்)", 1960),
            ("In re Sea Customs Act Reference (State property taxation)", "கடல் சுங்கச் சட்டம் குறிப்புரை (மாநில சொத்து வரி விதிப்பு)", 1963),
            ("In re Special Courts Bill Reference (Emergency trials)", "சிறப்பு நீதிமன்றங்கள் மசோதா குறிப்புரை (அவசரநிலை விசாரணைகள்)", 1978)
        ],
        "shuffle_order": [2, 4, 1, 3] # 1960, 1978, 1951, 1963 -> sorted is 1951(3), 1960(1), 1963(4), 1978(2) -> 3 - 1 - 4 - 2
    },
    # 13: Article 143 References (Modern)
    {
        "subtopic": "Modern Article 143 References (1991-2012)",
        "title_en": "Arrange the following modern Presidential references under Article 143 in chronological order:",
        "title_ta": "சரத்து 143-ன் கீழ் உள்ள பின்வரும் நவீன குடியரசுத் தலைவர் குறிப்புரைகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("In re Cauvery Water Disputes Tribunal Reference", "காவிரி நதிநீர் தகராறு தீர்ப்பாயம் குறிப்புரை", 1991),
            ("In re Special Reference No. 1 of 1998 (Third Judges Case / Collegium)", "1998-ன் சிறப்பு குறிப்புரை எண் 1 (மூன்றாவது நீதிபதிகள் வழக்கு / கொலீஜியம்)", 1998),
            ("In re Gujarat Assembly Election Reference under Article 174", "சரத்து 174-ன் கீழ் குஜராத் சட்டமன்றத் தேர்தல் குறிப்புரை", 2002),
            ("In re 2G Natural Resources Allocation Reference", "2ஜி இயற்கை வளங்கள் ஒதுக்கீடு குறிப்புரை", 2012)
        ],
        "shuffle_order": [4, 1, 3, 2] # 2012, 1991, 2002, 1998 -> sorted is 1991(2), 1998(4), 2002(3), 2012(1) -> 2 - 4 - 3 - 1
    },
    # 14: Emergency & Fundamental Rights Evolution
    {
        "subtopic": "Emergency & Article 21 Jurisprudence",
        "title_en": "Arrange the following constitutional events regarding Article 21 and the Attorney General's submissions in chronological order:",
        "title_ta": "சரத்து 21 மற்றும் தலைமை வழக்கறிஞரின் வாதங்கள் தொடர்பான பின்வரும் அரசியலமைப்பு நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("Proclamation of Internal Emergency under Article 352", "சரத்து 352-ன் கீழ் உள்நாட்டு அவசரநிலை பிரகடனம் செய்யப்படுதல்", 1975),
            ("ADM Jabalpur verdict upholding suspension of right to life", "வாழ்வுரிமை இடைநிறுத்தத்தை உறுதி செய்த ஏ.டி.எம். ஜபல்பூர் தீர்ப்பு", 1976),
            ("Enactment of 44th Constitutional Amendment protecting Articles 20 and 21", "சரத்துக்கள் 20 மற்றும் 21-ஐப் பாதுகாக்கும் 44-வது திருத்தச் சட்டம் இயற்றப்படுதல்", 1978),
            ("Puttaswamy judgment formally overruling ADM Jabalpur", "ஏ.டி.எம். ஜபல்பூர் தீர்ப்பை முறைப்படி ரத்து செய்த புட்டசாமி தீர்ப்பு", 2017)
        ],
        "shuffle_order": [3, 1, 4, 2] # 1978, 1975, 2017, 1976 -> sorted is 1975(2), 1976(4), 1978(1), 2017(3) -> 2 - 4 - 1 - 3
    },
    # 15: AGs of the 1960s-1970s
    {
        "subtopic": "Succession of 1960s-1970s AGs",
        "title_en": "Arrange the appointments of the following Attorneys General in chronological order:",
        "title_ta": "பின்வரும் தலைமை வழக்கறிஞர்களின் நியமனங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("Appointment of C.K. Daphtary", "சி.கே. தப்தாரி நியமிக்கப்படுதல்", 1963),
            ("Appointment of Niren De", "நீரேன் டே நியமிக்கப்படுதல்", 1968),
            ("Appointment of S.V. Gupte", "எஸ்.வி. குப்தே நியமிக்கப்படுதல்", 1977),
            ("Appointment of L.N. Sinha", "எல்.என். சின்ஹா நியமிக்கப்படுதல்", 1979)
        ],
        "shuffle_order": [4, 2, 1, 3] # 1979, 1968, 1963, 1977 -> sorted is 1963(3), 1968(2), 1977(4), 1979(1) -> 3 - 2 - 4 - 1
    },
    # 16: AGs of the 1980s-1990s
    {
        "subtopic": "Succession of 1980s-1990s AGs",
        "title_en": "Arrange the appointments of the following Law Officers as Attorney General in chronological order:",
        "title_ta": "பின்வரும் சட்ட அதிகாரிகள் தலைமை வழக்கறிஞராக நியமிக்கப்பட்டதை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("Appointment of K. Parasaran", "கே. பராசரன் நியமிக்கப்படுதல்", 1983),
            ("Appointment of Soli Sorabjee (1st term)", "சோலி சொராப்ஜி (முதல் முறை) நியமிக்கப்படுதல்", 1989),
            ("Appointment of G. Ramaswamy", "ஜி. ராமசுவாமி நியமிக்கப்படுதல்", 1990),
            ("Appointment of Milon K. Banerjee (1st term)", "மிலன் கே. பானர்ஜி (முதல் முறை) நியமிக்கப்படுதல்", 1992)
        ],
        "shuffle_order": [2, 4, 1, 3] # 1989, 1992, 1983, 1990 -> sorted is 1983(3), 1989(1), 1990(4), 1992(2) -> 3 - 1 - 4 - 2
    },
    # 17: AGs of the late 1990s-2000s
    {
        "subtopic": "Succession of 1990s-2000s AGs",
        "title_en": "Arrange the tenures of the following Attorneys General in chronological order:",
        "title_ta": "பின்வரும் தலைமை வழக்கறிஞர்களின் பதவிக்காலங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("Tenure of Ashok Desai begins", "அசோக் தேசாய் பதவிக்காலம் தொடங்குதல்", 1996),
            ("Tenure of Soli Sorabjee (2nd term) begins", "சோலி சொராப்ஜி (2-வது முறை) பதவிக்காலம் தொடங்குதல்", 1998),
            ("Tenure of Milon K. Banerjee (2nd term) begins", "மிலன் கே. பானர்ஜி (2-வது முறை) பதவிக்காலம் தொடங்குதல்", 2004),
            ("Tenure of G.E. Vahanvati begins", "ஜி.இ. வாகனவதி பதவிக்காலம் தொடங்குதல்", 2009)
        ],
        "shuffle_order": [3, 1, 4, 2] # 2004, 1996, 2009, 1998 -> sorted is 1996(2), 1998(4), 2004(1), 2009(3) -> 2 - 4 - 1 - 3
    },
    # 18: AGs from 2009 to Present
    {
        "subtopic": "Succession of 2009-Present AGs",
        "title_en": "Arrange the appointment of the following modern Attorneys General in chronological order:",
        "title_ta": "பின்வரும் நவீன தலைமை வழக்கறிஞர்களின் நியமனங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("Appointment of G.E. Vahanvati", "ஜி.இ. வாகனவதி நியமிக்கப்படுதல்", 2009),
            ("Appointment of Mukul Rohatgi", "முகுல் ரோஹத்கி நியமிக்கப்படுதல்", 2014),
            ("Appointment of K.K. Venugopal", "கே.கே. வேணுகோபால் நியமிக்கப்படுதல்", 2017),
            ("Appointment of R. Venkataramani", "ஆர். வெங்கடரமணி நியமிக்கப்படுதல்", 2022)
        ],
        "shuffle_order": [4, 1, 3, 2] # 2022, 2009, 2017, 2014 -> sorted is 2009(2), 2014(4), 2017(3), 2022(1) -> 2 - 4 - 3 - 1
    },
    # 19: Judicial Appointments Litigation
    {
        "subtopic": "Judges Cases Litigation",
        "title_en": "Arrange the following landmark 'Judges Cases' argued by successive Attorneys General in chronological order:",
        "title_ta": "அடுத்தடுத்த தலைமை வழக்கறிஞர்களால் வாதிடப்பட்ட பின்வரும் வரலாற்றுச் சிறப்புமிக்க 'நீதிபதிகள் வழக்குகளை' காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("First Judges Case (S.P. Gupta v. Union of India)", "முதலாவது நீதிபதிகள் வழக்கு (எஸ்.பி. குப்தா எதிர் இந்திய ஒன்றியம்)", 1981),
            ("Second Judges Case (SCAORA v. Union of India)", "இரண்டாவது நீதிபதிகள் வழக்கு (SCAORA எதிர் இந்திய ஒன்றியம்)", 1993),
            ("Third Judges Case (Special Reference under Article 143)", "மூன்றாவது நீதிபதிகள் வழக்கு (சரத்து 143-ன் கீழான சிறப்பு குறிப்புரை)", 1998),
            ("Fourth Judges Case (NJAC Act challenge)", "நான்காவது நீதிபதிகள் வழக்கு (NJAC சட்ட சவால் வழக்கு)", 2015)
        ],
        "shuffle_order": [2, 4, 1, 3] # 1993, 2015, 1981, 1998 -> sorted is 1981(3), 1993(1), 1998(4), 2015(2) -> 3 - 1 - 4 - 2
    },
    # 20: Cases Argued by K.K. Venugopal
    {
        "subtopic": "Litigation under K.K. Venugopal (2017-2022)",
        "title_en": "Arrange the following landmark judgments delivered during K.K. Venugopal's tenure as Attorney General in chronological order:",
        "title_ta": "கே.கே. வேணுகோபால் தலைமை வழக்கறிஞராக இருந்த காலத்தில் வழங்கப்பட்ட பின்வரும் முக்கியத் தீர்ப்புகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("Puttaswamy Privacy judgment (Right to privacy recognized)", "புட்டசாமி தீர்ப்பு (அந்தரங்க உரிமை அங்கீகரிக்கப்படுதல்)", 2017),
            ("Aadhaar Act Constitution Bench verdict", "ஆதார் சட்ட அரசியலமைப்பு அமர்வு தீர்ப்பு", 2018),
            ("Ayodhya Title Dispute final verdict", "அயோத்தி நிலத் தகராறு இறுதித் தீர்ப்பு", 2019),
            ("Janki Janhit verdict (103rd Amendment / EWS Quota upheld)", "ஜன்கி ஜன்ஹித் தீர்ப்பு (103-வது திருத்தம் / EWS இடஒதுக்கீடு உறுதி)", 2022)
        ],
        "shuffle_order": [4, 2, 1, 3] # 2022, 2018, 2017, 2019 -> sorted is 2017(3), 2018(2), 2019(4), 2022(1) -> 3 - 2 - 4 - 1
    },
    # 21: Cases Argued by Mukul Rohatgi
    {
        "subtopic": "Litigation under Mukul Rohatgi (2014-2017)",
        "title_en": "Arrange the following landmark constitutional events during Mukul Rohatgi's tenure as Attorney General in chronological order:",
        "title_ta": "முகுல் ரோஹத்கி தலைமை வழக்கறிஞராக இருந்த காலத்தில் நடைபெற்ற பின்வரும் முக்கிய அரசியலமைப்பு நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("Defending the 99th Constitutional Amendment (NJAC case hearings)", "99-வது அரசியலமைப்புத் திருத்தத்தை ஆதரித்து வாதாடுதல் (NJAC வழக்கு)", 2015),
            ("Arunachal Pradesh President's Rule hearings (Nabam Rebia case)", "அருணாச்சலப் பிரதேச குடியரசுத் தலைவர் ஆட்சி வழக்கு (நபம் ரெபியா)", 2016),
            ("Defending Union's stance on Demonetization before Supreme Court", "உச்ச நீதிமன்றத்தில் பணமதிப்பிழப்பு நடவடிக்கையை ஆதரித்து வாதாடுதல்", 2016),
            ("Arguments in Shayara Bano (Triple Talaq case)", "ஷயாரா பானோ வழக்கில் வாதங்கள் (முத்தலாக் வழக்கு)", 2017)
        ],
        "shuffle_order": [3, 1, 4, 2] # 2016(demonet), 2015, 2017, 2016(nabam) -> let's make months distinct:
        # Nabam Rebia is July 2016; Demonetization is Nov/Dec 2016.
        # sorted is 2015(2), July 2016(4), Nov 2016(1), 2017(3) -> 2 - 4 - 1 - 3
    },
    # 22: Federal Disputes Argued by AGs
    {
        "subtopic": "Federal Constitutional Litigation",
        "title_en": "Arrange the following landmark federal cases involving the Union of India and argued by Attorneys General in chronological order:",
        "title_ta": "தலைமை வழக்கறிஞர்களால் வாதிடப்பட்ட மத்திய அரசு சம்பந்தப்பட்ட பின்வரும் கூட்டாட்சி வழக்குகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("State of West Bengal v. Union of India (First Art 131 suit)", "மேற்கு வங்க அரசு எதிர் இந்திய ஒன்றியம் (முதல் சரத்து 131 வழக்கு)", 1963),
            ("State of Rajasthan v. Union of India (Dissolution of Assemblies)", "ராஜஸ்தான் அரசு எதிர் இந்திய ஒன்றியம் (சட்டமன்றங்கள் கலைப்பு வழக்கு)", 1977),
            ("S.R. Bommai v. Union of India (Judicial review of Article 356)", "எஸ்.ஆர். பொம்மை எதிர் இந்திய ஒன்றியம் (சரத்து 356 நீதிமன்ற மறுஆய்வு)", 1994),
            ("Government of NCT of Delhi v. Union of India (LG powers verdict)", "தில்லி அரசு எதிர் இந்திய ஒன்றியம் (துணைநிலை ஆளுநர் அதிகாரத் தீர்ப்பு)", 2018)
        ],
        "shuffle_order": [4, 1, 3, 2] # 2018, 1963, 1994, 1977 -> sorted is 1963(2), 1977(4), 1994(3), 2018(1) -> 2 - 4 - 3 - 1
    },
    # 23: RTI Controversy Chronology
    {
        "subtopic": "RTI Controversy Regarding AG Office",
        "title_en": "Arrange the following events concerning the application of the RTI Act to the Attorney General in chronological order:",
        "title_ta": "தலைமை வழக்கறிஞர் அலுவலகத்திற்கு RTI சட்டம் பொருந்துவது தொடர்பான பின்வரும் நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("Enactment of the Right to Information Act, 2005", "தகவல் அறியும் உரிமைச் சட்டம் 2005 இயற்றப்படுதல்", 2005),
            ("CIC decision declaring Attorney General as a 'public authority'", "தலைமை வழக்கறிஞர் ஒரு 'பொது அதிகாரம்' என CIC முடிவெடுத்தல்", 2008),
            ("Delhi High Court single bench ruling upholding CIC order", "CIC உத்தரவை உறுதி செய்த தில்லி உயர் நீதிமன்ற தனி நீதிபதி தீர்ப்பு", 2011),
            ("Supreme Court stay on Delhi HC order regarding AG RTI status", "AG RTI நிலை குறித்த தில்லி HC உத்தரவுக்கு உச்ச நீதிமன்றம் தடை விதித்தல்", 2015)
        ],
        "shuffle_order": [2, 4, 1, 3] # 2008, 2015, 2005, 2011 -> sorted is 2005(3), 2008(1), 2011(4), 2015(2) -> 3 - 1 - 4 - 2
    },
    # 24: Constitutional Amendment Defenses
    {
        "subtopic": "Constitutional Amendment Defenses",
        "title_en": "Arrange the following landmark constitutional amendments defended by Attorneys General before the Supreme Court in chronological order:",
        "title_ta": "உச்ச நீதிமன்றத்தில் தலைமை வழக்கறிஞர்களால் ஆதரித்து வாதிடப்பட்ட பின்வரும் முக்கிய அரசியலமைப்பு திருத்தங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("Defense of 1st Constitutional Amendment (Shankari Prasad case)", "1-வது அரசியலமைப்பு திருத்தத்தை ஆதரித்தல் (சங்கரி பிரசாத் வழக்கு)", 1951),
            ("Defense of 24th and 25th Constitutional Amendments (Kesavananda Bharati)", "24 மற்றும் 25-வது திருத்தங்களை ஆதரித்தல் (கேசவானந்த பாரதி)", 1973),
            ("Defense of 39th Constitutional Amendment (Indira Nehru Gandhi case)", "39-வது அரசியலமைப்பு திருத்தத்தை ஆதரித்தல் (இந்திரா நேரு காந்தி வழக்கு)", 1975),
            ("Defense of 99th Constitutional Amendment (NJAC case)", "99-வது அரசியலமைப்பு திருத்தத்தை ஆதரித்தல் (NJAC வழக்கு)", 2015)
        ],
        "shuffle_order": [3, 1, 4, 2] # 1975, 1951, 2015, 1973 -> sorted is 1951(2), 1973(4), 1975(1), 2015(3) -> 2 - 4 - 1 - 3
    },
    # 25: Landmark Verdicts under R. Venkataramani
    {
        "subtopic": "Landmark Verdicts under R. Venkataramani (2022-2024)",
        "title_en": "Arrange the following Supreme Court Constitution Bench verdicts delivered during R. Venkataramani's tenure as Attorney General in chronological order:",
        "title_ta": "ஆர். வெங்கடரமணி தலைமை வழக்கறிஞராக பதவி வகித்த போது வழங்கப்பட்ட பின்வரும் உச்ச நீதிமன்ற அரசியலமைப்பு அமர்வுத் தீர்ப்புகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "events": [
            ("Janki Janhit verdict upholding 10% EWS Reservation", "10% EWS இடஒதுக்கீட்டை உறுதி செய்த ஜன்கி ஜன்ஹித் தீர்ப்பு", 2022),
            ("Supriyo v. Union of India verdict (Same-Sex Marriage)", "சுப்ரியோ எதிர் இந்திய ஒன்றியம் தீர்ப்பு (ஒரே பாலின திருமணம்)", 2023),
            ("Verdict upholding Abrogation of Article 370 in J&K", "ஜம்மு காஷ்மீரில் சரத்து 370 ரத்தை உறுதி செய்த தீர்ப்பு", 2023),
            ("Association for Democratic Reforms verdict (Electoral Bonds struck down)", "தேர்தல் பத்திரத் திட்டத்தை ரத்து செய்த ADR தீர்ப்பு", 2024)
        ],
        "shuffle_order": [4, 1, 3, 2] # 2024, 2022, 2023(Dec), 2023(Oct) -> sorted is 2022(2), Oct 2023(4), Dec 2023(3), Feb 2024(1) -> 2 - 4 - 3 - 1
    }
]

def generate_chronology_permutations(correct_seq: list):
    """
    Generate 4 unique permutations where one is correct_seq,
    and NONE of them is [1, 2, 3, 4] if possible (correct_seq is guaranteed not [1, 2, 3, 4]).
    """
    all_perms = [
        [1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2],
        [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1],
        [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1],
        [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]
    ]
    
    # Filter out [1, 2, 3, 4] from options to be safe
    filtered = [p for p in all_perms if p != correct_seq and p != [1, 2, 3, 4]]
    random.seed(42 + sum(correct_seq))
    random.shuffle(filtered)
    
    distractors = filtered[:3]
    options_list = [correct_seq] + distractors
    # The correct one is at index 0 initially
    return options_list

def build_questions():
    questions = []
    
    for i, item in enumerate(raw_chronology_items):
        qid = f"AG_C_{i+1:03d}"
        
        # Determine presented order using shuffle_order (1-indexed)
        # shuffle_order gives the indices of events from item['events']
        s_order = item["shuffle_order"] # e.g. [3, 1, 4, 2]
        
        presented_events_en = []
        presented_events_ta = []
        presented_meta = [] # (original_index, label_en, label_ta, year)
        
        for p_idx, orig_1_idx in enumerate(s_order):
            orig_0_idx = orig_1_idx - 1
            lbl_en, lbl_ta, yr = item["events"][orig_0_idx]
            presented_events_en.append(f"{p_idx + 1}. {lbl_en}")
            presented_events_ta.append(f"{p_idx + 1}. {lbl_ta}")
            presented_meta.append((p_idx + 1, orig_0_idx, lbl_en, lbl_ta, yr))
            
        stem_en = f"{item['title_en']}\n" + "\n".join(presented_events_en)
        stem_ta = f"{item['title_ta']}\n" + "\n".join(presented_events_ta)
        
        # Now find the chronological order of presented numbers (1, 2, 3, 4)
        # Sort presented_meta by year (and original index if year ties)
        sorted_meta = sorted(presented_meta, key=lambda x: (x[4], x[1]))
        correct_seq = [x[0] for x in sorted_meta] # e.g. [2, 4, 1, 3]
        
        assert correct_seq != [1, 2, 3, 4], f"Presented order equals chronological order in {qid}!"
        
        # Build 4 permutation options
        opts_perms = generate_chronology_permutations(correct_seq)
        
        # Initially correct is at index 0 (option A)
        en_options = [" - ".join(str(d) for d in p) for p in opts_perms]
        ta_options = [" - ".join(str(d) for d in p) for p in opts_perms]
        
        # Format explanation with -> and 4-digit years
        exp_lines_en = [
            f"The correct chronological order is: {' -> '.join(str(d) for d in correct_seq)}.",
            "Key chronological dates and progression:"
        ]
        exp_lines_ta = [
            f"சரியான காலவரிசை ஒழுங்கு: {' -> '.join(str(d) for d in correct_seq)}.",
            "முக்கிய காலவரிசை நிகழ்வுகள்:"
        ]
        
        for step in sorted_meta:
            exp_lines_en.append(f"{step[0]}. {step[2]} ({step[4]})")
            exp_lines_ta.append(f"{step[0]}. {step[3]} ({step[4]})")
            
        exp_en = "\n".join(exp_lines_en)
        exp_ta = "\n".join(exp_lines_ta)
        
        why_en = {}
        why_ta = {}
        for idx, key in enumerate(["A", "B", "C", "D"]):
            if idx == 0:
                why_en[key] = f"Option {key} ({en_options[idx]}) accurately reflects the chronological sequence: {' -> '.join(str(d) for d in correct_seq)}."
                why_ta[key] = f"தெரிவு {key} ({ta_options[idx]}) சரியான காலவரிசையைத் துல்லியமாகப் பிரதிபலிக்கிறது: {' -> '.join(str(d) for d in correct_seq)}."
            else:
                why_en[key] = f"Option {key} ({en_options[idx]}) contains an incorrect chronological sequence."
                why_ta[key] = f"தெரிவு {key} ({ta_options[idx]}) தவறான காலவரிசையைக் கொண்டுள்ளது."
                
        q = make_ag_q(
            qid=qid,
            diff="Hard",
            qtype="Chronology",
            subtopic=item["subtopic"],
            en_stem=stem_en,
            ta_stem=stem_ta,
            en_a=en_options[0],
            ta_a=ta_options[0],
            en_b=en_options[1],
            ta_b=ta_options[1],
            en_c=en_options[2],
            ta_c=ta_options[2],
            en_d=en_options[3],
            ta_d=ta_options[3],
            correct_key="A",
            exp_en=exp_en,
            exp_ta=exp_ta,
            why_a_en=why_en["A"],
            why_a_ta=why_ta["A"],
            why_b_en=why_en["B"],
            why_b_ta=why_ta["B"],
            why_c_en=why_en["C"],
            why_c_ta=why_ta["C"],
            why_d_en=why_en["D"],
            why_d_ta=why_ta["D"],
            tip_en="Always memorize the sequential tenures and landmark constitutional cases of Attorneys General!",
            tip_ta="தலைமை வழக்கறிஞர்களின் தொடர்ச்சியான பதவிக்காலங்கள் மற்றும் முக்கிய வழக்குகளை எப்போதும் நினைவில் வையுங்கள்!",
            fact_en=f"Sequence: {' -> '.join(str(d) for d in correct_seq)} reflects historical dates from {sorted_meta[0][4]} to {sorted_meta[-1][4]}.",
            fact_ta=f"வரிசை: {' -> '.join(str(d) for d in correct_seq)} என்பது {sorted_meta[0][4]} முதல் {sorted_meta[-1][4]} வரையிலான வரலாற்று நிகழ்வுகளைக் குறிக்கிறது.",
            tags=["polity", "attorney_general_of_india", "chronology", item["subtopic"].lower().replace(" ", "_")]
        )
        questions.append(q)
        
    return questions

if __name__ == "__main__":
    qs = build_questions()
    print(f"Generated {len(qs)} raw Chronology questions.")
    
    # Verify raw questions with ChronologyValidator before rebalancing
    c_val = ChronologyValidator()
    c_report = c_val.validate_questions(qs)
    print("--- Pre-balance Chronology Audit ---")
    print(c_report.format_final_report())
    if not c_report.is_valid:
        for iss in c_report.issues:
            print("  Issue:", iss)
            
    # Balance keys across A, B, C, D
    balanced_qs = balance_question_keys(qs)
    
    # Audit after rebalancing
    c_report2 = c_val.validate_questions(balanced_qs)
    print("\n--- Post-balance Chronology Audit ---")
    print(c_report2.format_final_report())
    if not c_report2.is_valid:
        for iss in c_report2.issues:
            print("  Issue:", iss)
            
    out_path = os.path.join("data", "questions", "polity", "attorney_general_chronology.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_qs, f, ensure_ascii=False, indent=2)
        
    print(f"\nSaved balanced Chronology MCQs to {out_path}")
    
    # Standard ContentValidator check
    val = ContentValidator()
    report = val.validate_file(out_path, expected_count=25, expected_prefix="AG_C_")
    print(f"ContentValidator: {'PASS' if report.is_valid else 'FAIL'} | Total: {report.total_audited}")
    print(f"Key Distribution: {report.key_distribution}")
