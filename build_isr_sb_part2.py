# -*- coding: utf-8 -*-
"""
Builder for Inter-State Relations Statement-Based Part 2 (ISR_S_026 to ISR_S_050)
"""
import json
from gen_isr_statement_helper import make_q

def get_sb_part2():
    q = []

    # 026 - Ans B
    q.append(make_q(
        "ISR_S_026", "Medium",
        "Consider the following statements regarding the creation of Zonal Councils in India:\n1. The original 1950 Constitution contained provisions for five Zonal Councils under Article 263A.\n2. Five Zonal Councils (Northern, Central, Eastern, Western, and Southern) were established under Part III of the States Reorganisation Act, 1956.\nWhich of the statements given above is/are correct?",
        "இந்தியாவில் மண்டலக் குழுக்கள் உருவாக்கப்பட்டது தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 1950-ஆம் ஆண்டின் அசல் அரசியலமைப்பு உறுப்பு 263A-ன் கீழ் ஐந்து மண்டலக் குழுக்களுக்கான விதிகளைக் கொண்டிருந்தது.\n2. 1956-ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் பகுதி III-ன் கீழ் ஐந்து மண்டலக் குழுக்கள் (வடக்கு, மத்திய, கிழக்கு, மேற்கு மற்றும் தெற்கு) நிறுவப்பட்டன.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "B",
        "Statement 1 is incorrect: The Constitution never contained Article 263A; Zonal Councils are not constitutional bodies. Statement 2 is correct: Five Zonal Councils were established pursuant to Section 15 of the States Reorganisation Act, 1956, dividing the country into Northern, Central, Eastern, Western, and Southern zones.",
        "கூற்று 1 தவறு: அரசியலமைப்பில் உறுப்பு 263A என்ற விதியே இல்லை; மண்டலக் குழுக்கள் அரசியலமைப்பு அமைப்புகள் அல்ல. கூற்று 2 சரி: 1956 மாநில மறுசீரமைப்புச் சட்டம் பிரிவு 15-ன் கீழ் வடக்கு, மத்திய, கிழக்கு, மேற்கு, தெற்கு என ஐந்து மண்டலக் குழுக்கள் உருவாக்கப்பட்டன.",
        "Option A is incorrect because Article 263A does not exist in the Constitution.", "அரசியலமைப்பில் உறுப்பு 263A இல்லாததால் விருப்பம் A தவறு.",
        "Option B is correct because statement 2 accurately reflects the statutory genesis of the 5 Zonal Councils under the 1956 Act.", "1956 சட்டத்தின் கீழ் 5 மண்டலக் குழுக்கள் உருவானதை கூற்று 2 சரியாகக் குறிப்பிடுவதால் விருப்பம் B சரி.",
        "Option C is incorrect because statement 1 is an invented provision.", "கூற்று 1 தவறானது என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 2 is completely true.", "கூற்று 2 முற்றிலும் சரியானது என்பதால் விருப்பம் D தவறு.",
        "Zonal Councils are statutory creations of the States Reorganisation Act 1956, NOT Article 263.",
        "மண்டலக் குழுக்கள் 1956 மாநில மறுசீரமைப்புச் சட்டத்தால் உருவாக்கப்பட்டவை, உறுப்பு 263-ஆல் அல்ல.",
        "Five Zonal Councils were created under the States Reorganisation Act, 1956 to foster inter-state coordination.",
        "மாநிலங்களுக்கு இடையேயான ஒருங்கிணைப்பை வளர்க்க 1956 மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் 5 மண்டலக் குழுக்கள் உருவாக்கப்பட்டன.",
        tags=["Zonal Councils", "States Reorganisation Act 1956", "Statutory Origin"]
    ))

    # 027 - Ans C
    q.append(make_q(
        "ISR_S_027", "Medium",
        "Consider the following statements regarding the Northern Zonal Council:\n1. The Northern Zonal Council has its headquarters located in New Delhi.\n2. Its member units include Punjab, Haryana, Rajasthan, Himachal Pradesh, NCT of Delhi, and the Union Territories of Jammu & Kashmir, Ladakh, and Chandigarh.\nWhich of the statements given above is/are correct?",
        "வடக்கு மண்டலக் குழு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. வடக்கு மண்டலக் குழுவின் தலைமையகம் புதுதில்லியில் அமைந்துள்ளது.\n2. பஞ்சாப், ஹரியானா, ராஜஸ்தான், இமாச்சலப் பிரதேசம், தில்லி தேசிய தலைநகர் பிரதேசம் மற்றும் ஜம்மு-காஷ்மீர், லடாக், சண்டிகர் ஆகிய யூனியன் பிரதேசங்கள் இதன் உறுப்புப் பகுதிகளாகும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "C",
        "Both statements are correct: Statement 1 is correct: New Delhi is the headquarters of the Northern Zonal Council. Statement 2 is correct: Its member units encompass Punjab, Haryana, Rajasthan, Himachal Pradesh, NCT of Delhi, Chandigarh, Jammu & Kashmir, and Ladakh.",
        "இரண்டு கூற்றுகளும் சரியானவை: கூற்று 1 சரி: வடக்கு மண்டலக் குழுவின் தலைமையகம் புதுதில்லியில் உள்ளது. கூற்று 2 சரி: பஞ்சாப், ஹரியானா, ராஜஸ்தான், இமாச்சலப் பிரதேசம், தில்லி, சண்டிகர், ஜம்மு-காஷ்மீர், லடாக் ஆகியவை இதன் உறுப்பினர்களாக உள்ளன.",
        "Option A is incorrect because statement 2 is equally valid.", "கூற்று 2-ம் சரியானது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because statement 1 is equally valid.", "கூற்று 1-ம் சரியானது என்பதால் விருப்பம் B தவறு.",
        "Option C is correct as both headquarters and territorial jurisdiction of the Northern Zonal Council are correctly stated.", "தலைமையகம் மற்றும் உறுப்புப் பகுதிகள் இரண்டையும் சரியாகக் குறிப்பிடுவதால் விருப்பம் C சரி.",
        "Option D is incorrect because neither statement is false.", "எந்தக் கூற்றும் தவறானது அல்ல என்பதால் விருப்பம் D தவறு.",
        "Northern Zonal Council HQ: New Delhi; includes Punjab, Haryana, Rajasthan, HP, Delhi, J&K, Ladakh, Chandigarh.",
        "வடக்கு மண்டலக் குழு தலைமையகம்: புதுதில்லி; பஞ்சாப், ஹரியானா, ராஜஸ்தான், இமாச்சல பிரதேசம், தில்லி, ஜம்மு காஷ்மீர், லடாக், சண்டிகர் உறுப்பினர்கள்.",
        "Northern Zonal Council is headquartered in New Delhi and comprises northern states and UTs.",
        "வடக்கு மண்டலக் குழு புதுதில்லியைத் தலைமையகமாகக் கொண்டு வட மாநிலங்கள் மற்றும் யூனியன் பிரதேசங்களை உள்ளடக்கியுள்ளது.",
        tags=["Northern Zonal Council", "Headquarters New Delhi", "Member States"]
    ))

    # 028 - Ans A
    q.append(make_q(
        "ISR_S_028", "Hard",
        "Consider the following statements regarding the Central Zonal Council:\n1. The headquarters of the Central Zonal Council is located at Prayagraj (Allahabad).\n2. The member States of the Central Zonal Council are Uttar Pradesh, Madhya Pradesh, Uttarakhand, and Bihar.\nWhich of the statements given above is/are correct?",
        "மத்திய மண்டலக் குழு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மத்திய மண்டலக் குழுவின் தலைமையகம் பிரயாக்ராஜில் (அலகாபாத்) அமைந்துள்ளது.\n2. உத்தரப் பிரதேசம், மத்தியப் பிரதேசம், உத்தராகண்ட் மற்றும் பீகார் ஆகியவை மத்திய மண்டலக் குழுவின் உறுப்பு மாநிலங்கள் ஆகும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "A",
        "Statement 1 is correct: The headquarters of the Central Zonal Council is at Prayagraj (Allahabad). Statement 2 is incorrect: The member states of the Central Zonal Council are Uttar Pradesh, Madhya Pradesh, Uttarakhand, and CHHATTISGARH. Bihar is a member of the Eastern Zonal Council, not the Central Zonal Council.",
        "கூற்று 1 சரி: மத்திய மண்டலக் குழுவின் தலைமையகம் பிரயாக்ராஜில் (அலகாபாத்) உள்ளது. கூற்று 2 தவறு: உ.பி., ம.பி., உத்தராகண்ட் மற்றும் சத்தீஸ்கர் ஆகியவையே இதன் உறுப்பினர்கள். பீகார் கிழக்கு மண்டலக் குழுவின் உறுப்பினர் ஆகும்.",
        "Option A is correct because statement 1 is accurate, whereas statement 2 mistakenly includes Bihar.", "கூற்று 1 சரியானது மற்றும் கூற்று 2 பீகாரைத் தவறாகச் சேர்த்துள்ளதால் விருப்பம் A சரி.",
        "Option B is incorrect because Bihar belongs to the Eastern Zonal Council.", "பீகார் கிழக்கு மண்டலக் குழுவில் உள்ளதால் விருப்பம் B தவறு.",
        "Option C is incorrect because statement 2 is false.", "கூற்று 2 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 1 is true.", "கூற்று 1 உண்மையானது என்பதால் விருப்பம் D தவறு.",
        "Central Zonal Council states: UP, MP, Uttarakhand, Chhattisgarh (NOT Bihar). HQ is Prayagraj.",
        "மத்திய மண்டலக் குழு மாநிலங்கள்: உ.பி., ம.பி., உத்தராகண்ட், சத்தீஸ்கர் (பீகார் அல்ல). தலைமையகம்: பிரயாக்ராஜ்.",
        "Central Zonal Council is headquartered at Prayagraj with UP, MP, Uttarakhand, and Chhattisgarh as members.",
        "மத்திய மண்டலக் குழு பிரயாக்ராஜைத் தலைமையகமாகக் கொண்டு உ.பி, ம.பி, உத்தராகண்ட், சத்தீஸ்கரை உறுப்பினர்களாகக் கொண்டுள்ளது.",
        tags=["Central Zonal Council", "Prayagraj HQ", "Member States"]
    ))

    # 029 - Ans B
    q.append(make_q(
        "ISR_S_029", "Medium",
        "Consider the following statements regarding the Eastern Zonal Council:\n1. The headquarters of the Eastern Zonal Council is situated at Bhubaneswar.\n2. The member States of the Eastern Zonal Council comprise Bihar, Jharkhand, West Bengal, and Odisha.\nWhich of the statements given above is/are correct?",
        "கிழக்கு மண்டலக் குழு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. கிழக்கு மண்டலக் குழுவின் தலைமையகம் புவனேஸ்வரில் அமைந்துள்ளது.\n2. பீகார், ஜார்க்கண்ட், மேற்கு வங்காளம் மற்றும் ஒடிசா ஆகியவை கிழக்கு மண்டலக் குழுவின் உறுப்பு மாநிலங்கள் ஆகும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "B",
        "Statement 1 is incorrect: The headquarters of the Eastern Zonal Council is located at Kolkata, not Bhubaneswar. Statement 2 is correct: Its member States are Bihar, Jharkhand, West Bengal, and Odisha.",
        "கூற்று 1 தவறு: கிழக்கு மண்டலக் குழுவின் தலைமையகம் கொல்கத்தாவில் உள்ளது, புவனேஸ்வரில் அல்ல. கூற்று 2 சரி: பீகார், ஜார்க்கண்ட், மேற்கு வங்காளம் மற்றும் ஒடிசா ஆகியவை இதன் உறுப்பு மாநிலங்கள் ஆகும்.",
        "Option A is incorrect because the HQ is Kolkata.", "தலைமையகம் கொல்கத்தா என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because statement 2 accurately lists the four eastern member states.", "கூற்று 2 நான்கு கிழக்கு மாநிலங்களைச் சரியாகக் குறிப்பிடுவதால் விருப்பம் B சரி.",
        "Option C is incorrect because statement 1 is inaccurate.", "கூற்று 1 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 2 is factually true.", "கூற்று 2 உண்மையானது என்பதால் விருப்பம் D தவறு.",
        "Eastern Zonal Council HQ: Kolkata. Member States: Bihar, Jharkhand, Odisha, West Bengal.",
        "கிழக்கு மண்டலக் குழு தலைமையகம்: கொல்கத்தா. உறுப்பு மாநிலங்கள்: பீகார், ஜார்க்கண்ட், ஒடிசா, மேற்கு வங்காளம்.",
        "Eastern Zonal Council is headquartered in Kolkata and includes Bihar, Jharkhand, Odisha, and West Bengal.",
        "கிழக்கு மண்டலக் குழு கொல்கத்தாவைத் தலைமையகமாகக் கொண்டு பீகார், ஜார்க்கண்ட், ஒடிசா, மேற்கு வங்காளத்தை உள்ளடக்கியுள்ளது.",
        tags=["Eastern Zonal Council", "Kolkata HQ", "Member States"]
    ))

    # 030 - Ans D
    q.append(make_q(
        "ISR_S_030", "Medium",
        "Consider the following statements regarding the Western Zonal Council:\n1. The headquarters of the Western Zonal Council is located at Mumbai.\n2. The Council comprises the States of Goa, Gujarat, Maharashtra, and the Union Territory of Dadra and Nagar Haveli and Daman and Diu.\nWhich of the statements given above is/are correct?",
        "மேற்கு மண்டலக் குழு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. மேற்கு மண்டலக் குழுவின் தலைமையகம் மும்பையில் அமைந்துள்ளது.\n2. இக்குழுவில் கோவா, குஜராத், மகாராஷ்டிரா மற்றும் தாத்ரா & நகர் ஹவேலி மற்றும் டாமன் & டையூ யூனியன் பிரதேசம் ஆகியவை அடங்கும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "D",
        "Both statements are correct: The Western Zonal Council is headquartered at Mumbai and comprises Goa, Gujarat, Maharashtra, and the merged UT of Dadra and Nagar Haveli and Daman and Diu.",
        "இரண்டு கூற்றுகளும் சரியானவை: மேற்கு மண்டலக் குழுவின் தலைமையகம் மும்பையில் அமைந்துள்ளது; கோவா, குஜராத், மகாராஷ்டிரா மற்றும் இணைக்கப்பட்ட தாத்ரா & நகர் ஹவேலி மற்றும் டாமன் & டையூ ஆகியவை இதன் உறுப்பினர்களாக உள்ளன.",
        "Option A is incorrect because statement 2 is also completely true.", "கூற்று 2-ம் முற்றிலும் உண்மை என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because statement 1 is also completely true.", "கூற்று 1-ம் முற்றிலும் உண்மை என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because neither statement is false.", "எந்தக் கூற்றும் தவறானது அல்ல என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because both statements are factually and structurally accurate.", "இரண்டு கூற்றுகளும் சரியானவை என்பதால் விருப்பம் D சரி.",
        "Western Zonal Council HQ: Mumbai. Member States: Goa, Gujarat, Maharashtra, UT of DNH & DD.",
        "மேற்கு மண்டலக் குழு தலைமையகம்: மும்பை. உறுப்பினர்கள்: கோவா, குஜராத், மகாராஷ்டிரா, தாத்ரா நகர் ஹவேலி & டாமன் டையூ.",
        "Western Zonal Council is headquartered in Mumbai and covers Goa, Gujarat, Maharashtra, and DNH & DD.",
        "மேற்கு மண்டலக் குழு மும்பையைத் தலைமையகமாகக் கொண்டு கோவா, குஜராத், மகாராஷ்டிரா, DNH & DD-ஐ உள்ளடக்கியுள்ளது.",
        tags=["Western Zonal Council", "Mumbai HQ", "Goa Gujarat Maharashtra"]
    ))

    # 031 - Ans A
    q.append(make_q(
        "ISR_S_031", "Medium",
        "Consider the following statements regarding the Southern Zonal Council:\n1. The Southern Zonal Council has its headquarters located at Chennai.\n2. The member units comprise Andhra Pradesh, Karnataka, Kerala, Tamil Nadu, Telangana, and the Union Territory of Andaman and Nicobar Islands.\nWhich of the statements given above is/are correct?",
        "தெற்கு மண்டலக் குழு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. தெற்கு மண்டலக் குழுவின் தலைமையகம் சென்னையில் அமைந்துள்ளது.\n2. ஆந்திரப் பிரதேசம், கர்நாடகா, கேரளா, தமிழ்நாடு, தெலுங்கானா மற்றும் அந்தமான் நிக்கோபார் தீவுகள் யூனியன் பிரதேசம் ஆகியவை இதன் உறுப்புப் பகுதிகளாகும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "A",
        "Statement 1 is correct: Chennai is the headquarters of the Southern Zonal Council. Statement 2 is incorrect: Member units of the Southern Zonal Council are Andhra Pradesh, Karnataka, Kerala, Tamil Nadu, Telangana, and PUDUCHERRY. Andaman and Nicobar Islands and Lakshadweep are not members of any Zonal Council, though they are special invitees.",
        "கூற்று 1 சரி: தெற்கு மண்டலக் குழுவின் தலைமையகம் சென்னையில் உள்ளது. கூற்று 2 தவறு: ஆந்திரா, கர்நாடகா, கேரளா, தமிழ்நாடு, தெலுங்கானா மற்றும் புதுச்சேரி ஆகியவையே இதன் உறுப்பினர்கள். அந்தமான் நிக்கோபார் தீவுகள் மற்றும் லட்சத்தீவு எந்த மண்டலக் குழுவிலும் நிரந்தர உறுப்பினர்கள் அல்ல.",
        "Option A is correct because statement 1 is true and statement 2 mistakenly includes Andaman and Nicobar Islands.", "கூற்று 1 சரியானது மற்றும் கூற்று 2 அந்தமான் நிக்கோபார் தீவுகளைத் தவறாகச் சேர்த்துள்ளதால் விருப்பம் A சரி.",
        "Option B is incorrect because Puducherry is the UT member, not Andaman and Nicobar Islands.", "புதுச்சேரியே யூனியன் பிரதேச உறுப்பினர் என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because statement 2 is false.", "கூற்று 2 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 1 is verified.", "கூற்று 1 சரிபார்க்கப்பட்ட உண்மை என்பதால் விருப்பம் D தவறு.",
        "Southern Zonal Council: HQ Chennai. Members: AP, KA, KL, TN, TS, and Puducherry (NOT Andaman & Nicobar).",
        "தெற்கு மண்டலக் குழு: தலைமையகம் சென்னை. உறுப்பினர்கள்: ஆந்திரா, கர்நாடகா, கேரளா, தமிழ்நாடு, தெலுங்கானா, புதுச்சேரி (அந்தமான் அல்ல).",
        "Southern Zonal Council is headquartered at Chennai and includes the southern states plus Puducherry.",
        "தெற்கு மண்டலக் குழு சென்னையைத் தலைமையகமாகக் கொண்டு தென் மாநிலங்கள் மற்றும் புதுச்சேரியை உள்ளடக்கியுள்ளது.",
        tags=["Southern Zonal Council", "Chennai HQ", "TNPSC Core Fact"]
    ))

    # 032 - Ans B
    q.append(make_q(
        "ISR_S_032", "Medium",
        "Consider the following statements regarding the leadership of Zonal Councils:\n1. The Prime Minister serves as the common Chairman of all the five Zonal Councils.\n2. The Union Home Minister acts as the common Chairman of all five Zonal Councils.\nWhich of the statements given above is/are correct?",
        "மண்டலக் குழுக்களின் தலைமை தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஐந்து மண்டலக் குழுக்களுக்கும் பிரதமர் பொதுவான தலைவராகச் செயல்படுகிறார்.\n2. மத்திய உள்துறை அமைச்சர் ஐந்து மண்டலக் குழுக்களுக்கும் பொதுவான தலைவராகச் செயல்படுகிறார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "B",
        "Statement 1 is incorrect: The Prime Minister chairs the Inter-State Council, but does NOT chair the Zonal Councils. Statement 2 is correct: The Union Home Minister is the common Chairman of all five Zonal Councils established under the States Reorganisation Act, 1956.",
        "கூற்று 1 தவறு: பிரதமர் மாநிலங்களுக்கு இடையிலான மன்றத்திற்குத் தலைமை தாங்குகிறார், மண்டலக் குழுக்களுக்கு அல்ல. கூற்று 2 சரி: மத்திய உள்துறை அமைச்சரே ஐந்து மண்டலக் குழுக்களுக்கும் பொதுவான தலைவராகச் செயல்படுகிறார்.",
        "Option A is incorrect because the PM does not chair Zonal Councils.", "பிரதமர் மண்டலக் குழுக்களுக்குத் தலைமை தாங்குவதில்லை என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because the Union Home Minister is the statutory common Chairman of all Zonal Councils.", "மத்திய உள்துறை அமைச்சரே மண்டலக் குழுக்களின் பொதுத் தலைவர் என்பதால் விருப்பம் B சரி.",
        "Option C is incorrect because statement 1 is false.", "கூற்று 1 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 2 is true.", "கூற்று 2 உண்மையானது என்பதால் விருப்பம் D தவறு.",
        "Crucial distinction: PM chairs Inter-State Council; Union Home Minister chairs all Zonal Councils!",
        "முக்கிய வேறுபாடு: பிரதமர் மாநிலங்களுக்கு இடையிலான மன்றத்தின் தலைவர்; மத்திய உள்துறை அமைச்சர் மண்டலக் குழுக்களின் தலைவர்!",
        "Union Home Minister acts as the common Chairman for all five statutory Zonal Councils.",
        "ஐந்து சட்டப்பூர்வ மண்டலக் குழுக்களுக்கும் மத்திய உள்துறை அமைச்சர் பொதுத் தலைவராகச் செயல்படுகிறார்.",
        tags=["Zonal Council Chairman", "Union Home Minister", "States Reorganisation Act"]
    ))

    # 033 - Ans C
    q.append(make_q(
        "ISR_S_033", "Hard",
        "Consider the following statements regarding the Vice-Chairman of a Zonal Council:\n1. The Chief Ministers of the member States included in each zone act as Vice-Chairman by rotation.\n2. Each Chief Minister holds the office of Vice-Chairman for a period of one year at a time.\nWhich of the statements given above is/are correct?",
        "மண்டலக் குழுவின் துணைத் தலைவர் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. ஒவ்வொரு மண்டலத்திலும் உள்ள உறுப்பு மாநிலங்களின் முதலமைச்சர்கள் சுழற்சி முறையில் துணைத் தலைவராகச் செயல்படுகின்றனர்.\n2. ஒவ்வொரு முதலமைச்சரும் ஒரு நேரத்தில் ஒரு வருட காலத்திற்கு துணைத் தலைவர் பதவியை வகிக்கின்றனர்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "C",
        "Both statements are correct: Under the States Reorganisation Act, 1956, the Chief Minister of each member State in the zone acts as the Vice-Chairman of the Zonal Council by rotation, holding office for a period of one year at a time.",
        "இரண்டு கூற்றுகளும் சரியானவை: 1956 மாநில மறுசீரமைப்புச் சட்டத்தின்படி, மண்டலத்தில் உள்ள உறுப்பு மாநிலங்களின் முதலமைச்சர்கள் சுழற்சி முறையில் துணைத் தலைவராகப் பதவி வகிக்கின்றனர்; ஒவ்வொரு முதலமைச்சரும் ஒரு ஆண்டு காலத்திற்கு இப்பதவியை வகிக்கின்றனர்.",
        "Option A is incorrect because statement 2 is also completely true.", "கூற்று 2-ம் முற்றிலும் உண்மை என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because statement 1 is also completely true.", "கூற்று 1-ம் முற்றிலும் உண்மை என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because both statements accurately describe the rotation and tenure of Zonal Council Vice-Chairmen.", "சுழற்சி முறை மற்றும் 1 ஆண்டு பதவிக் காலத்தை இரண்டு கூற்றுகளும் சரியாக விளக்குவதால் விருப்பம் C சரி.",
        "Option D is incorrect because neither statement is false.", "எந்தக் கூற்றும் தவறானது அல்ல என்பதால் விருப்பம் D தவறு.",
        "Zonal Council Vice-Chairman rotates among member Chief Ministers annually (1 year tenure).",
        "மண்டலக் குழுவின் துணைத் தலைவர் பதவி உறுப்பு மாநில முதலமைச்சர்களிடையே ஆண்டுதோறும் சுழற்சி முறையில் (1 ஆண்டு) மாறுகிறது.",
        "Chief Ministers of member states hold the office of Zonal Council Vice-Chairman for one year by rotation.",
        "உறுப்பு மாநில முதலமைச்சர்கள் சுழற்சி முறையில் ஓராண்டு காலத்திற்கு மண்டலக் குழு துணைத் தலைவராகப் பதவி வகிக்கின்றனர்.",
        tags=["Zonal Council Vice-Chairman", "Annual Rotation", "Chief Ministers"]
    ))

    # 034 - Ans D
    q.append(make_q(
        "ISR_S_034", "Medium",
        "Consider the following statements regarding the North-Eastern Council (NEC):\n1. The North-Eastern Council was created under the States Reorganisation Act, 1956 as the sixth zonal council.\n2. Sikkim was included as an original founding member of the North-Eastern Council in 1971.\nWhich of the statements given above is/are correct?",
        "வடகிழக்குக் குழு (NEC) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. வடகிழக்குக் குழு 1956-ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் ஆறாவது மண்டலக் குழுவாக உருவாக்கப்பட்டது.\n2. 1971-ல் வடகிழக்குக் குழுவின் அசல் நிறுவன உறுப்பினராக சிக்கிம் சேர்க்கப்பட்டது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "D",
        "Both statements are incorrect: Statement 1 is incorrect: The North-Eastern Council was created under a separate statutory act, the North-Eastern Council Act, 1971 (not the States Reorganisation Act 1956). Statement 2 is incorrect: Sikkim was NOT a founding member in 1971; Sikkim was added to the NEC much later in December 2002 via the North-Eastern Council (Amendment) Act, 2002, becoming the 8th member.",
        "இரண்டு கூற்றுகளும் தவறானவை: கூற்று 1 தவறு: வடகிழக்குக் குழு 1971-ஆம் ஆண்டின் தனிச் சட்டமான வடகிழக்குக் குழு சட்டம் 1971-ன் கீழ் உருவாக்கப்பட்டது (1956 சட்டத்தின் கீழ் அல்ல). கூற்று 2 தவறு: சிக்கிம் 1971-ல் நிறுவன உறுப்பினர் அல்ல; 2002-ல் செய்யப்பட்ட சட்டத் திருத்தத்தின் மூலமே சிக்கிம் 8-வது உறுப்பினராகச் சேர்க்கப்பட்டது.",
        "Option A is incorrect because the NEC was created under the 1971 Act.", "NEC 1971 சட்டத்தின் கீழ் உருவாக்கப்பட்டதால் விருப்பம் A தவறு.",
        "Option B is incorrect because Sikkim joined in 2002, not 1971.", "சிக்கிம் 2002-ல் இணைந்ததால் விருப்பம் B தவறு.",
        "Option C is incorrect because both statements are factually flawed.", "இரண்டு கூற்றுகளும் தவறானவை என்பதால் விருப்பம் C தவறு.",
        "Option D is correct as both statements distort the origin and expansion of the North-Eastern Council.", "இரண்டு கூற்றுகளும் NEC-ன் தோற்றம் மற்றும் விரிவாக்கம் குறித்துத் தவறான தகவல்களைக் கொண்டுள்ளதால் விருப்பம் D சரி.",
        "North-Eastern Council: Created under NEC Act 1971 (NOT 1956 Act); Sikkim added in 2002 (8th state).",
        "வடகிழக்குக் குழு: 1971 NEC சட்டத்தின் கீழ் உருவானது (1956 சட்டம் அல்ல); சிக்கிம் 2002-ல் 8-வது மாநிலமாக இணைந்தது.",
        "North-Eastern Council was created by the NEC Act 1971, with Sikkim included in 2002.",
        "வடகிழக்குக் குழு 1971 சட்டத்தால் உருவாக்கப்பட்டது; சிக்கிம் 2002-ல் இதில் இணைக்கப்பட்டது.",
        tags=["North-Eastern Council", "NEC Act 1971", "Sikkim Addition 2002"]
    ))

    # 035 - Ans D
    q.append(make_q(
        "ISR_S_035", "Hard",
        "Consider the following statements regarding the leadership of the North-Eastern Council (NEC):\n1. Following the 2018 amendment by the Union Cabinet, the Union Home Minister serves as the ex-officio Chairman of the North-Eastern Council.\n2. The Minister of State (Independent Charge), Ministry of Development of North Eastern Region (DoNER) serves as the Vice-Chairman of the Council.\nWhich of the statements given above is/are correct?",
        "வடகிழக்குக் குழுவின் (NEC) தலைமை தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. 2018-ல் மத்திய அமைச்சரவை மேற்கொண்ட திருத்தத்தைத் தொடர்ந்து, மத்திய உள்துறை அமைச்சர் வடகிழக்குக் குழுவின் அலுவல்சார் தலைவராகச் செயல்படுகிறார்.\n2. வடகிழக்கு பிராந்திய மேம்பாட்டு அமைச்சகத்தின் (DoNER) இணை அமைச்சர் (தனிப்பொறுப்பு) இக்குழுவின் துணைத் தலைவராகச் செயல்படுகிறார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "D",
        "Both statements are correct: In June 2018, the Union Cabinet approved the nomination of the Union Home Minister as ex-officio Chairman of the North-Eastern Council and the Minister of State (Independent Charge), Ministry of Development of North Eastern Region (DoNER) as Vice-Chairman.",
        "இரண்டு கூற்றுகளும் சரியானவை: ஜூன் 2018-ல் மத்திய அமைச்சரவை எடுத்த முடிவின்படி, மத்திய உள்துறை அமைச்சர் வடகிழக்குக் குழுவின் அலுவல்சார் தலைவராகவும், DoNER அமைச்சகத்தின் இணை அமைச்சர் (தனிப்பொறுப்பு) துணைத் தலைவராகவும் நியமிக்கப்பட்டனர்.",
        "Option A is incorrect because statement 2 is also completely accurate.", "கூற்று 2-ம் முற்றிலும் சரியானது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because statement 1 is also completely accurate.", "கூற்று 1-ம் முற்றிலும் சரியானது என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because neither statement is false.", "எந்தக் கூற்றும் தவறானது அல்ல என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because both Chairman (Home Minister) and Vice-Chairman (DoNER Minister) designations were restructured in 2018.", "தலைவர் (உள்துறை அமைச்சர்) மற்றும் துணைத் தலைவர் (DoNER அமைச்சர்) நிலைகள் இரண்டும் 2018-ல் மாற்றியமைக்கப்பட்டதால் விருப்பம் D சரி.",
        "NEC leadership post-2018: Union Home Minister = Chairman; DoNER Minister = Vice-Chairman.",
        "2018-க்குப் பின் NEC தலைமை: மத்திய உள்துறை அமைச்சர் = தலைவர்; DoNER அமைச்சர் = துணைத் தலைவர்.",
        "Union Home Minister chairs the North-Eastern Council while DoNER Minister serves as Vice-Chairman.",
        "மத்திய உள்துறை அமைச்சர் வடகிழக்குக் குழுவின் தலைவராகவும், DoNER அமைச்சர் துணைத் தலைவராகவும் செயல்படுகின்றனர்.",
        tags=["NEC Leadership", "Home Minister Chairman", "DoNER Vice-Chairman"]
    ))

    # 036 - Ans B
    q.append(make_q(
        "ISR_S_036", "Medium",
        "Consider the following statements regarding the advisory mandate of Zonal Councils under the States Reorganisation Act, 1956:\n1. A Zonal Council may make recommendations to the Union Government and the member States regarding any matter of common interest in the field of economic and social planning.\n2. Decisions taken by a majority vote in a Zonal Council meeting are legally binding on all participating State legislatures.\nWhich of the statements given above is/are correct?",
        "1956-ஆம் ஆண்டின் மாநில மறுசீரமைப்புச் சட்டத்தின் கீழ் மண்டலக் குழுக்களின் ஆலோசனைக் கட்டளை தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பொருளாதார மற்றும் சமூகத் திட்டமிடல் துறையில் பொதுவான நலன் சார்ந்த எந்தவொரு விஷயத்திலும் மத்திய அரசுக்கும் உறுப்பு மாநிலங்களுக்கும் மண்டலக் குழு பரிந்துரைகளை வழங்கலாம்.\n2. மண்டலக் குழு கூட்டத்தில் பெரும்பான்மை வாக்குகளால் எடுக்கப்படும் முடிவுகள் பங்கேற்கும் அனைத்து மாநில சட்டமன்றங்களையும் சட்டப்பூர்வமாகக் கட்டுப்படுத்தும்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "A",
        "Statement 1 is correct: Under Section 21 of the States Reorganisation Act, 1956, Zonal Councils are advisory bodies empowered to discuss and make recommendations on economic and social planning, border disputes, linguistic minorities, and inter-state transport. Statement 2 is incorrect: Recommendations of Zonal Councils are purely advisory and have no legally binding effect on any State legislature or government.",
        "கூற்று 1 சரி: 1956 சட்டத்தின் பிரிவு 21-ன் படி, மண்டலக் குழுக்கள் பொருளாதாரத் திட்டமிடல், எல்லைப் பிரச்சினைகள், மொழிச் சிறுபான்மையினர் மற்றும் போக்குவரத்து குறித்துப் பரிந்துரைகளை வழங்கலாம். கூற்று 2 தவறு: மண்டலக் குழுவின் பரிந்துரைகள் ஆலோசனையே அன்றி எந்த மாநில சட்டமன்றத்தையும் சட்டப்பூர்வமாகக் கட்டுப்படுத்தாது.",
        "Option A is correct because statement 1 reflects Section 21 and statement 2 falsely claims binding legal force.", "கூற்று 1 பிரிவு 21-ஐக் குறிப்பிடுவதாலும், கூற்று 2 பிணைக்கும் அதிகாரம் இருப்பதாகத் தவறாகக் கூறுவதாலும் விருப்பம் A சரி.",
        "Option B is incorrect because Zonal Council decisions are non-binding.", "மண்டலக் குழுவின் முடிவுகள் பிணைப்பற்றவை என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because statement 2 is false.", "கூற்று 2 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 1 is factually true.", "கூற்று 1 உண்மையானது என்பதால் விருப்பம் D தவறு.",
        "Zonal Councils are strictly advisory bodies; their recommendations cannot bind any sovereign legislature.",
        "மண்டலக் குழுக்கள் ஆலோசனைக் குழுக்களே; அவற்றின் பரிந்துரைகள் எந்த சட்டமன்றத்தையும் கட்டுப்படுத்தாது.",
        "Zonal Councils make advisory recommendations on economic planning, border issues, and linguistic minorities.",
        "பொருளாதாரத் திட்டமிடல், எல்லை விவகாரங்கள், மொழிச் சிறுபான்மையினர் குறித்து மண்டலக் குழுக்கள் ஆலோசனை வழங்குகின்றன.",
        tags=["Zonal Council Functions", "Advisory Scope", "Section 21"]
    ))

    # 037 - Ans C
    q.append(make_q(
        "ISR_S_037", "Hard",
        "Consider the following statements regarding joint meetings of Zonal Councils:\n1. Two or more Zonal Councils can hold joint meetings to discuss matters of common interest to two or more zones.\n2. The joint meetings of two or more Zonal Councils are presided over by the Union Home Minister.\nWhich of the statements given above is/are correct?",
        "மண்டலக் குழுக்களின் கூட்டுக் கூட்டங்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இரண்டு அல்லது அதற்கு மேற்பட்ட மண்டலங்களுக்குப் பொதுவான நலன் சார்ந்த விஷயங்களை விவாதிக்க இரண்டு அல்லது அதற்கு மேற்பட்ட மண்டலக் குழுக்கள் கூட்டுக் கூட்டங்களை நடத்தலாம்.\n2. இரண்டு அல்லது அதற்கு மேற்பட்ட மண்டலக் குழுக்களின் கூட்டுக் கூட்டங்களுக்கு மத்திய உள்துறை அமைச்சர் தலைமை தாங்குகிறார்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "C",
        "Both statements are correct: Under Section 22 of the States Reorganisation Act, 1956: (1) Where it is desirable that two or more Zonal Councils should discuss a matter of common interest, they may hold joint meetings; (2) The joint meeting is presided over by the Union Home Minister (as the common Chairman).",
        "இரண்டு கூற்றுகளும் சரியானவை: 1956 மாநில மறுசீரமைப்புச் சட்டத்தின் பிரிவு 22-ன் படி: (1) பொதுவான விஷயங்களை விவாதிக்க இரண்டு அல்லது அதற்கு மேற்பட்ட மண்டலக் குழுக்கள் கூட்டுக் கூட்டங்களை நடத்தலாம்; (2) அத்தகைய கூட்டுக் கூட்டங்களுக்கு மத்திய உள்துறை அமைச்சர் தலைமை தாங்குகிறார்.",
        "Option A is incorrect because statement 2 is equally valid under Section 22.", "கூற்று 2-ம் பிரிவு 22-ன் கீழ் சரியானது என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because statement 1 is equally valid under Section 22.", "கூற்று 1-ம் பிரிவு 22-ன் கீழ் சரியானது என்பதால் விருப்பம் B தவறு.",
        "Option C is correct as Section 22 expressly provides for joint meetings presided over by the Union Home Minister.", "பிரிவு 22 கூட்டுக் கூட்டங்களுக்கும் அதற்கு உள்துறை அமைச்சர் தலைமை தாங்குவதற்கும் வழிவகை செய்வதால் விருப்பம் C சரி.",
        "Option D is incorrect because neither statement is false.", "எந்தக் கூற்றும் தவறானது அல்ல என்பதால் விருப்பம் D தவறு.",
        "Section 22 of 1956 Act enables joint meetings of Zonal Councils presided over by the Union Home Minister.",
        "1956 சட்டத்தின் பிரிவு 22 உள்துறை அமைச்சர் தலைமையில் மண்டலக் குழுக்களின் கூட்டுக் கூட்டங்களை நடத்த வகை செய்கிறது.",
        "Joint meetings of Zonal Councils can be held under the 1956 Act, presided over by the Union Home Minister.",
        "மத்திய உள்துறை அமைச்சர் தலைமையில் மண்டலக் குழுக்களின் கூட்டுக் கூட்டங்கள் 1956 சட்டத்தின் கீழ் நடத்தப்படலாம்.",
        tags=["Joint Zonal Meetings", "Section 22", "Union Home Minister"]
    ))

    # 038 - Ans D
    q.append(make_q(
        "ISR_S_038", "Medium",
        "Consider the following statements regarding the scope of Article 301 in Part XIII of the Constitution:\n1. Freedom of trade, commerce, and intercourse under Article 301 is restricted exclusively to interstate transactions across State borders.\n2. Intra-state trade within the borders of a single State is completely excluded from the protective ambit of Article 301.\nWhich of the statements given above is/are correct?",
        "அரசியலமைப்பின் பகுதி XIII-ல் உள்ள உறுப்பு 301-ன் வரம்பு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. உறுப்பு 301-ன் கீழான வர்த்தகம், வணிகம் மற்றும் உடனுறைவு சுதந்திரம் மாநில எல்லைகளைத் தாண்டிய மாநிலங்களுக்கு இடையிலான பரிவர்த்தனைகளுக்கு மட்டுமே பிரத்யேகமாகக் கட்டுப்படுத்தப்பட்டுள்ளது.\n2. ஒரே மாநிலத்தின் எல்லைக்குள் நடைபெறும் மாநிலத்திற்குள்ளான (intra-state) வர்த்தகம் உறுப்பு 301-ன் பாதுகாப்பு வரம்பிலிருந்து முற்றிலுமாக விலக்கப்பட்டுள்ளது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "D",
        "Both statements are incorrect: Article 301 explicitly declares that 'trade, commerce and intercourse throughout the territory of India shall be free'. The Supreme Court has repeatedly held (e.g., in the Atiabari Tea Co. case) that the freedom guaranteed by Article 301 applies not only to inter-State trade (between different States) but also to intra-State trade (within the borders of a single State).",
        "இரண்டு கூற்றுகளும் தவறானவை: உறுப்பு 301 'இந்தியா முழுவதும் வர்த்தகம், வணிகம் மற்றும் தொடர்பு சுதந்திரமாக இருக்க வேண்டும்' என்று கூறுகிறது. அத்தியாபாரி வழக்கில் உச்ச நீதிமன்றம் தெளிவுபடுத்தியபடி, உறுப்பு 301 மாநிலங்களுக்கு இடையிலான வர்த்தகத்திற்கு மட்டுமல்லாமல், ஒரு மாநிலத்திற்குள்ளான (intra-state) வர்த்தகத்திற்கும் சமமாகப் பொருந்தும்.",
        "Option A is incorrect because Article 301 covers intra-state trade as well.", "உறுப்பு 301 மாநிலத்திற்குள்ளான வர்த்தகத்தையும் உள்ளடக்கியதால் விருப்பம் A தவறு.",
        "Option B is incorrect because intra-state trade is protected under Article 301.", "மாநிலத்திற்குள்ளான வர்த்தகமும் உறுப்பு 301-ல் பாதுகாக்கப்படுவதால் விருப்பம் B தவறு.",
        "Option C is incorrect because both statements are contrary to settled constitutional law.", "இரண்டு கூற்றுகளும் அரசியலமைப்புச் சட்டத்திற்கு முரணாக உள்ளதால் விருப்பம் C தவறு.",
        "Option D is correct because Article 301 protects both inter-state and intra-state freedom of trade and commerce.", "உறுப்பு 301 மாநிலங்களுக்கு இடையேயான மற்றும் மாநிலத்திற்குள்ளான வர்த்தகச் சுதந்திரத்தைப் பாதுகாப்பதால் விருப்பம் D சரி.",
        "Article 301 applies throughout India to BOTH inter-State trade AND intra-State trade.",
        "உறுப்பு 301 இந்தியா முழுவதும் மாநிலங்களுக்கு இடையேயான மற்றும் மாநிலத்திற்குள்ளான வர்த்தகம் இரண்டிற்கும் பொருந்தும்.",
        "Article 301 guarantees trade, commerce, and intercourse freedom across both inter-state and intra-state borders.",
        "உறுப்பு 301 மாநிலங்களுக்கு இடையேயான மற்றும் மாநிலத்திற்குள்ளான வர்த்தகச் சுதந்திரத்தை உறுதி செய்கிறது.",
        tags=["Article 301", "Freedom of Trade", "Inter-State and Intra-State"]
    ))

    # 039 - Ans A
    q.append(make_q(
        "ISR_S_039", "Hard",
        "Consider the following statements regarding the source of Part XIII of the Indian Constitution:\n1. The framers of the Indian Constitution derived the concept of freedom of trade, commerce, and intercourse principally from Section 92 of the Australian Constitution.\n2. Unlike the Australian provision which is absolute in terms, the Indian Constitution incorporates extensive qualifications and exceptions in Articles 302 to 305.\nWhich of the statements given above is/are correct?",
        "இந்திய அரசியலமைப்பின் பகுதி XIII-ன் மூலங்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. இந்திய அரசியலமைப்பை உருவாக்கியவர்கள் வர்த்தகம், வணிகம் மற்றும் தொடர்பு சுதந்திரம் என்ற கருத்தை முக்கியமாக ஆஸ்திரேலிய அரசியலமைப்பின் பிரிவு 92-லிருந்து பெற்றனர்.\n2. ஆஸ்திரேலிய விதி நிபந்தனையற்றதாக உள்ளதைப் போலல்லாமல், இந்திய அரசியலமைப்பு உறுப்புகள் 302 முதல் 305 வரை விரிவான கட்டுப்பாடுகள் மற்றும் விதிவிலக்குகளை உள்ளடக்கியுள்ளது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "C",
        "Both statements are correct: Statement 1 is correct: Part XIII was heavily inspired by Section 92 of the Australian Constitution ('trade, commerce, and intercourse among the States... shall be absolutely free'). Statement 2 is correct: While Australia's Section 92 led to endless litigation because it lacked built-in qualifications, the Indian framers deliberately balanced freedom in Article 301 with regulatory powers and state monopolies in Articles 302–305.",
        "இரண்டு கூற்றுகளும் சரியானவை: கூற்று 1 சரி: பகுதி XIII ஆஸ்திரேலிய அரசியலமைப்பின் பிரிவு 92-ன் தாக்கத்தால் உருவாக்கப்பட்டது. கூற்று 2 சரி: ஆஸ்திரேலிய விதியில் வரம்புகள் இல்லாததால் பல வழக்குகள் எழுந்தன; எனவே இந்திய அரசியலமைப்பு வல்லுநர்கள் உறுப்புகள் 302 முதல் 305 வரை கட்டுப்பாடுகள் மற்றும் விதிவிலக்குகளைத் தெளிவாகச் சேர்த்தனர்.",
        "Option A is incorrect because statement 2 is also an established comparative constitutional fact.", "கூற்று 2-ம் சரியான ஒப்பீட்டு அரசியலமைப்பு உண்மை என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because statement 1 is also completely accurate.", "கூற்று 1-ம் முற்றிலும் சரியானது என்பதால் விருப்பம் B தவறு.",
        "Option C is correct as both the Australian origin and the intentional Indian regulatory exceptions are accurate.", "ஆஸ்திரேலிய தோற்றம் மற்றும் இந்திய கட்டுப்பாட்டு விதிவிலக்குகள் இரண்டும் சரியானவை என்பதால் விருப்பம் C சரி.",
        "Option D is incorrect because neither statement is false.", "எந்தக் கூற்றும் தவறானது அல்ல என்பதால் விருப்பம் D தவறு.",
        "Trade freedom origin: Australian Constitution (Section 92), but balanced with Indian statutory exceptions (Articles 302-305).",
        "வர்த்தக சுதந்திரத்தின் மூலம்: ஆஸ்திரேலிய அரசியலமைப்பு (பிரிவு 92), ஆனால் இந்தியாவில் உறுப்புகள் 302-305 மூலம் கட்டுப்பாடுகள் உள்ளன.",
        "Article 301 draws from Section 92 of the Australian Constitution but incorporates specific constitutional restrictions.",
        "உறுப்பு 301 ஆஸ்திரேலிய அரசியலமைப்பின் பிரிவு 92-ஐ அடிப்படையாகக் கொண்டிருந்தாலும் தெளிவான கட்டுப்பாடுகளைக் கொண்டுள்ளது.",
        tags=["Australian Constitution", "Section 92", "Comparative Polity"]
    ))

    # 040 - Ans B
    q.append(make_q(
        "ISR_S_040", "Medium",
        "Consider the following statements regarding Parliament's power under Article 302 of the Constitution:\n1. Parliament can impose restrictions on the freedom of trade, commerce, or intercourse only during a declared National Emergency under Article 352.\n2. Parliament may by law impose such restrictions on the freedom of trade, commerce, or intercourse between one State and another as may be required in the public interest.\nWhich of the statements given above is/are correct?",
        "அரசியலமைப்பின் 302-வது உறுப்பின் கீழ் நாடாளுமன்றத்தின் அதிகாரம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. உறுப்பு 352-ன் கீழ் அறிவிக்கப்பட்ட தேசிய அவசரநிலையின் போது மட்டுமே வர்த்தகம், வணிகம் அல்லது தொடர்பு சுதந்திரத்தின் மீது நாடாளுமன்றம் கட்டுப்பாடுகளை விதிக்க முடியும்.\n2. பொது நலனுக்குத் தேவைப்படும் பட்சத்தில், ஒரு மாநிலத்திற்கும் மற்றொரு மாநிலத்திற்கும் இடையேயான வர்த்தகம், வணிகம் அல்லது தொடர்பு சுதந்திரத்தின் மீது நாடாளுமன்றம் சட்டத்தின் மூலம் கட்டுப்பாடுகளை விதிக்கலாம்.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "B",
        "Statement 1 is incorrect: Article 302 is an ordinary legislative power that can be exercised at any time in the public interest, not restricted to emergency situations. Statement 2 is correct: Article 302 empowers Parliament by law to impose such restrictions on the freedom of trade, commerce or intercourse between one State and another or within any part of the territory of India as may be required in the public interest.",
        "கூற்று 1 தவறு: உறுப்பு 302 என்பது சாதாரண சட்டமியற்றும் அதிகாரமாகும்; இது பொது நலனுக்காக எப்போது வேண்டுமானாலும் பயன்படுத்தப்படலாம், அவசரநிலைக்கு மட்டும் உரியதல்ல. கூற்று 2 சரி: பொது நலனைக் கருதி மாநிலங்களுக்கு இடையேயான வர்த்தகத்தின் மீது நாடாளுமன்றம் சட்டத்தின் மூலம் கட்டுப்பாடுகளை விதிக்கலாம் என்று உறுப்பு 302 கூறுகிறது.",
        "Option A is incorrect because Article 302 does not require a proclamation of emergency.", "உறுப்பு 302-க்கு அவசரநிலை தேவைப்படாது என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because statement 2 captures the precise wording and scope of Article 302.", "கூற்று 2 உறுப்பு 302-ன் வாசகங்களைச் சரியாகக் குறிப்பிடுவதால் விருப்பம் B சரி.",
        "Option C is incorrect because statement 1 is false.", "கூற்று 1 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 2 is completely true.", "கூற்று 2 முற்றிலும் சரியானது என்பதால் விருப்பம் D தவறு.",
        "Article 302 gives Parliament power to impose restrictions in the 'public interest' in ordinary times.",
        "உறுப்பு 302 சாதாரண காலங்களிலும் 'பொது நலன்' கருதி கட்டுப்பாடுகளை விதிக்க நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது.",
        "Parliament can impose trade restrictions under Article 302 as required in the public interest.",
        "பொது நலன் கருதி உறுப்பு 302-ன் கீழ் வர்த்தகக் கட்டுப்பாடுகளை விதிக்க நாடாளுமன்றத்திற்கு அதிகாரம் உண்டு.",
        tags=["Article 302", "Parliamentary Power", "Public Interest Restrictions"]
    ))

    # 041 - Ans C
    q.append(make_q(
        "ISR_S_041", "Hard",
        "Consider the following statements regarding the non-discrimination rule under Article 303:\n1. Neither Parliament nor the Legislature of a State has the power to pass any law giving preference to one State over another by virtue of any entry relating to trade and commerce.\n2. Parliament is permitted an exception under Article 303(2) to make a discriminatory law if it is declared that it is necessary to do so for dealing with a situation arising from scarcity of goods in any part of India.\nWhich of the statements given above is/are correct?",
        "உறுப்பு 303-ன் கீழ் உள்ள பாகுபாடற்ற விதி தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. வர்த்தகம் மற்றும் வணிகம் தொடர்பான எந்தவொரு பதிவின் அடிப்படையிலும் ஒரு மாநிலத்திற்கு மற்றொரு மாநிலத்தை விட முன்னுரிமை அளிக்கும் சட்டத்தை இயற்ற நாடாளுமன்றத்திற்கோ அல்லது மாநில சட்டமன்றத்திற்கோ அதிகாரம் இல்லை.\n2. இந்தியாவின் எந்தப் பகுதியிலும் பொருட்கள் பற்றாக்குறையால் எழும் சூழ்நிலையைக் கையாள்வதற்கு அவ்வாறு செய்வது அவசியம் என்று அறிவிக்கப்பட்டால், பாகுபாடான சட்டத்தை இயற்ற உறுப்பு 303(2)-ன் கீழ் நாடாளுமன்றத்திற்கு விதிவிலக்கு அனுமதிக்கப்பட்டுள்ளது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "C",
        "Both statements are correct: Statement 1 is correct: Article 303(1) prohibits both Parliament and State Legislatures from making laws giving preference to one State over another or discriminating between States. Statement 2 is correct: Article 303(2) carves out an exception exclusively for Parliament (not State legislatures) to make discriminatory laws for dealing with situations arising from scarcity of goods in any part of India.",
        "இரண்டு கூற்றுகளும் சரியானவை: கூற்று 1 சரி: உறுப்பு 303(1) நாடாளுமன்றமும் மாநில சட்டமன்றங்களும் ஒரு மாநிலத்திற்கு முன்னுரிமை அளிக்கவோ அல்லது பாகுபாடு காட்டவோ கூடாது எனத் தடை செய்கிறது. கூற்று 2 சரி: உறுப்பு 303(2) நாட்டின் எந்தப் பகுதியிலும் பொருட்கள் பற்றாக்குறை ஏற்படும் போது அச்சூழலைக் கையாள நாடாளுமன்றத்திற்கு மட்டுமே பாகுபாடான சட்டங்களை இயற்ற விதிவிலக்கு அளிக்கிறது.",
        "Option A is incorrect because statement 2 is an explicit constitutional exception under Article 303(2).", "கூற்று 2 உறுப்பு 303(2)-ன் தெளிவான அரசியலமைப்பு விதிவிலக்கு என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because statement 1 is also completely accurate under Article 303(1).", "கூற்று 1-ம் உறுப்பு 303(1)-ன் படி சரியானது என்பதால் விருப்பம் B தவறு.",
        "Option C is correct because both the non-discrimination rule and the scarcity exception are authentic constitutional provisions.", "பாகுபாடற்ற விதி மற்றும் பற்றாக்குறை விதிவிலக்கு ஆகிய இரண்டும் சரியானவை என்பதால் விருப்பம் C சரி.",
        "Option D is incorrect because neither statement is false.", "எந்தக் கூற்றும் தவறானது அல்ல என்பதால் விருப்பம் D தவறு.",
        "Article 303 prohibits preference, but allows Parliament ONE exception: Dealing with SCARCITY of goods (Article 303(2)).",
        "உறுப்பு 303 பாகுபாட்டைத் தடை செய்தாலும், பொருட்கள் பற்றாக்குறையைக் கையாள நாடாளுமன்றத்திற்கு மட்டும் விதிவிலக்கு (303(2)) அளிக்கிறது.",
        "Article 303 forbids preference between states, with a sole exception for Parliament during scarcity of goods.",
        "பொருட்கள் பற்றாக்குறையின் போது நாடாளுமன்றத்திற்கு உள்ள விதிவிலக்கு தவிர்த்து, மாநிலங்களிடையே பாகுபாடு காட்டுவதை உறுப்பு 303 தடை செய்கிறது.",
        tags=["Article 303", "Non-Discrimination", "Scarcity Exception"]
    ))

    # 042 - Ans D
    q.append(make_q(
        "ISR_S_042", "Medium",
        "Consider the following statements regarding State taxation powers under Article 304(a):\n1. A State legislature can impose customs import tariffs exclusively on goods imported from neighboring States while exempting locally manufactured goods.\n2. Article 304(a) allows a State to levy a tax on imported goods that is substantially higher than the tax levied on similar goods produced within the State.\nWhich of the statements given above is/are correct?",
        "உறுப்பு 304(a)-ன் கீழ் மாநிலத்தின் வரி விதிக்கும் அதிகாரங்கள் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. உள்ளூரில் உற்பத்தி செய்யப்படும் பொருட்களுக்கு விலக்கு அளித்துவிட்டு, அண்டை மாநிலங்களிலிருந்து இறக்குமதி செய்யப்படும் பொருட்களுக்கு மட்டுமே பிரத்யேகமாக மாநில சட்டமன்றம் இறக்குமதி சுங்க வரிகளை விதிக்க முடியும்.\n2. மாநிலத்தில் உற்பத்தி செய்யப்படும் ஒத்த பொருட்களின் மீது விதிக்கப்படும் வரியை விட கணிசமாக அதிக வரியை இறக்குமதி செய்யப்படும் பொருட்களின் மீது விதிக்க உறுப்பு 304(a) மாநிலத்திற்கு அனுமதிக்கிறது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "D",
        "Both statements are incorrect: Article 304(a) allows a State legislature to impose taxes on goods imported from other States ONLY IF similar goods manufactured or produced in that State are subject to the same tax. It explicitly prohibits discrimination between imported goods and locally produced goods. A State cannot impose a higher tax or discriminatory tariff on outside goods.",
        "இரண்டு கூற்றுகளும் தவறானவை: உறுப்பு 304(a)-ன் படி, உள்ளூரில் உற்பத்தி செய்யப்படும் அதே பொருட்களுக்கு என்ன வரி விதிக்கப்படுகிறதோ, அதே வரியை மட்டுமே பிற மாநிலங்களிலிருந்து வரும் பொருட்கள் மீதும் விதிக்க முடியும். இறக்குமதி செய்யப்படும் பொருட்கள் மீது அதிக வரி விதிக்கவோ அல்லது பாகுபாடு காட்டவோ மாநிலங்களுக்கு உரிமை இல்லை.",
        "Option A is incorrect because States have no power to levy discriminatory tariffs on outside goods.", "வெளியூர் பொருட்கள் மீது பாகுபாடான வரிகளை விதிக்க மாநிலங்களுக்கு அதிகாரம் இல்லை என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because discriminatory higher taxation violates Article 304(a).", "அதிக வரி விதிப்பது உறுப்பு 304(a)-ஐ மீறுவதாகும் என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because both statements are unconstitutional.", "இரண்டு கூற்றுகளும் அரசியலமைப்பிற்கு முரணானவை என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because Article 304(a) mandates strict tax parity between outside and local goods.", "உறுப்பு 304(a) வெளி மாநில மற்றும் உள்ளூர் பொருட்களுக்கு இடையே சமமான வரி விதிப்பைக் கட்டாயமாக்குவதால் விருப்பம் D சரி.",
        "Article 304(a) golden rule: Outside goods can be taxed ONLY if similar local goods are taxed equally (non-discrimination).",
        "உறுப்பு 304(a) பொன்விதி: உள்ளூர் பொருட்களுக்கு விதிக்கப்படும் அதே வரி மட்டுமே வெளி மாநிலப் பொருட்கள் மீதும் விதிக்கப்படலாம்.",
        "Article 304(a) mandates non-discriminatory taxation between imported and locally produced goods.",
        "உறுப்பு 304(a) இறக்குமதி செய்யப்படும் மற்றும் உள்ளூரில் உற்பத்தி செய்யப்படும் பொருட்களிடையே பாகுபாடற்ற வரியை உறுதி செய்கிறது.",
        tags=["Article 304(a)", "State Taxation", "Non-Discriminatory Tax"]
    ))

    # 043 - Ans A
    q.append(make_q(
        "ISR_S_043", "Hard",
        "Consider the following statements regarding the power of a State Legislature under Article 304(b):\n1. A State legislature may by law impose reasonable restrictions on the freedom of trade, commerce, or intercourse with or within that State in the public interest.\n2. No Bill or amendment for the purposes of Article 304(b) shall be introduced or moved in the Legislature of a State without the previous sanction of the President.\nWhich of the statements given above is/are correct?",
        "உறுப்பு 304(b)-ன் கீழ் மாநில சட்டமன்றத்தின் அதிகாரம் தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. பொது நலனைக் கருதி அந்த மாநிலத்துடனோ அல்லது அதற்குள்ளோ வர்த்தகம், வணிகம் அல்லது தொடர்பு சுதந்திரத்தின் மீது மாநில சட்டமன்றம் சட்டத்தின் மூலம் நியாயமான கட்டுப்பாடுகளை விதிக்கலாம்.\n2. குடியரசுத் தலைவரின் முன் அனுமதியின்றி உறுப்பு 304(b)-ன் நோக்கங்களுக்கான எந்தவொரு மசோதாவையும் அல்லது திருத்தத்தையும் மாநில சட்டமன்றத்தில் அறிமுகப்படுத்தவோ அல்லது கொண்டுவரவோ முடியாது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "C",
        "Both statements are correct: Under Article 304(b), the Legislature of a State may by law impose reasonable restrictions in the public interest. However, the proviso to Article 304(b) mandates that 'no Bill or amendment for the purposes of clause (b) shall be introduced or moved in the Legislature of a State without the previous sanction of the President'.",
        "இரண்டு கூற்றுகளும் சரியானவை: உறுப்பு 304(b)-ன் கீழ் பொது நலன் கருதி நியாயமான கட்டுப்பாடுகளை விதிக்க மாநில சட்டமன்றத்திற்கு அதிகாரம் உண்டு. எனினும், உறுப்பு 304(b)-ன் வரம்புரையின்படி குடியரசுத் தலைவரின் முன் அனுமதியின்றி அத்தகைய மசோதாவை மாநில சட்டமன்றத்தில் அறிமுகப்படுத்த முடியாது.",
        "Option A is incorrect because statement 2 is also a mandatory proviso under Article 304(b).", "கூற்று 2-ம் உறுப்பு 304(b)-ன் கட்டாய நிபந்தனை என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because statement 1 is also completely accurate.", "கூற்று 1-ம் முற்றிலும் சரியானது என்பதால் விருப்பம் B தவறு.",
        "Option C is correct as both the power to impose reasonable restrictions and the requirement of Presidential prior sanction are accurate.", "நியாயமான கட்டுப்பாடுகள் விதிக்கும் அதிகாரம் மற்றும் குடியரசுத் தலைவரின் முன் அனுமதி ஆகிய இரண்டும் சரியானவை என்பதால் விருப்பம் C சரி.",
        "Option D is incorrect because neither statement is false.", "எந்தக் கூற்றும் தவறானது அல்ல என்பதால் விருப்பம் D தவறு.",
        "Crucial check: Article 304(b) requires Presidential PRIOR sanction before introducing the Bill in State Assembly!",
        "முக்கிய நிபந்தனை: உறுப்பு 304(b) மசோதாவை மாநில சட்டசபையில் அறிமுகப்படுத்தும் முன்பே குடியரசுத் தலைவரின் முன் அனுமதி பெறப்பட வேண்டும்!",
        "Article 304(b) allows reasonable trade restrictions by States only with prior Presidential sanction.",
        "உறுப்பு 304(b) குடியரசுத் தலைவரின் முன் அனுமதியுடன் மட்டுமே நியாயமான வர்த்தகக் கட்டுப்பாடுகளை விதிக்க மாநிலங்களுக்கு அனுமதிக்கிறது.",
        tags=["Article 304(b)", "Presidential Prior Sanction", "Reasonable Restrictions"]
    ))

    # 044 - Ans B
    q.append(make_q(
        "ISR_S_044", "Medium",
        "Consider the following statements regarding Article 305 and State monopolies:\n1. Laws providing for State monopolies (nationalization of trade or business) violate Article 301 and are unconstitutional.\n2. Article 305 saves laws creating State monopolies from being challenged on the ground that they violate Article 301 or Article 303.\nWhich of the statements given above is/are correct?",
        "உறுப்பு 305 மற்றும் அரசு ஏகபோகங்கள் (State monopolies) தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அரசு ஏகபோகங்களை வழங்கும் சட்டங்கள் (வர்த்தகம் அல்லது வணிகத்தை தேசியமயமாக்குதல்) உறுப்பு 301-ஐ மீறுவதால் அரசியலமைப்பிற்கு முரணானவை ஆகும்.\n2. அரசு ஏகபோகங்களை உருவாக்கும் சட்டங்கள் உறுப்பு 301 அல்லது உறுப்பு 303-ஐ மீறுகின்றன என்ற அடிப்படையில் சவாலுக்கு உட்படுத்தப்படுவதிலிருந்து உறுப்பு 305 அவற்றைப் பாதுகாக்கிறது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "B",
        "Statement 1 is incorrect: State monopolies (such as state road transport corporations or government electricity distribution) do not violate Article 301 because they are expressly protected. Statement 2 is correct: Article 305 explicitly saves any existing law or any law made by Parliament or a State legislature relating to State monopolies (carrying on of any trade or business by the State to the exclusion of citizens) from the operation of Articles 301 and 303.",
        "கூற்று 1 தவறு: அரசு ஏகபோகங்களை (போக்குவரத்துக் கழகங்கள், மின் விநியோகம் போன்றவை) ஏற்படுத்தும் சட்டங்கள் அரசியலமைப்பில் வெளிப்படையாகப் பாதுகாக்கப்படுவதால் அவை செல்லுபடியாகும். கூற்று 2 சரி: உறுப்பு 305 அரசு ஏகபோக சட்டங்களை உறுப்புகள் 301 மற்றும் 303-ன் கீழான சவால்களிலிருந்து பாதுகாக்கிறது.",
        "Option A is incorrect because state monopolies are constitutionally valid.", "அரசு ஏகபோகங்கள் அரசியலமைப்புப்படி செல்லுபடியாகும் என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because statement 2 captures the protective shield of Article 305.", "கூற்று 2 உறுப்பு 305-ன் பாதுகாப்பு வளையத்தைச் சரியாகக் குறிப்பிடுவதால் விருப்பம் B சரி.",
        "Option C is incorrect because statement 1 is false.", "கூற்று 1 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 2 is completely true.", "கூற்று 2 முற்றிலும் சரியானது என்பதால் விருப்பம் D தவறு.",
        "Article 305 protects State Monopolies (nationalisation) from trade freedom challenges under Article 301.",
        "உறுப்பு 305 அரசு ஏகபோகங்களை (தேசியமயமாக்கல்) உறுப்பு 301-ன் கீழான சவால்களிலிருந்து பாதுகாக்கிறது.",
        "Article 305 shields laws creating State monopolies from invalidation under Articles 301 and 303.",
        "உறுப்பு 305 அரசு ஏகபோகங்களை உருவாக்கும் சட்டங்கள் உறுப்புகள் 301 மற்றும் 303-ன் கீழ் ரத்தாகாமல் பாதுகாக்கிறது.",
        tags=["Article 305", "State Monopolies", "Nationalisation Shield"]
    ))

    # 045 - Ans C
    q.append(make_q(
        "ISR_S_045", "Hard",
        "Consider the following statements regarding Article 307 of the Constitution:\n1. Parliament may by law appoint such authority as it considers appropriate for carrying out the purposes of Articles 301, 302, 303, and 304.\n2. Till date, no statutory authority has been established by Parliament under the provisions of Article 307.\nWhich of the statements given above is/are correct?",
        "அரசியலமைப்பின் 307-வது உறுப்பு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. உறுப்புகள் 301, 302, 303 மற்றும் 304 ஆகியவற்றின் நோக்கங்களை நிறைவேற்றுவதற்குப் பொருத்தமான அதிகார அமைப்பை நாடாளுமன்றம் சட்டத்தின் மூலம் நியமிக்கலாம்.\n2. இன்று வரை, உறுப்பு 307-ன் விதிகளின் கீழ் எந்தவொரு சட்டப்பூர்வ அதிகார அமைப்பையும் நாடாளுமன்றம் நிறுவவில்லை.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "C",
        "Both statements are correct: Statement 1 is correct: Article 307 provides that Parliament may by law appoint an authority for carrying out the purposes of Articles 301 to 304 (similar to the Inter-State Commerce Commission in the USA). Statement 2 is correct: In reality, Parliament has never enacted legislation to set up any such authority under Article 307 to this day.",
        "இரண்டு கூற்றுகளும் சரியானவை: கூற்று 1 சரி: உறுப்புகள் 301 முதல் 304 வரையிலான நோக்கங்களைச் செயல்படுத்த நாடாளுமன்றம் ஒரு அதிகார அமைப்பை நியமிக்கலாம் என்று உறுப்பு 307 கூறுகிறது (அமெரிக்காவின் Inter-State Commerce Commission போல). கூற்று 2 சரி: நடைமுறையில், இன்று வரை உறுப்பு 307-ன் கீழ் அத்தகைய அதிகார அமைப்பு எதையும் நாடாளுமன்றம் அமைக்கவில்லை.",
        "Option A is incorrect because statement 2 is also an acknowledged constitutional fact.", "கூற்று 2-ம் ஒப்புக்கொள்ளப்பட்ட அரசியலமைப்பு உண்மை என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because statement 1 accurately cites Article 307.", "கூற்று 1 உறுப்பு 307-ஐச் சரியாகக் குறிப்பிடுவதால் விருப்பம் B தவறு.",
        "Option C is correct as both enabling power and non-implementation of Article 307 are true.", "அதிகாரம் வழங்குதல் மற்றும் இதுவரை நடைமுறைப்படுத்தப்படாத நிலை ஆகிய இரண்டும் உண்மை என்பதால் விருப்பம் C சரி.",
        "Option D is incorrect because neither statement is false.", "எந்தக் கூற்றும் தவறானது அல்ல என்பதால் விருப்பம் D தவறு.",
        "Article 307 allows appointment of a Trade & Commerce Authority, but NO such authority has ever been created!",
        "உறுப்பு 307 வர்த்தக அதிகார அமைப்பை நியமிக்க வழிசெய்தாலும், இதுவரை அத்தகைய அமைப்பு எதுவும் உருவாக்கப்படவில்லை!",
        "Article 307 empowers Parliament to appoint a trade authority, but no such body has ever been formed.",
        "உறுப்பு 307 வர்த்தக அதிகார அமைப்பை அமைக்க அதிகாரம் அளித்தாலும், இதுவரை அவ்வாறு எதுவும் உருவாக்கப்படவில்லை.",
        tags=["Article 307", "Inter-State Trade Authority", "Non-Constitution"]
    ))

    # 046 - Ans D
    q.append(make_q(
        "ISR_S_046", "Hard",
        "Consider the following statements regarding the landmark case of Atiabari Tea Co. v. State of Assam (1961):\n1. The Supreme Court ruled that tax laws are completely outside the purview of Article 301 under all circumstances.\n2. The Supreme Court held that only direct and immediate restrictions on the movement of goods violate the freedom guaranteed under Article 301.\nWhich of the statements given above is/are correct?",
        "அத்தியாபாரி டீ கம்பெனி எதிர் அசாம் மாநிலம் (1961) என்ற முக்கிய வழக்கு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. எந்தச் சூழ்நிலையிலும் வரிச் சட்டங்கள் உறுப்பு 301-ன் வரம்பிற்குள் வராது என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\n2. பொருட்களின் நடமாட்டத்தின் மீது விதிக்கப்படும் நேரடியான மற்றும் உடனடித் தடைகள் மட்டுமே உறுப்பு 301-ன் கீழ் உத்தரவாதம் அளிக்கப்பட்ட சுதந்திரத்தை மீறுவதாக அமையும் என்று உச்ச நீதிமன்றம் கூறியது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "B",
        "Statement 1 is incorrect: In the Atiabari case (1961), the 5-judge Constitution Bench held that taxing laws ARE within the purview of Article 301 if they directly and immediately impede the free flow of trade and commerce. Statement 2 is correct: The Supreme Court formulated the 'direct and immediate effect' test, holding that only laws which place direct and immediate restrictions on trade, commerce, and intercourse violate Article 301.",
        "கூற்று 1 தவறு: அத்தியாபாரி வழக்கில், வர்த்தகப் போக்குவரத்தை நேரடியாகத் தடுக்கும் வரிகள் உறுப்பு 301-ன் வரம்பிற்குள் வரும் என உச்ச நீதிமன்றம் தீர்ப்பளித்தது. கூற்று 2 சரி: பொருட்களின் சுதந்திரமான நடமாட்டத்தின் மீது நேரடியான மற்றும் உடனடித் தடைகளை (direct and immediate restrictions) ஏற்படுத்தும் வரிகள் மட்டுமே உறுப்பு 301-ஐ மீறுவதாக அமையும் என்ற கோட்பாட்டை நீதிமன்றம் வகுத்தது.",
        "Option A is incorrect because taxes can violate Article 301 if they directly restrict movement.", "நேரடித் தடையாக இருக்கும் வரிகள் உறுப்பு 301-ஐ மீறும் என்பதால் விருப்பம் A தவறு.",
        "Option B is correct because statement 2 captures the 'direct and immediate restrictions' doctrine laid down in Atiabari.", "அத்தியாபாரி வழக்கில் கூறப்பட்ட 'நேரடி மற்றும் உடனடித் தடைகள்' கோட்பாட்டை கூற்று 2 சரியாகக் குறிப்பிடுவதால் விருப்பம் B சரி.",
        "Option C is incorrect because statement 1 is false.", "கூற்று 1 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 2 is legally sound.", "கூற்று 2 சட்டப்படி சரியானது என்பதால் விருப்பம் D தவறு.",
        "Atiabari doctrine: Tax laws violate Article 301 if they impose 'direct and immediate restrictions' on trade movement.",
        "அத்தியாபாரி கோட்பாடு: வர்த்தக நகர்வின் மீது 'நேரடியான மற்றும் உடனடித் தடைகளை' விதித்தால் வரிச் சட்டங்களும் உறுப்பு 301-ஐ மீறும்.",
        "Atiabari Tea Co. case (1961) laid down the 'direct and immediate effect' doctrine under Article 301.",
        "அத்தியாபாரி வழக்கு (1961) உறுப்பு 301-ன் கீழ் 'நேரடி மற்றும் உடனடி விளைவு' கோட்பாட்டை வகுத்தது.",
        tags=["Atiabari Tea Case", "Direct and Immediate Doctrine", "Article 301 Taxes"]
    ))

    # 047 - Ans A
    q.append(make_q(
        "ISR_S_047", "Hard",
        "Consider the following statements regarding the Automobile Transport (Rajasthan) v. State of Rajasthan (1962) case:\n1. A 7-judge Constitution Bench held that regulatory measures or compensatory taxes imposed for using facilities do not violate Article 301.\n2. The Supreme Court ruled that all State vehicular taxes violate Article 301 regardless of whether road maintenance facilities are provided.\nWhich of the statements given above is/are correct?",
        "ஆட்டோமொபைல் டிரான்ஸ்போர்ட் (ராஜஸ்தான்) எதிர் ராஜஸ்தான் மாநிலம் (1962) வழக்கு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. வசதிகளைப் பயன்படுத்துவதற்காக விதிக்கப்படும் ஒழுங்குமுறை நடவடிக்கைகள் அல்லது ஈட்டு வரிகள் (compensatory taxes) உறுப்பு 301-ஐ மீறாது என்று 7 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வு தீர்ப்பளித்தது.\n2. சாலை பராமரிப்பு வசதிகள் வழங்கப்பட்டாலும் இல்லாவிட்டாலும், அனைத்து மாநில வாகன வரிகளும் உறுப்பு 301-ஐ மீறுவதாக அமையும் என்று உச்ச நீதிமன்றம் தீர்ப்பளித்தது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "A",
        "Statement 1 is correct: In the Automobile Transport case (1962), a 7-judge bench introduced the 'compensatory or regulatory tax' doctrine, ruling that taxes which facilitate trade (such as road taxes used to construct and maintain roads and bridges) do not violate Article 301. Statement 2 is incorrect: State vehicular taxes were expressly upheld on the ground that they were compensatory for the maintenance of roads.",
        "கூற்று 1 சரி: ஆட்டோமொபைல் டிரான்ஸ்போர்ட் வழக்கில் (1962), வர்த்தகத்தை எளிதாக்கும் ஒழுங்குமுறை நடவடிக்கைகள் அல்லது ஈட்டு வரிகள் (சாலை பராமரிப்பு போன்றவை) உறுப்பு 301-ஐ மீறாது என 7 நீதிபதிகள் அமர்வு தீர்ப்பளித்தது. கூற்று 2 தவறு: சாலை பராமரிப்பிற்கான வாகன வரிகள் ஈட்டு வரிகள் என்பதால் அவை செல்லும் என்று தீர்ப்பளிக்கப்பட்டது.",
        "Option A is correct because statement 1 reflects the landmark 'compensatory tax' theory while statement 2 contradicts the judgment.", "கூற்று 1 'ஈட்டு வரி' கோட்பாட்டைச் சரியாக விளக்குவதாலும், கூற்று 2 தீர்ப்பிற்கு முரணாக இருப்பதாலும் விருப்பம் A சரி.",
        "Option B is incorrect because vehicular taxes were upheld as compensatory.", "வாகன வரிகள் செல்லும் என்று தீர்ப்பளிக்கப்பட்டதால் விருப்பம் B தவறு.",
        "Option C is incorrect because statement 2 is false.", "கூற்று 2 தவறாக இருப்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 1 is true.", "கூற்று 1 உண்மையானது என்பதால் விருப்பம் D தவறு.",
        "Automobile Transport Case (1962) established the 'Compensatory Tax Doctrine' under Article 301.",
        "ஆட்டோமொபைல் டிரான்ஸ்போர்ட் வழக்கு (1962) உறுப்பு 301-ன் கீழ் 'ஈட்டு வரிக் கோட்பாட்டை' (Compensatory Tax Doctrine) நிறுவியது.",
        "Automobile Transport case ruled that compensatory and regulatory taxes do not impede Article 301 freedom.",
        "ஈட்டு வரிகள் மற்றும் ஒழுங்குமுறை நடவடிக்கைகள் உறுப்பு 301 வர்த்தக சுதந்திரத்தைத் தடுக்காது என ஆட்டோமொபைல் வழக்கில் தீர்ப்பளிக்கப்பட்டது.",
        tags=["Automobile Transport Case", "Compensatory Tax", "7-Judge Bench"]
    ))

    # 048 - Ans B
    q.append(make_q(
        "ISR_S_048", "Hard",
        "Consider the following statements regarding the 9-judge Constitution Bench ruling in Jindal Stainless Ltd. v. State of Haryana (2017):\n1. The 9-judge bench reaffirmed that States can only levy entry taxes if they directly prove a quantifiable compensatory benefit to payers.\n2. The Supreme Court overruled the 'compensatory tax' theory, holding that non-discriminatory entry tax levied under Article 304(a) does not violate Article 301.\nWhich of the statements given above is/are correct?",
        "ஜிண்டால் ஸ்டெயின்லெஸ் லிமிடெட் எதிர் ஹரியானா மாநிலம் (2017) வழக்கில் 9 நீதிபதிகள் கொண்ட அரசியலமைப்பு அமர்வின் தீர்ப்பு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. வரி செலுத்துவோருக்கு அளவிடக்கூடிய ஈட்டுப் பயனை நேரடியாக நிரூபித்தால் மட்டுமே மாநிலங்கள் நுழைவு வரியை விதிக்க முடியும் என்பதை 9 நீதிபதிகள் அமர்வு மீண்டும் உறுதிப்படுத்தியது.\n2. உச்ச நீதிமன்றம் 'ஈட்டு வரிக் கோட்பாட்டை' ரத்து செய்து, உறுப்பு 304(a)-ன் கீழ் விதிக்கப்படும் பாகுபாடற்ற நுழைவு வரி உறுப்பு 301-ஐ மீறாது என்று தீர்ப்பளித்தது.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "B",
        "Statement 1 is incorrect: The 9-judge bench explicitly discarded the quantifiable compensatory benefit requirement as judicially unworkable. Statement 2 is correct: By a 7:2 majority, the 9-judge Constitution Bench in Jindal Stainless (2017) overruled the compensatory tax theory originating from Automobile Transport, holding that non-discriminatory taxes (entry taxes) levied under Article 304(a) do not violate Article 301, as long as outside goods are not taxed higher than local goods.",
        "கூற்று 1 தவறு: அளவிடக்கூடிய ஈட்டுப் பயன் இருக்க வேண்டும் என்ற தேவையை 9 நீதிபதிகள் அமர்வு நிராகரித்தது. கூற்று 2 சரி: ஜிண்டால் ஸ்டெயின்லெஸ் வழக்கில் (2017), உச்ச நீதிமன்றம் ஈட்டு வரிக் கோட்பாட்டை ரத்து செய்தது; உள்ளூர் பொருட்களை விட வெளி மாநிலப் பொருட்கள் மீது அதிக வரி விதிக்கப்படாத வரை, உறுப்பு 304(a)-ன் கீழ் விதிக்கப்படும் நுழைவு வரி உறுப்பு 301-ஐ மீறாது என்று தீர்ப்பளித்தது.",
        "Option A is incorrect because the compensatory tax test was discarded.", "ஈட்டு வரிக் கோட்பாடு ரத்து செய்யப்பட்டதால் விருப்பம் A தவறு.",
        "Option B is correct because statement 2 captures the historic overruling of the compensatory tax test in 2017.", "2017 தீர்ப்பில் ஈட்டு வரிக் கோட்பாடு ரத்து செய்யப்பட்டதை கூற்று 2 சரியாகக் குறிப்பிடுவதால் விருப்பம் B சரி.",
        "Option C is incorrect because statement 1 is outdated law.", "கூற்று 1 காலாவதியான சட்டம் என்பதால் விருப்பம் C தவறு.",
        "Option D is incorrect because statement 2 is current constitutional jurisprudence.", "கூற்று 2 தற்போதைய அரசியலமைப்புச் சட்டம் என்பதால் விருப்பம் D தவறு.",
        "Jindal Stainless (2017, 9-judge bench): Overruled the compensatory tax theory; test is non-discrimination under Art 304(a).",
        "ஜிண்டால் ஸ்டெயின்லெஸ் (2017, 9 நீதிபதிகள் அமர்வு): ஈட்டு வரிக் கோட்பாட்டை ரத்து செய்தது; உறுப்பு 304(a)-ன் கீழ் பாகுபாடற்ற தன்மையே அளவுகோல்.",
        "Jindal Stainless (2017) discarded the compensatory tax doctrine and upheld non-discriminatory entry taxes.",
        "ஜிண்டால் ஸ்டெயின்லெஸ் (2017) ஈட்டு வரிக் கோட்பாட்டை நிராகரித்து, பாகுபாடற்ற நுழைவு வரிகள் செல்லும் என உறுதி செய்தது.",
        tags=["Jindal Stainless 2017", "9-Judge Bench", "Entry Tax Upheld"]
    ))

    # 049 - Ans C
    q.append(make_q(
        "ISR_S_049", "Hard",
        "Consider the following statements regarding the division of legislative powers over water in the Seventh Schedule:\n1. Water supplies, irrigation, canals, drainage, embankments, and water storage are under Entry 17 of the State List (List II).\n2. Regulation and development of inter-State rivers and river valleys is under Entry 56 of the Union List (List I), to the extent declared by Parliament by law to be expedient in the public interest.\nWhich of the statements given above is/are correct?",
        "ஏழாவது அட்டவணையில் நீர் தொடர்பான சட்டமியற்றும் அதிகாரப் பகிர்வு குறித்த பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. நீர் விநியோகம், நீர்ப்பாசனம், கால்வாய்கள், வடிகால், அணைக் கரைகள் மற்றும் நீர் சேமிப்பு ஆகியவை மாநிலப் பட்டியலின் (பட்டியல் II) பதிவு 17-ன் கீழ் உள்ளன.\n2. மாநிலங்களுக்கு இடையிலான நதிகள் மற்றும் நதிப் பள்ளத்தாக்குகளின் ஒழுங்குமுறை மற்றும் மேம்பாடு ஆகியவை பொது நலன் கருதி நாடாளுமன்றம் சட்டத்தின் மூலம் அறிவிக்கும் அளவிற்கு மத்தியப் பட்டியலின் (பட்டியல் I) பதிவு 56-ன் கீழ் உள்ளன.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "C",
        "Both statements are correct: Under the Seventh Schedule: Entry 17 of List II places water, irrigation, canals etc. in the State List, but expressly subject to Entry 56 of List I. Entry 56 of List I empowers the Union Parliament to regulate and develop inter-State rivers and river valleys to the extent declared by parliamentary law in the public interest.",
        "இரண்டு கூற்றுகளும் சரியானவை: ஏழாவது அட்டவணையின் கீழ்: மாநிலப் பட்டியலின் பதிவு 17 நீர், நீர்ப்பாசனம் மற்றும் கால்வாய்களை மாநிலப் பட்டியலில் வைக்கிறது (ஆனால் இது மத்தியப் பட்டியல் பதிவு 56-க்கு உட்பட்டது). மத்தியப் பட்டியல் பதிவு 56 நாடாளுமன்றத்தின் சட்ட அறிவிப்பின் அளவிற்கு நதிகளை ஒழுங்குபடுத்த ஒன்றியத்திற்கு அதிகாரம் அளிக்கிறது.",
        "Option A is incorrect because statement 2 is equally a valid constitutional provision.", "கூற்று 2-ம் சரியான அரசியலமைப்பு விதி என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because statement 1 is equally valid.", "கூற்று 1-ம் சரியானது என்பதால் விருப்பம் B தவறு.",
        "Option C is correct as both Entry 17 (State List) and Entry 56 (Union List) are precisely described.", "மாநிலப் பட்டியல் பதிவு 17 மற்றும் மத்தியப் பட்டியல் பதிவு 56 ஆகிய இரண்டும் சரியாக விவரிக்கப்பட்டுள்ளதால் விருப்பம் C சரி.",
        "Option D is incorrect because neither statement is false.", "எந்தக் கூற்றும் தவறானது அல்ல என்பதால் விருப்பம் D தவறு.",
        "Water Entry formula: State List Entry 17 is expressly subject to Union List Entry 56 (Inter-state rivers).",
        "நீர் பற்றிய விதி: மாநிலப் பட்டியல் பதிவு 17 என்பது மத்தியப் பட்டியல் பதிவு 56-க்கு (மாநிலங்களுக்கு இடையிலான நதிகள்) உட்பட்டது.",
        "Entry 17 of State List governs water, subject to Union regulation under Entry 56 of the Union List.",
        "மாநிலப் பட்டியல் பதிவு 17 நீரை நிர்வகிக்கிறது; எனினும் இது மத்தியப் பட்டியல் பதிவு 56-க்கு உட்பட்டது.",
        tags=["Entry 17 State List", "Entry 56 Union List", "Seventh Schedule Water"]
    ))

    # 050 - Ans D
    q.append(make_q(
        "ISR_S_050", "Medium",
        "Consider the following statements regarding the constitutional architecture of inter-State coordination in India:\n1. The Constitution created a single permanent constitutional body with binding adjudicatory jurisdiction over all interstate political and economic disputes.\n2. Under Article 263, any recommendations formulated by the Inter-State Council automatically supersede statutory acts passed by State legislatures.\nWhich of the statements given above is/are correct?",
        "இந்தியாவில் மாநிலங்களுக்கு இடையிலான ஒருங்கிணைப்பின் அரசியலமைப்பு கட்டமைப்பு தொடர்பான பின்வரும் கூற்றுகளைக் கவனியுங்கள்:\n1. அனைத்து மாநிலங்களுக்கு இடையிலான அரசியல் மற்றும் பொருளாதாரத் தகராறுகளின் மீதும் பிணைப்புள்ள தீர்ப்பளிக்கும் அதிகார வரம்பைக் கொண்ட ஒற்றை நிரந்தர அரசியலமைப்பு அமைப்பை அரசியலமைப்பு உருவாக்கியது.\n2. உறுப்பு 263-ன் கீழ் மாநிலங்களுக்கு இடையிலான மன்றத்தால் உருவாக்கப்படும் எந்தவொரு பரிந்துரைகளும் மாநில சட்டமன்றங்களால் இயற்றப்பட்ட சட்டப்பூர்வ சட்டங்களைத் தானாகவே ரத்து செய்கின்றன.\nமேலே கொடுக்கப்பட்ட கூற்றுகளில் சரியானது/சரியானவை எது/எவை?",
        "1 only", "1 மட்டும்",
        "2 only", "2 மட்டும்",
        "Both 1 and 2", "1 மற்றும் 2 ஆகிய இரண்டும்",
        "Neither 1 nor 2", "இரண்டும் அல்ல",
        "D",
        "Both statements are incorrect: Statement 1 is incorrect: The Indian Constitution did not create any single permanent adjudicatory body for all inter-state disputes; instead, it provides diverse mechanisms: Supreme Court original jurisdiction (Article 131), water tribunals (Article 262), and an advisory Inter-State Council (Article 263). Statement 2 is incorrect: Recommendations of the Inter-State Council under Article 263 are purely advisory and deliberative; they have no power to override or supersede acts of State legislatures.",
        "இரண்டு கூற்றுகளும் தவறானவை: கூற்று 1 தவறு: இந்திய அரசியலமைப்பு அனைத்துத் தகராறுகளுக்கும் ஒரே நிரந்தர தீர்ப்பளிக்கும் அமைப்பை உருவாக்கவில்லை; மாறாக உச்ச நீதிமன்ற மூல வரம்பு (உறுப்பு 131), நதிநீர் தீர்ப்பாயங்கள் (உறுப்பு 262), ஆலோசனைக் குழு (உறுப்பு 263) போன்ற பலதரப்பட்ட அமைப்புகளை வழங்கியுள்ளது. கூற்று 2 தவறு: உறுப்பு 263-ன் கீழான மன்றத்தின் பரிந்துரைகள் ஆலோசனையே அன்றி மாநிலச் சட்டங்களை ரத்து செய்ய முடியாது.",
        "Option A is incorrect because no single super-adjudicatory body exists.", "ஒற்றை உச்சகட்ட தீர்ப்பளிக்கும் அமைப்பு எதுவும் இல்லை என்பதால் விருப்பம் A தவறு.",
        "Option B is incorrect because ISC recommendations have zero overriding legal power.", "மன்றப் பரிந்துரைகளுக்கு மாநிலச் சட்டங்களை ரத்து செய்யும் அதிகாரம் இல்லை என்பதால் விருப்பம் B தவறு.",
        "Option C is incorrect because both statements represent constitutional misconceptions.", "இரண்டு கூற்றுகளும் அரசியலமைப்பு தவறான புரிதல்கள் என்பதால் விருப்பம் C தவறு.",
        "Option D is correct because the Indian federal framework relies on multi-tiered, advisory, and specialized judicial mechanisms.", "இந்திய கூட்டாட்சி கட்டமைப்பு பல அடுக்கு, ஆலோசனை மற்றும் சிறப்பு நீதித்துறை அமைப்புகளைக் கொண்டுள்ளதால் விருப்பம் D சரி.",
        "Federal inter-state mechanisms: Adjudicatory (SC Art 131 & Tribunals Art 262) + Advisory (ISC Art 263 & Zonal Councils).",
        "மாநிலங்களுக்கு இடையிலான கூட்டாட்சி அமைப்புகள்: தீர்ப்பளிக்கும் அமைப்புகள் (உச்ச நீதிமன்றம் 131 & தீர்ப்பாயங்கள் 262) + ஆலோசனைக் குழுக்கள் (மன்றம் 263 & மண்டலக் குழுக்கள்).",
        "Inter-state disputes are managed through distinct constitutional channels: Article 131, Article 262, and Article 263.",
        "மாநிலங்களுக்கு இடையேயான தகராறுகள் உறுப்புகள் 131, 262 மற்றும் 263 ஆகிய தனித்துவமான வழிகள் மூலம் கையாளப்படுகின்றன.",
        tags=["Inter-State Architecture", "Multi-Tier Federalism", "Advisory Nature"]
    ))

    return q
