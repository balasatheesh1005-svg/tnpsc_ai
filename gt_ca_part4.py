# Grand Test Constitutional Amendments - Part 4 (Q76 to Q100)
# Target Answer Key Distribution: 6 A, 6 B, 6 C, 7 D = 25 Total

part4_questions = []

def add_p4(q_id, difficulty, q_type, q_en, q_ta,
           opt_a_en, opt_a_ta, opt_b_en, opt_b_ta, opt_c_en, opt_c_ta, opt_d_en, opt_d_ta,
           correct_ans, exp_en, exp_ta,
           why_a_en, why_a_ta, why_b_en, why_b_ta, why_c_en, why_c_ta, why_d_en, why_d_ta,
           tip_en, tip_ta, fact_en, fact_ta, bloom, pyq_sim, tags):
    part4_questions.append({
        "id": q_id,
        "subject": "Polity",
        "topic": "Constitutional Amendments",
        "difficulty": difficulty,
        "question_type": q_type,
        "question": {"en": q_en, "ta": q_ta},
        "options": [
            {"id": "A", "en": opt_a_en, "ta": opt_a_ta},
            {"id": "B", "en": opt_b_en, "ta": opt_b_ta},
            {"id": "C", "en": opt_c_en, "ta": opt_c_ta},
            {"id": "D", "en": opt_d_en, "ta": opt_d_ta}
        ],
        "correct_answer": correct_ans,
        "explanation": {"en": exp_en, "ta": exp_ta},
        "why_not_others": {
            "A": {"en": why_a_en, "ta": why_a_ta},
            "B": {"en": why_b_en, "ta": why_b_ta},
            "C": {"en": why_c_en, "ta": why_c_ta},
            "D": {"en": why_d_en, "ta": why_d_ta}
        },
        "tnpsc_tip": {"en": tip_en, "ta": tip_ta},
        "revision_fact": {"en": fact_en, "ta": fact_ta},
        "source_reference": [
            "M. Laxmikanth — Indian Polity (Constitutional Amendments)",
            "TNPSC Nova AI Notes — Constitutional Amendments (Parts 1-3)",
            "NCERT Class XI - Indian Constitution at Work"
        ],
        "bloom_level": bloom,
        "estimated_time_sec": 60,
        "pyq_similarity": pyq_sim,
        "tags": tags
    })

# Q76 - Ans: A
add_p4(
    "polity_amendments_gt_076", "Hard", "pyq",
    "[TNPSC Group 1 Standard] Which of the following statements regarding the procedure for amending the Indian Constitution under Article 368 is INCORRECT?",
    "[டிஎன்பிஎஸ்சி குரூப் 1 தரநிலை] சரத்து 368-ன் கீழ் இந்திய அரசியலமைப்பைத் திருத்துவதற்கான நடைமுறை குறித்த பின்வரும் கூற்றுகளில் எது தவறானது?",
    "A Constitutional Amendment Bill can be initiated in a State Legislative Assembly if passed by a two-thirds majority.", "மாநில சட்டமன்றத்தில் 2/3 பங்கு பெரும்பான்மையுடன் நிறைவேற்றப்பட்டால், அரசியலமைப்பு திருத்த மசோதாவை மாநில சட்டமன்றத்தில் தொடங்கலாம்.",
    "Prior recommendation of the President is NOT required for introducing a Constitutional Amendment Bill.", "அரசியலமைப்பு திருத்த மசோதாவை அறிமுகப்படுத்த குடியரசுத் தலைவரின் முன் பரிந்துரை தேவையில்லை.",
    "There is no provision for a Joint Sitting of both Houses of Parliament to resolve a deadlock over an amendment bill.", "திருத்த மசோதாவின் முட்டுக்கட்டையைத் தீர்க்க நாடாளுமன்றத்தின் இரு அவைகளின் கூட்டு அமர்விற்கு எந்த விதியும் இல்லை.",
    "The President is bound to give assent to a Constitutional Amendment Bill passed by Parliament.", "நாடாளுமன்றத்தால் நிறைவேற்றப்பட்ட அரசியலமைப்பு திருத்த மசோதாவிற்கு ஒப்புதல் அளிக்க குடியரசுத் தலைவர் கடமைப்பட்டவர்.",
    "A",
    "📚 Core Explanation:\nOption A is INCORRECT (and hence the correct answer). A Constitutional Amendment Bill CANNOT be initiated in State Legislatures under any circumstances. It can only be introduced in either House of Parliament (Lok Sabha or Rajya Sabha). Options B, C, and D are all correct statements under Article 368.",
    "📚 முதன்மை விளக்கம்:\nவிருப்பம் A தவறான கூற்று (எனவே சரியான விடை). எந்தவொரு சூழ்நிலையிலும் மாநில சட்டமன்றங்களில் அரசியலமைப்பு திருத்த மசோதாவைத் தொடங்க முடியாது. இதை நாடாளுமன்றத்தின் இரு அவைகளில் மட்டுமே அறிமுகப்படுத்த முடியும்.",
    "Option A is correct because it identifies the incorrect statement.", "விருப்பம் A சரியானது, ஏனெனில் இது தவறான கூற்றை அடையாளம் காட்டுகிறது.",
    "Option B is a true statement.", "விருப்பம் B சரியான கூற்று.",
    "Option C is a true statement.", "விருப்பம் C சரியான கூற்று.",
    "Option D is a true statement.", "விருப்பம் D சரியான கூற்று.",
    "💡 TNPSC Tip: States cannot initiate amendment bills; their only role under Art 368 is to ratify federal amendment bills passed by Parliament.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: மாநிலங்களால் திருத்த மசோதாக்களைத் தொடங்க முடியாது; நாடாளுமன்றம் நிறைவேற்றும் கூட்டாட்சி மசோதாக்களுக்கு ஒப்புதல் மட்டுமே அளிக்க முடியும்.",
    "📖 Revision Fact: Initiation of Constitutional Amendment Bills is the exclusive monopoly of Parliament.",
    "📖 திருத்தல் செய்தி: அரசியலமைப்பு திருத்த மசோதாக்களைத் தொடங்குவது நாடாளுமன்றத்தின் பிரத்யேக அதிகாரமாகும்.",
    "Analyze", "High", ["PYQ Style", "Article 368 Procedure", "Initiation Monopoly"]
)

# Q77 - Ans: A
add_p4(
    "polity_amendments_gt_077", "Hard", "pyq",
    "[TNPSC Group 1 Standard] The 24th Constitutional Amendment Act, 1971 was passed primarily to nullify the effect of which Supreme Court judgment?",
    "[டிஎன்பிஎஸ்சி குரூப் 1 தரநிலை] 1971-ஆம் ஆண்டின் 24-வது அரசியலமைப்பு திருத்தச் சட்டம் முக்கியமாக எந்த உச்சநீதிமன்றத் தீர்ப்பின் விளைவை ரத்து செய்ய நிறைவேற்றப்பட்டது?",
    "Golaknath v. State of Punjab (1967)", "கோலக்நாத் எதிர் பஞ்சாப் மாநிலம் (1967)",
    "Shankari Prasad v. Union of India (1951)", "சங்கரி பிரசாத் எதிர் இந்திய ஒன்றியம் (1951)",
    "Kesavananda Bharati v. State of Kerala (1973)", "கேசவாநந்த பாரதி எதிர் கேரள மாநிலம் (1973)",
    "Minerva Mills v. Union of India (1980)", "மினெர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980)",
    "A",
    "📚 Core Explanation:\nThe 24th Constitutional Amendment Act, 1971 was enacted by Indira Gandhi government specifically to nullify the Supreme Court verdict in Golaknath Case (1967), which had held that Parliament cannot amend Fundamental Rights. The 24th Amendment amended Article 13 and Article 368 to restore Parliament's power to amend any Part of the Constitution.",
    "📚 முதன்மை விளக்கம்:\n1971-ஆம் ஆண்டின் 24-வது அரசியலமைப்பு திருத்தச் சட்டம், அடிப்படை உரிமைகளை நாடாளுமன்றம் திருத்த முடியாது என்று தீர்ப்பளித்த கோலக்நாத் வழக்கை (1967) ரத்து செய்வதற்காகவே இயற்றப்பட்டது.",
    "Option A is correct; 24th Amendment nullified Golaknath ruling.", "விருப்பம் A சரியானது.",
    "Option B is incorrect; Shankari Prasad upheld amending power.", "விருப்பம் B தவறானது.",
    "Option C is incorrect; Kesavananda Bharati came after 24th Amendment.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; Minerva Mills came in 1980.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 24th Amendment inserted Art 13(4) and Art 368(1), stating that Art 13 does not apply to Art 368 amendments.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 24-வது திருத்தம் சரத்து 13(4) மற்றும் 368(1)-ஐச் சேர்த்தது.",
    "📖 Revision Fact: Supreme Court in Kesavananda Bharati (1973) upheld the validity of 24th Amendment.",
    "📖 திருத்தல் செய்தி: கேசவாநந்த பாரதி வழக்கில் 24-வது திருத்தத்தின் செல்லுபடியாகும் தன்மை உறுதியளிக்கப்பட்டது.",
    "Remember", "High", ["PYQ Style", "24th Amendment", "Golaknath Case"]
)

# Q78 - Ans: A
add_p4(
    "polity_amendments_gt_078", "Medium", "pyq",
    "[TNPSC Group 1 Standard] The words 'Socialist', 'Secular', and 'Integrity' were added to the Preamble of the Indian Constitution by which Amendment Act?",
    "[டிஎன்பிஎஸ்சி குரூப் 1 தரநிலை] இந்திய அரசியலமைப்பின் முகப்புரையில் 'சமதர்ம', 'சமயச்சார்பற்ற', 'ஒருமைப்பாடு' என்ற வார்த்தைகள் எந்த திருத்தச் சட்டத்தின் மூலம் சேர்க்கப்பட்டன?",
    "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
    "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
    "1st Constitutional Amendment Act, 1951", "1-வது அரசியலமைப்பு திருத்தச் சட்டம், 1951",
    "73rd Constitutional Amendment Act, 1992", "73-வது அரசியலமைப்பு திருத்தச் சட்டம், 1992",
    "A",
    "📚 Core Explanation:\nThe Preamble of the Indian Constitution has been amended ONLY ONCE till date, by the 42nd Constitutional Amendment Act, 1976. It added three new words: 'Socialist', 'Secular', and 'Integrity' to the Preamble.",
    "📚 முதன்மை விளக்கம்:\nஇந்திய அரசியலமைப்பின் முகப்புரை இதுவரை ஒரே ஒரு முறை மட்டுமே திருத்தப்பட்டுள்ளது (1976-ன் 42-வது திருத்தச் சட்டம்). இது 'சமதர்ம', 'சமயச்சார்பற்ற', 'ஒருமைப்பாடு' ஆகிய மூன்று புதிய வார்த்தைகளைச் சேர்த்தது.",
    "Option A is correct; 42nd Amendment added the three words to Preamble.", "விருப்பம் A சரியானது.",
    "Option B is incorrect; 44th Amendment restored democratic rights.", "விருப்பம் B தவறானது.",
    "Option C is incorrect; 1st Amendment added 9th Schedule.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; 73rd Amendment related to Panchayati Raj.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Original description in Preamble was 'Sovereign Democratic Republic'; post-42nd Amendment it became 'Sovereign Socialist Secular Democratic Republic'.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 42-வது திருத்திற்குப் பின் முகப்புரை 'இறையாண்மை கொண்ட சமதர்ம சமயச்சார்பற்ற ஜனநாயகக் குடியரசு' என மாறியது.",
    "📖 Revision Fact: Kesavananda Bharati case (1973) held that Preamble is a part of the Constitution and can be amended under Article 368.",
    "📖 திருத்தல் செய்தி: முகப்புரை அரசியலமைப்பின் ஒரு பகுதி என்றும் அதை திருத்தலாம் என்றும் கேசவாநந்த பாரதி வழக்கு கூறியது.",
    "Remember", "High", ["PYQ Style", "Preamble Amendment", "42nd Amendment"]
)

# Q79 - Ans: A
add_p4(
    "polity_amendments_gt_079", "Medium", "pyq",
    "[TNPSC Group 1 Standard] The Right to Property ceased to be a Fundamental Right and became a legal right under Article 300A by virtue of which Constitutional Amendment?",
    "[டிஎன்பிஎஸ்சி குரூப் 1 தரநிலை] எந்த அரசியலமைப்பு திருத்தத்தின் மூலம் சொத்துரிமை அடிப்படை உரிமையிலிருந்து நீக்கப்பட்டு சரத்து 300A-ன் கீழ் சட்டப்பூர்வ உரிமையாக மாறியது?",
    "44th Constitutional Amendment Act, 1978", "44-வது அரசியலமைப்பு திருத்தச் சட்டம், 1978",
    "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
    "25th Constitutional Amendment Act, 1971", "25-வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
    "1st Constitutional Amendment Act, 1951", "1-வது அரசியலமைப்பு திருத்தச் சட்டம், 1951",
    "A",
    "📚 Core Explanation:\nThe 44th Constitutional Amendment Act, 1978 deleted the Right to Property from the list of Fundamental Rights (Articles 19(1)(f) and 31) and made it a constitutional/legal right under Article 300A in Part XII.",
    "📚 முதன்மை விளக்கம்:\n1978-ஆம் ஆண்டின் 44-வது அரசியலமைப்பு திருத்தச் சட்டம் சொத்துரிமையை அடிப்படை உரிமைகள் பட்டியலிலிருந்து (சரத்து 19(1)(f) மற்றும் 31) நீக்கி, பகுதி XII-ல் சரத்து 300A-ன் கீழ் சட்டப்பூர்வ உரிமையாக மாற்றியது.",
    "Option A is correct; 44th Amendment shifted Right to Property to Art 300A.", "விருப்பம் A சரியானது.",
    "Option B is incorrect; 42nd Amendment did not delete Right to Property.", "விருப்பம் B தவறானது.",
    "Option C is incorrect; 25th Amendment inserted Art 31C.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; 1st Amendment inserted Art 31A and 31B.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Right to Property is now a constitutional/legal right, NOT a fundamental right. It cannot be enforced directly under Art 32.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: சொத்துரிமை இப்போது ஒரு சட்டப்பூர்வ உரிமை மட்டுமே, அடிப்படை உரிமை அல்ல.",
    "📖 Revision Fact: Janata Party government under PM Morarji Desai enacted the 44th Amendment Act in 1978.",
    "📖 திருத்தல் செய்தி: பிரதமர் மொரார்ஜி தேசாய் தலைமையிலான ஜனதா கட்சி அரசு 44-வது திருத்தச் சட்டத்தை இயற்றியது.",
    "Remember", "High", ["PYQ Style", "Right to Property", "44th Amendment", "Article 300A"]
)

# Q80 - Ans: A
add_p4(
    "polity_amendments_gt_080", "Hard", "pyq",
    "[TNPSC Group 1 Standard] Under the 52nd Constitutional Amendment Act, 1985 (10th Schedule), who among the following is empowered to decide questions regarding disqualification of a member on grounds of defection?",
    "[டிஎன்பிஎஸ்சி குரூப் 1 தரநிலை] 1985-ஆம் ஆண்டின் 52-வது திருத்தச் சட்டத்தின் கீழ் (10-வது அட்டவணை), கட்சித் தாவல் காரணமாக ஒரு உறுப்பினரின் தகுதிநீக்கம் குறித்த கேள்விகளைத் தீர்மானிக்கும் அதிகாரம் பெற்றவர் யார்?",
    "Chairman or Speaker of the respective House", "சம்பந்தப்பட்ட அவையின் தலைவர் அல்லது சபாநாயகர்",
    "President of India on the advice of Election Commission", "தேர்தல் ஆணையத்தின் ஆலோசனையின் பேரில் இந்திய குடியரசுத் தலைவர்",
    "Supreme Court of India directly", "நேரடியாக இந்திய உச்சநீதிமன்றம்",
    "Governor of the concerned State", "சம்பந்தப்பட்ட மாநிலத்தின் ஆளுநர்",
    "A",
    "📚 Core Explanation:\nUnder Paragraph 6 of the 10th Schedule (inserted by 52nd Amendment Act 1985), any question regarding disqualification of a member on grounds of defection is decided by the Chairman (for Rajya Sabha/Legislative Council) or Speaker (for Lok Sabha/Legislative Assembly) of the House.",
    "📚 முதன்மை விளக்கம்:\n10-வது அட்டவணை பத்தி 6-ன் படி, கட்சித் தாவல் காரணமாக தகுதிநீக்கம் தொடர்பான கேள்விகளை அவையின் தலைவர் அல்லது சபாநாயகர் தீர்மானிக்கிறார்.",
    "Option A is correct; Speaker/Chairman decides defection disqualifications.", "விருப்பம் A சரியானது.",
    "Option B is incorrect; President decides Art 102(1) disqualifications (other grounds) on EC advice.", "விருப்பம் B தவறானது.",
    "Option C is incorrect; SC exercises judicial review post Speaker's decision.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; Governor decides Art 192 disqualifications on EC advice.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Distinguish: General disqualifications (Art 102/192) are decided by President/Governor on EC advice; Defection disqualifications (10th Schedule) are decided by Speaker/Chairman.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: பொதுவான தகுதிநீக்கங்களை தேர்தல் ஆணைய ஆலோசனையின் பேரில் குடியரசுத் தலைவர்/ஆளுநர் தீர்மானிக்கிறார்; கட்சித் தாவல் தகுதிநீக்கத்தை சபாநாயகர்/தலைவர் தீர்மானிக்கிறார்.",
    "📖 Revision Fact: In Kihoto Hollohan v. Zachillhu (1992), SC held that Speaker's decision under 10th Schedule is subject to judicial review.",
    "📖 திருத்தல் செய்தி: கிஹோட்டோ ஹோல்லோஹன் வழக்கில் (1992) சபாநாயகரின் தகுதிநீக்க முடிவு நீதிமன்ற ஆய்வுக்கு உட்பட்டது எனத் தீர்ப்பளிக்கப்பட்டது.",
    "Analyze", "High", ["PYQ Style", "52nd Amendment", "10th Schedule", "Speaker Power"]
)

# Q81 - Ans: B
add_p4(
    "polity_amendments_gt_081", "Medium", "pyq",
    "[TNPSC Group 1 Standard] The voting age in India was reduced from 21 years to 18 years under the Prime Ministership of whom, through the 61st Constitutional Amendment Act?",
    "[டிஎன்பிஎஸ்சி குரூப் 1 தரநிலை] 61-வது அரசியலமைப்பு திருத்தச் சட்டத்தின் மூலம் யாருடைய பிரதமரின் கீழ் இந்தியாவில் வாக்குரிமை வயது 21-லிருந்து 18 ஆகக் குறைக்கப்பட்டது?",
    "Indira Gandhi", "இந்திரா காந்தி",
    "Rajiv Gandhi", "ராஜீவ் காந்தி",
    "V.P. Singh", "வி.பி. சிங்",
    "P.V. Narasimha Rao", "பி.வி. நரசிம்ம ராவ்",
    "B",
    "📚 Core Explanation:\nThe 61st Constitutional Amendment Act, 1988 was enacted under the Prime Ministership of Rajiv Gandhi. It amended Article 326 to lower the voting age from 21 to 18 years to encourage youth participation in democracy.",
    "📚 முதன்மை விளக்கம்:\n1988-ஆம் ஆண்டின் 61-வது அரசியலமைப்பு திருத்தச் சட்டம் பிரதமர் ராஜீவ் காந்தி ஆட்சிக்காலத்தில் இயற்றப்பட்டது. இது இளைஞர்களின் ஜனநாயகப் பங்களிப்பை ஊக்குவிக்க வாக்குரிமை வயதை 21-லிருந்து 18 ஆகக் குறைக்க சரத்து 326-ஐத் திருத்தியது.",
    "Option A is incorrect; Indira Gandhi was PM during 42nd Amendment.", "விருப்பம் A தவறானது.",
    "Option B is correct; Rajiv Gandhi was PM during 61st Amendment.", "விருப்பம் B சரியானது.",
    "Option C is incorrect; V.P. Singh was PM during 1989-90.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; Narasimha Rao was PM during 73rd and 74th Amendments.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 61st Amendment Act was enacted in 1988 and came into force on March 28, 1989.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 61-வது திருத்தச் சட்டம் 1988-ல் இயற்றப்பட்டு மார்ச் 28, 1989 அன்று அமலுக்கு வந்தது.",
    "📖 Revision Fact: Following the 61st Amendment, Election Commission was made a multi-member body in October 1989.",
    "📖 திருத்தல் செய்தி: 61-வது திருத்தத்தைத் தொடர்ந்து அக்டோபர் 1989-ல் தேர்தல் ஆணையம் பல உறுப்பினர்களைக் கொண்ட அமைப்பாக மாற்றப்பட்டது.",
    "Remember", "High", ["PYQ Style", "61st Amendment", "Rajiv Gandhi", "Voting Age"]
)

# Q82 - Ans: B
add_p4(
    "polity_amendments_gt_082", "Hard", "pyq",
    "[TNPSC Group 1 Standard] Which of the following statements regarding the 73rd Constitutional Amendment Act, 1992 is INCORRECT?",
    "[டிஎன்பிஎஸ்சி குரூப் 1 தரநிலை] 1992-ஆம் ஆண்டின் 73-வது அரசியலமைப்பு திருத்தச் சட்டம் குறித்த பின்வரும் கூற்றுகளில் எது தவறானது?",
    "It added the 11th Schedule containing 29 functional items.", "இது 29 செயல்பாட்டுத் தலைப்புகளைக் கொண்ட 11-வது அட்டவணையைச் சேர்த்தது.",
    "The 3-tier Panchayati Raj system is mandatory for ALL states regardless of population.", "மக்கள் தொகையைப் பொருட்படுத்தாமல் அனைத்து மாநிலங்களுக்கும் 3-அடுக்கு பஞ்சாயத்து முறை கட்டாயமாகும்.",
    "It provided for a State Election Commission to conduct elections to Panchayats (Article 243K).", "பஞ்சாயத்துத் தேர்தல்களை நடத்த மாநில தேர்தல் ஆணையத்திற்கு இது வகைசெய்தது (சரத்து 243K).",
    "It provided for a State Finance Commission to review financial position of Panchayats every 5 years (Article 243I).", "பஞ்சாயத்துகளின் நிதி நிலையை ஒவ்வொரு 5 ஆண்டுகளுக்கும் திறனாய்வு செய்ய மாநில நிதி ஆணையத்திற்கு இது வகைசெய்தது (சரத்து 243I).",
    "B",
    "📚 Core Explanation:\nOption B is INCORRECT (hence correct choice). A state having a population NOT exceeding 20 lakhs may NOT constitute Panchayats at the intermediate level (Article 243B(2)). Thus, the 3-tier system is NOT mandatory for states with population below 20 lakhs. Options A, C, and D are all correct features.",
    "📚 முதன்மை விளக்கம்:\nவிருப்பம் B தவறான கூற்று (எனவே சரியான விடை). 20 லட்சத்திற்கு மிகாமல் மக்கள் தொகை கொண்ட மாநிலங்களுக்கு இடைநிலை அடுக்கில் (Panchayat Samiti) பஞ்சாயத்து அமைப்பது கட்டாயமில்லை (சரத்து 243B(2)).",
    "Option A is a true statement.", "விருப்பம் A சரியான கூற்று.",
    "Option B is incorrect because 3-tier system is not mandatory for states with population under 20 lakhs.", "விருப்பம் B தவறான கூற்று.",
    "Option C is a true statement.", "விருப்பம் C சரியான கூற்று.",
    "Option D is a true statement.", "விருப்பம் D சரியான கூற்று.",
    "💡 TNPSC Tip: Exception rule: 20 lakh population threshold for intermediate level panchayats under Art 243B(2).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: இடைநிலை பஞ்சாயத்து இல்லாதிருக்க 20 லட்சம் மக்கள் தொகை வரம்பு விதிவிலக்கு உள்ளது.",
    "📖 Revision Fact: 73rd Amendment does not apply to Nagaland, Meghalaya, Mizoram, and certain tribal areas.",
    "📖 திருத்தல் செய்தி: 73-வது திருத்தம் நாகாலாந்து, மேகாயா, மிசோரம் மற்றும் சில பழங்குடியினப் பகுதிகளுக்குப் பொருந்தாது.",
    "Analyze", "High", ["PYQ Style", "73rd Amendment", "Panchayati Raj Exception"]
)

# Q83 - Ans: B
add_p4(
    "polity_amendments_gt_083", "Medium", "pyq",
    "[TNPSC Group 1 Standard] The 86th Constitutional Amendment Act, 2002 inserted which clause under Article 51A to add the 11th Fundamental Duty?",
    "[டிஎன்பிஎஸ்சி குரூப் 1 தரநிலை] 11-வது அடிப்படைக் கடமையைச் சேர்க்க 2002-ஆம் ஆண்டின் 86-வது அரசியலமைப்பு திருத்தச் சட்டம் சரத்து 51A-ன் கீழ் எந்தப் பிரிவைச் சேர்த்தது?",
    "Article 51A(j)", "சரத்து 51A(j)",
    "Article 51A(k)", "சரத்து 51A(k)",
    "Article 51A(i)", "சரத்து 51A(i)",
    "Article 51A(h)", "சரத்து 51A(h)",
    "B",
    "📚 Core Explanation:\nThe 86th Constitutional Amendment Act, 2002 added clause (k) to Article 51A in Part IV-A of the Constitution. It states that it shall be the duty of every citizen who is a parent or guardian to provide opportunities for education to his child aged between 6 and 14 years.",
    "📚 முதன்மை விளக்கம்:\n2002-ஆம் ஆண்டின் 86-வது அரசியலமைப்பு திருத்தச் சட்டம் பகுதி IV-A-ல் சரத்து 51A(k) பிரிவைச் சேர்த்தது. இது 6-14 வயதுடைய குழந்தைகளுக்கு கல்வி வாய்ப்புகளை வழங்குவதை பெற்றோரின் கடமையாக்கியது.",
    "Option A is incorrect; Art 51A(j) deals with striving towards excellence.", "விருப்பம் A தவறானது.",
    "Option B is correct; Art 51A(k) is the 11th Fundamental Duty.", "விருப்பம் B சரியானது.",
    "Option C is incorrect; Art 51A(i) deals with safeguarding public property.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; Art 51A(h) deals with developing scientific temper.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: 42nd Amendment (1976) added 10 duties (51A(a) to 51A(j)); 86th Amendment (2002) added the 11th duty (51A(k)).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 42-வது திருத்தம் 10 கடமைகளைச் சேர்த்தது; 86-வது திருத்தம் 11-வது கடமையைச் (51A(k)) சேர்த்தது.",
    "📖 Revision Fact: Total Fundamental Duties under Article 51A present today is 11.",
    "📖 திருத்தல் செய்தி: தற்போது சரத்து 51A-ன் கீழ் உள்ள மொத்த அடிப்படைக் கடமைகள் 11 ஆகும்.",
    "Remember", "High", ["PYQ Style", "86th Amendment", "Article 51A(k)"]
)

# Q84 - Ans: B
add_p4(
    "polity_amendments_gt_084", "Hard", "pyq",
    "[TNPSC Group 1 Standard] Article 279A, inserted by the 101st Constitutional Amendment Act, 2016, provides for the constitution of which of the following bodies?",
    "[டிஎன்பிஎஸ்சி குரூப் 1 தரநிலை] 2016-ஆம் ஆண்டின் 101-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட சரத்து 279A பின்வரும் எந்த அமைப்பை அமைக்க வகைசெய்கிறது?",
    "Finance Commission of India", "இந்திய நிதி ஆணையம்",
    "Goods and Services Tax (GST) Council", "சரக்கு மற்றும் சேவை வரி (GST) கவுன்சில்",
    "Inter-State Council", "மாநிலங்களுக்கு இடையேயான கவுன்சில்",
    "National Development Council", "தேசிய வளர்ச்சி கவுன்சில்",
    "B",
    "📚 Core Explanation:\nArticle 279A was inserted by the 101st Constitutional Amendment Act, 2016 empowering the President to constitute the Goods and Services Tax (GST) Council within 60 days. The GST Council is a joint forum of Centre and States chaired by Union Finance Minister.",
    "📚 முதன்மை விளக்கம்:\n2016-ஆம் ஆண்டின் 101-வது அரசியலமைப்பு திருத்தச் சட்டத்தால் சேர்க்கப்பட்ட சரத்து 279A, மத்திய நிதி அமைச்சர் தலைமையில் ஜிஎஸ்டி (GST) கவுன்சிலை அமைக்க குடியரசுத் தலைவருக்கு அதிகாரம் அளிக்கிறது.",
    "Option A is incorrect; Finance Commission is constituted under Article 280.", "விருப்பம் A தவறானது.",
    "Option B is correct; Article 279A constituted the GST Council.", "விருப்பம் B சரியானது.",
    "Option C is incorrect; Inter-State Council is constituted under Article 263.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; National Development Council was an executive body.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: GST Council is a constitutional body under Art 279A. Its decisions are taken by a 3/4th weighted majority.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: ஜிஎஸ்டி கவுன்சில் சரத்து 279A-ன் கீழ் உள்ள அரசியலமைப்பு அமைப்பாகும்.",
    "📖 Revision Fact: Union Finance Minister is the ex-officio Chairperson of the GST Council.",
    "📖 திருத்தல் செய்தி: மத்திய நிதி அமைச்சர் ஜிஎஸ்டி கவுன்சிலின் பதவி வழித் தலைவர் ஆவார்.",
    "Remember", "High", ["PYQ Style", "101st Amendment", "GST Council", "Article 279A"]
)

# Q85 - Ans: B
add_p4(
    "polity_amendments_gt_085", "Hard", "pyq",
    "[TNPSC Group 1 Standard] Which landmark Supreme Court case laid down the doctrine that any law included in the Ninth Schedule after April 24, 1973 would be open to judicial review if it violates the Basic Structure?",
    "[டிஎன்பிஎஸ்சி குரூப் 1 தரநிலை] ஏப்ரல் 24, 1973-க்குப் பிறகு 9-வது அட்டவணையில் சேர்க்கப்படும் எந்தவொரு சட்டமும் அடிப்படை கட்டமைப்பை மீறினால் நீதிமன்ற ஆய்வுக்கு உட்பட்டது என்ற கோட்பாட்டை வகுத்த உச்சநீதிமன்ற வழக்கு எது?",
    "Minerva Mills v. Union of India (1980)", "மினெர்வா மில்ஸ் எதிர் இந்திய ஒன்றியம் (1980)",
    "I.R. Coelho v. State of Tamil Nadu (2007)", "ஐ.ஆர். கோயல்ஹோ எதிர் தமிழ்நாடு மாநிலம் (2007)",
    "L. Chandra Kumar v. Union of India (1997)", "எல். சந்திர குமார் எதிர் இந்திய ஒன்றியம் (1997)",
    "Indira Sawhney v. Union of India (1992)", "இந்திரா சாவ்னி எதிர் இந்திய ஒன்றியம் (1992)",
    "B",
    "📚 Core Explanation:\nIn I.R. Coelho v. State of Tamil Nadu (2007), a unanimous 9-judge Constitution bench held that Ninth Schedule laws added after April 24, 1973 do not enjoy immunity and can be struck down if they violate basic structure rights guaranteed under Articles 14, 19, and 21.",
    "📚 முதன்மை விளக்கம்:\n2007 ஐ.ஆர். கோயல்ஹோ எதிர் தமிழ்நாடு மாநில வழக்கில், 9 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு ஏப்ரல் 24, 1973-க்குப் பிறகு 9-வது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்கள் அடிப்படை உரிமைகளை மீறினால் நீதிமன்ற ஆய்வுக்கு உட்பட்டவை என தீர்ப்பளித்தது.",
    "Option A is incorrect; Minerva Mills (1980) struck down Art 368(4)&(5).", "விருப்பம் A தவறானது.",
    "Option B is correct; I.R. Coelho (2007) established Ninth Schedule judicial review post-1973.", "விருப்பம் B சரியானது.",
    "Option C is incorrect; L. Chandra Kumar (1997) dealt with tribunals.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; Indira Sawhney (1992) dealt with OBC reservation 50% cap.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Tamil Nadu's 69% Reservation Act 1994 (placed in 9th Schedule by 76th Amendment) is being challenged under the I.R. Coelho principles.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: தமிழ்நாட்டின் 69% இடஒதுக்கீட்டுச் சட்டம் 1994 (76-வது திருத்தம்) ஐ.ஆர். கோயல்ஹோ தீர்ப்பின் கீழ் சவால் செய்யப்பட்டுள்ளது.",
    "📖 Revision Fact: I.R. Coelho case is also known as the Ninth Schedule Case.",
    "📖 திருத்தல் செய்தி: ஐ.ஆர். கோயல்ஹோ வழக்கு 9-வது அட்டவணை வழக்கு என அழைக்கப்படுகிறது.",
    "Analyze", "High", ["PYQ Style", "IR Coelho Case", "Ninth Schedule", "Tamil Nadu 69 Percent"]
)

# Q86 - Ans: C
add_p4(
    "polity_amendments_gt_086", "Medium", "chronology",
    "Arrange the following recent Constitutional Amendment Acts in correct chronological order of their enactment:\n1. 101st Amendment (GST)\n2. 103rd Amendment (EWS Reservation)\n3. 104th Amendment (SC/ST Reservation Extension & Anglo-Indian Removal)\n4. 106th Amendment (Women's Reservation)\nSelect the correct code:",
    "அண்மைய அரசியலமைப்பு திருத்தச் சட்டங்களை இயற்றப்பட்ட சரியான காலவரிசைப்படி அமைக்கவும்:\n1. 101-வது திருத்தம் (ஜிஎஸ்டி)\n2. 103-வது திருத்தம் (EWS இடஒதுக்கீடு)\n3. 104-வது திருத்தம் (SC/ST நீட்டிப்பு & ஆங்கிலோ-இந்தியர் நீக்கம்)\n4. 106-வது திருத்தம் (மகளிர் இடஒதுக்கீடு)\nசரியான குறியீட்டைத் தேர்ந்தெடுக்கவும்:",
    "2 - 1 - 3 - 4", "2 - 1 - 3 - 4",
    "1 - 3 - 2 - 4", "1 - 3 - 2 - 4",
    "1 - 2 - 3 - 4", "1 - 2 - 3 - 4",
    "3 - 1 - 2 - 4", "3 - 1 - 2 - 4",
    "C",
    "📚 Core Explanation:\n- 101st Amendment Act: 2016 (GST).\n- 103rd Amendment Act: 2019 (10% EWS Reservation).\n- 104th Amendment Act: 2020 (SC/ST extension & Anglo-Indian nomination discontinuation).\n- 106th Amendment Act: 2023 (Nari Shakti Vandan Adhiniyam).\nHence, correct order is 1 - 2 - 3 - 4.",
    "📚 முதன்மை விளக்கம்:\n- 101-வது திருத்தம்: 2016 (GST).\n- 103-வது திருத்தம்: 2019 (EWS இடஒதுக்கீடு).\n- 104-வது திருத்தம்: 2020 (SC/ST நீட்டிப்பு).\n- 106-வது திருத்தம்: 2023 (மகளிர் இடஒதுக்கீடு).\nசரியான காலவரிசை 1 - 2 - 3 - 4.",
    "Option A is incorrect.", "விருப்பம் A தவறானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is correct as 1 (2016) -> 2 (2019) -> 3 (2020) -> 4 (2023).", "விருப்பம் C சரியானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Chronology: 101st (GST 2016) -> 102nd (NCBC 2018) -> 103rd (EWS 2019) -> 104th (SC/ST 2020) -> 105th (State OBC 2021) -> 106th (Women 2023).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: திருத்தங்களின் காலவரிசை: 101 (2016) -> 102 (2018) -> 103 (2019) -> 104 (2020) -> 105 (2021) -> 106 (2023).",
    "📖 Revision Fact: 105th Amendment Act was enacted in August 2021.",
    "📖 திருத்தல் செய்தி: 105-வது திருத்தச் சட்டம் ஆகஸ்ட் 2021-ல் இயற்றப்பட்டது.",
    "Apply", "High", ["Chronology", "Recent Amendments", "101st to 106th"]
)

# Q87 - Ans: C
add_p4(
    "polity_amendments_gt_087", "Hard", "statement",
    "Consider the following statements regarding the three amendment methods under the Indian Constitution:\n1. Amendments by Simple Majority are explicitly outside the scope of Article 368.\n2. Amendments under Article 368 by Special Majority require more than 50% of total membership of each House AND at least 2/3rd of members present and voting.\n3. Amendments affecting federal provisions require Special Majority of Parliament AND ratification by at least half of the State Assemblies by a Special Majority.\nWhich of the statements given above is/are correct?",
    "இந்திய அரசியலமைப்பின் மூன்று திருத்தும் முறைகள் குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. எளிய பெரும்பான்மை மூலம் செய்யப்படும் திருத்தங்கள் சரத்து 368-ன் வரம்பிற்கு வெளியே அமைபவை.\n2. சரத்து 368-ன் கீழ் சிறப்பு பெரும்பான்மை திருத்தங்களுக்கு ஒவ்வொரு அவையின் 50%-க்கும் அதிகமான உறுப்பினர்கள் மற்றும் வந்து வாக்களிக்கும் உறுப்பினர்களில் 2/3 பங்கு பெரும்பான்மை தேவை.\n3. கூட்டாட்சி விதிகளைப் பாதிக்கும் திருத்தங்களுக்கு நாடாளுமன்றத்தின் சிறப்பு பெரும்பான்மையுடன் பாதியளவு மாநில சட்டமன்றங்களின் சிறப்பு பெரும்பான்மை ஒப்புதலும் தேவை.\nமேற்கூறிய கூற்றுகளில் எது/எவை சரியானது?",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "C",
    "📚 Core Explanation:\nStatements 1 and 2 are CORRECT.\nStatement 3 is INCORRECT: State ratification of federal amendment bills requires only a SIMPLE MAJORITY (majority of members present and voting) in state legislatures, NOT a special majority.",
    "📚 முதன்மை விளக்கம்:\nகூற்றுகள் 1 மற்றும் 2 சரி.\nகூற்று 3 தவறு: மாநில சட்டமன்றங்களில் கூட்டாட்சி மசோதாக்களுக்கு ஒப்புதல் அளிக்க எளிய பெரும்பான்மை மட்டுமே போதுமானது; சிறப்பு பெரும்பான்மை தேவையில்லை.",
    "Option A is incorrect because 3 is false.", "விருப்பம் A தவறானது.",
    "Option B is incorrect because 3 is false.", "விருப்பம் B தவறானது.",
    "Option C is correct as statements 1 and 2 are true while 3 is false.", "விருப்பம் C சரியானது.",
    "Option D is incorrect because 3 is false.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Exam Trap: Parliament requires SPECIAL majority under Art 368, but State Assemblies require only SIMPLE majority for ratification.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: தேர்வு பொறி: நாடாளுமன்றத்திற்கு சிறப்பு பெரும்பான்மை தேவை, ஆனால் மாநில சட்டமன்றங்களின் ஒப்புதலுக்கு எளிய பெரும்பான்மையே போதுமானது.",
    "📖 Revision Fact: No time limit is fixed for states to pass ratification resolutions.",
    "📖 திருத்தல் செய்தி: மாநில ஒப்புதல் தீர்மானத்திற்கு அரசியலமைப்பில் காலக்கெடு எதுவுமில்லை.",
    "Analyze", "High", ["Amendment Methods", "Simple vs Special Majority", "State Ratification Trap"]
)

# Q88 - Ans: C
add_p4(
    "polity_amendments_gt_088", "Medium", "match_the_following",
    "Match List-I (Constitutional Subject) with List-II (Amendment Method Required) and select the correct code:\nList-I:\nA. Admission of new States (Article 2)\nB. Directive Principles of State Policy (Part IV)\nC. Election of the President (Articles 54 & 55)\nD. Abolition of Legislative Council (Article 169)\nList-II:\n1. Simple Majority of Parliament outside Article 368\n2. Special Majority of Parliament under Article 368\n3. Special Majority of Parliament + Ratification by half of States\n4. Simple Majority of Parliament outside Article 368",
    "பட்டியல்-I (அரசியலமைப்புத் தலைப்பு) பட்டியல்-II (தேவைப்படும் திருத்தும் முறை) உடன் பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்க:\nபட்டியல்-I:\nA. புதிய மாநிலங்களைச் சேர்ப்பது (சரத்து 2)\nB. அரசு நெறிமுறைக் கோட்பாடுகள் (பகுதி IV)\nC. குடியரசுத் தலைவர் தேர்தல் (சரத்து 54 & 55)\nD. சட்ட மேலவையை ஒழித்தல் (சரத்து 169)\nபட்டியல்-II:\n1. சரத்து 368-க்கு வெளியே நாடாளுமன்றத்தின் எளிய பெரும்பான்மை\n2. சரத்து 368-ன் கீழ் நாடாளுமன்றத்தின் சிறப்பு பெரும்பான்மை\n3. நாடாளுமன்ற சிறப்பு பெரும்பான்மை + பாதியளவு மாநிலங்களின் ஒப்புதல்\n4. சரத்து 368-க்கு வெளியே நாடாளுமன்றத்தின் எளிய பெரும்பான்மை",
    "A-1, B-3, C-2, D-4", "A-1, B-3, C-2, D-4",
    "A-2, B-1, C-3, D-4", "A-2, B-1, C-3, D-4",
    "A-1, B-2, C-3, D-4", "A-1, B-2, C-3, D-4",
    "A-3, B-2, C-1, D-4", "A-3, B-2, C-1, D-4",
    "C",
    "📚 Core Explanation:\n- Admission of new states (Art 2) = Simple Majority (A-1).\n- DPSP (Part IV) = Special Majority of Parliament alone (B-2).\n- Election of President (Art 54, 55) = Special Majority + State Ratification (C-3).\n- Abolition of Legislative Council (Art 169) = Simple Majority (D-4).\nCorrect match: A-1, B-2, C-3, D-4.",
    "📚 முதன்மை விளக்கம்:\n- புதிய மாநிலங்கள் (சரத்து 2) = எளிய பெரும்பான்மை (A-1).\n- DPSP (பகுதி IV) = சிறப்பு பெரும்பான்மை (B-2).\n- குடியரசுத் தலைவர் தேர்தல் = சிறப்பு பெரும்பான்மை + மாநில ஒப்புதல் (C-3).\n- சட்ட மேலவை ஒழிப்பு (சரத்து 169) = எளிய பெரும்பான்மை (D-4).",
    "Option A is incorrect.", "விருப்பம் A தவறானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is correct as all matches align accurately.", "விருப்பம் C சரியானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Simple Majority subjects are listed outside Article 368 (Art 2, 3, 4, 169, 5th/6th Schedule).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: எளிய பெரும்பான்மை விஷயங்கள் சரத்து 368-க்கு வெளியே பட்டியலிடப்பட்டுள்ளன.",
    "📖 Revision Fact: Amendments under Art 2 & 3 do not require procedure under Art 368.",
    "📖 திருத்தல் செய்தி: சரத்து 2 & 3 திருத்தங்களுக்கு சரத்து 368 நடைமுறை தேவையில்லை.",
    "Understand", "High", ["Match the Following", "Amendment Methods", "Article 2", "President Election"]
)

# Q89 - Ans: C
add_p4(
    "polity_amendments_gt_089", "Hard", "reasoning",
    "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): State Legislatures in India do NOT possess the power to initiate any bill or proposal for amending the Constitution.\nReason (R): The Indian Constitution vests the exclusive monopoly of initiating constitutional amendments in the Parliament of India.\nIn light of the above statements, choose the correct option:",
    "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளது:\nகூற்று (A): இந்தியாவில் மாநில சட்டமன்றங்களுக்கு அரசியலமைப்பைத் திருத்துவதற்கான எந்தவொரு மசோதா அல்லது முன்மொழிவைத் தொடங்கும் அதிகாரம் இல்லை.\nகாரணம் (R): இந்திய அரசியலமைப்புத் திருத்தங்களைத் தொடங்கும் பிரத்யேக ஏகபோக அதிகாரத்தை இந்திய நாடாளுமன்றத்திற்கு வழங்கியுள்ளது.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் சரியான விருப்பத்தைத் தேர்ந்தெடுக்கவும்:",
    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
    "(A) is true but (R) is false", "(A) உண்மை ஆனால் (R) தவறு",
    "Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை மற்றும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்",
    "(A) is false but (R) is true", "(A) தவறு ஆனால் (R) உண்மை",
    "C",
    "📚 Core Explanation:\nBoth Assertion (A) and Reason (R) are TRUE, and (R) is the correct explanation of (A). Unlike the US Constitution where states can initiate amendments (via Constitutional Convention), in India only Parliament can initiate a Constitutional Amendment Bill (Article 368). The only exception is state assemblies passing resolution for creation/abolition of legislative council under Art 169, but the bill itself is passed by Parliament.",
    "📚 முதன்மை விளக்கம்:\n(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-ன் சரியான விளக்கம். அமெரிக்கா போலல்லாமல் இந்தியாவில் மாநில சட்டமன்றங்களால் அரசியலமைப்பு திருத்த மசோதாவைத் தொடங்க முடியாது. நாடாளுமன்றத்திற்கு மட்டுமே அந்த அதிகாரம் உண்டு.",
    "Option A is incorrect because R explains A.", "விருப்பம் A தவறானது.",
    "Option B is incorrect because R is true.", "விருப்பம் B தவறானது.",
    "Option C is correct as both A and R are true and R explains A.", "விருப்பம் C சரியானது.",
    "Option D is incorrect because A is true.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Single exception: State Legislative Assembly can pass a resolution requesting Parliament to create or abolish Legislative Council (Art 169).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: ஒரே ஒரு விலக்கு: சரத்து 169-ன் கீழ் சட்ட மேலவையை உருவாக்க/ஒழிக்க மாநில சட்டமன்றம் தீர்மானம் இயற்றலாம்.",
    "📖 Revision Fact: In USA, 2/3rd of state legislatures can apply to Congress to call a convention for proposing amendments.",
    "📖 திருத்தல் செய்தி: அமெரிக்காவில் 2/3 பங்கு மாநிலங்கள் அரசியலமைப்பு திருத்த மாநாட்டைக் கூட்ட விண்ணப்பிக்கலாம்.",
    "Analyze", "High", ["Initiation Monopoly", "Parliament vs State Assembly", "Article 368"]
)

# Q90 - Ans: C
add_p4(
    "polity_amendments_gt_090", "Hard", "statement",
    "Consider the following statements regarding the limits on Parliament's Amending Power:\n1. Parliament has constituent power under Article 368, but this power is not absolute and cannot alter the Basic Structure of the Constitution.\n2. Fundamental Rights forming part of the Basic Structure (such as Article 14, 19, 21) cannot be destroyed by a Constitutional Amendment Act.\n3. Judicial Review is itself a part of the Basic Structure and cannot be abolished by amending Article 368.\nWhich of the statements given above are correct?",
    "நாடாளுமன்றத்தின் திருத்தும் அதிகாரத்திற்கான வரம்புகள் குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. சரத்து 368-ன் கீழ் நாடாளுமன்றத்திற்கு அரசியலமைப்பு ஆக்கல் அதிகாரம் உண்டு, ஆனால் இந்த அதிகாரம் வரம்பற்றதல்ல; அரசியலமைப்பின் அடிப்படை கட்டமைப்பை மாற்ற முடியாது.\n2. அடிப்படை கட்டமைப்பின் பகுதியாக உள்ள அடிப்படை உரிமைகளை (சரத்து 14, 19, 21 போன்றவை) அரசியலமைப்பு திருத்தச் சட்டத்தால் அழிக்க முடியாது.\n3. நீதிமன்ற ஆய்வே அடிப்படை கட்டமைப்பின் ஒரு பகுதியாகும்; சரத்து 368-ஐத் திருத்துவதன் மூலம் அதை ஒழிக்க முடியாது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "C",
    "📚 Core Explanation:\nAll three statements are CORRECT regarding the constitutional limits placed on Parliament's amending power by the Supreme Court through Kesavananda Bharati (1973), Minerva Mills (1980), and L. Chandra Kumar (1997) judgments.",
    "📚 முதன்மை விளக்கம்:\nநாடாளுமன்றத்தின் திருத்தும் அதிகாரத்திற்கான வரம்புகள் குறித்த மூன்று கூற்றுகளும் சரியானவை: கேசவாநந்த பாரதி (1973), மினெர்வா மில்ஸ் (1980), எல். சந்திர குமார் (1997) தீர்ப்புகள் மூலம் இது உறுதியளிக்கப்பட்டுள்ளது.",
    "Option A is incomplete.", "விருப்பம் A அரைகுறையானது.",
    "Option B is incomplete.", "விருப்பம் B அரைகுறையானது.",
    "Option C is correct as statements 1, 2, and 3 are all true.", "விருப்பம் C சரியானது.",
    "Option D is incomplete.", "விருப்பம் D அரைகுறையானது.",
    "💡 TNPSC Tip: Parliament's power under Art 368 is to AMEND (modify/refine) the Constitution, NOT to RE-WRITE or DESTROY it.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: நாடாளுமன்றத்தின் அதிகாரம் அரசியலமைப்பை திருத்துவதற்குத்தானே தவிர, அதை மாற்றி எழுதுவதற்கோ அல்லது அழிப்பதற்கோ அல்ல.",
    "📖 Revision Fact: Limited amending power is itself a basic feature (Minerva Mills 1980).",
    "📖 திருத்தல் செய்தி: வரம்பிற்குட்பட்ட திருத்தும் அதிகாரமே ஒரு அடிப்படை அம்சம் ஆகும்.",
    "Analyze", "High", ["Limits on Amending Power", "Basic Structure", "Judicial Review"]
)

# Q91 - Ans: D
add_p4(
    "polity_amendments_gt_091", "Medium", "single_choice",
    "Which Constitutional Amendment Act conferred the status of an 'Associate State' of India on Sikkim by adding a new 10th Schedule (which was later repealed by the 36th Amendment Act)?",
    "புதிய 10-வது அட்டவணையைச் சேர்த்து சிக்கிமுக்கு இந்தியாவின் 'இணை மாநிலம்' (Associate State) என்ற அந்தஸ்தை வழங்கிய திருத்தச் சட்டம் எது (பின்னர் 36-வது திருத்தத்தால் நீக்கப்பட்டது)?",
    "31st Constitutional Amendment Act, 1972", "31-வது அரசியலமைப்பு திருத்தச் சட்டம், 1972",
    "34th Constitutional Amendment Act, 1974", "34-வது அரசியலமைப்பு திருத்தச் சட்டம், 1974",
    "38th Constitutional Amendment Act, 1975", "38-வது அரசியலமைப்பு திருத்தச் சட்டம், 1975",
    "35th Constitutional Amendment Act, 1974", "35-வது அரசியலமைப்பு திருத்தச் சட்டம், 1974",
    "D",
    "📚 Core Explanation:\nThe 35th Constitutional Amendment Act, 1974 introduced a unique status of 'Associate State' for Sikkim and added the 10th Schedule detailing terms of association. Shortly after, the 36th Amendment Act, 1975 made Sikkim a full-fledged 22nd state and omitted the 10th Schedule (later reused for Anti-Defection).",
    "📚 முதன்மை விளக்கம்:\n1974-ஆம் ஆண்டின் 35-வது அரசியலமைப்பு திருத்தச் சட்டம் சிக்கிமுக்கு 'இணை மாநிலம்' என்ற தனித்துவமான அந்தஸ்தை வழங்கி 10-வது அட்டவணையைச் சேர்த்தது. பின்னர் 36-வது திருத்தச் சட்டம் (1975) சிக்கிமை முழு மாநிலமாக்கியது.",
    "Option A is incorrect; 31st Amendment increased Lok Sabha strength from 525 to 545.", "விருப்பம் A தவறானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is incorrect.", "விருப்பம் C தவறானது.",
    "Option D is correct; 35th Amendment made Sikkim an Associate State.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: Remember Sikkim sequence: 35th Amendment (1974) = Associate State; 36th Amendment (1975) = 22nd Full State.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: சிக்கிம் வரிசை: 35-வது (1974) = இணை மாநிலம்; 36-வது (1975) = 22-வது முழு மாநிலம்.",
    "📖 Revision Fact: 10th Schedule originally introduced for Sikkim was omitted by 36th Amendment and recreated in 1985 by 52nd Amendment for Anti-Defection.",
    "📖 திருத்தல் செய்தி: 10-வது அட்டவணை முதலில் சிக்கிமிற்காகச் சேர்க்கப்பட்டு பின்னர் கட்சித் தாவல் தடைச் சட்டத்திற்காக 1985-ல் மீண்டும் பயன்படுத்தப்பட்டது.",
    "Remember", "High", ["35th Amendment", "Sikkim Associate State", "36th Amendment"]
)

# Q92 - Ans: A
add_p4(
    "polity_amendments_gt_092", "Easy", "single_choice",
    "Which Constitutional Amendment Act created the State of Nagaland and introduced special provisions under Article 371A to respect Naga customary laws and traditions?",
    "நாகாலாந்து மாநிலத்தை உருவாக்கி, நாகா பழக்கவழக்கச் சட்டங்கள் மற்றும் மரபுகளை மதிக்கும் வகையில் சரத்து 371A-ன் கீழ் சிறப்பு விதிகளை அறிமுகப்படுத்திய திருத்தச் சட்டம் எது?",
    "13th Constitutional Amendment Act, 1962", "13-வது அரசியலமைப்பு திருத்தச் சட்டம், 1962",
    "10th Constitutional Amendment Act, 1961", "10-வது அரசியலமைப்பு திருத்தச் சட்டம், 1961",
    "12th Constitutional Amendment Act, 1962", "12-வது அரசியலமைப்பு திருத்தச் சட்டம், 1962",
    "14th Constitutional Amendment Act, 1962", "14-வது அரசியலமைப்பு திருத்தச் சட்டம், 1962",
    "A",
    "📚 Core Explanation:\nThe 13th Constitutional Amendment Act, 1962 provided for the creation of the State of Nagaland and inserted Article 371A giving special status to protect Naga customary law, religious practices, and land ownership.",
    "📚 முதன்மை விளக்கம்:\n1962-ஆம் ஆண்டின் 13-வது அரசியலமைப்பு திருத்தச் சட்டம் நாகாலாந்து மாநில உருவாக்கத்திற்கு வழிவகை செய்து, நாகா பழக்கவழக்கச் சட்டங்களைப் பாதுகாக்க சரத்து 371A-ஐச் சேர்த்தது.",
    "Option A is correct; 13th Amendment created Nagaland with Art 371A.", "விருப்பம் A சரியானது.",
    "Option B is incorrect; 10th Amendment was Dadra and Nagar Haveli.", "விருப்பம் B தவறானது.",
    "Option C is incorrect; 12th Amendment was Goa, Daman and Diu.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; 14th Amendment was Puducherry.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Nagaland became the 16th State of India on 1st December 1963.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: நாகாலாந்து டிசம்பர் 1, 1963 அன்று இந்தியாவின் 16-வது மாநிலமாக மாறியது.",
    "📖 Revision Fact: Under Article 371A, no Act of Parliament regarding Naga customary law applies to Nagaland unless approved by Nagaland Assembly.",
    "📖 திருத்தல் செய்தி: நாகாலாந்து சட்டமன்றத்தின் ஒப்புதலின்றி நாடாளுமன்றச் சட்டங்கள் நாகாலாந்திற்குப் பொருந்தாது.",
    "Remember", "High", ["13th Amendment", "Nagaland", "Article 371A"]
)

# Q93 - Ans: B
add_p4(
    "polity_amendments_gt_093", "Easy", "single_choice",
    "Which Constitutional Amendment Act incorporated Puducherry into the Union of India as a Union Territory and enabled Parliament to create legislatures for Union Territories?",
    "புதுச்சேரியை இந்திய ஒன்றியத்தில் ஒன்றிய பிரதேசமாக இணைத்து, ஒன்றிய பிரதேசங்களுக்கு சட்டமன்றங்களை உருவாக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளித்த திருத்தச் சட்டம் எது?",
    "10th Constitutional Amendment Act, 1961", "10-வது அரசியலமைப்பு திருத்தச் சட்டம், 1961",
    "14th Constitutional Amendment Act, 1962", "14-வது அரசியலமைப்பு திருத்தச் சட்டம், 1962",
    "12th Constitutional Amendment Act, 1962", "12-வது அரசியலமைப்பு திருத்தச் சட்டம், 1962",
    "13th Constitutional Amendment Act, 1962", "13-வது அரசியலமைப்பு திருத்தச் சட்டம், 1962",
    "B",
    "📚 Core Explanation:\nThe 14th Constitutional Amendment Act, 1962 incorporated Puducherry into the First Schedule as a Union Territory following French session and added Article 239A empowering Parliament to create Legislatures and Councils of Ministers for UTs.",
    "📚 முதன்மை விளக்கம்:\n1962-ஆம் ஆண்டின் 14-வது அரசியலமைப்பு திருத்தச் சட்டம் பிரெஞ்சு ஆட்சியில் இருந்த புதுச்சேரியை ஒன்றிய பிரதேசமாக இணைத்து, சரத்து 239A-ஐச் சேர்த்தது.",
    "Option A is incorrect; 10th Amendment was Dadra and Nagar Haveli.", "விருப்பம் A தவறானது.",
    "Option B is correct; 14th Amendment incorporated Puducherry.", "விருப்பம் B சரியானது.",
    "Option C is incorrect; 12th Amendment was Goa, Daman & Diu.", "விருப்பம் C தவறானது.",
    "Option D is incorrect; 13th Amendment was Nagaland.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Puducherry was under French rule until de jure transfer in 1962.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: புதுச்சேரி 1962 வரை பிரெஞ்சு ஆட்சியின் கீழ் இருந்தது.",
    "📖 Revision Fact: Puducherry was the first UT to have a Legislative Assembly under Article 239A.",
    "📖 திருத்தல் செய்தி: சரத்து 239A-ன் கீழ் சட்டமன்றத்தைக் கொண்ட முதல் ஒன்றிய பிரதேசம் புதுச்சேரி ஆகும்.",
    "Remember", "High", ["14th Amendment", "Puducherry", "Article 239A"]
)

# Q94 - Ans: C
add_p4(
    "polity_amendments_gt_094", "Medium", "single_choice",
    "Which Constitutional Amendment Act omitted the requirement of Quorum in Parliament and State Assemblies (later restored by the 44th Amendment Act)?",
    "நாடாளுமன்றம் மற்றும் மாநில சட்டமன்றங்களில் அவைக் கூட்டத் தேவையை (Quorum) நீக்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது (பின்னர் 44-வது திருத்தத்தால் மீண்டும் சேர்க்கப்பட்டது)?",
    "24th Constitutional Amendment Act, 1971", "24-வது அரசியலமைப்பு திருத்தச் சட்டம், 1971",
    "38th Constitutional Amendment Act, 1975", "38-வது அரசியலமைப்பு திருத்தச் சட்டம், 1975",
    "42nd Constitutional Amendment Act, 1976", "42-வது அரசியலமைப்பு திருத்தச் சட்டம், 1976",
    "39th Constitutional Amendment Act, 1975", "39-வது அரசியலமைப்பு திருத்தச் சட்டம், 1975",
    "C",
    "📚 Core Explanation:\nThe 42nd Constitutional Amendment Act, 1976 omitted the requirement of quorum (1/10th of total strength) in Parliament and State Assemblies, leaving it to be determined by rules of each House. The 44th Amendment Act, 1978 restored the constitutional quorum requirement.",
    "📚 முதன்மை விளக்கம்:\n1976-ஆம் ஆண்டின் 42-வது அரசியலமைப்பு திருத்தச் சட்டம் நாடாளுமன்றம் மற்றும் சட்டமன்றங்களில் குறைந்தபட்ச அவைக் கூட்டத் தேவையை (Quorum 1/10) நீக்கியது. பின்னர் 44-வது திருத்தச் சட்டம் 1978 இதை மீண்டும் மீட்டெடுத்தது.",
    "Option A is incorrect.", "விருப்பம் A தவறானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is correct; 42nd Amendment omitted quorum requirement.", "விருப்பம் C சரியானது.",
    "Option D is incorrect.", "விருப்பம் D தவறானது.",
    "💡 TNPSC Tip: Normal Quorum under Article 100(3) is 1/10th of total membership of the House.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: சரத்து 100(3)-ன் கீழ் சாதாரண அவைக் கூட்டம் 1/10 பங்கு உறுப்பினர்கள் ஆகும்.",
    "📖 Revision Fact: If there is no quorum, Speaker/Chairman must adjourn the House or suspend the meeting.",
    "📖 திருத்தல் செய்தி: அவைக் கூட்டம் (Quorum) இல்லை எனில் சபாநாயகர் அவையை ஒத்திவைக்க வேண்டும்.",
    "Remember", "High", ["42nd Amendment", "Quorum", "Article 100"]
)

# Q95 - Ans: D
add_p4(
    "polity_amendments_gt_095", "Hard", "statement",
    "Consider the following statements comparing emergency provisions under 42nd Amendment (1976) and 44th Amendment (1978):\n1. 42nd Amendment enabled President to declare National Emergency in any specified part of India; 44th Amendment retained this provision.\n2. 42nd Amendment allowed President's Rule under Art 356 to be extended for 1 year at a time up to 3 years; 44th Amendment reduced one-time extension to 6 months.\n3. 44th Amendment provided that President's Rule beyond 1 year requires Election Commission certification regarding election difficulty.\nWhich of the statements given above are correct?",
    "42-வது திருத்தம் (1976) மற்றும் 44-வது திருத்தம் (1978) ஆகியவற்றின் அவசரநிலை விதிகளை ஒப்பிடும் பின்வரும் கூற்றுகளை ஆராய்க:\n1. 42-வது திருத்தம் இந்தியாவின் குறிப்பிட்ட பகுதியில் தேசிய அவசரநிலையை அறிவிக்க குடியரசுத் தலைவருக்கு அதிகாரம் அளித்தது; 44-வது திருத்தம் இதை தக்கவைத்துக் கொண்டது.\n2. 42-வது திருத்தம் சரத்து 356 குடியரசுத் தலைவர் ஆட்சியை ஒரு நேரத்தில் 1 ஆண்டு என 3 ஆண்டுகள் வரை நீட்டிக்க அனுமதித்தது; 44-வது திருத்தம் ஒருமுறை நீட்டிப்பை 6 மாதங்களாகக் குறைத்தது.\n3. 1 ஆண்டிற்கு மேல் குடியரசுத் தலைவர் ஆட்சியை நீட்டிக்க தேர்தல் நடத்துவதில் சிரமம் இருப்பதாக தேர்தல் ஆணையத்தின் சான்றளிப்பு தேவை என 44-வது திருத்தம் வகைசெய்தது.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "📚 Core Explanation:\nAll three statements are CORRECT comparison details between 42nd (1976) and 44th (1978) Amendments regarding emergency provisions under Articles 352 and 356.",
    "📚 முதன்மை விளக்கம்:\nமூன்று கூற்றுகளும் 42 மற்றும் 44-வது திருத்தங்களின் அவசரநிலை விதிகளுக்கு இடையிலான சரியான ஒப்பீடுகளாகும்.",
    "Option A is incomplete.", "விருப்பம் A அரைகுறையானது.",
    "Option B is incomplete.", "விருப்பம் B அரைகுறையானது.",
    "Option C is incomplete.", "விருப்பம் C அரைகுறையானது.",
    "Option D is correct as statements 1, 2, and 3 are all true.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: Article 356 President's Rule max limit is 3 years, but 44th Amendment added 1-year constraint (needs EC certificate + National Emergency in force).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: சரத்து 356 அதிகபட்ச வரம்பு 3 ஆண்டுகள்; 1 ஆண்டிற்கு மேல் நீட்டிக்க தேர்தல் ஆணைய சான்றிதழ் தேவை.",
    "📖 Revision Fact: 44th Amendment Act required Parliamentary approval for National Emergency within 1 month (reduced from 2 months).",
    "📖 திருத்தல் செய்தி: 44-வது திருத்தம் தேசிய அவசரநிலைக்கு நாடாளுமன்ற ஒப்புதல் காலத்தை 1 மாதமாகக் குறைத்தது.",
    "Analyze", "High", ["42nd vs 44th Amendment", "Emergency Provisions", "Article 356 Limits"]
)

# Q96 - Ans: D
add_p4(
    "polity_amendments_gt_096", "Medium", "match_the_following",
    "Match List-I (Constitutional Amendment Act) with List-II (State / Territory Status Granted) and select the correct code:\nList-I:\nA. 13th Amendment Act, 1962\nB. 22nd Amendment Act, 1969\nC. 36th Amendment Act, 1975\nD. 56th Amendment Act, 1987\nList-II:\n1. State of Goa created\n2. Full-fledged 22nd State of Sikkim\n3. Autonomous State of Meghalaya within Assam\n4. State of Nagaland created with Article 371A",
    "பட்டியல்-I (அரசியலமைப்பு திருத்தச் சட்டம்) பட்டியல்-II (வழங்கப்பட்ட மாநில / பகுதி அந்தஸ்து) உடன் பொருத்தி சரியான குறியீட்டைத் தேர்ந்தெடுக்க:\nபட்டியல்-I:\nA. 13-வது திருத்தச் சட்டம், 1962\nB. 22-வது திருத்தச் சட்டம், 1969\nC. 36-வது திருத்தச் சட்டம், 1975\nD. 56-வது திருத்தச் சட்டம், 1987\nபட்டியல்-II:\n1. கோவா மாநிலம் உருவாக்கப்பட்டது\n2. சிக்கிம் 22-வது முழு மாநிலமாக்கப்பட்டது\n3. அசாமிற்குள் மேகாலயா தன்னாட்சி மாநிலமாக்கப்பட்டது\n4. நாகாலாந்து மாநிலம் சரத்து 371A உடன் உருவாக்கப்பட்டது",
    "A-4, B-3, C-1, D-2", "A-4, B-3, C-1, D-2",
    "A-3, B-4, C-2, D-1", "A-3, B-4, C-2, D-1",
    "A-4, B-2, C-3, D-1", "A-4, B-2, C-3, D-1",
    "A-4, B-3, C-2, D-1", "A-4, B-3, C-2, D-1",
    "D",
    "📚 Core Explanation:\n- 13th Amendment (1962) = Nagaland state creation (A-4).\n- 22nd Amendment (1969) = Autonomous State of Meghalaya within Assam (B-3).\n- 36th Amendment (1975) = Full State of Sikkim (C-2).\n- 56th Amendment (1987) = State of Goa created (D-1).\nCorrect match: A-4, B-3, C-2, D-1.",
    "📚 முதன்மை விளக்கம்:\n- 13-வது திருத்தம் (1962) = நாகாலாந்து மாநிலம் (A-4).\n- 22-வது திருத்தம் (1969) = அசாமிற்குள் மேகாலயா தன்னாட்சி (B-3).\n- 36-வது திருத்தம் (1975) = சிக்கிம் முழு மாநிலம் (C-2).\n- 56-வது திருத்தம் (1987) = கோவா மாநிலம் (D-1).",
    "Option A is incorrect.", "விருப்பம் A தவறானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is incorrect.", "விருப்பம் C தவறானது.",
    "Option D is correct as all matches correspond accurately.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: 56th Amendment made Goa a state (1987), while Daman & Diu remained a Union Territory.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 56-வது திருத்தம் கோவாவை மாநிலமாக்கியது, டாமன் & டையூ ஒன்றிய பிரதேசமாக நீடித்தது.",
    "📖 Revision Fact: Goa was liberated from Portuguese rule in December 1961 (Operation Vijay).",
    "📖 திருத்தல் செய்தி: கோவா டிசம்பர் 1961-ல் போர்த்துகீசிய ஆட்சியிலிருந்து விடுவிக்கப்பட்டது.",
    "Understand", "High", ["Match the Following", "State Creation Amendments", "13th 22nd 36th 56th Amendments"]
)

# Q97 - Ans: D
add_p4(
    "polity_amendments_gt_097", "Hard", "reasoning",
    "Given below are two statements, one labeled as Assertion (A) and the other as Reason (R):\nAssertion (A): If a Constitutional Amendment Bill passed by Lok Sabha is rejected by Rajya Sabha, the Bill lapses and cannot be passed through a Joint Sitting.\nReason (R): Article 108 of the Constitution providing for a Joint Sitting of both Houses of Parliament applies ONLY to Ordinary Bills and Financial Bills, and NOT to Constitutional Amendment Bills.\nIn light of the above statements, choose the correct option:",
    "கீழே இரண்டு கூற்றுகள் கொடுக்கப்பட்டுள்ளன. ஒன்று கூற்று (A) என்றும் மற்றொன்று காரணம் (R) என்றும் குறிக்கப்பட்டுள்ளது:\nகூற்று (A): மக்களவையால் நிறைவேற்றப்பட்ட அரசியலமைப்பு திருத்த மசோதாவை மாநிலங்களவை நிராகரித்தால், அம்மசோதா காலாவதியாகிறது மற்றும் கூட்டு அமர்வு மூலம் நிறைவேற்ற முடியாது.\nகாரணம் (R): சரத்து 108-ன் கீழ் நாடாளுமன்றத்தின் இரு அவைகளின் கூட்டு அமர்வு சாதாரண மற்றும் நிதி மசோதாக்களுக்கு மட்டுமே பொருந்தும்; அரசியலமைப்பு திருத்த மசோதாக்களுக்குப் பொருந்தாது.\nமேற்கண்ட கூற்றுகளின் அடிப்படையில் சரியான விருப்பத்தைத் தேர்ந்தெடுக்கவும்:",
    "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை ஆனால் (R) என்பது (A)-வின் சரியான விளக்கம் அல்ல",
    "(A) is true but (R) is false", "(A) உண்மை ஆனால் (R) தவறு",
    "(A) is false but (R) is true", "(A) தவறு ஆனால் (R) உண்மை",
    "Both (A) and (R) are true and (R) is the correct explanation of (A)", "(A) மற்றும் (R) இரண்டும் உண்மை மற்றும் (R) என்பது (A)-வின் சரியான விளக்கமாகும்",
    "D",
    "📚 Core Explanation:\nBoth Assertion (A) and Reason (R) are TRUE, and (R) is the correct explanation of (A). Because Article 108 does not apply to Constitutional Amendment Bills, there is no mechanism for joint sitting. If Rajya Sabha rejects the bill, the bill completely lapses.",
    "📚 முதன்மை விளக்கம்:\n(A) மற்றும் (R) இரண்டும் உண்மை, மற்றும் (R) என்பது (A)-ன் சரியான விளக்கம். சரத்து 108 அரசியலமைப்பு திருத்த மசோதாக்களுக்குப் பொருந்தாது என்பதால், மாநிலங்களவை நிராகரித்தால் மசோதா காலாவதியாகிவிடும்.",
    "Option A is incorrect because R explains A.", "விருப்பம் A தவறானது.",
    "Option B is incorrect because R is true.", "விருப்பம் B தவறானது.",
    "Option C is incorrect because A is true.", "விருப்பம் C தவறானது.",
    "Option D is correct as both A and R are true and R explains A.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: Example: 64th and 65th Amendment Bills (Panchayats & Municipalities) passed Lok Sabha in 1989 but lapsed because Rajya Sabha rejected them.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 1989-ல் 64 மற்றும் 65-வது திருத்த மசோதாக்களை மாநிலங்களவை நிராகரித்ததால் காலாவதியாயின.",
    "📖 Revision Fact: Rajya Sabha enjoys equal power with Lok Sabha in constitutional amendments.",
    "📖 திருத்தல் செய்தி: அரசியலமைப்பு திருத்தத்தில் மாநிலங்களவை மக்களவைக்கு நிகரான அதிகாரம் கொண்டது.",
    "Analyze", "High", ["Joint Sitting Disallowed", "Rajya Sabha Veto", "Article 108 Exception"]
)

# Q98 - Ans: D
add_p4(
    "polity_amendments_gt_098", "Medium", "single_choice",
    "Which Constitutional Amendment Act deleted Paragraph 3 of the Tenth Schedule, thereby removing the defense of 'split' in a political party to prevent rampant defections?",
    "கட்சித் தாவலைத் தடுக்க அரசியல் கட்சியில் 'பிளவு' (split) என்ற விலக்கு அளிக்கும் பத்தி 3-ஐ பத்தாவது அட்டவணையிலிருந்து நீக்கிய அரசியலமைப்பு திருத்தச் சட்டம் எது?",
    "52nd Constitutional Amendment Act, 1985", "52-வது அரசியலமைப்பு திருத்தச் சட்டம், 1985",
    "86th Constitutional Amendment Act, 2002", "86-வது அரசியலமைப்பு திருத்தச் சட்டம், 2002",
    "89th Constitutional Amendment Act, 2003", "89-வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
    "91st Constitutional Amendment Act, 2003", "91-வது அரசியலமைப்பு திருத்தச் சட்டம், 2003",
    "D",
    "📚 Core Explanation:\nThe 91st Constitutional Amendment Act, 2003 deleted Paragraph 3 of the Tenth Schedule. Prior to 2003, a split involving at least 1/3rd members was exempted from defection disqualification. Post-91st Amendment, only a merger involving at least 2/3rd members protects against defection.",
    "📚 முதன்மை விளக்கம்:\n2003-ஆம் ஆண்டின் 91-வது அரசியலமைப்பு திருத்தச் சட்டம் 10-வது அட்டவணையின் பத்தி 3-ஐ (1/3 பிளவு விலக்கு) நீக்கியது. இப்போது 2/3 உறுப்பினர்கள் இணையும் சேர்க்கை மட்டுமே கட்சித் தாவலில் இருந்து பாதுகாக்கும்.",
    "Option A is incorrect; 52nd Amendment introduced 10th Schedule with 1/3rd split rule.", "விருப்பம் A தவறானது.",
    "Option B is incorrect.", "விருப்பம் B தவறானது.",
    "Option C is incorrect.", "விருப்பம் C தவறானது.",
    "Option D is correct; 91st Amendment deleted 1/3rd split provision.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: 91st Amendment did TWO main things: 1) Capped Council of Ministers at 15%, 2) Abolished 1/3rd split in 10th Schedule.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: 91-வது திருத்தம் இரு முக்கிய காரியங்களைச் செய்தது: 15% அமைச்சரவை வரம்பு மற்றும் 1/3 பிளவு நீக்கம்.",
    "📖 Revision Fact: Merger under 10th Schedule requires agreement of at least two-thirds (66.67%) of members of the legislature party.",
    "📖 திருத்தல் செய்தி: 10-வது அட்டவணையின் கீழ் இணைப்பு செல்லுபடியாக 2/3 பங்கு உறுப்பினர்கள் ஒப்புக்கொள்ள வேண்டும்.",
    "Remember", "High", ["91st Amendment", "Tenth Schedule Split Removal", "Anti Defection"]
)

# Q99 - Ans: D
add_p4(
    "polity_amendments_gt_099", "Hard", "statement",
    "Consider the following evolution of Judicial Review over Constitutional Amendments in India:\n1. Shankari Prasad (1951) & Sajjan Singh (1965): Constitutional amendments are not 'law' under Article 13(2); Parliament can amend Fundamental Rights.\n2. Golaknath (1967): Constitutional amendments are 'law' under Article 13(2); Fundamental Rights are unamendable.\n3. Kesavananda Bharati (1973): Overruled Golaknath; Parliament can amend any part including FRs, subject to the Basic Structure Doctrine.\nWhich of the statements given above correctly describe this judicial evolution?",
    "இந்தியாவில் அரசியலமைப்பு திருத்தங்கள் மீதான நீதிமன்ற ஆய்வின் பரிணாம வளர்ச்சி குறித்த பின்வரும் கூற்றுகளை ஆராய்க:\n1. சங்கரி பிரசாத் (1951) & சஜ்ஜன் சிங் (1965): அரசியலமைப்பு திருத்தங்கள் சரத்து 13(2)-ன் கீழ் 'சட்டம்' அல்ல; நாடாளுமன்றம் அடிப்படை உரிமைகளைத் திருத்தலாம்.\n2. கோலக்நாத் (1967): அரசியலமைப்பு திருத்தங்கள் சரத்து 13(2)-ன் கீழ் 'சட்டம்' ஆகும்; அடிப்படை உரிமைகளை திருத்த முடியாது.\n3. கேசவாநந்த பாரதி (1973): கோலக்நாத் தீர்ப்பை ரத்து செய்தது; அடிப்படை கட்டமைப்புக்கு உட்பட்டு அடிப்படை உரிமைகள் உட்பட எந்தப் பகுதியையும் நாடாளுமன்றம் திருத்தலாம்.\nமேற்கூறிய கூற்றுகளில் எவை சரியானவை?",
    "1 and 2 only", "1 மற்றும் 2 மட்டுமே",
    "2 and 3 only", "2 மற்றும் 3 மட்டுமே",
    "1 and 3 only", "1 மற்றும் 3 மட்டுமே",
    "1, 2 and 3", "1, 2 மற்றும் 3",
    "D",
    "📚 Core Explanation:\nAll three statements correctly trace the 3-stage historic evolution of judicial review over constitutional amendments from Shankari Prasad (1951) -> Golaknath (1967) -> Kesavananda Bharati (1973).",
    "📚 முதன்மை விளக்கம்:\nமூன்று கூற்றுகளும் 1951 முதல் 1973 வரையிலான நீதிமன்ற ஆய்வு பரிணாம வளர்ச்சியைத் துல்லியமாக விவரிக்கின்றன.",
    "Option A is incomplete.", "விருப்பம் A அரைகுறையானது.",
    "Option B is incomplete.", "விருப்பம் B அரைகுறையானது.",
    "Option C is incomplete.", "விருப்பம் C அரைகுறையானது.",
    "Option D is correct as all three statements are true.", "விருப்பம் D சரியானது.",
    "💡 TNPSC Tip: Summary: 1951-67 (Absolute Power) -> 1967-73 (No Power over FR) -> 1973-Present (Limited Power subject to Basic Structure).",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: சுருக்கம்: 1951-67 (முழு அதிகாரம்) -> 1967-73 (அதிகாரமில்லை) -> 1973-தற்போது (அடிப்படை கட்டமைப்புக்கு உட்பட்ட அதிகாரம்).",
    "📖 Revision Fact: Kesavananda Bharati case judgment consists of 11 separate opinions spanning over 700 pages.",
    "📖 திருத்தல் செய்தி: கேசவாநந்த பாரதி தீர்ப்பு 700 பக்கங்களுக்கு மேல் 11 தனித்தனி தீர்ப்புகளைக் கொண்டது.",
    "Analyze", "High", ["Judicial Evolution", "Shankari Prasad", "Golaknath", "Kesavananda"]
)

# Q100 - Ans: D
add_p4(
    "polity_amendments_gt_100", "Hard", "single_choice",
    "Which of the following elements has NOT been declared by the Supreme Court as a part of the 'Basic Structure' of the Indian Constitution across various landmark judgments?",
    "பல்வேறு வரலாற்றுச் சிறப்புமிக்க தீர்ப்புகளில் உச்சநீதிமன்றத்தால் இந்திய அரசியலமைப்பின் 'அடிப்படை கட்டமைப்பின்' ஒரு பகுதியாக அறிவிக்கப்படாத அம்சம் எது?",
    "Supremacy of the Constitution and Rule of Law", "அரசியலமைப்பின் மேலாதிக்கம் மற்றும் சட்டத்தின் ஆட்சி",
    "Separation of powers between Legislature, Executive and Judiciary", "சட்டமன்றம், நிர்வாகம் மற்றும் நீதித்துறைக்கு இடையிலான அதிகாரப் பகிர்வு",
    "Secular character of the Constitution and Federalism", "அரசியலமைப்பின் சமயச்சார்பற்ற தன்மை மற்றும் கூட்டாட்சி",
    "Unrestricted and unreviewable constituent power of Parliament under Article 368", "சரத்து 368-ன் கீழ் நாடாளுமன்றத்தின் வரம்பற்ற மற்றும் மறுஆய்வு செய்ய முடியாத அரசியலமைப்பு ஆக்கல் அதிகாரம்",
    "D",
    "📚 Core Explanation:\nOption D is NOT part of the Basic Structure (and hence the correct answer). In fact, the Supreme Court in Minerva Mills (1980) held that Parliament does NOT have unrestricted constituent power and 'limited amending power' is itself a basic feature. Options A, B, and C are all recognized basic structure elements.",
    "📚 முதன்மை விளக்கம்:\nவிருப்பம் D அடிப்படை கட்டமைப்பின் பகுதி அல்ல (எனவே சரியான விடை). மினெர்வா மில்ஸ் வழக்கில் நாடாளுமன்றத்திற்கு வரம்பற்ற அதிகாரம் இல்லை என்றும், வரம்பிற்குட்பட்ட திருத்தும் அதிகாரமே அடிப்படை அம்சம் என்றும் உச்சநீதிமன்றம் கூறியது.",
    "Option A is a recognized basic structure element.", "விருப்பம் A அங்கீகரிக்கப்பட்ட அடிப்படை அம்சம்.",
    "Option B is a recognized basic structure element.", "விருப்பம் B அங்கீகரிக்கப்பட்ட அடிப்படை அம்சம்.",
    "Option C is a recognized basic structure element.", "விருப்பம் C அங்கீகரிக்கப்பட்ட அடிப்படை அம்சம்.",
    "Option D is correct as unrestricted amending power is invalid.", "விருப்பம் D சரியானது, ஏனெனில் வரம்பற்ற அதிகாரம் செல்லாது.",
    "💡 TNPSC Tip: Basic Structure elements include: Supremacy of Constitution, Rule of Law, Separation of Powers, Judicial Review, Secularism, Federalism, Free & Fair Elections, Welfare State, Harmony between FR & DPSP.",
    "💡 டிஎன்பிஎஸ்சி குறிப்பு: அடிப்படை கட்டமைப்பு அம்சங்களில் அரசியலமைப்பு மேலாதிக்கம், சட்டத்தின் ஆட்சி, அதிகாரப் பகிர்வு, நீதிமன்ற ஆய்வு, சமயச்சார்பின்மை, கூட்டாட்சி அடங்கும்.",
    "📖 Revision Fact: Basic Structure list is open-ended and expanded by Supreme Court on a case-by-case basis.",
    "📖 திருத்தல் செய்தி: அடிப்படை கட்டமைப்பு பட்டியல் முடிவற்றது, உச்சநீதிமன்றம் வழக்கு வாரியாக அதை விரிவாக்குகிறது.",
    "Evaluate", "High", ["Grand Test Synthesis", "Basic Structure Elements", "Minerva Mills"]
)

print("Part 4 questions Q76 to Q100 loaded completely.")
