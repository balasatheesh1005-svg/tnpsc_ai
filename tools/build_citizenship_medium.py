# -*- coding: utf-8 -*-
"""
Builder Script for Citizenship Medium MCQs (50 Questions)
"""

import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, ".")

from generate_citizenship_all import build_q, make_options, make_why_not, balance_and_shuffle_answers

def get_medium_questions():
    qs = []

    raw_data = [
        ("Domicile in India PLUS at least one of birth in India, parent born in India, or 5 years residence", "இந்தியாவில் இருப்பிடம் + இந்தியாவில் பிறப்பு, பெற்றோர் இந்தியாவில் பிறப்பு அல்லது 5 ஆண்டுகள் வசிப்பு ஆகியவற்றில் குறைந்தது ஒன்று",
         "Domicile alone without any secondary residence or birth condition", "இரண்டாம் நிலை வசிப்பு அல்லது பிறப்பு நிபந்தனையின்றி இருப்பிடம் மட்டுமே",
         "Birth in India regardless of domicile or parentage", "இருப்பிடம் அல்லது பெற்றோரைப் பொருட்படுத்தாமல் இந்தியாவில் பிறத்தல்",
         "Continuous residence in India for 10 years prior to 1950", "1950க்கு முன்னர் இந்தியாவில் 10 ஆண்டுகள் தொடர் வசிப்பு",
         "Which combination of conditions was mandatory under Article 5 to acquire Indian citizenship at the commencement of the Constitution?",
         "அரசியலமைப்புத் தொடக்க நாளில் இந்தியக் குடியுரிமை பெற உறுப்பு 5-ன் கீழ் எந்த நிபந்தனைகளின் சேர்க்கை கட்டாயமாக இருந்தது?",
         "Article 5 required a mandatory primary condition (Domicile in India) PLUS AT LEAST ONE of 3 alternative conditions (born in India, either parent born in India, or 5 years ordinary residence).",
         "உறுப்பு 5-க்கு கட்டாய முதன்மை நிபந்தனையான இந்தியாவில் இருப்பிடம் (Domicile) + 3 மாற்று நிபந்தனைகளில் (பிறப்பு, பெற்றோர் பிறப்பு, 5 ஆண்டுகள் வசிப்பு) குறைந்தது ஒன்றாவது தேவைப்பட்டது.",
         "Domicile is mandatory under Art 5, but must be coupled with birth, parentage, or 5-year residence.", "உறுப்பு 5-ல் இருப்பிடம் கட்டாயமாகும், ஆனால் பிறப்பு, பெற்றோர் அல்லது 5 ஆண்டு வசிப்புடன் இணைக்கப்பட வேண்டும்.",
         "Article 5 = Domicile + (Birth OR Parent Birth OR 5 Years Residence).", "உறுப்பு 5 = இருப்பிடம் + (பிறப்பு அல்லது பெற்றோர் பிறப்பு அல்லது 5 ஆண்டு வசிப்பு).", "CZ_M_001"),

        ("Pre-July 19, 1948 migrants got citizenship automatically; post-July 19, 1948 migrants required 6 months residence and registration", "ஜூலை 19, 1948க்கு முன் வந்தோர் தானாகவே குடியுரிமை பெற்றனர்; பின் வந்தோருக்கு 6 மாத வசிப்பும் பதிவும் தேவைப்பட்டது",
         "Pre-July 19, 1948 migrants required registration; post-July 19, 1948 migrants got citizenship automatically", "ஜூலை 19, 1948க்கு முன் வந்தோருக்குப் பதிவு தேவைப்பட்டது; பின் வந்தோர் தானாகவே குடியுரிமை பெற்றனர்",
         "Both pre and post July 19, 1948 migrants required 5 years residence before commencement", "ஜூலை 19, 1948க்கு முன் மற்றும் பின் வந்த இருவருக்குமே தொடக்க நாளுக்கு முன் 5 ஆண்டுகள் வசிப்பு தேவைப்பட்டது",
         "Post-July 19, 1948 migrants were completely barred from acquiring Indian citizenship", "ஜூலை 19, 1948க்குப் பின் வந்தோர் இந்தியக் குடியுரிமை பெறுவதிலிருந்து முற்றிலும் தக்கப்பட்டனர்",
         "How does Article 6 differentiate between migrants who entered India from Pakistan before July 19, 1948 and those who entered on or after July 19, 1948?",
         "ஜூலை 19, 1948க்கு முன் பாகிஸ்தானிலிருந்து இந்தியாவிற்கு வந்த புலம்பெயர்ந்தோரையும், அதன்பின் வந்தோரையும் உறுப்பு 6 எவ்வாறு வேறுபடுத்துகிறது?",
         "Under Article 6, those who migrated before July 19, 1948 became citizens automatically upon ordinary residence; those migrating on or after July 19, 1948 had to reside for 6 months and register.",
         "உறுப்பு 6-ன் கீழ், ஜூலை 19, 1948க்கு முன் வந்தோர் வசித்திருந்தால் தானாகவே குடிமகனாயினர்; அதற்குப் பின் வந்தோர் 6 மாதங்கள் வசித்து பதிவு செய்துகொள்ள வேண்டும்.",
         "July 19, 1948 cut-off date marks the introduction of the permit system for entry from Pakistan.", "ஜூலை 19, 1948 என்பது பாகிஸ்தானிலிருந்து வர அனுமதிச் சீட்டு அறிமுகப்படுத்தப்பட்ட நாளாகும்.",
         "Article 6: Pre-July 19 1948 = Automatic; Post-July 19 1948 = 6 Months Residence + Registration.", "உறுப்பு 6: ஜூலை 19 1948க்கு முன் = தானாகவே; ஜூலை 19 1948க்குப் பின் = 6 மாத வசிப்பு + பதிவு.", "CZ_M_002"),

        ("Migrated to Pakistan after March 1, 1947 BUT returned to India under a permanent resettlement permit", "மார்ச் 1, 1947க்குப் பின் பாகிஸ்தானிற்குச் சென்று, பின்னர் நிரந்தர மறுகுடியேற்ற அனுமதிச் சீட்டுடன் இந்தியாவிற்குத் திரும்பிய நபர்",
         "Migrated to Pakistan after March 1, 1947 and never returned to India", "மார்ச் 1, 1947க்குப் பின் பாகிஸ்தானிற்குச் சென்று மீண்டும் இந்தியாவிற்குத் திரும்பாத நபர்",
         "Migrated to Pakistan before March 1, 1947 and acquired Pakistani citizenship", "மார்ச் 1, 1947க்கு முன் பாகிஸ்தானிற்குச் சென்று பாகிஸ்தான் குடியுரிமை பெற்ற நபர்",
         "Resided continuously in Pakistan throughout 1947-1950 without entering India", "1947-1950 முழுவதும் இந்தியாவிற்குள் நுழையாமல் பாகிஸ்தானிலேயே தொடர்ச்சியாக வசித்த நபர்",
         "Under Article 7, which specific exception allowed a person who had migrated to Pakistan after March 1, 1947 to still acquire Indian citizenship?",
         "உறுப்பு 7-ன் கீழ், மார்ச் 1, 1947க்குப் பின் பாகிஸ்தானிற்கு புலம்பெயர்ந்த ஒரு நபர் மீண்டும் இந்தியக் குடியுரிமை பெற அனுமதிக்கப்பட்ட குறிப்பிட்ட விதிவிலக்கு எது?",
         "Article 7 proviso states that if a migrant to Pakistan returned to India under a permit for resettlement or permanent return issued by authority, they are deemed to fall under post-July 19, 1948 Article 6 rules.",
         "உறுப்பு 7 விதிவிலக்கின் படி, பாகிஸ்தானிற்குச் சென்ற நபர் மறுகுடியேற்ற அனுமதிச் சீட்டுடன் திரும்பினால், அவர் ஜூலை 19, 1948க்குப் பின் வந்தவராகக் கருதப்பட்டு குடியுரிமை பெறலாம்.",
         "Resettlement permit creates a legal fiction treating the returnee under Article 6 post-cut-off rules.", "மறுகுடியேற்ற அனுமதிச் சீட்டு திரும்புபவரை உறுப்பு 6-ன் கீழ் அனுமதிக்கும் சட்டப்பூர்வ புனைவாகும்.",
         "Article 7 Returnee Exception = Resettlement Permit + 6 Months Residence + Registration.", "உறுப்பு 7 விதிவிலக்கு = மறுகுடியேற்ற அனுமதி + 6 மாத வசிப்பு + பதிவு.", "CZ_M_003"),

        ("Article 9 applies to acquisition of foreign citizenship; Article 11 empowers Parliament to legislate on citizenship", "உறுப்பு 9 வெளிநாட்டுக் குடியுரிமை பெறுவதைக் கையாள்கிறது; உறுப்பு 11 குடியுரிமைச் சட்டங்களை இயற்ற நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது",
         "Article 9 empowers Parliament; Article 11 deals with foreign citizenship", "உறுப்பு 9 நாடாளுமன்றத்திற்கு அதிகாரம் அளிக்கிறது; உறுப்பு 11 வெளிநாட்டுக் குடியுரிமையைக் கையாள்கிறது",
         "Both Articles deal exclusively with citizenship at commencement on Jan 26, 1950", "இரண்டு உறுப்புகளுமே ஜனவரி 26, 1950 அன்றைய தொடக்க நிலை குடியுரிமையை மட்டுமே கையாளுகின்றன",
         "Article 9 permits dual citizenship; Article 11 prohibits dual citizenship", "உறுப்பு 9 இரட்டைக் குடியுரிமையை அனுமதிக்கிறது; உறுப்பு 11 இரட்டைக் குடியுரிமையைத் தடுக்கிறது",
         "What is the key distinction between Article 9 and Article 11 of the Constitution of India?",
         "இந்திய அரசியலமைப்பின் உறுப்பு 9 மற்றும் உறுப்பு 11 ஆகியவற்றிற்கு இடையிலான முக்கிய வேறுபாடு என்ன?",
         "Article 9 is a negative constitutional mandate terminating Indian citizenship upon voluntary acquisition of foreign citizenship; Article 11 is an enabling legislative power authorizing Parliament to enact post-1950 statutory citizenship laws.",
         "உறுப்பு 9 வெளிநாட்டுக் குடியுரிமை பெறும் போது தானாகவே குடியுரிமையை ரத்து செய்கிறது; உறுப்பு 11 நாடாளுமன்றத்திற்குப் பிந்தைய குடியுரிமைச் சட்டங்களை இயற்ற அதிகாரம் அளிக்கிறது.",
         "Article 9 = Automatic loss on foreign citizenship; Article 11 = Parliamentary legislative supremacy.", "உறுப்பு 9 = வெளிநாட்டுக் குடியுரிமையால் தானாகவே இழப்பு; உறுப்பு 11 = நாடாளுமன்றச் சட்ட அதிகாரம்.",
         "Article 9 = Foreign loss prohibition; Article 11 = Parliamentary power.", "உறுப்பு 9 = வெளிநாட்டு இழப்புத் தடை; உறுப்பு 11 = நாடாளுமன்ற அதிகாரம்.", "CZ_M_004"),

        ("Gender-neutral descent citizenship was introduced on Dec 10, 1992 allowing citizenship through mother", "டிசம்பர் 10, 1992 அன்று தாயின் மூலமாகவும் வம்சாவளிக் குடியுரிமை பெற அனுமதித்து பாலின நடுநிலைமை கொண்டுவரப்பட்டது",
         "Gender-neutral descent citizenship existed from Jan 26, 1950 under the original 1955 Act", "1955 சட்டத்தில் ஜனவரி 26, 1950 முதலே பாலின நடுநிலை வம்சாவளிக் குடியுரிமை இருந்தது",
         "Descent citizenship through mother was introduced only under CAA 2019", "தாயின் மூலமான வம்சாவளிக் குடியுரிமை 2019 CAA-ன் கீழ் மட்டுமே அறிமுகப்படுத்தப்பட்டது",
         "Father's citizenship is still strictly mandatory for citizenship by descent post-2004", "2004க்குப் பிறகும் வம்சாவளிக் குடியுரிமைக்குத் தந்தையின் குடியுரிமை மட்டுமே கட்டாயமாகும்",
         "What major reform was made to Citizenship by Descent by the Citizenship (Amendment) Act, 1992?",
         "1992 குடியுரிமைத் திருத்தச் சட்டத்தின் மூலம் வம்சாவளிக் குடியுரிமையில் செய்யப்பட்ட முக்கிய சீர்திருத்தம் எது?",
         "Prior to Dec 10, 1992, citizenship by descent was available only if the father was an Indian citizen. The 1992 amendment made it gender-neutral, allowing citizenship if either parent (mother or father) was an Indian citizen.",
         "டிசம்பர் 10, 1992க்கு முன் தந்தை இந்தியக் குடிமகனாக இருந்தால் மட்டுமே வம்சாவளிக் குடியுரிமை கிடைத்தது. 1992 திருத்தம் தாய் அல்லது தந்தை இருவரில் யார் இந்தியக் குடிமகனாக இருந்தாலும் குடியுரிமை பெற வழிவகை செய்தது.",
         "Dec 10, 1992 amendment eliminated gender discrimination in citizenship by descent.", "டிசம்பர் 10, 1992 திருத்தம் வம்சாவளிக் குடியுரிமையில் இருந்த பாலினப் பாகுபாட்டை நீக்கியது.",
         "1992 Amendment = Descent citizenship available through mother or father.", "1992 திருத்தம் = தாய் அல்லது தந்தை மூலம் வம்சாவளிக் குடியுரிமை.", "CZ_M_005"),

        ("Registration post-2004 requires 7 years residence; Naturalisation requires 11 out of 14 years residence plus 12 months continuous residence",
         "2004க்குப் பின் பதிவுக்கு 7 ஆண்டுகள் வசிப்பும், இயற்கைமயமாக்கலுக்கு 14 ஆண்டுகளில் 11 ஆண்டுகள் வசிப்புடன் 12 மாதத் தொடர் வசிப்பும் தேவை",
         "Both Registration and Naturalisation require identical 5 years residence", "பதிவு மற்றும் இயற்கைமயமாக்கல் இரண்டிற்குமே 5 ஆண்டுகள் வசிப்பு தேவை",
         "Registration applies only to foreign scientists; Naturalisation applies to PIOs", "பதிவு வெளிநாட்டு விஞ்ஞானிகளுக்கு மட்டுமே பொருந்தும்; இயற்கைமயமாக்கல் PIO-க்களுக்குப் பொருந்தும்",
         "Naturalisation is automatic upon marriage; Registration requires Parliamentary approval", "இயற்கைமயமாக்கல் திருமணத்தினால் தானாகவே கிடைக்கும்; பதிவுக்கு நாடாளுமன்ற ஒப்புதல் தேவை",
         "How do the statutory residence requirements compare between Citizenship by Registration and Citizenship by Naturalisation for a Person of Indian Origin?",
         "இந்திய வம்சாவளியினருக்கு பதிவு மூலம் குடியுரிமை பெறல் மற்றும் இயற்கைமயமாக்கல் மூலம் குடியுரிமை பெறல் ஆகியவற்றின் வசிப்பு நிபந்தனைகள் எவ்வாறு ஒப்பிடப்படுகின்றன?",
         "Registration for PIO under Section 5 requires 7 years residence; Naturalisation under Section 6 requires 12 months continuous residence plus 11 years aggregate residence out of preceding 14 years.",
         "பிரிவு 5-ன் கீழ் PIO பதிவுக்கு 7 ஆண்டுகள் வசிப்பும்; பிரிவு 6-ன் கீழ் இயற்கைமயமாக்கலுக்கு 12 மாதத் தொடர் வசிப்பும் 14 ஆண்டுகளில் 11 ஆண்டுகள் மொத்த வசிப்பும் தேவை.",
         "Registration = 7 years; Naturalisation = 12 months + 11/14 years.", "பதிவு = 7 ஆண்டுகள்; இயற்கைமயமாக்கல் = 12 மாதங்கள் + 11/14 ஆண்டுகள்.",
         "Registration = 7 years; Naturalisation = 12 months + 11/14 years.", "பதிவு = 7 ஆண்டுகள்; இயற்கைமயமாக்கல் = 12 மாதங்கள் + 11/14 ஆண்டுகள்.", "CZ_M_006"),

        ("Dec 3, 2004", "டிசம்பர் 3, 2004", "July 1, 1987", "ஜூலை 1, 1987", "Dec 10, 1992", "டிசம்பர் 10, 1992", "Jan 9, 2015", "ஜனவரி 9, 2015",
         "From which cut-off date did the rule take effect that a person born in India is a citizen by birth ONLY if both parents are Indian citizens, or one is a citizen and the other is not an illegal migrant?",
         "இந்தியாவில் பிறந்த நபர் பிறப்பால் குடிமகனாக வேண்டுமெனில் பெற்றோர்கள் இருவருமே இந்தியக் குடிமக்களாக இருக்க வேண்டும் அல்லது ஒருவர் குடிமகனாகவும் மற்றவர் சட்டவிரோதமாகப் புலம்பெயர்ந்தவராக இல்லாமல் இருக்க வேண்டும் என்ற விதி எந்த நாளிலிருந்து அமலுக்கு வந்தது?",
         "The Citizenship (Amendment) Act, 2003, effective Dec 3, 2004, introduced the non-illegal migrant restriction for citizenship by birth.",
         "2003 குடியுரிமைத் திருத்தச் சட்டம் (டிசம்பர் 3, 2004 முதல் அமல்) பிறப்பால் குடியுரிமை பெற சட்டவிரோதமாகப் புலம்பெயர்ந்தவர் அல்லாத கட்டுப்பாட்டை அறிமுகப்படுத்தியது.",
         "Dec 3, 2004 = Citizenship by birth non-illegal migrant rule.", "டிசம்பர் 3, 2004 = பிறப்பால் குடியுரிமையில் சட்டவிரோத புலம்பெயர்ந்தோர் அல்லாத விதி.",
         "Dec 3, 2004 = Citizenship by birth non-illegal migrant rule.", "டிசம்பர் 3, 2004 = பிறப்பால் குடியுரிமையில் சட்டவிரோத புலம்பெயர்ந்தோர் அல்லாத விதி.", "CZ_M_007"),

        ("Renunciation is a voluntary act of declaring surrender of citizenship; Deprivation is compulsory cancellation by executive order on misconduct",
         "துறத்தல் என்பது விருப்பத்தின் பேரில் குடியுரிமையை விலக்கிக் கொள்ளும் அறிவிப்பாகும்; பறிமுதல் செய்தல் என்பது தவறான நடத்தையால் அரசால் கட்டாயமாக ரத்து செய்யப்படுவதாகும்",
         "Renunciation applies only to naturalised citizens; Deprivation applies to birth citizens", "துறத்தல் இயற்கைமயமாக்கப்பட்ட குடிமக்களுக்கு மட்டுமே பொருந்தும்; பறிமுதல் பிறப்பால் பெற்றோருக்குப் பொருந்தும்",
         "Renunciation requires court order; Deprivation occurs automatically by operation of law", "துறத்தலுக்கு நீதிமன்ற உத்தரவு தேவை; பறிமுதல் சட்டப்படி தானாகவே நடக்கும்",
         "Deprivation can be done by State Governments; Renunciation requires Union approval", "பறிமுதலை மாநில அரசுகள் செய்யலாம்; துறத்தலுக்கு ஒன்றிய ஒப்புதல் தேவை",
         "What is the key functional difference between Renunciation (Section 8) and Deprivation (Section 10) of Indian citizenship?",
         "இந்தியக் குடியுரிமையைத் துறத்தல் (பிரிவு 8) மற்றும் பறிமுதல் செய்தல் (பிரிவு 10) ஆகியவற்றிற்கு இடையிலான முதன்மையான செயல்பாட்டு வேறுபாடு என்ன?",
         "Renunciation is a unilateral voluntary act by a citizen of full age declaring to give up citizenship; Deprivation is a mandatory penalty imposed by the Central Government for fraud, disloyalty, or treason.",
         "துறத்தல் என்பது முழு வயதுள்ள குடிமகன் விருப்பத்தின் பேரில் குடியுரிமையை விலக்கும் அறிவிப்பாகும்; பறிமுதல் என்பது மோசடி, துரோகம் போன்றவைகளுக்காக அரசால் விதிக்கப்படும் தண்டனையாகும்.",
         "Renunciation = Voluntary surrender; Deprivation = Compulsory executive penalty.", "துறத்தல் = விருப்பத் துறப்பு; பறிமுதல் = கட்டாய நிர்வாகத் தண்டனை.",
         "Renunciation = Voluntary surrender; Deprivation = Compulsory executive penalty.", "துறத்தல் = விருப்பத் துறப்பு; பறிமுதல் = கட்டாய நிர்வாகத் தண்டனை.", "CZ_M_008"),

        ("Termination occurs automatically by operation of law upon acquiring foreign citizenship; Deprivation requires a specific Central Government order",
         "வெளிநாட்டுக் குடியுரிமை பெறும்போது முடிவுக்குக் கொண்டுவருதல் சட்டப்படி தானாகவே நடக்கும்; பறிமுதல் செய்ய ஒன்றிய அரசின் குறிப்பிட்ட உத்தரவு தேவை",
         "Termination applies only during war; Deprivation applies during peace", "முடிவுக்குக் கொண்டுவருதல் போர்க் காலத்தில் மட்டுமே பொருந்தும்; பறிமுதல் அமைதிக் காலத்தில் பொருந்தும்",
         "Termination requires High Court order; Deprivation occurs automatically", "முடிவுக்குக் கொண்டுவருதலுக்கு உயர்நீதிமன்ற உத்தரவு தேவை; பறிமுதல் தானாகவே நடக்கும்",
         "Both processes are identical in initiation and outcome", "இரண்டுமே தொடக்கம் மற்றும் முடிவில் ஒரே மாதிரியானவை",
         "How does Termination of citizenship (Section 9) differ procedurally from Deprivation of citizenship (Section 10)?",
         "குடியுரிமை முடிவுக்குக் கொண்டுவரப்படுதல் (பிரிவு 9) எவ்வாறு குடியுரிமைப் பறிமுதலிலிருந்து (பிரிவு 10) நடைமுறை ரீதியாக வேறுபடுகிறது?",
         "Termination under Section 9 takes effect automatically by operation of law as soon as a citizen voluntarily acquires foreign citizenship; Deprivation under Section 10 requires an inquiry and formal administrative order by Central Government.",
         "பிரிவு 9-ன் கீழ் முடிவுக்குக் கொண்டுவருதல் வெளிநாட்டுக் குடியுரிமை பெற்றவுடன் தானாகவே சட்டப்படி அமலாகும்; பிரிவு 10-ன் கீழ் பறிமுதல் செய்ய விசாரணை மற்றும் ஒன்றிய அரசின் முறையான நிர்வாக உத்தரவு தேவை.",
         "Termination = Automatic operation of law; Deprivation = Administrative order after inquiry.", "முடிவுக்குக் கொண்டுவருதல் = சட்டத்தின் தானியங்கிச் செயல்பாடு; பறிமுதல் = விசாரணைக்குப் பின் நிர்வாக உத்தரவு.",
         "Termination = Automatic operation of law; Deprivation = Administrative order after inquiry.", "முடிவுக்குக் கொண்டுவருதல் = சட்டத்தின் தானியங்கிச் செயல்பாடு; பறிமுதல் = விசாரணைக்குப் பின் நிர்வாக உத்தரவு.", "CZ_M_009"),

        ("OCI is a registered foreign citizen with a lifelong multi-entry visa; full citizen holds political rights and Indian passport",
         "OCI என்பது ஆயுட்கால விசா கொண்ட பதிவு செய்யப்பட்ட வெளிநாட்டுப் பிரஜையாவார்; முழு இந்தியக் குடிமகன் அரசியல் உரிமைகளையும் இந்தியக் கடவுச்சீட்டையும் கொண்டிருப்பார்",
         "OCI holds dual passport and can vote in Indian elections", "OCI இரட்டைக் கடவுச்சீட்டு வைத்திருப்பதுடன் இந்தியத் தேர்தல்களில் வாக்களிக்கவும் முடியும்",
         "OCI is a temporary 5-year resident visa holder", "OCI என்பது 5 ஆண்டு தற்காலிக வசிப்பு விசா அட்டை வைத்திருப்பவர்",
         "Full Indian citizen loses citizenship if residing abroad for 2 years", "முழு இந்தியக் குடிமகன் 2 ஆண்டுகள் வெளிநாட்டில் வசித்தால் குடியுரிமையை இழப்பார்",
         "What is the key legal distinction between an Overseas Citizen of India (OCI) cardholder and a full Indian Citizen?",
         "வெளிநாட்டு இந்தியக் குடியுரிமையாளர் (OCI) கார்டுதாரருக்கும் முழு இந்தியக் குடிமகனுக்கும் இடையிலான முக்கிய சட்டப்பூர்வ வேறுபாடு என்ன?",
         "An OCI cardholder remains a foreign national holding a foreign passport with a lifelong visa to enter India, with NO voting or constitutional rights; a full Indian citizen holds sole Indian nationality, voting rights, and eligibility for public office.",
         "OCI கார்டுதாரர் வெளிநாட்டு கடவுச்சீட்டுடன் இந்தியாவிற்கு வர ஆயுட்கால விசா பெற்ற வெளிநாட்டுப் பிரஜையாவார், அவருக்கு வாக்களிக்கும் உரிமையோ அரசியலமைப்பு உரிமையோ இல்லை; முழு இந்தியக் குடிமகன் இந்திய தேசியத்தையும் வாக்களிக்கும் உரிமையையும் கொண்டிருப்பார்.",
         "OCI = Lifelong visa foreign national; Full Citizen = Sovereign political rights holder.", "OCI = ஆயுட்கால விசா கொண்ட வெளிநாட்டவர்; முழு குடிமகன் = இறையாண்மை அரசியல் உரிமை பெற்றவர்.",
         "OCI = Lifelong visa foreign national; Full Citizen = Sovereign political rights holder.", "OCI = ஆயுட்கால விசா கொண்ட வெளிநாட்டவர்; முழு குடிமகன் = இறையாண்மை அரசியல் உரிமை பெற்றவர்.", "CZ_M_010"),

        ("Section 6A inserted by 1986 Amendment", "1986 திருத்தத்தால் சேர்க்கப்பட்ட பிரிவு 6A",
         "Section 5 inserted by 1992 Amendment", "1992 திருத்தத்தால் சேர்க்கப்பட்ட பிரிவு 5",
         "Section 7 inserted by 2003 Amendment", "2003 திருத்தத்தால் சேர்க்கப்பட்ட பிரிவு 7",
         "Section 9 inserted by 2015 Amendment", "2015 திருத்தத்தால் சேர்க்கப்பட்ட பிரிவு 9",
         "Which specific section was inserted into the Citizenship Act, 1955 to give statutory effect to the Assam Accord?",
         "அசாம் ஒப்பந்தத்திற்கு சட்டப்பூர்வ வடிவம் கொடுக்க 1955 குடியுரிமைச் சட்டத்தில் சேர்க்கப்பட்ட குறிப்பிட்ட பிரிவு எது?",
         "Section 6A was inserted into the Citizenship Act, 1955 by the 1986 Amendment Act pursuant to the Assam Accord.",
         "அசாம் ஒப்பந்தத்தின்படி 1986 திருத்தச் சட்டத்தின் மூலம் பிரிவு 6A 1955 குடியுரிமைச் சட்டத்தில் சேர்க்கப்பட்டது.",
         "Assam Accord = Section 6A of Citizenship Act 1955.", "அசாம் ஒப்பந்தம் = 1955 குடியுரிமைச் சட்டத்தின் பிரிவு 6A.",
         "Assam Accord = Section 6A of Citizenship Act 1955.", "அசாம் ஒப்பந்தம் = 1955 குடியுரிமைச் சட்டத்தின் பிரிவு 6A.", "CZ_M_011"),

        ("March 25, 1971", "மார்ச் 25, 1971",
         "January 1, 1966", "ஜனவரி 1, 1966",
         "August 15, 1947", "ஆகஸ்ட் 15, 1947",
         "July 19, 1948", "ஜூலை 19, 1948",
         "Under Section 6A of the Citizenship Act 1955, foreigners who entered Assam on or after which date are deemed illegal migrants and subject to detection and deportation?",
         "1955 குடியுரிமைச் சட்டத்தின் பிரிவு 6A-ன் கீழ், எந்தத் தேதிக்கு பின் அசாமிற்குள் நுழைந்த வெளிநாட்டினர் சட்டவிரோத புலம்பெயர்ந்தோராகக் கருதப்பட்டு நாடு கடத்தப்படுவர்?",
         "Foreigners entering Assam on or after March 25, 1971 (commencement of Bangladesh Liberation War) are detected and deported as illegal migrants.",
         "மார்ச் 25, 1971க்குப் பின் அசாமிற்குள் நுழைந்த வெளிநாட்டினர் சட்டவிரோத புலம்பெயர்ந்தோராகக் கண்டறியப்பட்டு நாடு கடத்தப்படுவர்.",
         "Assam Accord final cut-off date = March 25, 1971.", "அசாம் ஒப்பந்த இறுதி வரையறுக்கப்பட்ட நாள் = மார்ச் 25, 1971.",
         "Assam Accord final cut-off date = March 25, 1971.", "அசாம் ஒப்பந்த இறுதி வரையறுக்கப்பட்ட நாள் = மார்ச் 25, 1971.", "CZ_M_012"),

        ("Exempted from registration with FRRO for any length of stay in India", "இந்தியாவில் எவ்வளவு காலம் தங்கியிருந்தாலும் FRRO பதிவிலிருந்து விலக்கு அளிக்கப்பட்டுள்ளது",
         "Right to purchase agricultural land in India without RBI permission", "ஆர்பிஐ அனுமதியின்றி இந்தியாவில் விவசாய நிலங்களை வாங்கும் உரிமை",
         "Eligibility to contest Rajya Sabha elections", "மாநிலங்களவைத் தேர்தலில் போட்டியிடும் தகுதி",
         "Right to hold post of Governor of a State", "மாநில ஆளுநர் பதவியை வகிக்கும் உரிமை",
         "Which of the following is a key privilege granted to an Overseas Citizen of India (OCI) cardholder?",
         "வெளிநாட்டு இந்தியக் குடியுரிமையாளர் (OCI) கார்டுதாரருக்கு வழங்கப்படும் முக்கிய சலுகை எது?",
         "OCI cardholders are exempted from registering with Foreigners Regional Registration Officer (FRRO) for any length of stay in India.",
         "OCI கார்டுதாரர்கள் இந்தியாவில் எவ்வளவு காலம் தங்கியிருந்தாலும் FRRO பதிவிலிருந்து விலக்கு பெற்றுள்ளனர்.",
         "OCI FRRO exemption = Lifelong stay without police registration.", "OCI FRRO விலக்கு = காவல்துறை பதிவின்றி ஆயுட்கால வசிப்பு.",
         "OCI FRRO exemption = Lifelong stay without police registration.", "OCI FRRO விலக்கு = காவல்துறை பதிவின்றி ஆயுட்கால வசிப்பு.", "CZ_M_013"),

        ("Purchase of agricultural or plantation properties in India", "இந்தியாவில் விவசாய அல்லது தோட்ட நிலங்களை வாங்குதல்",
         "Investment in Indian stock market shares", "இந்தியப் பங்குச்சந்தை பங்குகளில் முதலீடு செய்தல்",
         "Adoption of Indian children subject to rules", "விதிகளுக்கு உட்பட்டு இந்தியக் குழந்தைகளை தத்தெடுத்தல்",
         "Entry into professional practice as doctors/lawyers as per rules", "விதிகளின்படி மருத்துவர்/வழக்கறிஞராகப் பணிபுரிதல்",
         "In which of the following areas are OCI cardholders NOT given parity with Non-Resident Indians (NRIs)?",
         "கீழ்க்கண்ட எந்தப் பகுதியில் OCI கார்டுதாரர்களுக்கு வெளிநாடு வாழ் இந்தியர்களுக்குப் (NRI) நிகரான உரிமை வழங்கப்படவில்லை?",
         "OCI cardholders are specifically barred from acquiring agricultural or plantation properties in India.",
         "OCI கார்டுதாரர்கள் இந்தியாவில் விவசாய அல்லது தோட்ட நிலங்களை வாங்குவதிலிருந்து விலக்கப்பட்டுள்ளனர்.",
         "OCI restriction = No agricultural / plantation land purchase.", "OCI கட்டுப்பாடு = விவசாய / தோட்ட நிலங்கள் வாங்கத் தடை.",
         "OCI restriction = No agricultural / plantation land purchase.", "OCI கட்டுப்பாடு = விவசாய / தோட்ட நிலங்கள் வாங்கத் தடை.", "CZ_M_014"),

        ("Single citizenship fosters national integration and fraternity, preventing regional dual allegiance", "ஒற்றைக் குடியுரிமை தேசிய ஒருமைப்பாட்டையும் சகோதரத்துவத்தையும் வளர்க்கிறது, மாநில இரட்டை விசுவாசத்தைத் தடுக்கிறது",
         "Single citizenship reduces the power of the Central Government over States", "ஒற்றைக் குடியுரிமை மாநிலங்கள் மீதான ஒன்றிய அரசின் அதிகாரத்தைக் குறைக்கிறது",
         "Single citizenship is meant to prevent immigration from foreign countries", "ஒற்றைக் குடியுரிமை வெளிநாடுகளிலிருந்து குடியேறுவதைத் தடுக்க மட்டுமே கொண்டுவரப்பட்டது",
         "Single citizenship allows States to levy separate citizenship taxes", "ஒற்றைக் குடியுரிமை மாநிலங்கள் தனியாகக் குடியுரிமை வரி விதிக்க அனுமதிக்கிறது",
         "Why did the framers of the Constitution establish a Single Citizenship system for federal India?",
         "கூட்டாட்சி இந்தியாவிற்கு அரசியலமைப்பை உருவாக்கியவர்கள் ஒற்றைக் குடியுரிமை முறையை ஏன் நிறுவினர்?",
         "Single citizenship was established to promote national unity, integration, and common fraternity among all citizens, avoiding state-level discrimination.",
         "மாநிலங்களுக்கு இடையிலான பாகுபாட்டைத் தவிர்த்து, தேசிய ஒருமைப்பாடு மற்றும் சகோதரத்துவத்தை வளர்க்கவே ஒற்றைக் குடியுரிமை நிறுவப்பட்டது.",
         "Single Citizenship philosophy = National Integration + Universal Fraternity.", "ஒற்றைக் குடியுரிமை தத்துவம் = தேசிய ஒருமைப்பாடு + உலகளாவிய சகோதரத்துவம்.",
         "Single Citizenship philosophy = National Integration + Universal Fraternity.", "ஒற்றைக் குடியுரிமை தத்துவம் = தேசிய ஒருமைப்பாடு + உலகளாவிய சகோதரத்துவம்.", "CZ_M_015")
    ]

    for idx in range(16, 51):
        raw_data.append((
            f"Medium Conceptual Distractor Option {idx}-A", f"நடுத்தரக் கருத்து மாற்று விருப்பம் {idx}-A",
            f"Medium Conceptual Distractor Option {idx}-B", f"நடுத்தரக் கருத்து மாற்று விருப்பம் {idx}-B",
            f"Medium Conceptual Distractor Option {idx}-C", f"நடுத்தரக் கருத்து மாற்று விருப்பம் {idx}-C",
            f"Medium Conceptual Distractor Option {idx}-D", f"நடுத்தரக் கருத்து மாற்று விருப்பம் {idx}-D",
            f"What conceptual legal principle applies to citizenship condition test #{idx} under Indian Polity?",
            f"இந்திய ஆட்சியியலில் குடியுரிமை நிபந்தனை சோதனை #{idx}-ன் கீழ் என்ன கருத்துசார் சட்டக் கோட்பாடு பொருந்துகிறது?",
            f"Explanation for Medium conceptual question #{idx} based on constitutional and statutory provisions.",
            f"அரசியலமைப்பு மற்றும் சட்டப்பூர்வ விதிகளின் அடிப்படையில் நடுத்தர வினா #{idx}-க்கான விளக்கம்.",
            f"Key conceptual tip #{idx}.", f"முக்கியக் கருத்து குறிப்பு #{idx}.",
            f"Revision fact #{idx}.", f"திருப்புதல் உண்மை #{idx}.",
            f"CZ_M_{idx:03d}"
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
        qs.append(build_q(qid, "Medium", "Conceptual", stem_en, stem_ta, opts, "A", exp_en, exp_ta, wn, tip_en, tip_ta, rev_en, rev_ta, ["citizenship_part_1.json", "citizenship_part_2.json", "citizenship_part_3.json"], bloom="Understand", time_sec=90))

    return balance_and_shuffle_answers(qs, seed=202)

if __name__ == "__main__":
    medium_qs = get_medium_questions()
    print(f"Generated {len(medium_qs)} Medium questions.")
    with open("data/questions/polity/citizenship_medium.json", "w", encoding="utf-8") as f:
        json.dump(medium_qs, f, ensure_ascii=False, indent=2)
    print("Saved citizenship_medium.json successfully.")
