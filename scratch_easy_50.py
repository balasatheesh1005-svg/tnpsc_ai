import json
from scratch_make_150_cm_fast import mk

def get_easy_50():
    eq = []
    
    # 1. CM_E_001 (A)
    eq.append(mk(
        "CM_E_001", "Easy", "Remember", 45,
        "Which Article of the Indian Constitution provides for a Council of Ministers with the Chief Minister at the head to aid and advise the Governor?",
        "ஆளுநருக்கு உதவவும் ஆலோசனை வழங்கவும் முதலமைச்சரை தலைவராகக் கொண்ட அமைச்சரவை அமைப்பதற்கு வழிவகை செய்யும் இந்திய அரசியலமைப்பு உறுப்பு எது?",
        "Article 163", "உறுப்பு 163", "Article 164", "உறுப்பு 164", "Article 167", "உறுப்பு 167", "Article 169", "உறுப்பு 169", "A",
        "Article 163(1) mandates that there shall be a Council of Ministers with the Chief Minister at the head to aid and advise the Governor in the exercise of his functions, except in matters where the Governor acts in discretion.",
        "உறுப்பு 163(1)-ன்படி, ஆளுநர் தனது விருப்புரிமை அதிகாரங்களைத் தவிர மற்ற பணிகளை நிறைவேற்ற அவருக்கு உதவவும் ஆலோசனை வழங்கவும் முதலமைச்சரைத் தலைவராகக் கொண்ட அமைச்சரவை ஒன்று இருக்க வேண்டும்.",
        "Correct. Article 163 provides for aid and advice of Council of Ministers to Governor.", "சரி. உறுப்பு 163 ஆளுநருக்கு அமைச்சரவையின் உதவி மற்றும் ஆலோசனையைக் குறிப்பிடுகிறது.",
        "Incorrect. Article 164 deals with appointment, tenure, responsibility, oath, and salaries of Ministers.", "தவறு. உறுப்பு 164 அமைச்சர்களின் நியமனம், பதவிக்காலம், பொறுப்புடைமை, உறுதிமொழி மற்றும் ஊதியங்களைக் கையாள்கிறது.",
        "Incorrect. Article 167 specifies the duties of Chief Minister with respect to furnishing information to Governor.", "தவறு. உறுப்பு 167 ஆளுநருக்குத் தகவல் தெரிவிப்பதில் முதலமைச்சரின் கடமைகளைக் குறிப்பிடுகிறது.",
        "Incorrect. Article 169 deals with creation or abolition of Legislative Councils in States.", "தவறு. உறுப்பு 169 மாநிலங்களில் சட்ட மேலவைகளை உருவாக்குதல் அல்லது நீக்குதலைக் கையாள்கிறது.",
        "Article 163 at the State level corresponds to Article 74 at the Union level.", "மாநில அளவில் உறுப்பு 163 என்பது மத்திய அளவில் உறுப்பு 74-க்கு இணையானதாகும்.",
        "Article 163 mandates the Council of Ministers with CM at the head to aid and advise the Governor.", "ஆளுநருக்கு உதவவும் ஆலோசனை வழங்கவும் முதலமைச்சரைத் தலைவராகக் கொண்ட அமைச்சரவை இருக்க வேண்டும் என உறுப்பு 163 கூறுகிறது."
    ))

    # 2. CM_E_002 (B)
    eq.append(mk(
        "CM_E_002", "Easy", "Remember", 45,
        "Under Article 164(1) of the Indian Constitution, who appoints the Chief Minister of a State?",
        "இந்திய அரசியலமைப்பின் உறுப்பு 164(1)-ன் கீழ், ஒரு மாநிலத்தின் முதலமைச்சரை நியமிப்பவர் யார்?",
        "President of India", "இந்தியக் குடியரசுத் தலைவர்", "Governor of the State", "மாநில ஆளுநர்", "Speaker of Legislative Assembly", "சட்டமன்றப் பேரவைத் தலைவர்", "Chief Justice of High Court", "உயர் நீதிமன்றத் தலைமை நீதிபதி", "B",
        "Article 164(1) explicitly provides that the Chief Minister shall be appointed by the Governor, and the other Ministers shall be appointed by the Governor on the advice of the Chief Minister.",
        "உறுப்பு 164(1)-ன்படி, முதலமைச்சர் ஆளுநரால் நியமிக்கப்படுவார், மேலும் பிற அமைச்சர்கள் முதலமைச்சரின் ஆலோசனையின் பேரில் ஆளுநரால் நியமிக்கப்படுவார்கள்.",
        "Incorrect. President appoints Prime Minister and Union Ministers, not State Chief Ministers.", "தவறு. குடியரசுத் தலைவர் பிரதமரையும் மத்திய அமைச்சர்களையும் நியமிக்கிறார், மாநில முதலமைச்சரை அல்ல.",
        "Correct. Governor appoints the Chief Minister under Article 164(1).", "சரி. உறுப்பு 164(1)-ன் கீழ் ஆளுநர் முதலமைச்சரை நியமிக்கிறார்.",
        "Incorrect. Speaker presides over Legislative Assembly sessions.", "தவறு. சபாநாயகர் சட்டமன்றப் பேரவைக் கூட்டங்களைத் தலைமை தாங்குகிறார்.",
        "Incorrect. Chief Justice of High Court administers oath of office to the Governor.", "தவறு. உயர் நீதிமன்றத் தலைமை நீதிபதி ஆளுநருக்குப் பதவிப் பிரமாணம் செய்து வைக்கிறார்.",
        "Remember: Appointment of CM is by Governor (Art 164(1)); Appointment of PM is by President (Art 75(1)).", "நினைவில் கொள்க: முதலமைச்சர் ஆளுநரால் நியமிக்கப்படுகிறார் (உறுப்பு 164(1)); பிரதமர் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார் (உறுப்பு 75(1)).",
        "The Governor appoints the Chief Minister under Article 164(1).", "உறுப்பு 164(1)-ன் கீழ் ஆளுநர் முதலமைச்சரை நியமிக்கிறார்."
    ))

    # 3. CM_E_003 (C)
    eq.append(mk(
        "CM_E_003", "Easy", "Remember", 45,
        "Who is the de facto (real) executive head of the State Government in India?",
        "இந்தியாவில் மாநில அரசாங்கத்தின் உண்மையான (de facto) நிர்வாகத் தலைவர் யார்?",
        "Governor", "ஆளுநர்", "President", "குடியரசுத் தலைவர்", "Chief Minister", "முதலமைச்சர்", "Speaker of Legislative Assembly", "சட்டமன்றப் பேரவைத் தலைவர்", "C",
        "In the parliamentary system of government at the State level, the Governor is the de jure (nominal) executive head, while the Chief Minister is the de facto (real) executive head of the State Government.",
        "மாநில அளவில் நாடாளுமன்ற ஆட்சி முறையில், ஆளுநர் சட்டப்படியான (பெயரளவு) நிர்வாகத் தலைவராகவும், முதலமைச்சர் உண்மையான நிர்வாகத் தலைவராகவும் செயல்படுகிறார்.",
        "Incorrect. Governor is the de jure (nominal) executive head.", "தவறு. ஆளுநர் சட்டப்படியான (பெயரளவு) நிர்வாகத் தலைவர் ஆவார்.",
        "Incorrect. President is the de jure executive head of the Union Government.", "தவறு. குடியரசுத் தலைவர் மத்திய அரசின் சட்டப்படியான நிர்வாகத் தலைவர் ஆவார்.",
        "Correct. Chief Minister is the de facto (real) executive head of the State.", "சரி. முதலமைச்சர் மாநிலத்தின் உண்மையான நிர்வாகத் தலைவர் ஆவார்.",
        "Incorrect. Speaker is the presiding officer of the Legislative Assembly.", "தவறு. சபாநாயகர் சட்டமன்றப் பேரவையின் தலைமை அலுவலர் ஆவார்.",
        "Chief Minister is De Facto executive head; Governor is De Jure executive head.", "முதலமைச்சர் உண்மையான நிர்வாகத் தலைவர்; ஆளுநர் சட்டப்படியான நிர்வாகத் தலைவர்.",
        "The Chief Minister is the de facto executive head of the State Government.", "முதலமைச்சர் மாநில அரசாங்கத்தின் உண்மையான நிர்வாகத் தலைவர் ஆவார்."
    ))

    # 4. CM_E_004 (D)
    eq.append(mk(
        "CM_E_004", "Easy", "Remember", 45,
        "Who is the de jure (nominal/constitutional) executive head of a State in India?",
        "இந்தியாவில் ஒரு மாநிலத்தின் சட்டப்படியான (பெயரளவு/அரசியலமைப்பு) நிர்வாகத் தலைவர் யார்?",
        "Chief Minister", "முதலமைச்சர்", "Cabinet Secretary", "கேபினெட் செயலாளர்", "Advocate General", "அட்வகேட் ஜெனரல்", "Governor", "ஆளுநர்", "D",
        "The Governor is the de jure (constitutional/nominal) head of the State executive, while the Chief Minister is the de facto real executive head.",
        "ஆளுநர் மாநில நிர்வாகத்தின் சட்டப்படியான (அரசியலமைப்பு/பெயரளவு) தலைவராவார், ஆனால் முதலமைச்சர் உண்மையான நிர்வாகத் தலைவராவார்.",
        "Incorrect. Chief Minister is the de facto real executive head.", "தவறு. முதலமைச்சர் உண்மையான நிர்வாகத் தலைவர் ஆவார்.",
        "Incorrect. Cabinet Secretary is the administrative head of Union cabinet administration.", "தவறு. கேபினெட் செயலாளர் மத்திய கேபினெட் நிர்வாகத்தின் நிர்வாகத் தலைவர் ஆவார்.",
        "Incorrect. Advocate General is the chief legal advisor to the State Government.", "தவறு. அட்வகேட் ஜெனரல் மாநில அரசின் தலைமை சட்ட ஆலோசகர் ஆவார்.",
        "Correct. Governor is the de jure constitutional executive head of the State.", "சரி. ஆளுநர் மாநிலத்தின் சட்டப்படியான அரசியலமைப்பு நிர்வாகத் தலைவர் ஆவார்.",
        "Governor = Head of State (De Jure); CM = Head of Government (De Facto).", "ஆளுநர் = மாநிலத்தின் தலைவர் (சட்டப்படியானவர்); முதலமைச்சர் = அரசின் தலைவர் (உண்மையானவர்).",
        "The Governor is the de jure executive head of the State.", "ஆளுநர் மாநிலத்தின் சட்டப்படியான நிர்வாகத் தலைவர் ஆவார்."
    ))

    # 5. CM_E_005 (A)
    eq.append(mk(
        "CM_E_005", "Easy", "Remember", 45,
        "According to Article 164(2) of the Indian Constitution, the State Council of Ministers is collectively responsible to which body?",
        "இந்திய அரசியலமைப்பின் உறுப்பு 164(2)-ன் படி, மாநில அமைச்சரவை கூட்டாக எந்த அமைப்பிற்குப் பொறுப்புடையது?",
        "Legislative Assembly of the State", "மாநில சட்டமன்றப் பேரவை", "Legislative Council of the State", "மாநில சட்டமன்ற மேலவை", "Governor of the State", "மாநில ஆளுநர்", "High Court of the State", "மாநில உயர் நீதிமன்றம்", "A",
        "Article 164(2) states that the Council of Ministers shall be collectively responsible to the Legislative Assembly of the State.",
        "உறுப்பு 164(2)-ன்படி, மாநில அமைச்சரவை மாநில சட்டமன்றப் பேரவைக்கு மட்டுமே கூட்டாகப் பொறுப்புடையதாகும்.",
        "Correct. Council of Ministers is collectively responsible to the Legislative Assembly.", "சரி. அமைச்சரவை சட்டமன்றப் பேரவைக்குக் கூட்டாகப் பொறுப்புடையது.",
        "Incorrect. Legislative Council is the upper house and does not hold collective responsibility of ministers.", "தவறு. சட்டமன்ற மேலவை மேலவையாகும்; அமைச்சர்கள் மேலவைக்குக் கூட்டாகப் பொறுப்பல்ல.",
        "Incorrect. Individual responsibility is to the Governor under Art 164(1), but collective responsibility is to Assembly.", "தவறு. உறுப்பு 164(1)-ன் கீழ் தனிநபர் பொறுப்பு ஆளுநருக்கு உரியது, ஆனால் கூட்டுப் பொறுப்பு பேரவைக்கே.",
        "Incorrect. High Court is a judicial organ.", "தவறு. உயர் நீதிமன்றம் ஒரு நீதித்துறை அமைப்பாகும்.",
        "Collective responsibility is ONLY to the Legislative Assembly, not to the Council or Governor.", "கூட்டுப் பொறுப்புடைமை சட்டமன்றப் பேரவைக்கு மட்டுமே உரியது (மேலவைக்கோ ஆளுநருக்கோ அல்ல).",
        "The Council of Ministers is collectively responsible to the State Legislative Assembly under Article 164(2).", "உறுப்பு 164(2)-ன் கீழ் அமைச்சரவை மாநில சட்டமன்றப் பேரவைக்கு கூட்டாகப் பொறுப்புடையது."
    ))

    return eq

print("easy_50 setup ready.")
