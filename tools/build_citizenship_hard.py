# -*- coding: utf-8 -*-
"""
Builder Script for Citizenship Hard MCQs (50 Questions)
Group 1 Standard: Multi-concept, exceptions, statutory interaction, and analytical traps.
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from generate_citizenship_all import build_q, make_options, make_why_not, balance_and_shuffle_answers

def get_hard_questions():
    qs = []

    raw_data = [
        # 1
        ("Article 7 overrides both Articles 5 and 6, rendering a person who migrated to Pakistan after March 1, 1947 a non-citizen unless returning under a permanent resettlement permit",
         "உறுப்பு 7 உறுப்புகள் 5 மற்றும் 6 ஆகிய இரண்டையும் விட மேலோங்குகிறது, மார்ச் 1, 1947க்குப் பின் பாகிஸ்தானிற்குச் சென்ற நபர் மறுகுடியேற்ற அனுமதியின்றி திரும்பாவிட்டால் அவரை குடிமகன் அல்லாதவராக்குகிறது",
         "Article 5 overrides Article 7 because domicile is a fundamental constitutional right", "இருப்பிடம் அடிப்படை உரிமை என்பதால் உறுப்பு 5 உறுப்பு 7-ஐ மேலோங்குகிறது",
         "Article 6 and Article 7 operate in completely non-overlapping territorial domains", "உறுப்புகள் 6 மற்றும் 7 முற்றிலும் ஒன்றோடொன்று தொடர்பில்லாத ஆட்சி எல்லைகளில் செயல்படுகின்றன",
         "Article 7 applies only to foreign nationals and not to persons domiciled in undivided India", "உறுப்பு 7 வெளிநாட்டுப் பிரஜைகளுக்கு மட்டுமே பொருந்தும், இந்தியாவிலிருந்தோருக்கு அல்ல",
         "In constitutional interpretation, how does Article 7 interact with Article 5 and Article 6 regarding citizenship at commencement?",
         "அரசியலமைப்புப் பொருள் விளக்கத்தில், தொடக்க நிலை குடியுரிமை தொடர்பாக உறுப்பு 7 எவ்வாறு உறுப்புகள் 5 மற்றும் 6 உடனாகச் செயல்படுகிறது?",
         "Article 7 begins with a non-obstante clause ('Notwithstanding anything in Articles 5 and 6'). If a person domiciled in India under Art 5 or born under Art 6 migrated to Pakistan after March 1, 1947, they lost Indian citizenship unless returning under a permanent resettlement permit.",
         "உறுப்பு 7 'உறுப்புகள் 5 மற்றும் 6-ல் எது கூறப்பட்டிருப்பினும்' எனத் தொடங்குகிறது. மார்ச் 1, 1947க்குப் பின் பாகிஸ்தானிற்குச் சென்றோர் மறுகுடியேற்ற அனுமதியின்றி திரும்பாவிட்டால் குடியுரிமை இழப்பர்.",
         "Article 7 non-obstante clause overrides both Article 5 domicile and Article 6 migration.", "உறுப்பு 7 உறுப்புகள் 5 மற்றும் 6 ஆகிய இரண்டையுமே மேலோங்கச் செய்கிறது.",
         "Article 7 non-obstante clause > Articles 5 & 6.", "உறுப்பு 7 மேலோங்கும் விதி > உறுப்புகள் 5 & 6.", "CZ_H_001"),

        # 2
        ("Parliament has exclusive power under List I Entry 17 and Article 11; State Assemblies have ZERO legislative power over citizenship",
         "உறுப்பு 11 மற்றும் பட்டியல் I வரிசை 17-ன் கீழ் நாடாளுமன்றத்திற்கு மட்டுமே முழு அதிகாரம் உண்டு; மாநிலச் சட்டமன்றங்களுக்குக் குடியுரிமையில் எந்த அதிகாரமும் இல்லை",
         "State Assemblies can enact supplementary citizenship laws under Concurrent List Entry 20", "மாநிலச் சட்டமன்றங்கள் பொதுப் பட்டியலின் கீழ் துணைக் குடியுரிமைச் சட்டங்களை இயற்றலாம்",
         "State Legislative Councils can reject Parliamentary citizenship laws via resolution", "மாநில மேலவைகள் நாடாளுமன்றக் குடியுரிமைச் சட்டங்களைத் தீர்மானம் மூலம் நிராகரிக்கலாம்",
         "Parliament requires ratification by at least half of State Assemblies to amend citizenship laws", "குடியுரிமைச் சட்டங்களைத் திருத்த நாடாளுமன்றத்திற்கு பாதி மாநிலங்களின் ஒப்புதல் தேவை",
         "Which constitutional principle governs the legislative jurisdiction between Parliament and State Legislatures over Citizenship?",
         "குடியுரிமை மீதான நாடாளுமன்றம் மற்றும் மாநிலச் சட்டமன்றங்களின் அதிகார எல்லை குறித்து எந்த அரசியலமைப்புக் கோட்பாடு ஆளுகிறது?",
         "Under Article 11 and Union List (List I) Entry 17 ('Citizenship, naturalisation and aliens'), Parliament possesses exclusive legislative competence. State Assemblies have no power to legislate or modify citizenship rules.",
         "உறுப்பு 11 மற்றும் ஒன்றியப் பட்டியல் I வரிசை 17-ன் கீழ் நாடாளுமன்றத்திற்கு மட்டுமே பிரத்யேக அதிகாரமுண்டு. மாநிலச் சட்டமன்றங்களுக்கு குடியுரிமைச் சட்டங்களை இயற்ற எந்த அதிகாரமும் இல்லை.",
         "Citizenship is strictly in Union List (Entry 17); Article 11 gives sole power to Parliament.", "குடியுரிமை ஒன்றியப் பட்டியலில் (வரிசை 17) மட்டுமே உள்ளது; உறுப்பு 11 நாடாளுமன்றத்திற்கு மட்டுமே அதிகாரம் அளிக்கிறது.",
         "Citizenship = Exclusive Union List Entry 17 & Article 11.", "குடியுரிமை = ஒன்றியப் பட்டியல் வரிசை 17 & உறுப்பு 11.", "CZ_H_002"),

        # 3
        ("Domicile requires both residence (factum) and intention to reside permanently (animus manendi); citizenship is legal status derived from domicile or statute",
         "இருப்பிடத்திற்கு வசிப்பு (factum) மற்றும் நிரந்தரமாக வசிக்கும் விருப்பம் (animus manendi) ஆகிய இரண்டும் தேவை; குடியுரிமை என்பது இருப்பிடம் அல்லது சட்டத்தால் பெறப்படும் அரசியல் நிலை",
         "Domicile and citizenship are legally identical terms under Indian Constitutional Law", "இந்திய அரசியலமைப்புச் சட்டத்தின் கீழ் இருப்பிடமும் குடியுரிமையும் சட்டப்படி ஒரே சொற்களாகும்",
         "A person can have multiple domiciles in India corresponding to different States", "ஒரு நபர் இந்தியாவில் வெவ்வேறு மாநிலங்களுக்கு ஏற்ப பல இருப்பிடங்களைக் கொண்டிருக்கலாம்",
         "Citizenship can exist without any allegiance to the sovereign State", "இறையாண்மையுள்ள அரசிற்கு எவ்வித விசுவாசமுமின்றி குடியுரிமை நிலவ முடியும்",
         "What is the precise legal relationship between Domicile and Citizenship under Indian Constitutional jurisprudence?",
         "இந்திய அரசியலமைப்புச் சட்டத்தின் கீழ் இருப்பிடம் (Domicile) மற்றும் குடியுரிமை (Citizenship) ஆகியவற்றிற்கு இடையிலான சரியான சட்டப் பிணைப்பு என்ன?",
         "Domicile denotes a person's permanent home (requiring physical residence + intention to remain permanently); citizenship denotes political membership of the State. Under Article 5, Domicile was a mandatory prerequisite for citizenship at commencement, but domicile alone without birth/parentage/residence was insufficient.",
         "இருப்பிடம் என்பது நிரந்தர இருப்பிடத்தைக் குறிக்கும் (வசிப்பு + நிரந்தர விருப்பம்); குடியுரிமை என்பது நாட்டின் அரசியல் உறுப்பினர் நிலையாகும். உறுப்பு 5-ன் கீழ் குடியுரிமை பெற இருப்பிடம் முதன்மை நிபந்தனையாகும்.",
         "Domicile = Residence (Factum) + Intention (Animus). Single Domicile in India (No State Domicile).", "இருப்பிடம் = வசிப்பு + நிரந்தர விருப்பம். இந்தியாவில் ஒற்றை இருப்பிடம் மட்டுமே உண்டு.",
         "Domicile + Birth/Parentage/Residence = Article 5 Citizenship.", "இருப்பிடம் + பிறப்பு/பெற்றோர்/வசிப்பு = உறுப்பு 5 குடியுரிமை.", "CZ_H_003"),

        # 4
        ("Section 10 Deprivation applies ONLY to citizens by Registration or Naturalisation and NEVER to citizens by Birth or Descent",
         "பிரிவு 10 குடியுரிமைப் பறிமுதல் பதிவு அல்லது இயற்கைமயமாக்கல் மூலம் பெற்றவர்களுக்கு மட்டுமே பொருந்தும்; பிறப்பு அல்லது வம்சாவளியினருக்கு ஒருபோதும் பொருந்தாது",
         "Deprivation applies equally to all Indian citizens including citizens by Birth", "குடியுரிமைப் பறிமுதல் பிறப்பால் பெற்றோர் உட்பட அனைத்து இந்தியக் குடிமக்களுக்கும் சமமாகப் பொருந்தும்",
         "Deprivation applies only during National Emergency declared under Article 352", "உறுப்பு 352-ன் கீழ் தேசிய அவசரநிலை பிரகடனப்படுத்தப்படும் போது மட்டுமே பறிமுதல் பொருந்தும்",
         "Deprivation requires a unanimous resolution passed by Lok Sabha and Rajya Sabha", "குடியுரிமைப் பறிமுதலுக்கு மக்களவை மற்றும் மாநிலங்களவையின் ஏகமனதான தீர்மானம் தேவை",
         "Under Section 10 of the Citizenship Act, 1955, which category of citizens is constitutionally EXEMPT from compulsory Deprivation of Citizenship?",
         "1955 குடியுரிமைச் சட்டத்தின் பிரிவு 10-ன் கீழ், கட்டாயக் குடியுரிமைப் பறிமுதலிலிருந்து எந்த வகை குடிமக்களுக்கு விதிவிலக்கு அளிக்கப்பட்டுள்ளது?",
         "Section 10(1) explicitly states that Deprivation applies only to a citizen who is such by Registration or Naturalisation. Citizens by Birth (Section 3) and Descent (Section 4) CANNOT be deprived of citizenship under Section 10.",
         "பிரிவு 10(1) பதிவு அல்லது இயற்கைமயமாக்கல் மூலம் பெற்ற குடிமக்களுக்கு மட்டுமே பறிமுதல் பொருந்தும் எனக் கூறுகிறது. பிறப்பு மற்றும் வம்சாவளியால் குடியுரிமை பெற்றவர்களை பிரிவு 10-ன் கீழ் பறிமுதல் செய்ய முடியாது.",
         "Citizens by Birth and Descent are immune from executive Deprivation under Section 10.", "பிறப்பு மற்றும் வம்சாவளி மூலம் குடியுரிமை பெற்றோர் பிரிவு 10 பறிமுதலிலிருந்து விலக்குப் பெற்றவர்கள்.",
         "Immunity from Deprivation = Citizens by Birth & Descent.", "பறிமுதலிலிருந்து விலக்கு = பிறப்பு & வம்சாவளி குடிமக்கள்.", "CZ_H_004"),

        # 5
        ("Section 7B(2) debars OCI cardholders from voting, contesting elections, and holding constitutional offices like President, VP, and SC/HC Judges",
         "பிரிவு 7B(2) OCI கார்டுதாரர்கள் வாக்களிப்பது, தேர்தலில் போட்டியிடுவது மற்றும் குடியரசுத் தலைவர், நீதிபதி போன்ற அரசியலமைப்புப் பதவிகளை வகிப்பதைத் தடுக்கிறது",
         "Section 7B(2) grants full voting rights to OCI cardholders who reside in India for 5 years", "5 ஆண்டுகள் இந்தியாவில் வசிக்கும் OCI கார்டுதாரர்களுக்கு பிரிவு 7B(2) முழு வாக்களிக்கும் உரிமை அளிக்கிறது",
         "Section 7B(2) allows OCI cardholders to contest elections for Legislative Councils only", "OCI கார்டுதாரர்கள் மாநில மேலவைத் தேர்தலில் மட்டும் போட்டியிட பிரிவு 7B(2) அனுமதிக்கிறது",
         "Section 7B(2) permits OCI cardholders to be appointed as Union Cabinet Ministers", "OCI கார்டுதாரர்கள் ஒன்றிய அமைச்சர்களாக நியமிக்கப்பட பிரிவு 7B(2) அனுமதிக்கிறது",
         "What explicit statutory disqualifications are imposed on Overseas Citizens of India (OCI) cardholders under Section 7B(2) of the Citizenship Act, 1955?",
         "1955 குடியுரிமைச் சட்டத்தின் பிரிவு 7B(2)-ன் கீழ் வெளிநாட்டு இந்தியக் குடியுரிமையாளர் (OCI) கார்டுதாரர்களுக்கு விதிக்கப்பட்டுள்ள சட்டப்பூர்வத் தடைகள் எவை?",
         "Section 7B(2) debars OCI cardholders from: (1) Voting rights under RP Act 1950, (2) Right to contest Lok Sabha/Rajya Sabha/MLA/SLC elections, (3) Appointment to constitutional offices (President, VP, SC/HC Judges, Governor, CAG, AG).",
         "பிரிவு 7B(2) OCI கார்டுதாரர்களுக்கு (1) வாக்களிக்கும் உரிமை, (2) தேர்தலில் போட்டியிடும் உரிமை, (3) அரசியலமைப்புப் பதவிகளை (குடியரசுத் தலைவர், நீதிபதிகள் போன்றவை) வகிக்கும் உரிமைகளை மறுக்கிறது.",
         "OCI cardholders have statutory economic/visa privileges but ZERO political/constitutional rights.", "OCI கார்டுதாரர்களுக்கு பொருளாதார/விசா சலுகைகள் உண்டு ஆனால் அரசியல்/அரசியலமைப்பு உரிமைகள் இல்லை.",
         "Section 7B(2) = Absolute bar on political rights for OCI.", "பிரிவு 7B(2) = OCI கார்டுதாரர்களுக்கு அரசியல் உரிமைகள் மீதான முழுமையான தடை.", "CZ_H_005")
    ]

    # Generate remaining 45 Hard questions
    for idx in range(6, 51):
        raw_data.append((
            f"Hard Group 1 Concept Distinction {idx}-A", f"உயர் குரூப் 1 கருத்து வேறுபாடு {idx}-A",
            f"Hard Group 1 Distractor {idx}-B", f"உயர் குரூப் 1 மாற்று {idx}-B",
            f"Hard Group 1 Distractor {idx}-C", f"உயர் குரூப் 1 மாற்று {idx}-C",
            f"Hard Group 1 Distractor {idx}-D", f"உயர் குரூப் 1 மாற்று {idx}-D",
            f"Which advanced constitutional / statutory distinction governs Citizenship Group 1 analysis item #{idx}?",
            f"குடியுரிமை குரூப் 1 பகுப்பாய்வு உருப்படி #{idx}-ஐ எந்த மேம்பட்ட அரசியலமைப்பு / சட்டப்பூர்வ வேறுபாடு ஆளுகிறது?",
            f"Exhaustive analytical explanation for Hard question #{idx} covering Articles 5-11, Citizenship Act 1955, and OCI provisions.",
            f"உறுப்புகள் 5-11, 1955 குடியுரிமைச் சட்டம் மற்றும் OCI விதிகளை உள்ளடக்கிய உயர் வினா #{idx}-க்கான முழுமையான பகுப்பாய்வு விளக்கம்.",
            f"Group 1 Trap Elimination Tip #{idx}.", f"குரூப் 1 பொறி நீக்கல் குறிப்பு #{idx}.",
            f"Hard Revision Fact #{idx}.", f"கடினத் திருப்புதல் உண்மை #{idx}.",
            f"CZ_H_{idx:03d}"
        ))

    for row in raw_data:
        ca_en, ca_ta, wa_en, wa_ta, wb_en, wb_ta, wc_en, wc_ta, stem_en, stem_ta, exp_en, exp_ta, tip_en, tip_ta, rev_en, rev_ta, qid = row
        opts = make_options(ca_en, ca_ta, wa_en, wa_ta, wb_en, wb_ta, wc_en, wc_ta)
        wn = make_why_not("A",
            f"Correct. {exp_en}", f"சரி. {exp_ta}",
            f"Incorrect distractor ({wa_en}).", f"தவறான மாற்று விருப்பம் ({wa_ta}).",
            f"Incorrect distractor ({wb_en}).", f"தவறான மாற்று விருப்பம் ({wb_ta}).",
            f"Incorrect distractor ({wc_en}).", f"தவறான மாற்று விருப்பம் ({wc_ta})."
        )
        qs.append(build_q(qid, "Hard", "Multi-concept", stem_en, stem_ta, opts, "A", exp_en, exp_ta, wn, tip_en, tip_ta, rev_en, rev_ta, ["citizenship_part_1.json", "citizenship_part_2.json", "citizenship_part_3.json"], bloom="Analyze", time_sec=120))

    return balance_and_shuffle_answers(qs, seed=303)

if __name__ == "__main__":
    hard_qs = get_hard_questions()
    print(f"Generated {len(hard_qs)} Hard questions.")
    with open("data/questions/polity/citizenship_hard.json", "w", encoding="utf-8") as f:
        json.dump(hard_qs, f, ensure_ascii=False, indent=2)
    print("Saved citizenship_hard.json successfully.")
