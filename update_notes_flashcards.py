# -*- coding: utf-8 -*-
import json
import os

def update_jrap_notes():
    # Part 1
    p1 = 'data/notes/polity/judicial_review_activism_pil_part_1.json'
    with open(p1, 'r', encoding='utf-8') as f:
        d1 = json.load(f)
    d1['content']['mind_map'] = d1['content'].get('mind_map_p1', {})
    d1['content']['revision_cards'] = [
        {
            'id': 'jrap_p1_c1',
            'front_en': 'What is the constitutional meaning and scope of Judicial Review in India?',
            'front_ta': 'இந்தியாவில் நீதித்துறை மறுஆய்வின் அரசியலமைப்புப் பொருள் மற்றும் வரம்பு யாது?',
            'back_en': 'The power of Supreme Court and High Courts to examine the constitutional validity of legislative acts and executive orders, and strike them down if they violate the Constitution or Basic Structure.',
            'back_ta': 'சட்டமன்றச் சட்டங்கள் மற்றும் நிர்வாக உத்தரவுகளின் அரசியலமைப்புச் செல்லுபடியாகும் தன்மையை ஆராய்ந்து, அரசியலமைப்பு அல்லது அடிப்படைக் கட்டமைப்பை மீறினால் அவற்றைச் செல்லாததாக்கும் உச்ச மற்றும் உயர் நீதிமன்றங்களின் அதிகாரம்.'
        },
        {
            'id': 'jrap_p1_c2',
            'front_en': 'How does Article 13 act as the constitutional bedrock of Judicial Review?',
            'front_ta': 'உறுப்பு 13 எவ்வாறு நீதித்துறை மறுஆய்வின் அரசியலமைப்பு அடித்தளமாகச் செயல்படுகிறது?',
            'back_en': 'Article 13(2) expressly bars the State from making any law taking away or abridging Fundamental Rights; any law made in contravention is void ab initio.',
            'back_ta': 'உறுப்பு 13(2) அடிப்படை உரிமைகளைப் பறிக்கும் அல்லது குறைக்கும் எந்தவொரு சட்டத்தையும் அரசு இயற்றக்கூடாது என வெளிப்படையாகத் தடுக்கிறது; மீறி இயற்றப்படும் சட்டம் தொடக்கத்திலிருந்தே செல்லாது.'
        },
        {
            'id': 'jrap_p1_c3',
            'front_en': 'Compare the writ jurisdiction of Article 32 (SC) and Article 226 (HC).',
            'front_ta': 'உறுப்பு 32 (SC) மற்றும் உறுப்பு 226 (HC) ஆகியவற்றின் நீதிப்பேராணை வரம்பை ஒப்பிடுக.',
            'back_en': 'Article 32 is limited ONLY to enforcement of Fundamental Rights and is itself a FR; Article 226 covers Fundamental Rights AND "for any other purpose" (wider jurisdiction).',
            'back_ta': 'உறுப்பு 32 அடிப்படை உரிமைகளை அமல்படுத்துவதற்கு மட்டுமே பொருந்தும் மற்றும் தானே ஓர் அடிப்படை உரிமை; உறுப்பு 226 அடிப்படை உரிமைகள் மற்றும் "வேறு எந்த நோக்கத்திற்கும்" பொருந்தும் (பரந்த அதிகார வரம்பு).'
        },
        {
            'id': 'jrap_p1_c4',
            'front_en': 'Which landmark case propounded the Basic Structure Doctrine?',
            'front_ta': 'அடிப்படைக் கட்டமைப்புக் கோட்பாட்டை முன்வைத்த வரலாற்றுச் சிறப்புமிக்க வழக்கு எது?',
            'back_en': 'Kesavananda Bharati v. State of Kerala (1973) held that Parliament can amend any part of the Constitution under Art. 368 but cannot alter or destroy its Basic Structure.',
            'back_ta': 'கேசவாநந்த பாரதி v. கேரள மாநிலம் (1973) வழக்கில் நாடாளுமன்றம் உறுப்பு 368 கீழ் எதனையும் திருத்தலாம், ஆனால் அரசியலமைப்பின் அடிப்படைக் கட்டமைப்பை மாற்றவோ அழிக்கவோ முடியாது எனத் தீர்ப்பளிக்கப்பட்டது.'
        },
        {
            'id': 'jrap_p1_c5',
            'front_en': 'What did the Supreme Court hold regarding the Ninth Schedule in the I.R. Coelho Case (2007)?',
            'front_ta': 'I.R. கோயல்ஹோ வழக்கில் (2007) ஒன்பதாவது அட்டவணை குறித்து உச்ச நீதிமன்றம் என்ன தீர்ப்பளித்தது?',
            'back_en': 'Laws placed in the Ninth Schedule on or after 24 April 1973 are open to challenge and judicial review if they damage or destroy the Basic Structure (Articles 14, 19, 21).',
            'back_ta': '24 ஏப்ரல் 1973 அன்றோ அல்லது அதற்குப் பின்னரோ 9வது அட்டவணையில் சேர்க்கப்பட்ட சட்டங்கள் அடிப்படைக் கட்டமைப்பை (உறுப்புகள் 14, 19, 21) மீறினால் நீதித்துறை மறுஆய்வுக்கு உட்பட்டவை.'
        }
    ]
    with open(p1, 'w', encoding='utf-8') as f:
        json.dump(d1, f, indent=2, ensure_ascii=False)

    # Part 2
    p2 = 'data/notes/polity/judicial_review_activism_pil_part_2.json'
    with open(p2, 'r', encoding='utf-8') as f:
        d2 = json.load(f)
    d2['content']['mind_map'] = d2['content'].get('mind_map_p2', {})
    d2['content']['revision_cards'] = [
        {
            'id': 'jrap_p2_c1',
            'front_en': 'What is the core distinction between Judicial Activism and Judicial Overreach?',
            'front_ta': 'நீதித்துறை செயல்பாடு மற்றும் நீதித்துறை மிதமிஞ்சிய செயல்பாடு ஆகியவற்றிற்கு இடையேயான முக்கிய வேறுபாடு யாது?',
            'back_en': 'Judicial Activism proactively protects fundamental rights when executive/legislature fails; Judicial Overreach arbitrarily invades legislative/policy domains, violating separation of powers.',
            'back_ta': 'நீதித்துறை செயல்பாடு நிர்வாகம்/சட்டமன்றம் தவறும்போது உரிமைகளைப் பாதுகாக்கிறது; நீதித்துறை மிதமிஞ்சிய செயல்பாடு சட்டமன்ற/கொள்கை எல்லைகளைத் தன்னிச்சையாக ஆக்கிரமித்து அதிகாரப் பகிர்வை மீறுகிறது.'
        },
        {
            'id': 'jrap_p2_c2',
            'front_en': 'How did the Maneka Gandhi Case (1978) transform Article 21?',
            'front_ta': 'மேனகா காந்தி வழக்கு (1978) எவ்வாறு உறுப்பு 21-ஐ உருமாற்றியது?',
            'back_en': 'It replaced rigid "procedure established by law" with substantive "due process of law" (fair, just, and reasonable), massively expanding Article 21 rights.',
            'back_ta': 'இது "சட்டத்தால் உருவாக்கப்பட்ட நடைமுறை" என்பதை நியாயமான, நேர்மையான "சட்டத்தின் உரிய நடைமுறை" (Due Process) ஆக மாற்றி உறுப்பு 21 உரிமைகளை விரிவுபடுத்தியது.'
        },
        {
            'id': 'jrap_p2_c3',
            'front_en': 'What is the innovative procedural tool "Continuing Mandamus"?',
            'front_ta': '"தொடர் கட்டளையிடும் ஆணை" (Continuing Mandamus) என்ற புதுமையான நீதித்துறை உத்தி யாது?',
            'back_en': 'A series of ongoing judicial orders where the court retains jurisdiction to continuously monitor executive progress in complex public interest matters.',
            'back_ta': 'சிக்கலான பொது நல விவகாரங்களில் நிர்வாகத்தின் முன்னேற்றத்தைத் தொடர்ந்து கண்காணிக்க நீதிமன்றம் தனது அதிகார வரம்பைத் தக்கவைத்துக் கொள்ளும் தொடர் உத்தரவுகள்.'
        },
        {
            'id': 'jrap_p2_c4',
            'front_en': 'Which constitutional amendment established the NJAC and what was its judicial fate?',
            'front_ta': 'தேசிய நீதித்துறை நியமன ஆணையத்தை (NJAC) நிறுவிய அரசியலமைப்புத் திருத்தம் எது மற்றும் அதன் நீதித்துறை முடிவு என்ன?',
            'back_en': 'The 99th Constitutional Amendment Act (2014) established NJAC, which was struck down as unconstitutional by Supreme Court in 2015 for violating judicial independence.',
            'back_ta': '99வது அரசியலமைப்புத் திருத்தச் சட்டம் (2014) NJAC-ஐ நிறுவியது; நீதித்துறையின் சுதந்திரத்தை மீறியதற்காக 2015-ல் உச்ச நீதிமன்றத்தால் அது செல்லாது என ரத்து செய்யப்பட்டது.'
        },
        {
            'id': 'jrap_p2_c5',
            'front_en': 'Which judges pioneered Judicial Activism in the Indian Supreme Court?',
            'front_ta': 'இந்திய உச்ச நீதிமன்றத்தில் நீதித்துறை செயல்பாட்டை முன்னோடியாகத் தொடங்கிய நீதிபதிகள் யார்?',
            'back_en': 'Justice V.R. Krishna Iyer and Justice P.N. Bhagwati during the late 1970s and early 1980s.',
            'back_ta': '1970களின் பிற்பகுதியிலும் 1980களின் முற்பகுதியிலும் நீதிபதி வி.ஆர். கிருஷ்ண ஐயர் மற்றும் நீதிபதி பி.என். பகவதி ஆகியோர்.'
        }
    ]
    with open(p2, 'w', encoding='utf-8') as f:
        json.dump(d2, f, indent=2, ensure_ascii=False)

    # Part 3
    p3 = 'data/notes/polity/judicial_review_activism_pil_part_3.json'
    with open(p3, 'r', encoding='utf-8') as f:
        d3 = json.load(f)
    d3['content']['mind_map'] = d3['content'].get('master_mind_map_p3', {})
    d3['content']['revision_cards'] = [
        {
            'id': 'jrap_p3_c1',
            'front_en': 'What traditional legal requirement does Public Interest Litigation (PIL) relax?',
            'front_ta': 'பொது நல வழக்கு (PIL) எந்த பாரம்பரிய சட்டக் கட்டுப்பாட்டைத் தளர்த்துகிறது?',
            'back_en': 'Locus Standi (standing to sue); any public-spirited citizen or organisation can file a PIL on behalf of disadvantaged persons who cannot access courts.',
            'back_ta': 'வழக்குத் தொடுக்கும் தகுதி (Locus Standi); நீதிமன்றங்களை அணுக முடியாத ஒடுக்கப்பட்டோருக்காக எந்தவொரு பொதுநலன் கொண்ட குடிமகனும் அல்லது அமைப்பும் வழக்குத் தொடரலாம்.'
        },
        {
            'id': 'jrap_p3_c2',
            'front_en': 'What is "Epistolary Jurisdiction" in PIL jurisprudence?',
            'front_ta': 'பொது நல வழக்குகளில் "கடித அதிகார வரம்பு" (Epistolary Jurisdiction) என்றால் என்ன?',
            'back_en': 'The power of Supreme Court and High Courts to treat simple letters, postcards, or telegrams highlighting gross rights violations as formal writ petitions.',
            'back_ta': 'உரிமை மீறல்களைக் குறிப்பிடும் எளிய கடிதங்கள், அஞ்சல் அட்டைகள் அல்லது தந்திகளை முறையான நீதிப்பேராணை மனுக்களாக ஏற்கும் உச்ச மற்றும் உயர் நீதிமன்றங்களின் அதிகாரம்.'
        },
        {
            'id': 'jrap_p3_c3',
            'front_en': 'Which case is recognized as India\'s first reported PIL?',
            'front_ta': 'இந்தியாவின் முதல் பொது நல வழக்காக அங்கீகரிக்கப்பட்ட வழக்கு எது?',
            'back_en': 'Hussainara Khatoon v. Home Secretary, State of Bihar (1979), highlighting the plight of undertrial prisoners and establishing the right to speedy trial.',
            'back_ta': 'ஹுசைனாரா காதுன் v. உள்துறைச் செயலாளர், பீகார் மாநிலம் (1979); விசாரணைக் கைதிகளின் அவல நிலையை வெளிப்படுத்தி விரைவான விசாரணை உரிமையை நிறுவியது.'
        },
        {
            'id': 'jrap_p3_c4',
            'front_en': 'Which landmark case laid down mandatory guidelines on sexual harassment at workplace?',
            'front_ta': 'பணியிடத்தில் பாலியல் துன்புறுத்தலைத் தடுக்க கட்டாய வழிகாட்டுதல்களை வகுத்த வரலாற்றுச் சிறப்புமிக்க வழக்கு எது?',
            'back_en': 'Vishaka v. State of Rajasthan (1997), filling legislative vacuum under Art. 141 until POSH Act 2013 was enacted.',
            'back_ta': 'விசாகா v. ராஜஸ்தான் மாநிலம் (1997); 2013 POSH சட்டம் இயற்றப்படும் வரை உறுப்பு 141-ன் கீழ் சட்ட வெற்றிடத்தை நிரப்பியது.'
        },
        {
            'id': 'jrap_p3_c5',
            'front_en': 'What guidelines did the Supreme Court lay down in Balwant Singh Chaufal (2010)?',
            'front_ta': 'பல்வந்த் சிங் சௌபால் (2010) வழக்கில் உச்ச நீதிமன்றம் என்ன வழிகாட்டுதல்களை வகுத்தது?',
            'back_en': 'Strict 8-point guidelines to weed out frivolous, politically motivated, or extortionist PILs, preserving PIL for genuinely disadvantaged groups.',
            'back_ta': 'போலியான, அரசியல் உள்நோக்கம் கொண்ட அல்லது மிரட்டிப் பணம் பறிக்கும் பொது நல வழக்குகளை களையவும், உண்மையான எளிய மக்களுக்கு PIL-ஐப் பாதுகாக்கவும் 8 அம்ச வழிகாட்டுதல்கள்.'
        }
    ]
    with open(p3, 'w', encoding='utf-8') as f:
        json.dump(d3, f, indent=2, ensure_ascii=False)
    print('Updated JRAP notes with flashcards and mind_map successfully.')


def update_pc_notes():
    # Part 1
    p1 = 'data/notes/polity/parliamentary_committees_part_1.json'
    with open(p1, 'r', encoding='utf-8') as f:
        d1 = json.load(f)
    d1['content']['revision_cards'] = [
        {
            'id': 'pc_p1_c1',
            'front_en': 'What are the two constitutional provisions related to Parliamentary Committees?',
            'front_ta': 'நாடாளுமன்றக் குழுக்கள் தொடர்பான இரண்டு அரசியலமைப்பு விதிகள் யாவை?',
            'back_en': 'Article 105(3) deals with powers and privileges of committees, and Article 118(1) empowers each House to make rules for regulating its procedure and conduct of business including committees.',
            'back_ta': 'உறுப்பு 105(3) குழுக்களின் அதிகாரங்கள் மற்றும் சிறப்புரிமைகள் பற்றியது; உறுப்பு 118(1) குழுக்கள் உட்பட நடைமுறைகளை ஒழுங்குபடுத்த விதிகளை உருவாக்க அவைகளுக்கு அதிகாரம் அளிக்கிறது.'
        },
        {
            'id': 'pc_p1_c2',
            'front_en': 'What is the composition and chairmanship convention of Public Accounts Committee (PAC)?',
            'front_ta': 'பொதுக் கணக்குக் குழுவின் (PAC) அமைப்பு மற்றும் தலைவர் பதவி மரபு யாது?',
            'back_en': '22 members (15 Lok Sabha + 7 Rajya Sabha), elected annually by proportional representation (STV). Since 1967, the Chairperson is appointed by the Speaker from the Opposition in Lok Sabha.',
            'back_ta': '22 உறுப்பினர்கள் (15 மக்களவை + 7 மாநிலங்களவை), ஒற்றை மாற்று வாக்கு விகிதாசார பிரதிநிதித்துவ முறைப்படி தேர்ந்தெடுக்கப்படுகின்றனர். 1967 முதல் மரபுப்படி மக்களவையின் எதிர்க்கட்சியிலிருந்தே சபாநாயகரால் தலைவர் நியமிக்கப்படுகிறார்.'
        },
        {
            'id': 'pc_p1_c3',
            'front_en': 'What is unique about the composition of the Estimates Committee?',
            'front_ta': 'மதிப்பீட்டுக் குழுவின் அமைப்பில் உள்ள தனித்துவமான அம்சம் என்ன?',
            'back_en': 'It has 30 members, ALL elected exclusively from Lok Sabha. Rajya Sabha has NO representation in the Estimates Committee.',
            'back_ta': 'இதில் 30 உறுப்பினர்கள் உள்ளனர், அனைவரும் மக்களவையிலிருந்து மட்டுமே தேர்ந்தெடுக்கப்படுகின்றனர். மதிப்பீட்டுக் குழுவில் மாநிலங்களவைக்கு பிரதிநிதித்துவம் இல்லை.'
        },
        {
            'id': 'pc_p1_c4',
            'front_en': 'When was the Committee on Public Undertakings (COPU) created and on whose recommendation?',
            'front_ta': 'பொதுத்துறை நிறுவனங்களுக்கான குழு (COPU) எப்போது மற்றும் யாருடைய பரிந்துரையின் பேரில் உருவாக்கப்பட்டது?',
            'back_en': 'Created in 1964 on the recommendation of the Krishna Menon Committee. It has 22 members (15 LS + 7 RS), and its Chairperson must be a Lok Sabha member.',
            'back_ta': 'கிருஷ்ண மேனன் குழுவின் பரிந்துரையின் பேரில் 1964-ல் உருவாக்கப்பட்டது. 22 உறுப்பினர்கள் (15 LS + 7 RS) கொண்டது; இதன் தலைவர் கட்டாயம் மக்களவை உறுப்பினராக இருக்க வேண்டும்.'
        },
        {
            'id': 'pc_p1_c5',
            'front_en': 'Can a Minister be elected or nominated to any of the three Financial Committees?',
            'front_ta': 'மூன்று நிதிக் குழுக்களில் எதிலாவது ஒரு அமைச்சர் உறுப்பினராகத் தேர்ந்தெடுக்கப்படவோ நியமிக்கப்படவோ முடியுமா?',
            'back_en': 'NO. A Minister CANNOT be elected as a member of PAC, Estimates Committee, or COPU. If an existing member becomes a Minister, they cease to be a member.',
            'back_ta': 'முடியாது. PAC, மதிப்பீட்டுக் குழு அல்லது COPU ஆகியவற்றில் ஒரு அமைச்சர் உறுப்பினராக முடியாது. ஏற்கனவே உள்ள உறுப்பினர் அமைச்சரானால் அவர் உறுப்பினர் பதவியை இழக்கிறார்.'
        }
    ]
    with open(p1, 'w', encoding='utf-8') as f:
        json.dump(d1, f, indent=2, ensure_ascii=False)

    # Part 2
    p2 = 'data/notes/polity/parliamentary_committees_part_2.json'
    with open(p2, 'r', encoding='utf-8') as f:
        d2 = json.load(f)
    d2['content']['revision_cards'] = [
        {
            'id': 'pc_p2_c1',
            'front_en': 'What is the system and total strength of Departmentally Related Standing Committees (DRSCs)?',
            'front_ta': 'துறைசார் நிலைக்குழுக்களின் (DRSCs) அமைப்பு மற்றும் மொத்த எண்ணிக்கை யாது?',
            'back_en': 'Set up in 1993 (17 committees) and expanded to 24 in 2004. 16 function under Lok Sabha and 8 under Rajya Sabha. Each has 31 members (21 LS + 10 RS).',
            'back_ta': '1993-ல் (17 குழுக்கள்) அமைக்கப்பட்டு, 2004-ல் 24 ஆக விரிவாக்கப்பட்டது. 16 மக்களவையின் கீழும், 8 மாநிலங்களவையின் கீழும் செயல்படுகின்றன. ஒவ்வொன்றிலும் 31 உறுப்பினர்கள் (21 LS + 10 RS) உள்ளனர்.'
        },
        {
            'id': 'pc_p2_c2',
            'front_en': 'What are the main functions of DRSCs regarding Demands for Grants?',
            'front_ta': 'மானியக் கோரிக்கைகள் தொடர்பாக DRSC-களின் முக்கிய பணிகள் யாவை?',
            'back_en': 'To examine Demands for Grants of ministries during parliamentary recess and submit reports without proposing cut motions.',
            'back_ta': 'நாடாளுமன்ற இடைவேளையின் போது அமைச்சகங்களின் மானியக் கோரிக்கைகளை ஆராய்ந்து வெட்டுத் தீர்மானங்களை முன்மொழியாமல் அறிக்கைகளைச் சமர்ப்பித்தல்.'
        },
        {
            'id': 'pc_p2_c3',
            'front_en': 'What is the composition and role of the Committee on Privileges in Parliament?',
            'front_ta': 'நாடாளுமன்றத்தில் சிறப்புரிமைக் குழுவின் அமைப்பு மற்றும் பங்கு யாது?',
            'back_en': 'Lok Sabha committee has 15 members; Rajya Sabha committee has 10 members. It examines cases of breach of privilege and contempt of the House (semi-judicial role).',
            'back_ta': 'மக்களவைக் குழு 15 உறுப்பினர்களையும், மாநிலங்களவைக் குழு 10 உறுப்பினர்களையும் கொண்டது. சிறப்புரிமை மீறல் மற்றும் அவமதிப்பு வழக்குகளை ஆராய்கிறது (அரை-நீதித்துறை பங்கு).'
        },
        {
            'id': 'pc_p2_c4',
            'front_en': 'Who chairs the Business Advisory Committee (BAC) in Lok Sabha and Rajya Sabha?',
            'front_ta': 'மக்களவை மற்றும் மாநிலங்களவையில் அலுவல் ஆலோசனைக் குழுவுக்கு (BAC) தலைமை தாங்குபவர் யார்?',
            'back_en': 'In Lok Sabha, the Speaker is the ex-officio Chairman (15 members); in Rajya Sabha, the Chairman is the ex-officio Chairman (11 members).',
            'back_ta': 'மக்களவையில் சபாநாயகர் பதவிவழித் தலைவராவார் (15 உறுப்பினர்கள்); மாநிலங்களவையில் தலைவர் பதவிவழித் தலைவராவார் (11 உறுப்பினர்கள்).'
        },
        {
            'id': 'pc_p2_c5',
            'front_en': 'What is the function of the Committee on Subordinate Legislation?',
            'front_ta': 'துணைநிலைச் சட்டமன்றக் குழுவின் பணி யாது?',
            'back_en': 'To scrutinize whether powers to make regulations, rules, sub-rules, and bye-laws delegated by Parliament are being properly exercised within statutory limits.',
            'back_ta': 'நாடாளுமன்றத்தால் வழங்கப்பட்ட விதிகள், துணை விதிகள் மற்றும் ஒழுங்குமுறைகளை உருவாக்கும் அதிகாரம் சட்ட வரம்புகளுக்குள் சரியாகப் பயன்படுத்தப்படுகிறதா என்பதை ஆராய்தல்.'
        }
    ]
    with open(p2, 'w', encoding='utf-8') as f:
        json.dump(d2, f, indent=2, ensure_ascii=False)

    # Part 3
    p3 = 'data/notes/polity/parliamentary_committees_part_3.json'
    with open(p3, 'r', encoding='utf-8') as f:
        d3 = json.load(f)
    d3['content']['revision_cards'] = [
        {
            'id': 'pc_p3_c1',
            'front_en': 'What is an Ad Hoc Committee in the Indian Parliament?',
            'front_ta': 'இந்திய நாடாளுமன்றத்தில் தற்காலிகக் குழு (Ad Hoc Committee) என்றால் என்ன?',
            'back_en': 'A temporary committee constituted for a specific task or inquiry that ceases to exist once its task is finished and report is submitted.',
            'back_ta': 'குறிப்பிட்ட பணி அல்லது விசாரணைக்காக அமைக்கப்பட்டு, பணி முடிந்து அறிக்கை சமர்ப்பிக்கப்பட்டவுடன் கலைக்கப்படும் ஒரு தற்காலிகக் குழு.'
        },
        {
            'id': 'pc_p3_c2',
            'front_en': 'Differentiate between a Select Committee and a Joint Committee on a Bill.',
            'front_ta': 'ஒரு மசோதா மீதான தேர்வு குழு மற்றும் கூட்டுக் குழுவிற்கு இடையேயான வேறுபாடு யாது?',
            'back_en': 'A Select Committee consists of members from ONE House only; a Joint Committee includes members from BOTH Houses in a 2:1 ratio (Lok Sabha : Rajya Sabha).',
            'back_ta': 'தேர்வு குழு ஒரே ஒரு அவையின் உறுப்பினர்களை மட்டுமே கொண்டது; கூட்டுக் குழு 2:1 என்ற விகிதத்தில் (மக்களவை : மாநிலங்களவை) இரு அவைகளின் உறுப்பினர்களையும் உள்ளடக்கியது.'
        },
        {
            'id': 'pc_p3_c3',
            'front_en': 'What is a Joint Parliamentary Committee (JPC)?',
            'front_ta': 'கூட்டு நாடாளுமன்றக் குழு (JPC) என்றால் என்ன?',
            'back_en': 'An ad hoc joint committee set up on a motion adopted by one House and agreed to by the other to investigate specific issues of public concern or financial irregularities.',
            'back_ta': 'பொது முக்கியத்துவம் வாய்ந்த பிரச்சினைகள் அல்லது நிதி முறைகேடுகளை விசாரிக்க ஒரு அவையால் தீர்மானம் நிறைவேற்றப்பட்டு மற்றொரு அவையால் ஏற்கப்பட்டு அமைக்கப்படும் தற்காலிகக் கூட்டுக் குழு.'
        },
        {
            'id': 'pc_p3_c4',
            'front_en': 'Are Consultative Committees considered Parliamentary Committees?',
            'front_ta': 'ஆலோசனைக் குழுக்கள் (Consultative Committees) நாடாளுமன்றக் குழுக்களாகக் கருதப்படுகின்றனவா?',
            'back_en': 'NO. Consultative Committees are constituted by Ministry of Parliamentary Affairs, chaired by Union Ministers, and are NOT parliamentary committees in the constitutional sense.',
            'back_ta': 'இல்லை. ஆலோசனைக் குழுக்கள் நாடாளுமன்ற விவகாரங்கள் அமைச்சகத்தால் அமைக்கப்பட்டு, மத்திய அமைச்சர்களால் தலைமை தாங்கப்படுகின்றன; அவை அரசியலமைப்பு ரீதியான நாடாளுமன்றக் குழுக்கள் அல்ல.'
        },
        {
            'id': 'pc_p3_c5',
            'front_en': 'What electoral method is used to select members of Financial Committees and DRSCs?',
            'front_ta': 'நிதிக் குழுக்கள் மற்றும் DRSC உறுப்பினர்களைத் தேர்ந்தெடுக்க எந்த தேர்தல் முறை பயன்படுத்தப்படுகிறது?',
            'back_en': 'Proportional representation by means of the single transferable vote (PR-STV), ensuring all political parties get fair representation.',
            'back_ta': 'அனைத்து அரசியல் கட்சிகளுக்கும் நியாயமான பிரதிநிதித்துவம் கிடைப்பதை உறுதி செய்யும் ஒற்றை மாற்று வாக்கு மூலம் விகிதாசாரப் பிரதிநிதித்துவ முறை (PR-STV).'
        }
    ]
    with open(p3, 'w', encoding='utf-8') as f:
        json.dump(d3, f, indent=2, ensure_ascii=False)
    print('Updated PC notes with flashcards successfully.')


if __name__ == '__main__':
    update_jrap_notes()
    update_pc_notes()
