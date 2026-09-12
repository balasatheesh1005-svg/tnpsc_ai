"""
Generator for Election Commission Chronology 25 MCQs (EC_C_001 to EC_C_025).
Strictly adheres to the 24-field schema and ChronologyValidator requirements:
- Presented items in non-chronological order (presented != correct).
- Explanations with 4-digit years and sequence arrows (->).
- Balanced answer keys across A, B, C, D.
"""

import json
import os
import re
from ec_mcq_helper import make_ec_q
from tools.nova_content_engine.chronology_validator import ChronologyValidator

OUTPUT_PATH = os.path.join("data", "questions", "polity", "election_commission_chronology.json")

RAW_CHRONOLOGY = [
    # 1 - Target Key: A
    {
        "id": "EC_C_001",
        "intro_en": "Arrange the following historic institutional milestones of the Election Commission of India in chronological order:",
        "intro_ta": "இந்தியத் தேர்தல் ஆணையத்தின் பின்வரும் வரலாற்றுச் சிறப்புமிக்க நிறுவன மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Constitution (61st Amendment) Act lowering voting age to 18",
            "Establishment of the Election Commission of India under Article 324",
            "Promulgation of the Ordinance restoring permanent three-member Commission",
            "Conduct of the First General Elections of Independent India"
        ],
        "items_ta": [
            "வாக்களிக்கும் வயதை 18-ஆகக் குறைத்த 61-வது அரசியலமைப்புத் திருத்தச் சட்டம்",
            "சரத்து 324-ன் கீழ் இந்தியத் தேர்தல் ஆணையம் நிறுவப்படுதல்",
            "நிரந்தர 3 உறுப்பினர் ஆணையத்தை மீட்டெடுத்த அவசரச் சட்டம் பிறப்பிக்கப்படுதல்",
            "சுதந்திர இந்தியாவின் முதல் பொதுத் தேர்தல்கள் நடத்தப்படுதல்"
        ],
        "years": ["1988", "1950", "1993", "1951-1952"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "target_key": "A",
        "exp_en": "The correct chronological order is:\n2. Establishment of ECI: 25 January 1950\n4. First General Elections: October 1951 – February 1952\n1. 61st Constitutional Amendment Act: 1988 (enforced 1989)\n3. Three-member Commission restored: 1 October 1993\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "சரியான காலவரிசை:\n2. தேர்தல் ஆணையம் நிறுவப்பட்டது: 25 ஜனவரி 1950\n4. முதல் பொதுத் தேர்தல்: அக்டோபர் 1951 – பிப்ரவரி 1952\n1. 61-வது அரசியலமைப்புத் திருத்தச் சட்டம்: 1988\n3. மூன்று உறுப்பினர் ஆணையம் மீண்டும் நிறுவப்பட்டது: 1 அக்டோபர் 1993\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "ECI was established on 25 January 1950, celebrated nationwide as National Voters' Day.",
        "tip_ta": "தேர்தல் ஆணையம் 25 ஜனவரி 1950-ல் நிறுவப்பட்டது; இது தேசிய வாக்காளர் தினமாகக் கொண்டாடப்படுகிறது.",
        "fact_en": "Article 324 came into force on 26 November 1949, before the rest of the Constitution on 26 January 1950.",
        "fact_ta": "அரசியலமைப்பின் பிற பகுதிகள் ஜனவரி 26, 1950-ல் நடைமுறைக்கு வருவதற்கு முன்பே, நவம்பர் 26, 1949 அன்றே சரத்து 324 நடைமுறைக்கு வந்தது.",
        "tags": ["ECI History", "Chronology", "Milestones"]
    },
    # 2 - Target Key: B
    {
        "id": "EC_C_002",
        "intro_en": "Arrange the following distinguished Chief Election Commissioners of India in the order of their assumption of office:",
        "intro_ta": "இந்தியாவின் பின்வரும் தலைமைத் தேர்தல் ஆணையர்களை அவர்கள் பதவியேற்ற காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "T.N. Seshan",
            "Sukumar Sen",
            "J.M. Lyngdoh",
            "K.V.K. Sundaram"
        ],
        "items_ta": [
            "டி.என். சேஷன்",
            "சுகுமார் சென்",
            "ஜே.எம். லிங்டோ",
            "கே.வி.கே. சுந்தரம்"
        ],
        "years": ["1990-1996", "1950-1958", "2001-2004", "1958-1967"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[2, 1, 4, 3], [4, 2, 1, 3], [1, 2, 4, 3]],
        "target_key": "B",
        "exp_en": "The correct chronological tenure sequence is:\n2. Sukumar Sen: 1950 – 1958 (First CEC)\n4. K.V.K. Sundaram: 1958 – 1967 (Second CEC)\n1. T.N. Seshan: 1990 – 1996 (10th CEC)\n3. J.M. Lyngdoh: 2001 – 2004 (12th CEC)\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "சரியான பதவிக்கால காலவரிசை:\n2. சுகுமார் சென்: 1950 – 1958 (முதல் CEC)\n4. கே.வி.கே. சுந்தரம்: 1958 – 1967 (இரண்டாவது CEC)\n1. டி.என். சேஷன்: 1990 – 1996 (10-வது CEC)\n3. ஜே.எம். லிங்டோ: 2001 – 2004 (12-வது CEC)\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "Sukumar Sen was India's 1st CEC and also served as Chief Election Commissioner of Sudan in 1953.",
        "tip_ta": "சுகுமார் சென் இந்தியாவின் 1வது தலைமை தேர்தல் ஆணையர் ஆவார்; மேலும் 1953-ல் சூடானின் தலைமை தேர்தல் ஆணையராகவும் பணியாற்றினார்.",
        "fact_en": "K.V.K. Sundaram had the longest tenure as CEC (over 8 years and 8 months).",
        "fact_ta": "கே.வி.கே. சுந்தரம் தலைமைத் தேர்தல் ஆணையராக மிக நீண்ட காலம் (8 ஆண்டுகளுக்கும் மேலாக) பணியாற்றினார்.",
        "tags": ["Chief Election Commissioners", "Tenure", "Chronology"]
    },
    # 3 - Target Key: C
    {
        "id": "EC_C_003",
        "intro_en": "Arrange the following advancements in Indian voting technology and audit systems in chronological order of their introduction:",
        "intro_ta": "இந்திய வாக்குப்பதிவு தொழில்நுட்பம் மற்றும் தணிக்கை அமைப்புகளின் பின்வரும் முன்னேற்றங்களை அவை அறிமுகப்படுத்தப்பட்ட காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Experimental use of VVPAT in Noksen Assembly constituency of Nagaland",
            "First trial use of Electronic Voting Machines (EVMs) in Paravur, Kerala",
            "Mandatory 100% deployment of VVPAT units across all parliamentary constituencies",
            "Insertion of Section 61A in RPA 1951 providing statutory backing for EVMs"
        ],
        "items_ta": [
            "நாகாலாந்தின் நோக்சென் சட்டமன்றத் தொகுதியில் விவிபேட் (VVPAT) சோதனை பயன்பாடு",
            "கேரளாவின் பரவூரில் மின்னணு வாக்குப்பதிவு இயந்திரங்களின் (EVM) முதல் மாதிரி பயன்பாடு",
            "அனைத்து மக்களவைத் தொகுதிகளிலும் 100% விவிபேட் பயன்பாடு கட்டாயமாக்கப்படுதல்",
            "EVM-களுக்கு சட்டபூர்வ ஆதரவை வழங்க 1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தில் பிரிவு 61A சேர்க்கப்படுதல்"
        ],
        "years": ["2013", "1982", "2019", "1989"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "target_key": "C",
        "exp_en": "The correct chronological order is:\n2. First EVM trial in Paravur: May 1982\n4. Section 61A inserted in RPA 1951: March 1989\n1. Experimental VVPAT at Noksen: September 2013\n3. 100% VVPAT in Lok Sabha elections: April-May 2019\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "சரியான காலவரிசை:\n2. பரவூரில் முதல் EVM பயன்பாடு: மே 1982\n4. பிரிவு 61A சேர்க்கப்பட்டது: மார்ச் 1989\n1. நோக்செனில் விவிபேட் பயன்பாடு: செப்டம்பர் 2013\n3. 100% விவிபேட் பொதுத்தேர்தல்: ஏப்ரல்-மே 2019\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "EVMs were developed in collaboration with Bharat Electronics Limited (BEL) and Electronics Corporation of India Limited (ECIL).",
        "tip_ta": "EVM-கள் பாரத் எலக்ட்ரானிக்ஸ் (BEL) மற்றும் எலக்ட்ரானிக்ஸ் கார்ப்பரேஷன் ஆஃப் இந்தியா (ECIL) ஆகியவற்றால் உருவாக்கப்பட்டன.",
        "fact_en": "The 2004 Lok Sabha election was the first general election conducted entirely using EVMs.",
        "fact_ta": "2004 மக்களவைத் தேர்தலே நாடு முழுவதும் முழுமையாக EVM கொண்டு நடத்தப்பட்ட முதல் பொதுத் தேர்தலாகும்.",
        "tags": ["EVM", "VVPAT", "Voting Technology"]
    },
    # 4 - Target Key: D
    {
        "id": "EC_C_004",
        "intro_en": "Arrange the following landmark Supreme Court judgments concerning Indian electoral jurisprudence in chronological order:",
        "intro_ta": "இந்தியத் தேர்தல் நீதித்துறை தொடர்பான பின்வரும் வரலாற்றுச் சிறப்புமிக்க உச்ச நீதிமன்றத் தீர்ப்புகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Lily Thomas v. Union of India (striking down Section 8(4) of RPA 1951)",
            "Mohinder Singh Gill v. Chief Election Commissioner (plenary reservoir under Article 324)",
            "Sadiq Ali v. Election Commission of India (numerical test for party split)",
            "Anoop Baranwal v. Union of India (statutory collegium for CEC and ECs)"
        ],
        "items_ta": [
            "லில்லி தாமஸ் எதிர் இந்திய ஒன்றியம் (பிரிவு 8(4) ரத்து)",
            "மோஹிந்தர் சிங் கில் எதிர் தலைமை தேர்தல் ஆணையர் (சரத்து 324-ன் கீழ் முழுமையான அதிகாரம்)",
            "சாதிக் அலி எதிர் இந்திய தேர்தல் ஆணையம் (கட்சி பிளவிற்கான பெரும்பான்மை சோதனை)",
            "அனூப் பரன்வால் எதிர் இந்திய ஒன்றியம் (CEC மற்றும் EC நியமனத்திற்கான கொலீஜியம்)"
        ],
        "years": ["2013", "1978", "1972", "2023"],
        "correct_seq": [3, 2, 1, 4],
        "distractors": [[2, 3, 1, 4], [3, 1, 2, 4], [1, 3, 2, 4]],
        "target_key": "D",
        "exp_en": "The correct chronological sequence of SC judgments is:\n3. Sadiq Ali v. ECI: 1972\n2. Mohinder Singh Gill v. CEC: 1978\n1. Lily Thomas v. UOI: July 2013\n4. Anoop Baranwal v. UOI: March 2023\nChronological sequence: 3 -> 2 -> 1 -> 4.",
        "exp_ta": "உச்ச நீதிமன்ற தீர்ப்புகளின் சரியான காலவரிசை:\n3. சாதிக் அலி வழக்கு: 1972\n2. மோஹிந்தர் சிங் கில் வழக்கு: 1978\n1. லில்லி தாமஸ் வழக்கு: ஜூலை 2013\n4. அனூப் பரன்வால் வழக்கு: மார்ச் 2023\nகாலவரிசை: 3 -> 2 -> 1 -> 4.",
        "tip_en": "Mohinder Singh Gill established that Article 324 is a reservoir of power when enacted laws are silent.",
        "tip_ta": "சட்டங்கள் மௌனம் சாதிக்கும் போது சரத்து 324 தேர்தல் ஆணையத்திற்கு முழு அதிகாரத்தை வழங்குகிறது என மோஹிந்தர் சிங் கில் தீர்ப்பு உறுதி செய்தது.",
        "fact_en": "Lily Thomas ended the immunity enjoyed by convicted sitting legislators under Section 8(4) of RPA 1951.",
        "fact_ta": "லில்லி தாமஸ் தீர்ப்பு தகுதிநீக்கத்திலிருந்து சட்டமன்ற, பாராளுமன்ற உறுப்பினர்களுக்கு வழங்கப்பட்ட பாதுகாப்பை ரத்து செய்தது.",
        "tags": ["Landmark Cases", "Supreme Court", "Electoral Jurisprudence"]
    },
    # 5 - Target Key: A
    {
        "id": "EC_C_005",
        "intro_en": "Arrange the following Constitutional Amendment Acts relating to elections and legislature composition in chronological order:",
        "intro_ta": "தேர்தல்கள் மற்றும் சட்டமன்றங்களின் கட்டமைப்பு தொடர்பான பின்வரும் அரசியலமைப்புத் திருத்தச் சட்டங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Constitution (61st Amendment) Act lowering voting age from 21 to 18",
            "Constitution (19th Amendment) Act abolishing Election Tribunals and vesting jurisdiction in High Courts",
            "Constitution (84th Amendment) Act freezing constituency seat allocation until 2026",
            "Constitution (52nd Amendment) Act introducing the Anti-Defection Tenth Schedule"
        ],
        "items_ta": [
            "வாக்குரிமை வயதை 21-லிருந்து 18-ஆகக் குறைத்த 61-வது அரசியலமைப்புத் திருத்தச் சட்டம்",
            "தேர்தல் தீர்ப்பாயங்களை ரத்து செய்து உயர் நீதிமன்றங்களுக்கு அதிகாரம் அளித்த 19-வது திருத்தச் சட்டம்",
            "தொகுதிகளின் இடப் பங்கீட்டை 2026 வரை முடக்கிய 84-வது அரசியலமைப்புத் திருத்தச் சட்டம்",
            "கட்சித்தாவல் தடை 10-வது அட்டவணையை அறிமுகப்படுத்திய 52-வது திருத்தச் சட்டம்"
        ],
        "years": ["1988", "1966", "2001", "1985"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "target_key": "A",
        "exp_en": "The correct chronological sequence of Constitutional Amendments is:\n2. 19th Amendment Act: 1966 (abolished election tribunals)\n4. 52nd Amendment Act: 1985 (Tenth Schedule Anti-Defection)\n1. 61st Amendment Act: 1988 (lowered voting age to 18)\n3. 84th Amendment Act: 2001 (froze delimitation seats to 2026)\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "அரசியலமைப்புத் திருத்தச் சட்டங்களின் சரியான காலவரிசை:\n2. 19-வது திருத்தச் சட்டம்: 1966\n4. 52-வது திருத்தச் சட்டம்: 1985\n1. 61-வது திருத்தச் சட்டம்: 1988\n3. 84-வது திருத்தச் சட்டம்: 2001\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "The 19th Amendment amended Article 324(1) by deleting the word 'election tribunals'.",
        "tip_ta": "19-வது திருத்தச் சட்டம் சரத்து 324(1)-லிருந்து 'தேர்தல் தீர்ப்பாயங்கள்' என்ற வார்த்தையை நீக்கியது.",
        "fact_en": "The 84th Amendment froze the total seats in Lok Sabha based on the 1971 census until the first census taken after 2026.",
        "fact_ta": "84-வது திருத்தச் சட்டம் 1971 மக்கள் தொகை கணக்கெடுப்பின் அடிப்படையிலான மக்களவை இடங்களை 2026 வரை முடக்கியது.",
        "tags": ["Constitutional Amendments", "Delimitation", "Anti-Defection"]
    },
    # 6 - Target Key: B
    {
        "id": "EC_C_006",
        "intro_en": "Arrange the constitution of the following Delimitation Commissions of India in chronological order:",
        "intro_ta": "இந்தியாவின் பின்வரும் தொகுதி மறுவரையறை ஆணையங்கள் அமைக்கப்பட்டதை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Third Delimitation Commission constituted under 1972 Act",
            "First Delimitation Commission constituted under 1952 Act",
            "Fourth Delimitation Commission headed by Justice Kuldip Singh",
            "Second Delimitation Commission constituted under 1962 Act"
        ],
        "items_ta": [
            "1972 சட்டத்தின் கீழ் அமைக்கப்பட்ட மூன்றாவது தொகுதி மறுவரையறை ஆணையம்",
            "1952 சட்டத்தின் கீழ் அமைக்கப்பட்ட முதல் தொகுதி மறுவரையறை ஆணையம்",
            "நீதிபதி குல்தீப் சிங் தலைமையில் அமைக்கப்பட்ட நான்காவது தொகுதி மறுவரையறை ஆணையம்",
            "1962 சட்டத்தின் கீழ் அமைக்கப்பட்ட இரண்டாவது தொகுதி மறுவரையறை ஆணையம்"
        ],
        "years": ["1972", "1952", "2002", "1962"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[2, 1, 4, 3], [4, 2, 1, 3], [1, 2, 4, 3]],
        "target_key": "B",
        "exp_en": "The Delimitation Commissions were constituted in:\n2. First Delimitation Commission: 1952\n4. Second Delimitation Commission: 1962\n1. Third Delimitation Commission: 1972\n3. Fourth Delimitation Commission: 2002 (Justice Kuldip Singh)\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "தொகுதி மறுவரையறை ஆணையங்கள் அமைக்கப்பட்ட காலவரிசை:\n2. முதல் மறுவரையறை ஆணையம்: 1952\n4. இரண்டாவது மறுவரையறை ஆணையம்: 1962\n1. மூன்றாவது மறுவரையறை ஆணையம்: 1972\n3. நான்காவது மறுவரையறை ஆணையம்: 2002 (நீதிபதி குல்தீப் சிங்)\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "No Delimitation Commission was set up after the 1981 and 1991 censuses due to the 42nd Amendment freeze.",
        "tip_ta": "42-வது திருத்தச் சட்ட முடக்கம் காரணமாக 1981 மற்றும் 1991 மக்கள் தொகை கணக்கெடுப்புகளுக்குப் பின் மறுவரையறை ஆணையம் அமைக்கப்படவில்லை.",
        "fact_en": "Article 82 provides for readjustment of allocation of seats after each census by law enacted by Parliament.",
        "fact_ta": "ஒவ்வொரு மக்கள் தொகை கணக்கெடுப்பிற்குப் பிறகும் தொகுதிகளை மறுசீரமைக்க பாராளுமன்ற சட்டம் இயற்ற சரத்து 82 வகை செய்கிறது.",
        "tags": ["Delimitation Commission", "Article 82", "Constituency Delimitation"]
    },
    # 7 - Target Key: C
    {
        "id": "EC_C_007",
        "intro_en": "Arrange the following expert committees and law commission reports on electoral reforms in chronological order:",
        "intro_ta": "தேர்தல் சீர்திருத்தங்கள் குறித்த பின்வரும் நிபுணர் குழுக்கள் மற்றும் சட்ட ஆணைய அறிக்கைகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Indrajit Gupta Committee Report on State Funding of Elections",
            "Tarkunde Committee Report on Electoral Reform (appointed by Jayaprakash Narayan)",
            "Law Commission 255th Report on Electoral Reforms",
            "Dinesh Goswami Committee on Electoral Reforms"
        ],
        "items_ta": [
            "தேர்தல்களுக்கான அரசு நிதியுதவி குறித்த இந்திரஜித் குப்தா குழு அறிக்கை",
            "தேர்தல் சீர்திருத்தங்களுக்கான தர்குண்டே குழு அறிக்கை (ஜெயபிரகாஷ் நாராயணனால் நியமிக்கப்பட்டது)",
            "தேர்தல் சீர்திருத்தங்கள் குறித்த இந்திய சட்ட ஆணையத்தின் 255-வது அறிக்கை",
            "தேர்தல் சீர்திருத்தங்கள் குறித்த தினேஷ் கோஸ்வாமி குழு"
        ],
        "years": ["1998", "1974-1975", "2015", "1990"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "target_key": "C",
        "exp_en": "The correct chronological sequence of electoral reform committees is:\n2. Tarkunde Committee: 1974 – 1975\n4. Dinesh Goswami Committee: 1990\n1. Indrajit Gupta Committee: 1998\n3. Law Commission 255th Report: March 2015\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "தேர்தல் சீர்திருத்தக் குழுக்களின் சரியான காலவரிசை:\n2. தர்குண்டே குழு: 1974 – 1975\n4. தினேஷ் கோஸ்வாமி குழு: 1990\n1. இந்திரஜித் குப்தா குழு: 1998\n3. சட்ட ஆணையத்தின் 255-வது அறிக்கை: மார்ச் 2015\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "Indrajit Gupta Committee recommended partial state funding of elections in kind (goods/services), not cash.",
        "tip_ta": "இந்திரஜித் குப்தா குழு தேர்தல்களுக்கு பணமாக அல்லாமல் பொருட்களாக பகுதி அரசு நிதியுதவி அளிக்க பரிந்துரைத்தது.",
        "fact_en": "Dinesh Goswami Committee recommended EVM deployment and tightening anti-defection provisions.",
        "fact_ta": "தினேஷ் கோஸ்வாமி குழு EVM-களைப் பயன்படுத்துவதையும், கட்சித்தாவல் தடைச் சட்டத்தை வலுப்படுத்துவதையும் பரிந்துரைத்தது.",
        "tags": ["Electoral Committees", "Law Commission", "Electoral Reforms"]
    },
    # 8 - Target Key: D
    {
        "id": "EC_C_008",
        "intro_en": "Arrange the following statutory stages of an election process under Section 30 of the Representation of the People Act, 1951 in chronological order:",
        "intro_ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 30-ன் கீழ் தேர்தல் நடைமுறையின் பின்வரும் சட்டப்பூர்வ கட்டங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Scrutiny of nomination papers by Returning Officer",
            "Publication of official election notification calling upon the constituency to elect",
            "Last date for the withdrawal of candidatures",
            "Last date for making nominations by candidates"
        ],
        "items_ta": [
            "தேர்தல் நடத்தும் அதிகாரியால் வேட்புமனுக்கள் பரிசீலனை செய்யப்படுதல்",
            "தொகுதியை பிரதிநிதியை தேர்ந்தெடுக்க அழைக்கும் அதிகாரப்பூர்வ தேர்தல் அறிவிக்கை வெளியிடப்படுதல்",
            "வேட்புமனுக்களை திரும்பப் பெறுவதற்கான கடைசி நாள்",
            "வேட்பாளர்கள் வேட்புமனு தாக்கல் செய்வதற்கான கடைசி நாள்"
        ],
        "years": ["Step 3", "Step 1", "Step 4", "Step 2"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "target_key": "D",
        "exp_en": "Under Section 30 of the Representation of the People Act, 1951, the mandatory chronological stages are:\n2. Election notification issued: Section 30(a)\n4. Last date for making nominations: Section 30(b) (7th day after notification)\n1. Date for scrutiny of nominations: Section 30(c) (day immediately following last date for nomination)\n3. Last date for withdrawal of candidatures: Section 30(d) (2nd day after scrutiny)\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 30-ன் கீழ் காலவரிசை படிகள்:\n2. தேர்தல் அறிவிக்கை வெளியீடு: பிரிவு 30(a)\n4. வேட்புமனு தாக்கல் கடைசி நாள்: பிரிவு 30(b)\n1. வேட்புமனு பரிசீலனை: பிரிவு 30(c)\n3. வேட்புமனு வாபஸ் பெற கடைசி நாள்: பிரிவு 30(d)\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "Campaign period is the interval between the withdrawal of candidatures and 48 hours before the end of poll.",
        "tip_ta": "வேட்புமனு திரும்பப் பெற்றதற்கும் வாக்குப்பதிவு முடிவதற்கு 48 மணி நேரத்திற்கு முந்தைய காலத்திற்கும் இடைப்பட்டதே பிரச்சார காலமாகும்.",
        "fact_en": "Section 30 of RPA 1951 sets rigid statutory minimum timelines between nomination, scrutiny, withdrawal, and polling date.",
        "fact_ta": "1951 சட்டத்தின் பிரிவு 30 வேட்புமனு, பரிசீலனை, வாபஸ் மற்றும் வாக்குப்பதிவு தேதிகளுக்கு இடையிலான கால வரம்புகளை நிர்ணயிக்கிறது.",
        "tags": ["Section 30 RPA 1951", "Election Timeline", "Statutory Process"]
    },
    # 9 - Target Key: A
    {
        "id": "EC_C_009",
        "intro_en": "Arrange the following judicial interventions expanding voter transparency and choice in chronological order:",
        "intro_ta": "வாக்காளர் வெளிப்படைத்தன்மை மற்றும் தேர்வை விரிவுபடுத்திய பின்வரும் நீதிமன்றத் தலையீடுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "PUCL v. Union of India directing introduction of 'None of the Above' (NOTA) option",
            "Union of India v. Association for Democratic Reforms (ADR) mandating candidate criminal and asset disclosures",
            "Association for Democratic Reforms v. Union of India striking down the Electoral Bond Scheme",
            "PUCL v. Union of India declaring unconstitutional the ordinance restricting candidate disclosure"
        ],
        "items_ta": [
            "PUCL எதிர் இந்திய ஒன்றியம் வழக்கில் 'மேற்கண்ட எவருமில்லை' (NOTA) விருப்பத்தை அறிமுகப்படுத்த உத்தரவு",
            "ADR வழக்கில் வேட்பாளர்களின் குற்றப்பின்னணி மற்றும் சொத்து விபரங்களை வெளியிட கட்டாயமாக்குதல்",
            "தேர்தல் பத்திரத் திட்டத்தை அரசியலமைப்பிற்கு முரணானது என ரத்து செய்த ADR வழக்கு",
            "வேட்பாளர் தகவல் வெளிப்படுத்தலைக் கட்டுப்படுத்திய அவசரச் சட்டத்தை ரத்து செய்த PUCL வழக்கு"
        ],
        "years": ["2013", "2002", "2024", "2003"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "target_key": "A",
        "exp_en": "The chronological sequence of voter transparency rulings is:\n2. ADR judgment (candidate disclosure): May 2002\n4. PUCL judgment (striking down Section 33B): March 2003\n1. PUCL NOTA judgment: September 2013\n3. ADR Electoral Bond judgment: February 2024\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "வாக்காளர் வெளிப்படைத்தன்மை தீர்ப்புகளின் காலவரிசை:\n2. ADR தீர்ப்பு (சொத்து/குற்ற வெளிப்பாடு): மே 2002\n4. PUCL தீர்ப்பு (பிரிவு 33B ரத்து): மார்ச் 2003\n1. PUCL நோட்டா தீர்ப்பு: செப்டம்பர் 2013\n3. தேர்தல் பத்திரத் திட்ட ரத்து தீர்ப்பு: பிப்ரவரி 2024\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "Voters' right to know candidate backgrounds was grounded in Article 19(1)(a) freedom of speech and expression.",
        "tip_ta": "வேட்பாளர்களின் பின்னணியை அறியும் வாக்காளரின் உரிமை சரத்து 19(1)(a) பேச்சுரிமையின் அங்கமாக நிலைநாட்டப்பட்டது.",
        "fact_en": "NOTA was first implemented in the 2013 State Legislative Assembly elections in Delhi, Chhattisgarh, MP, Rajasthan, and Mizoram.",
        "fact_ta": "2013-ல் தில்லி, சத்தீஸ்கர், மத்தியப் பிரதேசம், ராஜஸ்தான், மிசோரம் சட்டமன்றத் தேர்தல்களில் முதன்முதலில் நோட்டா பயன்படுத்தப்பட்டது.",
        "tags": ["NOTA", "Electoral Transparency", "Supreme Court Judgments"]
    },
    # 10 - Target Key: B
    {
        "id": "EC_C_010",
        "intro_en": "Arrange the following events in the evolution of the Election Commission's multi-member composition in chronological order:",
        "intro_ta": "தேர்தல் ஆணையத்தின் பல உறுப்பினர் அமைப்பின் பரிணாம வளர்ச்சியின் பின்வரும் நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Presidential notification abolishing the two posts of Election Commissioners reverting ECI to a single-member body",
            "Establishment of the Election Commission as an inherently single-member body under Article 324(2)",
            "Chief Election Commissioner and other Election Commissioners (Conditions of Service) Amendment Ordinance making ECI permanently multi-member",
            "Presidential notification appointing two additional Election Commissioners (S.S. Dhanoa and V.S. Seigell) for the first time"
        ],
        "items_ta": [
            "இரண்டு தேர்தல் ஆணையர் பதவிகளை ரத்து செய்து மீண்டும் ஒற்றை உறுப்பினர் அமைப்பாக மாற்றிய குடியரசுத் தலைவர் அறிவிக்கை",
            "சரத்து 324(2)-ன் கீழ் தேர்தல் ஆணையம் ஒற்றை உறுப்பினர் அமைப்பாக நிறுவப்படுதல்",
            "தேர்தல் ஆணையத்தை நிரந்தரமாக பல உறுப்பினர் அமைப்பாக மாற்றிய அவசரச் சட்டம்",
            "முதன்முறையாக இரண்டு கூடுதல் தேர்தல் ஆணையர்களை (தனோவா மற்றும் சீகல்) நியமித்த குடியரசுத் தலைவர் அறிவிக்கை"
        ],
        "years": ["1990", "1950", "1993", "1989"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[2, 1, 4, 3], [4, 2, 1, 3], [1, 2, 4, 3]],
        "target_key": "B",
        "exp_en": "The institutional evolution of the multi-member Commission follows this timeline:\n2. Established as single-member body: 25 January 1950\n4. Two ECs appointed for the first time: 16 October 1989\n1. Two posts of ECs abolished: 1 January 1990\n3. Permanently made multi-member: 1 October 1993\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "பல உறுப்பினர் அமைப்பின் காலவரிசை:\n2. ஒற்றை உறுப்பினர் அமைப்பாக அமைந்தது: 25 ஜனவரி 1950\n4. முதன்முறையாக 2 கூடுதல் ஆணையர்கள் நியமனம்: 16 அக்டோபர் 1989\n1. இரண்டு ஆணையர் பதவிகள் ரத்து: 1 ஜனவரி 1990\n3. நிரந்தரமாக 3 உறுப்பினர் அமைப்பாக மாறியது: 1 அக்டோபர் 1993\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "S.S. Dhanoa challenged his removal when the post was abolished in 1990, but SC upheld the President's power in S.S. Dhanoa v. UOI.",
        "tip_ta": "1990-ல் பதவி ரத்து செய்யப்பட்டதை எஸ்.எஸ். தனோவா எதிர்த்தார்; ஆனால் குடியரசுத் தலைவரின் அதிகாரத்தை உச்ச நீதிமன்றம் உறுதி செய்தது.",
        "fact_en": "Since 1 October 1993, the Commission has functioned continuously as a 3-member collegiate body.",
        "fact_ta": "அக்டோபர் 1, 1993 முதல் தேர்தல் ஆணையம் தொடர்ந்து 3 உறுப்பினர்களைக் கொண்ட கூட்டு அமைப்பாக இயங்கி வருகிறது.",
        "tags": ["Multi-member Commission", "ECI Composition", "Dhanoa Case"]
    },
    # 11 - Target Key: C
    {
        "id": "EC_C_011",
        "intro_en": "Arrange the enactment/promulgation of the following core electoral statutes and statutory orders in chronological order:",
        "intro_ta": "பின்வரும் முதன்மையான தேர்தல் சட்டங்கள் மற்றும் சட்டப்பூர்வ ஆணைகள் இயற்றப்பட்டதை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Conduct of Elections Rules framed under Section 169 of RPA 1951",
            "Representation of the People Act, 1950 (governing qualification of voters and preparation of rolls)",
            "Election Symbols (Reservation and Allotment) Order promulgated under Article 324",
            "Representation of the People Act, 1951 (governing conduct of elections and disqualifications)"
        ],
        "items_ta": [
            "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 169-ன் கீழ் உருவாக்கப்பட்ட தேர்தல் நடத்தை விதிகள்",
            "1950 மக்கள் பிரதிநிதித்துவச் சட்டம் (வாக்காளர் தகுதிகள் மற்றும் வாக்காளர் பட்டியல் தயாரிப்பு)",
            "சரத்து 324-ன் கீழ் வெளியிடப்பட்ட தேர்தல் சின்னங்கள் (ஒதுக்கீடு) ஆணை",
            "1951 மக்கள் பிரதிநிதித்துவச் சட்டம் (தேர்தல் நடத்தை மற்றும் தகுதிநீக்கங்கள்)"
        ],
        "years": ["1961", "1950", "1968", "1951"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "target_key": "C",
        "exp_en": "The correct chronological enactment sequence is:\n2. Representation of the People Act, 1950: May 1950\n4. Representation of the People Act, 1951: July 1951\n1. Conduct of Elections Rules: April 1961\n3. Election Symbols (Reservation & Allotment) Order: August 1968\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "சரியான காலவரிசை:\n2. 1950 மக்கள் பிரதிநிதித்துவச் சட்டம்: மே 1950\n4. 1951 மக்கள் பிரதிநிதித்துவச் சட்டம்: ஜூலை 1951\n1. தேர்தல் நடத்தை விதிகள்: ஏப்ரல் 1961\n3. தேர்தல் சின்னங்கள் ஆணை: ஆகஸ்ட் 1968\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "RPA 1950 deals with pre-election preparation (rolls, delimitation); RPA 1951 deals with actual election conduct, disputes, and corrupt practices.",
        "tip_ta": "1950 சட்டம் தேர்தலுக்கு முந்தைய ஏற்பாடுகள் பற்றியது; 1951 சட்டம் தேர்தல் நடைமுறைகள் மற்றும் வழக்குகளைக் கையாள்கிறது.",
        "fact_en": "Conduct of Elections Rules 1961 supersedes the earlier Representation of the People (Conduct of Elections and Election Petitions) Rules, 1956.",
        "fact_ta": "1961 தேர்தல் நடத்தை விதிகள் முந்தைய 1956 விதிகளை ரத்து செய்து மாற்றியமைக்கப்பட்டன.",
        "tags": ["RPA 1950", "RPA 1951", "Election Symbols Order 1968"]
    },
    # 12 - Target Key: D
    {
        "id": "EC_C_012",
        "intro_en": "Arrange the introduction of the following voter identity and electoral roll modernizations in chronological order:",
        "intro_ta": "வாக்காளர் அடையாளம் மற்றும் வாக்காளர் பட்டியல் நவீனமயமாக்கலின் பின்வரும் அறிமுகங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Nationwide rollout of Photo Electoral Rolls (PER) containing pictures of voters",
            "Introduction of Electors Photo Identity Card (EPIC) under CEC T.N. Seshan",
            "Election Laws (Amendment) Act enabling voluntary linking of Aadhaar with Electoral Roll",
            "Representation of the People (Amendment) Act granting voting rights to Non-Resident Indians (NRIs)"
        ],
        "items_ta": [
            "வாக்காளர்களின் புகைப்படங்களுடன் கூடிய புகைப்பட வாக்காளர் பட்டியல் (PER) நாடு முழுவதும் அறிமுகம்",
            "தலைமை தேர்தல் ஆணையர் டி.என். சேஷன் தலைமையில் வாக்காளர் புகைப்பட அடையாள அட்டை (EPIC) அறிமுகம்",
            "வாக்காளர் அட்டையுடன் ஆதாரை விருப்பத்தின் பேரில் இணைக்க வகை செய்த தேர்தல் சட்டங்கள் (திருத்த) சட்டம்",
            "வெளிநாடு வாழ் இந்தியர்களுக்கு (NRI) வாக்குரிமை வழங்கிய மக்கள் பிரதிநிதித்துவ (திருத்த) சட்டம்"
        ],
        "years": ["2005", "1993", "2021", "2010"],
        "correct_seq": [2, 1, 4, 3],
        "distractors": [[1, 2, 4, 3], [2, 4, 1, 3], [4, 2, 1, 3]],
        "target_key": "D",
        "exp_en": "The correct chronological progression of electoral roll reforms is:\n2. EPIC introduced: 1993\n1. Photo Electoral Rolls nationwide: 2005\n4. NRI voting rights (Section 20A): 2010 (enforced Feb 2011)\n3. Aadhaar-Electoral Roll linkage Act: December 2021\nChronological sequence: 2 -> 1 -> 4 -> 3.",
        "exp_ta": "வாக்காளர் பட்டியல் சீர்திருத்தங்களின் காலவரிசை:\n2. EPIC அறிமுகம்: 1993\n1. புகைப்பட வாக்காளர் பட்டியல்: 2005\n4. வெளிநாடு வாழ் இந்தியர் வாக்குரிமை (பிரிவு 20A): 2010\n3. ஆதார்-வாக்காளர் அட்டை இணைப்புச் சட்டம்: டிசம்பர் 2021\nகாலவரிசை: 2 -> 1 -> 4 -> 3.",
        "tip_en": "The 2021 Amendment also substituted the single qualifying date (1st January) with four qualifying dates (1st Jan, 1st Apr, 1st Jul, 1st Oct).",
        "tip_ta": "2021 திருத்தம் ஜனவரி 1 என்ற ஒரே தகுதி நாளுக்குப் பதிலாக ஆண்டில் 4 தகுதி நாட்களை அறிமுகப்படுத்தியது.",
        "fact_en": "EPIC was first introduced under Section 28 of RPA 1950 and Registration of Electors Rules 1960.",
        "fact_ta": "1950 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 28-ன் கீழ் வாக்காளர் அடையாள அட்டை அறிமுகப்படுத்தப்பட்டது.",
        "tags": ["EPIC", "Photo Electoral Rolls", "NRI Voting", "Aadhaar Linkage"]
    },
    # 13 - Target Key: A
    {
        "id": "EC_C_013",
        "intro_en": "Arrange the following milestones in the anti-defection law framework of India in chronological order:",
        "intro_ta": "இந்தியாவின் கட்சித்தாவல் தடைச் சட்டக் கட்டமைப்பின் பின்வரும் மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Constitution (91st Amendment) Act abolishing split defense and capping Council of Ministers at 15%",
            "Y.B. Chavan Committee Report on Defections ('Aaya Ram Gaya Ram')",
            "Kihoto Hollohan v. Zachillhu upholding Tenth Schedule validity subject to judicial review",
            "Constitution (52nd Amendment) Act adding Tenth Schedule to the Constitution"
        ],
        "items_ta": [
            "பிளவு பாதுகாப்பை ரத்து செய்து அமைச்சரவை அளவை 15%-ஆகக் கட்டுப்படுத்திய 91-வது திருத்தச் சட்டம்",
            "கட்சித்தாவல் குறித்த ஒய்.பி. சவான் குழு அறிக்கை ('ஆயா ராம் கயா ராம்')",
            "10-வது அட்டவணையின் சட்டப்பூர்வ தன்மையை நீதிமன்ற ஆய்வுக்கு உட்படுத்தி உறுதி செய்த கிகோட்டோ ஹோலோஹன் வழக்கு",
            "அரசியலமைப்பில் 10-வது அட்டவணையை சேர்த்த 52-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
        ],
        "years": ["2003", "1968-1969", "1992", "1985"],
        "correct_seq": [2, 4, 3, 1],
        "distractors": [[4, 2, 3, 1], [2, 3, 4, 1], [3, 2, 4, 1]],
        "target_key": "A",
        "exp_en": "The correct chronological sequence of Anti-Defection milestones is:\n2. Y.B. Chavan Committee: 1968 – 1969\n4. 52nd Constitutional Amendment Act: 1985\n3. Kihoto Hollohan judgment: February 1992\n1. 91st Constitutional Amendment Act: 2003\nChronological sequence: 2 -> 4 -> 3 -> 1.",
        "exp_ta": "கட்சித்தாவல் தடை சட்ட வரலாற்று காலவரிசை:\n2. ஒய்.பி. சவான் குழு: 1968 – 1969\n4. 52-வது அரசியலமைப்புத் திருத்தச் சட்டம்: 1985\n3. கிகோட்டோ ஹோலோஹன் தீர்ப்பு: பிப்ரவரி 1992\n1. 91-வது அரசியலமைப்புத் திருத்தச் சட்டம்: 2003\nகாலவரிசை: 2 -> 4 -> 3 -> 1.",
        "tip_en": "The 91st Amendment deleted Paragraph 3 of the Tenth Schedule which previously protected party splits of 1/3rd members.",
        "tip_ta": "91-வது திருத்தம் 1/3 பங்கு உறுப்பினர்கள் பிரிவதை பாதுகாத்த 10-வது அட்டவணையின் பத்தி 3-ஐ நீக்கியது.",
        "fact_en": "Kihoto Hollohan held that the Speaker functions as a Tribunal when deciding disqualification under the Tenth Schedule.",
        "fact_ta": "10-வது அட்டவணையின் கீழ் தகுதிநீக்கத்தை தீர்மானிக்கும் போது சபாநாயகர் ஒரு தீர்ப்பாயமாகச் செயல்படுகிறார் என கிகோட்டோ தீர்ப்பு கூறியது.",
        "tags": ["Anti-Defection", "Tenth Schedule", "52nd Amendment", "91st Amendment"]
    },
    # 14 - Target Key: B
    {
        "id": "EC_C_014",
        "intro_en": "Arrange the following developments concerning election dispute adjudication in India in chronological order:",
        "intro_ta": "இந்தியாவில் தேர்தல் தகராறுகளை விசாரிப்பது தொடர்பான பின்வரும் முன்னேற்றங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Constitution (39th Amendment) Act seeking to place elections of PM and Speaker beyond judicial scrutiny",
            "Establishment of Election Tribunals under the original Representation of the People Act, 1951",
            "Indira Nehru Gandhi v. Raj Narain striking down Article 329A(4) and establishing free elections as Basic Structure",
            "Constitution (19th Amendment) Act abolishing Election Tribunals and transferring trial to High Courts"
        ],
        "items_ta": [
            "பிரதமர் மற்றும் சபாநாயகர் தேர்தல்களை நீதிமன்ற ஆய்வுக்கு அப்பால் வைக்க முயன்ற 39-வது அரசியலமைப்புத் திருத்தச் சட்டம்",
            "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் கீழ் தேர்தல் தீர்ப்பாயங்கள் நிறுவப்படுதல்",
            "சரத்து 329A(4)-ஐ ரத்து செய்து சுதந்திரமான தேர்தல்களை அடிப்படை அமைப்பாக நிலைநாட்டிய இந்திரா காந்தி எதிர் ராஜ் நாராயணன் வழக்கு",
            "தேர்தல் தீர்ப்பாயங்களை ரத்து செய்து விசாரணையை உயர் நீதிமன்றங்களுக்கு மாற்றிய 19-வது திருத்தச் சட்டம்"
        ],
        "years": ["August 1975", "1951", "November 1975", "1966"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[2, 1, 4, 3], [4, 2, 1, 3], [1, 2, 4, 3]],
        "target_key": "B",
        "exp_en": "The chronological sequence of election dispute adjudication is:\n2. Election Tribunals under RPA: 1951\n4. 19th Constitutional Amendment Act: 1966 (vested trial in High Courts)\n1. 39th Amendment Act: August 1975 (inserted Article 329A)\n3. Indira Nehru Gandhi v. Raj Narain: November 1975\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "தேர்தல் வழக்கு விசாரணை பரிணாம காலவரிசை:\n2. தேர்தல் தீர்ப்பாயங்கள்: 1951\n4. 19-வது திருத்தச் சட்டம்: 1966 (உயர்நீதிமன்றங்களுக்கு அதிகாரம்)\n1. 39-வது திருத்தச் சட்டம்: ஆகஸ்ட் 1975\n3. இந்திரா காந்தி எதிர் ராஜ் நாராயணன் தீர்ப்பு: நவம்பர் 1975\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "Election petitions are governed by Sections 80 to 116 of RPA 1951, filed within 45 days of result declaration.",
        "tip_ta": "தேர்தல் மனுக்கள் முடிவு அறிவிக்கப்பட்ட 45 நாட்களுக்குள் உயர் நீதிமன்றத்தில் தாக்கல் செய்யப்பட வேண்டும்.",
        "fact_en": "Indira Gandhi v. Raj Narain was the first case where the Supreme Court applied the Basic Structure doctrine to strike down a constitutional amendment.",
        "fact_ta": "அரசியலமைப்புத் திருத்தத்தை ரத்து செய்ய உச்ச நீதிமன்றம் அடிப்படை கட்டமைப்பு கோட்பாட்டைப் பயன்படுத்திய முதல் வழக்கு இதுவாகும்.",
        "tags": ["Election Petitions", "19th Amendment", "Basic Structure", "Indira Gandhi Case"]
    },
    # 15 - Target Key: C
    {
        "id": "EC_C_015",
        "intro_en": "Arrange the following events concerning party splits and symbol disputes under the Election Symbols Order 1968 in chronological order:",
        "intro_ta": "1968 தேர்தல் சின்னங்கள் ஆணையின் கீழ் கட்சி பிளவுகள் மற்றும் சின்னத் தகராறுகள் தொடர்பான பின்வரும் நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Dispute and freezing of the 'Two Leaves' symbol following the split in AIADMK after M.G. Ramachandran's demise",
            "Historic split in the Indian National Congress into Congress (R) and Congress (O)",
            "Allotment of the newly recognized national symbol 'Haldhar within wheel' to the Janata Party",
            "Sadiq Ali v. Election Commission of India establishing the numerical majority test"
        ],
        "items_ta": [
            "எம்.ஜி.ஆர் மறைவுக்குப் பின் அதிமுக பிளவின் போது 'இரட்டை இலை' சின்னம் முடக்கப்படுதல்",
            "இந்திய தேசிய காங்கிரசில் காங்கிரஸ் (R) மற்றும் காங்கிரஸ் (O) என ஏற்பட்ட வரலாற்றுப் பிளவு",
            "ஜனதா கட்சிக்கு அங்கீகரிக்கப்பட்ட 'ஏர் உழவன்' தேசிய சின்னம் ஒதுக்கப்படுதல்",
            "பெரும்பான்மை சோதனையை உறுதி செய்த சாதிக் அலி எதிர் இந்திய தேர்தல் ஆணையம் வழக்கு"
        ],
        "years": ["1988-1989", "1969", "1977", "1972"],
        "correct_seq": [2, 4, 3, 1],
        "distractors": [[4, 2, 3, 1], [2, 3, 4, 1], [3, 2, 4, 1]],
        "target_key": "C",
        "exp_en": "The correct chronological sequence of party split disputes is:\n2. Congress split (Syndicate vs Indicate): 1969\n4. Sadiq Ali judgment: 1972 (upheld majority test in legislative & organizational wings)\n3. Janata Party formed and allotted symbol: 1977\n1. AIADMK split and symbol freeze: 1988 – 1989 (later reunified)\nChronological sequence: 2 -> 4 -> 3 -> 1.",
        "exp_ta": "கட்சிப் பிளவு தகராறுகளின் காலவரிசை:\n2. காங்கிரஸ் பிளவு: 1969\n4. சாதிக் அலி தீர்ப்பு: 1972\n3. ஜனதா கட்சி சின்னம் ஒதுக்கீடு: 1977\n1. அதிமுக பிளவு மற்றும் சின்ன முடக்கம்: 1988 – 1989\nகாலவரிசை: 2 -> 4 -> 3 -> 1.",
        "tip_en": "Paragraph 15 of Election Symbols Order 1968 empowers ECI to decide disputes between splinter groups of a recognized party.",
        "tip_ta": "அங்கீகரிக்கப்பட்ட கட்சியின் பிளவுபட்ட குழுக்களுக்கு இடையேயான தகராறுகளைத் தீர்க்க சின்னங்கள் ஆணையின் பத்தி 15 ECI-க்கு அதிகாரம் அளிக்கிறது.",
        "fact_en": "In 1969, Congress lost its original 'Two Bullocks with Yoke on' symbol, leading to Sadiq Ali's landmark ruling.",
        "fact_ta": "1969-ல் காங்கிரஸ் தனது அசல் 'நுகத்தடி காளைகள்' சின்னத்தை இழந்தது, இது சாதிக் அலி தீர்ப்பிற்கு வழிவகுத்தது.",
        "tags": ["Election Symbols Order", "Party Splits", "Sadiq Ali Case"]
    },
    # 16 - Target Key: D
    {
        "id": "EC_C_016",
        "intro_en": "Arrange the following Chief Election Commissioners of India in the chronological order of their tenures:",
        "intro_ta": "இந்தியாவின் பின்வரும் தலைமைத் தேர்தல் ஆணையர்களை அவர்களின் பதவிக்கால காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "T.N. Seshan",
            "S.L. Shakdhar",
            "V.S. Ramadevi (India's first and only female CEC to date)",
            "R.V.S. Peri Sastri"
        ],
        "items_ta": [
            "டி.என். சேஷன்",
            "எஸ்.எல். சக்தார்",
            "வி.எஸ். ரமாதேவி (இந்தியாவின் முதல் பெண் தலைமை தேர்தல் ஆணையர்)",
            "ஆர்.வி.எஸ். பேரி சாஸ்திரி"
        ],
        "years": ["1990-1996", "1977-1982", "Nov-Dec 1990", "1986-1990"],
        "correct_seq": [2, 4, 3, 1],
        "distractors": [[4, 2, 3, 1], [2, 3, 4, 1], [3, 2, 4, 1]],
        "target_key": "D",
        "exp_en": "The correct chronological tenure sequence is:\n2. S.L. Shakdhar: June 1977 – June 1982\n4. R.V.S. Peri Sastri: January 1986 – November 1990\n3. V.S. Ramadevi: 26 November 1990 – 11 December 1990 (first woman CEC)\n1. T.N. Seshan: 12 December 1990 – 11 December 1996\nChronological sequence: 2 -> 4 -> 3 -> 1.",
        "exp_ta": "தலைமைத் தேர்தல் ஆணையர்களின் பதவிக்கால காலவரிசை:\n2. எஸ்.எல். சக்தார்: 1977 – 1982\n4. ஆர்.வி.எஸ். பேரி சாஸ்திரி: 1986 – 1990\n3. வி.எஸ். ரமாதேவி: நவம்பர் 1990 – டிசம்பர் 1990 (முதல் பெண் CEC)\n1. டி.என். சேஷன்: டிசம்பர் 1990 – டிசம்பர் 1996\nகாலவரிசை: 2 -> 4 -> 3 -> 1.",
        "tip_en": "V.S. Ramadevi had the shortest tenure of any CEC (only 16 days).",
        "tip_ta": "வி.எஸ். ரமாதேவி மிகக் குறுகிய காலம் (16 நாட்கள் மட்டுமே) தலைமை தேர்தல் ஆணையராகப் பணியாற்றினார்.",
        "fact_en": "S.L. Shakdhar was the first to propose the concept of voter identity cards (EPIC) in the late 1970s.",
        "fact_ta": "1970-களின் பிற்பகுதியில் வாக்காளர் அடையாள அட்டை யோசனையை முதன்முதலில் முன்மொழிந்தவர் எஸ்.எல். சக்தார் ஆவார்.",
        "tags": ["Chief Election Commissioners", "Ramadevi", "Seshan", "Chronology"]
    },
    # 17 - Target Key: A
    {
        "id": "EC_C_017",
        "intro_en": "Arrange the following statutory and policy measures governing election finance in India in chronological order:",
        "intro_ta": "இந்தியாவில் தேர்தல் நிதி தொடர்பான பின்வரும் சட்டப்பூர்வ மற்றும் கொள்கை நடவடிக்கைகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Introduction of the Electoral Bond Scheme via Finance Act, 2017",
            "Insertion of Sections 29B and 29C in RPA 1951 regulating political contributions and contribution reports",
            "Supreme Court judgment striking down the Electoral Bond Scheme as unconstitutional",
            "Statutory obligation on candidates to maintain a separate bank account for election expenditure"
        ],
        "items_ta": [
            "நிதிச் சட்டம் 2017-ன் மூலம் தேர்தல் பத்திரத் திட்டம் அறிமுகப்படுத்தப்படுதல்",
            "அரசியல் பங்களிப்புகளை ஒழுங்குபடுத்த 1951 சட்டத்தில் பிரிவுகள் 29B மற்றும் 29C சேர்க்கப்படுதல்",
            "தேர்தல் பத்திரத் திட்டத்தை அரசியலமைப்பிற்கு முரணானது என உச்ச நீதிமன்றம் ரத்து செய்தல்",
            "வேட்பாளர்கள் தேர்தல் செலவினங்களுக்காக தனி வங்கிக் கணக்கை பராமரிப்பதற்கான சட்டப்பூர்வ கட்டாயம்"
        ],
        "years": ["2017-2018", "2003", "2024", "2014"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "target_key": "A",
        "exp_en": "The chronological sequence of election finance developments is:\n2. Sections 29B & 29C inserted in RPA: September 2003\n4. Mandatory separate bank account for candidates: 2014\n1. Electoral Bond Scheme introduced: January 2018 (Finance Act 2017)\n3. Electoral Bond Scheme struck down by SC: 15 February 2024\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "தேர்தல் நிதி சீர்திருத்தங்களின் காலவரிசை:\n2. பிரிவுகள் 29B மற்றும் 29C சேர்க்கப்பட்டது: 2003\n4. வேட்பாளர்களுக்கு தனி வங்கிக் கணக்கு கட்டாயம்: 2014\n1. தேர்தல் பத்திரத் திட்டம் அறிமுகம்: 2017-2018\n3. தேர்தல் பத்திரத் திட்டத்தை உச்ச நீதிமன்றம் ரத்து செய்தது: 15 பிப்ரவரி 2024\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "Under Section 29C, political parties must report all corporate/individual donations exceeding Rs. 20,000 to the ECI.",
        "tip_ta": "பிரிவு 29C-ன் கீழ் ரூ. 20,000-க்கு மேற்பட்ட அனைத்து நன்கொடைகளையும் கட்சிகள் தேர்தல் ஆணையத்திற்கு தெரிவிக்க வேண்டும்.",
        "fact_en": "A Constitution Bench of 5 judges headed by CJI D.Y. Chandrachud unanimously invalidated Electoral Bonds in ADR v. UOI (2024).",
        "fact_ta": "தலைமை நீதிபதி சந்திரசூட் தலைமையிலான 5 நீதிபதிகள் கொண்ட அமர்வு தேர்தல் பத்திரங்களை ஒருமனதாக ரத்து செய்தது.",
        "tags": ["Electoral Finance", "Electoral Bonds", "Section 29C", "Chronology"]
    },
    # 18 - Target Key: B
    {
        "id": "EC_C_018",
        "intro_en": "Arrange the following developments regarding voting age and franchise qualifications in India in chronological order:",
        "intro_ta": "இந்தியாவில் வாக்குரிமை வயது மற்றும் தகுதிகள் தொடர்பான பின்வரும் முன்னேற்றங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Introduction of four qualifying dates per year (Jan 1, Apr 1, Jul 1, Oct 1) by Election Laws (Amendment) Act",
            "Adoption of universal adult suffrage at age 21 under original Article 326 of the Constitution",
            "Constitution (61st Amendment) Act lowering the voting age from 21 to 18 years",
            "Joint Parliamentary Committee on Amendments to Election Law recommending lowering voting age to 18"
        ],
        "items_ta": [
            "தேர்தல் சட்டங்கள் திருத்தச் சட்டம் மூலம் ஆண்டில் 4 தகுதி நாட்களை அறிமுகப்படுத்துதல்",
            "அரசியலமைப்பின் அசல் சரத்து 326-ன் கீழ் 21 வயதில் வயதுவந்தோர் வாக்குரிமையை ஏற்றுக்கொண்டது",
            "வாக்களிக்கும் வயதை 21-லிருந்து 18-ஆகக் குறைத்த 61-வது அரசியலமைப்புத் திருத்தச் சட்டம்",
            "வாக்குரிமை வயதை 18-ஆகக் குறைக்க பரிந்துரைத்த பாராளுமன்றக் கூட்டுக்குழு"
        ],
        "years": ["2021", "1950", "1988", "1972"],
        "correct_seq": [2, 4, 3, 1],
        "distractors": [[2, 3, 4, 1], [4, 2, 3, 1], [3, 2, 4, 1]],
        "target_key": "B",
        "exp_en": "The chronological sequence of franchise eligibility reforms is:\n2. Original Constitution enfranchising age 21: 1950\n4. Joint Parliamentary Committee recommendation: 1972\n3. 61st Constitutional Amendment Act: December 1988 (in force March 1989)\n1. Four qualifying dates introduced: December 2021\nChronological sequence: 2 -> 4 -> 3 -> 1.",
        "exp_ta": "வாக்குரிமை தகுதி சீர்திருத்தங்களின் காலவரிசை:\n2. அரசியலமைப்பு 21 வயது வாக்குரிமை: 1950\n4. பாராளுமன்றக் கூட்டுக்குழு பரிந்துரை: 1972\n3. 61-வது திருத்தச் சட்டம்: 1988 (நடைமுறை 1989)\n1. நான்கு தகுதி நாட்கள் சட்டம்: 2021\nகாலவரிசை: 2 -> 4 -> 3 -> 1.",
        "tip_en": "Prior to 2021, a citizen turning 18 on 2nd January had to wait an entire year until the next 1st January to register.",
        "tip_ta": "2021-க்கு முன்பு, ஜனவரி 2 அன்று 18 வயதை எட்டிய ஒருவர் வாக்காளராக பதிவு செய்ய அடுத்த ஆண்டு ஜனவரி 1 வரை காத்திருக்க வேண்டியிருந்தது.",
        "fact_en": "Dr. B.R. Ambedkar called adult franchise under Article 326 the greatest act of faith by the Constitution framers.",
        "fact_ta": "வயதுவந்தோர் வாக்குரிமையை அரசியலமைப்பு நிர்ணய சபையின் 'மிகப்பெரிய நம்பிக்கைச் செயல்' என்று டாக்டர் அம்பேத்கர் குறிப்பிட்டார்.",
        "tags": ["Voting Age", "61st Amendment", "Qualifying Dates", "Article 326"]
    },
    # 19 - Target Key: C
    {
        "id": "EC_C_019",
        "intro_en": "Arrange the following landmark electoral dispute cases before the Supreme Court of India in chronological order:",
        "intro_ta": "இந்திய உச்ச நீதிமன்றத்தின் முன் வந்த பின்வரும் வரலாற்றுச் சிறப்புமிக்க தேர்தல் தகராறு வழக்குகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Kuldip Nayar v. Union of India (upholding open ballot for Rajya Sabha elections)",
            "N.P. Ponnuswami v. Returning Officer, Namakkal (bar on court interference during poll process under Article 329(b))",
            "Public Interest Foundation v. Union of India (mandating criminal antecedent publicity in media)",
            "Mohinder Singh Gill v. Chief Election Commissioner (defining scope of Article 324)"
        ],
        "items_ta": [
            "குல்தீப் நய்யார் எதிர் இந்திய ஒன்றியம் (மாநிலங்களவைக்கான திறந்த வாக்கெடுப்பை உறுதி செய்தது)",
            "என்.பி. பொன்னுசாமி எதிர் நாமக்கல் தேர்தல் அதிகாரி (சரத்து 329(b)-ன் கீழ் நீதிமன்றத் தலையீட்டிற்குத் தடை)",
            "பப்ளிக் இன்ட்ரஸ்ட் ஃபவுண்டேஷன் வழக்கு (குற்றப் பின்னணியை ஊடகங்களில் விளம்பரப்படுத்துதல் கட்டாயம்)",
            "மோஹிந்தர் சிங் கில் வழக்கு (சரத்து 324-ன் முழுமையான அதிகார வரம்பை வரையறுத்தது)"
        ],
        "years": ["2006", "1952", "2018", "1978"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "target_key": "C",
        "exp_en": "The correct chronological sequence of landmark election cases is:\n2. N.P. Ponnuswami v. Returning Officer: 1952\n4. Mohinder Singh Gill v. CEC: 1978\n1. Kuldip Nayar v. UOI: 2006\n3. Public Interest Foundation v. UOI: September 2018\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "தேர்தல் வரலாற்று வழக்குகளின் காலவரிசை:\n2. என்.பி. பொன்னுசாமி வழக்கு: 1952\n4. மோஹிந்தர் சிங் கில் வழக்கு: 1978\n1. குல்தீப் நய்யார் வழக்கு: 2006\n3. பப்ளிக் இன்ட்ரஸ்ட் ஃபவுண்டேஷன் வழக்கு: 2018\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "In Public Interest Foundation (2018), SC directed political parties to publish criminal antecedents of candidates on website, social media, and newspapers.",
        "tip_ta": "2018 தீர்ப்பில் வேட்பாளர்களின் குற்றப்பின்னணியை செய்தித்தாள்கள் மற்றும் இணையதளங்களில் விளம்பரப்படுத்த கட்சிகளுக்கு உத்தரவிடப்பட்டது.",
        "fact_en": "Ponnuswami (1952) was the very first judgment of the Supreme Court interpreting Article 329(b).",
        "fact_ta": "சரத்து 329(b)-ஐ விளக்கி உச்ச நீதிமன்றம் வழங்கிய முதல் தீர்ப்பு பொன்னுசாமி (1952) வழக்காகும்.",
        "tags": ["Ponnuswami Case", "Kuldip Nayar", "Supreme Court", "Electoral Law"]
    },
    # 20 - Target Key: D
    {
        "id": "EC_C_020",
        "intro_en": "Arrange the following historical milestones involving the Election Commission of India in international and national outreach in chronological order:",
        "intro_ta": "இந்தியத் தேர்தல் ஆணையம் சர்வதேச மற்றும் தேசிய அளவில் மேற்கொண்ட வரலாற்றுச் சிறப்புமிக்க நிகழ்வுகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Inauguration of the first annual National Voters' Day (NVD) by the President of India",
            "Conduct of the First General Elections to the Lok Sabha and State Legislative Assemblies",
            "Hosting of the 4th General Assembly of the Association of World Election Bodies (A-WEB) in Bengaluru",
            "Indian election team led by Sukumar Sen successfully organizing the general elections of Sudan"
        ],
        "items_ta": [
            "குடியரசுத் தலைவரால் முதல் வருடாந்திர தேசிய வாக்காளர் தினம் (NVD) தொடங்கி வைக்கப்படுதல்",
            "மக்களவை மற்றும் மாநில சட்டமன்றங்களுக்கான முதல் பொதுத் தேர்தல்கள் நடத்தப்படுதல்",
            "பெங்களூருவில் உலகத் தேர்தல் அமைப்புகளின் சங்கத்தின் (A-WEB) 4-வது பொதுச் சபையை நடத்துதல்",
            "சுகுமார் சென் தலைமையிலான இந்திய தேர்தல் குழு சூடான் பொதுத் தேர்தலை வெற்றிகரமாக நடத்துதல்"
        ],
        "years": ["2011", "1951-1952", "2019", "1953"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "target_key": "D",
        "exp_en": "The chronological sequence of national and international outreach milestones is:\n2. First General Elections: October 1951 – February 1952\n4. Sudan elections under Sukumar Sen: 1953\n1. First National Voters' Day: 25 January 2011\n3. 4th A-WEB General Assembly in Bengaluru: September 2019\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "தேசிய மற்றும் சர்வதேச மைல்கற்களின் காலவரிசை:\n2. முதல் பொதுத் தேர்தல்: 1951 – 1952\n4. சூடான் தேர்தல் (சுகுமார் சென்): 1953\n1. முதல் தேசிய வாக்காளர் தினம்: 25 ஜனவரி 2011\n3. பெங்களூருவில் A-WEB பொதுச் சபை: செப்டம்பர் 2019\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "Association of World Election Bodies (A-WEB) is the largest international organization of election management bodies.",
        "tip_ta": "A-WEB என்பது உலகின் மிகப்பெரிய தேர்தல் மேலாண்மை அமைப்புகளின் சர்வதேச கூட்டமைப்பாகும்.",
        "fact_en": "National Voters' Day was instituted in 2011 to mark ECI's Foundation Day (25 January 1950) and boost youth registration.",
        "fact_ta": "தேர்தல் ஆணையம் தொடங்கப்பட்ட நாளான ஜனவரி 25-ஐ நினைவுகூரவும், இளைஞர் பதிவை ஊக்குவிக்கவும் 2011 முதல் NVD தொடங்கப்பட்டது.",
        "tags": ["National Voters Day", "Sukumar Sen", "A-WEB", "ECI Outreach"]
    },
    # 21 - Target Key: A
    {
        "id": "EC_C_021",
        "intro_en": "Arrange the following legal milestones governing the disqualification of convicted legislators under Section 8 of RPA 1951 in chronological order:",
        "intro_ta": "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தின் பிரிவு 8-ன் கீழ் குற்றவாளிகளான சட்டமன்ற உறுப்பினர்களின் தகுதிநீக்கம் தொடர்பான பின்வரும் சட்ட மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "K. Prabhakaran v. P. Jayarajan (upholding temporary differential protection for sitting legislators)",
            "Original enactment of Section 8 in the Representation of the People Act, 1951",
            "Lily Thomas v. Union of India (striking down Section 8(4) protection as unconstitutional)",
            "Parliamentary amendment inserting Section 8(4) providing a 3-month appeal window for sitting legislators"
        ],
        "items_ta": [
            "கே. பிரபாகரன் எதிர் பி. ஜெயராஜன் (சட்டமன்ற உறுப்பினர்களுக்கான தற்காலிக பாதுகாப்பை உறுதி செய்தது)",
            "1951 மக்கள் பிரதிநிதித்துவச் சட்டத்தில் பிரிவு 8 அசல் வடிவில் இயற்றப்படுதல்",
            "லில்லி தாமஸ் வழக்கில் பிரிவு 8(4) பாதுகாப்பை அரசியலமைப்பிற்கு முரணானது என ரத்து செய்தல்",
            "எம்.பி/எம்.எல்.ஏ-க்களுக்கு 3 மாத மேல்முறையீட்டு அவகாசம் வழங்கிய பிரிவு 8(4) திருத்தம்"
        ],
        "years": ["2005", "1951", "2013", "1956"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "target_key": "A",
        "exp_en": "The chronological sequence of Section 8 disqualification jurisprudence is:\n2. Original enactment of Section 8: July 1951\n4. Section 8(4) inserted by Parliament: 1956\n1. K. Prabhakaran judgment: January 2005\n3. Lily Thomas judgment: 10 July 2013\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "பிரிவு 8 தகுதிநீக்க சட்ட வரலாற்றின் காலவரிசை:\n2. பிரிவு 8 அசல் சட்டம்: ஜூலை 1951\n4. பிரிவு 8(4) சேர்க்கப்பட்டது: 1956\n1. கே. பிரபாகரன் தீர்ப்பு: ஜனவரி 2005\n3. லில்லி தாமஸ் தீர்ப்பு: 10 ஜூலை 2013\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "In Lok Prahari (2018), SC clarified that stay of conviction (not mere suspension of sentence) lifts the disqualification under Section 8.",
        "tip_ta": "2018 லோக் பிரஹாரி தீர்ப்பில் தண்டனைக்கு தடை விதிக்கப்பட்டால் மட்டுமே பிரிவு 8 தகுதிநீக்கம் நீங்கும் என தெளிவுபடுத்தப்பட்டது.",
        "fact_en": "Under Section 8(3), conviction for 2 or more years results in disqualification for the prison term plus a further 6 years upon release.",
        "fact_ta": "பிரிவு 8(3)-ன் கீழ் 2 ஆண்டுகள் சிறை தண்டனை பெற்றால், தண்டனைக் காலம் முடிந்து மேலும் 6 ஆண்டுகளுக்கு தகுதிநீக்கம் நீடிக்கும்.",
        "tags": ["Section 8 RPA 1951", "Lily Thomas Case", "Disqualification"]
    },
    # 22 - Target Key: B
    {
        "id": "EC_C_022",
        "intro_en": "Arrange the following statutory amendments and judicial rulings on the Presidential and Vice-Presidential Elections Act in chronological order:",
        "intro_ta": "குடியரசுத் தலைவர் மற்றும் துணைக் குடியரசுத் தலைவர் தேர்தல் சட்டம் தொடர்பான பின்வரும் திருத்தங்கள் மற்றும் தீர்ப்புகளை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Amendment Act raising proposers and seconders to 50 each for Presidential elections and security deposit to Rs. 15,000",
            "Enactment of the Presidential and Vice-Presidential Elections Act under Article 71",
            "In re Presidential Election reference (holding that dissolution of a State Legislative Assembly does not stall Presidential election)",
            "Amendment Act requiring 10 proposers and 10 seconders to discourage non-serious candidates"
        ],
        "items_ta": [
            "குடியரசுத் தலைவர் தேர்தலுக்கு முன்மொழிவோர் மற்றும் வழிமொழிவோரை தலா 50 ஆகவும் பிணைத்தொகையை ரூ. 15,000 ஆகவும் உயர்த்திய திருத்தச் சட்டம்",
            "சரத்து 71-ன் கீழ் குடியரசுத் தலைவர் மற்றும் துணைக் குடியரசுத் தலைவர் தேர்தல் சட்டம் இயற்றப்படுதல்",
            "ஒரு மாநில சட்டமன்றம் கலைக்கப்பட்டிருந்தாலும் குடியரசுத் தலைவர் தேர்தலை நிறுத்த முடியாது என்ற உச்ச நீதிமன்ற ஆலோசனைத் தீர்ப்பு",
            "தேவையற்ற வேட்பாளர்களைத் தடுக்க முன்மொழிவோர் மற்றும் வழிமொழிவோரை தலா 10 ஆக நிர்ணயித்த திருத்தச் சட்டம்"
        ],
        "years": ["1997", "1952", "June 1974", "August 1974"],
        "correct_seq": [2, 3, 4, 1],
        "distractors": [[2, 4, 3, 1], [4, 2, 3, 1], [3, 2, 4, 1]],
        "target_key": "B",
        "exp_en": "The correct chronological sequence of Presidential election law milestones is:\n2. Presidential & Vice-Presidential Elections Act enacted: 1952\n3. In re Presidential Election reference: June 1974 (Gujarat Assembly dissolution)\n4. Amendment requiring 10 proposers/seconders: August 1974\n1. Amendment increasing to 50 proposers/seconders: 1997\nChronological sequence: 2 -> 3 -> 4 -> 1.",
        "exp_ta": "குடியரசுத் தலைவர் தேர்தல் சட்ட வரலாற்றின் காலவரிசை:\n2. குடியரசுத் தலைவர் தேர்தல் சட்டம்: 1952\n3. உச்ச நீதிமன்ற ஆலோசனை தீர்ப்பு: ஜூன் 1974\n4. 10 முன்மொழிவோர் திருத்தம்: ஆகஸ்ட் 1974\n1. 50 முன்மொழிவோர் திருத்தம்: 1997\nகாலவரிசை: 2 -> 3 -> 4 -> 1.",
        "tip_en": "Under Article 71(1), all doubts and disputes arising out of the election of President or Vice-President are decided exclusively by the Supreme Court.",
        "tip_ta": "சரத்து 71(1)-ன் கீழ் குடியரசுத் தலைவர்/துணைக் குடியரசுத் தலைவர் தேர்தல் தகராறுகளை உச்ச நீதிமன்றம் மட்டுமே விசாரிக்க முடியும்.",
        "fact_en": "Security deposit for Presidential candidates was raised from Rs. 2,500 to Rs. 15,000 in 1997.",
        "fact_ta": "குடியரசுத் தலைவர் வேட்பாளரின் பிணைத்தொகை 1997-ல் ரூ. 2,500-லிருந்து ரூ. 15,000 ஆக உயர்த்தப்பட்டது.",
        "tags": ["Presidential Elections Act", "Article 71", "Proposers and Seconders"]
    },
    # 23 - Target Key: C
    {
        "id": "EC_C_023",
        "intro_en": "Arrange the following developmental milestones of the Model Code of Conduct (MCC) in chronological order:",
        "intro_ta": "மாதிரி நடத்தை விதிமுறைகளின் (MCC) பின்வரும் வளர்ச்சி மைல்கற்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Addition of a dedicated chapter on the 'Party in Power' to prevent abuse of governmental machinery",
            "First voluntary adoption of a code of conduct in Kerala State Legislative Assembly elections",
            "Incorporation of Part VIII on election manifestos following Supreme Court directions in S. Subramaniam Balaji case",
            "First nationwide circulation of the draft Code of Conduct by ECI to recognized political parties for Lok Sabha polls"
        ],
        "items_ta": [
            "அரசு அதிகார துஷ்பிரயோகத்தைத் தடுக்க 'ஆளும் கட்சி' மீதான பிரத்யேக அத்தியாயம் சேர்க்கப்படுதல்",
            "கேரள மாநில சட்டமன்றத் தேர்தலில் முதன்முதலில் தன்னார்வமாக நடத்தை விதிகள் ஏற்றுக்கொள்ளப்படுதல்",
            "எஸ். சுப்பிரமணியம் பாலாஜி வழக்கில் உச்ச நீதிமன்ற உத்தரவைத் தொடர்ந்து தேர்தல் அறிக்கைகள் குறித்த பகுதி VIII சேர்க்கப்படுதல்",
            "மக்களவைத் தேர்தலுக்காக அனைத்து அங்கீகரிக்கப்பட்ட கட்சிகளுக்கும் ECI முதன்முறையாக மாதிரி நடத்தை விதிகளை சுற்றுக்கு விடுதல்"
        ],
        "years": ["1979", "1960", "2014", "1962"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "target_key": "C",
        "exp_en": "The correct chronological evolution of the Model Code of Conduct is:\n2. First voluntary adoption in Kerala: 1960\n4. Circulated nationally for Lok Sabha elections: 1962\n1. Chapter on 'Party in Power' added: 1979\n3. Part VIII on election manifestos incorporated: 2014 (following Balaji case 2013)\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "மாதிரி நடத்தை விதிகளின் காலவரிசை வளர்ச்சி:\n2. கேரளாவில் முதல் பயன்பாடு: 1960\n4. தேசிய அளவில் முதல் சுற்றறிக்கை: 1962\n1. 'ஆளும் கட்சி' அத்தியாயம் சேர்க்கை: 1979\n3. தேர்தல் அறிக்கை வழிகாட்டுதல்கள் (பகுதி VIII): 2014\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "MCC comes into operation immediately upon the announcement of election schedule by the ECI and remains until results are declared.",
        "tip_ta": "தேர்தல் அட்டவணையை ECI அறிவித்த உடனேயே MCC நடைமுறைக்கு வந்து முடிவுகள் அறிவிக்கப்படும் வரை நீடிக்கும்.",
        "fact_en": "In S. Subramaniam Balaji v. State of Tamil Nadu (2013), SC held that freebies promised in manifestos do not constitute a corrupt practice under Section 123, but directed ECI to frame guidelines.",
        "fact_ta": "இலவச வாக்குறுதிகள் பிரிவு 123-ன் கீழ் ஊழல் நடவடிக்கை அல்ல என்றாலும் வழிகாட்டுதல்களை உருவாக்க ECI-க்கு பாலாஜி வழக்கில் உத்தரவிடப்பட்டது.",
        "tags": ["Model Code of Conduct", "Party in Power", "Election Manifestos", "Balaji Case"]
    },
    # 24 - Target Key: D
    {
        "id": "EC_C_024",
        "intro_en": "Arrange the launch of the following citizen and voter services platforms by the Election Commission in chronological order:",
        "intro_ta": "தேர்தல் ஆணையத்தால் குடிமக்கள் மற்றும் வாக்காளர் சேவை தளங்கள் அறிமுகப்படுத்தப்பட்டதை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Launch of cVIGIL mobile application for citizens to report Model Code of Conduct violations",
            "Launch of the Election Commission of India official website for public information",
            "Rollout of Saksham App for Persons with Disabilities (PwD) to facilitate accessible voting",
            "Full implementation of Electronically Transmitted Postal Ballot System (ETPBS) for Service Voters"
        ],
        "items_ta": [
            "மாதிரி நடத்தை விதிமுறை மீறல்களை குடிமக்கள் புகாரளிக்க cVIGIL மொபைல் செயலி அறிமுகம்",
            "பொது மக்கள் தகவலுக்காக இந்திய தேர்தல் ஆணையத்தின் அதிகாரப்பூர்வ இணையதளம் தொடக்கம்",
            "மாற்றுத்திறனாளிகள் வாக்களிப்பதை எளிதாக்க 'சக்ஷம்' (Saksham) செயலி தொடக்கம்",
            "ராணுவ மற்றும் அரசுப் பணியாளர்களுக்காக மின்னணு முறையில் தபால் வாக்கு (ETPBS) முழுமையாக அமல்"
        ],
        "years": ["2018", "1998", "2022", "2016-2019"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "target_key": "D",
        "exp_en": "The chronological sequence of ECI digital governance platforms is:\n2. ECI official website launched: February 1998\n4. ETPBS introduced for service voters: October 2016 (amendment to Conduct of Elections Rules)\n1. cVIGIL mobile app launched: July 2018\n3. Saksham App rolled out for PwD voters: 2022\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "டிஜிட்டல் தளங்களின் காலவரிசை:\n2. ECI அதிகாரப்பூர்வ இணையதளம்: 1998\n4. ETPBS தபால் வாக்கு முறை: 2016\n1. cVIGIL மொபைல் செயலி: 2018\n3. சக்ஷம் (Saksham) செயலி: 2022\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "cVIGIL guarantees response and action by Flying Squads within 100 minutes of citizen reporting with geotagged photo/video.",
        "tip_ta": "cVIGIL செயலி மூலம் செய்யப்படும் புகார்களுக்கு 100 நிமிடங்களுக்குள் பறக்கும் படையினர் நடவடிக்கை எடுப்பது உறுதி செய்யப்படுகிறது.",
        "fact_en": "Service voters include members of the armed forces, paramilitary forces, and diplomats posted abroad.",
        "fact_ta": "சேவை வாக்காளர்களில் ஆயுதப்படை வீரர்கள், துணை ராணுவப் படையினர் மற்றும் வெளிநாடுகளில் உள்ள இந்திய தூதரக அதிகாரிகள் அடங்குவர்.",
        "tags": ["cVIGIL", "Saksham App", "ETPBS", "Digital ECI"]
    },
    # 25 - Target Key: A
    {
        "id": "EC_C_025",
        "intro_en": "Arrange the following Constitutional Amendments and official acts regarding constituency delimitation in chronological order:",
        "intro_ta": "தொகுதி மறுவரையறை தொடர்பான பின்வரும் அரசியலமைப்புத் திருத்தங்கள் மற்றும் அதிகாரப்பூர்வ சட்டங்களை காலவரிசைப்படி ஒழுங்குபடுத்தவும்:",
        "items_en": [
            "Constitution (87th Amendment) Act providing for internal readjustment based on the 2001 census instead of 1991 census",
            "Constitution (42nd Amendment) Act freezing Lok Sabha and Assembly seat allocations based on the 1971 census until 2000",
            "Notification of final Delimitation Order for the Union Territory of Jammu and Kashmir",
            "Constitution (84th Amendment) Act extending the freeze on total seats until the year 2026"
        ],
        "items_ta": [
            "1991 மக்கள் தொகைக்கு பதிலாக 2001 மக்கள் தொகை அடிப்படையில் உள் தொகுதி மறுசீரமைப்பை அனுமதித்த 87-வது திருத்தச் சட்டம்",
            "1971 மக்கள் தொகை அடிப்படையில் மக்களவை மற்றும் சட்டமன்ற இடங்களை 2000 ஆண்டு வரை முடக்கிய 42-வது திருத்தச் சட்டம்",
            "ஜம்மு காஷ்மீர் யூனியன் பிரதேசத்திற்கான இறுதி தொகுதி மறுவரையறை ஆணை வெளியிடப்படுதல்",
            "மொத்த இடங்களின் மீதான முடக்கத்தை 2026 வரை நீட்டித்த 84-வது அரசியலமைப்புத் திருத்தச் சட்டம்"
        ],
        "years": ["2003", "1976", "2022", "2001"],
        "correct_seq": [2, 4, 1, 3],
        "distractors": [[4, 2, 1, 3], [2, 1, 4, 3], [1, 2, 4, 3]],
        "target_key": "A",
        "exp_en": "The chronological sequence of delimitation legislative milestones is:\n2. 42nd Amendment Act: 1976 (froze seats based on 1971 census until 2000)\n4. 84th Amendment Act: 2001 (extended freeze to 2026; allowed internal redraw on 1991 census)\n1. 87th Amendment Act: 2003 (shifted internal redraw baseline to 2001 census)\n3. J&K Delimitation Commission final order: May 2022\nChronological sequence: 2 -> 4 -> 1 -> 3.",
        "exp_ta": "தொகுதி மறுவரையறை சட்ட மைல்கற்களின் காலவரிசை:\n2. 42-வது திருத்தச் சட்டம்: 1976\n4. 84-வது திருத்தச் சட்டம்: 2001\n1. 87-வது திருத்தச் சட்டம்: 2003\n3. ஜம்மு காஷ்மீர் மறுவரையறை இறுதி ஆணை: மே 2022\nகாலவரிசை: 2 -> 4 -> 1 -> 3.",
        "tip_en": "The total number of seats in Lok Sabha remains capped at 543 until the first census taken after 2026.",
        "tip_ta": "2026-க்குப் பிறகு எடுக்கப்படும் முதல் மக்கள் தொகை கணக்கெடுப்பு வரை மக்களவை இடங்களின் எண்ணிக்கை 543 ஆக முடக்கப்பட்டுள்ளது.",
        "fact_en": "The J&K Delimitation Commission headed by Justice Ranjana Prakash Desai increased assembly seats in J&K from 83 to 90.",
        "fact_ta": "நீதிபதி ரஞ்சனா பிரகாஷ் தேசாய் தலைமையிலான ஜம்மு காஷ்மீர் மறுவரையறை ஆணையம் சட்டமன்ற இடங்களை 83-லிருந்து 90 ஆக உயர்த்தியது.",
        "tags": ["Delimitation Amendments", "42nd Amendment", "84th Amendment", "87th Amendment"]
    }
]

def format_seq(seq):
    return " - ".join(str(d) for d in seq)

def build_questions():
    questions = []
    for item in RAW_CHRONOLOGY:
        qid = item["id"]
        intro_en = item["intro_en"]
        intro_ta = item["intro_ta"]

        items_en = item["items_en"]
        items_ta = item["items_ta"]

        # Build English stem with 4 numbered lines
        lines_en = [intro_en]
        for idx, text in enumerate(items_en, start=1):
            lines_en.append(f"{idx}. {text}")
        lines_en.append("Select the correct answer from the codes given below:")
        q_en = "\n".join(lines_en)

        # Build Tamil stem with 4 numbered lines
        lines_ta = [intro_ta]
        for idx, text in enumerate(items_ta, start=1):
            lines_ta.append(f"{idx}. {text}")
        lines_ta.append("கீழே கொடுக்கப்பட்டுள்ள குறியீடுகளிலிருந்து சரியான விடையைத் தேர்ந்தெடுக்கவும்:")
        q_ta = "\n".join(lines_ta)

        corr_seq = item["correct_seq"]
        distractors = item["distractors"]
        target_key = item["target_key"]

        # Construct options dictionary with target_key getting correct_seq
        keys = ["A", "B", "C", "D"]
        other_keys = [k for k in keys if k != target_key]

        opt_seqs = {}
        opt_seqs[target_key] = corr_seq
        for idx, k in enumerate(other_keys):
            opt_seqs[k] = distractors[idx]

        options = []
        for k in keys:
            seq_str = format_seq(opt_seqs[k])
            options.append({"id": k, "en": seq_str, "ta": seq_str})

        # Why not others
        whys = {}
        for k in keys:
            if k == target_key:
                whys[k] = {
                    "en": f"Correct sequence is {format_seq(corr_seq)}.",
                    "ta": f"சரியான காலவரிசை {format_seq(corr_seq)} ஆகும்."
                }
            else:
                whys[k] = {
                    "en": f"Incorrect sequence '{format_seq(opt_seqs[k])}'. The verified chronological order is {format_seq(corr_seq)}.",
                    "ta": f"தவறான காலவரிசை '{format_seq(opt_seqs[k])}'. சரியான காலவரிசை {format_seq(corr_seq)} ஆகும்."
                }

        q = make_ec_q(
            qid=qid,
            diff="Hard",
            qtype="Chronology",
            subtopic="Electoral Milestones & Evolution",
            en_stem=q_en,
            ta_stem=q_ta,
            en_a=options[0]["en"],
            ta_a=options[0]["ta"],
            en_b=options[1]["en"],
            ta_b=options[1]["ta"],
            en_c=options[2]["en"],
            ta_c=options[2]["ta"],
            en_d=options[3]["en"],
            ta_d=options[3]["ta"],
            correct_key=target_key,
            exp_en=item["exp_en"],
            exp_ta=item["exp_ta"],
            why_a_en=whys["A"]["en"],
            why_a_ta=whys["A"]["ta"],
            why_b_en=whys["B"]["en"],
            why_b_ta=whys["B"]["ta"],
            why_c_en=whys["C"]["en"],
            why_c_ta=whys["C"]["ta"],
            why_d_en=whys["D"]["en"],
            why_d_ta=whys["D"]["ta"],
            tip_en=item["tip_en"],
            tip_ta=item["tip_ta"],
            fact_en=item["fact_en"],
            fact_ta=item["fact_ta"],
            tags=item["tags"]
        )
        questions.append(q)

    # Validate against dedicated ChronologyValidator
    report = ChronologyValidator.validate_questions(questions)
    print(report.format_final_report())
    if not report.is_valid:
        print("[ERROR] Chronology validation failed:")
        for iss in report.issues:
            print(" -", iss)
        raise ValueError("Chronology validation failed!")

    # Write output
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        json.dump(questions, f, ensure_ascii=False, indent=2)
    print(f"[SUCCESS] Wrote 25 Chronology MCQs to {OUTPUT_PATH}")

if __name__ == "__main__":
    build_questions()
