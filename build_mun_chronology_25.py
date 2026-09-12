# -*- coding: utf-8 -*-
"""
Builder for 25 Municipalities Chronology MCQs (MUN_C_001 to MUN_C_025).
Strictly adheres to 24-field schema, balanced keys, unique option permutations,
and authentic Tamil translation.
"""
import json
import os
from mun_mcq_helper import make_mun_q
from rebalance_mun_helper import balance_question_keys

def get_chronology_25():
    questions = []

    def make_chron_q(qid, subtopic, topic_label_en, topic_label_ta, events_en, events_ta, opt_tuples, correct_key, exp_en, exp_ta, tip_en, tip_ta, fact_en, fact_ta, tags):
        # Ensure all 4 options are distinct strings
        opts_set = set(t[1] for t in opt_tuples)
        assert len(opts_set) == 4, f"Options not unique in {qid}: {opts_set}"

        stem_en = f"Arrange the following events in chronological order ({topic_label_en}):\n"
        for num, text in events_en:
            stem_en += f"{num}. {text}\n"
        stem_en += "Select the correct chronological sequence:"

        stem_ta = f"பின்வரும் நிகழ்வுகளை காலவரிசைப்படி வரிசைப்படுத்துக ({topic_label_ta}):\n"
        for num, text in events_ta:
            stem_ta += f"{num}. {text}\n"
        stem_ta += "சரியான காலவரிசையைத் தேர்ந்தெடுக்கவும்:"

        en_opts = [t[1] for t in opt_tuples]
        ta_opts = [t[1] for t in opt_tuples]

        why_dict = {}
        for idx, key in enumerate(["A", "B", "C", "D"]):
            if key == correct_key:
                why_dict[f"why_{key.lower()}_en"] = f"Option {key} ({en_opts[idx]}) is correct. It accurately reflects the chronological order based on the historical timeline."
                why_dict[f"why_{key.lower()}_ta"] = f"விருப்பம் {key} ({en_opts[idx]}) சரியானது. வரலாற்று காலவரிசையின்படி இது சரியான வரிசையைக் குறிக்கிறது."
            else:
                why_dict[f"why_{key.lower()}_en"] = f"Option {key} ({en_opts[idx]}) is incorrect because the events are out of chronological order."
                why_dict[f"why_{key.lower()}_ta"] = f"விருப்பம் {key} ({en_opts[idx]}) தவறானது, ஏனெனில் நிகழ்வுகள் காலவரிசைப்படி அமையவில்லை."

        return make_mun_q(
            qid=qid,
            diff="Hard",
            qtype="Chronology",
            subtopic=subtopic,
            en_stem=stem_en,
            ta_stem=stem_ta,
            en_a=en_opts[0],
            ta_a=ta_opts[0],
            en_b=en_opts[1],
            ta_b=ta_opts[1],
            en_c=en_opts[2],
            ta_c=ta_opts[2],
            en_d=en_opts[3],
            ta_d=ta_opts[3],
            correct_key=correct_key,
            exp_en=exp_en,
            exp_ta=exp_ta,
            why_a_en=why_dict["why_a_en"],
            why_a_ta=why_dict["why_a_ta"],
            why_b_en=why_dict["why_b_en"],
            why_b_ta=why_dict["why_b_ta"],
            why_c_en=why_dict["why_c_en"],
            why_c_ta=why_dict["why_c_ta"],
            why_d_en=why_dict["why_d_en"],
            why_d_ta=why_dict["why_d_ta"],
            tip_en=tip_en,
            tip_ta=tip_ta,
            fact_en=fact_en,
            fact_ta=fact_ta,
            tags=tags
        )

    # C01: Colonial Foundations
    questions.append(make_chron_q(
        qid="MUN_C_001",
        subtopic="Colonial Evolution Set 1",
        topic_label_en="Early Municipal Milestones",
        topic_label_ta="ஆரம்பகால நகராட்சி மைல்கற்கள்",
        events_en=[
            ("1", "Royal Charter establishing Municipal Corporation at Madras"),
            ("2", "Royal Charter establishing Municipal Corporations and Mayor's Courts in Bombay and Calcutta"),
            ("3", "Lord Mayo's Resolution on Financial Decentralization"),
            ("4", "Lord Ripon's Landmark Resolution on Local Self-Government")
        ],
        events_ta=[
            ("1", "மெட்ராஸில் மாநகராட்சி அமைப்பதற்கான அரச பட்டயம் வழங்கப்படுதல்"),
            ("2", "பம்பாய் மற்றும் கல்கத்தாவில் மாநகராட்சிகள் மற்றும் மேயர் நீதிமன்றங்களை அமைத்த அரச பட்டயம்"),
            ("3", "நிதிப் பரவலாக்கம் குறித்த மேயோ பிரபுவின் தீர்மானம்"),
            ("4", "உள்ளாட்சி சுயஅரசாங்கம் குறித்த ரிப்பன் பிரபுவின் வரலாற்றுச் சிறப்புமிக்க தீர்மானம்")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "3 - 1 - 2 - 4")],
        correct_key="A",
        exp_en="Chronological timeline:\n1. Madras Corporation Charter: 1687 (inaugurated 1688)\n2. Bombay & Calcutta Corporations Charter: 1726\n3. Lord Mayo's Resolution: 1870\n4. Lord Ripon's Resolution: 1882.\nHence sequence is 1 - 2 - 3 - 4.",
        exp_ta="காலவரிசை:\n1. மெட்ராஸ் மாநகராட்சி பட்டயம்: 1687 (தொடக்கம் 1688)\n2. பம்பாய் மற்றும் கல்கத்தா மாநகராட்சி: 1726\n3. மேயோ பிரபுவின் தீர்மானம்: 1870\n4. ரிப்பன் பிரபுவின் தீர்மானம்: 1882.\nஎனவே சரியான வரிசை 1 - 2 - 3 - 4.",
        tip_en="Timeline anchor: Madras (1687) -> Bombay/Calcutta (1726) -> Mayo (1870) -> Ripon (1882).",
        tip_ta="நினைவுக்குறிப்பு: மெட்ராஸ் (1687) -> பம்பாய்/கல்கத்தா (1726) -> மேயோ (1870) -> ரிப்பன் (1882).",
        fact_en="Lord Ripon was the Viceroy of India from 1880 to 1884.",
        fact_ta="ரிப்பன் பிரபு 1880 முதல் 1884 வரை இந்தியாவின் வைஸ்ராயாக இருந்தார்.",
        tags=["colonial_evolution", "chronology", "ripon_mayo"]
    ))

    # C02: British Legislative Acts
    questions.append(make_chron_q(
        qid="MUN_C_002",
        subtopic="Colonial Acts Chronology",
        topic_label_en="Pre-Independence Statutory Acts",
        topic_label_ta="சுதந்திரத்திற்கு முந்தைய சட்டங்கள்",
        events_en=[
            ("1", "Act XXVI of 1850 (Permissive Municipal Act)"),
            ("2", "Towns Improvement Act of 1865 (Madras)"),
            ("3", "Government of India Act 1919 (Transferred Subject)"),
            ("4", "Government of India Act 1935 (Provincial Autonomy)")
        ],
        events_ta=[
            ("1", "1850-ஆம் ஆண்டின் சட்டம் XXVI (அனுமதித்த நகராட்சி சட்டம்)"),
            ("2", "1865-ஆம் ஆண்டின் நகர மேம்பாட்டுச் சட்டம் (மெட்ராஸ்)"),
            ("3", "1919-ஆம் ஆண்டு இந்திய அரசுச் சட்டம் (மாற்றப்பட்ட துறை)"),
            ("4", "1935-ஆம் ஆண்டு இந்திய அரசுச் சட்டம் (மாகாண தன்னாட்சி)")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 4 - 3"), ("C", "1 - 3 - 2 - 4"), ("D", "3 - 1 - 2 - 4")],
        correct_key="A",
        exp_en="Chronological order:\n1. Act XXVI: 1850\n2. Towns Improvement Act: 1865\n3. GoI Act: 1919\n4. GoI Act: 1935.\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="சரியான காலவரிசை:\n1. சட்டம் XXVI: 1850\n2. நகர மேம்பாட்டுச் சட்டம்: 1865\n3. இந்திய அரசுச் சட்டம்: 1919\n4. இந்திய அரசுச் சட்டம்: 1935.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="Statutory progression: 1850 -> 1865 -> 1919 -> 1935.",
        tip_ta="சட்டங்களின் வரிசை: 1850 -> 1865 -> 1919 -> 1935.",
        fact_en="Under the 1919 Act, local self-government came under elected Indian ministers for the first time.",
        fact_ta="1919 சட்டத்தின் கீழ் முதன்முறையாக உள்ளாட்சி அமைப்பு தேர்ந்தெடுக்கப்பட்ட இந்திய அமைச்சர்களின் கீழ் வந்தது.",
        tags=["colonial_statutes", "chronology", "1919_1935"]
    ))

    # C03: Post-Independence Urban Committees
    questions.append(make_chron_q(
        qid="MUN_C_003",
        subtopic="Urban Committees Set 1",
        topic_label_en="Post-Independence ULB Committees",
        topic_label_ta="சுதந்திரத்திற்குப் பிந்தைய நகர்ப்புற குழுக்கள்",
        events_en=[
            ("1", "Local Finance Enquiry Committee (P.K. Wattal)"),
            ("2", "Taxation Enquiry Commission (John Matthai)"),
            ("3", "Committee on Augmentation of Financial Resources of ULBs (Dr. Zakaria)"),
            ("4", "Rural-Urban Relationship Committee (A.P. Jain)")
        ],
        events_ta=[
            ("1", "உள்ளாட்சி நிதி ஆய்வுக் குழு (பி.கே. வாட்டல்)"),
            ("2", "வரிவிதிப்பு ஆய்வுக் குழு (ஜான் மத்தாய்)"),
            ("3", "நகர்ப்புற உள்ளாட்சி நிதி ஆதாரப் பெருக்கக் குழு (டாக்டர் ஜகாரியா)"),
            ("4", "கிராமப்புற-நகர்ப்புற உறவுக் குழு (ஏ.பி. ஜெயின்)")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "4 - 1 - 2 - 3")],
        correct_key="A",
        exp_en="Accurate committee chronology:\n1. Wattal Committee: 1949-51\n2. John Matthai Commission: 1953-54\n3. Zakaria Committee: 1963\n4. AP Jain Committee: 1963-66 (submitted final report in 1966 after Zakaria in 1963).\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="குழுக்களின் காலவரிசை:\n1. வாட்டல் குழு: 1949-51\n2. ஜான் மத்தாய் ஆணையம்: 1953-54\n3. ஜகாரியா குழு: 1963\n4. ஏ.பி. ஜெயின் குழு: 1963-66.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="Wattal (1949) -> Matthai (1953) -> Zakaria (1963) -> Jain (1963-66).",
        tip_ta="வாட்டல் (1949) -> மத்தாய் (1953) -> ஜகாரியா (1963) -> ஜெயின் (1963-66).",
        fact_en="John Matthai was India's first Railway Minister and subsequent Finance Minister.",
        fact_ta="ஜான் மத்தாய் இந்தியாவின் முதல் ரயில்வே அமைச்சர் மற்றும் முன்னாள் நிதி அமைச்சர் ஆவார்.",
        tags=["committees_chronology", "wattal_zakaria", "chronology"]
    ))

    # C04: Road to 74th Amendment
    questions.append(make_chron_q(
        qid="MUN_C_004",
        subtopic="Constitutional Journey",
        topic_label_en="Enactment Journey of 74th Amendment",
        topic_label_ta="74-வது திருத்தச் சட்டத்தின் சட்டப் பயணம்",
        events_en=[
            ("1", "National Commission on Urbanisation appointed under Charles Correa"),
            ("2", "P.K. Thungon Committee recommends constitutional recognition for urban local bodies"),
            ("3", "Introduction of 65th Constitutional Amendment (Nagarpalika) Bill by Rajiv Gandhi"),
            ("4", "Introduction of revised Nagarpalika Bill by V.P. Singh National Front Government")
        ],
        events_ta=[
            ("1", "சார்லஸ் கொரியா தலைமையில் தேசிய நகரமயமாக்கல் ஆணையம் அமைக்கப்படுதல்"),
            ("2", "பி.கே. துங்கன் குழு நகர்ப்புற உள்ளாட்சி அமைப்புகளுக்கு அரசியலமைப்பு அங்கீகாரம் பரிந்துரைத்தல்"),
            ("3", "ராஜீவ் காந்தி அரசால் 65-வது அரசியலமைப்பு திருத்த (நகர்பாலிகா) மசோதா அறிமுகப்படுத்தப்படுதல்"),
            ("4", "வி.பி. சிங் தலைமையிலான தேசிய முன்னணி அரசால் திருத்தப்பட்ட நகர்பாலிகா மசோதா அறிமுகம்")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "3 - 1 - 2 - 4")],
        correct_key="A",
        exp_en="Timeline of events:\n1. National Commission on Urbanisation: 1985 (reported 1988)\n2. P.K. Thungon Committee: 1988\n3. 65th Amendment Bill: August 1989\n4. V.P. Singh Bill: September 1990.\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="நிகழ்வுகளின் காலவரிசை:\n1. தேசிய நகரமயமாக்கல் ஆணையம்: 1985 (அறிக்கை 1988)\n2. பி.கே. துங்கன் குழு: 1988\n3. 65-வது திருத்த மசோதா: ஆகஸ்ட் 1989\n4. வி.பி. சிங் மசோதா: செப்டம்பர் 1990.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="Correa (1985) -> Thungon (1988) -> Rajiv Gandhi 65th (1989) -> VP Singh (1990).",
        tip_ta="கொரியா (1985) -> துங்கன் (1988) -> ராஜீவ் காந்தி (1989) -> வி.பி. சிங் (1990).",
        fact_en="Both the 65th Bill (1989) and the 1990 Bill failed before the Narasimha Rao govt succeeded in 1992.",
        fact_ta="1989 மற்றும் 1990 மசோதாக்கள் தோல்வியடைந்த பின் நரசிம்ம ராவ் அரசு 1992-ல் வெற்றி பெற்றது.",
        tags=["road_to_74th_caa", "nagarpalika_bill", "chronology"]
    ))

    # C05: 74th Amendment Bill Milestones
    questions.append(make_chron_q(
        qid="MUN_C_005",
        subtopic="Legislative Enactment Dates",
        topic_label_en="74th Amendment Legislative Milestones",
        topic_label_ta="74-வது திருத்தச் சட்டத்தின் முக்கிய தேதிகள்",
        events_en=[
            ("1", "74th Amendment Bill introduced in Lok Sabha by P.V. Narasimha Rao Government (September 1991)"),
            ("2", "Bill passed by Parliament (December 1992)"),
            ("3", "Bill receives Presidential assent (April 20, 1993)"),
            ("4", "74th Constitutional Amendment Act comes into force (June 1, 1993)")
        ],
        events_ta=[
            ("1", "பி.வி. நரசிம்ம ராவ் அரசால் 74-வது திருத்த மசோதா மக்களவையில் அறிமுகம் (செப்டம்பர் 1991)"),
            ("2", "நாடாளுமன்றத்தின் இரு அவைகளிலும் மசோதா நிறைவேற்றம் (டிசம்பர் 1992)"),
            ("3", "மசோதாவிற்கு குடியரசுத் தலைவர் ஒப்புதல் அளித்தல் (ஏப்ரல் 20, 1993)"),
            ("4", "74-வது அரசியலமைப்பு திருத்தச் சட்டம் நடைமுறைக்கு வருதல் (ஜூன் 1, 1993)")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "4 - 3 - 2 - 1")],
        correct_key="A",
        exp_en="Precise legislative sequence:\n1. Introduction in Lok Sabha: September 1991\n2. Passed by Lok Sabha (Dec 22) and Rajya Sabha (Dec 23): December 1992\n3. Presidential assent: April 20, 1993\n4. Enforcement date: June 1, 1993.\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="சட்டமன்ற நிகழ்வுகளின் வரிசை:\n1. மக்களவையில் அறிமுகம்: செப்டம்பர் 1991\n2. நாடாளுமன்றத்தில் நிறைவேற்றம்: டிசம்பர் 1992\n3. குடியரசுத் தலைவர் ஒப்புதல்: ஏப்ரல் 20, 1993\n4. நடைமுறைக்கு வந்த நாள்: ஜூன் 1, 1993.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="Sep 1991 (Intro) -> Dec 1992 (Passage) -> Apr 1993 (Assent) -> Jun 1, 1993 (Enforcement).",
        tip_ta="செப் 1991 -> டிச 1992 -> ஏப்ரல் 1993 -> ஜூன் 1, 1993.",
        fact_en="Over 50% of the State Legislatures ratified the bill between December 1992 and April 1993.",
        fact_ta="டிசம்பர் 1992 முதல் ஏப்ரல் 1993 வரை 50%க்கும் அதிகமான மாநில சட்டமன்றங்கள் இதற்கு ஒப்புதல் அளித்தன.",
        tags=["74th_caa_enactment", "dates_milestones", "chronology"]
    ))

    # C06: Tamil Nadu Municipal Corporations Set 1
    questions.append(make_chron_q(
        qid="MUN_C_006",
        subtopic="TN Corporations Evolution 1",
        topic_label_en="First Four Corporations in Tamil Nadu",
        topic_label_ta="தமிழ்நாட்டின் முதல் நான்கு மாநகராட்சிகள்",
        events_en=[
            ("1", "Establishment of Madras Corporation"),
            ("2", "Elevation of Madurai to Corporation"),
            ("3", "Elevation of Coimbatore to Corporation"),
            ("4", "Elevation of Tiruchirappalli to Corporation")
        ],
        events_ta=[
            ("1", "மெட்ராஸ் மாநகராட்சி தோற்றுவிக்கப்படுதல்"),
            ("2", "மதுரை மாநகராட்சியாக தரம் உயர்த்தப்படுதல்"),
            ("3", "கோயம்புத்தூர் மாநகராட்சியாக தரம் உயர்த்தப்படுதல்"),
            ("4", "திருச்சிராப்பள்ளி மாநகராட்சியாக தரம் உயர்த்தப்படுதல்")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "3 - 1 - 2 - 4")],
        correct_key="A",
        exp_en="Elevation sequence:\n1. Chennai (Madras): 1688\n2. Madurai: 1971\n3. Coimbatore: 1981\n4. Tiruchirappalli: 1994 (along with Salem).\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="மாநகராட்சிகள் அமைக்கப்பட்ட காலவரிசை:\n1. சென்னை: 1688\n2. மதுரை: 1971\n3. கோயம்புத்தூர்: 1981\n4. திருச்சிராப்பள்ளி: 1994.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="TN Corporation Order: Chennai (1688) -> Madurai (1971) -> Coimbatore (1981) -> Trichy (1994).",
        tip_ta="வரிசை: சென்னை (1688) -> மதுரை (1971) -> கோவை (1981) -> திருச்சி (1994).",
        fact_en="Salem Corporation was established in the same year as Tiruchirappalli (1994).",
        fact_ta="சேலம் மாநகராட்சி திருச்சிராப்பள்ளியுடன் அதே ஆண்டில் (1994) அமைக்கப்பட்டது.",
        tags=["tn_corporations", "chennai_madurai_coimbatore", "chronology"]
    ))

    # C07: Tamil Nadu Municipal Corporations Set 2
    questions.append(make_chron_q(
        qid="MUN_C_007",
        subtopic="TN Corporations Evolution 2",
        topic_label_en="Corporations Elevated from 1994 to 2014",
        topic_label_ta="1994 முதல் 2014 வரை அமைக்கப்பட்ட மாநகராட்சிகள்",
        events_en=[
            ("1", "Tirunelveli Municipal Corporation"),
            ("2", "Tiruppur Municipal Corporation"),
            ("3", "Vellore Municipal Corporation"),
            ("4", "Thanjavur Municipal Corporation")
        ],
        events_ta=[
            ("1", "திருநெல்வேலி மாநகராட்சி"),
            ("2", "திருப்பூர் மாநகராட்சி"),
            ("3", "வேலூர் மாநகராட்சி"),
            ("4", "தஞ்சாவூர் மாநகராட்சி")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "4 - 1 - 2 - 3")],
        correct_key="A",
        exp_en="Chronological order:\n1. Tirunelveli: 1994\n2. Tiruppur: 2008 (elevated in early 2008)\n3. Vellore: 2008 (elevated mid 2008 with Thoothukudi)\n4. Thanjavur: 2014 (elevated with Dindigul).\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="காலவரிசை:\n1. திருநெல்வேலி: 1994\n2. திருப்பூர்: 2008\n3. வேலூர்: 2008\n4. தஞ்சாவூர்: 2014.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="Tirunelveli (1994) -> Tiruppur/Vellore (2008) -> Thanjavur (2014).",
        tip_ta="நெல்லை (1994) -> திருப்பூர்/வேலூர் (2008) -> தஞ்சை (2014).",
        fact_en="Dindigul and Thanjavur were both upgraded in 2014.",
        fact_ta="திண்டுக்கல் மற்றும் தஞ்சாவூர் இரண்டும் 2014-ல் தரம் உயர்த்தப்பட்டன.",
        tags=["tn_corporations_2", "tirunelveli_thanjavur", "chronology"]
    ))

    # C08: Recent Tamil Nadu Corporations (2019 - 2021)
    questions.append(make_chron_q(
        qid="MUN_C_008",
        subtopic="TN Corporations Evolution 3",
        topic_label_en="Elevation of Recent Corporations in TN",
        topic_label_ta="சமீபத்திய தமிழக மாநகராட்சிகள்",
        events_en=[
            ("1", "Nagercoil Corporation"),
            ("2", "Avadi Corporation"),
            ("3", "Tambaram Corporation"),
            ("4", "Kanchipuram & Sivakasi Corporations")
        ],
        events_ta=[
            ("1", "நாகர்கோவில் மாநகராட்சி"),
            ("2", "ஆவடி மாநகராட்சி"),
            ("3", "தாம்பரம் மாநகராட்சி"),
            ("4", "காஞ்சிபுரம் & சிவகாசி மாநகராட்சிகள்")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "3 - 1 - 2 - 4")],
        correct_key="A",
        exp_en="Elevation timeline:\n1. Nagercoil: February 2019 (along with Hosur)\n2. Avadi: June 2019\n3. Tambaram: November 2021\n4. Kanchipuram & Sivakasi: Late November 2021 (along with Karur and Cuddalore).\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="காலவரிசை:\n1. நாகர்கோவில்: பிப்ரவரி 2019\n2. ஆவடி: ஜூன் 2019\n3. தாம்பரம்: நவம்பர் 2021\n4. காஞ்சிபுரம் & சிவகாசி: நவம்பர் 2021 இறுதி.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="Nagercoil/Hosur (Early 2019) -> Avadi (Mid 2019) -> Tambaram/Kanchi/Sivakasi (Late 2021).",
        tip_ta="நாகர்கோவில்/ஓசூர் (2019 தொடக்கம்) -> ஆவடி (2019 நடுப்பகுதி) -> தாம்பரம்/காஞ்சி (2021).",
        fact_en="Sivakasi is world-renowned as the fireworks and printing capital of India.",
        fact_ta="சிவகாசி இந்தியாவின் பட்டாசு மற்றும் அச்சுத் தொழிலின் தலைநகரமாக விளங்குகிறது.",
        tags=["recent_tn_corporations", "chronology", "2019_2021"]
    ))

    # C09: Evolution of Central Urban Schemes
    questions.append(make_chron_q(
        qid="MUN_C_009",
        subtopic="Central Urban Programs",
        topic_label_en="Evolution of Central Urban Missions",
        topic_label_ta="மத்திய நகர்ப்புற திட்டங்களின் பரிணாமம்",
        events_en=[
            ("1", "Integrated Development of Small and Medium Towns (IDSMT)"),
            ("2", "Jawaharlal Nehru National Urban Renewal Mission (JNNURM)"),
            ("3", "Swachh Bharat Mission (Urban)"),
            ("4", "Smart Cities Mission & AMRUT")
        ],
        events_ta=[
            ("1", "சிறு மற்றும் நடுத்தர நகரங்களின் ஒருங்கிணைந்த வளர்ச்சித் திட்டம் (IDSMT)"),
            ("2", "ஜவஹர்லால் நேரு தேசிய நகர்ப்புற புதுப்பித்தல் இயக்கம் (JNNURM)"),
            ("3", "தூய்மை இந்தியா இயக்கம் (நகர்ப்புறம்)"),
            ("4", "ஸ்மார்ட் சிட்டீஸ் திட்டம் & அம்ருத் (AMRUT)")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 4 - 3"), ("C", "1 - 3 - 2 - 4"), ("D", "3 - 1 - 2 - 4")],
        correct_key="A",
        exp_en="Chronological launch dates:\n1. IDSMT: 1979-80\n2. JNNURM: December 2005\n3. Swachh Bharat Mission (Urban): October 2, 2014\n4. Smart Cities Mission & AMRUT: June 25, 2015.\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="திட்டங்கள் தொடங்கப்பட்ட காலவரிசை:\n1. IDSMT: 1979-80\n2. JNNURM: டிசம்பர் 2005\n3. தூய்மை இந்தியா இயக்கம்: அக்டோபர் 2, 2014\n4. ஸ்மார்ட் சிட்டீஸ் & அம்ருத்: ஜூன் 25, 2015.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="Urban Missions: IDSMT (1979) -> JNNURM (2005) -> SBM-U (2014) -> Smart Cities/AMRUT (2015).",
        tip_ta="IDSMT (1979) -> JNNURM (2005) -> தூய்மை இந்தியா (2014) -> ஸ்மார்ட் சிட்டீஸ் (2015).",
        fact_en="JNNURM was the first mission to link central capital grants with mandatory municipal governance reforms.",
        fact_ta="JNNURM மத்திய மானியங்களை கட்டாய நகராட்சி சீர்திருத்தங்களுடன் இணைத்த முதல் திட்டமாகும்.",
        tags=["central_schemes", "jnnurm_amrut", "chronology"]
    ))

    # C10: Major Central Statutes on Urban Governance
    questions.append(make_chron_q(
        qid="MUN_C_010",
        subtopic="Central Urban Acts",
        topic_label_en="Enactment of Central Municipal Statutes",
        topic_label_ta="மத்திய நகர்ப்புற சட்டங்கள் இயற்றப்பட்ட வரிசை",
        events_en=[
            ("1", "Cantonments Act, 1924"),
            ("2", "Major Port Trusts Act, 1963"),
            ("3", "Registration of Births and Deaths Act, 1969"),
            ("4", "Cantonments Act, 2006 (repealing 1924 Act)")
        ],
        events_ta=[
            ("1", "1924-ஆம் ஆண்டின் பாசறைகள் சட்டம்"),
            ("2", "1963-ஆம் ஆண்டின் பெரிய துறைமுகப் பொறுப்புக் கழகச் சட்டம்"),
            ("3", "1969-ஆம் ஆண்டின் பிறப்பு மற்றும் இறப்பு பதிவு சட்டம்"),
            ("4", "2006-ஆம் ஆண்டின் பாசறைகள் சட்டம் (1924 சட்டத்தை ரத்து செய்தது)")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "4 - 1 - 2 - 3")],
        correct_key="A",
        exp_en="Chronological order:\n1. Cantonments Act: 1924\n2. Major Port Trusts Act: 1963\n3. RBD Act: 1969\n4. Modern Cantonments Act: 2006.\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="காலவரிசை:\n1. பாசறைகள் சட்டம்: 1924\n2. பெரிய துறைமுகங்கள் சட்டம்: 1963\n3. பிறப்பு/இறப்பு பதிவு சட்டம்: 1969\n4. புதிய பாசறைகள் சட்டம்: 2006.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="Acts: 1924 (Cantonment old) -> 1963 (Port) -> 1969 (RBD) -> 2006 (Cantonment new).",
        tip_ta="சட்டங்கள்: 1924 -> 1963 -> 1969 -> 2006.",
        fact_en="The Cantonments Act 2006 introduced reservations for women and modern financial accountability.",
        fact_ta="2006 பாசறைகள் சட்டம் பெண்களுக்கு இடஒதுக்கீடு மற்றும் நவீன நிதி தணிக்கையை அறிமுகப்படுத்தியது.",
        tags=["central_statutes", "cantonments_port_trust", "chronology"]
    ))

    # C11: Constitutional Articles Part IXA Sequential 1
    questions.append(make_chron_q(
        qid="MUN_C_011",
        subtopic="Articles Sequence 1",
        topic_label_en="Constitutional Articles Sequence (243P - 243S)",
        topic_label_ta="அரசியலமைப்பு உறுப்புகள் வரிசை (243P - 243S)",
        events_en=[
            ("1", "Article 243P (Definitions)"),
            ("2", "Article 243Q (Constitution of Municipalities)"),
            ("3", "Article 243R (Composition of Municipalities)"),
            ("4", "Article 243S (Constitution and composition of Wards Committees)")
        ],
        events_ta=[
            ("1", "உறுப்பு 243P (வரைவிலக்கணங்கள்)"),
            ("2", "உறுப்பு 243Q (நகராட்சிகள் அமைத்தல்)"),
            ("3", "உறுப்பு 243R (நகராட்சிகளின் கட்டமைப்பு)"),
            ("4", "உறுப்பு 243S (வார்டு குழுக்கள் அமைத்தல் மற்றும் கட்டமைப்பு)")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "4 - 3 - 2 - 1")],
        correct_key="A",
        exp_en="Sequential alphabetical order in Part IXA:\n1. Article 243P\n2. Article 243Q\n3. Article 243R\n4. Article 243S.\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="பகுதி IXA-ன் அகரவரிசை உறுப்புகள்:\n1. உறுப்பு 243P\n2. உறுப்பு 243Q\n3. உறுப்பு 243R\n4. உறுப்பு 243S.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="Alphabetical order in Constitution: P -> Q -> R -> S.",
        tip_ta="அகரவரிசை: P -> Q -> R -> S.",
        fact_en="Part IX covers 243 to 243-O; Part IXA covers 243P to 243ZG.",
        fact_ta="பகுதி IX 243 முதல் 243-O வரை; பகுதி IXA 243P முதல் 243ZG வரை.",
        tags=["articles_sequence", "243p_to_243s", "chronology"]
    ))

    # C12: Constitutional Articles Part IXA Sequential 2
    questions.append(make_chron_q(
        qid="MUN_C_012",
        subtopic="Articles Sequence 2",
        topic_label_en="Constitutional Articles Sequence (243T - 243W)",
        topic_label_ta="அரசியலமைப்பு உறுப்புகள் வரிசை (243T - 243W)",
        events_en=[
            ("1", "Article 243T (Reservation of seats)"),
            ("2", "Article 243U (Duration of Municipalities)"),
            ("3", "Article 243V (Disqualifications for membership)"),
            ("4", "Article 243W (Powers, authority and responsibilities)")
        ],
        events_ta=[
            ("1", "உறுப்பு 243T (இடஒதுக்கீடு)"),
            ("2", "உறுப்பு 243U (நகராட்சிகளின் பதவிக்காலம்)"),
            ("3", "உறுப்பு 243V (உறுப்பினர் தகுதிநீக்கங்கள்)"),
            ("4", "உறுப்பு 243W (அதிகாரங்கள், பொறுப்புகள்)")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "3 - 1 - 4 - 2")],
        correct_key="A",
        exp_en="Sequential alphabetical order:\n1. Article 243T\n2. Article 243U\n3. Article 243V\n4. Article 243W.\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="அகரவரிசை உறுப்புகள்:\n1. உறுப்பு 243T\n2. உறுப்பு 243U\n3. உறுப்பு 243V\n4. உறுப்பு 243W.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="T -> U -> V -> W.",
        tip_ta="T -> U -> V -> W.",
        fact_en="Article 243T reservation provisions are subject to the same sunset timeline as Article 334 for SC/ST quotas.",
        fact_ta="உறுப்பு 243T இடஒதுக்கீடு SC/ST பிரிவினருக்கு உறுப்பு 334-ன் கால வரம்பிற்கு உட்பட்டது.",
        tags=["articles_sequence", "243t_to_243w", "chronology"]
    ))

    # C13: Constitutional Articles Part IXA Sequential 3
    questions.append(make_chron_q(
        qid="MUN_C_013",
        subtopic="Articles Sequence 3",
        topic_label_en="Constitutional Articles Sequence (243X - 243ZA)",
        topic_label_ta="அரசியலமைப்பு உறுப்புகள் வரிசை (243X - 243ZA)",
        events_en=[
            ("1", "Article 243X (Taxes and Funds)"),
            ("2", "Article 243Y (Finance Commission)"),
            ("3", "Article 243Z (Audit of accounts)"),
            ("4", "Article 243ZA (Elections to Municipalities)")
        ],
        events_ta=[
            ("1", "உறுப்பு 243X (வரிகள் மற்றும் நிதிகள்)"),
            ("2", "உறுப்பு 243Y (நிதி ஆணையம்)"),
            ("3", "உறுப்பு 243Z (கணக்குகள் தணிக்கை)"),
            ("4", "உறுப்பு 243ZA (நகராட்சிகளுக்கான தேர்தல்கள்)")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "4 - 3 - 2 - 1")],
        correct_key="A",
        exp_en="Sequential order:\n1. Article 243X\n2. Article 243Y\n3. Article 243Z\n4. Article 243ZA.\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="அகரவரிசை:\n1. உறுப்பு 243X\n2. உறுப்பு 243Y\n3. உறுப்பு 243Z\n4. உறுப்பு 243ZA.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="X -> Y -> Z -> ZA.",
        tip_ta="X -> Y -> Z -> ZA.",
        fact_en="After single letter Z, the sequence rolls into dual letters: ZA, ZB, ZC, ZD, ZE, ZF, ZG.",
        fact_ta="Z-க்கு பிறகு ZA, ZB, ZC, ZD, ZE, ZF, ZG என இரட்டை எழுத்துக்களாக தொடர்கிறது.",
        tags=["articles_sequence", "243x_to_243za", "chronology"]
    ))

    # C14: Constitutional Articles Part IXA Sequential 4
    questions.append(make_chron_q(
        qid="MUN_C_014",
        subtopic="Articles Sequence 4",
        topic_label_en="Constitutional Articles Sequence (243ZD - 243ZG)",
        topic_label_ta="அரசியலமைப்பு உறுப்புகள் வரிசை (243ZD - 243ZG)",
        events_en=[
            ("1", "Article 243ZD (Committee for District Planning)"),
            ("2", "Article 243ZE (Committee for Metropolitan Planning)"),
            ("3", "Article 243ZF (Continuance of existing laws and municipalities)"),
            ("4", "Article 243ZG (Bar to interference by courts in electoral matters)")
        ],
        events_ta=[
            ("1", "உறுப்பு 243ZD (மாவட்ட திட்டக் குழு)"),
            ("2", "உறுப்பு 243ZE (பெருநகர திட்டக் குழு)"),
            ("3", "உறுப்பு 243ZF (நடைமுறையிலுள்ள சட்டங்கள் மற்றும் நகராட்சிகள் தொடருதல்)"),
            ("4", "உறுப்பு 243ZG (தேர்தல் விவகாரங்களில் நீதிமன்றங்கள் தலையிடத் தடை)")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "4 - 3 - 2 - 1")],
        correct_key="A",
        exp_en="Concluding sequence of Part IXA:\n1. Article 243ZD (DPC)\n2. Article 243ZE (MPC)\n3. Article 243ZF (Transitional)\n4. Article 243ZG (Judicial Bar).\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="பகுதி IXA-ன் நிறைவு உறுப்புகள்:\n1. உறுப்பு 243ZD (DPC)\n2. உறுப்பு 243ZE (MPC)\n3. உறுப்பு 243ZF (இடைக்கால விதி)\n4. உறுப்பு 243ZG (நீதிமன்றத் தடை).\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="ZD (District) -> ZE (Metro) -> ZF (Transition) -> ZG (Bar).",
        tip_ta="ZD (மாவட்டம்) -> ZE (பெருநகரம்) -> ZF (இடைக்காலம்) -> ZG (தடை).",
        fact_en="Article 243ZG is the final barrier protecting completed local elections from routine litigation.",
        fact_ta="உறுப்பு 243ZG தேர்தல் முடிவுகளை வழக்கமான வழக்குகளிலிருந்து பாதுகாக்கும் இறுதிக் கவசமாகும்.",
        tags=["articles_sequence", "243zd_to_243zg", "chronology"]
    ))

    # C15: Sequential Steps in Municipal Election
    questions.append(make_chron_q(
        qid="MUN_C_015",
        subtopic="Election Administration",
        topic_label_en="Procedural Sequence of Municipal Elections",
        topic_label_ta="நகராட்சித் தேர்தல் நடைமுறைகளின் காலவரிசை",
        events_en=[
            ("1", "Delimitation of wards and reservation notification by State Government"),
            ("2", "Preparation and publication of ward-wise electoral rolls by SEC"),
            ("3", "Issuance of statutory election notification and filing of nominations"),
            ("4", "Polling, counting of votes, and declaration of results")
        ],
        events_ta=[
            ("1", "வார்டுகள் மறுவரையறை மற்றும் இடஒதுக்கீடு அறிவிப்பு வெளியிடுதல்"),
            ("2", "SEC மூலம் வார்டு வாரியான வாக்காளர் பட்டியல் தயாரித்து வெளியிடப்படுதல்"),
            ("3", "சட்டப்பூர்வ தேர்தல் அறிவிப்பு மற்றும் வேட்புமனு தாக்கல் தொடங்குதல்"),
            ("4", "வாக்குப்பதிவு, வாக்கு எண்ணிக்கை மற்றும் தேர்தல் முடிவுகள் அறிவிப்பு")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "3 - 1 - 2 - 4")],
        correct_key="A",
        exp_en="Standard election cycle:\n1. Delimitation & Reservation notification\n2. Preparation of Electoral Rolls\n3. Statutory Notification & Nominations\n4. Polling, Counting & Declaration.\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="தேர்தல் நடைமுறைகளின் வரிசை:\n1. மறுவரையறை & இடஒதுக்கீடு\n2. வாக்காளர் பட்டியல் தயாரிப்பு\n3. தேர்தல் அறிவிப்பு & வேட்புமனு\n4. வாக்குப்பதிவு & முடிவு அறிவிப்பு.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="Delimitation -> Electoral Rolls -> Notification & Nominations -> Voting & Results.",
        tip_ta="மறுவரையறை -> வாக்காளர் பட்டியல் -> தேர்தல் அறிவிப்பு -> வாக்குப்பதிவு.",
        fact_en="Once step 3 begins, Article 243ZG completely bars court intervention.",
        fact_ta="படி 3 தொடங்கியவுடன் உறுப்பு 243ZG நீதிமன்ற தலையீட்டை முழுமையாகத் தடுக்கிறது.",
        tags=["election_procedure", "chronology", "process"]
    ))

    # C16: Evolution of Local Government Legislation in Tamil Nadu
    questions.append(make_chron_q(
        qid="MUN_C_016",
        subtopic="TN Statutory Evolution",
        topic_label_en="Statutory Acts of Tamil Nadu Urban Governance",
        topic_label_ta="தமிழக நகர்ப்புற உள்ளாட்சி சட்டங்களின் வரலாறு",
        events_en=[
            ("1", "Madras City Municipal Act, 1919 (governing Corporation of Madras)"),
            ("2", "Tamil Nadu District Municipalities Act, 1920"),
            ("3", "Madurai City Municipal Corporation Act, 1971"),
            ("4", "Tamil Nadu Urban Local Bodies Act, 1998")
        ],
        events_ta=[
            ("1", "1919-ஆம் ஆண்டின் மெட்ராஸ் மாநகராட்சி சட்டம்"),
            ("2", "1920-ஆம் ஆண்டின் தமிழ்நாடு மாவட்ட நகராட்சிகள் சட்டம்"),
            ("3", "1971-ஆம் ஆண்டின் மதுரை மாநகராட்சி சட்டம்"),
            ("4", "1998-ஆம் ஆண்டின் தமிழ்நாடு நகர்ப்புற உள்ளாட்சி அமைப்புகள் சட்டம்")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "4 - 1 - 2 - 3")],
        correct_key="A",
        exp_en="Tamil Nadu urban statutory milestones:\n1. Madras City Municipal Act: 1919\n2. TN District Municipalities Act: 1920\n3. Madurai Corporation Act: 1971\n4. TN Urban Local Bodies Act: 1998.\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="தமிழக நகராட்சி சட்டங்களின் வரலாறு:\n1. மெட்ராஸ் மாநகராட்சி சட்டம்: 1919\n2. தமிழ்நாடு மாவட்ட நகராட்சிகள் சட்டம்: 1920\n3. மதுரை மாநகராட்சி சட்டம்: 1971\n4. தமிழ்நாடு நகர்ப்புற உள்ளாட்சி சட்டம்: 1998.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="TN Acts: 1919 (Madras) -> 1920 (District Municipalities) -> 1971 (Madurai) -> 1998 (Urban Local Bodies).",
        tip_ta="தமிழ்நாடு சட்டங்கள்: 1919 -> 1920 -> 1971 -> 1998.",
        fact_en="Comprehensive unified rules under the TN Urban Local Bodies Act were notified in 2023.",
        fact_ta="தமிழ்நாடு நகர்ப்புற உள்ளாட்சி சட்டத்தின் கீழான ஒருங்கிணைந்த புதிய விதிகள் 2023-ல் வெளியிடப்பட்டன.",
        tags=["tn_statutory_acts", "1919_1920_1998", "chronology"]
    ))

    # C17: Evolution of Women's Local Representation in TN
    questions.append(make_chron_q(
        qid="MUN_C_017",
        subtopic="TN Women Representation Evolution",
        topic_label_en="Evolution of Women's Representation in TN Local Bodies",
        topic_label_ta="தமிழக உள்ளாட்சிகளில் பெண்கள் இடஒதுக்கீடு பரிணாமம்",
        events_en=[
            ("1", "Enactment of Tamil Nadu Municipal Laws (Amendment) Act providing 33% reservation for women"),
            ("2", "First municipal elections held under Part IXA in Tamil Nadu with 33% quota for women"),
            ("3", "Enactment of landmark amendment bill enhancing women's reservation to 50%"),
            ("4", "First urban local body elections held in Tamil Nadu with 50% reservation for women")
        ],
        events_ta=[
            ("1", "பெண்களுக்கு 33% இடஒதுக்கீடு வழங்கும் தமிழ்நாடு நகராட்சி சட்டத் திருத்தம் இயற்றப்படுதல்"),
            ("2", "33% ஒதுக்கீட்டுடன் பகுதி IXA-ன் கீழ் தமிழ்நாட்டில் முதல் நகராட்சித் தேர்தல்கள் நடைபெறுதல்"),
            ("3", "பெண்கள் இடஒதுக்கீட்டை 50%-ஆக உயர்த்திய வரலாற்றுச் சிறப்புமிக்க திருத்தச் சட்டம் இயற்றப்படுதல்"),
            ("4", "50% பெண்கள் இடஒதுக்கீட்டுடன் தமிழ்நாட்டில் முதல் நகர்ப்புற உள்ளாட்சித் தேர்தல்கள் நடைபெறுதல்")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "3 - 1 - 2 - 4")],
        correct_key="A",
        exp_en="Milestones in women's empowerment in TN:\n1. 33% Reservation Enactment: 1994\n2. First 33% Elections: October 1996\n3. 50% Reservation Enactment: February 2016\n4. First 50% Urban Elections: February 2022.\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="தமிழகத்தில் பெண்கள் அதிகாரமளித்தல் மைல்கற்கள்:\n1. 33% இடஒதுக்கீடு சட்டம்: 1994\n2. முதல் 33% தேர்தல்: அக்டோபர் 1996\n3. 50% இடஒதுக்கீடு சட்டம்: பிப்ரவரி 2016\n4. முதல் 50% நகர்ப்புற தேர்தல்: பிப்ரவரி 2022.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="TN Women Quota Timeline: 1994 (33% Act) -> 1996 (33% Polls) -> 2016 (50% Act) -> 2022 (50% Polls).",
        tip_ta="1994 (33% சட்டம்) -> 1996 (தேர்தல்) -> 2016 (50% சட்டம்) -> 2022 (தேர்தல்).",
        fact_en="R. Priya was elected as Chennai's first Dalit woman Mayor following the 2022 elections.",
        fact_ta="2022 தேர்தலுக்குப் பிறகு ஆர். பிரியா சென்னையின் முதல் தலித் பெண் மேயராக தேர்ந்தெடுக்கப்பட்டார்.",
        tags=["women_representation_tn", "chronology", "1994_2022"]
    ))

    # C18: Evolution of Municipal Accounting Standards
    questions.append(make_chron_q(
        qid="MUN_C_018",
        subtopic="Municipal Accounting Reforms",
        topic_label_en="Evolution of Municipal Financial Accounting",
        topic_label_ta="நகராட்சி நிதி கணக்கியல் முறைகளின் பரிணாமம்",
        events_en=[
            ("1", "Traditional single-entry cash-based municipal accounting system"),
            ("2", "National Municipal Accounting Manual (NMAM) developed by Union Ministry"),
            ("3", "Transition to accrual-based double-entry accounting system across urban local bodies"),
            ("4", "Integration of digital GIS-based real-time property tax accounting and online payments")
        ],
        events_ta=[
            ("1", "பாரம்பரிய ஒற்றைப் பதிவு ரொக்க அடிப்படையிலான நகராட்சி கணக்கியல் முறை"),
            ("2", "மத்திய அமைச்சகத்தால் தேசிய நகராட்சி கணக்கியல் கையேடு (NMAM) உருவாக்கப்படுதல்"),
            ("3", "நகர்ப்புற உள்ளாட்சிகளில் இருமுறைப் பதிவு நிதிசார் கணக்கியல் முறைக்கு (Accrual) மாறுதல்"),
            ("4", "டிஜிட்டல் GIS அடிப்படையிலான நிகழ்நேர சொத்துவரி கணக்கியல் மற்றும் ஆன்லைன் கட்டண ஒருங்கிணைப்பு")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "4 - 1 - 2 - 3")],
        correct_key="A",
        exp_en="Evolutionary accounting stages:\n1. Colonial cash-based single entry (pre-2000s)\n2. NMAM released in December 2004\n3. Nationwide transition to accrual-based double entry (2005 onwards under JNNURM)\n4. GIS-integrated digital revenue platforms (2018 onwards).\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="கணக்கியல் சீர்திருத்த படிகள்:\n1. ரொக்க முறை (2000-க்கு முன்)\n2. NMAM கையேடு (2004)\n3. இருமுறைப் பதிவு நிதிசார் கணக்கியல் (2005 முதல்)\n4. GIS டிஜிட்டல் முறை (2018 முதல்).\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="Cash system -> NMAM (2004) -> Accrual Double Entry (2005) -> GIS Digital (2018).",
        tip_ta="ரொக்க முறை -> NMAM (2004) -> இருமுறைப் பதிவு (2005) -> GIS (2018).",
        fact_en="Tamil Nadu was among the first states to convert all municipalities to accrual-based accounting.",
        fact_ta="அனைத்து நகராட்சிகளையும் இருமுறைப் பதிவு முறைக்கு மாற்றிய முதல் மாநிலங்களில் தமிழ்நாடு ஒன்றாகும்.",
        tags=["accounting_reforms", "nmam_accrual", "chronology"]
    ))

    # C19: Solid Waste Management Regulatory Framework
    questions.append(make_chron_q(
        qid="MUN_C_019",
        subtopic="Solid Waste Rules Evolution",
        topic_label_en="Evolution of Urban Solid Waste Management Rules",
        topic_label_ta="நகர்ப்புற திடக்கழிவு மேலாண்மை விதிகளின் பரிணாமம்",
        events_en=[
            ("1", "Municipal Solid Wastes (Management and Handling) Rules, 2000"),
            ("2", "National Urban Sanitation Policy (NUSP) launched"),
            ("3", "Solid Waste Management Rules, 2016 (superseding 2000 Rules)"),
            ("4", "Nationwide ban on identified single-use plastic items")
        ],
        events_ta=[
            ("1", "நகராட்சி திடக்கழிவுகள் (மேலாண்மை மற்றும் கையாளுதல்) விதிகள், 2000"),
            ("2", "தேசிய நகர்ப்புற சுகாதாரக் கொள்கை (NUSP) தொடங்கப்படுதல்"),
            ("3", "திடக்கழிவு மேலாண்மை விதிகள், 2016 (2000 விதிகளுக்குப் பதிலாக)"),
            ("4", "நாடு தழுவிய அளவில் ஒருமுறை பயன்படுத்தும் பிளாஸ்டிக் பொருட்களுக்கு தடை விதித்தல்")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "3 - 1 - 2 - 4")],
        correct_key="A",
        exp_en="Chronological environmental milestones:\n1. MSW Rules: 2000\n2. NUSP: 2008\n3. Solid Waste Management Rules: April 2016\n4. Single-use plastic ban: July 1, 2022 (in TN, ban was introduced earlier in Jan 2019).\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="சுற்றுச்சூழல் விதிகளின் வரிசை:\n1. MSW விதிகள்: 2000\n2. NUSP கொள்கை: 2008\n3. திடக்கழிவு மேலாண்மை விதிகள்: 2016\n4. ஒருமுறை பயன்படுத்தும் பிளாஸ்டிக் தடை: 2022 (தமிழகத்தில் 2019).\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="2000 Rules -> 2008 NUSP -> 2016 SWM Rules -> 2022 Plastic Ban.",
        tip_ta="2000 விதிகள் -> 2008 கொள்கை -> 2016 புதிய விதிகள் -> 2022 பிளாஸ்டிக் தடை.",
        fact_en="Tamil Nadu pioneered source segregation through Micro Composting Centres (MCCs) in municipalities.",
        fact_ta="நுண் உர மையங்கள் (MCC) மூலம் கழிவுகளை தரம் பிரிப்பதில் தமிழ்நாடு முன்னோடியாக உள்ளது.",
        tags=["solid_waste_management", "environmental_rules", "chronology"]
    ))

    # C20: Union Finance Commissions Grants to ULBs
    questions.append(make_chron_q(
        qid="MUN_C_020",
        subtopic="Finance Commissions Grants",
        topic_label_en="Sequence of Finance Commissions Aiding Local Bodies",
        topic_label_ta="உள்ளாட்சிகளுக்கு நிதி வழங்கிய மத்திய நிதி ஆணையங்களின் வரிசை",
        events_en=[
            ("1", "Eleventh Finance Commission (A.M. Khusro)"),
            ("2", "Twelfth Finance Commission (C. Rangarajan)"),
            ("3", "Thirteenth Finance Commission (Vijay Kelkar)"),
            ("4", "Fourteenth Finance Commission (Y.V. Reddy)")
        ],
        events_ta=[
            ("1", "பதினோராவது நிதி ஆணையம் (ஏ.எம். குஸ்ரோ)"),
            ("2", "பன்னிரண்டாவது நிதி ஆணையம் (சி. ரங்கராஜன்)"),
            ("3", "பதின்மூன்றாவது நிதி ஆணையம் (விஜய் கேல்கர்)"),
            ("4", "பதினான்காவது நிதி ஆணையம் (ஒய்.வி. ரெட்டி)")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "4 - 3 - 2 - 1")],
        correct_key="A",
        exp_en="Sequential sequence of Finance Commissions:\n1. 11th FC (2000-2005): First to recommend specific grants under Article 280(3)(c)\n2. 12th FC (2005-2010)\n3. 13th FC (2010-2015)\n4. 14th FC (2015-2020).\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="மத்திய நிதி ஆணையங்களின் வரிசை:\n1. 11-வது நிதி ஆணையம் (2000-2005)\n2. 12-வது நிதி ஆணையம் (2005-2010)\n3. 13-வது நிதி ஆணையம் (2010-2015)\n4. 14-வது நிதி ஆணையம் (2015-2020).\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="11th (Khusro) -> 12th (Rangarajan) -> 13th (Kelkar) -> 14th (Reddy) -> 15th (N.K. Singh).",
        tip_ta="11-வது -> 12-வது -> 13-வது -> 14-வது -> 15-வது.",
        fact_en="The 11th Finance Commission was the first to give grants following the 73rd and 74th Amendments.",
        fact_ta="73 மற்றும் 74-வது திருத்தங்களுக்குப் பிறகு உள்ளாட்சிகளுக்கு மானியங்களை பரிந்துரைத்த முதல் ஆணையம் 11-வது நிதி ஆணையம் ஆகும்.",
        tags=["finance_commissions", "ulb_grants", "chronology"]
    ))

    # C21: Urban Health Infrastructure Evolution
    questions.append(make_chron_q(
        qid="MUN_C_021",
        subtopic="Urban Health Services",
        topic_label_en="Evolution of Urban Public Health Programs",
        topic_label_ta="நகர்ப்புற பொது சுகாதார திட்டங்களின் பரிணாமம்",
        events_en=[
            ("1", "National Rural Health Mission (NRHM) launched"),
            ("2", "National Urban Health Mission (NUHM) approved by Cabinet"),
            ("3", "Amalgamation of NRHM and NUHM into National Health Mission (NHM)"),
            ("4", "Launch of Ayushman Bharat Urban Health and Wellness Centres (now Arogya Mandirs)")
        ],
        events_ta=[
            ("1", "தேசிய ஊரக சுகாதார இயக்கம் (NRHM) தொடங்கப்படுதல்"),
            ("2", "தேசிய நகர்ப்புற சுகாதார இயக்கத்திற்கு (NUHM) அமைச்சரவை ஒப்புதல் அளித்தல்"),
            ("3", "NRHM மற்றும் NUHM ஆகியவற்றை இணைத்து தேசிய சுகாதார இயக்கம் (NHM) உருவாக்கப்படுதல்"),
            ("4", "ஆயுஷ்மான் பாரத் நகர்ப்புற நல்வாழ்வு மையங்கள் (ஆரோக்கிய மந்திருக்குகள்) தொடங்கப்படுதல்")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "3 - 1 - 2 - 4")],
        correct_key="A",
        exp_en="Chronological urban health milestones:\n1. NRHM: April 2005\n2. NUHM approved: May 2013\n3. NHM overarching framework: 2014\n4. Ayushman Bharat HWCs: 2018.\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="சுகாதாரத் திட்டங்களின் காலவரிசை:\n1. NRHM: ஏப்ரல் 2005\n2. NUHM ஒப்புதல்: மே 2013\n3. NHM ஒருங்கிணைப்பு: 2014\n4. ஆயுஷ்மான் பாரத்: 2018.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="NRHM (2005) -> NUHM (2013) -> NHM (2014) -> Ayushman Bharat (2018).",
        tip_ta="NRHM (2005) -> NUHM (2013) -> NHM (2014) -> ஆயுஷ்மான் பாரத் (2018).",
        fact_en="NUHM focuses specifically on urban poor and slum dwellers through Urban Primary Health Centres (UPHCs).",
        fact_ta="NUHM நகர்ப்புற ஆரம்ப சுகாதார நிலையங்கள் (UPHC) மூலம் நகர்ப்புற ஏழைகளுக்கு சேவை வழங்குகிறது.",
        tags=["urban_health", "nuhm_nhm", "chronology"]
    ))

    # C22: Budgeting and Planning Process in ULBs
    questions.append(make_chron_q(
        qid="MUN_C_022",
        subtopic="Municipal Budget Cycle",
        topic_label_en="Sequential Stages of Municipal Annual Budgeting",
        topic_label_ta="நகராட்சி ஆண்டு நிதிநிலை அறிக்கை தயாரிக்கும் படிகள்",
        events_en=[
            ("1", "Preparation of draft budget estimates by Municipal Commissioner and department heads"),
            ("2", "Scrutiny and modification of draft budget by the Standing Committee on Taxation and Finance"),
            ("3", "Debate, voting, and formal passage of annual budget by the full Municipal Council"),
            ("4", "Submission of passed budget to the State Government and statutory post-expenditure audit")
        ],
        events_ta=[
            ("1", "மாநகராட்சி ஆணையர் மற்றும் துறைத் தலைவர்களால் வரைவு நிதிநிலை அறிக்கை மதிப்பீடுகள் தயாரித்தல்"),
            ("2", "வரிவிதிப்பு மற்றும் நிதி நிலைக்குழுவால் வரைவு வரவு-செலவுத் திட்டம் ஆய்வு செய்யப்பட்டு திருத்தப்படுதல்"),
            ("3", "முழு நகர்மன்றக் கூட்டத்தில் விவாதிக்கப்பட்டு, வாக்கெடுப்பு மூலம் நிதிநிலை அறிக்கை நிறைவேற்றப்படுதல்"),
            ("4", "நிறைவேற்றப்பட்ட நிதிநிலை அறிக்கை மாநில அரசுக்கு சமர்ப்பிக்கப்படுதல் மற்றும் சட்டப்பூர்வ தணிக்கை")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "3 - 1 - 2 - 4")],
        correct_key="A",
        exp_en="Standard municipal budget cycle:\n1. Preparation by Commissioner & accounts wing\n2. Scrutiny by Standing Committee\n3. Approval by full Council\n4. Submission to State & post-audit.\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="நிதிநிலை அறிக்கை நடைமுறை வரிசை:\n1. ஆணையரால் தயாரிப்பு\n2. நிலைக்குழு ஆய்வு\n3. மன்றத்தில் நிறைவேற்றம்\n4. தணிக்கை.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="Preparation -> Committee Scrutiny -> Council Approval -> State Submission & Audit.",
        tip_ta="தயாரிப்பு -> நிலைக்குழு ஆய்வு -> மன்ற ஒப்புதல் -> தணிக்கை.",
        fact_en="Municipal budgets must be passed before March 31 of every financial year.",
        fact_ta="ஒவ்வொரு நிதியாண்டும் மார்ச் 31-க்குள் நகராட்சி நிதிநிலை அறிக்கை நிறைவேற்றப்பட வேண்டும்.",
        tags=["municipal_budget", "financial_cycle", "chronology"]
    ))

    # C23: Evolution of Slum Clearance in Tamil Nadu
    questions.append(make_chron_q(
        qid="MUN_C_023",
        subtopic="TN Slum Policies",
        topic_label_en="Evolution of Slum Housing Policies in TN",
        topic_label_ta="தமிழக குடிசை மாற்று கொள்கைகளின் வரலாறு",
        events_en=[
            ("1", "Enactment of Tamil Nadu Slum Areas (Improvement and Clearance) Act, 1971"),
            ("2", "Establishment of statutory Tamil Nadu Slum Clearance Board (TNSCB)"),
            ("3", "Implementation of Rajiv Awas Yojana (RAY) for slum-free cities"),
            ("4", "Renaming of TNSCB to Tamil Nadu Urban Habitat Development Board (TNUHDB)")
        ],
        events_ta=[
            ("1", "தமிழ்நாடு சேரிப் பகுதிகள் (மேம்பாடு மற்றும் அகற்றுதல்) சட்டம் 1971 இயற்றப்படுதல்"),
            ("2", "சட்டப்பூர்வ தமிழ்நாடு குடிசை மாற்று வாரியம் (TNSCB) அமைக்கப்படுதல்"),
            ("3", "சேரிகளற்ற நகரங்களுக்கான ராஜீவ் ஆவாஸ் யோஜனா (RAY) திட்டம் செயல்படுத்தப்படுதல்"),
            ("4", "குடிசை மாற்று வாரியம் 'தமிழ்நாடு நகர்ப்புற வாழ்விட மேம்பாட்டு வாரியம்' என பெயர் மாற்றம் செய்யப்படுதல்")
        ],
        opt_tuples=[("A", "2 - 1 - 3 - 4"), ("B", "1 - 2 - 3 - 4"), ("C", "2 - 3 - 1 - 4"), ("D", "3 - 1 - 2 - 4")],
        correct_key="A",
        exp_en="Historical sequence:\n1. TNSCB was established by executive order in September 1970 [2]\n2. Followed by statutory Act: Tamil Nadu Slum Areas Act in 1971 [1]\n3. Rajiv Awas Yojana launched: 2011 [3]\n4. Renaming to TNUHDB: September 2021 [4].\nSequence is 2 - 1 - 3 - 4.",
        exp_ta="காலவரிசை:\n1. குடிசை மாற்று வாரியம் தொடக்கம்: செப்டம்பர் 1970 [2]\n2. சேரிப் பகுதிகள் சட்டம்: 1971 [1]\n3. ராஜீவ் ஆவாஸ் யோஜனா: 2011 [3]\n4. TNUHDB பெயர் மாற்றம்: செப்டம்பர் 2021 [4].\nவரிசை 2 - 1 - 3 - 4.",
        tip_en="Board created in 1970 -> Act passed in 1971 -> RAY in 2011 -> Renamed in 2021.",
        tip_ta="வாரியம் 1970 -> சட்டம் 1971 -> RAY 2011 -> பெயர் மாற்றம் 2021.",
        fact_en="TNSCB was established under the visionary leadership of Chief Minister M. Karunanidhi in 1970.",
        fact_ta="முதலமைச்சர் மு. கருணாநிதியால் 1970-ல் குடிசை மாற்று வாரியம் தொடங்கப்பட்டது.",
        tags=["tn_slum_policies", "tnscb_tnuhdb", "chronology"]
    ))

    # C24: Historical Evolution of Madras Local Boards
    questions.append(make_chron_q(
        qid="MUN_C_024",
        subtopic="Madras Local Boards Evolution",
        topic_label_en="Evolution of Local Boards in Madras Presidency",
        topic_label_ta="மெட்ராஸ் மாகாண உள்ளாட்சி வாரியங்களின் பரிணாமம்",
        events_en=[
            ("1", "Madras District Road Cess Act (first statutory local tax in Madras)"),
            ("2", "Madras Local Funds Act (creating Circle Boards)"),
            ("3", "Madras Local Boards Act (establishing Taluk Boards and District Boards)"),
            ("4", "Madras Village Panchayats Act (formal statutory recognition of village panchayats)")
        ],
        events_ta=[
            ("1", "மெட்ராஸ் மாவட்ட சாலை வரிச் சட்டம் (மெட்ராஸின் முதல் உள்ளாட்சி வரி)"),
            ("2", "மெட்ராஸ் உள்ளாட்சி நிதிச் சட்டம் (வட்டார வாரியங்கள் உருவாக்கம்)"),
            ("3", "மெட்ராஸ் உள்ளாட்சி வாரியங்கள் சட்டம் (தாலுகா மற்றும் மாவட்ட வாரியங்கள்)"),
            ("4", "மெட்ராஸ் கிராம பஞ்சாயத்துகள் சட்டம் (கிராம பஞ்சாயத்துகளுக்கு சட்டப்பூர்வ அங்கீகாரம்)")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "3 - 1 - 2 - 4")],
        correct_key="A",
        exp_en="Chronological progression in Madras Presidency:\n1. Madras District Road Cess Act: 1866\n2. Madras Local Funds Act: 1871\n3. Madras Local Boards Act: 1884 (implementing Ripon reforms)\n4. Madras Village Panchayats Act: 1920.\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="மெட்ராஸ் மாகாண வரலாற்று வரிசை:\n1. மாவட்ட சாலை வரிச் சட்டம்: 1866\n2. உள்ளாட்சி நிதிச் சட்டம்: 1871\n3. உள்ளாட்சி வாரியங்கள் சட்டம்: 1884\n4. கிராம பஞ்சாயத்துகள் சட்டம்: 1920.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="Madras Acts: 1866 -> 1871 -> 1884 -> 1920.",
        tip_ta="மெட்ராஸ் சட்டங்கள்: 1866 -> 1871 -> 1884 -> 1920.",
        fact_en="The 1884 Act created a two-tier rural structure: Taluk Boards and District Boards.",
        fact_ta="1884 சட்டம் தாலுகா வாரியம் மற்றும் மாவட்ட வாரியம் என்ற இரு அடுக்கு அமைப்பை உருவாக்கியது.",
        tags=["madras_local_boards", "colonial_history", "chronology"]
    ))

    # C25: DPC Plan Consolidation Lifecycle
    questions.append(make_chron_q(
        qid="MUN_C_025",
        subtopic="DPC Planning Stages",
        topic_label_en="Stages of District Development Plan Formulation",
        topic_label_ta="மாவட்ட வளர்ச்சித் திட்டம் உருவாக்கப்படும் நிலைகள்",
        events_en=[
            ("1", "Individual Panchayats and Municipalities formulate their localized annual development plans"),
            ("2", "District Planning Committee consolidates rural and urban plans under Article 243ZD"),
            ("3", "Assessment of shared resources, spatial planning, and water environmental integration by DPC"),
            ("4", "Chairperson of the DPC forwards the final draft development plan to the State Government")
        ],
        events_ta=[
            ("1", "ஊராட்சிகள் மற்றும் நகராட்சிகள் தங்கள் உள்ளூர் வளர்ச்சித் திட்டங்களைத் தயாரித்தல்"),
            ("2", "மாவட்ட திட்டக் குழு உறுப்பு 243ZD-ன் கீழ் ஊரக மற்றும் நகர்ப்புற திட்டங்களை ஒருங்கிணைத்தல்"),
            ("3", "பகிரப்பட்ட வளங்கள், நீர்நிலைகள் மற்றும் சுற்றுச்சூழல் காரணிகளை DPC ஆய்வு செய்து திருத்துதல்"),
            ("4", "DPC தலைவர் இறுதி வரைவு வளர்ச்சித் திட்டத்தை மாநில அரசுக்கு அனுப்பி வைத்தல்")
        ],
        opt_tuples=[("A", "1 - 2 - 3 - 4"), ("B", "2 - 1 - 3 - 4"), ("C", "1 - 3 - 2 - 4"), ("D", "3 - 1 - 2 - 4")],
        correct_key="A",
        exp_en="Procedural sequence under Article 243ZD:\n1. Preparation of localized plans by PRIs and ULBs\n2. Consolidation into draft district plan\n3. Examination of spatial planning, water resources, and infrastructure\n4. Transmission of final draft to State Government.\nSequence is 1 - 2 - 3 - 4.",
        exp_ta="உறுப்பு 243ZD-ன் கீழ் மாவட்ட திட்டமிடல் வரிசை:\n1. உள்ளாட்சி அமைப்புகள் திட்டம் தயாரித்தல்\n2. DPC ஒருங்கிணைத்தல்\n3. வளங்கள் மற்றும் உள்கட்டமைப்பு ஆய்வு\n4. மாநில அரசுக்கு சமர்ப்பித்தல்.\nவரிசை 1 - 2 - 3 - 4.",
        tip_en="Local plans -> Consolidation -> Environmental resource synthesis -> Forwarding to State Govt.",
        tip_ta="உள்ளூர் திட்டம் -> ஒருங்கிணைப்பு -> வள ஆய்வு -> மாநில அரசுக்கு சமர்ப்பித்தல்.",
        fact_en="Article 243ZD(4) explicitly specifies that the plan goes to the State Government, not the Union.",
        fact_ta="உறுப்பு 243ZD(4) திட்டம் மாநில அரசுக்குத் தான் அனுப்பப்பட வேண்டும் என்று தெளிவாகக் கூறுகிறது.",
        tags=["dpc_lifecycle", "article_243zd", "planning_process", "chronology"]
    ))

    return questions

def main():
    questions = get_chronology_25()
    assert len(questions) == 25, f"Expected 25 questions, got {len(questions)}"
    
    # Balance keys across A, B, C, D
    balanced = balance_question_keys(questions)
    
    out_dir = os.path.join("data", "questions", "polity")
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "municipalities_chronology.json")
    
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(balanced, f, ensure_ascii=False, indent=2)
        
    print(f"[SUCCESS] Wrote {len(balanced)} Chronology MCQs to {out_file}")

if __name__ == "__main__":
    main()
