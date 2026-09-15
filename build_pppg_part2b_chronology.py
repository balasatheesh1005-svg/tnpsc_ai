# -*- coding: utf-8 -*-
"""
Build 25 Chronology MCQs for Political Parties & Pressure Groups (PPPG_C_001 to PPPG_C_025)
TNPSC Nova AI Content Engine
"""
import json
import os
from collections import Counter
from political_parties_pressure_groups_mcq_helper import make_pppg_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset
from tools.nova_content_engine.chronology_validator import ChronologyValidator

def get_chronology_questions():
    questions = []

    # 25 Distinct, Authentic Chronology Scenarios with Non-Chronological Presentation Order
    # Format:
    # (num, subtopic, [ev1_en, ev2_en, ev3_en, ev4_en], [ev1_ta, ev2_ta, ev3_ta, ev4_ta],
    #  [optA, optB, optC, optD], correct_key, exp_en, exp_ta)
    # Ensure correct option is NOT "1 - 2 - 3 - 4" and all 4 options are unique permutations!

    chrono_data = [
        # C_001: 19th Century Pre-Independence Associations
        ("001", "Early Political Associations",
         ["1. Formation of the Indian Association by Surendranath Banerjee",
          "2. Establishment of the Landholders' Society in Calcutta",
          "3. Foundation of the Madras Mahajana Sabha",
          "4. Establishment of the East India Association by Dadabhai Naoroji in London"],
         ["1. சுரேந்திரநாத் பானர்ஜியால் இந்திய சங்கம் உருவாக்கப்பட்டது",
          "2. கொல்கத்தாவில் நிலப்பிரபுக்கள் சங்கம் தொடங்கப்பட்டது",
          "3. சென்னை மகாஜன சபை நிறுவப்பட்டது",
          "4. தாதாபாய் நௌரோஜியால் லண்டனில் கிழக்கு இந்திய சங்கம் தொடங்கப்பட்டது"],
         ["2 - 4 - 1 - 3", "4 - 2 - 1 - 3", "2 - 1 - 4 - 3", "1 - 2 - 4 - 3"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. Landholders' Society (1838)\n- 4. East India Association (1866)\n- 1. Indian Association (1876)\n- 3. Madras Mahajana Sabha (1884)\nChronological sequence: 2 (1838) → 4 (1866) → 1 (1876) → 3 (1884).",
         "சரியான காலவரிசை:\n- 2. நிலப்பிரபுக்கள் சங்கம் (1838)\n- 4. கிழக்கு இந்திய சங்கம் (1866)\n- 1. இந்திய சங்கம் (1876)\n- 3. சென்னை மகாஜன சபை (1884)\nவரிசை: 2 (1838) → 4 (1866) → 1 (1876) → 3 (1884)."),

        # C_002: Pre-Independence Major Political Parties
        ("002", "Pre-Independence Political Parties",
         ["1. Formation of the Communist Party of India (CPI)",
          "2. Foundation of the All India Muslim League",
          "3. Establishment of the Indian National Congress (INC)",
          "4. Foundation of the Congress Socialist Party (CSP)"],
         ["1. இந்திய கம்யூனிஸ்ட் கட்சி (CPI) தொடங்கப்பட்டது",
          "2. அகில இந்திய முஸ்லிம் லீக் நிறுவப்பட்டது",
          "3. இந்திய தேசிய காங்கிரஸ் (INC) உருவாக்கப்பட்டது",
          "4. காங்கிரஸ் சோசலிஸ்ட் கட்சி (CSP) தொடங்கப்பட்டது"],
         ["3 - 2 - 1 - 4", "2 - 3 - 1 - 4", "3 - 1 - 2 - 4", "1 - 3 - 2 - 4"], "A",
         "The correct chronological order with 4-digit years is:\n- 3. Indian National Congress (1885)\n- 2. All India Muslim League (1906)\n- 1. Communist Party of India (1925)\n- 4. Congress Socialist Party (1934)\nChronological sequence: 3 (1885) → 2 (1906) → 1 (1925) → 4 (1934).",
         "சரியான காலவரிசை:\n- 3. இந்திய தேசிய காங்கிரஸ் (1885)\n- 2. முஸ்லிம் லீக் (1906)\n- 1. இந்திய கம்யூனிஸ்ட் கட்சி (1925)\n- 4. காங்கிரஸ் சோசலிஸ்ட் கட்சி (1934)\nவரிசை: 3 (1885) → 2 (1906) → 1 (1925) → 4 (1934)."),

        # C_003: Trade Union Movement Milestones
        ("003", "Trade Union Federation Milestones",
         ["1. Formation of the Indian National Trade Union Congress (INTUC)",
          "2. Establishment of India's first organized union: Madras Labour Union",
          "3. Foundation of Centre of Indian Trade Unions (CITU)",
          "4. Foundation of the All India Trade Union Congress (AITUC)"],
         ["1. இந்திய தேசிய தொழிற்சங்க காங்கிரஸ் (INTUC) உருவாக்கப்பட்டது",
          "2. இந்தியாவின் முதல் தொழிற்சங்கமான சென்னை தொழிலாளர் சங்கம் அமைக்கப்பட்டது",
          "3. இந்திய தொழிற்சங்க மையம் (CITU) தொடங்கப்பட்டது",
          "4. அகில இந்திய தொழிற்சங்க காங்கிரஸ் (AITUC) தொடங்கப்பட்டது"],
         ["2 - 4 - 1 - 3", "4 - 2 - 1 - 3", "2 - 1 - 4 - 3", "1 - 2 - 4 - 3"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. Madras Labour Union (1918)\n- 4. All India Trade Union Congress (1920)\n- 1. Indian National Trade Union Congress (1947)\n- 3. Centre of Indian Trade Unions (1970)\nChronological sequence: 2 (1918) → 4 (1920) → 1 (1947) → 3 (1970).",
         "சரியான காலவரிசை:\n- 2. சென்னை தொழிலாளர் சங்கம் (1918)\n- 4. அகில இந்திய தொழிற்சங்க காங்கிரஸ் (1920)\n- 1. இந்திய தேசிய தொழிற்சங்க காங்கிரஸ் (1947)\n- 3. இந்திய தொழிற்சங்க மையம் (1970)\nவரிசை: 2 (1918) → 4 (1920) → 1 (1947) → 3 (1970)."),

        # C_004: Historic Peasant / Agrarian Satyagrahas
        ("004", "Peasant Movements and Satyagrahas",
         ["1. Bardoli Satyagraha under Sardar Vallabhbhai Patel",
          "2. Champaran Indigo Satyagraha led by Mahatma Gandhi",
          "3. Establishment of All India Kisan Sabha at Lucknow",
          "4. Kheda Peasant Satyagraha in Gujarat"],
         ["1. சர்தார் வல்லபாய் படேல் தலைமையில் பர்தோலி சத்தியாகிரகம்",
          "2. மகாத்மா காந்தி தலைமையில் சம்பாரண் அவுரி சத்தியாகிரகம்",
          "3. லக்னோவில் அகில இந்திய கிசான் சபா தொடங்கப்பட்டது",
          "4. குஜராத்தில் கேதா விவசாயிகள் சத்தியாகிரகம்"],
         ["2 - 4 - 1 - 3", "4 - 2 - 1 - 3", "2 - 1 - 4 - 3", "1 - 4 - 2 - 3"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. Champaran Satyagraha (1917)\n- 4. Kheda Satyagraha (1918)\n- 1. Bardoli Satyagraha (1928)\n- 3. All India Kisan Sabha (1936)\nChronological sequence: 2 (1917) → 4 (1918) → 1 (1928) → 3 (1936).",
         "சரியான காலவரிசை:\n- 2. சம்பாரண் சத்தியாகிரகம் (1917)\n- 4. கேதா சத்தியாகிரகம் (1918)\n- 1. பர்தோலி சத்தியாகிரகம் (1928)\n- 3. அகில இந்திய கிசான் சபா (1936)\nவரிசை: 2 (1917) → 4 (1918) → 1 (1928) → 3 (1936)."),

        # C_005: Evolution of Dravidian Parties in Tamil Nadu
        ("005", "Dravidian Parties in Tamil Nadu",
         ["1. Formation of All India Anna Dravida Munnetra Kazhagam (AIADMK) by MGR",
          "2. Formation of South Indian Liberal Federation (Justice Party)",
          "3. Formation of Marumalarchi Dravida Munnetra Kazhagam (MDMK)",
          "4. Foundation of Dravida Munnetra Kazhagam (DMK) by C.N. Annadurai"],
         ["1. எம்.ஜி.ஆரால் அனைத்திந்திய அண்ணா திராவிட முன்னேற்றக் கழகம் தொடங்கப்பட்டது",
          "2. தென்னிந்திய நல உரிமைச் சங்கம் (நீதிக் கட்சி) தொடங்கப்பட்டது",
          "3. மறுமலர்ச்சி திராவிட முன்னேற்றக் கழகம் (MDMK) தொடங்கப்பட்டது",
          "4. சி.என். அண்ணாதுரையால் திராவிட முன்னேற்றக் கழகம் (DMK) தொடங்கப்பட்டது"],
         ["2 - 4 - 1 - 3", "4 - 2 - 1 - 3", "2 - 1 - 4 - 3", "1 - 2 - 4 - 3"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. Justice Party (1916)\n- 4. Dravida Munnetra Kazhagam (1949)\n- 1. AIADMK (1972)\n- 3. MDMK (1994)\nChronological sequence: 2 (1916) → 4 (1949) → 1 (1972) → 3 (1994).",
         "சரியான காலவரிசை:\n- 2. நீதிக் கட்சி (1916)\n- 4. திமுக (1949)\n- 1. அதிமுக (1972)\n- 3. மதிமுக (1994)\nவரிசை: 2 (1916) → 4 (1949) → 1 (1972) → 3 (1994)."),

        # C_006: Evolution of Apex Business Pressure Groups
        ("006", "Apex Business Chambers",
         ["1. Establishment of Associated Chambers of Commerce and Industry of India (ASSOCHAM)",
          "2. Founding of Engineering and Iron Trades Association (earliest precursor of CII)",
          "3. Formation of All India Manufacturers' Organisation (AIMO) by M. Visvesvaraya",
          "4. Foundation of Federation of Indian Chambers of Commerce and Industry (FICCI)"],
         ["1. இந்திய இணைந்த வர்த்தக மற்றும் தொழிற்துறை கூட்டமைப்பு (ASSOCHAM) நிறுவப்பட்டது",
          "2. பொறியியல் மற்றும் இரும்பு வர்த்தக சங்கம் (CII-ன் தொடக்க அமைப்பு) உருவானது",
          "3. எம். விஸ்வேஸ்வரய்யாவால் அகில இந்திய உற்பத்தியாளர்கள் சங்கம் (AIMO) உருவாக்கப்பட்டது",
          "4. இந்திய வர்த்தக மற்றும் தொழிற்துறை கூட்டமைப்பு (FICCI) நிறுவப்பட்டது"],
         ["2 - 1 - 4 - 3", "1 - 2 - 4 - 3", "2 - 4 - 1 - 3", "4 - 2 - 1 - 3"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. Precursor of CII (1895)\n- 1. ASSOCHAM (1920)\n- 4. FICCI (1927)\n- 3. AIMO (1941)\nChronological sequence: 2 (1895) → 1 (1920) → 4 (1927) → 3 (1941).",
         "சரியான காலவரிசை:\n- 2. CII தொடக்க அமைப்பு (1895)\n- 1. ASSOCHAM (1920)\n- 4. FICCI (1927)\n- 3. AIMO (1941)\nவரிசை: 2 (1895) → 1 (1920) → 4 (1927) → 3 (1941)."),

        # C_007: Evolution of Prominent Regional Parties
        ("007", "Prominent Regional Parties",
         ["1. Formation of Telugu Desam Party (TDP) in Andhra Pradesh",
          "2. Foundation of Shiromani Akali Dal (SAD) in Punjab",
          "3. Establishment of Asom Gana Parishad (AGP) in Assam",
          "4. Founding of Biju Janata Dal (BJD) in Odisha"],
         ["1. ஆந்திரப் பிரதேசத்தில் தெலுங்கு தேசம் கட்சி தொடங்கப்பட்டது",
          "2. பஞ்சாபில் சிரோமணி அகாலி தளம் தொடங்கப்பட்டது",
          "3. அசாமில் அசோம் கண பரிஷத் தொடங்கப்பட்டது",
          "4. ஒடிசாவில் பிஜு ஜனதா தளம் தொடங்கப்பட்டது"],
         ["2 - 1 - 3 - 4", "1 - 2 - 3 - 4", "2 - 3 - 1 - 4", "3 - 2 - 1 - 4"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. Shiromani Akali Dal (1920)\n- 1. Telugu Desam Party (1982)\n- 3. Asom Gana Parishad (1985)\n- 4. Biju Janata Dal (1997)\nChronological sequence: 2 (1920) → 1 (1982) → 3 (1985) → 4 (1997).",
         "சரியான காலவரிசை:\n- 2. சிரோமணி அகாலி தளம் (1920)\n- 1. தெலுங்கு தேசம் (1982)\n- 3. அசோம் கண பரிஷத் (1985)\n- 4. பிஜு ஜனதா தளம் (1997)\nவரிசை: 2 (1920) → 1 (1982) → 3 (1985) → 4 (1997)."),

        # C_008: Formation of Student Pressure Groups
        ("008", "Student Organizations",
         ["1. Formation of Students' Federation of India (SFI)",
          "2. Foundation of All India Students' Federation (AISF)",
          "3. Establishment of National Students' Union of India (NSUI)",
          "4. Founding of Akhil Bharatiya Vidyarthi Parishad (ABVP)"],
         ["1. இந்திய மாணவர் கூட்டமைப்பு (SFI) உருவாக்கப்பட்டது",
          "2. அகில இந்திய மாணவர் பெருமன்றம் (AISF) தொடங்கப்பட்டது",
          "3. இந்திய தேசிய மாணவர் ஒன்றியம் (NSUI) அமைக்கப்பட்டது",
          "4. அகில பாரதிய வித்யார்த்தி பரிஷத் (ABVP) உருவாக்கப்பட்டது"],
         ["2 - 4 - 1 - 3", "4 - 2 - 1 - 3", "2 - 1 - 4 - 3", "1 - 2 - 4 - 3"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. All India Students' Federation (1936)\n- 4. Akhil Bharatiya Vidyarthi Parishad (1949)\n- 1. Students' Federation of India (1970)\n- 3. National Students' Union of India (1971)\nChronological sequence: 2 (1936) → 4 (1949) → 1 (1970) → 3 (1971).",
         "சரியான காலவரிசை:\n- 2. AISF (1936)\n- 4. ABVP (1949)\n- 1. SFI (1970)\n- 3. NSUI (1971)\nவரிசை: 2 (1936) → 4 (1949) → 1 (1970) → 3 (1971)."),

        # C_009: Environmental Pressure Movements
        ("009", "Environmental Movements",
         ["1. Launch of Appiko Movement in the Western Ghats of Karnataka",
          "2. Beginning of Chipko Movement in Uttarakhand",
          "3. Formation of Narmada Bachao Andolan led by Medha Patkar",
          "4. Launch of Silent Valley Movement in Kerala"],
         ["1. கர்நாடகாவின் மேற்குத் தொடர்ச்சி மலையில் அப்பிகோ இயக்கம் தொடங்கப்பட்டது",
          "2. உத்தராகண்டில் சிப்கோ இயக்கம் தொடங்கியது",
          "3. மேதா பட்கர் தலைமையில் நர்மதா பச்சாவோ அந்தோலன் உருவாக்கப்பட்டது",
          "4. கேரளாவில் அமைதிப் பள்ளத்தாக்கு இயக்கம் தொடங்கப்பட்டது"],
         ["2 - 4 - 1 - 3", "4 - 2 - 1 - 3", "2 - 1 - 4 - 3", "1 - 2 - 4 - 3"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. Chipko Movement (1973)\n- 4. Silent Valley Movement (1978)\n- 1. Appiko Movement (1983)\n- 3. Narmada Bachao Andolan (1985)\nChronological sequence: 2 (1973) → 4 (1978) → 1 (1983) → 3 (1985).",
         "சரியான காலவரிசை:\n- 2. சிப்கோ இயக்கம் (1973)\n- 4. அமைதிப் பள்ளத்தாக்கு இயக்கம் (1978)\n- 1. அப்பிகோ இயக்கம் (1983)\n- 3. நர்மதா பச்சாவோ அந்தோலன் (1985)\nவரிசை: 2 (1973) → 4 (1978) → 1 (1983) → 3 (1985)."),

        # C_010: Statutory and Constitutional Milestones of Parties
        ("010", "Statutory Framework of Parties",
         ["1. Insertion of Section 29A into RPA 1951 for registration of political parties",
          "2. Promulgation of Election Symbols (Reservation and Allotment) Order",
          "3. Enactment of the Representation of the People Act",
          "4. Enactment of 52nd Constitutional Amendment Act (Anti-Defection Law)"],
         ["1. கட்சிகள் பதிவிற்காக மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ல் பிரிவு 29A சேர்க்கப்பட்டது",
          "2. தேர்தல் சின்னங்கள் (ஒதுக்கீடு மற்றும் பங்கீடு) ஆணை பிறப்பிக்கப்பட்டது",
          "3. மக்கள் பிரதிநிதித்துவச் சட்டம் இயற்றப்பட்டது",
          "4. 52வது அரசியலமைப்பு திருத்தச் சட்டம் (கட்சித் தாவல் தடைச் சட்டம்) இயற்றப்பட்டது"],
         ["3 - 2 - 4 - 1", "2 - 3 - 4 - 1", "3 - 4 - 2 - 1", "4 - 3 - 2 - 1"], "A",
         "The correct chronological order with 4-digit years is:\n- 3. Representation of the People Act (1951)\n- 2. Election Symbols Order (1968)\n- 4. 52nd Amendment Act (1985)\n- 1. Section 29A inserted (1988)\nChronological sequence: 3 (1951) → 2 (1968) → 4 (1985) → 1 (1988).",
         "சரியான காலவரிசை:\n- 3. மக்கள் பிரதிநிதித்துவச் சட்டம் (1951)\n- 2. தேர்தல் சின்னங்கள் ஆணை (1968)\n- 4. 52வது திருத்தச் சட்டம் (1985)\n- 1. பிரிவு 29A சேர்க்கை (1988)\nவரிசை: 3 (1951) → 2 (1968) → 4 (1985) → 1 (1988)."),

        # C_011: Electoral Reform Committees on Parties
        ("011", "Electoral Reform Committees",
         ["1. Indrajit Gupta Committee recommendations on State Funding of Elections",
          "2. Tarkunde Committee appointed by Jayaprakash Narayan on electoral reforms",
          "3. Law Commission of India 255th Report on Electoral Reforms",
          "4. Dinesh Goswami Committee Report on Electoral Reforms"],
         ["1. தேர்தல் அரசு நிதி குறித்து இந்திரஜித் குப்தா குழு பரிந்துரை",
          "2. ஜெயபிரகாஷ் நாராயணால் நியமிக்கப்பட்ட தர்குண்டே குழு அறிக்கை",
          "3. இந்திய சட்ட ஆணையத்தின் 255வது தேர்தல் சீர்திருத்த அறிக்கை",
          "4. தேர்தல் சீர்திருத்தங்கள் குறித்த தினேஷ் கோஸ்வாமி குழு அறிக்கை"],
         ["2 - 4 - 1 - 3", "4 - 2 - 1 - 3", "2 - 1 - 4 - 3", "1 - 2 - 4 - 3"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. Tarkunde Committee (1974)\n- 4. Dinesh Goswami Committee (1990)\n- 1. Indrajit Gupta Committee (1998)\n- 3. Law Commission 255th Report (2015)\nChronological sequence: 2 (1974) → 4 (1990) → 1 (1998) → 3 (2015).",
         "சரியான காலவரிசை:\n- 2. தர்குண்டே குழு (1974)\n- 4. தினேஷ் கோஸ்வாமி குழு (1990)\n- 1. இந்திரஜித் குப்தா குழு (1998)\n- 3. சட்ட ஆணையம் 255வது அறிக்கை (2015)\nவரிசை: 2 (1974) → 4 (1990) → 1 (1998) → 3 (2015)."),

        # C_012: Formation of Major National Parties (Post-1970)
        ("012", "Post-1970 National Parties",
         ["1. Formation of Bharatiya Janata Party (BJP) under Atal Bihari Vajpayee",
          "2. Formation of the unified Janata Party",
          "3. Foundation of Aam Aadmi Party (AAP) by Arvind Kejriwal",
          "4. Formation of Bahujan Samaj Party (BSP) by Kanshi Ram"],
         ["1. வாஜ்பாய் தலைமையில் பாரதிய ஜனதா கட்சி (BJP) தொடங்கப்பட்டது",
          "2. ஒருங்கிணைந்த ஜனதா கட்சி உருவானது",
          "3. அரவிந்த் கெஜ்ரிவாலால் ஆம் ஆத்மி கட்சி (AAP) தொடங்கப்பட்டது",
          "4. கன்ஷிராமால் பகுஜன் சமாஜ் கட்சி (BSP) தொடங்கப்பட்டது"],
         ["2 - 1 - 4 - 3", "1 - 2 - 4 - 3", "2 - 4 - 1 - 3", "4 - 2 - 1 - 3"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. Janata Party (1977)\n- 1. Bharatiya Janata Party (1980)\n- 4. Bahujan Samaj Party (1984)\n- 3. Aam Aadmi Party (2012)\nChronological sequence: 2 (1977) → 1 (1980) → 4 (1984) → 3 (2012).",
         "சரியான காலவரிசை:\n- 2. ஜனதா கட்சி (1977)\n- 1. பாரதிய ஜனதா கட்சி (1980)\n- 4. பகுஜன் சமாஜ் கட்சி (1984)\n- 3. ஆம் ஆத்மி கட்சி (2012)\nவரிசை: 2 (1977) → 1 (1980) → 4 (1984) → 3 (2012)."),

        # C_013: Landmark Supreme Court Rulings on Parties & Elections
        ("013", "Judicial Rulings on Elections",
         ["1. Lily Thomas v. Union of India striking down Section 8(4) of RPA",
          "2. Sadiq Ali v. Election Commission of India establishing numerical test for symbols",
          "3. Union of India v. ADR mandating disclosure of candidate background and wealth",
          "4. ADR v. Union of India striking down the Electoral Bonds Scheme"],
         ["1. மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 8(4)-ஐ ரத்து செய்த லில்லி தாமஸ் வழக்கு",
          "2. சின்னங்கள் தகராறில் பெரும்பான்மை சோதனையை நிறுவிய சாதிக் அலி வழக்கு",
          "3. வேட்பாளர்களின் சொத்து மற்றும் குற்றப்பின்னணியை அறிவிக்க உத்தரவிட்ட ADR வழக்கு",
          "4. தேர்தல் பத்திரத் திட்டத்தை ரத்து செய்த ADR எதிர் இந்திய யூனியன் வழக்கு"],
         ["2 - 3 - 1 - 4", "3 - 2 - 1 - 4", "2 - 1 - 3 - 4", "1 - 2 - 3 - 4"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. Sadiq Ali Case (1972)\n- 3. Association for Democratic Reforms Case (2002)\n- 1. Lily Thomas Case (2013)\n- 4. Electoral Bonds Verdict (2024)\nChronological sequence: 2 (1972) → 3 (2002) → 1 (2013) → 4 (2024).",
         "சரியான காலவரிசை:\n- 2. சாதிக் அலி வழக்கு (1972)\n- 3. ADR வழக்கு (2002)\n- 1. லில்லி தாமஸ் வழக்கு (2013)\n- 4. தேர்தல் பத்திர தீர்ப்பு (2024)\nவரிசை: 2 (1972) → 3 (2002) → 1 (2013) → 4 (2024)."),

        # C_014: Dalit and Backward Classes Organizations
        ("014", "Social Justice Pressure Groups",
         ["1. Formation of Dalit Panthers in Maharashtra by Namdeo Dhasal",
          "2. Establishment of Sri Narayana Dharma Paripalana (SNDP) Yogam in Kerala",
          "3. Foundation of Bahujan Samaj Party (BSP)",
          "4. Formation of All India Backward and Minority Communities Employees Federation (BAMCEF)"],
         ["1. மகாராஷ்டிராவில் நாம்தேவ் தாசலால் தலித் பாந்தர்ஸ் தொடங்கப்பட்டது",
          "2. கேரளாவில் ஸ்ரீ நாராயண தர்ம பரிபாலன (SNDP) யோகம் நிறுவப்பட்டது",
          "3. பகுஜன் சமாஜ் கட்சி (BSP) தொடங்கப்பட்டது",
          "4. BAMCEF கூட்டமைப்பு அமைக்கப்பட்டது"],
         ["2 - 1 - 4 - 3", "1 - 2 - 4 - 3", "2 - 4 - 1 - 3", "4 - 2 - 1 - 3"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. SNDP Yogam (1903)\n- 1. Dalit Panthers (1972)\n- 4. BAMCEF (1978)\n- 3. Bahujan Samaj Party (1984)\nChronological sequence: 2 (1903) → 1 (1972) → 4 (1978) → 3 (1984).",
         "சரியான காலவரிசை:\n- 2. SNDP யோகம் (1903)\n- 1. தலித் பாந்தர்ஸ் (1972)\n- 4. BAMCEF (1978)\n- 3. பகுஜன் சமாஜ் (1984)\nவரிசை: 2 (1903) → 1 (1972) → 4 (1978) → 3 (1984)."),

        # C_015: Left Movements & Party Splits
        ("015", "Left Parties Evolution",
         ["1. Formation of Communist Party of India (Marxist-Leninist) [CPI(ML)]",
          "2. Foundation of the Communist Party of India (CPI)",
          "3. Formation of Revolutionary Socialist Party (RSP)",
          "4. Major ideological split in CPI leading to the formation of CPI(M)"],
         ["1. இந்திய கம்யூனிஸ்ட் கட்சி (மார்க்சிஸ்ட்-லெனினிஸ்ட்) உருவானது",
          "2. இந்திய கம்யூனிஸ்ட் கட்சி (CPI) தொடங்கப்பட்டது",
          "3. புரட்சிகர சோசலிஸ்ட் கட்சி (RSP) உருவானது",
          "4. சிபிஐ பிளவுபட்டு மார்க்சிஸ்ட் கம்யூனிஸ்ட் கட்சி (CPI(M)) உருவானது"],
         ["2 - 3 - 4 - 1", "3 - 2 - 4 - 1", "2 - 4 - 3 - 1", "4 - 2 - 3 - 1"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. CPI Foundation (1925)\n- 3. RSP Foundation (1940)\n- 4. CPI(M) Formation (1964)\n- 1. CPI(ML) Formation (1969)\nChronological sequence: 2 (1925) → 3 (1940) → 4 (1964) → 1 (1969).",
         "சரியான காலவரிசை:\n- 2. சிபிஐ தோற்றம் (1925)\n- 3. RSP தோற்றம் (1940)\n- 4. சிபிஎம் உருவாக்கம் (1964)\n- 1. சிபிஐ(எம்எல்) தோற்றம் (1969)\nவரிசை: 2 (1925) → 3 (1940) → 4 (1964) → 1 (1969)."),

        # C_016: Modern Farmers' Movement Organizations
        ("016", "Modern Agrarian Pressure Groups",
         ["1. Formation of Bharatiya Kisan Union (BKU) under Mahendra Singh Tikait",
          "2. Foundation of Shetkari Sanghatana in Maharashtra by Sharad Joshi",
          "3. Historic Repeal of the three Central Farm Acts after nationwide protests",
          "4. Formation of Karnataka Rajya Raitha Sangha (KRRS) by M.D. Nanjundaswamy"],
         ["1. மகேந்திர சிங் திகாயத் தலைமையில் பாரதிய கிசான் யூனியன் (BKU) தொடங்கப்பட்டது",
          "2. சரத் ஜோஷியால் மகாராஷ்டிராவில் ஷேத்காரி சங்கடனா தொடங்கப்பட்டது",
          "3. நாடு தழுவிய விவசாயிகள் போராட்டத்திற்குப் பின் மூன்று வேளாண் சட்டங்கள் ரத்து",
          "4. எம்.டி. நஞ்சுண்டசுவாமியால் கர்நாடக மாநில ரைத சங்க (KRRS) அமைக்கப்பட்டது"],
         ["2 - 4 - 1 - 3", "4 - 2 - 1 - 3", "2 - 1 - 4 - 3", "1 - 2 - 4 - 3"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. Shetkari Sanghatana (1979)\n- 4. KRRS (1980)\n- 1. Bharatiya Kisan Union (1987)\n- 3. Repeal of Farm Laws (2021)\nChronological sequence: 2 (1979) → 4 (1980) → 1 (1987) → 3 (2021).",
         "சரியான காலவரிசை:\n- 2. ஷேத்காரி சங்கடனா (1979)\n- 4. KRRS (1980)\n- 1. பாரதிய கிசான் யூனியன் (1987)\n- 3. வேளாண் சட்டங்கள் ரத்து (2021)\nவரிசை: 2 (1979) → 4 (1980) → 1 (1987) → 3 (2021)."),

        # C_017: Civil Society and Rights Groups
        ("017", "Civil Society Rights Movements",
         ["1. Formation of People's Union for Democratic Rights (PUDR)",
          "2. Foundation of People's Union for Civil Liberties (PUCL) by JP Narayan",
          "3. Establishment of National Human Rights Commission (NHRC) by Parliament",
          "4. Enactment of Right to Information (RTI) Act spearheaded by MKSS"],
         ["1. மக்கள் ஜனநாயக உரிமைக் கூட்டமைப்பு (PUDR) தொடங்கப்பட்டது",
          "2. ஜெயபிரகாஷ் நாராயணால் மக்கள் சிவில் உரிமைக் கூட்டமைப்பு (PUCL) நிறுவப்பட்டது",
          "3. நாடாளுமன்றச் சட்டத்தால் தேசிய மனித உரிமைகள் ஆணையம் அமைக்கப்பட்டது",
          "4. MKSS இயக்கத்தின் தொடர் போராட்டத்தால் தகவல் அறியும் உரிமைச் சட்டம் இயற்றப்பட்டது"],
         ["2 - 1 - 3 - 4", "1 - 2 - 3 - 4", "2 - 3 - 1 - 4", "3 - 2 - 1 - 4"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. PUCL (1976)\n- 1. PUDR (1981)\n- 3. NHRC (1993)\n- 4. RTI Act (2005)\nChronological sequence: 2 (1976) → 1 (1981) → 3 (1993) → 4 (2005).",
         "சரியான காலவரிசை:\n- 2. PUCL (1976)\n- 1. PUDR (1981)\n- 3. NHRC (1993)\n- 4. தகவல் அறியும் உரிமைச் சட்டம் (2005)\nவரிசை: 2 (1976) → 1 (1981) → 3 (1993) → 4 (2005)."),

        # C_018: Religious and Cultural Pressure Groups
        ("018", "Religious Pressure Groups",
         ["1. Foundation of Jamaat-e-Islami Hind",
          "2. Establishment of Shiromani Gurdwara Parbandhak Committee (SGPC)",
          "3. Formation of Vishva Hindu Parishad (VHP)",
          "4. Foundation of Rashtriya Swayamsevak Sangh (RSS) by Dr. K.B. Hedgewar"],
         ["1. ஜமாத்-இ-இஸ்லாமி ஹிந்த் தொடங்கப்பட்டது",
          "2. சிரோமணி குருத்வாரா பிரபந்தக் குழு (SGPC) அமைக்கப்பட்டது",
          "3. விஸ்வ ஹிந்து பரிஷத் (VHP) தொடங்கப்பட்டது",
          "4. டாக்டர் ஹெட்கேவாரால் ராஷ்ட்ரிய சுயம்சேவக் சங்கம் (RSS) நிறுவப்பட்டது"],
         ["2 - 4 - 1 - 3", "4 - 2 - 1 - 3", "2 - 1 - 4 - 3", "1 - 2 - 4 - 3"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. SGPC (1920)\n- 4. RSS (1925)\n- 1. Jamaat-e-Islami Hind (1948)\n- 3. Vishva Hindu Parishad (1964)\nChronological sequence: 2 (1920) → 4 (1925) → 1 (1948) → 3 (1964).",
         "சரியான காலவரிசை:\n- 2. SGPC (1920)\n- 4. ஆர்எஸ்எஸ் (1925)\n- 1. ஜமாத்-இ-இஸ்லாமி (1948)\n- 3. விஸ்வ ஹிந்து பரிஷத் (1964)\nவரிசை: 2 (1920) → 4 (1925) → 1 (1948) → 3 (1964)."),

        # C_019: Women's Organizations and Political Rights
        ("019", "Women's Movements and Empowerment",
         ["1. Establishment of Self-Employed Women's Association (SEWA) by Ela Bhatt",
          "2. Foundation of All India Women's Conference (AIWC)",
          "3. Constitution of National Commission for Women (NCW)",
          "4. Enactment of Nari Shakti Vandan Adhiniyam (106th Amendment Act) for 33% reservation"],
         ["1. இலா பட்டால் சுயதொழில் மகளிர் சங்கம் (SEWA) நிறுவப்பட்டது",
          "2. அகில இந்திய பெண்கள் மாநாடு (AIWC) தொடங்கப்பட்டது",
          "3. தேசிய மகளிர் ஆணையம் (NCW) அமைக்கப்பட்டது",
          "4. 33% இடஒதுக்கீடுக்கான நாரி சக்தி வந்தன் அதினியம் (106வது திருத்தச் சட்டம்) இயற்றப்பட்டது"],
         ["2 - 1 - 3 - 4", "1 - 2 - 3 - 4", "2 - 3 - 1 - 4", "3 - 2 - 1 - 4"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. AIWC (1927)\n- 1. SEWA (1972)\n- 3. National Commission for Women (1992)\n- 4. 106th Amendment Act (2023)\nChronological sequence: 2 (1927) → 1 (1972) → 3 (1992) → 4 (2023).",
         "சரியான காலவரிசை:\n- 2. AIWC (1927)\n- 1. SEWA (1972)\n- 3. தேசிய மகளிர் ஆணையம் (1992)\n- 4. 106வது திருத்தச் சட்டம் (2023)\nவரிசை: 2 (1927) → 1 (1972) → 3 (1992) → 4 (2023)."),

        # C_020: Regional Splinter & State Parties in North/East India
        ("020", "Regional Parties Formation in 1990s",
         ["1. Formation of Rashtriya Janata Dal (RJD) in Bihar by Lalu Prasad Yadav",
          "2. Formation of Samajwadi Party (SP) in Uttar Pradesh by Mulayam Singh Yadav",
          "3. Foundation of All India Trinamool Congress (AITC) by Mamata Banerjee",
          "4. Formation of Nationalist Congress Party (NCP) by Sharad Pawar"],
         ["1. பீகாரில் லாலு பிரசாத் யாதவால் ராஷ்ட்ரிய ஜனதா தளம் (RJD) தொடங்கப்பட்டது",
          "2. உத்தரப் பிரதேசத்தில் முலாயம் சிங் யாதவால் சமாஜ்வாதி கட்சி (SP) தொடங்கப்பட்டது",
          "3. மம்தா பானர்ஜியால் அகில இந்திய திரிணாமுல் காங்கிரஸ் தொடங்கப்பட்டது",
          "4. சரத் பவாரால் தேசியவாத காங்கிரஸ் கட்சி (NCP) தொடங்கப்பட்டது"],
         ["2 - 1 - 3 - 4", "1 - 2 - 3 - 4", "2 - 3 - 1 - 4", "3 - 2 - 1 - 4"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. Samajwadi Party (1992)\n- 1. Rashtriya Janata Dal (1997)\n- 3. All India Trinamool Congress (1998)\n- 4. Nationalist Congress Party (1999)\nChronological sequence: 2 (1992) → 1 (1997) → 3 (1998) → 4 (1999).",
         "சரியான காலவரிசை:\n- 2. சமாஜ்வாதி கட்சி (1992)\n- 1. ராஷ்ட்ரிய ஜனதா தளம் (1997)\n- 3. திரிணாமுல் காங்கிரஸ் (1998)\n- 4. தேசியவாத காங்கிரஸ் (1999)\nவரிசை: 2 (1992) → 1 (1997) → 3 (1998) → 4 (1999)."),

        # C_021: ECI Election Reforms & Recognition Rules
        ("021", "ECI Electoral Reforms & Symbols Notifications",
         ["1. National People's Party (NPP) recognized as National Party",
          "2. ECI amends Election Symbols Order extending performance review from 5 to 10 years",
          "3. Aam Aadmi Party (AAP) officially recognized as a National Party",
          "4. Introduction of NOTA (None of the Above) option on ballot papers following SC direction"],
         ["1. தேசிய மக்கள் கட்சி (NPP) தேசியக் கட்சியாக அங்கீகரிக்கப்பட்டது",
          "2. சின்னங்கள் ஆணையைத் திருத்தி செயல்திறன் மறுஆய்வு காலத்தை 5-லிருந்து 10 ஆண்டுகளாக ECI மாற்றியது",
          "3. ஆம் ஆத்மி கட்சி அதிகாரப்பூர்வமாக தேசியக் கட்சியாக அங்கீகரிக்கப்பட்டது",
          "4. உச்சநீதிமன்ற உத்தரவின்படி வாக்குச்சீட்டில் 'நோட்டா' (NOTA) விருப்பத்தேர்வு அறிமுகம்"],
         ["4 - 2 - 1 - 3", "2 - 4 - 1 - 3", "4 - 1 - 2 - 3", "1 - 4 - 2 - 3"], "A",
         "The correct chronological order with 4-digit years is:\n- 4. Introduction of NOTA (2013)\n- 2. ECI 10-year review amendment (2016)\n- 1. NPP recognition (2019)\n- 3. AAP recognition (2023)\nChronological sequence: 4 (2013) → 2 (2016) → 1 (2019) → 3 (2023).",
         "சரியான காலவரிசை:\n- 4. நோட்டா அறிமுகம் (2013)\n- 2. தேர்தல் ஆணையத்தின் 10 ஆண்டு திருத்தம் (2016)\n- 1. NPP அங்கீகாரம் (2019)\n- 3. ஆம் ஆத்மி அங்கீகாரம் (2023)\nவரிசை: 4 (2013) → 2 (2016) → 1 (2019) → 3 (2023)."),

        # C_022: Coalition Governments and National Alliances
        ("022", "Coalition Alliances Era",
         ["1. Formation of United Progressive Alliance (UPA) coalition",
          "2. Formation of National Democratic Alliance (NDA) under Atal Bihari Vajpayee",
          "3. United Front government formed with H.D. Deve Gowda as Prime Minister",
          "4. National Front government formed with V.P. Singh as Prime Minister"],
         ["1. ஐக்கிய முற்போக்குக் கூட்டணி (UPA) அமைக்கப்பட்டது",
          "2. வாஜ்பாய் தலைமையில் தேசிய ஜனநாயகக் கூட்டணி (NDA) அமைக்கப்பட்டது",
          "3. தேவ கவுடா பிரதமராக ஐக்கிய முன்னணி அரசு அமைக்கப்பட்டது",
          "4. வி.பி. சிங் பிரதமராக தேசிய முன்னணி அரசு அமைக்கப்பட்டது"],
         ["4 - 3 - 2 - 1", "3 - 4 - 2 - 1", "4 - 2 - 3 - 1", "2 - 4 - 3 - 1"], "A",
         "The correct chronological order with 4-digit years is:\n- 4. National Front Government (1989)\n- 3. United Front Government (1996)\n- 2. National Democratic Alliance (1998)\n- 1. United Progressive Alliance (2004)\nChronological sequence: 4 (1989) → 3 (1996) → 2 (1998) → 1 (2004).",
         "சரியான காலவரிசை:\n- 4. தேசிய முன்னணி (1989)\n- 3. ஐக்கிய முன்னணி (1996)\n- 2. தேசிய ஜனநாயகக் கூட்டணி (1998)\n- 1. ஐக்கிய முற்போக்குக் கூட்டணி (2004)\nவரிசை: 4 (1989) → 3 (1996) → 2 (1998) → 1 (2004)."),

        # C_023: Tribal & Regional Autonomy Accords
        ("023", "Regional Autonomy Accords",
         ["1. Signing of the historic Mizo Peace Accord ending MNF insurgency",
          "2. Creation of Bodoland Territorial Council under 6th Schedule",
          "3. Creation of Nagaland as a distinct State of the Indian Union",
          "4. Formation of Darjeeling Gorkha Hill Council under DGHC Accord"],
         ["1. மிசோ தேசிய முன்னணியின் கிளர்ச்சியை முடிவுக்குக் கொண்டுவந்த மிசோரம் வரலாற்று அமைதி ஒப்பந்தம்",
          "2. 6வது அட்டவணையின் கீழ் போடோலாந்து பிராந்திய கவுன்சில் உருவாக்கப்பட்டது",
          "3. இந்திய யூனியனில் நாகாலாந்து தனி மாநிலமாக உருவாக்கப்பட்டது",
          "4. DGHC ஒப்பந்தத்தின் கீழ் டார்ஜிலிங் கோர்க்கா மலை கவுன்சில் அமைக்கப்பட்டது"],
         ["3 - 1 - 4 - 2", "1 - 3 - 4 - 2", "3 - 4 - 1 - 2", "4 - 3 - 1 - 2"], "A",
         "The correct chronological order with 4-digit years is:\n- 3. Nagaland statehood (1963)\n- 1. Mizo Peace Accord (1986)\n- 4. DGHC Accord (1988)\n- 2. Bodoland Territorial Council (2003)\nChronological sequence: 3 (1963) → 1 (1986) → 4 (1988) → 2 (2003).",
         "சரியான காலவரிசை:\n- 3. நாகாலாந்து மாநிலம் (1963)\n- 1. மிசோ அமைதி ஒப்பந்தம் (1986)\n- 4. டார்ஜிலிங் கவுன்சில் (1988)\n- 2. போடோலாந்து கவுன்சில் (2003)\nவரிசை: 3 (1963) → 1 (1986) → 4 (1988) → 2 (2003)."),

        # C_024: Seminal Scholarly Monographs on Indian Parties
        ("024", "Seminal Political Science Books",
         ["1. Publication of 'In Pursuit of Lakshmi' by Lloyd and Susanne Rudolph",
          "2. Publication of 'Politics in India' by Rajni Kothari",
          "3. Publication of 'The Politics of India Since Independence' by Paul Brass",
          "4. Publication of 'The Politics of Scarcity' by Myron Weiner"],
         ["1. லாயிட் மற்றும் சுசேன் ருடால்ஃபின் 'இன் பர்சூட் ஆஃப் லட்சுமி' நூல் வெளியீடு",
          "2. ரஜினி கோத்தாரியின் 'பாலிடிக்ஸ் இன் இந்தியா' நூல் வெளியீடு",
          "3. பால் பிராசின் 'தி பாலிடிக்ஸ் ஆஃப் இந்தியா சின்ஸ் இன்டிபென்டன்ஸ்' நூல் வெளியீடு",
          "4. மைரான் வீனரின் 'தி பாலிடிக்ஸ் ஆஃப் ஸ்கேர்சிட்டி' நூல் வெளியீடு"],
         ["4 - 2 - 1 - 3", "2 - 4 - 1 - 3", "4 - 1 - 2 - 3", "1 - 4 - 2 - 3"], "A",
         "The correct chronological order with 4-digit years is:\n- 4. The Politics of Scarcity (1962)\n- 2. Politics in India (1970)\n- 1. In Pursuit of Lakshmi (1987)\n- 3. The Politics of India Since Independence (1990)\nChronological sequence: 4 (1962) → 2 (1970) → 1 (1987) → 3 (1990).",
         "சரியான காலவரிசை:\n- 4. தி பாலிடிக்ஸ் ஆஃப் ஸ்கேர்சிட்டி (1962)\n- 2. பாலிடிக்ஸ் இன் இந்தியா (1970)\n- 1. இன் பர்சூட் ஆஃப் லட்சுமி (1987)\n- 3. தி பாலிடிக்ஸ் ஆஃப் இந்தியா (1990)\nவரிசை: 4 (1962) → 2 (1970) → 1 (1987) → 3 (1990)."),

        # C_025: Voting Age and Election Technology Evolution
        ("025", "Electoral Process Milestones",
         ["1. Reduction of voting age from 21 to 18 years by 61st Constitutional Amendment Act",
          "2. Conduct of First General Elections in independent India under universal adult suffrage",
          "3. First pilot use of Voter Verifiable Paper Audit Trail (VVPAT) in Noksen constituency",
          "4. Complete nationwide deployment of Electronic Voting Machines (EVMs) in Lok Sabha elections"],
         ["1. 61வது அரசியலமைப்பு திருத்தச் சட்டம் மூலம் வாக்களிக்கும் வயது 21-லிருந்து 18 ஆகக் குறைப்பு",
          "2. சுதந்திர இந்தியாவில் வயதுவந்தோர் வாக்குரிமை அடிப்படையில் முதல் பொதுத் தேர்தல் நடத்தல்",
          "3. நோக்சென் இடைத்தேர்தலில் முதன்முதலாக VVPAT இயந்திரங்கள் முன்னோடிப் பயன்பாடு",
          "4. மக்களவைத் தேர்தலில் நாடு முழுவதும் முழுமையாக மின்னணு வாக்குப்பதிவு இயந்திரங்கள் (EVM) பயன்பாடு"],
         ["2 - 1 - 4 - 3", "1 - 2 - 4 - 3", "2 - 4 - 1 - 3", "4 - 2 - 1 - 3"], "A",
         "The correct chronological order with 4-digit years is:\n- 2. First General Elections (1951)\n- 1. 61st Amendment Act (1988)\n- 4. Complete nationwide EVM use (2004)\n- 3. VVPAT pilot in Nagaland (2013)\nChronological sequence: 2 (1951) → 1 (1988) → 4 (2004) → 3 (2013).",
         "சரியான காலவரிசை:\n- 2. முதல் பொதுத் தேர்தல் (1951)\n- 1. 61வது திருத்தச் சட்டம் (1988)\n- 4. நாடு தழுவிய EVM (2004)\n- 3. VVPAT முன்னோட்டம் (2013)\nவரிசை: 2 (1951) → 1 (1988) → 4 (2004) → 3 (2013).")
    ]

    for item in chrono_data:
        num, subtopic, ev_en, ev_ta, opts, correct_key, exp_en, exp_ta = item
        qid = f"PPPG_C_{num}"

        clean_opts = list(opts)

        # Ensure all 4 unique
        assert len(set(clean_opts)) == 4, f"Duplicate options in {qid}: {clean_opts}"

        # Ensure correct key option is NOT 1-2-3-4
        corr_idx = {"A": 0, "B": 1, "C": 2, "D": 3}[correct_key]
        assert clean_opts[corr_idx].replace(" ", "") != "1-2-3-4", f"Critical fail in {qid}: correct sequence is 1-2-3-4!"

        # Ensure 4-digit years and arrow in explanation
        assert "→" in exp_en, f"Missing arrow in {qid} exp_en"
        assert "→" in exp_ta, f"Missing arrow in {qid} exp_ta"

        # Format stem
        en_stem = "Arrange the following events in correct chronological order:\n" + "\n".join(ev_en) + "\nSelect the correct code:"
        ta_stem = "பின்வரும் நிகழ்வுகளை சரியான காலவரிசையில் வரிசைப்படுத்துக:\n" + "\n".join(ev_ta) + "\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:"

        en_a = clean_opts[0]
        ta_a = clean_opts[0]
        en_b = clean_opts[1]
        ta_b = clean_opts[1]
        en_c = clean_opts[2]
        ta_c = clean_opts[2]
        en_d = clean_opts[3]
        ta_d = clean_opts[3]

        why_a_en = f"Evaluation of Option A ({en_a}): Sequence verification."
        why_a_ta = f"ஆப்ஷன் A ({ta_a}) மதிப்பீடு: காலவரிசை சரிபார்ப்பு."
        why_b_en = f"Evaluation of Option B ({en_b}): Sequence verification."
        why_b_ta = f"ஆப்ஷன் B ({ta_b}) மதிப்பீடு: காலவரிசை சரிபார்ப்பு."
        why_c_en = f"Evaluation of Option C ({en_c}): Sequence verification."
        why_c_ta = f"ஆப்ஷன் C ({ta_c}) மதிப்பீடு: காலவரிசை சரிபார்ப்பு."
        why_d_en = f"Evaluation of Option D ({en_d}): Sequence verification."
        why_d_ta = f"ஆப்ஷன் D ({ta_d}) மதிப்பீடு: காலவரிசை சரிபார்ப்பு."
        tip_en = "Identify the milestone years of parties, movements, and laws to establish the timeline sequence."
        tip_ta = "கட்சிகள், இயக்கங்கள் மற்றும் சட்டங்களின் முக்கிய ஆண்டுகளைக் கொண்டு வரிசையை அமைக்கவும்."
        fact_en = "Representation of the People Act was enacted in 1951; Election Symbols Order was promulgated in 1968."
        fact_ta = "மக்கள் பிரதிநிதித்துவச் சட்டம் 1951-ல் இயற்றப்பட்டது; தேர்தல் சின்னங்கள் ஆணை 1968-ல் பிறப்பிக்கப்பட்டது."

        q = make_pppg_q(
            qid, "Hard", "chronology", subtopic,
            en_stem, ta_stem,
            en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d,
            correct_key,
            exp_en, exp_ta,
            why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta
        )
        questions.append(q)

    # Apply locked randomizer
    balanced_questions = randomize_and_balance_dataset(questions, seed=209)

    keys = [q["correct_answer"] for q in balanced_questions]
    counts = Counter(keys)
    print("Part 2B PPPG Chronology Key counts:", counts)
    assert len(balanced_questions) == 25
    for opt in ["A", "B", "C", "D"]:
        assert 6 <= counts[opt] <= 7

    out_path = "data/questions/polity/political_parties_pressure_groups_chronology.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_questions, f, indent=2, ensure_ascii=False)
    print(f"Successfully wrote 25 chronology MCQs to {out_path}")

    # Immediately run dedicated ChronologyValidator
    c_rep = ChronologyValidator.validate_file(out_path)
    print("Dedicated Chronology Validator Result:")
    print(c_rep.format_final_report())
    assert c_rep.is_valid, f"ChronologyValidator failed: {c_rep.issues}"

if __name__ == "__main__":
    get_chronology_questions()
