# -*- coding: utf-8 -*-
"""
Grand Test Batch 1: SCH_GT_001 to SCH_GT_025
Covers:
- First Schedule (001-008)
- Second Schedule (009-016)
- Third Schedule (017-024)
- Fourth Schedule (025)
"""
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.insert(0, os.path.dirname(__file__))

from sch_mcq_helper import make_sch_q

def get_batch1():
    qs = []

    # GT001
    qs.append(make_sch_q(
        "SCH_GT_001", "Easy", "Conceptual", "First Schedule",
        "Which Schedule of the Indian Constitution would need to be modified if the name of an existing State is changed by Parliament?",
        "ஒரு இருக்கும் மாநிலத்தின் பெயரைப் பாராளுமன்றம் மாற்றினால் இந்திய அரசியலமைப்பின் எந்த அட்டவணையைத் திருத்த வேண்டும்?",
        "First Schedule", "முதல் அட்டவணை",
        "Third Schedule", "மூன்றாவது அட்டவணை",
        "Fifth Schedule", "ஐந்தாவது அட்டவணை",
        "Seventh Schedule", "ஏழாவது அட்டவணை",
        "A",
        "The First Schedule contains the names and territorial extent of all States and Union Territories. Changing the name of a State under Article 3 requires altering the First Schedule.",
        "முதல் அட்டவணை அனைத்து மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களின் பெயர்களைக் கொண்டுள்ளது. சரத்து 3-ன் கீழ் ஒரு மாநிலத்தின் பெயரை மாற்றினால் முதல் அட்டவணை திருத்தப்பட வேண்டும்.",
        "Correct. First Schedule lists the names of States.", "சரியானது. முதல் அட்டவணை மாநிலங்களின் பெயர்களைப் பட்டியலிடுகிறது.",
        "Incorrect. Third Schedule deals with oaths.", "தவறானது. மூன்றாவது அட்டவணை பிரமாணங்களைக் கையாள்கிறது.",
        "Incorrect. Fifth Schedule is Scheduled Areas.", "தவறானது. ஐந்தாவது அட்டவணை அட்டவணைப் பகுதிகள் பற்றியது.",
        "Incorrect. Seventh Schedule is legislative lists.", "தவறானது. ஏழாவது அட்டவணை சட்டப் பட்டியல்கள்.",
        "First Schedule: Lists names and territories of 28 States and 8 UTs.",
        "முதல் அட்டவணை: 28 மாநிலங்கள் மற்றும் 8 UTகளின் பெயர்களைப் பட்டியலிடுகிறது."
    ))

    # GT002
    qs.append(make_sch_q(
        "SCH_GT_002", "Medium", "Conceptual", "First Schedule",
        "Under Article 1(2) of the Constitution, where are the States and the territories thereof specified?",
        "அரசியலமைப்பின் சரத்து 1(2)-ன் படி, மாநிலங்களும் அவற்றின் ஆட்சிப் பகுதிகளும் எங்கு குறிப்பிடப்பட்டுள்ளன?",
        "In the First Schedule", "முதல் அட்டவணையில்",
        "In the Second Schedule", "இரண்டாவது அட்டவணையில்",
        "In Part III of the Constitution", "அரசியலமைப்பின் பகுதி III-ல்",
        "In the Preamble", "முகப்புரையில்",
        "A",
        "Article 1(2) of the Constitution explicitly states: 'The States and the territories thereof shall be as specified in the First Schedule.'",
        "அரசியலமைப்பின் சரத்து 1(2) தெளிவாகக் கூறுகிறது: 'மாநிலங்களும் அவற்றின் ஆட்சிப் பகுதிகளும் முதல் அட்டவணையில் குறிப்பிடப்பட்டுள்ளவாறு இருக்கும்.'",
        "Correct. Article 1(2) refers directly to the First Schedule.", "சரியானது. சரத்து 1(2) நேரடியாக முதல் அட்டவணையைக் குறிப்பிடுகிறது.",
        "Incorrect. Second Schedule specifies salaries.", "தவறானது. இரண்டாவது அட்டவணை சம்பளங்களைக் குறிப்பிடுகிறது.",
        "Incorrect. Part III is Fundamental Rights.", "தவறானது. பகுதி III அடிப்படை உரிமைகள் பற்றியது.",
        "Incorrect. Preamble does not list states.", "தவறானது. முகப்புரை மாநிலங்களைப் பட்டியலிடுவதில்லை.",
        "Article 1(2) links Indian statehood directly to the First Schedule.",
        "சரத்து 1(2) இந்திய மாநில அமைப்பை நேரடியாக முதல் அட்டவணையுடன் இணைக்கிறது."
    ))

    # GT003
    qs.append(make_sch_q(
        "SCH_GT_003", "Medium", "Conceptual", "First Schedule",
        "Which constitutional amendment integrated the Portuguese territory of Goa, Daman and Diu into the First Schedule as a Union Territory in 1962?",
        "1962-ல் போர்த்துகீசிய பகுதியான கோவா, டாமன் மற்றும் டையூவை முதல் அட்டவணையில் யூனியன் பிரதேசமாக இணைத்த அரசியலமைப்புத் திருத்தம் எது?",
        "12th Constitutional Amendment Act, 1962", "12வது அரசியலமைப்புத் திருத்தச் சட்டம், 1962",
        "10th Constitutional Amendment Act, 1961", "10வது அரசியலமைப்புத் திருத்தச் சட்டம், 1961",
        "14th Constitutional Amendment Act, 1962", "14வது அரசியலமைப்புத் திருத்தச் சட்டம், 1962",
        "7th Constitutional Amendment Act, 1956", "7வது அரசியலமைப்புத் திருத்தச் சட்டம், 1956",
        "A",
        "The 12th Constitutional Amendment Act, 1962 amended the First Schedule to include Goa, Daman and Diu as the eighth Union Territory of India following Operation Vijay.",
        "விஜய் நடவடிக்கையைத் தொடர்ந்து, 12வது அரசியலமைப்புத் திருத்தச் சட்டம் 1962, கோவா, டாமன் மற்றும் டையூவை இந்தியாவின் எட்டாவது யூனியன் பிரதேசமாக முதல் அட்டவணையில் சேர்த்தது.",
        "Correct. 12th CAA 1962 incorporated Goa, Daman & Diu.", "சரியானது. 12வது திருத்தம் 1962 கோவா, டாமன் & டையூவை இணைத்தது.",
        "Incorrect. 10th CAA 1961 incorporated Dadra & Nagar Haveli.", "தவறானது. 10வது திருத்தம் தாத்ரா & நாகர் ஹவேலியை இணைத்தது.",
        "Incorrect. 14th CAA 1962 incorporated Puducherry.", "தவறானது. 14வது திருத்தம் புதுச்சேரியை இணைத்தது.",
        "Incorrect. 7th CAA 1956 was States Reorganisation.", "தவறானது. 7வது திருத்தம் மாநிலங்கள் மறுசீரமைப்பு பற்றியது.",
        "Territory incorporations: 10th (DNH), 12th (Goa/Daman/Diu), 14th (Puducherry).",
        "பகுதிகள் இணைப்பு: 10வது (DNH), 12வது (கோவா/டாமன்/டையூ), 14வது (புதுச்சேரி)."
    ))

    # GT004
    qs.append(make_sch_q(
        "SCH_GT_004", "Hard", "Conceptual", "First Schedule",
        "Which of the following constitutional provisions declares that laws enacted under Article 2 or Article 3 that amend the First Schedule are NOT deemed amendments under Article 368?",
        "முதல் அட்டவணையைத் திருத்தும் சரத்து 2 அல்லது 3-ன் கீழான சட்டங்கள் சரத்து 368-ன் கீழான அரசியலமைப்புத் திருத்தமாகக் கருதப்படாது என அறிவிக்கும் அரசியலமைப்பு சரத்து எது?",
        "Article 4(2)", "சரத்து 4(2)",
        "Article 2(1)", "சரத்து 2(1)",
        "Article 3(a)", "சரத்து 3(a)",
        "Article 368(1)", "சரத்து 368(1)",
        "A",
        "Article 4(2) explicitly provides that no law referred to in Article 2 or Article 3 shall be deemed to be an amendment of this Constitution for the purposes of Article 368.",
        "சரத்து 4(2) தெளிவாகக் கூறுகிறது: சரத்து 2 அல்லது சரத்து 3-ல் குறிப்பிடப்பட்டுள்ள எந்தவொரு சட்டமும் சரத்து 368-ன் நோக்கங்களுக்காக இந்த அரசியலமைப்பின் திருத்தமாகக் கருதப்படாது.",
        "Correct. Article 4(2) exempts Art 2/3 laws from Article 368 procedure.", "சரியானது. சரத்து 4(2) சரத்து 2/3 சட்டங்களை சரத்து 368 நடைமுறையிலிருந்து விலக்குகிறது.",
        "Incorrect. Article 2 deals with admission of new states.", "தவறானது. சரத்து 2 புதிய மாநிலங்களைச் சேர்த்தல் பற்றியது.",
        "Incorrect. Article 3 deals with formation of new states.", "தவறானது. சரத்து 3 புதிய மாநிலங்களை உருவாக்குதல் பற்றியது.",
        "Incorrect. Article 368(1) is constituent power of Parliament.", "தவறானது. சரத்து 368(1) பாராளுமன்றத்தின் அரசியலமைப்புத் திருத்தும் அதிகாரம் பற்றியது.",
        "Article 4(2): Reorganizing states and altering First Schedule requires only a simple majority.",
        "சரத்து 4(2): மாநிலங்களை மறுசீரமைக்கவும் முதல் அட்டவணையைத் திருத்தவும் எளிய பெரும்பான்மை போதுமானது."
    ))

    # GT005
    qs.append(make_sch_q(
        "SCH_GT_005", "Medium", "Conceptual", "First Schedule",
        "Which French establishment was incorporated into the First Schedule as a Union Territory by the 14th Constitutional Amendment Act, 1962?",
        "14வது அரசியலமைப்புத் திருத்தச் சட்டம் 1962 மூலம் முதல் அட்டவணையில் யூனியன் பிரதேசமாக இணைக்கப்பட்ட பிரெஞ்சு பகுதி எது?",
        "Puducherry (Pondicherry)", "புதுச்சேரி",
        "Goa", "கோவா",
        "Dadra and Nagar Haveli", "தாத்ரா மற்றும் நாகர் ஹவேலி",
        "Chandigarh", "சண்டிகர்",
        "A",
        "The 14th Constitutional Amendment Act, 1962 incorporated the former French territories of Pondicherry, Karikal, Mahe, and Yanam into the First Schedule as the Union Territory of Pondicherry.",
        "14வது அரசியலமைப்புத் திருத்தச் சட்டம் 1962, பாண்டிச்சேரி, காரைக்கால், மாஹே மற்றும் ஏனாம் ஆகிய முன்னாள் பிரெஞ்சு பகுதிகளை பாண்டிச்சேரி யூனியன் பிரதேசமாக முதல் அட்டவணையில் இணைத்தது.",
        "Correct. Puducherry was added via 14th CAA 1962.", "சரியானது. புதுச்சேரி 14வது திருத்தம் 1962 மூலம் சேர்க்கப்பட்டது.",
        "Incorrect. Goa was added via 12th CAA.", "தவறானது. கோவா 12வது திருத்தம் மூலம் சேர்க்கப்பட்டது.",
        "Incorrect. Dadra and Nagar Haveli was 10th CAA.", "தவறானது. தாத்ரா மற்றும் நாகர் ஹவேலி 10வது திருத்தம்.",
        "Incorrect. Chandigarh was created in 1966.", "தவறானது. சண்டிகர் 1966-ல் உருவாக்கப்பட்டது.",
        "Puducherry: Ceded by France in 1954; de jure transfer and 14th CAA in 1962.",
        "புதுச்சேரி: 1954-ல் பிரான்சால் ஒப்படைக்கப்பட்டு, 1962-ல் 14வது திருத்தம் மூலம் இணைக்கப்பட்டது."
    ))

    # GT006
    qs.append(make_sch_q(
        "SCH_GT_006", "Hard", "Conceptual", "First Schedule",
        "When Andhra State was created on linguistic lines in 1953, carving out territory from Madras State, which city was established as its initial capital?",
        "1953-ல் மெட்ராஸ் மாநிலத்திலிருந்து பிரிக்கப்பட்டு மொழி வாரியாக ஆந்திர மாநிலம் உருவாக்கப்பட்ட போது, அதன் தொடக்கத் தலைநகரமாக எந்த நகரம் அமைக்கப்பட்டது?",
        "Kurnool", "கர்நூல்",
        "Hyderabad", "ஹைதராபாத்",
        "Amaravati", "அமராவதி",
        "Visakhapatnam", "விசாகப்பட்டினம்",
        "A",
        "When Andhra State was carved out of Madras State under the Andhra State Act, 1953, Kurnool was made its capital. Later in 1956, when Andhra Pradesh was formed by merging Telangana, Hyderabad became the capital.",
        "1953-ல் ஆந்திர மாநிலச் சட்டத்தின் கீழ் ஆந்திரா உருவாக்கப்பட்ட போது கர்நூல் அதன் தலைநகரமானது. பின்னர் 1956-ல் தெலங்கானா இணைக்கப்பட்டு ஆந்திரப் பிரதேசம் உருவான போது ஹைதராபாத் தலைநகரமானது.",
        "Correct. Kurnool was the original capital of Andhra State in 1953.", "சரியானது. 1953-ல் ஆந்திர மாநிலத்தின் தொடக்கத் தலைநகரம் கர்நூல் ஆகும்.",
        "Incorrect. Hyderabad became capital in 1956.", "தவறானது. ஹைதராபாத் 1956-ல் தலைநகரமானது.",
        "Incorrect. Amaravati was designated post-2014.", "தவறானது. அமராவதி 2014-க்குப் பின் அறிவிக்கப்பட்டது.",
        "Incorrect. Visakhapatnam was never the sole historical capital in 1953.", "தவறானது. விசாகப்பட்டினம் 1953-ல் தலைநகரமாக இருக்கவில்லை.",
        "Andhra State 1953: First linguistic state; capital was Kurnool; High Court was at Guntur.",
        "ஆந்திர மாநிலம் 1953: முதல் மொழிவாரி மாநிலம்; தலைநகரம் கர்நூல்; உயர்நீதிமன்றம் குண்டூர்."
    ))

    # GT007
    qs.append(make_sch_q(
        "SCH_GT_007", "Medium", "Conceptual", "First Schedule",
        "By which Act was Uttaranchal renamed as Uttarakhand in the First Schedule in 2006?",
        "எந்தச் சட்டத்தின் மூலம் 2006-ல் முதல் அட்டவணையில் உத்தராஞ்சல் என்பது உத்தரகாண்ட் எனப் பெயர் மாற்றம் செய்யப்பட்டது?",
        "Uttaranchal (Alteration of Name) Act, 2006", "உத்தராஞ்சல் (பெயர் மாற்ற) சட்டம், 2006",
        "States Reorganisation Act, 2006", "மாநிலங்கள் மறுசீரமைப்புச் சட்டம், 2006",
        "Constitution 94th Amendment Act, 2006", "அரசியலமைப்பு 94வது திருத்தச் சட்டம், 2006",
        "Delimitation Act, 2006", "தொகுதி மறுசீரமைப்புச் சட்டம், 2006",
        "A",
        "Parliament enacted the Uttaranchal (Alteration of Name) Act, 2006 to substitute the name 'Uttarakhand' for 'Uttaranchal' in the First Schedule, effective January 1, 2007.",
        "பாராளுமன்றம் உத்தராஞ்சல் (பெயர் மாற்ற) சட்டம் 2006-ஐ இயற்றி, முதல் அட்டவணையில் 'உத்தராஞ்சல்' என்பதற்குப் பதிலாக 'உத்தரகாண்ட்' என மாற்றியது (2007 ஜனவரி 1 முதல் அமல்).",
        "Correct. Enacted by Uttaranchal (Alteration of Name) Act, 2006.", "சரியானது. உத்தராஞ்சல் (பெயர் மாற்ற) சட்டம் 2006 மூலம் மாற்றப்பட்டது.",
        "Incorrect. No States Reorganisation Act was enacted in 2006.", "தவறானது. 2006-ல் மாநிலங்கள் மறுசீரமைப்புச் சட்டம் இயற்றப்படவில்லை.",
        "Incorrect. 94th CAA 2006 freed Bihar from having a mandatory Tribal Welfare Minister.", "தவறானது. 94வது திருத்தம் பீகாரில் பழங்குடி அமைச்சர் கட்டாயத்தை நீக்கியது.",
        "Incorrect. Delimitation Act does not rename states.", "தவறானது. தொகுதி மறுசீரமைப்பு சட்டம் பெயர்களை மாற்றுவதில்லை.",
        "Name alterations amending First Schedule: Madras -> Tamil Nadu (1969), Mysore -> Karnataka (1973), Uttaranchal -> Uttarakhand (2006), Orissa -> Odisha (2011).",
        "முதல் அட்டவணை பெயர் மாற்றங்கள்: மெட்ராஸ் -> தமிழ்நாடு (1969), மைசூர் -> கர்நாடகா (1973), உத்தராஞ்சல் -> உத்தரகாண்ட் (2006), ஒரிசா -> ஒடியா (2011)."
    ))

    # GT008
    qs.append(make_sch_q(
        "SCH_GT_008", "Medium", "Conceptual", "First Schedule",
        "When the Madras State was officially renamed as 'Tamil Nadu' in the First Schedule, who was the Chief Minister of Tamil Nadu?",
        "முதல் அட்டவணையில் மெட்ராஸ் மாநிலம் அதிகாரப்பூர்வமாக 'தமிழ்நாடு' எனப் பெயர் மாற்றம் செய்யப்பட்ட போது, தமிழ்நாட்டின் முதலமைச்சராக இருந்தவர் யார்?",
        "C.N. Annadurai", "பேரறிஞர் சி.என். அண்ணாதுரை",
        "K. Kamaraj", "பெருந்தலைவர் கே. காமராஜர்",
        "M. Karunanidhi", "மு. கருணாநிதி",
        "M.G. Ramachandran", "எம்.ஜி. ராமச்சந்திரன்",
        "A",
        "Under Chief Minister C.N. Annadurai, the Madras Legislative Assembly unanimously passed a resolution in July 1967 to rename Madras State as Tamil Nadu. Parliament then enacted the Madras State (Alteration of Name) Act, 1968, amending the First Schedule with effect from January 14, 1969.",
        "முதலமைச்சர் சி.என். அண்ணாதுரை தலைமையில் தமிழக சட்டமன்றம் 1967 ஜூலையில் மெட்ராஸ் மாநிலத்தை தமிழ்நாடு என பெயர் மாற்ற ஒருமனதாக தீர்மானம் நிறைவேற்றியது. பின்னர் பாராளுமன்றம் மெட்ராஸ் மாநில (பெயர் மாற்ற) சட்டம் 1968-ஐ இயற்றி, 1969 ஜனவரி 14 முதல் முதல் அட்டவணையைத் திருத்தியது.",
        "Correct. C.N. Annadurai was Chief Minister during the historic renaming.", "சரியானது. வரலாற்றுச் சிறப்புமிக்க பெயர் மாற்றத்தின் போது சி.என். அண்ணாதுரை முதலமைச்சராக இருந்தார்.",
        "Incorrect. Kamaraj was CM earlier (1954-1963).", "தவறானது. காமராஜர் முன்னதாக முதலமைச்சராக இருந்தார் (1954-1963).",
        "Incorrect. Karunanidhi became CM in February 1969 after Annadurai's demise.", "தவறானது. அண்ணாதுரை மறைவுக்குப் பின் பிப்ரவரி 1969-ல் கருணாநிதி முதலமைச்சரானார்.",
        "Incorrect. MGR became CM in 1977.", "தவறானது. எம்.ஜி.ஆர் 1977-ல் முதலமைச்சரானார்.",
        "Madras -> Tamil Nadu: Renaming took effect on January 14, 1969 (Pongal Day).",
        "மெட்ராஸ் -> தமிழ்நாடு: பெயர் மாற்றம் 1969 ஜனவரி 14 (பொங்கல் திருநாள்) அன்று அமலுக்கு வந்தது."
    ))

    # GT009
    qs.append(make_sch_q(
        "SCH_GT_009", "Hard", "Conceptual", "Second Schedule",
        "In the Second Schedule of the Indian Constitution, Part B originally contained provisions regarding which functionaries, which was subsequently omitted by the 7th Constitutional Amendment Act, 1956?",
        "இந்திய அரசியலமைப்பின் இரண்டாவது அட்டவணையில், பகுதி B முதலில் எந்தப் பொறுப்பாளர்களைப் பற்றிய விதிகளைக் கொண்டிருந்தது, இது பின்னர் 1956-ன் 7வது அரசியலமைப்புத் திருத்தச் சட்டத்தால் நீக்கப்பட்டது?",
        "Ministers of Part B States and Rajpramukhs", "பகுதி B மாநிலங்களின் அமைச்சர்கள் மற்றும் ராஜ்பிரமுகர்கள்",
        "High Court Judges of Part C States", "பகுதி C மாநிலங்களின் உயர்நீதிமன்ற நீதிபதிகள்",
        "Advocate Generals of States", "மாநிலங்களின் அட்வகேட் ஜெனரல்கள்",
        "Secretariat staff of the Parliament", "பாராளுமன்றத்தின் செயலக ஊழியர்கள்",
        "A",
        "Part B of the Second Schedule originally provided for the salaries and allowances of Ministers and Rajpramukhs of Part B States. With the abolition of the fourfold classification of states by the 7th CAA, 1956, Part B was omitted.",
        "இரண்டாவது அட்டவணையின் பகுதி B முதலில் பகுதி B மாநிலங்களின் அமைச்சர்கள் மற்றும் ராஜ்பிரமுகர்களின் சம்பளம் மற்றும் படிகளை வழங்கியது. 7வது திருத்தம் 1956 மூலம் மாநிலங்களின் நான்கு வகை வகைப்பாடு ஒழிக்கப்பட்டதால், பகுதி B நீக்கப்பட்டது.",
        "Correct. Part B dealt with Part B state heads and was deleted by the 7th Amendment.", "சரியானது. பகுதி B பகுதி B மாநிலத் தலைவர்களைக் கையாண்டது மற்றும் 7வது திருத்தத்தால் நீக்கப்பட்டது.",
        "Incorrect. High Court Judges are in Part D.", "தவறானது. உயர்நீதிமன்ற நீதிபதிகள் பகுதி D-ல் உள்ளனர்.",
        "Incorrect. Advocate Generals are not in the Second Schedule.", "தவறானது. அட்வகேட் ஜெனரல்கள் இரண்டாவது அட்டவணையில் இல்லை.",
        "Incorrect. Secretariat staff salaries are under Articles 98 and 187.", "தவறானது. செயலக ஊழியர்களின் சம்பளம் சரத்து 98 மற்றும் 187-ன் கீழ் உள்ளது.",
        "Second Schedule originally had Parts A, B, C, D, E. Part B was deleted in 1956.",
        "இரண்டாவது அட்டவணை முதலில் A, B, C, D, E பகுதிகளைக் கொண்டிருந்தது. பகுதி B 1956-ல் நீக்கப்பட்டது."
    ))

    # GT010
    qs.append(make_sch_q(
        "SCH_GT_010", "Medium", "Conceptual", "Second Schedule",
        "Under Part E of the Second Schedule, the salary and rights in respect of leave of absence and pension are specified for which constitutional authority?",
        "இரண்டாவது அட்டவணையின் பகுதி E-ன் கீழ், எந்த அரசியலமைப்பு அதிகாரியின் சம்பளம், விடுப்பு மற்றும் ஓய்வூதியம் தொடர்பான உரிமைகள் குறிப்பிடப்பட்டுள்ளன?",
        "Comptroller and Auditor-General of India", "இந்திய தலைமை கணக்குத் தணிக்கையாளர் (CAG)",
        "Attorney-General for India", "இந்திய தலைமை வழக்கறிஞர் (Attorney-General)",
        "Chief Election Commissioner", "தலைமை தேர்தல் ஆணையர்",
        "Chairman of Union Public Service Commission", "மத்திய அரசுப் பணியாளர் தேர்வாணையத்தின் தலைவர்",
        "A",
        "Part E of the Second Schedule specifically deals with provisions as to the Comptroller and Auditor-General of India under Article 148(3). The Attorney-General's remuneration is determined by the President under Article 76(6) and is not in the Second Schedule.",
        "இரண்டாவது அட்டவணையின் பகுதி E சரத்து 148(3)-ன் கீழ் இந்திய தலைமை கணக்குத் தணிக்கையாளருக்கான விதிகளைக் குறிப்பிடுகிறது. தலைமை வழக்கறிஞரின் ஊதியம் குடியரசுத் தலைவரால் சரத்து 76(6)-ன் கீழ் நிர்ணயிக்கப்படுகிறது.",
        "Correct. Part E specifies salaries and pensions of the CAG.", "சரியானது. பகுதி E சிஏஜியின் சம்பளம் மற்றும் ஓய்வூதியங்களைக் குறிப்பிடுகிறது.",
        "Incorrect. Attorney-General salary is determined by President under Article 76(6).", "தவறானது. தலைமை வழக்கறிஞர் சம்பளம் சரத்து 76(6)-ன் கீழ் குடியரசுத் தலைவரால் தீர்மானிக்கப்படுகிறது.",
        "Incorrect. CEC salary is determined by Parliament via Election Commission Act.", "தவறானது. தலைமை தேர்தல் ஆணையர் சம்பளம் தேர்தல் ஆணையச் சட்டத்தின் மூலம் தீர்மானிக்கப்படுகிறது.",
        "Incorrect. UPSC Chairman conditions are under Article 318.", "தவறானது. UPSC தலைவர் நிபந்தனைகள் சரத்து 318-ன் கீழ் உள்ளன.",
        "Part E of Second Schedule: Exclusively dedicated to the Comptroller and Auditor-General of India.",
        "இரண்டாவது அட்டவணையின் பகுதி E: இந்திய தலைமை கணக்குத் தணிக்கையாளருக்கு மட்டுமே பிரத்யேகமானது."
    ))

    # GT011
    qs.append(make_sch_q(
        "SCH_GT_011", "Hard", "Conceptual", "Second Schedule",
        "According to Part D of the Second Schedule, how are the salaries and allowances of Supreme Court Judges determined if not specified by parliamentary legislation?",
        "இரண்டாவது அட்டவணையின் பகுதி D-ன் படி, பாராளுமன்றச் சட்டத்தால் குறிப்பிடப்படாத வரை, உச்சநீதிமன்ற நீதிபதிகளின் சம்பளம் மற்றும் படிகள் எவ்வாறு தீர்மானிக்கப்படுகின்றன?",
        "They receive the amounts explicitly specified in the Second Schedule", "அவர்கள் இரண்டாவது அட்டவணையில் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ள தொகைகளைப் பெறுகிறார்கள்",
        "They are fixed at the discretion of the President of India", "அவை இந்தியக் குடியரசுத் தலைவரின் விருப்பப்படி நிர்ணயிக்கப்படுகின்றன",
        "They are decided annually by the Union Finance Ministry", "அவை மத்திய நிதி அமைச்சகத்தால் ஆண்டுதோறும் தீர்மானிக்கப்படுகின்றன",
        "They are determined by a collegium of senior-most judges", "அவை மூத்த நீதிபதிகள் கொண்ட கொலீஜியத்தால் தீர்மானிக்கப்படுகின்றன",
        "A",
        "Article 125(1) states that Judges of the Supreme Court receive salaries determined by Parliament by law, and until so determined, as specified in the Second Schedule.",
        "சரத்து 125(1) கூறுகிறது: உச்சநீதிமன்ற நீதிபதிகள் பாராளுமன்றச் சட்டத்தால் தீர்மானிக்கப்படும் சம்பளங்களைப் பெறுவார்கள், அவ்வாறு தீர்மானிக்கப்படாத வரை இரண்டாவது அட்டவணையில் குறிப்பிடப்பட்டுள்ள தொகையைப் பெறுவார்கள்.",
        "Correct. Second Schedule serves as the constitutional default until Parliament legislates.", "சரியானது. பாராளுமன்றம் சட்டம் இயற்றும் வரை இரண்டாவது அட்டவணை இயல்புநிலைத் தொகையாக அமைகிறது.",
        "Incorrect. President has no discretion to determine judicial salaries arbitrarily.", "தவறானது. நீதிபதிகளின் சம்பளத்தை தன்னிச்சையாக நிர்ணயிக்க குடியரசுத் தலைவருக்கு அதிகாரம் இல்லை.",
        "Incorrect. Finance Ministry cannot alter judicial salaries.", "தவறானது. நிதி அமைச்சகம் நீதித்துறை சம்பளங்களை மாற்ற முடியாது.",
        "Incorrect. The Collegium has no authority over judicial compensation.", "தவறானது. நீதிபதிகளின் ஊதியத்தின் மீது கொலீஜியத்திற்கு அதிகாரம் இல்லை.",
        "Article 125(1): Judicial salaries default to Second Schedule until parliamentary enactment.",
        "சரத்து 125(1): பாராளுமன்றச் சட்டம் இயற்றப்படும் வரை நீதித்துறை சம்பளங்கள் இரண்டாவது அட்டவணையின்படி இருக்கும்."
    ))

    # GT012
    qs.append(make_sch_q(
        "SCH_GT_012", "Medium", "Conceptual", "Second Schedule",
        "Why are the emoluments, allowances, and expenditure relating to the offices listed in the Second Schedule charged directly upon the Consolidated Fund of India?",
        "இரண்டாவது அட்டவணையில் பட்டியலிடப்பட்டுள்ள பதவிகளுக்கான ஊதியங்கள் மற்றும் படிகள் ஏன் நேரடியாக இந்திய ஒருங்கிணைந்த நிதியத்தின் மீது சுமத்தப்படுகின்றன?",
        "To ensure that their payments are non-votable and immune from annual political pressure in Parliament", "அவர்களின் கொடுப்பனவுகள் வாக்களிப்பிற்கு உட்படுத்தப்படாமல், பாராளுமன்றத்தின் வருடாந்திர அரசியல் அழுத்தத்திலிருந்து விடுபடுவதை உறுதிசெய்ய",
        "To allow the Prime Minister to alter their salaries without parliamentary debate", "பாராளுமன்ற விவாதமின்றி பிரதம மந்திரி அவர்களின் சம்பளத்தை மாற்ற அனுமதிப்பதற்காக",
        "Because the Public Account of India lacks sufficient constitutional reserves", "இந்திய பொதுக் கணக்கில் போதுமான அரசியலமைப்பு கையிருப்பு இல்லாததால்",
        "To exempt all these offices from auditing by the Comptroller and Auditor-General", "இந்த அனைத்து பதவிகளையும் இந்திய தலைமை கணக்குத் தணிக்கையாளரின் தணிக்கையிலிருந்து விலக்குவதற்கு",
        "A",
        "Expenditure charged upon the Consolidated Fund of India (Article 112(3)) can be discussed in Parliament but is not submitted to the vote of Parliament, preserving judicial and constitutional independence.",
        "இந்திய ஒருங்கிணைந்த நிதியத்தின் மீது சுமத்தப்படும் செலவுகள் (சரத்து 112(3)) பாராளுமன்றத்தில் விவாதிக்கப்படலாம், ஆனால் வாக்களிப்பிற்கு விடப்படாது; இது நீதித்துறை மற்றும் அரசியலமைப்பு சுதந்திரத்தைப் பாதுகாக்கிறது.",
        "Correct. Charged expenditure is non-votable to secure independence.", "சரியானது. சுதந்திரத்தைப் பாதுகாக்க சுமத்தப்பட்ட செலவுகள் வாக்களிப்பிற்கு உட்படாதவை.",
        "Incorrect. Prime Minister cannot alter their salaries.", "தவறானது. பிரதமர் அவர்களின் சம்பளத்தை மாற்ற முடியாது.",
        "Incorrect. It has nothing to do with Public Account reserves.", "தவறானது. பொதுக் கணக்கு கையிருப்புடன் இதற்கு தொடர்பில்லை.",
        "Incorrect. Constitutional offices are subject to audit where applicable.", "தவறானது. அரசியலமைப்பு அலுவலகங்கள் தணிக்கைக்கு உட்பட்டவை.",
        "Charged expenditure: Discussable but non-votable in Parliament (Article 112(3)).",
        "சுமத்தப்பட்ட செலவு: பாராளுமன்றத்தில் விவாதிக்கலாம், ஆனால் வாக்களிக்க முடியாது (சரத்து 112(3))."
    ))

    # GT013
    qs.append(make_sch_q(
        "SCH_GT_013", "Easy", "Conceptual", "Second Schedule",
        "Which part of the Second Schedule specifies the salaries and allowances of the Speaker and Deputy Speaker of the House of the People and the Chairman and Deputy Chairman of the Council of States?",
        "மக்களவை சபாநாயகர், துணை சபாநாயகர் மற்றும் மாநிலங்களவைத் தலைவர், துணைத் தலைவர் ஆகியோரின் சம்பளம் மற்றும் படிகளை இரண்டாவது அட்டவணையின் எந்தப் பகுதி குறிப்பிடுகிறது?",
        "Part C", "பகுதி C",
        "Part A", "பகுதி A",
        "Part D", "பகுதி D",
        "Part E", "பகுதி E",
        "A",
        "Part C of the Second Schedule specifies provisions as to the Speaker and Deputy Speaker of the House of the People, Chairman and Deputy Chairman of the Council of States, and presiding officers of State Legislatures.",
        "இரண்டாவது அட்டவணையின் பகுதி C மக்களவை சபாநாயகர், துணை சபாநாயகர், மாநிலங்களவைத் தலைவர், துணைத் தலைவர் மற்றும் மாநில சட்டமன்றங்களின் அவைத் தலைவர்கள் பற்றிய விதிகளைக் குறிப்பிடுகிறது.",
        "Correct. Part C deals with legislative presiding officers.", "சரியானது. பகுதி C சட்டமன்ற அவைத் தலைவர்களைக் கையாள்கிறது.",
        "Incorrect. Part A deals with President and Governors.", "தவறானது. பகுதி A குடியரசுத் தலைவர் மற்றும் ஆளுநர்களைக் கையாள்கிறது.",
        "Incorrect. Part D deals with Judges.", "தவறானது. பகுதி D நீதிபதிகளைக் கையாள்கிறது.",
        "Incorrect. Part E deals with the CAG.", "தவறானது. பகுதி E சிஏஜியைக் கையாள்கிறது.",
        "Second Schedule breakdown: Part A (President/Governors), Part C (Presiding Officers), Part D (Judges), Part E (CAG).",
        "இரண்டாவது அட்டவணை பிரிவு: பகுதி A (குடியரசுத் தலைவர்/ஆளுநர்கள்), பகுதி C (அவைத் தலைவர்கள்), பகுதி D (நீதிபதிகள்), பகுதி E (CAG)."
    ))

    # GT014
    qs.append(make_sch_q(
        "SCH_GT_014", "Medium", "Conceptual", "Second Schedule",
        "Under Article 125(2) and the Second Schedule, can the allowances, rights in respect of leave of absence, or pension of a Supreme Court Judge be varied to their disadvantage after appointment?",
        "சரத்து 125(2) மற்றும் இரண்டாவது அட்டவணையின் கீழ், உச்சநீதிமன்ற நீதிபதியின் படிகள், விடுப்பு உரிமைகள் அல்லது ஓய்வூதியம் ஆகியவை நியமனத்திற்குப் பிறகு அவர்களுக்கு பாதகமாக மாற்றப்பட முடியுமா?",
        "No, they cannot be varied to their disadvantage after appointment", "இல்லை, நியமனத்திற்குப் பிறகு அவை அவர்களுக்கு பாதகமாக மாற்றப்பட முடியாது",
        "Yes, by a simple majority resolution passed in Lok Sabha", "ஆம், மக்களவையில் நிறைவேற்றப்படும் எளிய பெரும்பான்மைத் தீர்மானத்தின் மூலம்",
        "Yes, whenever the Union Cabinet passes an executive notification", "ஆம், மத்திய அமைச்சரவை நிர்வாக அறிவிப்பை வெளியிடும் போதெல்லாம்",
        "Yes, upon the recommendation of the Law Commission of India", "ஆம், இந்திய சட்ட ஆணையத்தின் பரிந்துரையின் பேரில்",
        "A",
        "Article 125(2) explicitly provides that neither the privileges nor the allowances of a Judge nor his rights in respect of leave of absence or pension shall be varied to his disadvantage after his appointment.",
        "சரத்து 125(2) வெளிப்படையாகக் கூறுகிறது: ஒரு நீதிபதியின் சலுகைகள், படிகள் அல்லது விடுப்பு, ஓய்வூதியம் தொடர்பான உரிமைகள் அவரது நியமனத்திற்குப் பிறகு அவருக்கு பாதகமாக மாற்றப்படக்கூடாது.",
        "Correct. Under Article 125(2), judicial conditions cannot be diminished during tenure.", "சரியானது. சரத்து 125(2)-ன் படி, பதவிக் காலத்தில் நீதித்துறை நிபந்தனைகளைக் குறைக்க முடியாது.",
        "Incorrect. Lok Sabha cannot diminish judges' terms by simple resolution.", "தவறானது. மக்களவை எளிய தீர்மானம் மூலம் குறைக்க முடியாது.",
        "Incorrect. Executive notifications cannot diminish statutory judicial terms.", "தவறானது. நிர்வாக அறிவிப்பு நீதித்துறை நிபந்தனைகளைக் குறைக்க முடியாது.",
        "Incorrect. Law Commission has no power to alter judicial salaries.", "தவறானது. சட்ட ஆணையத்திற்கு சம்பளத்தை மாற்ற அதிகாரம் இல்லை.",
        "Protection of Judicial Independence: Terms cannot be altered to disadvantage, except during Financial Emergency (Art 360).",
        "நீதித்துறை சுதந்திரப் பாதுகாப்பு: நிதி அவசரநிலையைத் தவிர (சரத்து 360) பிற நேரங்களில் நிபந்தனைகளைப் பாதகமாக மாற்ற முடியாது."
    ))

    # GT015
    qs.append(make_sch_q(
        "SCH_GT_015", "Easy", "Conceptual", "Second Schedule",
        "What is the monthly salary of the President of India specified by Parliament under the Second Schedule framework since the 2018 budget revision?",
        "2018 பட்ஜெட் திருத்தத்திற்குப் பிறகு இரண்டாவது அட்டவணை கட்டமைப்பின் கீழ் பாராளுமன்றத்தால் நிர்ணயிக்கப்பட்ட இந்தியக் குடியரசுத் தலைவரின் மாதச் சம்பளம் என்ன?",
        "Rs. 5,00,000 per month", "மாதம் ரூ. 5,00,000",
        "Rs. 4,00,000 per month", "மாதம் ரூ. 4,00,000",
        "Rs. 3,50,000 per month", "மாதம் ரூ. 3,50,000",
        "Rs. 2,50,000 per month", "மாதம் ரூ. 2,50,000",
        "A",
        "In the 2018 Union Budget, Parliament increased the salary of the President of India to Rs. 5,00,000 per month (from Rs. 1.5 lakh). The Vice-President receives Rs. 4,00,000 and Governors receive Rs. 3,50,000.",
        "2018 மத்திய பட்ஜெட்டில், இந்தியக் குடியரசுத் தலைவரின் மாதச் சம்பளத்தை பாராளுமன்றம் ரூ. 5,00,000 ஆக உயர்த்தியது. குடியரசுத் துணைத் தலைவர் ரூ. 4,00,000-ம், ஆளுநர்கள் ரூ. 3,50,000-ம் பெறுகின்றனர்.",
        "Correct. President's monthly salary is Rs. 5 lakh.", "சரியானது. குடியரசுத் தலைவரின் மாதச் சம்பளம் ரூ. 5 லட்சம்.",
        "Incorrect. Rs. 4,00,000 is the salary of the Vice-President.", "தவறானது. ரூ. 4,00,000 என்பது குடியரசுத் துணைத் தலைவரின் சம்பளம்.",
        "Incorrect. Rs. 3,50,000 is the salary of State Governors.", "தவறானது. ரூ. 3,50,000 என்பது மாநில ஆளுநர்களின் சம்பளம்.",
        "Incorrect. Rs. 2,50,000 is the salary of Supreme Court Judges.", "தவறானது. ரூ. 2,50,000 என்பது உச்சநீதிமன்ற நீதிபதிகளின் சம்பளம்.",
        "Current Salaries: President (Rs. 5L), Vice-President (Rs. 4L), Governor (Rs. 3.5L), CJI (Rs. 2.8L), SC Judges (Rs. 2.5L).",
        "தற்போதைய சம்பளங்கள்: குடியரசுத் தலைவர் (5 லட்ச), துணைத் தலைவர் (4 லட்ச), ஆளுநர் (3.5 லட்ச), தலைமை நீதிபதி (2.8 லட்ச), உச்சநீதிமன்ற நீதிபதி (2.5 லட்ச)."
    ))

    # GT016
    qs.append(make_sch_q(
        "SCH_GT_016", "Medium", "Conceptual", "Second Schedule",
        "Why are the salaries and allowances of the Prime Minister and Union Council of Ministers absent from the Second Schedule of the Indian Constitution?",
        "இந்திய அரசியலமைப்பின் இரண்டாவது அட்டவணையில் பிரதம மந்திரி மற்றும் மத்திய அமைச்சரவையின் சம்பளம் மற்றும் படிகள் ஏன் இடம் பெறவில்லை?",
        "Because Article 75(6) empowers Parliament to determine ministerial salaries separately by statutory law", "ஏனெனில் சரத்து 75(6) பாராளுமன்றத்திற்கு அமைச்சர்களின் சம்பளங்களை தனிச் சட்டத்தின் மூலம் நிர்ணயிக்க அதிகாரம் அளிக்கிறது",
        "Because Ministers receive executive honorariums from the Contingency Fund of India", "ஏனெனில் அமைச்சர்கள் இந்திய அவசரகால நிதியிலிருந்து நிர்வாக கௌரவ ஊதியத்தைப் பெறுகிறார்கள்",
        "Because Ministers are treated as civil servants governed by Article 309", "ஏனெனில் அமைச்சர்கள் சரத்து 309-ன் கீழ் ஆளப்படும் அரசு ஊழியர்களாகக் கருதப்படுகிறார்கள்",
        "Because the Constituent Assembly forgot to include ministers in the draft", "ஏனெனில் அரசியலமைப்பு நிர்ணய சபை அமைச்சர்களை வரைவில் சேர்க்க மறந்துவிட்டது",
        "A",
        "Under Article 75(6), the salaries and allowances of Ministers are determined by Parliament by law from time to time via the Salaries and Allowances of Ministers Act, 1952, not under the Second Schedule.",
        "சரத்து 75(6)-ன் கீழ், அமைச்சர்களின் சம்பளம் மற்றும் படிகள் பாராளுமன்றத்தால் அவ்வப்போது சட்டம் இயற்றி (அமைச்சர்கள் சம்பளச் சட்டம் 1952) தீர்மானிக்கப்படுகின்றன; அவை இரண்டாவது அட்டவணையில் இல்லை.",
        "Correct. Governed by Article 75(6) and separate legislation.", "சரியானது. சரத்து 75(6) மற்றும் தனிச் சட்டத்தால் ஆளப்படுகிறது.",
        "Incorrect. Contingency Fund is for unforeseen disasters, not salaries.", "தவறானது. அவசரகால நிதி எதிர்பாராத பேரழிவுகளுக்கானது, சம்பளத்திற்கு அல்ல.",
        "Incorrect. Ministers are political executives, not Article 309 civil servants.", "தவறானது. அமைச்சர்கள் அரசியல் நிர்வாகிகள், அரசு ஊழியர்கள் அல்ல.",
        "Incorrect. Omission was a deliberate constitutional choice.", "தவறானது. திட்டமிட்டே பாராளுமன்ற சட்டத்திற்கு விடப்பட்டது.",
        "Ministers: Salaries governed by Article 75(6) (Union) and Article 164(5) (States), not Second Schedule.",
        "அமைச்சர்கள்: சம்பளம் சரத்து 75(6) (மத்திய) மற்றும் 164(5) (மாநில) மூலம் தீர்மானிக்கப்படுகிறது, இரண்டாவது அட்டவணை அல்ல."
    ))

    # GT017
    qs.append(make_sch_q(
        "SCH_GT_017", "Hard", "Conceptual", "Third Schedule",
        "Which crucial pledge was added to the forms of oath in the Third Schedule by the Constitution (16th Amendment) Act, 1963?",
        "அரசியலமைப்பு (16வது திருத்தச்) சட்டம் 1963 மூலம் மூன்றாவது அட்டவணையில் உள்ள உறுதிமொழி படிவங்களில் சேர்க்கப்பட்ட முக்கியமான வாசகம் எது?",
        "'Uphold the sovereignty and integrity of India'", "'இந்தியாவின் இறையாண்மையையும் ஒருமைப்பாட்டையும் நிலைநிறுத்துவேன்'",
        "'Protect the secular fabric of the Republic'", "'குடியரசின் மதச்சார்பற்ற கட்டமைப்பைப் பாதுகாப்பேன்'",
        "'Promote scientific temper and humanism'", "'அறிவியல் மனப்பான்மை மற்றும் மனிதநேயத்தை வளர்ப்பேன்'",
        "'Eradicate untouchability across the nation'", "'நாடு முழுவதும் தீண்டாமையை ஒழிப்பேன்'",
        "A",
        "Following the recommendations of the National Integration Council and the Committee on National Integration, the 16th Amendment, 1963 added the phrase 'uphold the sovereignty and integrity of India' to the oaths in the Third Schedule.",
        "தேசிய ஒருமைப்பாட்டுக் குழுவின் பரிந்துரைகளைத் தொடர்ந்து, 1963-ன் 16வது திருத்தச் சட்டம் மூன்றாவது அட்டவணையில் உள்ள உறுதிமொழிகளில் 'இந்தியாவின் இறையாண்மையையும் ஒருமைப்பாட்டையும் நிலைநிறுத்துவேன்' என்ற வாசகத்தைச் சேர்த்தது.",
        "Correct. 16th Amendment 1963 introduced the sovereignty and integrity pledge.", "சரியானது. 16வது திருத்தம் 1963 இறையாண்மை மற்றும் ஒருமைப்பாடு வாசகத்தை அறிமுகப்படுத்தியது.",
        "Incorrect. Secularism was added to the Preamble by the 42nd CAA 1976.", "தவறானது. மதச்சார்பின்மை 42வது திருத்தம் 1976 மூலம் முகப்புரையில் சேர்க்கப்பட்டது.",
        "Incorrect. Scientific temper is a Fundamental Duty under Art 51A(h).", "தவறானது. அறிவியல் மனப்பான்மை சரத்து 51A(h)-ன் கீழான அடிப்படை கடமையாகும்.",
        "Incorrect. Untouchability is abolished by Article 17.", "தவறானது. தீண்டாமை சரத்து 17-ன் கீழ் ஒழிக்கப்பட்டுள்ளது.",
        "16th Amendment Act, 1963: Added 'sovereignty and integrity of India' to Third Schedule oaths and Article 19 restrictions.",
        "16வது திருத்தச் சட்டம் 1963: மூன்றாவது அட்டவணை உறுதிமொழிகளிலும் சரத்து 19 கட்டுப்பாடுகளிலும் 'இறையாண்மை மற்றும் ஒருமைப்பாடு' சேர்த்தது."
    ))

    # GT018
    qs.append(make_sch_q(
        "SCH_GT_018", "Medium", "Conceptual", "Third Schedule",
        "In the Third Schedule, which constitutional office requires subscribing to two distinct forms of oath: an Oath of Office and an Oath of Secrecy?",
        "மூன்றாவது அட்டவணையில், எந்த அரசியலமைப்பு பதவிக்கு இரண்டு வெவ்வேறு உறுதிமொழி படிவங்கள் (பதவிப் பிரமாணம் மற்றும் இரகசியக் காப்புப் பிரமாணம்) எடுக்கப்பட வேண்டும்?",
        "Union Ministers and State Ministers", "மத்திய அமைச்சர்கள் மற்றும் மாநில அமைச்சர்கள்",
        "Judges of the Supreme Court and High Courts", "உச்சநீதிமன்ற மற்றும் உயர்நீதிமன்ற நீதிபதிகள்",
        "Comptroller and Auditor-General of India", "இந்திய தலைமை கணக்குத் தணிக்கையாளர்",
        "Members of Parliament and State Legislatures", "பாராளுமன்ற மற்றும் மாநில சட்டமன்ற உறுப்பினர்கள்",
        "A",
        "Forms I and II are the Oath of Office and Oath of Secrecy for Union Ministers; Forms V and VI are the Oath of Office and Oath of Secrecy for State Ministers. Judges and legislators take only an oath of office.",
        "படிவங்கள் I மற்றும் II மத்திய அமைச்சர்களுக்கான பதவிப் பிரமாணம் மற்றும் இரகசியக் காப்புப் பிரமாணம் ஆகும்; படிவங்கள் V மற்றும் VI மாநில அமைச்சர்களுக்கானவை. நீதிபதிகளும் எம்.பி.க்களும் பதவிப் பிரமாணம் மட்டுமே ஏற்கின்றனர்.",
        "Correct. Only Ministers take both an oath of office and an oath of secrecy.", "சரியானது. அமைச்சர்கள் மட்டுமே பதவி மற்றும் இரகசியக் காப்பு ஆகிய இரு உறுதிமொழிகளையும் ஏற்கின்றனர்.",
        "Incorrect. Judges take an oath of office and allegiance, not secrecy.", "தவறானது. நீதிபதிகள் பதவி மற்றும் விசுவாசப் பிரமாணம் மட்டுமே ஏற்கின்றனர்.",
        "Incorrect. CAG takes an oath of office, not secrecy.", "தவறானது. சிஏஜி பதவிப் பிரமாணம் மட்டுமே ஏற்கிறார்.",
        "Incorrect. Legislators take an oath of allegiance under Art 99/188.", "தவறானது. சட்டமன்ற உறுப்பினர்கள் விசுவாசப் பிரமாணம் மட்டுமே ஏற்கின்றனர்.",
        "Third Schedule: Ministers take two oaths (Office + Secrecy). All others take one oath.",
        "மூன்றாவது அட்டவணை: அமைச்சர்கள் இரண்டு உறுதிமொழிகளை (பதவி + இரகசியம்) ஏற்கின்றனர்; மற்றவர்கள் ஒரு உறுதிமொழி மட்டுமே."
    ))

    # GT019
    qs.append(make_sch_q(
        "SCH_GT_019", "Hard", "Conceptual", "Third Schedule",
        "Under Form III/A of the Third Schedule, before whom must a candidate contesting elections to Parliament make and subscribe the requisite oath?",
        "மூன்றாவது அட்டவணையின் படிவம் III/A-ன் கீழ், பாராளுமன்றத் தேர்தலில் போட்டியிடும் வேட்பாளர் யாருக்கு முன்பாகத் தேவையான உறுதிமொழியை எடுத்து கையொப்பமிட வேண்டும்?",
        "A person authorized by the Election Commission of India (typically the Returning Officer)", "இந்திய தேர்தல் ஆணையத்தால் அங்கீகரிக்கப்பட்ட நபர் (பொதுவாக தேர்தல் நடத்தும் அலுவலர் - Returning Officer)",
        "The Chief Justice of India or a designated Supreme Court Judge", "இந்திய தலைமை நீதிபதி அல்லது அவரால் நியமிக்கப்பட்ட உச்சநீதிமன்ற நீதிபதி",
        "The President of India at Rashtrapati Bhavan", "ராஷ்டிரபதி பவனில் இந்தியக் குடியரசுத் தலைவர்",
        "The Speaker of the Lok Sabha inside Parliament House", "பாராளுமன்ற வளாகத்தில் மக்களவை சபாநாயகர்",
        "A",
        "Under Article 84(a) and the Third Schedule (Form III/A), an election candidate must make the oath before a person authorized by the Election Commission, such as the Returning Officer or Assistant Returning Officer.",
        "சரத்து 84(a) மற்றும் மூன்றாவது அட்டவணையின் (படிவம் III/A) படி, தேர்தல் வேட்பாளர் தேர்தல் நடத்தும் அலுவலர் (RO) போன்ற தேர்தல் ஆணையத்தால் அங்கீகரிக்கப்பட்ட நபருக்கு முன்பாக உறுதிமொழி எடுக்க வேண்டும்.",
        "Correct. Candidate oath is made before an authorized officer (Returning Officer).", "சரியானது. வேட்பாளர் உறுதிமொழி தேர்தல் நடத்தும் அலுவலர் முன் எடுக்கப்படுகிறது.",
        "Incorrect. Chief Justice administers oath to the President.", "தவறானது. தலைமை நீதிபதி குடியரசுத் தலைவருக்கு உறுதிமொழி செய்து வைக்கிறார்.",
        "Incorrect. President administers oath to Ministers and Judges.", "தவறானது. குடியரசுத் தலைவர் அமைச்சர்களுக்கும் நீதிபதிகளுக்கும் உறுதிமொழி செய்து வைக்கிறார்.",
        "Incorrect. Lok Sabha Speaker does not administer candidate oaths.", "தவறானது. மக்களவை சபாநாயகர் வேட்பாளர் உறுதிமொழிகளை ஏற்பதில்லை.",
        "Candidate Oath: Introduced by 16th CAA 1963 to ensure loyalty before contesting elections.",
        "வேட்பாளர் உறுதிமொழி: தேர்தலில் போட்டியிடும் முன்பே விசுவாசத்தை உறுதிசெய்ய 16வது திருத்தம் 1963 மூலம் அறிமுகப்படுத்தப்பட்டது."
    ))

    # GT020
    qs.append(make_sch_q(
        "SCH_GT_020", "Medium", "Conceptual", "Third Schedule",
        "Under Article 148(2), the Comptroller and Auditor-General of India makes and subscribes an oath according to the form set out in which Schedule?",
        "சரத்து 148(2)-ன் கீழ், இந்திய தலைமை கணக்குத் தணிக்கையாளர் எந்த அட்டவணையில் குறிப்பிடப்பட்டுள்ள படிவத்தின்படி உறுதிமொழி ஏற்றுக்கொள்கிறார்?",
        "Third Schedule (Form IV)", "மூன்றாவது அட்டவணை (படிவம் IV)",
        "Second Schedule (Part E)", "இரண்டாவது அட்டவணை (பகுதி E)",
        "First Schedule (Part II)", "முதல் அட்டவணை (பகுதி II)",
        "Fourth Schedule (Table A)", "நான்காவது அட்டவணை (அட்டவணை A)",
        "A",
        "Form IV of the Third Schedule sets out the form of oath or affirmation to be made by the Judges of the Supreme Court and the Comptroller and Auditor-General of India under Article 148(2).",
        "மூன்றாவது அட்டவணையின் படிவம் IV, சரத்து 148(2)-ன் கீழ் உச்சநீதிமன்ற நீதிபதிகள் மற்றும் இந்திய தலைமை கணக்குத் தணிக்கையாளர் ஏற்கும் உறுதிமொழிப் படிவத்தைக் குறிப்பிடுகிறது.",
        "Correct. CAG oath is set out in Form IV of the Third Schedule.", "சரியானது. சிஏஜி உறுதிமொழி மூன்றாவது அட்டவணையின் படிவம் IV-ல் உள்ளது.",
        "Incorrect. Second Schedule Part E covers CAG salary, not oath.", "தவறானது. இரண்டாவது அட்டவணை பகுதி E சிஏஜி சம்பளத்தைக் குறிக்கிறது, உறுதிமொழி அல்ல.",
        "Incorrect. First Schedule is territories.", "தவறானது. முதல் அட்டவணை ஆட்சிப் பகுதிகள் பற்றியது.",
        "Incorrect. Fourth Schedule is Rajya Sabha seats.", "தவறானது. நான்காவது அட்டவணை மாநிலங்களவை இடங்கள்.",
        "Form IV of Third Schedule: Shared by Judges of Supreme Court and the CAG.",
        "மூன்றாவது அட்டவணையின் படிவம் IV: உச்சநீதிமன்ற நீதிபதிகள் மற்றும் சிஏஜி ஆகிய இருவராலும் பகிர்ந்து கொள்ளப்படுகிறது."
    ))

    # GT021
    qs.append(make_sch_q(
        "SCH_GT_021", "Hard", "Conceptual", "Third Schedule",
        "Under Article 104 of the Constitution, what penalty is levied per day if a person sits or votes as a Member of Parliament before taking the Third Schedule oath?",
        "அரசியலமைப்பின் சரத்து 104-ன் கீழ், ஒரு நபர் மூன்றாவது அட்டவணை உறுதிமொழியை எடுப்பதற்கு முன் பாராளுமன்ற உறுப்பினராக அமர்ந்தால் அல்லது வாக்களித்தால் ஒரு நாளைக்கு விதிக்கப்படும் அபராதம் என்ன?",
        "Rs. 500 per day recoverable as a debt due to the Union", "மத்திய அரசுக்குச் செலுத்த வேண்டிய கடனாக வசூலிக்கப்படும் நாள் ஒன்றுக்கு ரூ. 500",
        "Rs. 5,000 per day deducted from member's salary", "உறுப்பினரின் சம்பளத்திலிருந்து கழிக்கப்படும் நாள் ஒன்றுக்கு ரூ. 5,000",
        "Rs. 10,000 per day with immediate disqualification", "உடனடி தகுதியிழப்புடன் நாள் ஒன்றுக்கு ரூ. 10,000",
        "Rs. 1,000 per day remitted to the Election Commission", "தேர்தல் ஆணையத்திற்குச் செலுத்தப்படும் நாள் ஒன்றுக்கு ரூ. 1,000",
        "A",
        "Article 104 provides that if a person sits or votes as a member of either House before making the oath under Article 99 and Third Schedule, he shall be liable to a penalty of Rs. 500 for each day, recoverable as a debt due to the Union.",
        "சரத்து 104 கூறுகிறது: ஒரு நபர் சரத்து 99 மற்றும் மூன்றாவது அட்டவணையின் கீழ் உறுதிமொழி எடுப்பதற்கு முன் அவையில் அமர்ந்தால் அல்லது வாக்களித்தால், அவர் ஒரு நாளைக்கு ரூ. 500 அபராதம் செலுத்த வேண்டும் (மத்திய அரசுக்குரிய கடனாக வசூலிக்கப்படும்).",
        "Correct. Article 104 imposes a Rs. 500 daily penalty for unsworn sitting/voting.", "சரியானது. சரத்து 104 உறுதிமொழி எடுக்காமல் அமர்ந்தால் ரூ. 500 அபராதம் விதிக்கிறது.",
        "Incorrect. Penalty is Rs. 500, not Rs. 5,000.", "தவறானது. அபராதம் ரூ. 500, ரூ. 5,000 அல்ல.",
        "Incorrect. It does not lead to automated immediate disqualification.", "தவறானது. இது உடனடி தகுதியிழப்புக்கு வழிவகுக்காது.",
        "Incorrect. Money goes to the Union Consolidated Fund, not Election Commission.", "தவறானது. தொகை மத்திய அரசுக்கே சேரும், தேர்தல் ஆணையத்திற்கு அல்ல.",
        "Articles 104 (Parliament) and 193 (State Legislatures): Rs. 500 daily penalty for sitting or voting before taking oath.",
        "சரத்து 104 (பாராளுமன்றம்) மற்றும் 193 (சட்டமன்றம்): உறுதிமொழி ஏற்பதற்கு முன் அமர்ந்தால் நாள் ஒன்றுக்கு ரூ. 500 அபராதம்."
    ))

    # GT022
    qs.append(make_sch_q(
        "SCH_GT_022", "Medium", "Conceptual", "Third Schedule",
        "Which specific phrase is contained in the Third Schedule oath for Supreme Court and High Court Judges regarding their judicial impartiality?",
        "நீதித்துறை நடுநிலைமை தொடர்பாக உச்சநீதிமன்ற மற்றும் உயர்நீதிமன்ற நீதிபதிகளுக்கான மூன்றாவது அட்டவணை உறுதிமொழியில் உள்ள குறிப்பிட்ட வாசகம் எது?",
        "'Without fear or favour, affection or ill-will'", "'பயமோ தயவோ, விருப்போ வெறுப்போ இன்றி'",
        "'Without political alignment or personal prejudice'", "'அரசியல் சார்போ தனிப்பட்ட தப்பெண்ணமோ இன்றி'",
        "'With utmost loyalty to the elected executive government'", "'தேர்ந்தெடுக்கப்பட்ட நிர்வாக அரசாங்கத்திற்கு மிகுந்த விசுவாசத்துடன்'",
        "'In complete conformity with the directives of the Law Ministry'", "'சட்ட அமைச்சகத்தின் உத்தரவுகளுக்கு முழுமையாக இணங்கி'",
        "A",
        "The oath of a Judge of the Supreme Court and High Court in the Third Schedule mandates: 'perform the duties of my office without fear or favour, affection or ill-will and that I will uphold the Constitution and the laws.'",
        "மூன்றாவது அட்டவணையில் உச்சநீதிமன்ற மற்றும் உயர்நீதிமன்ற நீதிபதிகளின் உறுதிமொழி குறிப்பிடுகிறது: 'பயமோ தயவோ, விருப்போ வெறுப்போ இன்றி என் கடமைகளை ஆற்றுவேன் மற்றும் அரசியலமைப்பையும் சட்டங்களையும் நிலைநிறுத்துவேன்.'",
        "Correct. 'Without fear or favour, affection or ill-will' is the canonical judicial phrase.", "சரியானது. 'பயமோ தயவோ, விருப்போ வெறுப்போ இன்றி' என்பது நீதித்துறை வாசகம்.",
        "Incorrect. Not part of the constitutional oath text.", "தவறானது. இது அரசியலமைப்பு வாசகம் அல்ல.",
        "Incorrect. Judges owe loyalty to the Constitution, not the executive government.", "தவறானது. நீதிபதிகள் அரசியலமைப்பிற்கு மட்டுமே விசுவாசமாக இருக்க வேண்டும்.",
        "Incorrect. Judges are independent of the Law Ministry.", "தவறானது. நீதிபதிகள் சட்ட அமைச்சகத்திலிருந்து சுதந்திரமானவர்கள்.",
        "Judicial Oath: 'Without fear or favour, affection or ill-will' (Forms IV and VIII).",
        "நீதித்துறை உறுதிமொழி: 'பயமோ தயவோ, விருப்போ வெறுப்போ இன்றி' (படிவங்கள் IV மற்றும் VIII)."
    ))

    # GT023
    qs.append(make_sch_q(
        "SCH_GT_023", "Easy", "Conceptual", "Third Schedule",
        "What wording in the Third Schedule allows a non-believer or secular individual to take office without invoking a deity?",
        "மூன்றாவது அட்டவணையில் உள்ள எந்த வாசகம் கடவுள் நம்பிக்கை இல்லாதவர் அல்லது மதச்சார்பற்ற நபர் கடவுளின் பெயரைப் பயன்படுத்தாமல் பதவியேற்க அனுமதிக்கிறது?",
        "'Solemnly affirm'", "'உளமார உறுதி கூறுகிறேன்'",
        "'Promise by conscience'", "'மனசாட்சியின்படி வாக்களிக்கிறேன்'",
        "'Attest by truth'", "'உண்மையின் மீது சான்றளிக்கிறேன்'",
        "'Declare with honor'", "'மரியாதையுடன் பிரகடனம் செய்கிறேன்'",
        "A",
        "Every form of oath in the Third Schedule provides the alternative: 'Swear in the name of God' OR 'Solemnly affirm', permitting individuals to make an affirmation without religious reference.",
        "மூன்றாவது அட்டவணையில் உள்ள ஒவ்வொரு படிவமும் 'கடவுளின் பெயரால் ஆணையிட்டு' அல்லது 'உளமார உறுதி கூறுகிறேன்' என்ற மாற்றீட்டை வழங்குகிறது, இது மதச்சார்பற்ற நபர்கள் உறுதியேற்க அனுமதிக்கிறது.",
        "Correct. 'Solemnly affirm' is the legal alternative to swearing by God.", "சரியானது. கடவுளின் பெயரால் உறுதி ஏற்பதற்கு மாற்றாக 'உளமார உறுதி கூறுகிறேன்' என்பது உள்ளது.",
        "Incorrect. 'Promise by conscience' is not the constitutional terminology.", "தவறானது. இது அரசியலமைப்பு கலைச்சொல் அல்ல.",
        "Incorrect. 'Attest by truth' is not used.", "தவறானது. இது பயன்படுத்தப்படவில்லை.",
        "Incorrect. 'Declare with honor' is not used in Indian oaths.", "தவறானது. இந்திய உறுதிமொழிகளில் இது பயன்படுத்தப்படவில்லை.",
        "Third Schedule: Always gives choice between 'Swear in the name of God' and 'Solemnly affirm'.",
        "மூன்றாவது அட்டவணை: 'கடவுளின் பெயரால் ஆணையிடுதல்' அல்லது 'உளமார உறுதி கூறுதல்' ஆகிய இரு தேர்வுகளை எப்போதும் வழங்குகிறது."
    ))

    # GT024
    qs.append(make_sch_q(
        "SCH_GT_024", "Medium", "Conceptual", "Third Schedule",
        "Why is the oath of the Vice-President of India not found in the Third Schedule of the Indian Constitution?",
        "இந்திய அரசியலமைப்பின் மூன்றாவது அட்டவணையில் இந்தியக் குடியரசுத் துணைத் தலைவரின் உறுதிமொழி ஏன் இடம் பெறவில்லை?",
        "Because it is explicitly prescribed under Article 69 within the main text of the Constitution", "ஏனெனில் இது அரசியலமைப்பின் முதன்மைப் பகுதியில் சரத்து 69-ன் கீழ் வெளிப்படையாகக் குறிப்பிடப்பட்டுள்ளது",
        "Because the Vice-President takes an oath only as the Chairman of the Rajya Sabha under Article 89", "ஏனெனில் குடியரசுத் துணைத் தலைவர் சரத்து 89-ன் கீழ் மாநிலங்களவைத் தலைவராக மட்டுமே உறுதிமொழி ஏற்கிறார்",
        "Because the Vice-President is administered oath by the Lok Sabha Speaker under Parliamentary Rules", "ஏனெனில் குடியரசுத் துணைத் தலைவருக்கு பாராளுமன்ற விதிகளின் கீழ் மக்களவை சபாநாயகர் உறுதிமொழி செய்து வைக்கிறார்",
        "Because the Vice-President does not take an oath upon assuming constitutional office", "ஏனெனில் குடியரசுத் துணைத் தலைவர் அரசியலமைப்புப் பதவியேற்கும் போது உறுதிமொழி எடுப்பதில்லை",
        "A",
        "The oaths of the President (Article 60), Vice-President (Article 69), and Governors (Article 159) are contained directly in individual constitutional articles, not in the Third Schedule.",
        "குடியரசுத் தலைவர் (சரத்து 60), குடியரசுத் துணைத் தலைவர் (சரத்து 69) மற்றும் ஆளுநர்களின் (சரத்து 159) உறுதிமொழிகள் மூன்றாவது அட்டவணையில் இல்லாமல் நேரடியாக அரசியலமைப்பு சரத்துகளில் உள்ளன.",
        "Correct. Vice-President's oath is set out in Article 69.", "சரியானது. குடியரசுத் துணைத் தலைவரின் உறுதிமொழி சரத்து 69-ல் உள்ளது.",
        "Incorrect. He takes oath as Vice-President, not merely as Chairman.", "தவறானது. அவர் தலைவராக மட்டுமின்றி துணைத் தலைவராகவும் உறுதிமொழி ஏற்கிறார்.",
        "Incorrect. President of India administers the oath to the Vice-President.", "தவறானது. குடியரசுத் தலைவர் துணைத் தலைவருக்கு உறுதிமொழி செய்து வைக்கிறார்.",
        "Incorrect. Oath is mandatory before entering office.", "தவறானது. பதவியேற்பதற்கு முன் உறுதிமொழி கட்டாயமானது.",
        "Oaths outside Third Schedule: President (Art 60), Vice-President (Art 69), Governor (Art 159).",
        "மூன்றாவது அட்டவணைக்கு வெளியே உள்ள உறுதிமொழிகள்: குடியரசுத் தலைவர் (சரத்து 60), துணைத் தலைவர் (சரத்து 69), ஆளுநர் (சரத்து 159)."
    ))

    # GT025
    qs.append(make_sch_q(
        "SCH_GT_025", "Medium", "Conceptual", "Fourth Schedule",
        "When Uttarakhand was carved out of Uttar Pradesh in November 2000, how many Rajya Sabha seats were allocated to Uttarakhand in the Fourth Schedule?",
        "நவம்பர் 2000-ல் உத்தரப் பிரதேசத்திலிருந்து பிரிக்கப்பட்டு உத்தரகாண்ட் உருவாக்கப்பட்ட போது, நான்காவது அட்டவணையில் உத்தரகாண்டிற்கு எத்தனை மாநிலங்களவை இடங்கள் ஒதுக்கப்பட்டன?",
        "3 seats", "3 இடங்கள்",
        "1 seat", "1 இடம்",
        "5 seats", "5 இடங்கள்",
        "7 seats", "7 இடங்கள்",
        "A",
        "Under the Uttar Pradesh Reorganisation Act, 2000, which amended the Fourth Schedule, 3 Rajya Sabha seats were allocated to Uttarakhand, while Uttar Pradesh retained 31 seats.",
        "நான்காவது அட்டவணையைத் திருத்திய உத்தரப் பிரதேச மறுசீரமைப்புச் சட்டம் 2000-ன் கீழ், உத்தரகாண்டிற்கு 3 மாநிலங்களவை இடங்கள் ஒதுக்கப்பட்டன; உத்தரப் பிரதேசம் 31 இடங்களைத் தக்க வைத்துக் கொண்டது.",
        "Correct. Uttarakhand has 3 seats in the Fourth Schedule.", "சரியானது. உத்தரகாண்டிற்கு நான்காவது அட்டவணையில் 3 இடங்கள் உள்ளன.",
        "Incorrect. 1 seat is typical of smaller North-Eastern states and Goa.", "தவறானது. 1 இடம் சிறிய வடகிழக்கு மாநிலங்கள் மற்றும் கோவாவிற்கு உரியது.",
        "Incorrect. Chhattisgarh received 5 seats.", "தவறானது. சத்தீஸ்கருக்கு 5 இடங்கள் ஒதுக்கப்பட்டன.",
        "Incorrect. Jharkhand received 6 seats.", "தவறானது. ஜார்க்கண்டிற்கு 6 இடங்கள் ஒதுக்கப்பட்டன.",
        "2000 Reorganisation (Rajya Sabha seats): Uttarakhand (3), Chhattisgarh (5), Jharkhand (6).",
        "2000 மறுசீரமைப்பு (மாநிலங்களவை இடங்கள்): உத்தரகாண்ட் (3), சத்தீஸ்கர் (5), ஜார்க்கண்ட் (6)."
    ))

    return qs

if __name__ == "__main__":
    qs = get_batch1()
    print(f"Batch 1 generated {len(qs)} questions.")
