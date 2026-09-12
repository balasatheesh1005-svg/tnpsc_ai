import json
from scratch_make_q import make_q

easy_qs = []

# 1. CM_E_001 (A)
easy_qs.append(make_q(
    "CM_E_001", "Easy", "Remember", 45,
    "Which Article of the Indian Constitution provides for a Council of Ministers with the Chief Minister at the head to aid and advise the Governor?",
    "ஆளுநருக்கு உதவவும் ஆலோசனை வழங்கவும் முதலமைச்சரை தலைவராகக் கொண்ட அமைச்சரவை அமைப்பதற்கு வழிவகை செய்யும் இந்திய அரசியலமைப்பு உறுப்பு எது?",
    "Article 163", "உறுப்பு 163",
    "Article 164", "உறுப்பு 164",
    "Article 167", "உறுப்பு 167",
    "Article 169", "உறுப்பு 169",
    "A",
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
easy_qs.append(make_q(
    "CM_E_002", "Easy", "Remember", 45,
    "Under Article 164(1) of the Indian Constitution, who appoints the Chief Minister of a State?",
    "இந்திய அரசியலமைப்பின் உறுப்பு 164(1)-ன் கீழ், ஒரு மாநிலத்தின் முதலமைச்சரை நியமிப்பவர் யார்?",
    "President of India", "இந்தியக் குடியரசுத் தலைவர்",
    "Governor of the State", "மாநில ஆளுநர்",
    "Speaker of the Legislative Assembly", "சட்டமன்றப் பேரவைத் தலைவர்",
    "Chief Justice of the High Court", "உயர் நீதிமன்றத் தலைமை நீதிபதி",
    "B",
    "Article 164(1) explicitly provides that the Chief Minister shall be appointed by the Governor, and the other Ministers shall be appointed by the Governor on the advice of the Chief Minister.",
    "உறுப்பு 164(1)-ன்படி, முதலமைச்சர் ஆளுநரால் நியமிக்கப்படுவார், மேலும் பிற அமைச்சர்கள் முதலமைச்சரின் ஆலோசனையின் பேரில் ஆளுநரால் நியமிக்கப்படுவார்கள்.",
    "Incorrect. President appoints Prime Minister and Union Ministers, not State Chief Ministers.", "தவறு. குடியரசுத் தலைவர் பிரதமரையும் மத்திய அமைச்சர்களையும் நியமிக்கிறார், மாநில முதலமைச்சரை அல்ல.",
    "Correct. Governor appoints the Chief Minister under Article 164(1).", "சரி. உறுப்பு 164(1)-ன் கீழ் ஆளுநர் முதலமைச்சரை நியமிக்கிறார்.",
    "Incorrect. Speaker presides over Legislative Assembly sessions.", "தவறு. சபாநாயகர் சட்டமன்றப் பேரவைக் கூட்டங்களைத் தலைமை தாங்குகிறார்.",
    "Incorrect. Chief Justice of High Court administers oath of office to the Governor.", "தவறு. உயர் நீதிமன்றத் தலைமை நீதிபதி ஆளுநருக்குப் பதவிப் பிரமாணம் செய்து வைக்கிறார்.",
    "Remember: Appointment of CM is by Governor (Art 164(1)); Appointment of PM is by President (Art 75(1)).", "நினைவில் கொள்க: முதலமைச்சர் ஆளுநரால் நியமிக்கப்படுகிறார் (உறுப்பு 164(1)); பிரதமர் குடியரசுத் தலைவரால் நியமிக்கப்படுகிறார் (உறுப்பு 75(1)).",
    "The Governor appoints the Chief Minister under Article 164(1).", "உறுப்பு 164(1)-ன் கீழ் ஆளுநர் முதலமைச்சரை நியமிக்கிறார்."
))

# Save early check for build script
print("Easy module setup working.")
