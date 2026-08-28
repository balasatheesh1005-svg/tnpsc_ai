import json
import os
import sys
import re

sys.stdout.reconfigure(encoding='utf-8')

# Helper function to generate deep, specific bilingual Distractor Analysis & TNPSC Tips for a question
def enrich_question(q):
    qid = q.get('id') or q.get('question_id')
    q_en = (q.get('question_en') or (q.get('question', {}).get('en') if isinstance(q.get('question'), dict) else '') or '').strip()
    q_ta = (q.get('question_ta') or (q.get('question', {}).get('ta') if isinstance(q.get('question'), dict) else '') or '').strip()
    exp_en = (q.get('explanation_en') or (q.get('explanation', {}).get('en') if isinstance(q.get('explanation'), dict) else '') or '').strip()
    exp_ta = (q.get('explanation_ta') or (q.get('explanation', {}).get('ta') if isinstance(q.get('explanation'), dict) else '') or '').strip()
    
    corr_ans = q.get('correct_answer') or 'A'
    opts = q.get('options', [])
    opt_map = {}
    for o in opts:
        if isinstance(o, dict):
            opt_map[o.get('id')] = {
                'en': o.get('en', '').strip(),
                'ta': o.get('ta', '').strip()
            }

    # Extract option texts
    opt_a_en = opt_map.get('A', {}).get('en', '')
    opt_b_en = opt_map.get('B', {}).get('en', '')
    opt_c_en = opt_map.get('C', {}).get('en', '')
    opt_d_en = opt_map.get('D', {}).get('en', '')

    opt_a_ta = opt_map.get('A', {}).get('ta', '')
    opt_b_ta = opt_map.get('B', {}).get('ta', '')
    opt_c_ta = opt_map.get('C', {}).get('ta', '')
    opt_d_ta = opt_map.get('D', {}).get('ta', '')

    q_lower = q_en.lower()
    exp_lower = exp_en.lower()

    # Generate Distractor Analysis for each option A, B, C, D
    wno = {}
    for key in ['A', 'B', 'C', 'D']:
        o_en = opt_map.get(key, {}).get('en', '')
        o_ta = opt_map.get(key, {}).get('ta', '')
        
        if key == corr_ans:
            # Correct Option explanation
            en_desc = f"Correct. {o_en} is the constitutionally correct provision under the Indian Constitution. {exp_en}"
            ta_desc = f"சரி. {o_ta} என்பது இந்திய அரசியலமைப்பின் படி சரியான பிரிவாகும். {exp_ta}"
        else:
            # Incorrect Option distractor analysis - analyze context
            en_desc = ""
            ta_desc = ""
            
            o_lower = o_en.lower()
            
            # Context 1: Article numbers (52, 53, 54, 55, 56, 58, 59, 60, 61, 65, 72, 74, 112, 123, 352, 356, 358, 359, 360)
            if "article" in o_lower or "உறுப்பு" in o_ta or re.search(r'\b\d{2,3}\b', o_lower):
                if "52" in o_lower:
                    en_desc = "Incorrect. Article 52 states that there shall be a President of India (establishes the office)."
                    ta_desc = "தவறு. உறுப்பு 52 இந்தியாவில் ஒரு குடியரசுத் தலைவர் இருப்பார் எனப் பதவியை மட்டுமே உருவாக்குகிறது."
                elif "53" in o_lower:
                    en_desc = "Incorrect. Article 53 vests the executive power of the Union in the President."
                    ta_desc = "தவறு. உறுப்பு 53 ஒன்றியத்தின் நிர்வாக அதிகாரங்களை குடியரசுத் தலைவரிடம் ஒப்படைக்கிறது."
                elif "54" in o_lower:
                    en_desc = "Incorrect. Article 54 defines the Electoral College for the election of the President."
                    ta_desc = "தவறு. உறுப்பு 54 குடியரசுத் தலைவர் தேர்தலுக்கான வாக்காளர் குழுவை (Electoral College) வரையறுக்கிறது."
                elif "55" in o_lower:
                    en_desc = "Incorrect. Article 55 deals with the manner of election of the President (Proportional Representation by STV)."
                    ta_desc = "தவறு. உறுப்பு 55 குடியரசுத் தலைவர் தேர்தல் முறையை (விகிதாச்சார பிரதிநிதித்துவ ஒற்றை மாற்று வாக்கு) விவரிக்கிறது."
                elif "56" in o_lower:
                    en_desc = "Incorrect. Article 56 deals with the term of office of the President (5 years)."
                    ta_desc = "தவறு. உறுப்பு 56 குடியரசுத் தலைவரின் பதவிக் காலத்தைக் (5 ஆண்டுகள்) குறிப்பிடுகிறது."
                elif "58" in o_lower:
                    en_desc = "Incorrect. Article 58 lays down qualifications for election as President."
                    ta_desc = "தவறு. உறுப்பு 58 குடியரசுத் தலைவராவதற்கான தகுதிகளைக் குறிப்பிடுகிறது."
                elif "59" in o_lower:
                    en_desc = "Incorrect. Article 59 specifies conditions of the President's office."
                    ta_desc = "தவறு. உறுப்பு 59 குடியரசுத் தலைவர் அலுவலகத்திற்கான நிபந்தனைகளைக் குறிப்பிடுகிறது."
                elif "60" in o_lower:
                    en_desc = "Incorrect. Article 60 prescribes the oath or affirmation by the President."
                    ta_desc = "தவறு. உறுப்பு 60 குடியரசுத் தலைவரின் பதவிப் பிரமாணத்தைக் குறிப்பிடுகிறது."
                elif "61" in o_lower:
                    en_desc = "Incorrect. Article 61 details the procedure for impeachment of the President."
                    ta_desc = "தவறு. உறுப்பு 61 குடியரசுத் தலைவரைப் பதவி நீக்கம் செய்யும் (Impeachment) நடைமுறையைக் குறிப்பிடுகிறது."
                elif "65" in o_lower:
                    en_desc = "Incorrect. Article 65 specifies the Vice-President acting as President during vacancy."
                    ta_desc = "தவறு. உறுப்பு 65 காலியிடங்களின் போது துணைக் குடியரசுத் தலைவர் செயல் குடியரசுத் தலைவராகச் செயல்படுவதைக் குறிப்பிடுகிறது."
                elif "72" in o_lower:
                    en_desc = "Incorrect. Article 72 empowers the President to grant pardons, reprieves, respites, and remissions."
                    ta_desc = "தவறு. உறுப்பு 72 குடியரசுத் தலைவரின் மன்னிப்பளிக்கும் அதிகாரத்தைக் (Pardoning Power) குறிப்பிடுகிறது."
                elif "74" in o_lower:
                    en_desc = "Incorrect. Article 74 mandates a Council of Ministers headed by the PM to aid and advise the President."
                    ta_desc = "தவறு. உறுப்பு 74 குடியரசுத் தலைவருக்கு உதவவும் ஆலோசிக்கவும் பிரதமரைத் தலைவராகக் கொண்ட அமைச்சரவையைக் குறிப்பிடுகிறது."
                elif "112" in o_lower:
                    en_desc = "Incorrect. Article 112 deals with the Annual Financial Statement (Budget)."
                    ta_desc = "தவறு. உறுப்பு 112 வருடாந்திர நிதிநிலை அறிக்கையைக் (பட்ஜெட்) குறிப்பிடுகிறது."
                elif "123" in o_lower:
                    en_desc = "Incorrect. Article 123 empowers the President to promulgate Ordinances during recess of Parliament."
                    ta_desc = "தவறு. உறுப்பு 123 நாடாளுமன்றக் கூட்டத்தொடர் இல்லாதபோது அவசரச் சட்டம் (Ordinance) பிறப்பிக்கும் அதிகாரத்தைக் குறிப்பிடுகிறது."
                elif "352" in o_lower:
                    en_desc = "Incorrect. Article 352 relates to National Emergency (War, External Aggression, Armed Rebellion)."
                    ta_desc = "தவறு. உறுப்பு 352 தேசிய அவசரநிலையைக் (போர், வெளிநாட்டுக் ஆக்கிரமிப்பு, ஆயுதமேந்திய கலகம்) குறிப்பிடுகிறது."
                elif "356" in o_lower:
                    en_desc = "Incorrect. Article 356 relates to President's Rule (State Emergency) due to failure of constitutional machinery."
                    ta_desc = "தவறு. உறுப்பு 356 மாநிலத்தில் அரசியலமைப்பு இயந்திரம் செயலிழக்கும் போது குடியரசுத் தலைவர் ஆட்சியைப் பிரகடனம் செய்வதைக் குறிப்பிடுகிறது."
                elif "360" in o_lower:
                    en_desc = "Incorrect. Article 360 relates to Financial Emergency."
                    ta_desc = "தவறு. உறுப்பு 360 நிதி அவசரநிலையைக் குறிப்பிடுகிறது."
                else:
                    en_desc = f"Incorrect. Option {key} ({o_en}) references a different constitutional provision."
                    ta_desc = f"தவறு. தெரிவு {key} ({o_ta}) வேறு அரசியலமைப்பு விதியைக் குறிக்கிறது."
            
            # Context 2: Electoral College & Membership (Nominated, Legislative Council, Vice-President, etc.)
            elif "nominated" in o_lower:
                en_desc = "Incorrect. Nominated members of Parliament do NOT vote in the Presidential election (Electoral College under Art 54), though they participate in impeachment."
                ta_desc = "தவறு. நாடாளுமன்ற நியமன உறுப்பினர்கள் குடியரசுத் தலைவர் தேர்தலில் வாக்களிக்க முடியாது (உறுப்பு 54), ஆனால் பதவி நீக்கத்தில் பங்கேற்பர்."
            elif "legislative council" in o_lower or "mlc" in o_lower:
                en_desc = "Incorrect. Members of State Legislative Councils (MLCs) are completely excluded from the Presidential Electoral College."
                ta_desc = "தவறு. மாநில மேலவை உறுப்பினர்கள் (MLCs) குடியரசுத் தலைவர் தேர்தலில் வாக்களிக்கும் உரிமையற்றவர்கள்."
            elif "vice-president" in o_lower or "governor" in o_lower or "prime minister" in o_lower:
                en_desc = f"Incorrect. This confuses the President's constitutional role with that of the {o_en}."
                ta_desc = f"தவறு. இது குடியரசுத் தலைவரின் அரசியலமைப்புப் பொறுப்பை {o_ta}-ன் பொறுப்புடன் குழப்புகிறது."

            # Context 3: Veto types (Absolute, Suspensive, Pocket, Qualified)
            elif "qualified veto" in o_lower:
                en_desc = "Incorrect. Qualified veto is possessed by the US President (overridden by 2/3rd majority); the Indian President does NOT possess qualified veto."
                ta_desc = "தவறு. தகுதிவாய்ந்த வீட்டோ (Qualified Veto) அமெரிக்க குடியரசுத் தலைவரிடம் மட்டுமே உள்ளது; இந்திய குடியரசுத் தலைவருக்கு இந்த அதிகாரம் இல்லை."
            elif "suspensive veto" in o_lower:
                en_desc = "Incorrect. Suspensive veto can be overridden by a simple majority upon returning the bill, but CANNOT be exercised over Money Bills or Constitutional Amendment Bills."
                ta_desc = "தவறு. இடைநிறுத்த வீட்டோவை நாடாளுமன்றம் சாதாரண பெரும்பான்மையுடன் மீண்டும் நிறைவேற்றலாம்; ஆனால் நிதி மசோதா மற்றும் அரசியலமைப்பு திருத்த மசோதாக்களுக்கு இதைப் பயன்படுத்த முடியாது."
            elif "absolute veto" in o_lower:
                en_desc = "Incorrect. Absolute veto means withholding assent so the bill dies. Exercised only for Private Members' Bills or when Cabinet resigns."
                ta_desc = "தவறு. முற்றுரிமை வீட்டோ என்பது மசோதாவுக்கு ஒப்புதல் அளிக்காமல் நிராகரிப்பதாகும். இது தனிநபர் மசோதாக்கள் அல்லது அமைச்சரவை ராஜினாமா செய்யும் போது மட்டுமே பயன்படுத்தப்படும்."
            elif "pocket veto" in o_lower:
                en_desc = "Incorrect. Pocket veto means keeping the bill pending indefinitely without taking action. Exercised by Giani Zail Singh in 1986."
                ta_desc = "தவறு. பாக்கெட் வீட்டோ என்பது மசோதா மீது எந்த நடவடிக்கையும் எடுக்காமல் காலவரையின்றி நிலுவையில் வைப்பதாகும் (1986-ல் கியானி ஜெயில் சிங் பயன்படுத்தினார்)."

            # Context 4: Pardoning Power terms (Pardon, Reprieve, Respite, Remission, Commutation)
            elif "pardon" in o_lower and "respite" not in o_lower and "remission" not in o_lower:
                en_desc = "Incorrect. Pardon completely absolves the offender from all sentences, punishments, and disqualifications."
                ta_desc = "தவறு. மன்னிப்பு (Pardon) என்பது குற்றவாளியின் அனைத்து தண்டனைகள் மற்றும் தகுதியின்மைகளையும் முழுமையாக நீக்குகிறது."
            elif "commutation" in o_lower:
                en_desc = "Incorrect. Commutation means substituting a lighter form of punishment for a harsher one (e.g. death sentence to life imprisonment)."
                ta_desc = "தவறு. உருமாற்றம் (Commutation) என்பது ஒரு தண்டனையை லேசான தண்டனையாக மாற்றுவதாகும் (எ.கா. மரண தண்டனையை ஆயுள் தண்டனையாக மாற்றுவது)."
            elif "remission" in o_lower:
                en_desc = "Incorrect. Remission means reducing the period of sentence without changing its character (e.g. 2 years rigorous to 1 year rigorous)."
                ta_desc = "தவறு. தண்டனைக் குறைப்பு (Remission) என்பது தண்டனையின் தன்மையை மாற்றாமல் அதன் காலத்தைக் குறைப்பதாகும்."
            elif "respite" in o_lower:
                en_desc = "Incorrect. Respite means awarding a lesser sentence in place of one originally awarded due to special facts like pregnancy or disability."
                ta_desc = "தவறு. நிவாரணம் (Respite) என்பது கர்ப்பம் அல்லது உடல் ஊனம் போன்ற சிறப்பு காரணங்களுக்காகக் குறைந்த தண்டனை அளிப்பதாகும்."
            elif "reprieve" in o_lower:
                en_desc = "Incorrect. Reprieve means a temporary stay of execution of a sentence, especially a death sentence."
                ta_desc = "தவறு. தற்காலிகத் தடை (Reprieve) என்பது தண்டனையை (குறிப்பாக மரண தண்டனையை) தற்காலிகமாக நிறுத்தி வைப்பதாகும்."

            # Fallback if no specialized pattern triggered
            if not en_desc:
                en_desc = f"Incorrect. Option {key} ({o_en}) is not supported by the constitutional facts under Article reference or President Notes."
                ta_desc = f"தவறு. தெரிவு {key} ({o_ta}) அரசியலமைப்பு விதிகள் அல்லது குடியரசுத் தலைவர் குறிப்புகளின் படி தவறான கூற்றாகும்."

            wno[key] = {
                "en": en_desc,
                "ta": ta_desc
            }

        # Put correct option in wno dictionary
        if key == corr_ans:
            wno[key] = {
                "en": f"Correct. {o_en} is the accurate constitutional answer. {exp_en}",
                "ta": f"சரி. {o_ta} என்பது சரியான அரசியலமைப்பு பதிலாகும். {exp_ta}"
            }

    # Generate Question-Specific TNPSC Tip
    tip_en = ""
    tip_ta = ""

    if "article 54" in q_lower or "electoral college" in q_lower:
        tip_en = "TNPSC Exam Tip: Always remember that ONLY ELECTED members (MPs of both Houses + State MLAs + UT MLAs of Delhi, Puducherry & J&K) vote in Presidential elections. Nominated MPs and State MLCs are strictly EXCLUDED."
        tip_ta = "TNPSC தேர்வு குறிப்பு: குடியரசுத் தலைவர் தேர்தலில் தேர்ந்தெடுக்கப்பட்ட உறுப்பினர்கள் (MPs, MLAs) மட்டுமே வாக்களிக்க முடியும். நியமன உறுப்பினர்கள் மற்றும் மாநில மேலவை உறுப்பினர்கள் (MLCs) வாக்களிக்க முடியாது என்பதை நினைவில் கொள்க."
    elif "article 61" in q_lower or "impeachment" in q_lower:
        tip_en = "TNPSC Exam Tip: For Presidential impeachment (Art 61), the resolution must be passed by 2/3rd majority of the TOTAL MEMBERSHIP of each House. Nominated MPs CAN vote in impeachment, but State MLAs CANNOT."
        tip_ta = "TNPSC தேர்வு குறிப்பு: குடியரசுத் தலைவர் பதவி நீக்கத்தில் (உறுப்பு 61) ஒவ்வொரு அவையின் மொத்த உறுப்பினர்களில் 2/3 பங்கு பெரும்பான்மை தேவை. நியமன எம்பிக்கள் வாக்களிக்கலாம், ஆனால் மாநில எல்.எல்.ஏக்கள் வாக்களிக்க முடியாது."
    elif "article 72" in q_lower or "pardon" in q_lower:
        tip_en = "TNPSC Exam Tip: Only the President (Article 72) can pardon a Death Sentence and Court Martial punishments. State Governors (Article 161) cannot pardon death sentences (they can only commute/remit/respite/suspend)."
        tip_ta = "TNPSC தேர்வு குறிப்பு: மரண தண்டனை மற்றும் இராணுவ நீதிமன்றத் தண்டனைகளை குடியரசுத் தலைவர் (உறுப்பு 72) மட்டுமே மன்னிக்க முடியும். ஆளுநரால் (உறுப்பு 161) மரண தண்டனையை மன்னிக்க முடியாது (குறைக்க/நிறுத்த மட்டுமே முடியும்)."
    elif "article 123" in q_lower or "ordinance" in q_lower:
        tip_en = "TNPSC Exam Tip: An Ordinance under Article 123 is a temporary law promulgated during recess of Parliament. Its maximum duration is 6 months and 6 weeks (42 days from reassembly of Parliament)."
        tip_ta = "TNPSC தேர்வு குறிப்பு: அவசரச் சட்டம் (உறுப்பு 123) என்பது நாடாளுமன்றக் கூட்டம் இல்லாத போது பிறப்பிக்கப்படும் தற்காலிகச் சட்டமாகும். இதன் அதிகபட்ச காலம் 6 மாதங்கள் மற்றும் 6 வாரங்கள் (கூட்டம் கூடியதிலிருந்து 42 நாட்கள்) ஆகும்."
    elif "veto" in q_lower or "assent" in q_lower:
        tip_en = "TNPSC Exam Tip: The President CANNOT return or exercise Veto power over a Constitutional Amendment Bill (24th CAA 1971 made assent mandatory). Also, Suspensive Veto cannot be exercised over Money Bills."
        tip_ta = "TNPSC தேர்வு குறிப்பு: அரசியலமைப்பு திருத்த மசோதாவிற்கு குடியரசுத் தலைவர் கட்டாயம் ஒப்புதல் அளிக்க வேண்டும் (24-வது திருத்தம் 1971). மேலும், நிதி மசோதாவிற்கு இடைநிறுத்த வீட்டோவைப் பயன்படுத்த முடியாது."
    elif "article 352" in q_lower or "article 356" in q_lower or "article 360" in q_lower or "emergency" in q_lower:
        tip_en = "TNPSC Exam Tip: Remember approval timelines: National Emergency (Art 352) = 1 month by 2/3rd special majority; President's Rule (Art 356) = 2 months by simple majority (max 3 years); Financial Emergency (Art 360) = 2 months by simple majority (no max limit)."
        tip_ta = "TNPSC தேர்வு குறிப்பு: அவசரநிலை ஒப்புதல் காலங்கள்: தேசிய அவசரநிலை (352) = 1 மாதம் (சிறப்பு பெரும்பான்மை); குடியரசுத் தலைவர் ஆட்சி (356) = 2 மாதங்கள் (சாதாரண பெரும்பான்மை, அதிகபட்சம் 3 ஆண்டுகள்); நிதி அவசரநிலை (360) = 2 மாதங்கள் (காலவரம்பில்லை)."
    elif "article 358" in q_lower or "article 359" in q_lower:
        tip_en = "TNPSC Exam Tip: Article 358 automatically suspends Article 19 ONLY during External Emergency (War/External Aggression). Article 359 suspends enforcement of specified FRs, but Articles 20 and 21 CAN NEVER BE SUSPENDED (44th CAA 1978)."
        tip_ta = "TNPSC தேர்வு குறிப்பு: உறுப்பு 358 வெளிநாட்டுக் ஆக்கிரமிப்பின் போது மட்டுமே உறுப்பு 19-ஐத் தற்காலிகமாக நிறுத்தும். உறுப்பு 359-ன் கீழ் பிற உரிமைகளை நிறுத்தினாலும், உறுப்புகள் 20 மற்றும் 21-ஐ ஒருபோதும் நிறுத்த முடியாது (44-வது திருத்தம் 1978)."
    elif "article 74" in q_lower or "advice" in q_lower:
        tip_en = "TNPSC Exam Tip: The 42nd CAA 1976 made Cabinet advice binding on the President. The 44th CAA 1978 gave the President power to send advice back ONCE for reconsideration, but after reconsideration the advice is strictly binding."
        tip_ta = "TNPSC தேர்வு குறிப்பு: 42-வது திருத்தம் 1976 அமைச்சரவை ஆலோசனையைக் குடியரசுத் தலைவருக்குக் கட்டாயமாக்கியது. 44-வது திருத்தம் 1978 ஒருமுறை மறுபரிசீலனைக்கு அனுப்ப அனுமதி அளித்தது; ஆனால் மறுபரிசீலனைக்குப் பின் ஆலோசனை கட்டாயமாகும்."
    elif "article 58" in q_lower or "qualification" in q_lower or "age" in q_lower:
        tip_en = "TNPSC Exam Tip: Minimum age for President is 35 years (same for VP and Governor). Must be qualified for Lok Sabha election (whereas Vice-President must be qualified for Rajya Sabha election)."
        tip_ta = "TNPSC தேர்வு குறிப்பு: குடியரசுத் தலைவருக்கான குறைந்தபட்ச வயது 35 ஆண்டுகள். அவர் மக்களவை (Lok Sabha) உறுப்பினராவதற்கான தகுதி பெற்றிருக்க வேண்டும் (துணைக் குடியரசுத் தலைவர் மாநிலங்களவை தகுதி பெற்றிருக்க வேண்டும்)."
    else:
        tip_en = f"TNPSC Exam Tip: Focus on the specific constitutional Article and provisions governing '{q.get('topic', 'President')}'. Pay attention to exceptions and precise constitutional terminology for Group 1 preliminary questions."
        tip_ta = f"TNPSC தேர்வு குறிப்பு: '{q.get('topic', 'குடியரசுத் தலைவர்')}' தொடர்பான குறிப்பிட்ட அரசியலமைப்பு விதிகள் மற்றும் விதிவிலக்குகளை கவனமாகப் படித்து நினைவில் கொள்க."

    # Update question fields
    q['why_not_others'] = wno
    q['tnpsc_tip'] = {
        "en": tip_en,
        "ta": tip_ta
    }
    q['trap_point'] = {
        "en": tip_en,
        "ta": tip_ta
    }
    
    return q
