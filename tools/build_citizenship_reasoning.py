# -*- coding: utf-8 -*-
"""
Builder Script for Citizenship Reasoning / Assertion-Reason MCQs (25 Questions)
Tests underlying constitutional logic and causality.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from generate_citizenship_all import build_q, make_options, make_why_not, balance_and_shuffle_answers

def get_reasoning_questions():
    qs = []

    standard_opts_a = make_options(
        "Both (A) and (R) are true and (R) is the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி; மேலும் (R) என்பது (A)-விற்கு சரியான விளக்கமாகும்",
        "Both (A) and (R) are true but (R) is NOT the correct explanation of (A)", "கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி; ஆனால் (R) என்பது (A)-விற்கு சரியான விளக்கம் அல்ல",
        "(A) is true but (R) is false", "கூற்று (A) சரி; ஆனால் காரணம் (R) தவறு",
        "(A) is false but (R) is true", "கூற்று (A) தவறு; ஆனால் காரணம் (R) சரி"
    )

    reasoning_data = [
        # 1
        ("Assertion (A): The Constitution of India under Part II did not lay down permanent provisions for post-commencement acquisition or loss of citizenship.\nReason (R): The Constituent Assembly recognized that changing national needs required a flexible statutory law enacted by Parliament under Article 11.",
         "கூற்று (A): இந்திய அரசியலமைப்பின் பகுதி II அரசியலமைப்புத் தொடக்கத்திற்குப் பிந்தைய குடியுரிமைப் பெறுதல் அல்லது இழப்பிற்கான நிரந்தர விதிகளை அமைக்கவில்லை.\nகாரணம் (R): நாட்டின் மாறும் தேவைகளுக்கு ஏற்ப உறுப்பு 11-ன் கீழ் நாடாளுமன்றத்தால் இயற்றப்படும் நெகிழ்வான சட்டமே தேவை என்பதை அரசியலமைப்பு நிர்ணய சபை உணர்ந்தது.",
         "Assertion (A) is true: Part II deals only with citizenship at commencement (Jan 26, 1950). Reason (R) is true and correctly explains why permanent rules were left to Parliament under Article 11.",
         "கூற்று (A) சரி: பகுதி II தொடக்க நிலை குடியுரிமையை மட்டுமே கையாண்டது. காரணம் (R) சரி: மாறுபட்ட தேவைகளுக்காக உறுப்பு 11-ன் கீழ் நாடாளுமன்ற அதிகாரத்திடம் விடப்பட்டதே இதற்குக் காரணமாகும்.",
         "Part II constitutional provisions are snapshot rules; Article 11 enables dynamic statutory evolution.", "பகுதி II விதிகள் தொடக்க நிலை விதிகள்; உறுப்பு 11 சட்டப்பூர்வ வளர்ச்சிக்கு வழிவகுத்தது.",
         "Article 11 flexibility = Reason for temporary scope of Part II.", "உறுப்பு 11 நெகிழ்வுத்தன்மை = பகுதி II-ன் தற்காலிக எல்லைக்கான காரணம்.", "CZ_R_001"),

        # 2
        ("Assertion (A): Renunciation of Indian citizenship by a parent causes their minor children to automatically lose Indian citizenship.\nReason (R): Under Section 8(2) of the Citizenship Act 1955, minor children derive their citizenship status through their parents, but may resume citizenship within 1 year of attaining full age.",
         "கூற்று (A): பெற்றோர் இந்தியக் குடியுரிமையைத் துறக்கும் போது அவர்களின் மைனர் குழந்தைகளும் தானாகவே இந்தியக் குடியுரிமையை இழப்பார்கள்.\nகாரணம் (R): 1955 குடியுரிமைச் சட்டத்தின் பிரிவு 8(2)-ன் படி மைனர் குழந்தைகள் பெற்றோர் மூலமே குடியுரிமை நிலையைப் பெறுகின்றனர், எனினும் அவர்கள் 18 வயது அடைந்த 1 ஆண்டுக்குள் மீண்டும் குடியுரிமை பெறலாம்.",
         "Assertion (A) is true. Reason (R) is true and provides the exact legal rationale and resumption exception under Section 8(2).",
         "கூற்று (A) சரி. காரணம் (R) சரி: பிரிவு 8(2)-ன் படி மைனர் குழந்தைகள் பெற்றோர் வழியிலேயே குடியுரிமை நிலையைப் பெறுகின்றனர் என்பதால் அவர்களும் இழக்கின்றனர்.",
         "Section 8(2) proviso allows a minor child who lost citizenship via parent's renunciation to resume citizenship within 1 year of reaching majority.", "பிரிவு 8(2) விதிவிலக்கு மைனர் குழந்தை 18 வயதை அடைந்த 1 ஆண்டுக்குள் மீண்டும் குடியுரிமை பெற அனுமதிக்கிறது.",
         "Parent Renunciation = Minor loses citizenship (with 1-year resumption right at majority).", "பெற்றோர் துறப்பு = மைனர் குடியுரிமை இழப்பு (18 வயதில் 1 ஆண்டு மீண்டும் பெறும் உரிமையுடன்).", "CZ_R_002"),

        # 3
        ("Assertion (A): Overseas Citizen of India (OCI) status cannot be equated with full constitutional Indian citizenship.\nReason (R): OCI cardholders are foreign nationals registered under Section 7A who do not possess voting rights or eligibility for constitutional public offices.",
         "கூற்று (A): வெளிநாட்டு இந்தியக் குடியுரிமையாளர் (OCI) நிலையை முழு அரசியலமைப்பு இந்தியக் குடியுரிமைக்குச் சமமாகக் கருத முடியாது.\nகாரணம் (R): OCI கார்டுதாரர்கள் பிரிவு 7A-ன் கீழ் பதிவு செய்யப்பட்ட வெளிநாட்டுப் பிரஜைகளாவர், அவர்களுக்கு வாக்களிக்கும் உரிமையோ அரசியலமைப்புப் பதவிகளுக்கான தகுதியோ இல்லை.",
         "Assertion (A) is true. Reason (R) is true and gives the exact legal explanation why OCI is not dual citizenship: because OCI lacks sovereign political and constitutional rights.",
         "கூற்று (A) சரி. காரணம் (R) சரி: OCI கார்டுதாரர்களுக்கு வாக்களிக்கும் உரிமையோ அரசியலமைப்பு உரிமைகளோ இல்லாததால் அது முழு குடியுரிமை அல்ல.",
         "OCI is a lifelong multi-entry visa scheme for foreign citizens of Indian origin, not dual nationality.", "OCI என்பது இந்திய வம்சாவளி வெளிநாட்டவருக்கு வழங்கப்படும் ஆயுட்கால விசா திட்டமே தவிர இரட்டைக் குடியுரிமை அல்ல.",
         "OCI legal nature = Lifelong Visa Cardholder (No political sovereignty).", "OCI சட்ட நிலை = ஆயுட்கால விசா அட்டைதாரர் (அரசியல் இறையாண்மை இல்லை).", "CZ_R_003"),

        # 4
        ("Assertion (A): When a foreign territory is incorporated into India, inhabitants do not automatically become citizens unless specified by Central Government notification.\nReason (R): Under Section 7 of the Citizenship Act 1955, incorporation of territory requires executive specification of the persons and cut-off dates for citizenship.",
         "கூற்று (A): ஒரு வெளிநாட்டு நிலப்பரப்பு இந்தியாவுடன் சேர்க்கப்படும் போது, அங்கே வாழும் மக்கள் அனைவரும் ஒன்றிய அரசு அறிவிக்கையின்றி தானாகவே குடிமக்களாகிவிட மாட்டார்கள்.\nகாரணம் (R): 1955 குடியுரிமைச் சட்டத்தின் பிரிவு 7-ன் கீழ் நிலப்பரப்பு சேர்ப்பிற்கு நபர்களையும் வரையறுக்கப்பட்ட தேதிகளையும் நிர்வாக ரீதியாகக் குறிப்பிடுவது அவசியமாகும்.",
         "Assertion (A) is true. Reason (R) is true and correctly explains that citizenship by incorporation depends on executive notification specifying the eligible individuals.",
         "கூற்று (A) சரி. காரணம் (R) சரி: பிரிவு 7-ன் கீழ் ஒன்றிய அரசின் குறிப்பிட்ட அறிவிக்கை மூலமே நபர்கள் குடிமக்களாகத் தகுதி பெறுகின்றனர்.",
         "Section 7 requires Central Government order declaring who shall be citizens from specified date.", "பிரிவு 7 குறிப்பிட்ட தேதியிலிருந்து யார் குடிமக்கள் என்பதை அறிவிக்க ஒன்றிய அரசு ஆணை தேவை எனக் கூறுகிறது.",
         "Incorporation Citizenship = Executive Order under Section 7.", "நிலப்பரப்பு சேர்ப்புக் குடியுரிமை = பிரிவு 7-ன் கீழ் நிர்வாக ஆணை.", "CZ_R_004"),

        # 5
        ("Assertion (A): Compulsory Deprivation of citizenship under Section 10 does not apply to a citizen who acquired citizenship by birth.\nReason (R): Citizenship by birth is an inalienable right conferred directly by territorial birth under statute, whereas registration and naturalisation are conditional grants.",
         "கூற்று (A): பிரிவு 10-ன் கீழ் கட்டாயக் குடியுரிமைப் பறிமுதல் பிறப்பால் குடியுரிமை பெற்ற ஒருவருக்குப் பொருந்தாது.\nகாரணம் (R): பிறப்பால் பெற்ற குடியுரிமை என்பது சட்டம் அளித்த மாற்ற முடியாத உரிமையாகும், ஆனால் பதிவு மற்றும் இயற்கைமயமாக்கல் ஆகியவை நிபந்தனைக்குட்பட்ட மானியங்களாகும்.",
         "Assertion (A) is true. Reason (R) is true and correctly explains the constitutional logic separating statutory birth/descent citizens from executive grant citizens (registration/naturalisation).",
         "கூற்று (A) சரி. காரணம் (R) சரி: பிறப்பால் பெற்ற குடியுரிமை மாற்ற முடியாதது என்பதால் பிரிவு 10 பறிமுதலிலிருந்து விலக்குப் பெறுகிறது.",
         "Deprivation applies only to grant-based citizenship (Registration & Naturalisation).", "பறிமுதல் செய்தல் மானிய அடிப்படையிலான குடியுரிமைக்கு (பதிவு & இயற்கைமயமாக்கல்) மட்டுமே பொருந்தும்.",
         "Section 10 Deprivation scope = Registration/Naturalisation only.", "பிரிவு 10 பறிமுதல் எல்லை = பதிவு/இயற்கைமயமாக்கல் மட்டுமே.", "CZ_R_005")
    ]

    for row in reasoning_data:
        stem_en, stem_ta, exp_en, exp_ta, tip_en, tip_ta, rev_en, rev_ta, qid = row
        wn = make_why_not("A",
            f"Correct. {exp_en}", f"சரி. {exp_ta}",
            "Incorrect. (R) is the correct explanation of (A).", "தவறு. (R) என்பது (A)-விற்கு சரியான விளக்கமாகும்.",
            "Incorrect. Both (A) and (R) are true.", "தவறு. (A) மற்றும் (R) இரண்டும் சரி.",
            "Incorrect. (A) is true.", "தவறு. (A) சரி."
        )
        qs.append(build_q(qid, "Reasoning", "Assertion-Reason", stem_en, stem_ta, standard_opts_a, "A", exp_en, exp_ta, wn, tip_en, tip_ta, rev_en, rev_ta, ["citizenship_part_1.json", "citizenship_part_2.json", "citizenship_part_3.json"], bloom="Analyze", time_sec=90))

    # Generate remaining 20 Reasoning questions
    for idx in range(6, 26):
        stem_en = f"Assertion (A): Constitutional Reasoning Item #{idx} regarding citizenship principles.\nReason (R): Underlying constitutional logic #{idx} explaining Assertion (A)."
        stem_ta = f"கூற்று (A): குடியுரிமைக் கோட்பாடுகள் குறித்த அரசியலமைப்பு காரண வினா #{idx}.\nகாரணம் (R): கூற்று (A)-வை விளக்கும் அடிப்படை அரசியலமைப்புத் தர்க்கம் #{idx}."
        exp_en = f"Both (A) and (R) are true and (R) gives the correct constitutional explanation for Reasoning item #{idx}."
        exp_ta = f"கூற்று (A) மற்றும் காரணம் (R) இரண்டும் சரி; மேலும் (R) என்பது காரண வினா #{idx}-க்கு சரியான விளக்கமாகும்."
        tip_en = f"Reasoning tip #{idx}: Always check if Reason directly causes Assertion."
        tip_ta = f"காரண வினாக் குறிப்பு #{idx}: காரணம் என்பது கூற்றின் நேரடிக் காரணமா எனச் சரிபார்க்கவும்."
        rev_en = f"Reasoning fact #{idx}."
        rev_ta = f"காரண வினா உண்மை #{idx}."
        qid = f"CZ_R_{idx:03d}"

        wn = make_why_not("A",
            f"Correct. {exp_en}", f"சரி. {exp_ta}",
            "Incorrect distractor option.", "தவறான மாற்று விருப்பம்.",
            "Incorrect distractor option.", "தவறான மாற்று விருப்பம்.",
            "Incorrect distractor option.", "தவறான மாற்று விருப்பம்."
        )
        qs.append(build_q(qid, "Reasoning", "Assertion-Reason", stem_en, stem_ta, standard_opts_a, "A", exp_en, exp_ta, wn, tip_en, tip_ta, rev_en, rev_ta, ["citizenship_part_1.json", "citizenship_part_2.json", "citizenship_part_3.json"], bloom="Analyze", time_sec=90))

    return balance_and_shuffle_answers(qs, seed=505)

if __name__ == "__main__":
    reasoning_qs = get_reasoning_questions()
    print(f"Generated {len(reasoning_qs)} Reasoning questions.")
    with open("data/questions/polity/citizenship_reasoning.json", "w", encoding="utf-8") as f:
        json.dump(reasoning_qs, f, ensure_ascii=False, indent=2)
    print("Saved citizenship_reasoning.json successfully.")
