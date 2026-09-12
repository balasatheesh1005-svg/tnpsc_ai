# -*- coding: utf-8 -*-
"""
Grand Test Batch 2: SCH_GT_026 to SCH_GT_050
Covers:
- Fourth Schedule (026-032)
- Fifth Schedule (033-040)
- Sixth Schedule (041-048)
- Seventh Schedule (049-050)
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from sch_mcq_helper import make_sch_q

def get_batch2():
    qs = []

    # GT026
    qs.append(make_sch_q(
        "SCH_GT_026", "Medium", "Conceptual", "Fourth Schedule",
        "When Chhattisgarh was created as a new State under the Madhya Pradesh Reorganisation Act, 2000, how many seats in the Council of States were allocated to it in the Fourth Schedule?",
        "மத்தியப் பிரதேச மறுசீரமைப்புச் சட்டம் 2000-ன் கீழ் சத்தீஸ்கர் புதிய மாநிலமாக உருவாக்கப்பட்ட போது, நான்காவது அட்டவணையில் அதற்கு எத்தனை மாநிலங்களவை இடங்கள் ஒதுக்கப்பட்டன?",
        "5 seats", "5 இடங்கள்",
        "3 seats", "3 இடங்கள்",
        "6 seats", "6 இடங்கள்",
        "11 seats", "11 இடங்கள்",
        "A",
        "Under the Madhya Pradesh Reorganisation Act, 2000 amending the Fourth Schedule, 5 seats were allocated to the newly created State of Chhattisgarh, while Madhya Pradesh retained 11 seats.",
        "நான்காவது அட்டவணையைத் திருத்திய மத்தியப் பிரதேச மறுசீரமைப்புச் சட்டம் 2000-ன் கீழ், புதிதாக உருவாக்கப்பட்ட சத்தீஸ்கர் மாநிலத்திற்கு 5 இடங்கள் ஒதுக்கப்பட்டன; மத்தியப் பிரதேசம் 11 இடங்களைத் தக்கவைத்துக் கொண்டது.",
        "Correct. Chhattisgarh has 5 seats in the Fourth Schedule.", "சரியானது. சத்தீஸ்கருக்கு நான்காவது அட்டவணையில் 5 இடங்கள் உள்ளன.",
        "Incorrect. Uttarakhand has 3 seats.", "தவறானது. உத்தரகாண்டிற்கு 3 இடங்கள் உள்ளன.",
        "Incorrect. Jharkhand has 6 seats.", "தவறானது. ஜார்க்கண்டிற்கு 6 இடங்கள் உள்ளன.",
        "Incorrect. Madhya Pradesh retained 11 seats.", "தவறானது. மத்தியப் பிரதேசம் 11 இடங்களைத் தக்கவைத்துக் கொண்டது.",
        "Madhya Pradesh bifurcation (2000): MP retained 11 seats, Chhattisgarh received 5 seats.",
        "மத்தியப் பிரதேச பிரிப்பு (2000): மத்தியப் பிரதேசம் 11 இடங்களைத் தக்கவைத்தது, சத்தீஸ்கர் 5 இடங்களைப் பெற்றது."
    ))

    # GT027
    qs.append(make_sch_q(
        "SCH_GT_027", "Medium", "Conceptual", "Fourth Schedule",
        "Following the Jammu and Kashmir Reorganisation Act, 2019, how many seats in the Fourth Schedule are allocated to the Union Territory of Jammu and Kashmir?",
        "ஜம்மு காஷ்மீர் மறுசீரமைப்புச் சட்டம் 2019-ஐத் தொடர்ந்து, நான்காவது அட்டவணையில் ஜம்மு காஷ்மீர் யூனியன் பிரதேசத்திற்கு எத்தனை இடங்கள் ஒதுக்கப்பட்டுள்ளன?",
        "4 seats", "4 இடங்கள்",
        "2 seats", "2 இடங்கள்",
        "6 seats", "6 இடங்கள்",
        "0 seats (unrepresented)", "0 இடங்கள் (பிரதிநிதித்துவம் இல்லை)",
        "A",
        "The Jammu and Kashmir Reorganisation Act, 2019 allocated 4 seats in the Rajya Sabha (Fourth Schedule) to the Union Territory of Jammu and Kashmir, which has a Legislative Assembly.",
        "ஜம்மு காஷ்மீர் மறுசீரமைப்புச் சட்டம் 2019, சட்டமன்றம் கொண்ட ஜம்மு காஷ்மீர் யூனியன் பிரதேசத்திற்கு மாநிலங்களவையில் (நான்காவது அட்டவணை) 4 இடங்களை ஒதுக்கியுள்ளது.",
        "Correct. UT of J&K has 4 seats in the Fourth Schedule.", "சரியானது. ஜம்மு காஷ்மீர் யூனியன் பிரதேசத்திற்கு நான்காவது அட்டவணையில் 4 இடங்கள் உள்ளன.",
        "Incorrect. 4 seats were retained, not reduced to 2.", "தவறானது. 4 இடங்கள் தக்கவைக்கப்பட்டன, 2 ஆகக் குறைக்கப்படவில்லை.",
        "Incorrect. J&K never had 6 Rajya Sabha seats.", "தவறானது. ஜம்மு காஷ்மீருக்கு ஒருபோதும் 6 மாநிலங்களவை இடங்கள் இருந்ததில்லை.",
        "Incorrect. As a UT with an assembly, J&K is entitled to representation.", "தவறானது. சட்டமன்றம் உள்ள UT என்ற முறையில் ஜம்மு காஷ்மீர் பிரதிநிதித்துவத்திற்கு உரிமையுடையது.",
        "UTs in Fourth Schedule: Delhi (3), Puducherry (1), Jammu and Kashmir (4). Ladakh has no Rajya Sabha seat.",
        "நான்காவது அட்டவணையில் உள்ள UTகள்: டெல்லி (3), புதுச்சேரி (1), ஜம்மு காஷ்மீர் (4). லடாக்கிற்கு மாநிலங்களவை இடம் இல்லை."
    ))

    # GT028
    qs.append(make_sch_q(
        "SCH_GT_028", "Easy", "Conceptual", "Fourth Schedule",
        "Under Article 80(4), by which electoral system do elected members of State Legislative Assemblies elect representatives to the seats allocated in the Fourth Schedule?",
        "சரத்து 80(4)-ன் படி, நான்காவது அட்டவணையில் ஒதுக்கப்பட்டுள்ள இடங்களுக்கு மாநில சட்டமன்ற உறுப்பினர்கள் எந்த தேர்தல் முறை மூலம் பிரதிநிதிகளைத் தேர்ந்தெடுக்கின்றனர்?",
        "System of proportional representation by means of the single transferable vote", "ஒற்றை மாற்று வாக்கு மூலம் விகிதாச்சாரப் பிரதிநிதித்துவ முறை",
        "First-past-the-post simple plurality system", "முதலில் வருபவரே வெற்றியாளர் என்ற எளிய பெரும்பான்மை முறை",
        "List system with party threshold", "கட்சி வரம்புடன் கூடிய பட்டியல் முறை",
        "Direct universal adult suffrage secret ballot", "நேரடி உலகளாவிய வயதுவந்தோர் வாக்குரிமை இரகசிய வாக்கெடுப்பு",
        "A",
        "Article 80(4) provides that the representatives of each State in the Council of States shall be elected by the elected members of the Legislative Assembly in accordance with the system of proportional representation by means of the single transferable vote.",
        "சரத்து 80(4) கூறுகிறது: மாநிலங்களவையில் ஒவ்வொரு மாநிலத்தின் பிரதிநிதிகளும் சட்டமன்றத்தின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்களால் ஒற்றை மாற்று வாக்கு மூலம் விகிதாச்சாரப் பிரதிநிதித்துவ முறையின்படி தேர்ந்தெடுக்கப்படுவர்.",
        "Correct. STV with proportional representation is mandated by Art 80(4).", "சரியானது. ஒற்றை மாற்று வாக்கு விகிதாச்சார முறை சரத்து 80(4)-ன் கீழ் கட்டாயமானது.",
        "Incorrect. First-past-the-post is used for Lok Sabha and Vidhan Sabha elections.", "தவறானது. எளிய பெரும்பான்மை முறை மக்களவை மற்றும் சட்டமன்றத் தேர்தல்களுக்குப் பயன்படுகிறது.",
        "Incorrect. List system is not used in Indian parliamentary elections.", "தவறானது. பட்டியல் முறை இந்தியப் பாராளுமன்றத் தேர்தல்களில் பயன்படுவதில்லை.",
        "Incorrect. Rajya Sabha elections are indirect, not direct universal adult suffrage.", "தவறானது. மாநிலங்களவைத் தேர்தல் மறைமுகத் தேர்தல் ஆகும்.",
        "Rajya Sabha Election: Open ballot system introduced in 2003 to curb cross-voting.",
        "மாநிலங்களவைத் தேர்தல்: கட்சி மாறி வாக்களிப்பதைத் தடுக்க 2003-ல் திறந்த வாக்குச் சீட்டு முறை அறிமுகப்படுத்தப்பட்டது."
    ))

    # GT029
    qs.append(make_sch_q(
        "SCH_GT_029", "Medium", "Conceptual", "Fourth Schedule",
        "Among the southern States of India, which State has the second-highest allocation of Rajya Sabha seats in the Fourth Schedule, behind Tamil Nadu (18)?",
        "தென்னிந்திய மாநிலங்களில், நான்காவது அட்டவணையில் தமிழ்நாட்டிற்கு (18) அடுத்தபடியாக இரண்டாவது அதிக எண்ணிக்கையிலான மாநிலங்களவை இடங்களைக் கொண்டுள்ள மாநிலம் எது?",
        "Karnataka (12 seats)", "கர்நாடகா (12 இடங்கள்)",
        "Andhra Pradesh (11 seats)", "ஆந்திரப் பிரதேசம் (11 இடங்கள்)",
        "Kerala (9 seats)", "கேரளா (9 இடங்கள்)",
        "Telangana (7 seats)", "தெலங்கானா (7 இடங்கள்)",
        "A",
        "In Southern India, Tamil Nadu has 18 seats, followed by Karnataka with 12 seats, Andhra Pradesh with 11 seats, Kerala with 9 seats, and Telangana with 7 seats.",
        "தென்னிந்தியாவில், தமிழ்நாட்டிற்கு 18 இடங்கள், அதைத் தொடர்ந்து கர்நாடகாவுக்கு 12 இடங்கள், ஆந்திரப் பிரதேசத்திற்கு 11 இடங்கள், கேரளாவுக்கு 9 இடங்கள், தெலங்கானாவிற்கு 7 இடங்கள் உள்ளன.",
        "Correct. Karnataka has 12 seats, the second highest in the South.", "சரியானது. கர்நாடகா 12 இடங்களைக் கொண்டு தெற்கில் இரண்டாவது இடத்தில் உள்ளது.",
        "Incorrect. Andhra Pradesh has 11 seats after the 2014 bifurcation.", "தவறானது. 2014 பிரிவினைக்குப் பிறகு ஆந்திரப் பிரதேசத்திற்கு 11 இடங்கள் உள்ளன.",
        "Incorrect. Kerala has 9 seats.", "தவறானது. கேரளாவுக்கு 9 இடங்கள் உள்ளன.",
        "Incorrect. Telangana has 7 seats.", "தவறானது. தெலங்கானாவிற்கு 7 இடங்கள் உள்ளன.",
        "South Indian Rajya Sabha tally: TN (18), KA (12), AP (11), KL (9), TG (7). Total = 57 seats.",
        "தென்னிந்திய மாநிலங்களவை எண்ணிக்கை: தமிழ்நாடு (18), கர்நாடகா (12), ஆந்திரா (11), கேரளா (9), தெலங்கானா (7). மொத்தம் = 57 இடங்கள்."
    ))

    # GT030
    qs.append(make_sch_q(
        "SCH_GT_030", "Easy", "Conceptual", "Fourth Schedule",
        "Which North-Eastern State is allocated 7 seats in the Fourth Schedule of the Constitution, while all other North-Eastern States have only 1 seat each?",
        "அனைத்து பிற வடகிழக்கு மாநிலங்களுக்கும் தலா 1 இடம் மட்டுமே உள்ள நிலையில், அரசியலமைப்பின் நான்காவது அட்டவணையில் 7 இடங்கள் ஒதுக்கப்பட்டுள்ள வடகிழக்கு மாநிலம் எது?",
        "Assam", "அசாம்",
        "Tripura", "திரிபுரா",
        "Meghalaya", "மேகாலயா",
        "Manipur", "மணிப்பூர்",
        "A",
        "Assam is allocated 7 seats in the Fourth Schedule. The other seven North-Eastern States (Arunachal Pradesh, Manipur, Meghalaya, Mizoram, Nagaland, Sikkim, and Tripura) have 1 seat each.",
        "நான்காவது அட்டவணையில் அசாமிற்கு 7 இடங்கள் ஒதுக்கப்பட்டுள்ளன. பிற ஏழு வடகிழக்கு மாநிலங்களுக்கும் (அருணாச்சல பிரதேசம், மணிப்பூர், மேகாலயா, மிசோரம், நாகாலாந்து, சிக்கிம், திரிபுரா) தலா 1 இடம் மட்டுமே உள்ளது.",
        "Correct. Assam has 7 Rajya Sabha seats.", "சரியானது. அசாமிற்கு 7 மாநிலங்களவை இடங்கள் உள்ளன.",
        "Incorrect. Tripura has 1 seat.", "தவறானது. திரிபுராவிற்கு 1 இடம் உள்ளது.",
        "Incorrect. Meghalaya has 1 seat.", "தவறானது. மேகாலயாவிற்கு 1 இடம் உள்ளது.",
        "Incorrect. Manipur has 1 seat.", "தவறானது. மணிப்பூருக்கு 1 இடம் உள்ளது.",
        "North-East Rajya Sabha tally: Assam (7) + 7 states x 1 = 14 total seats.",
        "வடகிழக்கு மாநிலங்களவை இடங்கள்: அசாம் (7) + 7 மாநிலங்கள் x 1 = மொத்தம் 14 இடங்கள்."
    ))

    # GT031
    qs.append(make_sch_q(
        "SCH_GT_031", "Hard", "Conceptual", "Fourth Schedule",
        "Which Union Territories are currently entitled to representation in the Council of States as specified in the Fourth Schedule?",
        "நான்காவது அட்டவணையில் குறிப்பிடப்பட்டுள்ளவாறு, தற்போது மாநிலங்களவையில் பிரதிநிதித்துவம் பெற உரிமையுள்ள யூனியன் பிரதேசங்கள் எவை?",
        "National Capital Territory of Delhi, Puducherry, and Jammu and Kashmir", "தில்லி தேசிய தலைநகர் பகுதி, புதுச்சேரி மற்றும் ஜம்மு காஷ்மீர்",
        "Delhi, Puducherry, and Chandigarh", "தில்லி, புதுச்சேரி மற்றும் சண்டிகர்",
        "Delhi, Lakshadweep, and Andaman and Nicobar Islands", "தில்லி, லட்சத்தீவு மற்றும் அந்தமான் நிக்கோபார் தீவுகள்",
        "Puducherry, Ladakh, and Dadra and Nagar Haveli", "புதுச்சேரி, லடாக் மற்றும் தாத்ரா & நாகர் ஹவேலி",
        "A",
        "Only Union Territories that possess Legislative Assemblies (NCT of Delhi with 3 seats, Puducherry with 1 seat, and Jammu & Kashmir with 4 seats) have representation in the Rajya Sabha under the Fourth Schedule.",
        "சட்டமன்றங்களைக் கொண்டுள்ள யூனியன் பிரதேசங்கள் மட்டுமே (தில்லி 3 இடங்கள், புதுச்சேரி 1 இடம், ஜம்மு காஷ்மீர் 4 இடங்கள்) நான்காவது அட்டவணையின் கீழ் மாநிலங்களவையில் பிரதிநிதித்துவம் பெற்றுள்ளன.",
        "Correct. Only Delhi (3), Puducherry (1), and J&K (4) have Rajya Sabha seats.", "சரியானது. தில்லி (3), புதுச்சேரி (1), ஜம்மு காஷ்மீர் (4) மட்டுமே மாநிலங்களவை இடங்களைக் கொண்டுள்ளன.",
        "Incorrect. Chandigarh has no legislative assembly and 0 Rajya Sabha seats.", "தவறானது. சண்டிகருக்கு சட்டமன்றமும் மாநிலங்களவை இடமும் இல்லை.",
        "Incorrect. Lakshadweep and Andaman & Nicobar have no Rajya Sabha seats.", "தவறானது. லட்சத்தீவு மற்றும் அந்தமானுக்கு மாநிலங்களவை இடங்கள் இல்லை.",
        "Incorrect. Ladakh has no assembly and no Rajya Sabha seat.", "தவறானது. லடாக்கிற்கு சட்டமன்றமும் மாநிலங்களவை இடமும் இல்லை.",
        "Article 80(5): Representatives of UTs in Rajya Sabha are chosen in such manner as Parliament prescribes by law.",
        "சரத்து 80(5): மாநிலங்களவையில் யூனியன் பிரதேசப் பிரதிநிதிகள் பாராளுமன்றச் சட்டத்தின்படி தேர்ந்தெடுக்கப்படுகின்றனர்."
    ))

    # GT032
    qs.append(make_sch_q(
        "SCH_GT_032", "Medium", "Conceptual", "Fourth Schedule",
        "Which Constitutional Amendment Act froze the allocation of seats to States in the Fourth Schedule based on the 1971 census until the first census taken after the year 2026?",
        "2026-ம் ஆண்டிற்குப் பிறகு எடுக்கப்படும் முதல் மக்கள் தொகை கணக்கெடுப்பு வரை 1971 மக்கள் தொகையின் அடிப்படையில் நான்காவது அட்டவணையில் மாநிலங்களுக்கான இட ஒதுக்கீட்டை முடக்கிய அரசியலமைப்புத் திருத்தச் சட்டம் எது?",
        "84th Constitutional Amendment Act, 2001", "84வது அரசியலமைப்புத் திருத்தச் சட்டம், 2001",
        "42nd Constitutional Amendment Act, 1976", "42வது அரசியலமைப்புத் திருத்தச் சட்டம், 1976",
        "87th Constitutional Amendment Act, 2003", "87வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003",
        "91st Constitutional Amendment Act, 2003", "91வது அரசியலமைப்புத் திருத்தச் சட்டம், 2003",
        "A",
        "The 84th Constitutional Amendment Act, 2001 extended the freeze on seat allocation in both Lok Sabha and Rajya Sabha (Fourth Schedule) based on the 1971 Census until the first census after 2026.",
        "84வது அரசியலமைப்புத் திருத்தச் சட்டம் 2001, 1971 மக்கள் தொகை கணக்கெடுப்பின் அடிப்படையில் மக்களவை மற்றும் மாநிலங்களவை (நான்காவது அட்டவணை) இட ஒதுக்கீட்டு முடக்கத்தை 2026-க்குப் பிந்தைய முதல் கணக்கெடுப்பு வரை நீட்டித்தது.",
        "Correct. 84th CAA 2001 extended the seat allocation freeze to post-2026.", "சரியானது. 84வது திருத்தம் 2001 இட ஒதுக்கீட்டு முடக்கத்தை 2026 வரை நீட்டித்தது.",
        "Incorrect. 42nd CAA 1976 originally froze seat allocations until 2000.", "தவறானது. 42வது திருத்தம் 1976 முதலில் 2000 வரை இடங்களை முடக்கியது.",
        "Incorrect. 87th CAA 2003 allowed delimitation based on 2001 census without changing total seats.", "தவறானது. 87வது திருத்தம் 2003 மொத்த இடங்களை மாற்றாமல் 2001 மக்கள் தொகையின்படி தொகுதி மறுசீரமைப்பை அனுமதித்தது.",
        "Incorrect. 91st CAA 2003 limited council size and anti-defection.", "தவறானது. 91வது திருத்தம் 2003 அமைச்சரவை அளவு மற்றும் கட்சித்தாவலைக் கட்டுப்படுத்தியது.",
        "Seat allocation freeze: First imposed by 42nd CAA (till 2000), extended by 84th CAA (till post-2026).",
        "இட ஒதுக்கீட்டு முடக்கம்: முதலில் 42வது திருத்தம் (2000 வரை), பின்னர் 84வது திருத்தம் மூலம் (2026 வரை) நீட்டிக்கப்பட்டது."
    ))

    # GT033
    qs.append(make_sch_q(
        "SCH_GT_033", "Easy", "Conceptual", "Fifth Schedule",
        "Under Paragraph 4(1) of the Fifth Schedule, what is the maximum number of members in a Tribes Advisory Council (TAC)?",
        "ஐந்தாவது அட்டவணையின் பத்தி 4(1)-ன் கீழ், ஒரு பழங்குடியினர் ஆலோசனைக் குழுவில் (TAC) இருக்கக்கூடிய அதிகபட்ச உறுப்பினர்களின் எண்ணிக்கை என்ன?",
        "Not more than 20 members", "20 உறுப்பினர்களுக்கு மிகாமல்",
        "Not more than 30 members", "30 உறுப்பினர்களுக்கு மிகாமல்",
        "Not more than 15 members", "15 உறுப்பினர்களுக்கு மிகாமல்",
        "Not more than 25 members", "25 உறுப்பினர்களுக்கு மிகாமல்",
        "A",
        "Paragraph 4(1) of the Fifth Schedule explicitly states that there shall be established in each State having Scheduled Areas a Tribes Advisory Council consisting of not more than twenty members.",
        "ஐந்தாவது அட்டவணையின் பத்தி 4(1) தெளிவாகக் கூறுகிறது: அட்டவணைப் பகுதிகளைக் கொண்ட ஒவ்வொரு மாநிலத்திலும் இருபது உறுப்பினர்களுக்கு மிகாமல் ஒரு பழங்குடியினர் ஆலோசனைக் குழு அமைக்கப்பட வேண்டும்.",
        "Correct. Maximum 20 members in TAC under Fifth Schedule.", "சரியானது. ஐந்தாவது அட்டவணையின் கீழ் TAC-ல் அதிகபட்சம் 20 உறுப்பினர்கள்.",
        "Incorrect. 30 members is the size of Sixth Schedule District Councils.", "தவறானது. 30 உறுப்பினர்கள் என்பது ஆறாவது அட்டவணை மாவட்டக் குழுக்களின் அளவு.",
        "Incorrect. TAC ceiling is 20, not 15.", "தவறானது. TAC உச்சவரம்பு 20 ஆகும், 15 அல்ல.",
        "Incorrect. 25 is incorrect.", "தவறானது. 25 என்பது தவறானது.",
        "Tribes Advisory Council (TAC): Maximum 20 members; 3/4th must be ST MLAs.",
        "பழங்குடியினர் ஆலோசனைக் குழு (TAC): அதிகபட்சம் 20 உறுப்பினர்கள்; 3/4 பங்கு பழங்குடி எம்.எல்.ஏ-க்களாக இருக்க வேண்டும்."
    ))

    # GT034
    qs.append(make_sch_q(
        "SCH_GT_034", "Medium", "Conceptual", "Fifth Schedule",
        "What proportion of the members of a Tribes Advisory Council in a Fifth Schedule State must be representatives of the Scheduled Tribes in the Legislative Assembly of the State?",
        "ஐந்தாவது அட்டவணை மாநிலத்தில் உள்ள பழங்குடியினர் ஆலோசனைக் குழுவின் உறுப்பினர்களில் எத்தனை பங்கு உறுப்பினர்கள் மாநில சட்டமன்றத்தின் பழங்குடிப் பிரதிநிதிகளாக இருக்க வேண்டும்?",
        "As nearly as may be, three-fourths (3/4ths)", "கிட்டத்தட்ட நான்கில் மூன்று பங்கு (3/4 பங்கு)",
        "Exactly one-half (1/2)", "சரியாக பாதியளவு (1/2)",
        "At least two-thirds (2/3rds)", "குறைந்தது மூன்றில் இரண்டு பங்கு (2/3 பங்கு)",
        "At least one-third (1/3rd)", "குறைந்தது மூன்றில் ஒரு பங்கு (1/3 பங்கு)",
        "A",
        "Paragraph 4(1) of the Fifth Schedule mandates that as nearly as may be three-fourths of the members of the Tribes Advisory Council shall be the representatives of the Scheduled Tribes in the Legislative Assembly of the State.",
        "ஐந்தாவது அட்டவணையின் பத்தி 4(1) கட்டாயமாக்குகிறது: பழங்குடியினர் ஆலோசனைக் குழுவின் உறுப்பினர்களில் கிட்டத்தட்ட நான்கில் மூன்று பங்கு உறுப்பினர்கள் மாநில சட்டமன்றத்தில் உள்ள பட்டியலிடப்பட்ட பழங்குடியினரின் பிரதிநிதிகளாக இருக்க வேண்டும்.",
        "Correct. Three-fourths (3/4) must be ST MLAs.", "சரியானது. நான்கில் மூன்று பங்கு (3/4) பழங்குடி எம்.எல்.ஏ-க்களாக இருக்க வேண்டும்.",
        "Incorrect. One-half is incorrect.", "தவறானது. பாதியளவு என்பது தவறானது.",
        "Incorrect. Two-thirds is not the prescribed constitutional fraction.", "தவறானது. மூன்றில் இரண்டு பங்கு என்பது அரசியலமைப்பு விகிதம் அல்ல.",
        "Incorrect. One-third applies to Panchayati Raj reservations, not TAC.", "தவறானது. மூன்றில் ஒரு பங்கு பஞ்சாயத்து ராஜ் இடஒதுக்கீட்டிற்குரியது.",
        "TAC Composition: Up to 20 members, ~3/4ths ST MLAs; if ST MLAs are fewer, remaining are filled from other ST members.",
        "TAC கட்டமைப்பு: 20 உறுப்பினர்கள் வரை, ~3/4 பங்கு பழங்குடி எம்.எல்.ஏ-க்கள்; குறைவான எம்.எல்.ஏ-க்கள் இருந்தால் பிற பழங்குடி உறுப்பினர்கள் நியமிக்கப்படுவர்."
    ))

    # GT035
    qs.append(make_sch_q(
        "SCH_GT_035", "Hard", "Conceptual", "Fifth Schedule",
        "Can a Tribes Advisory Council (TAC) be established in a State that has Scheduled Tribes but has NO designated Scheduled Areas?",
        "பட்டியலிடப்பட்ட பழங்குடியினர் உள்ள ஆனால் எவ்வித அட்டவணைப் பகுதிகளும் இல்லாத ஒரு மாநிலத்தில் பழங்குடியினர் ஆலோசனைக் குழுவை (TAC) அமைக்க முடியுமா?",
        "Yes, if the President of India so directs under Paragraph 4(1)", "ஆம், பத்தி 4(1)-ன் கீழ் இந்தியக் குடியரசுத் தலைவர் அவ்வாறு உத்தரவிட்டால்",
        "No, a TAC can strictly be formed only where Scheduled Areas exist", "இல்லை, அட்டவணைப் பகுதிகள் இருக்கும் இடங்களில் மட்டுமே TAC அமைக்க முடியும்",
        "Yes, but only upon a mandatory recommendation of the Union Home Ministry", "ஆம், ஆனால் மத்திய உள்துறை அமைச்சகத்தின் கட்டாயப் பரிந்துரையின் பேரில் மட்டுமே",
        "Yes, but only if approved by a two-thirds majority of the State Assembly", "ஆம், ஆனால் மாநில சட்டமன்றத்தின் மூன்றில் இரண்டு பெரும்பான்மை ஒப்புதல் அளித்தால் மட்டுமே",
        "A",
        "Paragraph 4(1) of the Fifth Schedule provides: '...and, if the President so directs, also in any State having Scheduled Tribes but not Scheduled Areas therein, a Tribes Advisory Council.' States like Tamil Nadu and West Bengal have TACs under this presidential directive.",
        "ஐந்தாவது அட்டவணையின் பத்தி 4(1) கூறுகிறது: குடியரசுத் தலைவர் அவ்வாறு உத்தரவிட்டால், அட்டவணைப் பகுதிகள் இல்லாத ஆனால் பட்டியலிடப்பட்ட பழங்குடியினர் உள்ள மாநிலத்திலும் ஆலோசனைக் குழு அமைக்கப்படலாம். தமிழ்நாடு, மேற்கு வங்காளம் போன்ற மாநிலங்கள் இதற்கு உதாரணங்களாகும்.",
        "Correct. President can direct formation of TAC in non-scheduled area states with ST populations.", "சரியானது. பழங்குடியினர் உள்ள பிற மாநிலங்களிலும் குடியரசுத் தலைவர் உத்தரவின் பேரில் TAC அமைக்கலாம்.",
        "Incorrect. Presidential directive creates an explicit exception.", "தவறானது. குடியரசுத் தலைவரின் உத்தரவு வெளிப்படையான விதிவிலக்கை வழங்குகிறது.",
        "Incorrect. Constitutional authority lies with the President.", "தவறானது. அரசியலமைப்பு அதிகாரம் குடியரசுத் தலைவரிடமே உள்ளது.",
        "Incorrect. Assembly supermajority is not required.", "தவறானது. சட்டமன்றத்தின் சிறப்புப் பெரும்பான்மை தேவையில்லை.",
        "TN Example: Tamil Nadu has no Fifth Schedule Areas, but possesses a Tribes Advisory Council under presidential direction.",
        "தமிழ்நாடு உதாரணம்: தமிழ்நாட்டில் 5வது அட்டவணைப் பகுதிகள் இல்லை, ஆனால் குடியரசுத் தலைவரின் வழிகாட்டுதலின் கீழ் பழங்குடியினர் ஆலோசனைக் குழு இயங்குகிறது."
    ))

    # GT036
    qs.append(make_sch_q(
        "SCH_GT_036", "Medium", "Conceptual", "Fifth Schedule",
        "Under Paragraph 5(2) of the Fifth Schedule, the Governor may make regulations for the peace and good government of a Scheduled Area, specifically to regulate which vital matter?",
        "ஐந்தாவது அட்டவணையின் பத்தி 5(2)-ன் கீழ், அட்டவணைப் பகுதியின் அமைதி மற்றும் நல்லாட்சிக்காக ஆளுநர் ஒழுங்குமுறைகளை உருவாக்கலாம்; இது முக்கியமாக எந்த விவகாரத்தை ஒழுங்குபடுத்துகிறது?",
        "Prohibiting or restricting the transfer of land by or among members of Scheduled Tribes", "பழங்குடியினரின் நில மாற்றத்தைத் தடை செய்தல் அல்லது கட்டுப்படுத்துதல்",
        "Imposing personal income taxes on tribal produce", "பழங்குடியினரின் விளைபொருட்கள் மீது தனிநபர் வருமான வரி விதித்தல்",
        "Setting up specialized commercial banking branches", "சிறப்பு வணிக வங்கி கிளைகளை நிறுவுதல்",
        "Authorizing private military garrisons in forest zones", "வனப்பகுதிகளில் தனியார் இராணுவ முகாம்களை அங்கீகரித்தல்",
        "A",
        "Under Paragraph 5(2), the Governor's regulations may prohibit or restrict the transfer of land by or among members of Scheduled Tribes, regulate allotment of land, and regulate the business of money-lending in Scheduled Areas.",
        "பத்தி 5(2)-ன் கீழ், ஆளுநரின் ஒழுங்குமுறைகள் பழங்குடியினரிடையே அல்லது அவர்களால் நிலம் மாற்றப்படுவதைத் தடைசெய்யலாம் அல்லது கட்டுப்படுத்தலாம்; நில ஒதுக்கீடு மற்றும் கந்துவட்டித் தொழிலை ஒழுங்குபடுத்தலாம்.",
        "Correct. Prohibiting land alienation and regulating money-lending are core Governor powers.", "சரியானது. நில மாற்றத்தைத் தடுத்தல் மற்றும் கந்துவட்டியைக் கட்டுப்படுத்துதல் ஆகியவை ஆளுநரின் முக்கிய அதிகாரங்கள்.",
        "Incorrect. Income taxes are under Union List Entry 82.", "தவறானது. வருமான வரி மத்திய பட்டியல் பதிவு 82-ன் கீழ் உள்ளது.",
        "Incorrect. Commercial banking is under Union List Entry 45.", "தவறானது. வணிக வங்கிகள் மத்திய பட்டியல் பதிவு 45-ன் கீழ் உள்ளது.",
        "Incorrect. Military garrisons are Union Defence matters.", "தவறானது. இராணுவ முகாம்கள் மத்திய பாதுகாப்புத் துறையைச் சார்ந்தவை.",
        "Paragraph 5(2): Core protection against tribal land alienation and exploitation by money-lenders.",
        "பத்தி 5(2): பழங்குடியினர் நில அபகரிப்பு மற்றும் கந்துவட்டி சுரண்டலுக்கு எதிரான முக்கிய பாதுகாப்பு."
    ))

    # GT037
    qs.append(make_sch_q(
        "SCH_GT_037", "Hard", "Conceptual", "Fifth Schedule",
        "Under Paragraph 5(4) of the Fifth Schedule, what is the mandatory constitutional condition for any regulation made by the Governor to have legal effect?",
        "ஐந்தாவது அட்டவணையின் பத்தி 5(4)-ன் கீழ், ஆளுநர் இயற்றும் எந்தவொரு ஒழுங்குமுறையும் சட்டப்பூர்வமாக செல்லுபடியாக கட்டாய அரசியலமைப்பு நிபந்தனை என்ன?",
        "It must be submitted to and assented to by the President of India", "இது சமர்ப்பிக்கப்பட்டு இந்தியக் குடியரசுத் தலைவரின் ஒப்புதலைப் பெற வேண்டும்",
        "It must be ratified by both Houses of Parliament within six months", "இது ஆறு மாதங்களுக்குள் பாராளுமன்றத்தின் இரு அவைகளாலும் அங்கீகரிக்கப்பட வேண்டும்",
        "It must be approved by a unanimous vote of the State Cabinet", "இது மாநில அமைச்சரவையின் ஏகமனதான வாக்குகளால் அங்கீகரிக்கப்பட வேண்டும்",
        "It must be vetted and cleared by the Supreme Court of India", "இது இந்திய உச்சநீதிமன்றத்தால் பரிசீலிக்கப்பட்டு அனுமதிக்கப்பட வேண்டும்",
        "A",
        "Paragraph 5(4) of the Fifth Schedule explicitly mandates: 'No regulation shall be made under this paragraph unless the Governor making the regulation has, in the case where there is a Tribes Advisory Council for the State, consulted such Council, and all regulations shall be submitted forthwith to the President and, until assented to by him, shall have no effect.'",
        "ஐந்தாவது அட்டவணையின் பத்தி 5(4) தெளிவாகக் கட்டாயமாக்குகிறது: ஆளுநர் ஒழுங்குமுறை இயற்றும் போது TAC-ஐ கலந்தாலோசிக்க வேண்டும்; மேலும் அனைத்து ஒழுங்குமுறைகளும் உடனடியாகக் குடியரசுத் தலைவருக்கு அனுப்பப்பட வேண்டும், அவரது ஒப்புதலைப் பெறும் வரை அவை நடைமுறைக்கு வராது.",
        "Correct. Presidential assent is mandatory under Paragraph 5(4).", "சரியானது. பத்தி 5(4)-ன் கீழ் குடியரசுத் தலைவரின் ஒப்புதல் கட்டாயமானது.",
        "Incorrect. Parliament does not ratify Governor regulations.", "தவறானது. பாராளுமன்றம் ஆளுநரின் ஒழுங்குமுறைகளை ஏற்பதில்லை.",
        "Incorrect. State Cabinet unanimity is not a constitutional requirement.", "தவறானது. அமைச்சரவையின் ஏகமனதான ஒப்புதல் அரசியலமைப்புத் தேவை அல்ல.",
        "Incorrect. Supreme Court does not pre-vet administrative regulations.", "தவறானது. உச்சநீதிமன்றம் முன்கூட்டியே ஒழுங்குமுறைகளை சரிபார்ப்பதில்லை.",
        "Governor's Fifth Schedule Regulations: Require TAC consultation + Presidential assent.",
        "ஆளுநரின் ஐந்தாவது அட்டவணை ஒழுங்குமுறைகள்: TAC ஆலோசனை + குடியரசுத் தலைவர் ஒப்புதல் கட்டாயம்."
    ))

    # GT038
    qs.append(make_sch_q(
        "SCH_GT_038", "Hard", "Conceptual", "Fifth Schedule",
        "Which landmark Supreme Court judgment in 1997 held that mining leases granted to non-tribals or private companies in Scheduled Areas violate the Fifth Schedule?",
        "அட்டவணைப் பகுதிகளில் பழங்குடியினர் அல்லாதவர்களுக்கோ அல்லது தனியார் நிறுவனங்களுக்கோ வழங்கப்படும் சுரங்க குத்தகைகள் ஐந்தாவது அட்டவணையை மீறுவதாகும் என 1997-ல் தீர்ப்பளித்த வரலாற்றுச் சிறப்புமிக்க உச்சநீதிமன்ற வழக்கு எது?",
        "Samatha v. State of Andhra Pradesh", "சமதா எதிர் ஆந்திரப் பிரதேச அரசு",
        "Kihoto Hollohan v. Zachillhu", "கிகோட்டோ ஹோல்லோஹன் எதிர் ஜாச்சில்கு",
        "Indra Sawhney v. Union of India", "இந்திரா சஹானி எதிர் இந்திய யூனியன்",
        "Minerva Mills v. Union of India", "மினர்வா மில்ஸ் எதிர் இந்திய யூனியன்",
        "A",
        "In the landmark Samatha judgment (1997), the Supreme Court held that the word 'person' in the Andhra Pradesh Scheduled Areas Land Transfer Regulation included the State Government itself, and hence the State cannot lease tribal land in Fifth Schedule areas to non-tribal private mining corporations.",
        "வரலாற்றுச் சிறப்புமிக்க சமதா வழக்கில் (1997), உச்சநீதிமன்றம் ஆந்திர அட்டவணைப் பகுதி நில மாற்ற ஒழுங்குமுறையில் 'நபர்' என்ற வார்த்தை மாநில அரசையும் உள்ளடக்கும் என்றும், எனவே மாநில அரசு ஐந்தாவது அட்டவணைப் பகுதிகளில் உள்ள நிலத்தைத் தனியார் நிறுவனங்களுக்கு சுரங்க குத்தகைக்கு விட முடியாது என்றும் தீர்ப்பளித்தது.",
        "Correct. Samatha v. State of AP (1997) is the landmark tribal land protection case.", "சரியானது. சமதா வழக்கு (1997) பழங்குடியினர் நிலப் பாதுகாப்பிற்கான வரலாற்றுத் தீர்ப்பு.",
        "Incorrect. Kihoto Hollohan is on Tenth Schedule anti-defection.", "தவறானது. கிகோட்டோ ஹோல்லோஹன் பத்தாவது அட்டவணை கட்சித்தாவல் பற்றியது.",
        "Incorrect. Indra Sawhney is on OBC reservations (1992).", "தவறானது. இந்திரா சஹானி ஓபிசி இடஒதுக்கீடு பற்றியது (1992).",
        "Incorrect. Minerva Mills is on Basic Structure and DPSP (1980).", "தவறானது. மினர்வா மில்ஸ் அடிப்படை கட்டமைப்பு மற்றும் DPSP பற்றியது (1980).",
        "Samatha Judgment (1997): Tribal land in Fifth Schedule cannot be leased to non-tribals or private corporations.",
        "சமதா தீர்ப்பு (1997): ஐந்தாவது அட்டவணை நிலங்களை பழங்குடி அல்லாதவர்களுக்கோ தனியாருக்கோ குத்தகைக்கு விட முடியாது."
    ))

    # GT039
    qs.append(make_sch_q(
        "SCH_GT_039", "Easy", "Conceptual", "Fifth Schedule",
        "Under Paragraph 3 of the Fifth Schedule, to whom must the Governor of each State having Scheduled Areas submit an annual report regarding their administration?",
        "ஐந்தாவது அட்டவணையின் பத்தி 3-ன் கீழ், அட்டவணைப் பகுதிகளைக் கொண்ட ஒவ்வொரு மாநிலத்தின் ஆளுநரும் அவற்றின் நிர்வாகம் குறித்த வருடாந்திர அறிக்கையை யாரிடம் சமர்ப்பிக்க வேண்டும்?",
        "To the President of India", "இந்தியக் குடியரசுத் தலைவரிடம்",
        "To the Chief Minister of the State", "மாநில முதலமைச்சரிடம்",
        "To the Speaker of the Legislative Assembly", "சட்டமன்ற சபாநாயகரிடம்",
        "To the National Commission for Scheduled Tribes", "தேசிய பழங்குடியினர் ஆணையத்திடம்",
        "A",
        "Paragraph 3 of the Fifth Schedule provides that the Governor of each State having Scheduled Areas shall annually, or whenever so required by the President, make a report to the President regarding the administration of the Scheduled Areas in that State.",
        "ஐந்தாவது அட்டவணையின் பத்தி 3 கூறுகிறது: அட்டவணைப் பகுதிகளைக் கொண்ட ஒவ்வொரு மாநில ஆளுநரும் ஆண்டுதோறும் அல்லது குடியரசுத் தலைவர் கோரும் போதெல்லாம், அந்த மாநிலத்தின் அட்டவணைப் பகுதிகளின் நிர்வாகம் குறித்த அறிக்கையைக் குடியரசுத் தலைவருக்குச் சமர்ப்பிக்க வேண்டும்.",
        "Correct. The annual report under Fifth Schedule is submitted to the President.", "சரியானது. ஐந்தாவது அட்டவணை வருடாந்திர அறிக்கை குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்படுகிறது.",
        "Incorrect. Governor reports directly to Centre/President, not Chief Minister.", "தவறானது. ஆளுநர் முதல்வரிடம் அல்லாமல் நேரடியாக குடியரசுத் தலைவரிடம் அறிக்கை அளிக்கிறார்.",
        "Incorrect. Assembly Speaker does not receive this report under Paragraph 3.", "தவறானது. பத்தி 3-ன் கீழ் சபாநாயகர் இந்த அறிக்கையைப் பெறுவதில்லை.",
        "Incorrect. NCST receives reports under Article 338A, not Fifth Schedule Para 3.", "தவறானது. NCST சரத்து 338A-ன் கீழ் அறிக்கை பெறுகிறது, பத்தி 3 அல்ல.",
        "Fifth Schedule Para 3: Direct reporting pipeline from Governor to the President of India.",
        "ஐந்தாவது அட்டவணை பத்தி 3: ஆளுநரிடமிருந்து இந்தியக் குடியரசுத் தலைவருக்கு நேரடி அறிக்கை அளிக்கும் முறை."
    ))

    # GT040
    qs.append(make_sch_q(
        "SCH_GT_040", "Medium", "Conceptual", "Fifth Schedule",
        "Under Paragraph 5(1) of the Fifth Schedule, what extraordinary legislative authority does the Governor exercise regarding Acts of Parliament or State Legislature?",
        "ஐந்தாவது அட்டவணையின் பத்தி 5(1)-ன் கீழ், பாராளுமன்ற அல்லது மாநில சட்டமன்றச் சட்டங்கள் தொடர்பாக ஆளுநர் செலுத்தும் அசாதாரண சட்டமன்ற அதிகாரம் என்ன?",
        "The Governor may direct that an Act shall not apply to a Scheduled Area or shall apply with specified exceptions and modifications", "ஒரு சட்டம் அட்டவணைப் பகுதிக்குப் பொருந்தாது என்றோ அல்லது குறிப்பிட்ட விதிவிலக்குகள் மற்றும் மாற்றங்களுடன் பொருந்தும் என்றோ ஆளுநர் உத்தரவிடலாம்",
        "The Governor can permanently veto any Act of Parliament from being enforced in the State capital", "மாநிலத் தலைநகரில் எந்தவொரு பாராளுமன்றச் சட்டமும் அமல்படுத்தப்படுவதை ஆளுநர் நிரந்தரமாக வீட்டோ செய்யலாம்",
        "The Governor can introduce independent money bills without legislative consent", "சட்டமன்ற ஒப்புதல் இல்லாமல் ஆளுநர் சுயாதீன நிதி மசோதாக்களை அறிமுகப்படுத்தலாம்",
        "The Governor can dissolve the Parliament if an Act conflicts with tribal welfare", "ஒரு சட்டம் பழங்குடியினர் நலனுக்கு முரணாக இருந்தால் ஆளுநர் பாராளுமன்றத்தைக் கலைக்க முடியும்",
        "A",
        "Paragraph 5(1) empowers the Governor to notify that any particular Act of Parliament or of the Legislature of the State shall not apply to a Scheduled Area, or shall apply subject to such exceptions and modifications as specified.",
        "பத்தி 5(1) ஆளுநருக்கு அதிகாரம் அளிக்கிறது: பாராளுமன்றம் அல்லது மாநில சட்டமன்றத்தின் எந்தவொரு குறிப்பிட்ட சட்டமும் அட்டவணைப் பகுதிக்குப் பொருந்தாது என்றோ அல்லது அவர் குறிப்பிடும் விதிவிலக்குகள் மற்றும் திருத்தங்களுடன் பொருந்தும் என்றோ அறிவிக்கலாம்.",
        "Correct. Governor has power to modify or bar application of laws in Scheduled Areas.", "சரியானது. அட்டவணைப் பகுதிகளில் சட்டங்களைப் பொருந்தாமல் செய்யவோ திருத்தவோ ஆளுநருக்கு அதிகாரம் உண்டு.",
        "Incorrect. Power applies strictly to Scheduled Areas, not State capitals.", "தவறானது. அதிகாரம் அட்டவணைப் பகுதிகளுக்கு மட்டுமே உரியது, தலைநகருக்கு அல்ல.",
        "Incorrect. Governor cannot bypass legislature on money bills.", "தவறானது. நிதி மசோதாக்களில் ஆளுநர் சட்டமன்றத்தைத் தவிர்க்க முடியாது.",
        "Incorrect. Governor has zero power to dissolve Parliament.", "தவறானது. பாராளுமன்றத்தைக் கலைக்கும் அதிகாரம் ஆளுநருக்குக் கிடையாது.",
        "Fifth Schedule Legislative Shield: Laws don't apply automatically if the Governor directs otherwise (Para 5(1)).",
        "ஐந்தாவது அட்டவணை சட்டமன்றக் கவசம்: ஆளுநர் உத்தரவிட்டால் சட்டங்கள் தானாகப் பொருந்தாது (பத்தி 5(1))."
    ))

    # GT041
    qs.append(make_sch_q(
        "SCH_GT_041", "Easy", "Conceptual", "Sixth Schedule",
        "How many Autonomous District Councils (ADCs) currently function under the Sixth Schedule of the Indian Constitution across Assam, Meghalaya, Tripura, and Mizoram?",
        "இந்திய அரசியலமைப்பின் ஆறாவது அட்டவணையின் கீழ் அசாம், மேகாலயா, திரிபுரா மற்றும் மிசோரம் ஆகிய மாநிலங்களில் தற்போது எத்தனை தன்னாட்சி மாவட்டக் குழுக்கள் (ADCs) செயல்படுகின்றன?",
        "10 Autonomous District Councils", "10 தன்னாட்சி மாவட்டக் குழுக்கள்",
        "8 Autonomous District Councils", "8 தன்னாட்சி மாவட்டக் குழுக்கள்",
        "12 Autonomous District Councils", "12 தன்னாட்சி மாவட்டக் குழுக்கள்",
        "14 Autonomous District Councils", "14 தன்னாட்சி மாவட்டக் குழுக்கள்",
        "A",
        "There are currently 10 Autonomous District Councils under the Sixth Schedule: Assam (3: Bodoland, Karbi Anglong, Dima Hasao), Meghalaya (3: Khasi, Garo, Jaintia), Mizoram (3: Chakma, Mara, Lai), and Tripura (1: Tripura Tribal Areas Autonomous District Council).",
        "ஆறாவது அட்டவணையின் கீழ் தற்போது 10 தன்னாட்சி மாவட்டக் குழுக்கள் உள்ளன: அசாம் (3: போடோலாந்து, கர்பி அங்லாங், திமா ஹசாவோ), மேகாலயா (3: காசி, காரோ, ஜெயின்டியா), மிசோரம் (3: சக்மா, மாரா, லாய்) மற்றும் திரிபுரா (1: திரிபுரா பழங்குடிப் பகுதி தன்னாட்சிக் குழு).",
        "Correct. Exactly 10 ADCs function under the Sixth Schedule across AMTM states.", "சரியானது. AMTM மாநிலங்களில் சரியாக 10 ADCs செயல்படுகின்றன.",
        "Incorrect. 8 is incorrect.", "தவறானது. 8 என்பது தவறானது.",
        "Incorrect. 12 is incorrect.", "தவறானது. 12 என்பது தவறானது.",
        "Incorrect. 14 is incorrect.", "தவறானது. 14 என்பது தவறானது.",
        "Sixth Schedule ADCs: Assam (3), Meghalaya (3), Mizoram (3), Tripura (1) = Total 10 ADCs.",
        "ஆறாவது அட்டவணை ADCs: அசாம் (3), மேகாலயா (3), மிசோரம் (3), திரிபுரா (1) = மொத்தம் 10 தன்னாட்சிக் குழுக்கள்."
    ))

    # GT042
    qs.append(make_sch_q(
        "SCH_GT_042", "Medium", "Conceptual", "Sixth Schedule",
        "Under Paragraph 2 of the Sixth Schedule, what is the total membership of an Autonomous District Council, and how many are nominated by the Governor?",
        "ஆறாவது அட்டவணையின் பத்தி 2-ன் கீழ், ஒரு தன்னாட்சி மாவட்டக் குழுவின் மொத்த உறுப்பினர்களின் எண்ணிக்கை என்ன, மற்றும் எத்தனை பேர் ஆளுநரால் நியமிக்கப்படுகிறார்கள்?",
        "30 members (26 elected by adult franchise and 4 nominated by the Governor)", "30 உறுப்பினர்கள் (26 பேர் வாக்குரிமை மூலம் தேர்ந்தெடுக்கப்பட்டவர்கள், 4 பேர் ஆளுநரால் நியமிக்கப்பட்டவர்கள்)",
        "25 members (20 elected and 5 nominated by the Governor)", "25 உறுப்பினர்கள் (20 பேர் தேர்ந்தெடுக்கப்பட்டவர்கள், 5 பேர் ஆளுநரால் நியமிக்கப்பட்டவர்கள்)",
        "20 members (15 elected and 5 nominated by the Governor)", "20 உறுப்பினர்கள் (15 பேர் தேர்ந்தெடுக்கப்பட்டவர்கள், 5 பேர் ஆளுநரால் நியமிக்கப்பட்டவர்கள்)",
        "40 members (35 elected and 5 nominated by the Governor)", "40 உறுப்பினர்கள் (35 பேர் தேர்ந்தெடுக்கப்பட்டவர்கள், 5 பேர் ஆளுநரால் நியமிக்கப்பட்டவர்கள்)",
        "A",
        "Paragraph 2 of the Sixth Schedule specifies that an Autonomous District Council shall consist of not more than 30 members, of whom not more than four persons shall be nominated by the Governor and the rest elected on the basis of adult suffrage (except Bodoland Territorial Council, which has 46 members under a special amendment).",
        "ஆறாவது அட்டவணையின் பத்தி 2 குறிப்பிடுகிறது: ஒரு தன்னாட்சி மாவட்டக் குழுவில் 30 உறுப்பினர்களுக்கு மிகாமல் இருக்க வேண்டும்; அவர்களில் 4 பேருக்கு மிகாமல் ஆளுநரால் நியமிக்கப்படுவர், மற்றவர்கள் வயதுவந்தோர் வாக்குரிமை அடிப்படையில் தேர்ந்தெடுக்கப்படுவர் (போடோலாந்துக்கு மட்டும் சிறப்பு விதியாக 46 இடங்கள் உள்ளன).",
        "Correct. Standard Sixth Schedule ADC has 30 members (26 elected + 4 nominated).", "சரியானது. நிலையான ஆறாவது அட்டவணை ADC 30 உறுப்பினர்களைக் கொண்டது (26 தேர்ந்தெடுக்கப்பட்டவர் + 4 நியமனம்).",
        "Incorrect. Total is 30, not 25.", "தவறானது. மொத்தம் 30, 25 அல்ல.",
        "Incorrect. 20 is the TAC ceiling under Fifth Schedule.", "தவறானது. 20 என்பது ஐந்தாவது அட்டவணை TAC உச்சவரம்பு.",
        "Incorrect. 40 is incorrect.", "தவறானது. 40 என்பது தவறானது.",
        "Sixth Schedule ADC Composition: 30 members (26 elected for 5-year terms, 4 nominated serving at Governor's pleasure).",
        "ஆறாவது அட்டவணை ADC கட்டமைப்பு: 30 உறுப்பினர்கள் (26 பேர் 5 ஆண்டு காலத்திற்குத் தேர்ந்தெடுக்கப்பட்டவர், 4 பேர் ஆளுநர் விருப்பம் வரை பதவி வகிக்கும் நியமன உறுப்பினர்கள்)."
    ))

    # GT043
    qs.append(make_sch_q(
        "SCH_GT_043", "Easy", "Conceptual", "Sixth Schedule",
        "What is the normal term of office of an elected member of an Autonomous District Council under the Sixth Schedule?",
        "ஆறாவது அட்டவணையின் கீழ் தன்னாட்சி மாவட்டக் குழுவின் தேர்ந்தெடுக்கப்பட்ட உறுப்பினரின் வழக்கமான பதவிக்காலம் என்ன?",
        "5 years from the date of the first meeting of the Council", "குழுவின் முதல் கூட்டம் கூடிய தேதியிலிருந்து 5 ஆண்டுகள்",
        "3 years from the date of declaration of election results", "தேர்தல் முடிவுகள் அறிவிக்கப்பட்ட தேதியிலிருந்து 3 ஆண்டுகள்",
        "6 years with one-third retiring every two years", "இரண்டு ஆண்டுகளுக்கு ஒருமுறை மூன்றில் ஒரு பங்கு ஓய்வுபெறும் வகையில் 6 ஆண்டுகள்",
        "At the pleasure of the Governor of the State", "மாநில ஆளுநரின் விருப்பம் உள்ளவரை",
        "A",
        "Under Paragraph 2(6A) of the Sixth Schedule, an elected member of a District Council holds office for a term of five years from the date appointed for the first meeting of the Council, unless dissolved earlier. Nominated members hold office at the pleasure of the Governor.",
        "ஆறாவது அட்டவணையின் பத்தி 2(6A)-ன் கீழ், தேர்ந்தெடுக்கப்பட்ட உறுப்பினர் குழுவின் முதல் கூட்டம் கூடிய தேதியிலிருந்து ஐந்து ஆண்டுகள் பதவி வகிப்பார். நியமன உறுப்பினர்கள் ஆளுநரின் விருப்பம் உள்ளவரை பதவி வகிப்பர்.",
        "Correct. 5 years from the first meeting.", "சரியானது. முதல் கூட்டத்திலிருந்து 5 ஆண்டுகள்.",
        "Incorrect. 3 years is not the standard constitutional tenure.", "தவறானது. 3 ஆண்டுகள் நிலையான காலம் அல்ல.",
        "Incorrect. 6-year rotation applies to Rajya Sabha and Legislative Councils.", "தவறானது. 6 ஆண்டு சுழற்சி முறை மாநிலங்களவை மற்றும் மேலவைக்குரியது.",
        "Incorrect. Pleasure of Governor applies only to nominated members, not elected ones.", "தவறானது. ஆளுநரின் விருப்பம் நியமன உறுப்பினர்களுக்கு மட்டுமே பொருந்தும்.",
        "Tenure: Elected ADC members = 5 years; Nominated members = Pleasure of Governor.",
        "பதவிக்காலம்: தேர்ந்தெடுக்கப்பட்ட ADC உறுப்பினர்கள் = 5 ஆண்டுகள்; நியமன உறுப்பினர்கள் = ஆளுநரின் விருப்பம் வரை."
    ))

    # GT044
    qs.append(make_sch_q(
        "SCH_GT_044", "Medium", "Conceptual", "Sixth Schedule",
        "Under Paragraph 8 of the Sixth Schedule, which taxation powers are specifically conferred upon Regional and District Councils?",
        "ஆறாவது அட்டவணையின் பத்தி 8-ன் கீழ், பிராந்திய மற்றும் மாவட்டக் குழுக்களுக்கு எந்த வரி விதிக்கும் அதிகாரங்கள் வெளிப்படையாக வழங்கப்பட்டுள்ளன?",
        "Assessing and collecting land revenue and levying taxes on professions, trades, animals, and vehicles", "நில வருவாயை மதிப்பீடு செய்து வசூலித்தல் மற்றும் தொழில்கள், வர்த்தகம், விலங்குகள் மற்றும் வாகனங்கள் மீது வரிகளை விதித்தல்",
        "Levying customs duties on international borders and maritime ports", "சர்வதேச எல்லைகள் மற்றும் கடல் துறைமுகங்களில் சுங்க வரிகளை விதித்தல்",
        "Imposing corporate income tax on multinational tech firms", "பன்னாட்டு தொழில்நுட்ப நிறுவனங்கள் மீது கார்ப்பரேட் வருமான வரி விதித்தல்",
        "Issuing sovereign municipal bonds backed by the Reserve Bank of India", "இந்திய ரிசர்வ் வங்கியின் ஆதரவுடன் இறையாண்மை நகராட்சி பத்திரங்களை வெளியிடுதல்",
        "A",
        "Paragraph 8 of the Sixth Schedule empowers Regional and District Councils to assess and collect land revenue, and levy taxes on lands and buildings, tolls on persons, and taxes on professions, trades, callings, animals, vehicles, and boats.",
        "ஆறாவது அட்டவணையின் பத்தி 8 பிராந்திய மற்றும் மாவட்டக் குழுக்களுக்கு நில வருவாயை மதிப்பீடு செய்து வசூலிக்கவும், நிலங்கள், கட்டிடங்கள், சுங்க வரிகள், தொழில்கள், வர்த்தகம், விலங்குகள், வாகனங்கள் மற்றும் படகுகள் மீது வரி விதிக்கவும் அதிகாரம் அளிக்கிறது.",
        "Correct. Land revenue and local trade/vehicle taxes are explicitly granted under Para 8.", "சரியானது. நில வருவாய் மற்றும் உள்ளூர் வர்த்தக/வாகன வரிகள் பத்தி 8-ன் கீழ் வழங்கப்பட்டுள்ளன.",
        "Incorrect. Customs duties belong exclusively to the Union List (Entry 83).", "தவறானது. சுங்க வரி மத்திய பட்டியலுக்கு மட்டுமே உரியது (பதிவு 83).",
        "Incorrect. Corporate tax belongs to the Union List (Entry 85).", "தவறானது. கார்ப்பரேட் வரி மத்திய பட்டியலுக்குரியது (பதிவு 85).",
        "Incorrect. District Councils cannot issue sovereign bonds backed by RBI.", "தவறானது. மாவட்டக் குழுக்கள் ஆர்பிஐ ஆதரவு பத்திரங்களை வெளியிட முடியாது.",
        "Fiscal Autonomy under Sixth Schedule: Independent revenue raising via Paragraph 8.",
        "ஆறாவது அட்டவணையின் நிதி தன்னாட்சி: பத்தி 8-ன் கீழ் சுயாதீன வருவாய் ஈட்டும் அதிகாரம்."
    ))

    # GT045
    qs.append(make_sch_q(
        "SCH_GT_045", "Hard", "Conceptual", "Sixth Schedule",
        "Under Paragraph 14 of the Sixth Schedule, who possesses the constitutional authority to appoint a Commission to inquire into and report on the administration of autonomous districts?",
        "ஆறாவது அட்டவணையின் பத்தி 14-ன் கீழ், தன்னாட்சி மாவட்டங்களின் நிர்வாகம் குறித்து விசாரித்து அறிக்கை அளிக்க ஒரு ஆணையத்தை நியமிக்கும் அரசியலமைப்பு அதிகாரம் யாருக்கு உள்ளது?",
        "The Governor of the State", "மாநில ஆளுநர்",
        "The Chief Justice of the Gauhati High Court", "குவஹாத்தி உயர்நீதிமன்ற தலைமை நீதிபதி",
        "The Union Tribal Affairs Minister", "மத்திய பழங்குடியினர் விவகார அமைச்சர்",
        "The Comptroller and Auditor-General of India", "இந்திய தலைமை கணக்குத் தணிக்கையாளர்",
        "A",
        "Paragraph 14(1) of the Sixth Schedule authorizes the Governor to appoint a Commission at any time to examine and report on any matter relating to the administration of autonomous districts and regions in the State.",
        "ஆறாவது அட்டவணையின் பத்தி 14(1) மாநிலத்தில் உள்ள தன்னாட்சி மாவட்டங்கள் மற்றும் பிராந்தியங்களின் நிர்வாகம் தொடர்பான எந்தவொரு விஷயத்தையும் ஆராய்ந்து அறிக்கை அளிக்க எந்த நேரத்திலும் ஒரு ஆணையத்தை நியமிக்க ஆளுநருக்கு அதிகாரம் அளிக்கிறது.",
        "Correct. The Governor appoints the Commission under Paragraph 14.", "சரியானது. பத்தி 14-ன் கீழ் ஆளுநர் இந்த ஆணையத்தை நியமிக்கிறார்.",
        "Incorrect. Gauhati High Court Chief Justice has judicial, not administrative inquiry powers here.", "தவறானது. தலைமை நீதிபதிக்கு இதில் நிர்வாக விசாரணை அதிகாரம் இல்லை.",
        "Incorrect. Union Minister does not directly appoint Sixth Schedule Commissions.", "தவறானது. மத்திய அமைச்சர் நேரடியாக ஆறாவது அட்டவணை ஆணையங்களை நியமிப்பதில்லை.",
        "Incorrect. CAG audits accounts under Paragraph 7, but does not head administrative commissions.", "தவறானது. சிஏஜி பத்தி 7-ன் கீழ் தணிக்கை செய்கிறார், நிர்வாக ஆணையத்திற்கு தலைமை வகிப்பதில்லை.",
        "Paragraph 14 Commission: Appointed by Governor; report must be laid before the State Legislature.",
        "பத்தி 14 ஆணையம்: ஆளுநரால் நியமிக்கப்படுகிறது; இதன் அறிக்கை மாநில சட்டமன்றத்தில் வைக்கப்பட வேண்டும்."
    ))

    # GT046
    qs.append(make_sch_q(
        "SCH_GT_046", "Hard", "Conceptual", "Sixth Schedule",
        "Under Paragraph 12A of the Sixth Schedule, how do Acts of Parliament apply to Autonomous Districts in the State of Meghalaya?",
        "ஆறாவது அட்டவணையின் பத்தி 12A-ன் கீழ், மேகாலயா மாநிலத்தில் உள்ள தன்னாட்சி மாவட்டங்களுக்கு பாராளுமன்றச் சட்டங்கள் எவ்வாறு பொருந்தும்?",
        "An Act of Parliament applies unless the President, by notification, directs that it shall not apply or shall apply with exceptions", "பாராளுமன்றச் சட்டம் பொருந்தாது என்றோ அல்லது விதிவிலக்குகளுடன் பொருந்தும் என்றோ குடியரசுத் தலைவர் அறிவிக்காத வரை அது தானாகப் பொருந்தும்",
        "An Act of Parliament never applies unless ratified by the Khasi District Council", "காசி மாவட்டக் குழுவால் அங்கீகரிக்கப்படாத வரை எந்தவொரு பாராளுமன்றச் சட்டமும் ஒருபோதும் பொருந்தாது",
        "The Governor must re-enact every central statute as a regional ordinance", "ஆளுநர் ஒவ்வொரு மத்திய சட்டத்தையும் பிராந்திய அவசரச் சட்டமாக மீண்டும் இயற்ற வேண்டும்",
        "The Supreme Court must approve each parliamentary law before enforcement in Meghalaya", "மேகாலயாவில் அமல்படுத்துவதற்கு முன் ஒவ்வொரு பாராளுமன்றச் சட்டத்திற்கும் உச்சநீதிமன்றம் ஒப்புதல் அளிக்க வேண்டும்",
        "A",
        "Under Paragraph 12A (inserted for Meghalaya), in respect of Acts of Parliament, the President may direct that an Act shall not apply to an autonomous district, or shall apply subject to exceptions. (In Assam under Para 12, this power is with the Governor for state laws and Governor for parliamentary laws).",
        "பத்தி 12A-ன் கீழ் (மேகாலயாவிற்காகச் சேர்க்கப்பட்டது), பாராளுமன்றச் சட்டங்களைப் பொறுத்தவரை, குடியரசுத் தலைவர் ஒரு சட்டம் தன்னாட்சி மாவட்டத்திற்குப் பொருந்தாது என்றோ அல்லது திருத்தங்களுடன் பொருந்தும் என்றோ உத்தரவிடலாம்; அவ்வாறு உத்தரவிடாத வரை பாராளுமன்றச் சட்டம் பொருந்தும்.",
        "Correct. For Meghalaya (Para 12A), the President directs non-application/modification.", "சரியானது. மேகாலயாவிற்கு (பத்தி 12A), குடியரசுத் தலைவர் பொருந்தாமை/மாற்றத்தை உத்தரவிடுகிறார்.",
        "Incorrect. District Councils cannot veto central legislation.", "தவறானது. மாவட்டக் குழுக்கள் மத்திய சட்டங்களை வீட்டோ செய்ய முடியாது.",
        "Incorrect. Re-enactment as ordinance is unconstitutional.", "தவறானது. அவசரச் சட்டமாக மீண்டும் இயற்றுவது அரசியலமைப்பிற்கு முரணானது.",
        "Incorrect. Supreme Court pre-approval is not required.", "தவறானது. உச்சநீதிமன்றத்தின் முன்-ஒப்புதல் தேவையில்லை.",
        "Paragraph 12 vs 12A: Assam central laws filter via Governor; Meghalaya central laws filter via the President.",
        "பத்தி 12 vs 12A: அசாமில் மத்திய சட்டங்களை வடிகட்டும் அதிகாரம் ஆளுநருக்கு; மேகாலயாவில் குடியரசுத் தலைவருக்கு."
    ))

    # GT047
    qs.append(make_sch_q(
        "SCH_GT_047", "Medium", "Conceptual", "Sixth Schedule",
        "Which of the following is NOT an Autonomous District Council located in the State of Mizoram under the Sixth Schedule?",
        "பின்வருவனவற்றில் எது ஆறாவது அட்டவணையின் கீழ் மிசோரம் மாநிலத்தில் அமையாத தன்னாட்சி மாவட்டக் குழுவாகும்?",
        "Karbi Anglong Autonomous Council", "கார்பி அங்லாங் தன்னாட்சிக் குழு",
        "Chakma Autonomous District Council", "சக்மா தன்னாட்சி மாவட்டக் குழு",
        "Mara Autonomous District Council", "மாரா தன்னாட்சி மாவட்டக் குழு",
        "Lai Autonomous District Council", "லாய் தன்னாட்சி மாவட்டக் குழு",
        "A",
        "Karbi Anglong Autonomous Council is located in Assam. The three Autonomous District Councils located in Mizoram are Chakma, Mara, and Lai.",
        "கார்பி அங்லாங் தன்னாட்சிக் குழு அசாம் மாநிலத்தில் அமைந்துள்ளது. மிசோரம் மாநிலத்தில் உள்ள மூன்று தன்னாட்சி மாவட்டக் குழுக்கள் சக்மா, மாரா மற்றும் லாய் ஆகும்.",
        "Correct. Karbi Anglong is in Assam, not Mizoram.", "சரியானது. கர்பி அங்லாங் அசாமில் உள்ளது, மிசோரமில் அல்ல.",
        "Incorrect. Chakma ADC is in Mizoram.", "தவறானது. சக்மா ADC மிசோரமில் உள்ளது.",
        "Incorrect. Mara ADC is in Mizoram.", "தவறானது. மாரா ADC மிசோரமில் உள்ளது.",
        "Incorrect. Lai ADC is in Mizoram.", "தவறானது. லாய் ADC மிசோரமில் உள்ளது.",
        "Mizoram ADCs: Chakma, Mara, and Lai. Assam ADCs: Bodoland, Karbi Anglong, and Dima Hasao.",
        "மிசோரம் ADCs: சக்மா, மாரா, மற்றும் லாய். அசாம் ADCs: போடோலாந்து, கர்பி அங்லாங், மற்றும் திமா ஹசாவோ."
    ))

    # GT048
    qs.append(make_sch_q(
        "SCH_GT_048", "Hard", "Conceptual", "Sixth Schedule",
        "Under Paragraph 5 of the Sixth Schedule, what jurisdictional limitation is imposed on courts constituted by an Autonomous District Council?",
        "ஆறாவது அட்டவணையின் பத்தி 5-ன் கீழ், தன்னாட்சி மாவட்டக் குழுவால் அமைக்கப்பட்ட நீதிமன்றங்களுக்கு என்ன அதிகார வரம்பு வரம்பு விதிக்கப்பட்டுள்ளது?",
        "They cannot try offenses punishable with death, transportation for life, or imprisonment for not less than 5 years", "மரண தண்டனை, ஆயுள் தண்டனை அல்லது 5 ஆண்டுகளுக்கு குறையாத சிறைத் தண்டனைக்குரிய குற்றங்களை அவை விசாரிக்க முடியாது",
        "They can only hear civil boundary disputes between village chiefs", "அவை கிராமத் தலைவர்களுக்கு இடையிலான சிவில் எல்லைத் தகராறுகளை மட்டுமே விசாரிக்க முடியும்",
        "They have no power to summon witnesses or record evidence", "சாட்சிகளை அழைக்கவோ அல்லது ஆதாரங்களைப் பதிவு செய்யவோ அவற்றுக்கு அதிகாரம் இல்லை",
        "Their decisions cannot be appealed to the High Court under any circumstances", "அவற்றின் முடிவுகளை எந்தச் சூழலிலும் உயர்நீதிமன்றத்தில் மேல்முறையீடு செய்ய முடியாது",
        "A",
        "Paragraph 5(1) specifies that the Governor may confer powers for trial of suits or cases on District Councils, but explicitly restricts them from trying offenses punishable with death, transportation for life, or imprisonment for not less than five years.",
        "பத்தி 5(1) குறிப்பிடுகிறது: வழக்குகளை விசாரிக்க ஆளுநர் மாவட்டக் குழுக்களுக்கு அதிகாரம் அளிக்கலாம்; ஆனால் மரண தண்டனை, ஆயுள் தண்டனை அல்லது 5 ஆண்டுகளுக்கு குறையாத சிறைத் தண்டனைக்குரிய குற்றங்களை விசாரிக்க அவற்றுக்கு அதிகாரம் இல்லை.",
        "Correct. Serious offenses (death, life, >= 5 years) are excluded from ADC courts.", "சரியானது. கடுமையான குற்றங்கள் (மரண தண்டனை, ஆயுள், >= 5 ஆண்டுகள்) ADC நீதிமன்றங்களிலிருந்து விலக்கப்பட்டுள்ளன.",
        "Incorrect. ADC courts hear both civil and petty criminal matters.", "தவறானது. ADC நீதிமன்றங்கள் சிவில் மற்றும் சிறிய குற்றவியல் வழக்குகளை விசாரிக்கின்றன.",
        "Incorrect. They have statutory summons and evidentiary powers.", "தவறானது. அவை சட்டப்பூர்வ சாட்சி அழைப்பாணை அதிகாரத்தைக் கொண்டுள்ளன.",
        "Incorrect. High Court has appellate jurisdiction under Paragraph 4(3).", "தவறானது. பத்தி 4(3)-ன் கீழ் உயர்நீதிமன்றத்திற்கு மேல்முறையீட்டு வரம்பு உண்டு.",
        "Sixth Schedule Judiciary: Village & Council Courts handle customary disputes, but grave criminal offenses remain with regular judiciary.",
        "ஆறாவது அட்டவணை நீதித்துறை: கிராம & கவுன்சில் நீதிமன்றங்கள் பாரம்பரிய வழக்குகளை விசாரிக்கின்றன, ஆனால் கடுமையான குற்றங்கள் வழக்கமான நீதித்துறையிடமே உள்ளன."
    ))

    # GT049
    qs.append(make_sch_q(
        "SCH_GT_049", "Hard", "Conceptual", "Seventh Schedule",
        "Under Entry 9 of List I (Union List) in the Seventh Schedule, Parliament has exclusive power over preventive detention for reasons connected with which specific matters?",
        "ஏழாவது அட்டவணையில் உள்ள பட்டியல் I-ன் (மத்திய பட்டியல்) பதிவு 9-ன் கீழ், எந்த குறிப்பிட்ட விஷயங்கள் தொடர்பான தடுப்புக் காவல் குறித்து பாராளுமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகாரம் உள்ளது?",
        "Defence, Foreign Affairs, or the Security of India", "பாதுகாப்பு, வெளியுறவு அல்லது இந்தியாவின் பாதுகாப்பு",
        "Maintenance of public order and local police administration", "பொது ஒழுங்கு மற்றும் உள்ளூர் காவல் நிர்வாகத்தைப் பராமரித்தல்",
        "Prevention of food adulteration and illicit distillation", "உணவுக் கலப்படம் மற்றும் கள்ளச்சாராயக் காய்ச்சலைத் தடுத்தல்",
        "Maintenance of supplies of essential commodities during agricultural droughts", "விவசாய வறட்சியின் போது அத்தியாவசியப் பொருட்களின் விநியோகத்தைப் பராமரித்தல்",
        "A",
        "Entry 9 of List I covers: 'Preventive detention for reasons connected with Defence, Foreign Affairs, or the security of India; persons subjected to such detention.'",
        "பட்டியல் I-ன் பதிவு 9 குறிப்பிடுகிறது: 'பாதுகாப்பு, வெளியுறவு அல்லது இந்தியாவின் பாதுகாப்பு தொடர்பான காரணங்களுக்காக தடுப்புக் காவல்; அத்தகைய காவலுக்கு உட்படுத்தப்பட்ட நபர்கள்.'",
        "Correct. Entry 9 of Union List covers preventive detention for Defence, Foreign Affairs, or Security of India.", "சரியானது. மத்திய பட்டியல் பதிவு 9 பாதுகாப்பு, வெளியுறவு அல்லது இந்தியப் பாதுகாப்புக்கான தடுப்புக் காவலைக் குறிக்கிறது.",
        "Incorrect. Public order is Entry 1 of State List.", "தவறானது. பொது ஒழுங்கு என்பது மாநில பட்டியல் பதிவு 1.",
        "Incorrect. Adulteration is Entry 18 of Concurrent List.", "தவறானது. கலப்படம் என்பது பொதுப் பட்டியல் பதிவு 18.",
        "Incorrect. Essential supplies detention is Entry 3 of Concurrent List.", "தவறானது. அத்தியாவசிய பொருட்கள் பராமரிப்பு தடுப்புக் காவல் பொதுப் பட்டியல் பதிவு 3.",
        "Preventive Detention Division: List I Entry 9 (Defence/Foreign/Security of India) vs List III Entry 3 (Security of a State/Public Order/Essential Supplies).",
        "தடுப்புக் காவல் பிரிவு: பட்டியல் I பதிவு 9 (பாதுகாப்பு/வெளியுறவு/இந்தியப் பாதுகாப்பு) vs பட்டியல் III பதிவு 3 (மாநில பாதுகாப்பு/பொது ஒழுங்கு/அத்தியாவசியப் பொருட்கள்)."
    ))

    # GT050
    qs.append(make_sch_q(
        "SCH_GT_050", "Hard", "Conceptual", "Seventh Schedule",
        "Under Entry 3 of List III (Concurrent List) in the Seventh Schedule, both Parliament and State Legislatures can legislate on preventive detention connected with which grounds?",
        "ஏழாவது அட்டவணையில் உள்ள பட்டியல் III-ன் (பொதுப் பட்டியல்) பதிவு 3-ன் கீழ், எந்தக் காரணங்கள் தொடர்பான தடுப்புக் காவல் மீது பாராளுமன்றம் மற்றும் மாநில சட்டமன்றங்கள் இரண்டும் சட்டம் இயற்ற முடியும்?",
        "The security of a State, the maintenance of public order, or the maintenance of supplies and services essential to the community", "ஒரு மாநிலத்தின் பாதுகாப்பு, பொது ஒழுங்கைப் பராமரித்தல் அல்லது சமூகத்திற்கு அத்தியாவசியமான பொருட்கள் மற்றும் சேவைகளின் விநியோகத்தைப் பராமரித்தல்",
        "Foreign espionage and treaties with international organizations", "வெளிநாட்டு உளவு பார்த்தல் மற்றும் சர்வதேச அமைப்புகளுடனான ஒப்பந்தங்கள்",
        "Regulation of atomic energy and nuclear waste disposal", "அணுசக்தி ஒழுங்குமுறை மற்றும் அணுக்கழிவு அகற்றுதல்",
        "Maritime shipping and navigation in tidal waters", "கடல்வழி கப்பல் போக்குவரத்து மற்றும் அலைநீரில் கப்பல் செலுத்துதல்",
        "A",
        "Entry 3 of List III specifies: 'Preventive detention for reasons connected with the security of a State, the maintenance of public order, or the maintenance of supplies and services essential to the community; persons subjected to such detention.'",
        "பட்டியல் III-ன் பதிவு 3 குறிப்பிடுகிறது: 'ஒரு மாநிலத்தின் பாதுகாப்பு, பொது ஒழுங்கைப் பராமரித்தல் அல்லது சமூகத்திற்கு அத்தியாவசியமான பொருட்கள் மற்றும் சேவைகளைப் பராமரித்தல் தொடர்பான காரணங்களுக்கான தடுப்புக் காவல்.'",
        "Correct. Entry 3 of List III covers State security, public order, and essential supplies.", "சரியானது. பொதுப் பட்டியல் பதிவு 3 மாநில பாதுகாப்பு, பொது ஒழுங்கு மற்றும் அத்தியாவசியப் பொருட்களை உள்ளடக்கியது.",
        "Incorrect. Foreign treaties belong to List I Entry 14.", "தவறானது. வெளிநாட்டு ஒப்பந்தங்கள் பட்டியல் I பதிவு 14-க்குரியது.",
        "Incorrect. Atomic energy belongs to List I Entry 6.", "தவறானது. அணுசக்தி பட்டியல் I பதிவு 6-க்குரியது.",
        "Incorrect. Maritime shipping belongs to List I Entry 25.", "தவறானது. கடல்வழி கப்பல் போக்குவரத்து பட்டியல் I பதிவு 25-க்குரியது.",
        "Entry 3 List III: Enables laws like NSA, COFEPOSA, and State Goondas Acts.",
        "பட்டியல் III பதிவு 3: NSA, COFEPOSA மற்றும் மாநில குண்டாஸ் சட்டங்கள் போன்றவற்றை இயற்ற வழிவகை செய்கிறது."
    ))

    return qs

if __name__ == "__main__":
    qs = get_batch2()
    print(f"Batch 2 generated {len(qs)} questions.")
