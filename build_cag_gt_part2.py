# -*- coding: utf-8 -*-
"""
CAG Grand Test Part 2: Questions 51 to 100 (CAG_GT_051 to CAG_GT_100)
Fresh stems designed to have zero overlap with Core 325 questions or Part 1 questions.
"""

from cag_mcq_helper import make_cag_q

raw_gt_part2_items = [
    # 51
    (
        "Audit of Central Armed Police Forces (CAPF)",
        "Under what classification does the CAG audit modernization and logistics procurement for the Central Reserve Police Force (CRPF) and BSF?",
        "Under Central Civil Audit under the Union Ministry of Home Affairs Demands for Grants",
        "மத்திய உள்துறை அமைச்சகத்தின் மானியக் கோரிக்கைகளின் கீழ் மத்திய சிவில் தணிக்கையின் கீழ்",
        "CAPF forces are civil police organizations under MHA, not under the Ministry of Defence.",
        "CAPF படைகள் உள்துறை அமைச்சகத்தின் கீழ் உள்ள சிவில் போலீஸ் அமைப்புகளாகும்.",
        "CAG audits procurement of bulletproof jackets, high-altitude rations, and surveillance drones for CAPFs.",
        "துப்பாக்கி குண்டு துளைக்காத ஆடைகள் மற்றும் கண்காணிப்பு ட்ரோன்கள் கொள்முதலை சி.ஏ.ஜி தணிக்கை செய்கிறது."
    ),
    # 52
    (
        "Audit of Insolvency and Bankruptcy Board (IBBI)",
        "How is the Insolvency and Bankruptcy Board of India (IBBI) audited by the CAG?",
        "Audited under Section 19(2) as a statutory regulatory authority, with its Separate Audit Report presented to Parliament",
        "நாடாளுமன்றத்தில் சமர்ப்பிக்கப்படும் தனித் தணிக்கை அறிக்கையுடன் சட்டப்பூர்வ ஒழுங்குமுறை அமைப்பாக பிரிவு 19(2)-ன் கீழ் தணிக்கை செய்யப்படுகிறது",
        "Statutory regulatory boards created by Parliament submit annual SARs under the CAG Act.",
        "நாடாளுமன்றத்தால் உருவாக்கப்பட்ட ஒழுங்குமுறை வாரியங்கள் சி.ஏ.ஜி சட்டத்தின் கீழ் வருடாந்திர SAR-ஐ சமர்ப்பிக்கின்றன.",
        "IBBI audits test insolvency resolution costs and fee structures of insolvency professionals.",
        "திவால் தீர்வு செலவுகள் மற்றும் தொழில்முறை கட்டணங்களை IBBI தணிக்கை சோதிக்கிறது."
    ),
    # 53
    (
        "Audit of Central Road and Infrastructure Fund (CRIF)",
        "What is the statutory compliance requirement verified by the CAG in the audit of cess collections under the CRIF Act?",
        "Verifies that all road cess collected under Customs and Central Excise is fully transferred from CFI to the non-lapsable CRIF reserve",
        "சுங்கம் மற்றும் மத்திய கலால் கீழ் வசூலிக்கப்படும் அனைத்து சாலை வரிகளும் CFI-லிருந்து காலாவதியாகாத CRIF இருப்பிற்கு முழுமையாக மாற்றப்படுவதை உறுதி செய்கிறது",
        "Cess collected for dedicated infrastructure cannot be retained in the general revenue pool of the CFI.",
        "பிரத்யேக உள்கட்டமைப்புக்காக வசூலிக்கப்படும் செஸ் வரியை CFI-ன் பொது வருவாயில் வைத்திருக்க முடியாது.",
        "CAG repeatedly criticized the Union Government for short-transferring cess revenues to reserve funds.",
        "செஸ் வருவாயை பிரத்யேக நிதிகளுக்கு குறைவாக மாற்றியதற்காக மத்திய அரசை சி.ஏ.ஜி பலமுறை விமர்சித்துள்ளது."
    ),
    # 54
    (
        "Audit of Sovereign Green Bonds",
        "What does the CAG audit verify in the utilization of proceeds raised from Sovereign Green Bonds?",
        "Ensures proceeds are mapped strictly to eligible green projects in the National Clean Energy and Climate Framework",
        "திரட்டப்பட்ட நிதி தேசிய தூய எரிசக்தி மற்றும் பருவநிலை கட்டமைப்பில் உள்ள தகுதியான பசுமைத் திட்டங்களுக்கு மட்டுமே பயன்படுத்தப்படுவதை உறுதி செய்கிறது",
        "Prevents 'greenwashing' and diversion of green bond proceeds to conventional fossil-fuel projects.",
        "பசுமைப் பத்திர நிதி வழக்கமான புதைபடிவ எரிபொருள் திட்டங்களுக்கு திசைதிருப்பப்படுவதை இது தடுக்கிறது.",
        "India issued its first tranche of Sovereign Green Bonds in early 2023.",
        "2023 ஆம் ஆண்டின் தொடக்கத்தில் இந்தியா தனது முதல் இறையாண்மை பசுமைப் பத்திரங்களை வெளியிட்டது."
    ),
    # 55
    (
        "Audit of National Highways Toll Plazas and Concessions",
        "What did the CAG highlight regarding toll fee collections beyond the concession recovery period in its highway audits?",
        "NHAI continued collecting full toll rates at certain plazas instead of reducing fees to 40% after capital recovery",
        "மூலதனச் செலவு மீட்கப்பட்ட பிறகு சுங்கக் கட்டணத்தை 40%-ஆகக் குறைக்காமல் முழு கட்டணத்தையும் NHAI தொடர்ந்து வசூலித்ததை சுட்டிக்காட்டியது",
        "Under National Highways Fee Rules 2008, toll fee must drop to 40% after recovery of capital cost.",
        "2008 தேசிய நெடுஞ்சாலை கட்டண விதிகளின் கீழ் மூலதன செலவு மீட்கப்பட்ட பின் கட்டணம் 40%-ஆகக் குறைய வேண்டும்.",
        "CAG's 2023 performance report on NHAI Bharatmala project led to massive public debates.",
        "பாரத்மாலா திட்டம் மீதான சி.ஏ.ஜியின் 2023 அறிக்கை பெரும் மக்கள் விவாதங்களுக்கு வழிவகுத்தது."
    ),
    # 56
    (
        "Audit of PM SVANidhi Scheme",
        "What is the focus of CAG's audit on the PM Street Vendor's AtmaNirbhar Nidhi (PM SVANidhi) scheme?",
        "Verifies non-performing asset (NPA) rates, timely release of interest subsidies, and digital transaction cash-back credits",
        "வாராக் கடன் (NPA) விகிதங்கள், வட்டி மானியம் சரியான நேரத்தில் வழங்கப்படுவது மற்றும் டிஜிட்டல் பண திரும்பப் பெறுதல்களை சரிபார்க்கிறது",
        "Micro-credit welfare schemes undergo automated data matching to evaluate loan recovery.",
        "நுண்கடன் நலத்திட்டங்கள் கடன் வசூலை மதிப்பிடுவதற்காக தானியங்கி தரவு ஒப்பீட்டிற்கு உட்படுத்தப்படுகின்றன.",
        "Aadhaar authentication prevents multiple loans to non-existent vendors.",
        "ஆதார் சரிபார்ப்பு இல்லாத விற்பனையாளர்களுக்கு பல கடன்கள் வழங்கப்படுவதைத் தடுக்கிறது."
    ),
    # 57
    (
        "Audit of Defence Offset Contracts",
        "What major shortfall was highlighted by the CAG in its performance audit of defence offset contracts?",
        "Foreign defence vendors failed to discharge mandatory offset obligations to invest 30-50% in Indian aerospace companies",
        "வெளிநாட்டு பாதுகாப்பு நிறுவனங்கள் இந்திய விண்வெளித் துறையில் 30-50% முதலீடு செய்ய வேண்டிய ஆஃப்செட் கடமைகளை நிறைவேற்றத் தவறியதை சுட்டிக்காட்டியது",
        "Defence Procurement Procedure (DPP) mandates offset investments in high-value military deals.",
        "உயர் மதிப்புள்ள ராணுவ ஒப்பந்தங்களில் ஆஃப்செட் முதலீடுகளை பாதுகாப்பு கொள்முதல் நடைமுறை கட்டாயமாக்குகிறது.",
        "CAG recommended imposing financial penalties and vendor debarment for offset defaults.",
        "ஆஃப்செட் கடமைகளை மீறும் நிறுவனங்களுக்கு நிதி அபராதம் விதிக்க சி.ஏ.ஜி பரிந்துரைத்தது."
    ),
    # 58
    (
        "Audit of University Grants Commission (UGC) Grants",
        "What does the CAG scrutinize during the audit of central grants disbursed by the UGC to universities?",
        "Whether general development assistance was released without obtaining Utilization Certificates for earlier grants",
        "முந்தைய மானியங்களுக்கான பயன்பாட்டுச் சான்றிதழ்களைப் பெறாமல் புதிய வளர்ச்சி உதவிகள் விடுவிக்கப்பட்டதா என ஆராய்கிறது",
        "Rule 238 of General Financial Rules (GFR) forbids releasing grants if previous UCs are overdue.",
        "GFR விதி 238 முந்தைய சான்றிதழ்கள் நிலுவையில் இருக்கும் போது புதிய மானியங்களை விடுவிப்பதைத் தடை செய்கிறது.",
        "Unadjusted UC pendency running into thousands of crores is a recurring CAG audit finding.",
        "ஆயிரக்கணக்கான கோடி ரூபாய் பயன்பாட்டு சான்றிதழ்கள் நிலுவையில் இருப்பது அடிக்கடி சுட்டிக்காட்டப்படும் தணிக்கைக் குறிப்பாகும்."
    ),
    # 59
    (
        "Audit of Judicial Infrastructure Grants",
        "In its performance audit of the Centrally Sponsored Scheme for Judicial Infrastructure, what did the CAG flag?",
        "Substantial central funds remained unutilized in state treasuries while subordinate court complexes suffered infrastructure deficits",
        "கீழமை நீதிமன்றங்கள் உள்கட்டமைப்பு பற்றாக்குறையால் அவதிப்படும் வேளையில் மத்திய நிதி மாநில கருவூலங்களில் முடங்கிக் கிடந்ததை சுட்டிக்காட்டியது",
        "Courtroom construction and digital infrastructure require synchronized Centre-State fund matching.",
        "நீதிமன்ற அறைகள் கட்டுமானம் மற்றும் டிஜிட்டல் கட்டமைப்பு மத்திய-மாநில நிதி ஒருங்கிணைப்பைக் கோருகின்றன.",
        "CAG reports directly informed Supreme Court hearings on court infrastructure modernization.",
        "நீதிமன்ற உள்கட்டமைப்பு நவீனமயமாக்கல் குறித்த உச்ச நீதிமன்ற விசாரணைகளுக்கு சி.ஏ.ஜி அறிக்கைகள் உதவின."
    ),
    # 60
    (
        "Audit of Atomic Mineral Exploration",
        "How does the CAG assess expenditure incurred by the Atomic Minerals Directorate for Exploration and Research (AMD)?",
        "Evaluates core drilling meterage costs, exploration target achievements, and security of radioactive ore samples",
        "ஆழ்துளை துளையிடும் செலவுகள், ஆய்வு இலக்கு அடைவுகள் மற்றும் கதிரியக்க தாது மாதிரிகளின் பாதுகாப்பை மதிப்பிடுகிறது",
        "Strategic uranium and thorium exploration accounts are audited under specialized security safeguards.",
        "யுரேனியம் மற்றும் தோரியம் ஆய்வு கணக்குகள் சிறப்பு பாதுகாப்பு நெறிமுறைகளின் கீழ் தணிக்கை செய்யப்படுகின்றன.",
        "CAG scrutinizes mineral extraction royalty agreements between AMD and State Governments.",
        "AMD மற்றும் மாநில அரசுகளுக்கு இடையேயான கனிம உரிமைத்தொகை ஒப்பந்தங்களை சி.ஏ.ஜி ஆய்வு செய்கிறது."
    ),
    # 61
    (
        "Audit of Central Drugs Standard Control Organisation (CDSCO)",
        "What was a critical finding in CAG's audit of drug regulation by CDSCO?",
        "Shortage of drug inspectors, inadequate testing laboratories, and delays in testing imported drug batches",
        "மருந்து ஆய்வாளர்கள் பற்றாக்குறை, போதிய பரிசோதனை ஆய்வகங்கள் இல்லாமை மற்றும் இறக்குமதி மருந்துகளைப் பரிசோதிப்பதில் தாமதம்",
        "Public health regulatory audits evaluate whether enforcement mechanisms prevent counterfeit medicines.",
        "போலி மருந்துகளைத் தடுக்கும் அமலாக்க வழிமுறைகள் செயல்படுகின்றனவா என்பதை பொது சுகாதார தணிக்கை மதிப்பிடுகிறது.",
        "CAG audits recommend setting up NABL-accredited testing facilities at major sea and air ports.",
        "முக்கிய துறைமுகங்கள் மற்றும் விமான நிலையங்களில் அங்கீகரிக்கப்பட்ட ஆய்வகங்களை அமைக்க சி.ஏ.ஜி பரிந்துரைத்தது."
    ),
    # 62
    (
        "Audit of Border Roads Organisation (BRO)",
        "In performance audits of strategic border road projects, what does the CAG primarily identify as the root cause of delays?",
        "Delays in environmental clearances, protracted land acquisition, and unsuitability of heavy rock-cutting machinery",
        "சுற்றுச்சூழல் அனுமதிகளில் தாமதம், நிலம் கையகப்படுத்துதல் தாமதம் மற்றும் பாறை உடைக்கும் இயந்திரங்களின் பொருத்தமின்மை",
        "Strategic border infrastructure along China and Pakistan borders is audited under the Ministry of Defence umbrella.",
        "சீனா மற்றும் பாகிஸ்தான் எல்லைகளில் உள்ள உத்திசார் உள்கட்டமைப்பு பாதுகாப்பு அமைச்சகத்தின் கீழ் தணிக்கை செய்யப்படுகிறது.",
        "CAG audits helped streamline procurement powers delegated to BRO Border Commanders.",
        "BRO தளபதிகளுக்கு வழங்கப்பட்ட கொள்முதல் அதிகாரங்களை நெறிப்படுத்த சி.ஏ.ஜி தணிக்கைகள் உதவின."
    ),
    # 63
    (
        "Audit of Special Assistance to States for Capital Investment (SASCI)",
        "How does the CAG audit the 50-year interest-free loans granted to States under SASCI?",
        "Verifies that loans were utilized strictly for capital expenditure and not diverted to meet revenue deficits or salaries",
        "கடன்கள் மூலதனச் செலவுகளுக்கு மட்டுமே பயன்படுத்தப்பட்டனவா மற்றும் வருவாய்ப் பற்றாக்குறை அல்லது ஊதியங்களுக்கு திருப்பப்படவில்லை என்பதை சரிபார்க்கிறது",
        "Capital loan assistance is untied but conditional on avoiding revenue expenditure substitution.",
        "மூலதனக் கடன் உதவி நிபந்தனைக்குட்பட்டது மற்றும் வருவாய் செலவுகளுக்குப் பயன்படுத்துவது தடைசெய்யப்பட்டுள்ளது.",
        "State Finance Accounts detail individual drawdowns and asset creations under this scheme.",
        "மாநில நிதிக் கணக்குகள் இத்திட்டத்தின் கீழ் பெறப்பட்ட கடன்கள் மற்றும் உருவாக்கப்பட்ட சொத்துக்களை விவரிக்கின்றன."
    ),
    # 64
    (
        "Audit of Archaeological Survey of India (ASI) Monuments",
        "What was the main systemic failure revealed in CAG's performance audit on the preservation of national monuments by ASI?",
        "Loss of traceable coordinates of numerous protected monuments due to rapid unauthorized urban encroachments",
        "வேகமான நகர்ப்புற ஆக்கிரமிப்புகள் காரணமாக பாதுகாக்கப்பட்ட பல நினைவுச் சின்னங்களின் அமைவிடம் காணாமல் போனது",
        "Preservation audits check compliance with the Ancient Monuments and Archaeological Sites and Remains Act 1958.",
        "பண்டைய நினைவுச் சின்னங்கள் சட்டம் 1958-ன் இணக்கத்தை இந்த தணிக்கை சரிபார்க்கிறது.",
        "CAG recommended physical satellite mapping and geo-fencing of all Centrally Protected Monuments.",
        "அனைத்து பாதுகாக்கப்பட்ட நினைவுச் சின்னங்களையும் செயற்கைக்கோள் வரைபடம் மூலம் புவி-வேலி அமைக்க சி.ஏ.ஜி பரிந்துரைத்தது."
    ),
    # 65
    (
        "Audit of Inland Water Transport Subsidies",
        "What does the CAG verify in the freight subsidy claims submitted by national waterway cargo operators?",
        "Bills of lading, weighbridge receipts, and verified vessel AIS satellite tracking records",
        "சரக்கு ஏற்றுமதி ரசீதுகள், எடை மேடை சீட்டுகள் மற்றும் கப்பலின் AIS செயற்கைக்கோள் கண்காணிப்பு பதிவுகள்",
        "Subsidies disbursed to promote inland water cargo require cross-verification with port gate logs.",
        "உள்நாட்டு நீர்வழி போக்குவரத்தை ஊக்குவிக்க வழங்கப்படும் மானியங்கள் துறைமுக பதிவேடுகளுடன் ஒப்பிடப்பட வேண்டும்.",
        "Prevents paper freight movements designed to siphon off environmental logistics subsidies.",
        "சுற்றுச்சூழல் தளவாட மானியங்களை முறைகேடாகப் பெற போலியாக காகிதத்தில் சரக்கு போக்குவரத்து காட்டப்படுவதை இது தடுக்கிறது."
    ),
    # 66
    (
        "Audit of Civil Aviation Security Fee (ASF)",
        "How does the CAG audit the collection and disbursement of Aviation Security Fee collected from airline passengers?",
        "Ensures funds collected by airlines are deposited into a dedicated escrow account used strictly for CISF airport security deployment",
        "பயணிகளிடமிருந்து வசூலிக்கப்படும் கட்டணம் CISF விமான நிலைய பாதுகாப்பிற்கு மட்டுமே பயன்படுத்தப்படும் பிரத்யேக கணக்கில் சேருவதை உறுதி செய்கிறது",
        "Passenger-funded security cesses cannot be appropriated into the general commercial revenues of airport operators.",
        "பயணிகள் செலுத்தும் பாதுகாப்புக் கட்டணத்தை விமான நிலைய நிறுவனங்கள் தங்கள் வணிக வருவாயாக மாற்ற முடியாது.",
        "Scrutinizes whether non-aeronautical revenue subsidizes CISF operational costs.",
        "CISF இயக்கச் செலவுகளுக்கு கட்டண நிதி முறையாக வழங்கப்படுகிறதா என்பதை தணிக்கை ஆராய்கிறது."
    ),
    # 67
    (
        "Audit of National Pension System (NPS) Central Recordkeeping",
        "What does the CAG audit verify regarding government matching contributions under NPS?",
        "Timely credit of the employer's 14% matching contribution and employee 10% deduction into CRA PRAN accounts",
        "அரசின் 14% பங்கு மற்றும் ஊழியரின் 10% பிடித்தம் உரிய காலத்தில் PRAN கணக்குகளில் வரவு வைக்கப்படுவதை சரிபார்க்கிறது",
        "Delays by drawing and disbursing officers (DDOs) cause investment market opportunity losses to employees.",
        "DDO அதிகாரிகள் தாமதம் செய்தால் ஊழியர்களுக்கு முதலீட்டு சந்தை வாய்ப்பு இழப்பு ஏற்படுகிறது.",
        "CAG reports mandate payment of penal interest to employees for departmental contribution delays.",
        "துறைசார் தாமதங்களுக்கு ஊழியர்களுக்கு அபராத வட்டி வழங்க சி.ஏ.ஜி அறிக்கைகள் உத்தரவிடுகின்றன."
    ),
    # 68
    (
        "Audit of Inland Container Freight Stations (CFSs)",
        "What is the focus of CAG's audit on private Container Freight Stations operating under customs bonding?",
        "Verification of customs duty recovery on long-uncleared uncleared air/sea cargo and prevention of pilferage",
        "நீண்ட காலமாக விடுவிக்கப்படாத சரக்குகள் மீதான சுங்க வரி மீட்பு மற்றும் திருட்டைத் தடுத்தல்",
        "Customs bonding requires private operators to execute surety bonds guaranteeing statutory duties.",
        "தனியார் நிறுவனங்கள் சட்டப்பூர்வ வரிகளுக்கு உத்தரவாதம் அளிக்கும் பிணைப் பத்திரங்களை சமர்ப்பிக்க வேண்டும்.",
        "CAG audits led to auction of unclaimed container cargo stranded for over five years.",
        "ஐந்து ஆண்டுகளுக்கும் மேலாக முடங்கிக் கிடந்த உரிமைகோரப்படாத கொள்கலன்களை ஏலம் விட சி.ஏ.ஜி தணிக்கை வழிவகுத்தது."
    ),
    # 69
    (
        "Audit of Micro, Small and Medium Enterprises (MSME) Credit Guarantees",
        "What does the CAG audit scrutinize in the functioning of the CGTMSE trust?",
        "Settlement ratio of default claims, prudential guarantee reserve adequacy, and verification of underlying loan assets",
        "வாராக் கடன் கோரிக்கைகளின் தீர்வு விகிதம், இருப்பு நிதியின் போதுமான தன்மை மற்றும் அடிப்படைக் கடன் சொத்துக்களின் சரிபார்ப்பு",
        "Credit guarantee trusts operate on government seed capital provided from the Consolidated Fund of India.",
        "கடன் உத்தரவாத அறக்கட்டளைகள் இந்தியத் திரட்டப்பட்ட நிதியிலிருந்து வழங்கப்படும் அரசு மூலதனத்தில் இயங்குகின்றன.",
        "Ensures banks do not claim guarantee payouts for recklessly disbursed unsecured advances.",
        "பொறுப்பற்ற முறையில் வழங்கப்பட்ட கடன்களுக்கு வங்கிகள் உத்தரவாத இழப்பீட்டைப் பெறுவதை இது தடுக்கிறது."
    ),
    # 70
    (
        "Audit of National Mission for Clean Ganga (NMCG)",
        "In its performance audit of Namami Gange, what was a key infrastructure bottleneck highlighted by the CAG?",
        "Under-utilization of constructed Sewage Treatment Plants (STPs) due to incomplete trunk sewer pipeline networks",
        "முழுமையடையாத கழிவுநீர் குழாய் இணைப்பு காரணமாக கட்டப்பட்ட கழிவுநீர் சுத்திகரிப்பு நிலையங்கள் (STPs) முழுமையாகப் பயன்படுத்தப்படாதது",
        "Clean Ganga audit evaluates whether pollution load reduction targets were actually achieved at river discharge points.",
        "ஆற்றில் கலக்கும் கழிவுநீரின் அளவை குறைக்கும் இலக்குகள் எட்டப்பட்டனவா என்பதை கங்கை தணிக்கை மதிப்பிடுகிறது.",
        "CAG revealed that many STPs were operating at less than 50% of installed capacity.",
        "பல சுத்திகரிப்பு நிலையங்கள் தங்களது திறனில் 50%-க்கும் குறைவாகவே இயங்குவதை சி.ஏ.ஜி சுட்டிக்காட்டியது."
    ),
    # 71
    (
        "Audit of Indian Railways Scrap Disposal",
        "What is the primary compliance check in CAG's audit of railway scrap metal auctions?",
        "Adherence to e-auction reserve prices, physical weighbridge reconciliations, and prevention of cartel bidding",
        "மின்-ஏல அடிப்படை விலை நிர்ணயம், எடை மேடை பதிவுகள் மற்றும் ஏலதாரர்களின் கூட்டு முறைகேடுகளைத் தடுத்தல்",
        "Scrap sales constitute a major source of non-fare revenue for the Indian Railways exchequer.",
        "பழைய இரும்பு விற்பனை ரயில்வே கருவூலத்திற்கு ஒரு முக்கிய கட்டணமில்லா வருவாய் ஆதாரமாகும்.",
        "Discrepancies between surveyed scrap quantity and actual lifted weight are flagged by the CAG.",
        "மதிப்பிடப்பட்ட பழைய இரும்பு அளவிற்கும் தூக்கப்பட்ட உண்மையான எடைக்கும் உள்ள முரண்பாடுகளை சி.ஏ.ஜி சுட்டிக்காட்டுகிறது."
    ),
    # 72
    (
        "Audit of Sagarmala Port-Led Industrialization",
        "What did the CAG highlight in its review of coastal economic zones under Sagarmala?",
        "Slow land acquisition by maritime States and sluggish investment realization in coastal industrial clusters",
        "கடலோர மாநிலங்களால் நிலம் கையகப்படுத்துவதில் தாமதம் மற்றும் தொழில்துறை மண்டலங்களில் மெதுவான முதலீட்டு வரவு",
        "Sagarmala aims to reduce logistics costs through coastal shipping and port-rail connectivity.",
        "சாகர்மாலா திட்டம் கடலோர கப்பல் போக்குவரத்து மூலம் சரக்கு தளவாட செலவைக் குறைக்க முயல்கிறது.",
        "CAG performance reports recommended prioritization of multimodal rail-port freight corridors.",
        "ரயில்-துறைமுக பன்முக சரக்குப் போக்குவரத்து வழித்தடங்களுக்கு முன்னுரிமை அளிக்க சி.ஏ.ஜி பரிந்துரைத்தது."
    ),
    # 73
    (
        "Audit of Central Public Procurement Portal (CPPP)",
        "What does the CAG verify in automated IT audits of the Central Public Procurement Portal?",
        "Tender submission timestamp integrity, fairness in bid opening workflows, and detection of single-vendor collusion",
        "டெண்டர் சமர்ப்பிப்பு நேர முத்திரை நேர்மை, ஏலத் திறப்பு நியாயம் மற்றும் ஒற்றை விற்பனையாளர் கூட்டு முறைகேடுகளைக் கண்டறிதல்",
        "Digital procurement systems are audited to ensure level playing fields for all commercial bidders.",
        "அனைத்து வணிக ஏலதாரர்களுக்கும் சமமான வாய்ப்பை உறுதி செய்ய டிஜிட்டல் கொள்முதல் முறைகள் தணிக்கை செய்யப்படுகின்றன.",
        "Algorithms analyze IP addresses and digital signatures to detect bid-rigging syndicates.",
        "ஏல முறைகேடுகளைக் கண்டறிய ஐபி முகவரிகள் மற்றும் டிஜிட்டல் கையொப்பங்களை தணிக்கை வழிமுறைகள் பகுப்பாய்வு செய்கின்றன."
    ),
    # 74
    (
        "Audit of Urea Subsidy Direct Transfers",
        "How does the CAG evaluate the efficacy of the direct subsidy transfer mechanism to fertilizer companies?",
        "Checks whether energy norms were updated and whether actual gas consumption matched declared plant efficiencies",
        "எரிசக்தி விதிமுறைகள் புதுப்பிக்கப்பட்டனவா மற்றும் உண்மையான எரிவாயு நுகர்வு ஆலை செயல்திறனுடன் பொருந்துகிறதா என சோதிக்கிறது",
        "Energy efficiency audits save thousands of crores in public urea production subsidies.",
        "எரிசக்தி திறன் தணிக்கைகள் பொது யூரியா உற்பத்தி மானியங்களில் ஆயிரக்கணக்கான கோடி ரூபாயை மிச்சப்படுத்துகின்றன.",
        "Urea plants with higher specific energy consumption face proportionate subsidy cutbacks.",
        "அதிக எரிசக்தியைப் பயன்படுத்தும் யூரியா ஆலைகள் விகிதாசார மானியக் குறைப்பை எதிர்கொள்கின்றன."
    ),
    # 75
    (
        "Audit of National Digital Health Mission (ABDM)",
        "What is the primary security audit benchmark applied by the CAG to the Ayushman Bharat Digital Mission platform?",
        "Adherence to ISO/IEC 27001 standards and patient health data privacy protection guidelines under DPDP Act",
        "ISO/IEC 27001 தரநிலைகள் மற்றும் DPDP சட்டத்தின் கீழ் நோயாளி சுகாதாரத் தரவு தனியுரிமை பாதுகாப்பு வழிகாட்டுதல்கள்",
        "Digital health registries containing citizen electronic health records require impenetrable cyber audits.",
        "குடிமக்களின் சுகாதார ஆவணங்களைக் கொண்ட டிஜிட்டல் தளங்கள் ஊடுருவ முடியாத இணைய தணிக்கையைக் கோருகின்றன.",
        "CAG evaluates third-party system integrations and Consent Manager architectures.",
        "மூன்றாம் தரப்பு அமைப்புகளின் ஒருங்கிணைப்பு மற்றும் ஒப்புதல் மேலாளர் கட்டமைப்பை சி.ஏ.ஜி மதிப்பீடு செய்கிறது."
    ),
    # 76
    (
        "Audit of Defence Ordnance Factories Corporatization",
        "What does the CAG audit in the newly formed seven Defence Public Sector Undertakings (DPSUs) created from OFB?",
        "Valuation of transferred fixed assets, working capital loans, order book execution, and production cost efficiency",
        "மாற்றப்பட்ட நிலையான சொத்துக்களின் மதிப்பீடு, நடைமுறை மூலதனக் கடன்கள் மற்றும் உற்பத்தி செலவுத் திறன்",
        "In 2021, the Ordnance Factory Board (OFB) was converted into 7 corporate entities audited under the Companies Act.",
        "2021-ல் ஆயுதத் தொழிற்சாலை வாரியம் நிறுவனங்கள் சட்டத்தின் கீழ் தணிக்கை செய்யப்படும் 7 பொதுத்துறை நிறுவனங்களாக மாற்றப்பட்டது.",
        "CAG conducts supplementary audit of all 7 new defence corporations under Section 19(1).",
        "அனைத்து 7 புதிய பாதுகாப்பு நிறுவனங்களையும் பிரிவு 19(1)-ன் கீழ் சி.ஏ.ஜி துணைத் தணிக்கை செய்கிறது."
    ),
    # 77
    (
        "Audit of Public Distribution System (PDS) End-to-End Automation",
        "What did the CAG evaluate in the rollout of Point of Sale (ePoS) devices across Fair Price Shops?",
        "Network connectivity downtimes, biometric failure handling mechanisms, and genuine beneficiary grievance redresals",
        "நெட்வொர்க் இணைப்பு முடக்கம், கைரேகை சரிபார்ப்பு தோல்விகளை கையாளும் முறை மற்றும் பயனாளிகள் குறைதீர்ப்பு",
        "Ensures automated ration distribution does not inadvertently exclude vulnerable elderly citizens.",
        "தானியங்கி ரேஷன் விநியோகம் முதியோரை திட்டத்திலிருந்து தற்செயலாக ஒதுக்கிவிடாமல் இருப்பதை உறுதி செய்கிறது.",
        "CAG recommended fallback offline OTP or nominee authorization protocols.",
        "ஆஃப்லைன் OTP அல்லது பிரதிநிதி அங்கீகார நெறிமுறைகளைப் பின்பற்ற சி.ஏ.ஜி பரிந்துரைத்தது."
    ),
    # 78
    (
        "Audit of Coastal Security Infrastructure",
        "In its performance audit of the Coastal Security Scheme, what major vulnerability did the CAG flag?",
        "Non-operational interceptor speedboats due to fuel budget deficits and delayed construction of coastal police stations",
        "எரிபொருள் பட்ஜெட் பற்றாக்குறையால் இயங்காத அதிவேகப் படகுகள் மற்றும் கடலோர காவல் நிலையங்கள் கட்டுமானத்தில் தாமதம்",
        "Coastal police infrastructure is jointly funded by MHA and coastal State Governments.",
        "கடலோர காவல் நிலைய உள்கட்டமைப்பு மத்திய உள்துறை மற்றும் கடலோர மாநிலங்களால் கூட்டாக நிதியளிக்கப்படுகிறது.",
        "Audit followed up on post-26/11 maritime counter-terrorism recommendations.",
        "மும்பை 26/11 தாக்குதலுக்குப் பிந்தைய கடல்சார் பயங்கரவாத எதிர்ப்புப் பரிந்துரைகளை இந்த தணிக்கை ஆய்வு செய்தது."
    ),
    # 79
    (
        "Audit of Central University Faculty Recruitment",
        "What does the CAG verify in compliance audits of faculty appointments in Central Universities?",
        "Adherence to statutory reservation rosters for SC, ST, OBC, and EWS categories as per UGC regulations",
        "UGC விதிமுறைகளின்படி எஸ்சி, எஸ்டி, ஓபிசி மற்றும் EWS பிரிவினருக்கான சட்டப்பூர்வ இடஒதுக்கீட்டுப் பதிவேடுகளைப் பின்பற்றுதல்",
        "Statutory reservation roster non-compliance is treated as an illegal employment appointment.",
        "சட்டப்பூர்வ இடஒதுக்கீட்டுப் பதிவேட்டைப் பின்பற்றாதது சட்டவிரோத பணி நியமனமாகக் கருதப்படுகிறது.",
        "Universities are questioned for keeping backlog reserved vacancies unfilled indefinitely.",
        "இடஒதுக்கீட்டுப் பின்னடைவு காலியிடங்களை நிரப்பாமல் வைத்திருக்கும் பல்கலைக்கழகங்களை சி.ஏ.ஜி கேள்வி கேட்கிறது."
    ),
    # 80
    (
        "Audit of Solar Park Infrastructure",
        "What did the CAG scrutinize in the implementation of the Ultra Mega Renewable Energy Power Parks scheme?",
        "Delay in external power transmission system (ISTS) commissioning causing idle solar generation capacity",
        "வெளிப்புற மின் பகிர்மான கட்டமைப்பு (ISTS) அமைப்பதில் தாமதத்தால் சூரிய மின் உற்பத்தி திறன் முடங்கியதை சுட்டிக்காட்டியது",
        "Solar generation assets cannot supply power without synchronized green energy transmission corridors.",
        "பசுமை மின் பகிர்மான வழித்தடங்கள் இன்றி சூரிய மின் உற்பத்தி நிலையங்களால் மின்சாரத்தை விநியோகிக்க முடியாது.",
        "CAG exposed heavy fixed deemed generation charges paid to private developers without receiving power.",
        "மின்சாரம் பெறாமலேயே தனியார் நிறுவனங்களுக்கு நிலையான கட்டணம் செலுத்தப்பட்டதை சி.ஏ.ஜி வெளிப்படுத்தியது."
    ),
    # 81
    (
        "Audit of Flood Management Programme (FMP)",
        "What was the primary observation of the CAG in its nationwide audit of flood management and forecasting?",
        "Deficit of telemetry automatic water-level recorders and acute shortages of river embankment maintenance funds",
        "தானியங்கி நீர்மட்ட அளவீட்டு கருவிகள் பற்றாக்குறை மற்றும் நதிக்கரை தடுப்புச்சுவர் பராமரிப்பு நிதி பற்றாக்குறை",
        "Central Water Commission (CWC) flood forecasting networks are audited under the Ministry of Jal Shakti.",
        "மத்திய நீர் ஆணையத்தின் (CWC) வெள்ள முன்னறிவிப்பு நெட்வொர்க் ஜல் சக்தி அமைச்சகத்தின் கீழ் தணிக்கை செய்யப்படுகிறது.",
        "Delays in executing critical flood wall projects exacerbated recurring monsoon flood losses.",
        "வெள்ளத் தடுப்பு சுவர் திட்டங்களில் ஏற்பட்ட தாமதங்கள் பருவமழை வெள்ள இழப்புகளை அதிகரித்தன."
    ),
    # 82
    (
        "Audit of National Rail Safety Fund (Rashtriya Rail Sanraksha Kosh)",
        "What did the CAG expose in its performance audit of the RRSK non-lapsable safety fund?",
        "Diversion of dedicated railway safety funds for non-safety amenities like footboards and official furniture",
        "ரயில்வே பாதுகாப்பு நிதியை காலணிகள், தளவாடங்கள் போன்ற பாதுகாப்பு சாராத பிற செலவுகளுக்கு திசைதிருப்பியதை வெளிப்படுத்தியது",
        "RRSK was created with a corpus of Rs. 1 lakh crore over five years exclusively for critical safety renewals.",
        "ரயில்வே பாதுகாப்பு பணிகளுக்காக மட்டுமே ஐந்து ஆண்டுகளில் ரூ. 1 லட்சம் கோடி நிதியுடன் RRSK உருவாக்கப்பட்டது.",
        "Track renewals and electronic interlocking signaling were neglected in favor of cosmetic amenities.",
        "அழகுபடுத்தும் செலவுகளுக்காக தண்டவாள புதுப்பித்தல் மற்றும் எலக்ட்ரானிக் இன்டர்லாக்கிங் சிக்னல் பணிகள் புறக்கணிக்கப்பட்டன."
    ),
    # 83
    (
        "Audit of Deep Sea Fishing Subsidies",
        "What does the CAG verify in the audit of deep-sea fishing vessel conversion subsidies under Blue Economy?",
        "Installation of statutory satellite transponders, valid maritime merchant shipping registration, and traditional crew composition",
        "சட்டப்பூர்வ செயற்கைக்கோள் டிரான்ஸ்பாண்டர் பொருத்துதல், கப்பல் பதிவு மற்றும் பாரம்பரிய மீனவர் குழு அமைப்பு",
        "Promotes transition of traditional fishermen away from overcrowded bottom-trawling coastal waters.",
        "பாரம்பரிய மீனவர்கள் கடலோர தரைமட்ட வலை மீன்பிடிப்பிலிருந்து ஆழ்கடல் மீன்பிடிப்பிற்கு மாறுவதை இது ஊக்குவிக்கிறது.",
        "Ensures subsidized deep sea vessels do not illegally trawl within territorial territorial waters.",
        "மானியம் பெற்ற ஆழ்கடல் படகுகள் கடலோரப் பகுதியில் சட்டவிரோதமாக மீன்பிடிப்பதைத் தடுக்கிறது."
    ),
    # 84
    (
        "Audit of National Apprenticeship Promotion Scheme (NAPS)",
        "What did the CAG scrutinize regarding employer claims under NAPS?",
        "Verification of actual apprentice stipend disbursements through Aadhaar-seeded bank accounts before releasing government subsidy",
        "அரசு மானியத்தை விடுவிப்பதற்கு முன் ஆதார் இணைக்கப்பட்ட வங்கிக் கணக்குகள் மூலம் தொழிற்பழகுநர் உதவித்தொகை வழங்கப்பட்டதை சரிபார்த்தல்",
        "Prevents private industrial establishments from submitting inflated dummy apprentice claims.",
        "தனியார் தொழிற்கூடங்கள் போலி தொழிற்பழகுநர் பட்டியலை சமர்ப்பித்து மானியம் பெறுவதை இது தடுக்கிறது.",
        "Apprenticeship training must conform to statutory National Council for Vocational Training curricula.",
        "தொழிற்பழகுநர் பயிற்சி சட்டப்பூர்வ NCVT பாடத்திட்டத்தின்படி அமைய வேண்டும்."
    ),
    # 85
    (
        "Audit of National Highway Land Acquisition Delays",
        "What did the CAG identify as a primary cause of cost escalation in NHAI highway widening projects?",
        "Award of construction tenders to EPC contractors before achieving 80% physical possession of land as required by rules",
        "விதிகளின்படி தேவையான 80% நில உடமை பெறப்படுவதற்கு முன்பே EPC ஒப்பந்தக்காரர்களுக்கு டெண்டர்களை வழங்கியதால் செலவு அதிகரித்தது",
        "Contractors claim heavy idle machinery and labor idling claims against NHAI when land is unavailable.",
        "நிலம் கிடைக்காத போது ஒப்பந்தக்காரர்கள் NHAI மீது பெரும் இழப்பீட்டுத் தொகையைக் கோருகின்றனர்.",
        "CAG recommended strictly enforcing the 80% encumbrance-free land possession threshold before awarding bids.",
        "டெண்டர் வழங்குவதற்கு முன் 80% வில்லங்கமில்லா நில உடமை பெறுவதை கட்டாயமாக்க சி.ஏ.ஜி பரிந்துரைத்தது."
    ),
    # 86
    (
        "Audit of Civil Hospital Infection Control Measures",
        "What did the CAG evaluate in performance audits of district hospitals across States?",
        "Biomedical waste management compliance, availability of piped oxygen at all beds, and infection control protocols",
        "உயிரி மருத்துவக் கழிவு மேலாண்மை இணக்கம், அனைத்து படுக்கைகளிலும் குழாய் ஆக்ஸிஜன் இருப்பு மற்றும் தொற்று கட்டுப்பாட்டு நெறிமுறைகள்",
        "Health audits check compliance with Biomedical Waste Management Rules 2016.",
        "சுகாதாரத் தணிக்கைகள் 2016 உயிரி மருத்துவக் கழிவு மேலாண்மை விதிகளின் இணக்கத்தை சரிபார்க்கின்றன.",
        "Unsegregated infectious waste disposal was flagged across multiple state government hospitals.",
        "பிரித்தெடுக்கப்படாத தொற்று கழிவுகள் அகற்றப்படுவதை பல மாநில அரசு மருத்துவமனைகளில் சி.ஏ.ஜி சுட்டிக்காட்டியது."
    ),
    # 87
    (
        "Audit of PM Formalisation of Micro Food Processing Enterprises (PMFME)",
        "What does the CAG audit test in seed capital disbursements to Self Help Groups under PMFME?",
        "Verification of functional food processing equipment purchase and recovery from group common revolving funds",
        "செயல்பாட்டில் உள்ள உணவு பதப்படுத்தும் உபகரணங்கள் வாங்குதல் மற்றும் சுழல் நிதியிலிருந்து திரும்பப் பெறுவதை சரிபார்த்தல்",
        "One District One Product (ODOP) focus requires processing aligned with notified agricultural crops.",
        "ஒரு மாவட்டம் ஒரு தயாரிப்பு (ODOP) என்பது அறிவிக்கப்பட்ட பயிர்களுடன் பதப்படுத்துதலை இணைக்கிறது.",
        "Audit verifies that seed capital is not diverted for personal domestic consumption by SHG members.",
        "சுயஉதவிக் குழு உறுப்பினர்கள் மூலதன நிதியை குடும்ப தனிப்பட்ட செலவுகளுக்கு மாற்றாமல் இருப்பதை தணிக்கை உறுதி செய்கிறது."
    ),
    # 88
    (
        "Audit of Metro Rail System Concessions",
        "In its performance audit of urban Metro Rail projects, what did the CAG observe regarding ridership projections?",
        "Actual ridership achieved was less than 25% to 35% of DPR projections, causing heavy operational cash losses",
        "உண்மையான பயணிகளின் எண்ணிக்கை திட்ட மதிப்பீட்டில் 25% முதல் 35% மட்டுமே இருந்ததால் பெரும் இயக்க இழப்புகள் ஏற்பட்டன",
        "Inflated Detailed Project Report (DPR) passenger projections distort financial internal rate of return (FIRR) models.",
        "மிகைப்படுத்தப்பட்ட திட்ட மதிப்பீட்டு பயணிகள் எண்ணிக்கை நிதி வருவாய் மாதிரிகளை சிதைக்கிறது.",
        "CAG recommended realistic multimodal fare integration with city bus systems to bolster ridership.",
        "பயணிகள் எண்ணிக்கையை அதிகரிக்க நகரப் பேருந்துகளுடன் பன்முக கட்டண ஒருங்கிணைப்பை சி.ஏ.ஜி பரிந்துரைத்தது."
    ),
    # 89
    (
        "Audit of Pradhan Mantri Gram Sadak Yojana (PMGSY)",
        "What did the CAG verify in laboratory testing of road pavement quality under PMGSY?",
        "Compliance with bitumen thickness specifications, core compaction tests, and five-year maintenance performance",
        "தார் தடிமன் விவரக்குறிப்புகள், கோர் சுருக்க சோதனைகள் மற்றும் ஐந்தாண்டு பராமரிப்பு செயல்திறன் இணக்கம்",
        "National Quality Monitors (NQMs) and State Quality Monitors (SQMs) testing logs are scrutinized by the CAG.",
        "தேசிய மற்றும் மாநில தரக் கண்காணிப்பாளர்களின் பரிசோதனைப் பதிவேடுகளை சி.ஏ.ஜி தீவிரமாக ஆய்வு செய்கிறது.",
        "Contractors failing 5-year maintenance warranties are recommended for forfeiture of security deposits.",
        "ஐந்தாண்டு பராமரிப்பு உத்தரவாதத்தை மீறும் ஒப்பந்தக்காரர்களின் பாதுகாப்பு வைப்புத்தொகையைப் பறிமுதல் செய்ய பரிந்துரைக்கப்படுகிறது."
    ),
    # 90
    (
        "Audit of Electronic Toll Gate Software Integrity",
        "How did the CAG audit investigate potential toll plaza revenue leaks in national highway corridors?",
        "Performed data reconciliation comparing camera automated number plate recognition (ANPR) logs with FASTag payment records",
        "கேமரா தானியங்கி வாகன எண் தகடு (ANPR) பதிவுகளை பாஸ்டேக் கட்டணப் பதிவுகளுடன் ஒப்பிட்டுத் தணிக்கை செய்தது",
        "Unregistered vehicles passing through toll lanes without automated debits reveal toll plaza leakages.",
        "கட்டணப் பிடித்தம் இன்றி சுங்கச் சாவடிகளைக் கடக்கும் வாகனங்கள் வருவாய் கசிவை வெளிப்படுத்துகின்றன.",
        "Automated big data reconciliation algorithms in CDMA detect plaza software tampering.",
        "CDMA மையத்தின் தானியங்கி தரவு பகுப்பாய்வு வழிமுறைகள் சுங்க மென்பொருள் முறைகேடுகளைக் கண்டறிகின்றன."
    ),
    # 91
    (
        "Audit of National AYUSH Mission (NAM)",
        "What was a key finding in CAG's audit of AYUSH healthcare dispensaries and drug testing laboratories?",
        "Shortage of pharmacopoeial testing equipment and non-accreditation of state AYUSH manufacturing pharmacies",
        "மருந்தியல் பரிசோதனை உபகரணங்கள் பற்றாக்குறை மற்றும் மாநில அரசு ஆயுஷ் மருந்து தயாரிப்பு நிலையங்களின் அங்கீகாரமின்மை",
        "Quality standards under the Drugs and Cosmetics Act 1940 apply to traditional ayurvedic and siddha formulations.",
        "1940 மருந்துகள் மற்றும் அழகுசாதனப் பொருட்கள் சட்டம் பாரம்பரிய ஆயுர்வேத மற்றும் சித்த மருந்துகளுக்கும் பொருந்தும்.",
        "CAG urged establishing strict standardization protocols for heavy metal content in herbal medicines.",
        "மூலிகை மருந்துகளில் கன உலோகங்களின் அளவை முறைப்படுத்த கடுமையான தரநிலைகளை சி.ஏ.ஜி வலியுறுத்தியது."
    ),
    # 92
    (
        "Audit of National Rural Drinking Water Quality",
        "What did the CAG identify in the performance audit of rural water purification plants under Jal Jeevan Mission?",
        "High percentage of water quality testing laboratories lacked NABL accreditation and lacked reagents for heavy metal testing",
        "பெரும்பாலான குடிநீர் பரிசோதனை ஆய்வகங்கள் NABL அங்கீகாரம் பெறவில்லை மற்றும் கன உலோக பரிசோதனைக்கான ரசாயனங்கள் இல்லை",
        "Safe potable drinking water is a fundamental right under Article 21 enforced through audit verification.",
        "பாதுகாப்பான குடிநீர் என்பது சரத்து 21-ன் கீழ் அடிப்படை உரிமையாகும்; தணிக்கை இதனை உறுதி செய்கிறது.",
        "Water quality surveillance registers in Gram Panchayats are cross-checked with block laboratory entries.",
        "கிராம பஞ்சாயத்து குடிநீர் தரப் பதிவேடுகள் வட்டார ஆய்வகப் பதிவுகளுடன் ஒப்பிட்டு சரிபார்க்கப்படுகின்றன."
    ),
    # 93
    (
        "Audit of Dedicated Freight Corridor (DFC) Project",
        "What did the CAG scrutinize regarding the Western and Eastern Dedicated Freight Corridors?",
        "Coordination delays with zonal railways in constructing feeder link junctions and underutilization of electrified rolling stock",
        "இணைப்பு சந்திப்புகளை அமைப்பதில் மண்டல ரயில்வேயுடன் ஒருங்கிணைப்பு தாமதம் மற்றும் மின்சார ரயில் எஞ்சின் குறைவான பயன்பாடு",
        "Dedicated Freight Corridor Corporation of India Limited (DFCCIL) is a PSU audited under Section 19(1).",
        "இந்திய பிரத்யேக சரக்கு வழித்தட கழகம் (DFCCIL) பிரிவு 19(1)-ன் கீழ் தணிக்கை செய்யப்படும் பொதுத்துறை நிறுவனமாகும்.",
        "Assesses whether average freight train speed increased from 25 kmph to projected 60 kmph.",
        "சரக்கு ரயில்களின் சராசரி வேகம் மணிக்கு 25 கி.மீ-லிருந்து திட்டமிடப்பட்ட 60 கி.மீ-ஆக அதிகரித்ததா என ஆராய்கிறது."
    ),
    # 94
    (
        "Audit of High Altitude Clothing for Armed Forces",
        "What did the CAG expose in its audit of Extreme Cold Climate (ECC) clothing and gear for Siachen troops?",
        "Delays in procurement forcing troops to use recycled, obsolete clothing and critical shortages of snow goggles",
        "கொள்முதல் தாமதத்தால் வீரர்கள் பழைய காலாவதியான ஆடைகளைப் பயன்படுத்த நேரிட்டது மற்றும் பனி கண்ணாடிகள் பற்றாக்குறை",
        "Audits troops welfare procurement under the Master General of Sustenance (MGS) branch of the Indian Army.",
        "இந்திய ராணுவத்தின் தளவாட பராமரிப்புப் பிரிவின் கீழ் படை வீரர்கள் நலன் சார்ந்த கொள்முதல்களைத் தணிக்கை செய்கிறது.",
        "Procurement delays of up to four years for specialized winter boots were severely criticized.",
        "சிறப்பு குளிர்கால காலணிகள் கொள்முதலில் நான்கு ஆண்டுகள் வரை தாமதமானது கடுமையாக விமர்சிக்கப்பட்டது."
    ),
    # 95
    (
        "Audit of Inland Warehousing Facilities (CWC)",
        "What was the focus of CAG's audit on the Central Warehousing Corporation (CWC)?",
        "Capacity utilization of cold storages, revenue leakage in private bonded warehouse leases, and modern silo conversion rates",
        "குளிர்பதன கிடங்குகளின் பயன்பாட்டு திறன், தனியார் ஒப்பந்த குத்தகை வரி இழப்பு மற்றும் நவீன சேமிப்பு சிலோ மாற்ற விகிதங்கள்",
        "CWC is a statutory public corporation audited under its founding statute and Section 19(2).",
        "மத்திய சேமிப்புக் கிடங்கு கழகம் (CWC) அதன் சட்டம் மற்றும் பிரிவு 19(2)-ன் கீழ் தணிக்கை செய்யப்படுகிறது.",
        "CAG flagged high transit spillage and grain dampness damages during monsoon storage.",
        "பருவமழைக் காலத்தில் தானியங்கள் நனைந்து சேதமடைவதையும் போக்குவரத்து இழப்புகளையும் சி.ஏ.ஜி சுட்டிக்காட்டியது."
    ),
    # 96
    (
        "Audit of PM eBus Sewa Deployment",
        "What is the primary operational check in CAG's audit of public-private partnership electric bus concessions?",
        "Verification of actual operated bus-kilometer logs, charging infrastructure readiness, and viability gap fund disbursements",
        "இயக்கப்பட்ட உண்மையான பேருந்து-கிலோமீட்டர் பதிவுகள், சார்ஜிங் கட்டமைப்பு தயார்நிலை மற்றும் நிதி இடைவெளி மானிய விநியோகம்",
        "Electric bus concessions operate on Gross Cost Contract (GCC) models where operators are paid per kilometer.",
        "மின்சார பேருந்து ஒப்பந்தங்கள் ஒரு கிலோமீட்டருக்கு கட்டணம் செலுத்தும் மொத்த செலவு ஒப்பந்த (GCC) மாதிரியில் இயங்குகின்றன.",
        "Ensures bus operators are not paid for unoperated scheduled trips.",
        "இயக்கப்படாத அட்டவணை பயணங்களுக்கு பேருந்து நிறுவனங்களுக்கு பணம் வழங்கப்படாமல் இருப்பதை இது உறுதி செய்கிறது."
    ),
    # 97
    (
        "Audit of Direct Tax Appeals and Pendency",
        "What did the CAG expose in its performance audit of the Income Tax Appellate mechanism?",
        "Hundreds of thousands of crores blocked in prolonged departmental disputes due to non-filing of appeals within limitation periods",
        "காலக்கெடுவிற்குள் மேல்முறையீடு செய்யாததால் நீண்ட கால துறைசார் வழக்குகளில் பல லட்சம் கோடி ரூபாய் வரி முடங்கிக் கிடப்பது",
        "Direct tax receipt audit verifies efficiency of Dispute Resolution Panels and CIT (Appeals).",
        "நேரடி வரி வரவுத் தணிக்கை மேல்முறையீட்டு ஆணையர்கள் மற்றும் சர்ச்சை தீர்வு குழுக்களின் செயல்திறனை சரிபார்க்கிறது.",
        "CAG urged the Central Board of Direct Taxes (CBDT) to adopt standard litigation management software.",
        "வழக்குகளை நிர்வகிக்க நிலையான மென்பொருளைப் பயன்படுத்த நேரடி வரிகள் வாரியத்திற்கு (CBDT) சி.ஏ.ஜி வலியுறுத்தியது."
    ),
    # 98
    (
        "Audit of Plastic Waste Management Rules Compliance",
        "In its performance audit of plastic waste management, what did the CAG observe regarding Extended Producer Responsibility (EPR)?",
        "Absence of authentic audit trails for EPR certificates traded by brand owners and lack of recycling data verification",
        "நிறுவனங்களால் வாங்கப்படும் EPR சான்றிதழ்களுக்கான உண்மையான தணிக்கை தடங்கள் இல்லாமை மற்றும் மறுசுழற்சி தரவு சரிபார்ப்பு குறைபாடு",
        "CPCB centralized EPR portal is audited by the CAG to eliminate fraudulent plastic credit trading.",
        "போலி பிளாஸ்டிக் வரவு வர்த்தகத்தைத் தடுக்க மத்திய மாசுக் கட்டுப்பாட்டு வாரியத்தின் EPR தளத்தை சி.ஏ.ஜி தணிக்கை செய்கிறது.",
        "Unregulated single-use plastic manufacturing units operating without consent were identified.",
        "அனுமதியின்றி இயங்கும் முறைசாரா ஒருமுறை பயன்படுத்தும் பிளாஸ்டிக் உற்பத்தி ஆலைகளை தணிக்கை அடையாளம் காட்டியது."
    ),
    # 99
    (
        "Audit of National Apprenticeship Training Scheme for Engineering Graduates",
        "What did the CAG verify in the stipend subsidies reimbursed to commercial enterprises under NATS?",
        "Matching student enrolment on the national portal with institutional biometric attendance and direct DBT bank receipts",
        "தேசிய தளத்தில் மாணவர் பதிவு, கல்வி நிறுவன கைரேகை வருகைப் பதிவு மற்றும் நேரடி DBT வங்கி ரசீதுகளை ஒப்பிட்டு சரிபார்த்தல்",
        "Administered under the Ministry of Education, NATS provides on-the-job industrial engineering training.",
        "கல்வி அமைச்சகத்தின் கீழ் நிர்வகிக்கப்படும் NATS பொறியியல் மாணவர்களுக்கு களப் பயிற்சியை வழங்குகிறது.",
        "Prevents private commercial firms from claiming subsidized training stipends for regular permanent staff.",
        "வழக்கமான நிரந்தர ஊழியர்களுக்கு மானிய உதவித்தொகையை தனியார் நிறுவனங்கள் கோருவதை இது தடுக்கிறது."
    ),
    # 100
    (
        "Audit of Artificial Intelligence Applications in Audit (CDMA Innovation)",
        "What is the primary breakthrough achieved by the CAG's Centre for Data Management and Analytics (CDMA) in OIOS integration?",
        "Deployment of machine learning predictive algorithms for automated risk profiling, anomaly detection, and fraud pattern recognition",
        "தானியங்கி இடர் மதிப்பீடு, முரண்பாடுகளைக் கண்டறிதல் மற்றும் மோசடி முறைகளை அடையாளம் காண இயந்திர கற்றல் வழிமுறைகளைப் பயன்படுத்துதல்",
        "Pioneering digital audit evolution: CAG combines constitutional authority with 21st-century predictive data science.",
        "முன்னோடி டிஜிட்டல் தணிக்கை: சி.ஏ.ஜி தனது அரசியலமைப்பு அதிகாரத்தை 21ஆம் நூற்றாண்டின் முன்கணிப்பு தரவு அறிவியலுடன் இணைக்கிறது.",
        "India's digital audit algorithms were presented as a global benchmark at INTOSAI and ASOSAI conferences.",
        "இந்தியாவின் டிஜிட்டல் தணிக்கை வழிமுறைகள் INTOSAI மற்றும் ASOSAI சர்வதேச மாநாடுகளில் முன்மாதிரியாக முன்வைக்கப்பட்டன."
    )
]

def get_gt_part2_questions():
    questions = []
    for idx, item in enumerate(raw_gt_part2_items, start=51):
        qid = f"CAG_GT_{idx:03d}"
        topic, stem, correct_en, correct_ta, tip_en, tip_ta, fact_en, fact_ta = item
        
        opts = [
            (correct_en, correct_ta),
            ("Subject to summary approval by the Union Cabinet Secretary without legislative scrutiny", "சட்டமன்ற ஆய்வின்றி மத்திய அமைச்சரவைச் செயலாளரின் சுருக்கமான ஒப்புதலுக்கு உட்பட்டது"),
            ("Completely exempt from any form of constitutional audit under judicial doctrine", "நீதிமன்றக் கோட்பாட்டின் கீழ் எந்தவொரு அரசியலமைப்பு தணிக்கையிலிருந்தும் முற்றிலும் விலக்கு பெற்றது"),
            ("Audited exclusively by private commercial banks operating at district level", "மாவட்ட அளவில் இயங்கும் தனியார் வணிக வங்கிகளால் மட்டுமே தணிக்கை செய்யப்படுவது")
        ]
        correct_key = "A"
        
        why_en = {
            "A": f"Option A is correct: {correct_en}. This constitutional and statutory rule ensures public accountability.",
            "B": f"Option B ({opts[1][0]}) is incorrect in this constitutional context.",
            "C": f"Option C ({opts[2][0]}) is incorrect in this constitutional context.",
            "D": f"Option D ({opts[3][0]}) is incorrect in this constitutional context."
        }
        why_ta = {
            "A": f"தெரிவு A சரி: {correct_ta}. இந்த அரசியலமைப்பு மற்றும் சட்டப்பூர்வ விதி பொது நிதிப் பொறுப்புடைமையை உறுதி செய்கிறது.",
            "B": f"தெரிவு B ({opts[1][1]}) இந்த அரசியலமைப்புச் சூழலில் தவறானதாகும்.",
            "C": f"தெரிவு C ({opts[2][1]}) இந்த அரசியலமைப்புச் சூழலில் தவறானதாகும்.",
            "D": f"தெரிவு D ({opts[3][1]}) இந்த அரசியலமைப்புச் சூழலில் தவறானதாகும்."
        }
        
        q = make_cag_q(
            qid=qid,
            diff="Hard",
            qtype="Single Choice",
            subtopic=topic,
            en_stem=f"{stem}",
            ta_stem=f"{stem}?",
            en_a=opts[0][0],
            ta_a=opts[0][1],
            en_b=opts[1][0],
            ta_b=opts[1][1],
            en_c=opts[2][0],
            ta_c=opts[2][1],
            en_d=opts[3][0],
            ta_d=opts[3][1],
            correct_key=correct_key,
            exp_en=f"{correct_en}.\nThis standard procedural practice protects financial accountability in public governance.",
            exp_ta=f"{correct_ta}.\nஇந்த நடைமுறை பொது நிர்வாகத்தில் நிதிப் பொறுப்புடைமையைப் பாதுகாக்கிறது.",
            why_a_en=why_en["A"],
            why_a_ta=why_ta["A"],
            why_b_en=why_en["B"],
            why_b_ta=why_ta["B"],
            why_c_en=why_en["C"],
            why_c_ta=why_ta["C"],
            why_d_en=why_en["D"],
            why_d_ta=why_ta["D"],
            tip_en=tip_en,
            tip_ta=tip_ta,
            fact_en=fact_en,
            fact_ta=fact_ta,
            tags=["polity", "comptroller_and_auditor_general", "grand_test", topic.lower().replace(" ", "_")]
        )
        questions.append(q)
    return questions

if __name__ == "__main__":
    qs = get_gt_part2_questions()
    print(f"Generated {len(qs)} questions for CAG GT Part 2.")
