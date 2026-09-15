# -*- coding: utf-8 -*-
"""
Build 25 Match the Following MCQs for Political Parties & Pressure Groups (PPPG_MF_001 to PPPG_MF_025)
TNPSC Nova AI Content Engine
"""
import json
import os
import shutil
from collections import Counter
from political_parties_pressure_groups_mcq_helper import make_pppg_q
from tools.nova_content_engine.answer_randomizer import randomize_and_balance_dataset

def get_match_questions():
    questions = []

    match_specs = [
        # MF_001: Party Symbols & Parties
        ("001", "Party Symbols", "Medium",
         "Match List-I (National / State Political Party) with List-II (Reserved Election Symbol):\nList-I:\na) Bharatiya Janata Party (BJP)\nb) Indian National Congress (INC)\nc) Bahujan Samaj Party (BSP)\nd) All India Anna Dravida Munnetra Kazhagam (AIADMK)\nList-II:\n1. Hand\n2. Lotus\n3. Two Leaves\n4. Elephant (except in Assam)\nSelect the correct code:",
         "பட்டியல்-I (தேசிய / மாநில அரசியல் கட்சி) உடன் பட்டியல்-II (ஒதுக்கப்பட்ட தேர்தல் சின்னம்) பொருத்துக:\nபட்டியல்-I:\na) பாரதிய ஜனதா கட்சி (BJP)\nb) இந்திய தேசிய காங்கிரஸ் (INC)\nc) பகுஜன் சமாஜ் கட்சி (BSP)\nd) அனைத்திந்திய அண்ணா திராவிட முன்னேற்றக் கழகம் (AIADMK)\nபட்டியல்-II:\n1. கை\n2. தாமரை\n3. இரட்டை இலை\n4. யானை (அசாம் நீங்கலாக)\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "A",
         "BJP -> Lotus (2); INC -> Hand (1); BSP -> Elephant (4); AIADMK -> Two Leaves (3). Code: 2-1-4-3.",
         "பாஜக -> தாமரை (2); காங்கிரஸ் -> கை (1); பகுஜன் சமாஜ் -> யானை (4); அதிமுக -> இரட்டை இலை (3). குறியீடு: 2-1-4-3."),

        # MF_002: Founding Years of Major Parties
        ("002", "Founding Years of Parties", "Medium",
         "Match List-I (Political Party) with List-II (Year of Foundation):\nList-I:\na) Indian National Congress (INC)\nb) Communist Party of India (CPI)\nc) Bharatiya Janata Party (BJP)\nd) Aam Aadmi Party (AAP)\nList-II:\n1. 1925\n2. 1885\n3. 2012\n4. 1980\nSelect the correct code:",
         "பட்டியல்-I (அரசியல் கட்சி) உடன் பட்டியல்-II (தொடங்கப்பட்ட ஆண்டு) பொருத்துக:\nபட்டியல்-I:\na) இந்திய தேசிய காங்கிரஸ் (INC)\nb) இந்திய கம்யூனிஸ்ட் கட்சி (CPI)\nc) பாரதிய ஜனதா கட்சி (BJP)\nd) ஆம் ஆத்மி கட்சி (AAP)\nபட்டியல்-II:\n1. 1925\n2. 1885\n3. 2012\n4. 1980\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "INC -> 1885 (2); CPI -> 1925 (1); BJP -> 1980 (4); AAP -> 2012 (3). Code: 2-1-4-3.",
         "காங்கிரஸ் -> 1885 (2); சிபிஐ -> 1925 (1); பாஜக -> 1980 (4); ஆம் ஆத்மி -> 2012 (3). குறியீடு: 2-1-4-3."),

        # MF_003: Regional Parties and Founders
        ("003", "Regional Parties and Founders", "Medium",
         "Match List-I (Regional Political Party) with List-II (Key Founder / Pioneer):\nList-I:\na) Dravida Munnetra Kazhagam (DMK)\nb) Telugu Desam Party (TDP)\nc) All India Trinamool Congress (AITC)\nd) All India Anna Dravida Munnetra Kazhagam (AIADMK)\nList-II:\n1. N.T. Rama Rao\n2. C.N. Annadurai\n3. M.G. Ramachandran\n4. Mamata Banerjee\nSelect the correct code:",
         "பட்டியல்-I (மாநில அரசியல் கட்சி) உடன் பட்டியல்-II (முக்கிய நிறுவனர்) பொருத்துக:\nபட்டியல்-I:\na) திராவிட முன்னேற்றக் கழகம் (DMK)\nb) தெலுங்கு தேசம் கட்சி (TDP)\nc) அகில இந்திய திரிணாமுல் காங்கிரஸ் (AITC)\nd) அனைத்திந்திய அண்ணா திராவிட முன்னேற்றக் கழகம் (AIADMK)\nபட்டியல்-II:\n1. என்.டி. ராமராவ்\n2. சி.என். அண்ணாதுரை\n3. எம்.ஜி. ராமச்சந்திரன்\n4. மம்தா பானர்ஜி\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "DMK -> C.N. Annadurai (2); TDP -> N.T. Rama Rao (1); AITC -> Mamata Banerjee (4); AIADMK -> M.G. Ramachandran (3). Code: 2-1-4-3.",
         "திமுக -> சி.என். அண்ணாதுரை (2); தெலுங்கு தேசம் -> என்.டி.ஆர் (1); திரிணாமுல் -> மம்தா பானர்ஜி (4); அதிமுக -> எம்.ஜி.ஆர் (3). குறியீடு: 2-1-4-3."),

        # MF_004: Central Trade Unions and Political Linkages
        ("004", "Trade Union Affiliations", "Medium",
         "Match List-I (Central Trade Union Federation) with List-II (Allied Political Party / Ideology):\nList-I:\na) Indian National Trade Union Congress (INTUC)\nb) All India Trade Union Congress (AITUC)\nc) Centre of Indian Trade Unions (CITU)\nd) Bharatiya Mazdoor Sangh (BMS)\nList-II:\n1. Communist Party of India (CPI)\n2. Indian National Congress (INC)\n3. Rashtriya Swayamsevak Sangh / Nationalist Ideology\n4. Communist Party of India (Marxist) [CPI(M)]\nSelect the correct code:",
         "பட்டியல்-I (மத்திய தொழிற்சங்க கூட்டமைப்பு) உடன் பட்டியல்-II (தொடர்புடைய அரசியல் கட்சி / சித்தாந்தம்) பொருத்துக:\nபட்டியல்-I:\na) இந்திய தேசிய தொழிற்சங்க காங்கிரஸ் (INTUC)\nb) அகில இந்திய தொழிற்சங்க காங்கிரஸ் (AITUC)\nc) இந்திய தொழிற்சங்க மையம் (CITU)\nd) பாரதிய மஸ்தூர் சங்கம் (BMS)\nபட்டியல்-II:\n1. இந்திய கம்யூனிஸ்ட் கட்சி (CPI)\n2. இந்திய தேசிய காங்கிரஸ் (INC)\n3. ராஷ்ட்ரிய சுயம்சேவக் சங்கம் / தேசியவாத சித்தாந்தம்\n4. மார்க்சிஸ்ட் கம்யூனிஸ்ட் கட்சி [CPI(M)]\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "A",
         "INTUC -> INC (2); AITUC -> CPI (1); CITU -> CPI(M) (4); BMS -> RSS ideology (3). Code: 2-1-4-3.",
         "INTUC -> காங்கிரஸ் (2); AITUC -> சிபிஐ (1); CITU -> சிபிஎம் (4); BMS -> ஆர்எஸ்எஸ்/பாஜக தொடர்பு (3). குறியீடு: 2-1-4-3."),

        # MF_005: Business Chambers and Founding Years
        ("005", "Business Associations", "Hard",
         "Match List-I (Apex Business Organization) with List-II (Year of Establishment):\nList-I:\na) Federation of Indian Chambers of Commerce and Industry (FICCI)\nb) Associated Chambers of Commerce and Industry of India (ASSOCHAM)\nc) Confederation of Indian Industry (CII - origin as Engineering and Iron Trades Association)\nd) All India Manufacturers' Organisation (AIMO)\nList-II:\n1. 1920\n2. 1927\n3. 1941\n4. 1895\nSelect the correct code:",
         "பட்டியல்-I (முக்கிய வணிக கூட்டமைப்பு) உடன் பட்டியல்-II (நிறுவப்பட்ட ஆண்டு) பொருத்துக:\nபட்டியல்-I:\na) இந்திய வர்த்தக மற்றும் தொழிற்துறை கூட்டமைப்பு (FICCI)\nb) இந்திய இணைந்த வர்த்தக மற்றும் தொழிற்துறை கூட்டமைப்பு (ASSOCHAM)\nc) இந்திய தொழில் கூட்டமைப்பு (CII - தோற்றம்)\nd) அகில இந்திய உற்பத்தியாளர்கள் சங்கம் (AIMO)\nபட்டியல்-II:\n1. 1920\n2. 1927\n3. 1941\n4. 1895\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-1, d-2", "a-4, b-3, c-1, d-2",
         "a-3, b-4, c-2, d-1", "a-3, b-4, c-2, d-1", "A",
         "FICCI -> 1927 (2); ASSOCHAM -> 1920 (1); CII (origin) -> 1895 (4); AIMO -> 1941 (3). Code: 2-1-4-3.",
         "FICCI -> 1927 (2); ASSOCHAM -> 1920 (1); CII தோற்றம் -> 1895 (4); AIMO -> 1941 (3). குறியீடு: 2-1-4-3."),

        # MF_006: Farmers' Organizations & Leaders
        ("006", "Farmers' Organizations and Leaders", "Medium",
         "Match List-I (Agrarian Pressure Group) with List-II (Associated Leader / Region):\nList-I:\na) Bharatiya Kisan Union (BKU)\nb) Shetkari Sanghatana\nc) Karnataka Rajya Raitha Sangha (KRRS)\nd) All India Kisan Sabha (AIKS, 1936)\nList-II:\n1. Sharad Joshi (Maharashtra)\n2. Mahendra Singh Tikait (Uttar Pradesh / North India)\n3. Swami Sahajanand Saraswati\n4. Prof. M.D. Nanjundaswamy (Karnataka)\nSelect the correct code:",
         "பட்டியல்-I (விவசாயிகள் அழுத்தக் குழு) உடன் பட்டியல்-II (தொடர்புடைய தலைவர் / பகுதி) பொருத்துக:\nபட்டியல்-I:\na) பாரதிய கிசான் யூனியன் (BKU)\nb) ஷேத்காரி சங்கடனா\nc) கர்நாடக மாநில ரைத சங்க (KRRS)\nd) அகில இந்திய கிசான் சபா (AIKS, 1936)\nபட்டியல்-II:\n1. சரத் ஜோஷி (மகாராஷ்டிரா)\n2. மகேந்திர சிங் திகாயத் (உத்தரப் பிரதேசம் / வட இந்தியா)\n3. சுவாமி சகஜானந்த சரஸ்வதி\n4. பேராசிரியர் எம்.டி. நஞ்சுண்டசுவாமி (கர்நாடகா)\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "BKU -> Tikait (2); Shetkari Sanghatana -> Sharad Joshi (1); KRRS -> Nanjundaswamy (4); AIKS -> Sahajanand Saraswati (3). Code: 2-1-4-3.",
         "BKU -> திகாயத் (2); ஷேத்காரி -> சரத் ஜோஷி (1); KRRS -> நஞ்சுண்டசுவாமி (4); AIKS -> சகஜானந்த சரஸ்வதி (3). குறியீடு: 2-1-4-3."),

        # MF_007: Student Organizations and Parent Groups
        ("007", "Student Organizations", "Medium",
         "Match List-I (Student Pressure Group) with List-II (Parent Organization / Ideological Alignment):\nList-I:\na) Akhil Bharatiya Vidyarthi Parishad (ABVP)\nb) National Students' Union of India (NSUI)\nc) Students' Federation of India (SFI)\nd) All India Students' Federation (AISF)\nList-II:\n1. Indian National Congress (INC)\n2. Rashtriya Swayamsevak Sangh (RSS)\n3. Communist Party of India (CPI)\n4. Communist Party of India (Marxist) [CPI(M)]\nSelect the correct code:",
         "பட்டியல்-I (மாணவர் அழுத்தக் குழு) உடன் பட்டியல்-II (தாய் அமைப்பு / அரசியல் தொடர்பு) பொருத்துக:\nபட்டியல்-I:\na) அகில பாரதிய வித்யார்த்தி பரிஷத் (ABVP)\nb) இந்திய தேசிய மாணவர் ஒன்றியம் (NSUI)\nc) இந்திய மாணவர் கூட்டமைப்பு (SFI)\nd) அகில இந்திய மாணவர் பெருமன்றம் (AISF)\nபட்டியல்-II:\n1. இந்திய தேசிய காங்கிரஸ் (INC)\n2. ராஷ்ட்ரிய சுயம்சேவக் சங்கம் (RSS)\n3. இந்திய கம்யூனிஸ்ட் கட்சி (CPI)\n4. மார்க்சிஸ்ட் கம்யூனிஸ்ட் கட்சி [CPI(M)]\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "A",
         "ABVP -> RSS (2); NSUI -> INC (1); SFI -> CPI(M) (4); AISF -> CPI (3). Code: 2-1-4-3.",
         "ABVP -> ஆர்எஸ்எஸ் (2); NSUI -> காங்கிரஸ் (1); SFI -> சிபிஎம் (4); AISF -> சிபிஐ (3). குறியீடு: 2-1-4-3."),

        # MF_008: Political Scientists & Concepts
        ("008", "Political Thinkers and Party Systems", "Hard",
         "Match List-I (Political Theorist / Scholar) with List-II (Core Conceptual Contribution on Parties):\nList-I:\na) Maurice Duverger\nb) Rajni Kothari\nc) Giovanni Sartori\nd) W.H. Morris-Jones\nList-II:\n1. The Congress System (One-Party Dominance with internal consensus)\n2. Plurality/First-Past-the-Post electoral systems favor a two-party system\n3. One-Party Dominance with open competition and bargaining\n4. Typology of Party Systems based on ideological distance and polarization\nSelect the correct code:",
         "பட்டியல்-I (அரசியல் கோட்பாட்டாளர் / அறிஞர்) உடன் பட்டியல்-II (கட்சிக் கோட்பாட்டு பங்களிப்பு) பொருத்துக:\nபட்டியல்-I:\na) மாரிஸ் டுவெர்ஜர் (Maurice Duverger)\nb) ரஜினி கோத்தாரி (Rajni Kothari)\nc) ஜியோவானி சார்டோரி (Giovanni Sartori)\nd) டபிள்யூ.ஹெச். மோரிஸ்-ஜோன்ஸ் (W.H. Morris-Jones)\nபட்டியல்-II:\n1. காங்கிரஸ் அமைப்பு (உள் ஒருமித்த கருத்துடன் கூடிய ஒரு கட்சி ஆதிக்கம்)\n2. முதல் நிலைப் பெரும்பான்மை முறை இரு-கட்சி முறைக்கு வழிவகுக்கும்\n3. திறந்த போட்டி மற்றும் பேரம் பேசுதலுடன் கூடிய ஒரு கட்சி ஆதிக்கம்\n4. சித்தாந்த இடைவெளி மற்றும் துருவமுனைப்பு அடிப்படையிலான கட்சி அமைப்பு வகைப்பாடு\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-1, d-2", "a-4, b-3, c-1, d-2",
         "a-3, b-4, c-2, d-1", "a-3, b-4, c-2, d-1", "A",
         "Duverger -> Law on plurality systems (2); Kothari -> Congress System (1); Sartori -> Polarized pluralism typology (4); Morris-Jones -> One-party dominance with bargaining (3). Code: 2-1-4-3.",
         "டுவெர்ஜர் -> பெரும்பான்மை விதி (2); கோத்தாரி -> காங்கிரஸ் அமைப்பு (1); சார்டோரி -> வகைப்பாடு (4); மோரிஸ்-ஜோன்ஸ் -> பேரம் பேசும் ஒரு கட்சி ஆதிக்கம் (3). குறியீடு: 2-1-4-3."),

        # MF_009: Classification of Pressure Groups (Gabriel Almond)
        ("009", "Gabriel Almond Pressure Group Typology", "Hard",
         "Match List-I (Pressure Group Category according to Gabriel Almond) with List-II (Empirical Example):\nList-I:\na) Institutional Interest Groups\nb) Associational Interest Groups\nc) Non-Associational Interest Groups\nd) Anomic Interest Groups\nList-II:\n1. Trade Unions (AITUC, BMS) and Business Chambers (FICCI)\n2. Civil Services Association, Indian Military Officer Corps\n3. Spontaneous riots, flash street mobs, and student stone-pelting crowds\n4. Caste Panchayats, linguistic kinship groups, and tribal ethnic councils\nSelect the correct code:",
         "பட்டியல்-I (கேப்ரியல் ஆல்மண்டின் அழுத்தக் குழு வகைப்பாடு) உடன் பட்டியல்-II (நடைமுறை உதாரணம்) பொருத்துக:\nபட்டியல்-I:\na) நிறுவன அழுத்தக் குழுக்கள் (Institutional)\nb) சங்க அழுத்தக் குழுக்கள் (Associational)\nc) சங்கம் சாரா அழுத்தக் குழுக்கள் (Non-Associational)\nd) ஒழுங்கற்ற அழுத்தக் குழுக்கள் (Anomic)\nபட்டியல்-II:\n1. தொழிற்சங்கங்கள் (AITUC) மற்றும் வணிக சபைகள் (FICCI)\n2. குடிமைப்பணி அதிகாரிகளின் சங்கம், ராணுவ அதிகாரிகள் அமைப்பு\n3. திடீர் கலவரங்கள், உடனடி வன்முறை ஆர்ப்பாட்டங்கள்\n4. சாதிப் பஞ்சாயத்துகள், மொழி மற்றும் பழங்குடி இனக் குழுக்கள்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-2, d-1", "a-3, b-4, c-2, d-1",
         "a-4, b-3, c-1, d-2", "a-4, b-3, c-1, d-2", "A",
         "Institutional -> Bureaucracy/Military (2); Associational -> Trade Unions/FICCI (1); Non-Associational -> Caste/Tribal groups (4); Anomic -> Flash riots/mobs (3). Code: 2-1-4-3.",
         "நிறுவனக் குழு -> குடிமைப்பணி/ராணுவம் (2); சங்கக் குழு -> FICCI/தொழிற்சங்கங்கள் (1); சங்கம் சாரா -> சாதி/இனக் குழு (4); ஒழுங்கற்ற -> திடீர் வன்முறைக் கூட்டம் (3). குறியீடு: 2-1-4-3."),

        # MF_010: Legal Provisions and Election Rules
        ("010", "Legal Framework for Parties", "Medium",
         "Match List-I (Statutory Provision / Order) with List-II (Subject / Purpose):\nList-I:\na) Section 29A of RPA 1951\nb) Paragraph 6A of Election Symbols Order 1968\nc) Paragraph 6B of Election Symbols Order 1968\nd) Paragraph 15 of Election Symbols Order 1968\nList-II:\n1. Conditions for recognition as a State Party\n2. Registration of political associations as political parties with the Election Commission\n3. Power of Commission in relation to splinter groups or rival factions of a recognized party\n4. Conditions for recognition as a National Party\nSelect the correct code:",
         "பட்டியல்-I (சட்டப்பிரிவு / தேர்தல் ஆணை) உடன் பட்டியல்-II (பொருள் / நோக்கம்) பொருத்துக:\nபட்டியல்-I:\na) மக்கள் பிரதிநிதித்துவச் சட்டம் 1951, பிரிவு 29A\nb) தேர்தல் சின்னங்கள் ஆணை 1968, பத்தி 6A\nc) தேர்தல் சின்னங்கள் ஆணை 1968, பத்தி 6B\nd) தேர்தல் சின்னங்கள் ஆணை 1968, பத்தி 15\nபட்டியல்-II:\n1. மாநிலக் கட்சியாக அங்கீகரிப்பதற்கான நிபந்தனைகள்\n2. தேர்தல் ஆணையத்திடம் அரசியல் கட்சிகளாகப் பதிவு செய்தல்\n3. கட்சியில் பிளவு அல்லது போட்டி பிரிவுகள் எழும்போது ஆணையத்தின் தீர்ப்பு அதிகாரம்\n4. தேசியக் கட்சியாக அங்கீகரிப்பதற்கான நிபந்தனைகள்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "A",
         "Sec 29A -> Registration (2); Para 6A -> State Party conditions (1); Para 6B -> National Party conditions (4); Para 15 -> Faction dispute decision (3). Code: 2-1-4-3.",
         "பிரிவு 29A -> கட்சிகள் பதிவு (2); பத்தி 6A -> மாநிலக் கட்சி நிபந்தனை (1); பத்தி 6B -> தேசியக் கட்சி நிபந்தனை (4); பத்தி 15 -> பிளவு/சின்னத் தகராறு (3). குறியீடு: 2-1-4-3."),

        # MF_011: Environmental Movements and Leaders
        ("011", "Environmental Pressure Groups and Leaders", "Medium",
         "Match List-I (Environmental Movement / Pressure Group) with List-II (Leading Figure / State):\nList-I:\na) Chipko Movement (1973)\nb) Narmada Bachao Andolan (1985)\nc) Appiko Movement (1983)\nd) Silent Valley Movement (1978)\nList-II:\n1. Medha Patkar\n2. Sunderlal Bahuguna and Gaura Devi (Uttarakhand)\n3. Kerala Sastra Sahitya Parishad (KSSP)\n4. Pandurang Hegde (Karnataka)\nSelect the correct code:",
         "பட்டியல்-I (சுற்றுச்சூழல் இயக்கம் / அழுத்தக் குழு) உடன் பட்டியல்-II (முன்னணித் தலைவர் / மாநிலம்) பொருத்துக:\nபட்டியல்-I:\na) சிப்கோ இயக்கம் (1973)\nb) நர்மதா பச்சாவோ அந்தோலன் (1985)\nc) அப்பிகோ இயக்கம் (1983)\nd) அமைதிப் பள்ளத்தாக்கு இயக்கம் (1978)\nபட்டியல்-II:\n1. மேதா பட்கர்\n2. சுந்தர்லால் பகுகுணா மற்றும் கௌரா தேவி (உத்தராகண்ட்)\n3. கேரளா சாஸ்திர சாகித்ய பரிஷத் (கேரளா)\n4. பாண்டுரங் ஹெக்டே (கர்நாடகா)\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "Chipko -> Sunderlal Bahuguna (2); NBA -> Medha Patkar (1); Appiko -> Pandurang Hegde (4); Silent Valley -> KSSP (3). Code: 2-1-4-3.",
         "சிப்கோ -> பகுகுணா (2); நர்மதா -> மேதா பட்கர் (1); அப்பிகோ -> பாண்டுரங் ஹெக்டே (4); அமைதிப் பள்ளத்தாக்கு -> KSSP (3). குறியீடு: 2-1-4-3."),

        # MF_012: Pre-Independence Associations and Founders
        ("012", "Pre-Independence Political Associations", "Medium",
         "Match List-I (Pre-Independence Association) with List-II (Founder / Key Organizer):\nList-I:\na) Landholders' Society (1838)\nb) East India Association (1866)\nc) Indian Association (1876)\nd) Madras Mahajana Sabha (1884)\nList-II:\n1. Dadabhai Naoroji (London)\n2. Dwarkanath Tagore and Radhakanta Deb (Calcutta)\n3. M. Veeraraghavachariar, G. Subramania Iyer, and P. Anandacharlu\n4. Surendranath Banerjee and Ananda Mohan Bose\nSelect the correct code:",
         "பட்டியல்-I (சுதந்திரத்திற்கு முந்தைய சங்கம்) உடன் பட்டியல்-II (நிறுவனர் / அமைப்பாளர்) பொருத்துக:\nபட்டியல்-I:\na) நிலப்பிரபுக்கள் சங்கம் (1838)\nb) கிழக்கு இந்திய சங்கம் (1866)\nc) இந்திய சங்கம் (1876)\nd) சென்னை மகாஜன சபை (1884)\nபட்டியல்-II:\n1. தாதாபாய் நௌரோஜி (லண்டன்)\n2. துவாரகநாத் தாகூர் மற்றும் ராதாகாந்த தேவ் (கொல்கத்தா)\n3. எம். வீரராகவாச்சாரியார், ஜி. சுப்பிரமணிய ஐயர், பி. அனந்தாச்சார்லு\n4. சுரேந்திரநாத் பானர்ஜி மற்றும் ஆனந்த மோகன் போஸ்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "A",
         "Landholders' Society -> Dwarkanath Tagore (2); East India Association -> Dadabhai Naoroji (1); Indian Association -> Surendranath Banerjee (4); Madras Mahajana Sabha -> Veeraraghavachariar/Anandacharlu (3). Code: 2-1-4-3.",
         "நிலப்பிரபுக்கள் சங்கம் -> தாகூர் (2); கிழக்கு இந்திய சங்கம் -> நௌரோஜி (1); இந்திய சங்கம் -> பானர்ஜி (4); சென்னை மகாஜன சபை -> வீரராகவாச்சாரியார் (3). குறியீடு: 2-1-4-3."),

        # MF_013: Caste & Backward Classes Associations
        ("013", "Caste and Social Movement Pressure Groups", "Hard",
         "Match List-I (Social Movement / Caste Pressure Group) with List-II (Founder / Pioneer):\nList-I:\na) SNDP Yogam (1903)\nb) South Indian Liberal Federation (Justice Party, 1916)\nc) Bahujan Samaj Party (BSP, 1984)\nd) Dalit Panthers (1972)\nList-II:\n1. Dr. T.M. Nair and P. Theagaraya Chetty\n2. Sri Narayana Guru and Dr. Palpu\n3. Namdeo Dhasal and Arjun Dangle\n4. Manyawar Kanshi Ram\nSelect the correct code:",
         "பட்டியல்-I (சமூக இயக்கம் / சாதி அழுத்தக் குழு) உடன் பட்டியல்-II (நிறுவனர் / முன்னோடி) பொருத்துக:\nபட்டியல்-I:\na) ஸ்ரீ நாராயண தர்ம பரிபாலன யோகம் (SNDP, 1903)\nb) தென்னிந்திய நல உரிமைச் சங்கம் (நீதிக் கட்சி, 1916)\nc) பகுஜன் சமாஜ் கட்சி (1984)\nd) தலித் பாந்தர்ஸ் (1972)\nபட்டியல்-II:\n1. டாக்டர் டி.எம். நாயர் மற்றும் பி. தியாகராய செட்டி\n2. ஸ்ரீ நாராயண குரு மற்றும் டாக்டர் பல்பு\n3. நாம்தேவ் தாசல் மற்றும் அர்ஜுன் டாங்லே\n4. மான்யவர் கன்ஷிராம்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "SNDP Yogam -> Sri Narayana Guru (2); Justice Party -> T.M. Nair / Theagaraya Chetty (1); BSP -> Kanshi Ram (4); Dalit Panthers -> Namdeo Dhasal (3). Code: 2-1-4-3.",
         "SNDP யோகம் -> நாராயண குரு (2); நீதிக் கட்சி -> டி.எம். நாயர்/தியாகராய செட்டி (1); பகுஜன் சமாஜ் -> கன்ஷிராம் (4); தலித் பாந்தர்ஸ் -> நாம்தேவ் தாசல் (3). குறியீடு: 2-1-4-3."),

        # MF_014: Women's & Civil Society Pressure Groups
        ("014", "Women and Civil Liberties Groups", "Medium",
         "Match List-I (Civil Society / Women's Pressure Group) with List-II (Founder / Key Association):\nList-I:\na) All India Women's Conference (AIWC, 1927)\nb) Self-Employed Women's Association (SEWA, 1972)\nc) People's Union for Civil Liberties (PUCL, 1976)\nd) Mazdoor Kisan Shakti Sangathan (MKSS, 1990)\nList-II:\n1. Ela Bhatt\n2. Margaret Cousins and Maharani Chimnabai Gaekwad\n3. Aruna Roy and Nikhil Dey\n4. Jayaprakash Narayan\nSelect the correct code:",
         "பட்டியல்-I (குடிமைச் சமூகம் / மகளிர் அழுத்தக் குழு) உடன் பட்டியல்-II (நிறுவனர் / முன்னோடி) பொருத்துக:\nபட்டியல்-I:\na) அகில இந்திய பெண்கள் மாநாடு (AIWC, 1927)\nb) சுயதொழில் மகளிர் சங்கம் (SEWA, 1972)\nc) மக்கள் சிவில் உரிமைக் கூட்டமைப்பு (PUCL, 1976)\nd) மஸ்தூர் கிசான் சக்தி சங்கத்தன் (MKSS, 1990)\nபட்டியல்-II:\n1. இலா பட்\n2. மார்கரெட் கசின்ஸ் மற்றும் மகாராணி சிம்னாபாய் கெய்க்வாட்\n3. அருணா ராய் மற்றும் நிகில் டே\n4. ஜெயபிரகாஷ் நாராயண்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "AIWC -> Margaret Cousins (2); SEWA -> Ela Bhatt (1); PUCL -> JP Narayan (4); MKSS -> Aruna Roy (3). Code: 2-1-4-3.",
         "AIWC -> மார்கரெட் கசின்ஸ் (2); SEWA -> இலா பட் (1); PUCL -> ஜெயபிரகாஷ் நாராயண் (4); MKSS -> அருணா ராய் (3). குறியீடு: 2-1-4-3."),

        # MF_015: Committees on Electoral Reforms & Parties
        ("015", "Electoral Reform Committees", "Hard",
         "Match List-I (Committee / Commission) with List-II (Key Recommendation on Parties):\nList-I:\na) Tarkunde Committee (1974-75)\nb) Dinesh Goswami Committee (1990)\nc) Indrajit Gupta Committee (1998)\nd) Law Commission 255th Report (2015)\nList-II:\n1. State funding of elections exclusively in kind (facilities, not cash)\n2. Appointment of Election Commissioners through a collegium and lowering voting age to 18\n3. Comprehensive regulation of internal party democracy and strict disclosure of election donations\n4. State assistance in kind to recognized political parties and stringent anti-defection amendments\nSelect the correct code:",
         "பட்டியல்-I (தேர்தல் சீர்திருத்தக் குழு) உடன் பட்டியல்-II (முக்கிய பரிந்துரை) பொருத்துக:\nபட்டியல்-I:\na) தர்குண்டே குழு (1974-75)\nb) தினேஷ் கோஸ்வாமி குழு (1990)\nc) இந்திரஜித் குப்தா குழு (1998)\nd) சட்ட ஆணையத்தின் 255வது அறிக்கை (2015)\nபட்டியல்-II:\n1. பணமாக அன்றி பொருட்களாக மட்டுமே அரசு தேர்தல் நிதி அளித்தல்\n2. கொலீஜியம் மூலம் தேர்தல் ஆணையர்கள் நியமனம் & வாக்களிக்கும் வயது 18 ஆகக் குறைப்பு\n3. உள்கட்சி ஜனநாயகத்தை சட்டப்பூர்வமாக ஒழுங்குபடுத்துதல் மற்றும் நன்கொடை வெளிப்படைத்தன்மை\n4. அங்கீகரிக்கப்பட்ட கட்சிகளுக்கு அரசு ஆதரவு மற்றும் கட்சித் தாவல் தடைச் சட்ட வலுப்படுத்தல்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-4, c-1, d-3", "a-2, b-4, c-1, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-1, c-4, d-2", "a-3, b-1, c-4, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "Tarkunde -> Collegium / voting age 18 (2); Goswami -> Anti-defection / state help (4); Indrajit Gupta -> State funding in kind (1); Law Commission 255th -> Internal democracy / donation disclosure (3). Code: 2-4-1-3.",
         "தர்குண்டே -> கொலீஜியம்/வயது 18 (2); கோஸ்வாமி -> கட்சித் தாவல்/அரசு ஆதரவு (4); இந்திரஜித் குப்தா -> பொருட்களாக தேர்தல் நிதி (1); சட்ட ஆணையம் 255வது -> உள்கட்சி ஜனநாயகம் (3). குறியீடு: 2-4-1-3."),

        # MF_016: Pressure Group Operational Techniques
        ("016", "Pressure Group Techniques", "Medium",
         "Match List-I (Operational Method) with List-II (Practical Modality):\nList-I:\na) Direct Lobbying\nb) Public Interest Litigation (PIL)\nc) Mass Mobilization and Bandhs\nd) Media Campaigns and Propagandizing\nList-II:\n1. Invoking judicial review under Article 32/226 to protect public rights\n2. Interacting directly with bureaucrats and legislators to influence bills\n3. Influencing public opinion and shaping voter perception through press releases and adverts\n4. Paralyzing public transport and trade through nationwide strikes\nSelect the correct code:",
         "பட்டியல்-I (செயல்பாட்டு உத்தி) உடன் பட்டியல்-II (நடைமுறை வடிவம்) பொருத்துக:\nபட்டியல்-I:\na) நேரடி லாபி செய்தல் (Direct Lobbying)\nb) பொதுநல வழக்கு (PIL)\nc) மக்கள் திரளல் மற்றும் பந்த் (Bandh)\nd) ஊடகப் பிரச்சாரம் (Media Campaigns)\nபட்டியல்-II:\n1. பொது உரிமைகளைப் பாதுகாக்க உறுப்பு 32/226-ன் கீழ் நீதிமன்றத்தை நாடுதல்\n2. மசோதாக்களை மாற்ற அதிகாரிகள் மற்றும் சட்டமன்ற உறுப்பினர்களை நேரடியாகச் சந்தித்தல்\n3. செய்தி அறிக்கைகள் மற்றும் விளம்பரங்கள் மூலம் பொதுக் கருத்தை உருவாக்குதல்\n4. நாடு தழுவிய வேலைநிறுத்தங்கள் மூலம் பொதுப்போக்குவரத்து மற்றும் வணிகத்தை முடக்குதல்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "A",
         "Direct Lobbying -> Meeting bureaucrats (2); PIL -> Art 32/226 (1); Mass Mobilization -> Bandhs/strikes (4); Media Campaigns -> Shaping public opinion (3). Code: 2-1-4-3.",
         "லாபி செய்தல் -> அதிகாரிகள் சந்திப்பு (2); பொதுநல வழக்கு -> நீதிமன்ற ஆய்வு (1); மக்கள் திரளல் -> வேலைநிறுத்தம் (4); ஊடகப் பிரச்சாரம் -> பொதுக் கருத்து (3). குறியீடு: 2-1-4-3."),

        # MF_017: Regional Parties and Native States
        ("017", "Regional Parties and Home States", "Medium",
         "Match List-I (Regional Political Party) with List-II (Primary Base State):\nList-I:\na) Biju Janata Dal (BJD)\nb) Asom Gana Parishad (AGP)\nc) Shiromani Akali Dal (SAD)\nd) Jharkhand Mukti Morcha (JMM)\nList-II:\n1. Assam\n2. Odisha\n3. Jharkhand\n4. Punjab\nSelect the correct code:",
         "பட்டியல்-I (மாநிலக் கட்சி) உடன் பட்டியல்-II (முக்கிய சொந்த மாநிலம்) பொருத்துக:\nபட்டியல்-I:\na) பிஜு ஜனதா தளம் (BJD)\nb) அசோம் கண பரிஷத் (AGP)\nc) சிரோமணி அகாலி தளம் (SAD)\nd) ஜார்க்கண்ட் முக்தி மோர்ச்சா (JMM)\nபட்டியல்-II:\n1. அசாம்\n2. ஒடிசா\n3. ஜார்க்கண்ட்\n4. பஞ்சாப்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "BJD -> Odisha (2); AGP -> Assam (1); SAD -> Punjab (4); JMM -> Jharkhand (3). Code: 2-1-4-3.",
         "BJD -> ஒடிசா (2); AGP -> அசாம் (1); அகாலி தளம் -> பஞ்சாப் (4); JMM -> ஜார்க்கண்ட் (3). குறியீடு: 2-1-4-3."),

        # MF_018: Party Registration Criteria (ECI Forms & Timeline)
        ("018", "Party Registration Procedural Details", "Hard",
         "Match List-I (Registration Aspect under Section 29A RPA) with List-II (Statutory Mandate):\nList-I:\na) Time limit for filing application after party formation\nb) Mandatory allegiance pledge in party constitution\nc) Processing fee submitted with application\nd) Minimum number of registered voter founding members\nList-II:\n1. Allegiance to Constitution of India and principles of socialism, secularism, and democracy\n2. Within 30 days of the date of its formation\n3. 100 registered electors subscribing to the application with affidavits\n4. Non-refundable fee of Rs 10,000 (prescribed by ECI)\nSelect the correct code:",
         "பட்டியல்-I (மக்கள் பிரதிநிதித்துவச் சட்டம் பிரிவு 29A அம்சங்கள்) உடன் பட்டியல்-II (சட்டப்பூர்வ நிபந்தனை) பொருத்துக:\nபட்டியல்-I:\na) கட்சி உருவாக்கப்பட்ட பின் விண்ணப்பம் தாக்கல் செய்ய கால அவகாசம்\nb) கட்சியின் விதிகளில் இடம்பெற வேண்டிய உறுதிமொழி\nc) விண்ணப்பக் கட்டணம்\nd) ஆரம்ப உறுப்பினர்களாக கையெழுத்திட வேண்டிய குறைந்தபட்ச வாக்காளர்கள்\nபட்டியல்-II:\n1. இந்திய அரசியலமைப்பு, சோசலிசம், மதச்சார்பின்மை மற்றும் ஜனநாயகத்திற்கான பற்றுறுதி\n2. உருவாக்கப்பட்ட நாளிலிருந்து 30 நாட்களுக்குள்\n3. பிரமாணப் பத்திரங்களுடன் கையெழுத்திடும் 100 பதிவுபெற்ற வாக்காளர்கள்\n4. ரூ. 10,000 திரும்பப் பெற முடியாத கட்டணம்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "A",
         "Time limit -> 30 days (2); Allegiance -> Constitution & secularism (1); Processing fee -> Rs 10,000 (4); Minimum electors -> 100 (3). Code: 2-1-4-3.",
         "கால அவகாசம் -> 30 நாட்கள் (2); உறுதிமொழி -> அரசியலமைப்பு/மதச்சார்பின்மை (1); கட்டணம் -> ரூ. 10,000 (4); குறைந்தபட்ச வாக்காளர்கள் -> 100 (3). குறியீடு: 2-1-4-3."),

        # MF_019: Landmark Judgments on Parties & Elections
        ("019", "Judicial Precedents on Political Parties", "Hard",
         "Match List-I (Landmark Case) with List-II (Constitutional / Legal Ruling):\nList-I:\na) Association for Democratic Reforms (ADR, 2002)\nb) Lily Thomas v. Union of India (2013)\nc) Sadiq Ali v. Election Commission of India (1972)\nd) Common Cause v. Union of India (1996)\nList-II:\n1. Immediate disqualification of convicted MPs/MLAs sentenced to >= 2 years (struck down Sec 8(4))\n2. Voters have a fundamental right under Article 19(1)(a) to know candidates' criminal antecedents\n3. Political parties must maintain audited accounts and submit expenditure statements under IT Act\n4. Test of majority in legislative wing and organizational wing governs symbol allocation in party splits\nSelect the correct code:",
         "பட்டியல்-I (முக்கிய வழக்கு) உடன் பட்டியல்-II (நீதிமன்றத் தீர்ப்பு) பொருத்துக:\nபட்டியல்-I:\na) ஜனநாயக சீர்திருத்தங்களுக்கான கூட்டமைப்பு (ADR, 2002)\nb) லில்லி தாமஸ் எதிர் இந்திய யூனியன் (2013)\nc) சாதிக் அலி எதிர் இந்திய தேர்தல் ஆணையம் (1972)\nd) காமன் காஸ் எதிர் இந்திய யூனியன் (1996)\nபட்டியல்-II:\n1. 2 ஆண்டுகள் தண்டனை பெற்ற நாடாளுமன்ற/சட்டமன்ற உறுப்பினர்கள் உடனடியாக தகுதிநீக்கம்\n2. வேட்பாளர்களின் குற்றப்பின்னணியை அறிய வாக்காளர்களுக்கு உறுப்பு 19(1)(a)-ன் கீழ் உரிமை உண்டு\n3. அரசியல் கட்சிகள் தணிக்கை செய்யப்பட்ட கணக்குகளைப் பராமரித்து வருமான வரி அறிக்கையைத் தாக்கல் செய்ய வேண்டும்\n4. கட்சியில் பிளவு ஏற்படும் போது சட்டமன்ற மற்றும் அமைப்பு ரீதியான பெரும்பான்மை சோதனை\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "ADR (2002) -> Candidate background disclosure (2); Lily Thomas (2013) -> Immediate disqualification (1); Sadiq Ali (1972) -> Test of majority for symbol (4); Common Cause (1996) -> Audited accounts (3). Code: 2-1-4-3.",
         "ADR -> பின்னணி அறிவிப்பு (2); லில்லி தாமஸ் -> உடனடி தகுதிநீக்கம் (1); சாதிக் அலி -> பெரும்பான்மை சோதனை (4); காமன் காஸ் -> கணக்குத் தணிக்கை (3). குறியீடு: 2-1-4-3."),

        # MF_020: Political Parties in Tamil Nadu
        ("020", "Tamil Nadu Political Parties and Formation", "Medium",
         "Match List-I (Tamil Nadu Political Party) with List-II (Year of Foundation):\nList-I:\na) Dravida Kazhagam (DK)\nb) Dravida Munnetra Kazhagam (DMK)\nc) All India Anna Dravida Munnetra Kazhagam (AIADMK)\nd) Marumalarchi Dravida Munnetra Kazhagam (MDMK)\nList-II:\n1. 1949\n2. 1944\n3. 1994\n4. 1972\nSelect the correct code:",
         "பட்டியல்-I (தமிழ்நாடு அரசியல் கட்சி) உடன் பட்டியல்-II (தொடங்கப்பட்ட ஆண்டு) பொருத்துக:\nபட்டியல்-I:\na) திராவிடர் கழகம் (DK)\nb) திராவிட முன்னேற்றக் கழகம் (DMK)\nc) அனைத்திந்திய அண்ணா திராவிட முன்னேற்றக் கழகம் (AIADMK)\nd) மறுமலர்ச்சி திராவிட முன்னேற்றக் கழகம் (MDMK)\nபட்டியல்-II:\n1. 1949\n2. 1944\n3. 1994\n4. 1972\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "A",
         "DK -> 1944 (2); DMK -> 1949 (1); AIADMK -> 1972 (4); MDMK -> 1994 (3). Code: 2-1-4-3.",
         "திக -> 1944 (2); திமுக -> 1949 (1); அதிமுக -> 1972 (4); மதிமுக -> 1994 (3). குறியீடு: 2-1-4-3."),

        # MF_021: Types of Pressure Groups (Scholarly Classification)
        ("021", "Pressure Group Focus Areas", "Medium",
         "Match List-I (Category of Pressure Group) with List-II (Illustrative Example):\nList-I:\na) Professional Association\nb) Agrarian Organization\nc) Linguistic / Cultural Organization\nd) Ideological / Promotional Group\nList-II:\n1. Bharatiya Kisan Union (BKU)\n2. Indian Medical Association (IMA)\n3. People for the Ethical Treatment of Animals (PETA) / Amnesty\n4. Hindi Sahitya Sammelan / Tamil Sangam\nSelect the correct code:",
         "பட்டியல்-I (அழுத்தக் குழு வகை) உடன் பட்டியல்-II (விளக்க உதாரணம்) பொருத்துக:\nபட்டியல்-I:\na) தொழில்முறை சங்கம்\nb) விவசாய சங்கம்\nc) மொழி / கலாச்சார அமைப்பு\nd) சித்தாந்த / கொள்கை ஆதரவுக் குழு\nபட்டியல்-II:\n1. பாரதிய கிசான் யூனியன் (BKU)\n2. இந்திய மருத்துவ சங்கம் (IMA)\n3. விலங்கு நல அமைப்பு (PETA) / அம்னஸ்டி\n4. இந்தி சாகித்ய சம்மேளனம் / தமிழ்ச் சங்கம்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "Professional -> IMA (2); Agrarian -> BKU (1); Linguistic -> Hindi Sahitya Sammelan / Tamil Sangam (4); Promotional -> PETA/Amnesty (3). Code: 2-1-4-3.",
         "தொழில்முறை -> IMA (2); விவசாயம் -> BKU (1); மொழி -> தமிழ்ச் சங்கம் (4); கொள்கை ஆதரவு -> PETA (3). குறியீடு: 2-1-4-3."),

        # MF_022: National Parties Recognized Status (2023-2024 List)
        ("022", "National Parties and State Strongholds", "Medium",
         "Match List-I (Recognized National Party) with List-II (Key Recognition Milestone / Origin):\nList-I:\na) National People's Party (NPP)\nb) Aam Aadmi Party (AAP)\nc) Communist Party of India (Marxist) [CPI(M)]\nd) Bahujan Samaj Party (BSP)\nList-II:\n1. Recognized as National Party in 2023 after Gujarat & Goa elections\n2. First Northeast-based party to get National Party status (2019)\n3. Founded in 1984 representing Scheduled Castes, Scheduled Tribes, and OBCs\n4. Formed in 1964 following ideological split from undivided CPI\nSelect the correct code:",
         "பட்டியல்-I (அங்கீகரிக்கப்பட்ட தேசியக் கட்சி) உடன் பட்டியல்-II (அங்கீகார மைல்கல் / தோற்றம்) பொருத்துக:\nபட்டியல்-I:\na) தேசிய மக்கள் கட்சி (NPP)\nb) ஆம் ஆத்மி கட்சி (AAP)\nc) மார்க்சிஸ்ட் கம்யூனிஸ்ட் கட்சி [CPI(M)]\nd) பகுஜன் சமாஜ் கட்சி (BSP)\nபட்டியல்-II:\n1. குஜராத் & கோவா தேர்தல்களுக்குப் பின் 2023-ல் தேசியக் கட்சி அந்தஸ்து பெற்றது\n2. தேசியக் கட்சி அந்தஸ்து பெற்ற வடகிழக்கு இந்தியாவின் முதல் கட்சி (2019)\n3. எஸ்சி, எஸ்டி மற்றும் ஓபிசி மக்களை பிரதிநிதித்துவப்படுத்தி 1984-ல் உருவானது\n4. 1964-ல் இந்திய கம்யூனிஸ்ட் கட்சியிலிருந்து சித்தாந்த ரீதியாகப் பிரிந்து உருவானது\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2", "A",
         "NPP -> Northeast party (2); AAP -> 2023 recognition (1); CPI(M) -> 1964 split (4); BSP -> 1984 Kanshi Ram (3). Code: 2-1-4-3.",
         "NPP -> வடகிழக்கு கட்சி (2); ஆம் ஆத்மி -> 2023 அந்தஸ்து (1); சிபிஎம் -> 1964 பிளவு (4); பகுஜன் சமாஜ் -> 1984 இயக்கம் (3). குறியீடு: 2-1-4-3."),

        # MF_023: Tribal & Regional Autonomy Pressure Groups
        ("023", "Tribal and Regional Autonomy Movements", "Hard",
         "Match List-I (Regional / Autonomy Pressure Group) with List-II (State / Regional Demand):\nList-I:\na) All Bodo Students' Union (ABSU)\nb) Gorkha National Liberation Front (GNLF)\nc) Jharkhand Mukti Morcha (prior to 2000 statehood)\nd) Mizo National Front (MNF - prior to 1986 Accord)\nList-II:\n1. Darjeeling Hills (West Bengal)\n2. Bodoland Territorial Region (Assam)\n3. Mizoram (Independent statehood / sovereignty demand)\n4. Chhota Nagpur and Santhal Parganas statehood (Bihar)\nSelect the correct code:",
         "பட்டியல்-I (பிராந்திய சுயாட்சி அழுத்தக் குழு) உடன் பட்டியல்-II (மாநிலம் / சுயாட்சிக் கோரிக்கை) பொருத்துக:\nபட்டியல்-I:\na) அகில போடோ மாணவர் சங்கம் (ABSU)\nb) கோர்க்கா தேசிய விடுதலை முன்னணி (GNLF)\nc) ஜார்க்கண்ட் முக்தி மோர்ச்சா (2000-க்கு முன்)\nd) மிசோ தேசிய முன்னணி (MNF - 1986 ஒப்பந்தத்திற்கு முன்)\nபட்டியல்-II:\n1. டார்ஜிலிங் மலைப்பகுதி (மேற்கு வங்கம்)\n2. போடோலாந்து பகுதி (அசாம்)\n3. மிசோரம் (சுதந்திரம் / தனி மாநிலக் கோரிக்கை)\n4. சோட்டா நாக்பூர் மற்றும் சந்தால் பர்கானா தனி மாநிலக் கோரிக்கை (பீகார்)\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-1, d-2", "a-4, b-3, c-1, d-2",
         "a-3, b-4, c-2, d-1", "a-3, b-4, c-2, d-1", "A",
         "ABSU -> Bodoland (2); GNLF -> Darjeeling (1); JMM -> Chhota Nagpur/Jharkhand (4); MNF -> Mizoram (3). Code: 2-1-4-3.",
         "ABSU -> போடோலாந்து (2); GNLF -> டார்ஜிலிங் (1); JMM -> சோட்டா நாக்பூர் (4); MNF -> மிசோரம் (3). குறியீடு: 2-1-4-3."),

        # MF_024: Religious & Caste Pressure Groups
        ("024", "Religious and Cultural Pressure Groups", "Medium",
         "Match List-I (Cultural / Religious Organization) with List-II (Year of Establishment):\nList-I:\na) Rashtriya Swayamsevak Sangh (RSS)\nb) Shiromani Gurdwara Parbandhak Committee (SGPC)\nc) Vishva Hindu Parishad (VHP)\nd) Jamaat-e-Islami Hind\nList-II:\n1. 1920\n2. 1925\n3. 1948\n4. 1964\nSelect the correct code:",
         "பட்டியல்-I (கலாச்சார / மத அமைப்பு) உடன் பட்டியல்-II (நிறுவப்பட்ட ஆண்டு) பொருத்துக:\nபட்டியல்-I:\na) ராஷ்ட்ரிய சுயம்சேவக் சங்கம் (RSS)\nb) சிரோமணி குருத்வாரா பிரபந்தக் குழு (SGPC)\nc) விஸ்வ ஹிந்து பரிஷத் (VHP)\nd) ஜமாத்-இ-இஸ்லாமி ஹிந்த்\nபட்டியல்-II:\n1. 1920\n2. 1925\n3. 1948\n4. 1964\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-4, b-3, c-1, d-2", "a-4, b-3, c-1, d-2",
         "a-3, b-4, c-2, d-1", "a-3, b-4, c-2, d-1", "A",
         "RSS -> 1925 (2); SGPC -> 1920 (1); VHP -> 1964 (4); Jamaat -> 1948 (3). Code: 2-1-4-3.",
         "RSS -> 1925 (2); SGPC -> 1920 (1); VHP -> 1964 (4); ஜமாத் -> 1948 (3). குறியீடு: 2-1-4-3."),

        # MF_025: Scholarly Books on Indian Politics and Parties
        ("025", "Seminal Books on Indian Politics", "Hard",
         "Match List-I (Scholarly Book / Monograph) with List-II (Author / Political Scientist):\nList-I:\na) Politics in India (1970)\nb) In Pursuit of Lakshmi: The Political Economy of the Indian State (1987)\nc) The Politics of Scarcity: Public Pressure and Political Response in India (1962)\nd) Factional Politics in an Indian State: The Congress Party in Uttar Pradesh (1965)\nList-II:\n1. Lloyd I. Rudolph and Susanne Hoeber Rudolph\n2. Rajni Kothari\n3. Paul R. Brass\n4. Myron Weiner\nSelect the correct code:",
         "பட்டியல்-I (அரசியல் ஆய்வு நூல்) உடன் பட்டியல்-II (ஆசிரியர் / அரசியல் அறிஞர்) பொருத்துக:\nபட்டியல்-I:\na) பாலிடிக்ஸ் இன் இந்தியா (Politics in India, 1970)\nb) இன் பர்சூட் ஆஃப் லட்சுமி (In Pursuit of Lakshmi, 1987)\nc) தி பாலிடிக்ஸ் ஆஃப் ஸ்கேர்சிட்டி (The Politics of Scarcity, 1962)\nd) ஃபேக்ஷனல் பாலிடிக்ஸ் இன் அன் இந்தியன் ஸ்டேட் (1965)\nபட்டியல்-II:\n1. லாயிட் ஐ. ருடால்ஃப் மற்றும் சுசேன் ருடால்ஃப்\n2. ரஜினி கோத்தாரி\n3. பால் ஆர். பிராஸ்\n4. மைரான் வீனர்\nசரியான குறியீட்டைத் தேர்ந்தெடுக்க:",
         "a-2, b-1, c-4, d-3", "a-2, b-1, c-4, d-3",
         "a-1, b-2, c-3, d-4", "a-1, b-2, c-3, d-4",
         "a-3, b-4, c-1, d-2", "a-3, b-4, c-1, d-2",
         "a-4, b-3, c-2, d-1", "a-4, b-3, c-2, d-1", "A",
         "Politics in India -> Rajni Kothari (2); In Pursuit of Lakshmi -> Rudolph & Rudolph (1); Politics of Scarcity -> Myron Weiner (4); Factional Politics -> Paul Brass (3). Code: 2-1-4-3.",
         "பாலிடிக்ஸ் இன் இந்தியா -> ரஜினி கோத்தாரி (2); இன் பர்சூட் ஆஃப் லட்சுமி -> ருடால்ஃப் (1); பாலிடிக்ஸ் ஆஃப் ஸ்கேர்சிட்டி -> மைரான் வீனர் (4); ஃபேக்ஷனல் பாலிடிக்ஸ் -> பால் பிராஸ் (3). குறியீடு: 2-1-4-3.")
    ]

    for item in match_specs:
        num, subtopic, diff, en_stem, ta_stem, en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d, correct_key, exp_en, exp_ta = item
        qid = f"PPPG_MF_{num}"
        why_a_en = f"Evaluation of Option A ({en_a}): Correct matching of the respective organizations, provisions, and leaders."
        why_a_ta = f"ஆப்ஷன் A ({ta_a}) மதிப்பீடு: நிறுவனங்கள், பிரிவுகள் மற்றும் தலைவர்களின் சரியான பொருத்தம்."
        why_b_en = f"Evaluation of Option B ({en_b}): Mismatched pairings across lists."
        why_b_ta = f"ஆப்ஷன் B ({ta_b}) மதிப்பீடு: பட்டியல்களுக்கு இடையிலான தவறான பொருத்தம்."
        why_c_en = f"Evaluation of Option C ({en_c}): Inverted codes and mismatched associations."
        why_c_ta = f"ஆப்ஷன் C ({ta_c}) மதிப்பீடு: தலைகீழ் குறியீடுகள் மற்றும் தவறான இணைப்புகள்."
        why_d_en = f"Evaluation of Option D ({en_d}): Distractor pairing."
        why_d_ta = f"ஆப்ஷன் D ({ta_d}) மதிப்பீடு: தவறான தெரிவு."
        tip_en = "Confirm code associations by identifying at least two definite pairs in the lists."
        tip_ta = "பட்டியல்களில் குறைந்தது இரண்டு உறுதியான ஜோடிகளை அடையாளம் கண்டு குறியீட்டை உறுதி செய்க."
        fact_en = "Political parties contest elections for power, whereas pressure groups influence public policy from outside."
        fact_ta = "அரசியல் கட்சிகள் ஆட்சியைப் பிடிக்க தேர்தலில் போட்டியிடுகின்றன, ஆனால் அழுத்தக் குழுக்கள் வெளியில் இருந்து கொள்கைகளை மாற்றுகின்றன."

        q = make_pppg_q(
            qid, diff, "match_the_following", subtopic,
            en_stem, ta_stem,
            en_a, ta_a, en_b, ta_b, en_c, ta_c, en_d, ta_d,
            correct_key,
            exp_en, exp_ta,
            why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
            tip_en, tip_ta, fact_en, fact_ta
        )
        questions.append(q)

    # Apply locked randomizer
    balanced_questions = randomize_and_balance_dataset(questions, seed=208)

    keys = [q["correct_answer"] for q in balanced_questions]
    counts = Counter(keys)
    print("Part 2B PPPG Match Key counts:", counts)
    assert len(balanced_questions) == 25
    for opt in ["A", "B", "C", "D"]:
        assert 6 <= counts[opt] <= 7

    out_path = "data/questions/polity/political_parties_pressure_groups_match_the_following.json"
    alias_path = "data/questions/polity/political_parties_pressure_groups_match.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(balanced_questions, f, indent=2, ensure_ascii=False)
    shutil.copyfile(out_path, alias_path)
    print(f"Successfully wrote 25 match MCQs to {out_path} and {alias_path}")

if __name__ == "__main__":
    get_match_questions()
