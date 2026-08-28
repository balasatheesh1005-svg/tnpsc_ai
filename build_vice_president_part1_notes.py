import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

print("==================================================")
print("BUILDING VICE-PRESIDENT NOTES — PART 1")
print("==================================================")

part1_data = {
  "meta": {
    "topic_id": "polity_vice_president_part_1",
    "repository_id": "polity_vice_president",
    "display_title": "Vice-President – Part 1",
    "part": 1,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "Vice-President of India",
    "language": "English + Tamil"
  },
  "metadata": {
    "topic_id": "polity_vice_president_part_1",
    "repository_id": "polity_vice_president",
    "display_title": "Vice-President – Part 1",
    "part": 1,
    "total_parts": 3,
    "subject": "polity",
    "chapter": "Vice-President of India",
    "language": "English + Tamil"
  },
  "keywords": [
    "Vice-President of India",
    "Article 63",
    "Article 64",
    "Article 65",
    "Article 66",
    "Article 67",
    "Article 68",
    "Article 69",
    "Article 70",
    "Article 71",
    "Electoral College",
    "Single Transferable Vote",
    "Ex-officio Chairman",
    "Rajya Sabha Qualification",
    "TNPSC Polity"
  ],
  "learning_outcomes": {
    "Understand": {
      "en": [
        "Master the constitutional position of the Vice-President under Article 63 as the second highest office in India.",
        "Understand the Electoral College composition under Article 66 (Elected + Nominated MPs; No State MLAs).",
        "Differentiate between President's weighted vote-value formula and Vice-President's equal MP vote value system.",
        "Learn qualifications (Rajya Sabha eligibility, 35 years age) and oath (Article 69 administered by President).",
        "Distinguish between Presidential Impeachment (Art 61) and Vice-President Removal (Art 67b) foundation."
      ],
      "ta": [
        "உறுப்பு 63-ன் கீழ் இந்தியாவின் இரண்டாவது மிக உயர்ந்த அரசியலமைப்பு பதவியான துணைக் குடியரசுத் தலைவரின் நிலையைத் தெரிந்துகொள்ளுதல்.",
        "உறுப்பு 66-ன் கீழ் வாக்காளர் குழுவின் அமைப்பைப் புரிந்துகொள்ளுதல் (தேர்ந்தெடுக்கப்பட்ட + நியமன எம்பிக்கள்; மாநில எம்.எல்.ஏக்கள் இல்லை).",
        "குடியரசுத் தலைவரின் எடையுள்ள வாக்கு மதிப்பு முறைக்கும் துணைக் குடியரசுத் தலைவரின் சமமான வாக்கு மதிப்பு முறைக்கும் இடையிலான வேறுபாட்டைப் புரிந்துகொள்ளுதல்.",
        "தகுதிகள் (மாநிலங்களவை உறுப்பினர் தகுதி, 35 வயது) மற்றும் பதவிப் பிரமாணம் (உறுப்பு 69 - குடியரசுத் தலைவரால் வழங்கப்படுவது) பற்றிக் கற்றல்.",
        "குடியரசுத் தலைவர் பதவி நீக்கம் (உறுப்பு 61) மற்றும் துணைக் குடியரசுத் தலைவர் பதவி நீக்கம் (உறுப்பு 67b) இடையிலான வேறுபாட்டைத் தெளிவுபடுத்துதல்."
      ]
    }
  },
  "subject": "polity",
  "topic": "Vice-President",
  "language": "English + Tamil",
  "ui_type": "standard_notes",
  "sections": [
    {
      "id": "sec_constitutional_position",
      "title_en": "1. Constitutional Position & Executive Role (Articles 63 & 64)",
      "title_ta": "1. அரசியலமைப்பு நிலை & நிர்வாகப் பொறுப்பு (உறுப்புகள் 63 & 64)",
      "type": "standard_topic"
    },
    {
      "id": "sec_articles_map",
      "title_en": "2. Comprehensive Articles Map (Articles 63 to 71)",
      "title_ta": "2. முழுமையான அரசியலமைப்பு விதிகள் வரைபடம் (உறுப்புகள் 63 முதல் 71)",
      "type": "standard_topic"
    },
    {
      "id": "sec_electoral_college",
      "title_en": "3. Election of Vice-President & Electoral College (Article 66)",
      "title_ta": "3. துணைக் குடியரசுத் தலைவர் தேர்தல் & வாக்காளர் குழு (உறுப்பு 66)",
      "type": "standard_topic"
    },
    {
      "id": "sec_election_method_vote_value",
      "title_en": "4. Election Method (STV) & Vote Value Principle",
      "title_ta": "4. தேர்தல் முறை (STV) & வாக்கு மதிப்புத் தத்துவம்",
      "type": "standard_topic"
    },
    {
      "id": "sec_qualifications",
      "title_en": "5. Qualifications for Office (Article 66(3))",
      "title_ta": "5. பதவிக்கான தகுதிகள் (உறுப்பு 66(3))",
      "type": "standard_topic"
    },
    {
      "id": "sec_conditions_of_office",
      "title_en": "6. Conditions of Office & Emoluments",
      "title_ta": "6. அலுவலக நிபந்தனைகள் & ஊதியங்கள்",
      "type": "standard_topic"
    },
    {
      "id": "sec_term_re-election",
      "title_en": "7. Term of Office & Re-election (Article 67)",
      "title_ta": "7. பதவிக் காலம் & மீண்டும் தேர்ந்தெடுக்கப்படுதல் (உறுப்பு 67)",
      "type": "standard_topic"
    },
    {
      "id": "sec_resignation_oath",
      "title_en": "8. Resignation & Oath of Office (Articles 67 & 69)",
      "title_ta": "8. ராஜினாமா & பதவிப் பிரமாணம் (உறுப்புகள் 67 & 69)",
      "type": "standard_topic"
    },
    {
      "id": "sec_removal_foundation",
      "title_en": "9. Removal Procedure Foundation (Article 67(b))",
      "title_ta": "9. பதவி நீக்க நடைமுறை அடிப்படை (உறுப்பு 67(b))",
      "type": "standard_topic"
    },
    {
      "id": "sec_vacancy_foundation",
      "title_en": "10. Vacancy in Office Foundation (Article 68 & 71)",
      "title_ta": "10. பதவிக் காலியிடம் & தேர்தல் தகராறுகள் (உறுப்புகள் 68 & 71)",
      "type": "standard_topic"
    },
    {
      "id": "comparison_tables",
      "title_en": "11. Mandatory Comparison Tables (Oppositional Analysis)",
      "title_ta": "11. கட்டாய ஒப்பீட்டு அட்டவணைகள் (எதிரெதிர் பகுப்பாய்வு)",
      "type": "comparison"
    },
    {
      "id": "mind_map",
      "title_en": "12. Mind Map & TNPSC Trap Points",
      "title_ta": "12. மன வரைபடம் & TNPSC தேர்வுப் பொறிகள்",
      "type": "mind_map"
    }
  ],
  "content": {
    "definition": {
      "en": "The Vice-President of India occupies the second highest constitutional office in the country, ranking next to the President of India in the official warrant of precedence. Modelled on the American Vice-Presidency, the office serves a dual constitutional role: as the Ex-officio Chairman of the Rajya Sabha (Council of States) under Article 64, and as the Acting President during casual vacancies in the presidency under Article 65.",
      "ta": "இந்தியத் துணைக் குடியரசுத் தலைவர் நாட்டின் இரண்டாவது மிக உயர்ந்த அரசியலமைப்புப் பதவியை வகிக்கிறார், அதிகாரப்பூர்வ முன்னுரிமைப் பட்டியலில் (Warrant of Precedence) குடியரசுத் தலைவருக்கு அடுத்தபடியாகப் பட்டியலிடப்படுகிறார். அமெரிக்கத் துணைக் குடியரசுத் தலைவர் பதவியின் மாதிரியில் வடிவமைக்கப்பட்ட இப்பதவி இரட்டை அரசியலமைப்புப் பொறுப்பைக் கொண்டுள்ளது: உறுப்பு 64-ன் கீழ் மாநிலங்களவையின் (Rajya Sabha) பதவிவழித் தலைவராகவும் (Ex-officio Chairman), உறுப்பு 65-ன் கீழ் குடியரசுத் தலைவர் பதவிக் காலியிடங்களின் போது செயல் குடியரசுத் தலைவராகவும் பணியாற்றுகிறார்."
    },
    "introduction": {
      "en": "Part V of the Constitution of India (The Union Chapter I - The Executive) lays down the provisions governing the Vice-President of India under Articles 63 to 71. The Indian Vice-President is elected indirectly by an Electoral College consisting of members of both Houses of Parliament. Unlike the President's election, State Legislative Assemblies do not participate in the Vice-President's election, but nominated MPs are fully entitled to vote.",
      "ta": "இந்திய அரசியலமைப்பின் பகுதி V (ஒன்றியம் அத்தியாயம் I - நிர்வாகம்) உறுப்புகள் 63 முதல் 71 வரை துணைக் குடியரசுத் தலைவர் தொடர்பான விதிகளைக் குறிப்பிடுகிறது. இந்தியத் துணைக் குடியரசுத் தலைவர் நாடாளுமன்றத்தின் இரு அவை உறுப்பினர்களையும் கொண்ட வாக்காளர் குழுவால் மறைமுகமாகத் தேர்ந்தெடுக்கப்படுகிறார். குடியரசுத் தலைவர் தேர்தலைப் போலன்றி, மாநில சட்டமன்ற உறுப்பினர்கள் இத்தேர்தலில் பங்கேற்பதில்லை, ஆனால் நாடாளுமன்ற நியமன உறுப்பினர்கள் வாக்களிக்கும் முழு உரிமை பெற்றவர்கள்."
    },
    "sec_constitutional_position": [
      {
        "title": "1. Constitutional Order of Precedence & Dual Role",
        "points": {
          "en": [
            "Second Highest Office: The Vice-President ranks 2nd in the official Indian Warrant of Precedence, immediately after the President of India.",
            "Union Executive Member: Under Part V Chapter 1, the Union Executive consists of the President, Vice-President, Prime Minister, Council of Ministers, and Attorney General of India.",
            "American Model Adaptation: The office is modelled on the lines of the US Vice-President, but with a crucial constitutional difference: when the US Vice-President succeeds to a vacant presidency, he becomes President for the remainder of the unexpired term; whereas the Indian Vice-President only acts as President for a maximum period of 6 months until a new President is elected.",
            "Dual Constitutional Capacity: Holds office primarily as Ex-officio Chairman of the Rajya Sabha (Article 64), receiving salary and allowances in that parliamentary capacity under the Second Schedule."
          ],
          "ta": [
            "இரண்டாவது மிக உயர்ந்த பதவி: அதிகாரப்பூர்வ முன்னுரிமைப் பட்டியலில் குடியரசுத் தலைவருக்கு அடுத்து 2-வது இடத்தில் துணைக் குடியரசுத் தலைவர் உள்ளார்.",
            "ஒன்றிய நிர்வாக உறுப்பினர்: பகுதி V அத்தியாயம் 1-ன் படி, ஒன்றிய நிர்வாகம் என்பது குடியரசுத் தலைவர், துணைக் குடியரசுத் தலைவர், பிரதமர், அமைச்சரவை மற்றும் இந்திய தலைமை வழக்கறிஞரைக் (AGI) கொண்டது.",
            "அமெரிக்க மாதிரி தழுவல்: அமெரிக்கத் துணைக் குடியரசுத் தலைவர் மாதிரியில் உருவாக்கப்பட்டாலும் ஒரு முக்கிய வேறுபாடு உள்ளது: அமெரிக்காவில் காலியிடம் ஏற்படும் போது துணைக் குடியரசுத் தலைவர் மீதமுள்ள முழு பதவிக் காலத்திற்கும் குடியரசுத் தலைவராகிறார்; ஆனால் இந்தியாவில் புதிய குடியரசுத் தலைவர் தேர்ந்தெடுக்கப்படும் வரை அதிகபட்சம் 6 மாதங்கள் மட்டுமே செயல் குடியரசுத் தலைவராக இருக்க முடியும்.",
            "இரட்டை அரசியலமைப்புத் திறன்: உறுப்பு 64-ன் கீழ் மாநிலங்களவையின் பதவிவழித் தலைவராகப் பணியாற்றி, இரண்டாம் அட்டவணையின் கீழ் அதற்கான ஊதியத்தைப் பெறுகிறார்."
          ]
        }
      }
    ],
    "sec_articles_map": [
      {
        "title": "2. Constitutional Articles Map (Articles 63 to 71)",
        "points": {
          "en": [
            "Article 63: The Vice-President of India — Mandates that 'There shall be a Vice-President of India'.",
            "Article 64: Vice-President to be Ex-Officio Chairman of Rajya Sabha — States that the Vice-President shall not hold any other office of profit.",
            "Article 65: Vice-President to Act as President or Discharge Functions — During casual vacancies (death, resignation, removal) or absence/illness of President.",
            "Article 66: Election of Vice-President — Specifies Electoral College, system of STV, and qualifications (35 years age, RS eligibility).",
            "Article 67: Term of Office of Vice-President — 5-year term, resignation to President, removal by Rajya Sabha resolution agreed by Lok Sabha.",
            "Article 68: Time of Holding Election to Fill Vacancy — Election to fill vacancy caused by expiration of term shall be completed before expiration.",
            "Article 69: Oath or Affirmation by Vice-President — Administered by the President of India or a person appointed by him.",
            "Article 70: Discharge of President's Functions in Other Contingencies — Parliament may make provision for contingencies not provided in Chapter I.",
            "Article 71: Election Disputes — Supreme Court has exclusive and final authority to inquire into and decide disputes relating to President/VP elections."
          ],
          "ta": [
            "உறுப்பு 63: இந்தியத் துணைக் குடியரசுத் தலைவர் — 'இந்தியாவிற்கு ஒரு துணைக் குடியரசுத் தலைவர் இருக்க வேண்டும்' எனக் குறிப்பிடுகிறது.",
            "உறுப்பு 64: மாநிலங்களவையின் பதவிவழித் தலைவர் — துணைக் குடியரசுத் தலைவர் வேறு ஆதாயம் தரும் பதவிகளை வகிக்கக் கூடாது.",
            "உறுப்பு 65: செயல் குடியரசுத் தலைவராகச் செயல்படுதல் — குடியரசுத் தலைவர் பதவிக் காலியிடம் அல்லது நோய்/வருகையின்மையின் போது செயல்படுதல்.",
            "உறுப்பு 66: துணைக் குடியரசுத் தலைவர் தேர்தல் — வாக்காளர் குழு, ஒற்றை மாற்று வாக்கு முறை மற்றும் தகுதிகளைக் (35 வயது, மாநிலங்களவை தகுதி) குறிப்பிடுகிறது.",
            "உறுப்பு 67: பதவிக் காலம் — 5 ஆண்டுகள், குடியரசுத் தலைவரிடம் ராஜினாமா, மாநிலங்களவைத் தீர்மானம் மூலம் பதவி நீக்கம்.",
            "உறுப்பு 68: காலியிடத் தேர்தல் காலம் — பதவிக் காலம் முடிவதற்கு முன்பே அடுத்த தேர்தலை நடத்தி முடிக்க வேண்டும்.",
            "உறுப்பு 69: பதவிப் பிரமாணம் — குடியரசுத் தலைவர் அல்லது அவரால் நியமிக்கப்பட்ட நபரால் வழங்கப்படுகிறது.",
            "உறுப்பு 70: இதர அவசர நிலைகளில் குடியரசுத் தலைவர் பணிகளைச் செய்தல் — அரசியலமைப்பில் குறிப்பிடப்படாத இதர சூழல்களுக்கு நாடாளுமன்றம் சட்டமியற்றலாம்.",
            "உறுப்பு 71: தேர்தல் தகராறுகள் — குடியரசுத் தலைவர் / துணைக் குடியரசுத் தலைவர் தேர்தல் தொடர்பான தகராறுகளை உச்ச நீதிமன்றம் மட்டுமே விசாரித்து இறுதித் தீர்ப்பு அளிக்கும்."
          ]
        }
      }
    ],
    "sec_electoral_college": [
      {
        "title": "3. Electoral College for Vice-President (Article 66(1))",
        "points": {
          "en": [
            "Composition: Consists of members of BOTH Houses of Parliament (Lok Sabha + Rajya Sabha) assembled at a joint meeting.",
            "INCLUSION of Nominated MPs: BOTH elected AND nominated members of Parliament are eligible to vote in the Vice-President's election.",
            "EXCLUSION of State Assemblies: Members of State Legislative Assemblies (MLAs) DO NOT participate in the Vice-President's election (unlike President's election).",
            "EXCLUSION of Legislative Councils: Members of State Legislative Councils (MLCs) are completely excluded.",
            "Rationale for Exclusion of States: Dr. B.R. Ambedkar explained that the President is the Head of State and his powers extend to administration of States; hence States participate. The Vice-President's normal function is to preside over Rajya Sabha; only rarely he acts as President for a short period."
          ],
          "ta": [
            "அமைப்பு: நாடாளுமன்றத்தின் இரு அவைகளின் (மக்களவை + மாநிலங்களவை) உறுப்பினர்களைக் கொண்ட கூட்டு அமைப்பாகும்.",
            "நியமன எம்பிக்கள் சேர்க்கை: தேர்ந்தெடுக்கப்பட்ட மற்றும் நியமன எம்பிக்கள் இருவருமே துணைக் குடியரசுத் தலைவர் தேர்தலில் வாக்களிக்கத் தகுதியுடையவர்கள்.",
            "மாநில சட்டமன்றங்கள் விலக்கு: மாநில சட்டமன்ற உறுப்பினர்கள் (MLAs) இத்தேர்தலில் பங்கேற்பதில்லை (குடியரசுத் தலைவர் தேர்தலிலிருந்து மாறுபட்டது).",
            "மாநில மேலவைகள் விலக்கு: மாநில மேலவை உறுப்பினர்கள் (MLCs) முற்றிலுமாக விலக்கப்பட்டுள்ளனர்.",
            "விலக்கிற்கான காரணம்: டாக்டர் பி.ஆர். அம்பேத்கர் விளக்கத்தின் படி, குடியரசுத் தலைவர் நாட்டின் தலைவர் என்பதால் மாநிலங்கள் பங்கேற்கின்றன. துணைக் குடியரசுத் தலைவரின் இயல்பான பணி மாநிலங்களவையை நடத்துவதே ஆகும்."
          ]
        }
      }
    ],
    "sec_election_method_vote_value": [
      {
        "title": "4. Method of Election & Equal Vote Value Principle",
        "points": {
          "en": [
            "Proportional Representation by STV: Elected by the system of proportional representation by means of the single transferable vote.",
            "Secret Ballot: Voting is conducted by secret ballot (Art 66(1)). Open ballot is prohibited.",
            "EQUAL MP VOTE VALUE: Unlike the Presidential election where MLAs and MPs have weighted vote values calculated using 1971 census population figures, EVERY MP IN THE VICE-PRESIDENT ELECTION HAS AN EQUAL VOTE VALUE OF EXACTLY 1.",
            "Quota Requirement: To win, a candidate must secure a fixed quota of votes (Quota = [Total Valid Votes / 2] + 1)."
          ],
          "ta": [
            "ஒற்றை மாற்று வாக்கு விகிதாச்சார பிரதிநிதித்துவம்: ஒற்றை மாற்று வாக்கு மூலம் விகிதாச்சார பிரதிநிதித்துவ முறையில் தேர்ந்தெடுக்கப்படுகிறார்.",
            "ரகசிய வாக்கெடுப்பு: வாக்கெடுப்பு ரகசிய முறையில் நடத்தப்படுகிறது (உறுப்பு 66(1)).",
            "சமமான வாக்கு மதிப்பு: குடியரசுத் தலைவர் தேர்தலில் 1971 மக்கள் தொகை அடிப்படையில் எடையுள்ள வாக்கு மதிப்பு கணக்கிடப்படும். ஆனால் துணைக் குடியரசுத் தலைவர் தேர்தலில் ஒவ்வொரு எம்பியின் வாக்கு மதிப்பும் சரியாக 1 (சமமானது).",
            "வாக்கு வரம்பு (Quota): வெற்றி பெற ஒரு வேட்பாளர் குறிப்பிட்ட வாக்கு வரம்பைப் பெற வேண்டும் (Quota = [மொத்த செல்லுபடியாகும் வாக்குகள் / 2] + 1)."
          ]
        }
      }
    ],
    "sec_qualifications": [
      {
        "title": "5. Qualifications for Election as Vice-President (Article 66(3))",
        "points": {
          "en": [
            "Citizenship: Must be a Citizen of India.",
            "Minimum Age: Must have completed 35 years of age.",
            "Rajya Sabha Qualification: Must be qualified for election as a member of the Council of States (Rajya Sabha). Note: President requires qualification for House of the People (Lok Sabha).",
            "Office of Profit Restriction: Must not hold any office of profit under the Government of India, State Government, or any local/other authority.",
            "Exempted Offices (Not Office of Profit): Sitting President, Sitting Vice-President, Governor of any State, and Union or State Minister are NOT considered holding an office of profit for contesting election."
          ],
          "ta": [
            "குடியுரிமை: இந்தியக் குடிமகனாக இருக்க வேண்டும்.",
            "குறைந்தபட்ச வயது: 35 வயது பூர்த்தியடைந்திருக்க வேண்டும்.",
            "மாநிலங்களவை தகுதி: மாநிலங்களவை (Rajya Sabha) உறுப்பினராவதற்கான தகுதியைப் பெற்றிருக்க வேண்டும். (குடியரசுத் தலைவர் மக்களவை தகுதி பெற வேண்டும்).",
            "ஆதாயம் தரும் பதவித் தடை: மத்திய, மாநில அல்லது உள்ளாட்சி அமைப்புகளில் ஆதாயம் தரும் பதவிகளை வகிக்கக் கூடாது.",
            "விலக்களிக்கப்பட்ட பதவிகள்: பதவியிலுள்ள குடியரசுத் தலைவர், துணைக் குடியரசுத் தலைவர், மாநில ஆளுநர் மற்றும் மத்திய/மாநில அமைச்சர்கள் பதவிகள் ஆதாயம் தரும் பதவிகளாகக் கருதப்படாது."
          ]
        }
      }
    ],
    "sec_conditions_of_office": [
      {
        "title": "6. Conditions of Office & Emoluments",
        "points": {
          "en": [
            "No Parliamentary / State Seat: Shall not be a member of either House of Parliament or State Legislature. If an MP or MLA is elected, he is deemed to have vacated his seat on the date he enters office.",
            "No Office of Profit: Shall not hold any other office of profit during his term.",
            "Salary Structure: The Constitution does not fix any salary for the Vice-President as such. He receives his regular salary in his capacity as Ex-Officio Chairman of Rajya Sabha (fixed by Parliament).",
            "Salary when Acting as President: When acting as President under Article 65, he does not perform duties of Chairman of Rajya Sabha and receives the salary and allowances of the President of India."
          ],
          "ta": [
            "நாடாளுமன்ற/சட்டமன்ற உறுப்பினர் பதவி இல்லை: நாடாளுமன்றம் அல்லது மாநில சட்டமன்ற உறுப்பினராக இருக்கக் கூடாது. தேர்ந்தெடுக்கப்பட்டால், பதவியேற்கும் நாளில் அப் பதவி காலியானதாகக் கருதப்படும்.",
            "ஆதாயம் தரும் பதவி இல்லை: பதவிக் காலத்தில் வேறு ஆதாயம் தரும் பதவிகளை வகிக்கக் கூடாது.",
            "ஊதிய அமைப்பு: துணைக் குடியரசுத் தலைவர் பதவிக்கு தனியாக ஊதியம் அரசியலமைப்பில் நிர்ணயிக்கப்படவில்லை. மாநிலங்களவை தலைவராக மட்டுமே ஊதியம் பெறுகிறார்.",
            "செயல் குடியரசுத் தலைவராக ஊதியம்: உறுப்பு 65-ன் கீழ் செயல் குடியரசுத் தலைவராகப் பணியாற்றும் போது, குடியரசுத் தலைவருக்கான ஊதியம் மற்றும் படிகளைப் பெறுகிறார் (மாநிலங்களவை தலைவராக ஊதியம் பெறமாட்டார்)."
          ]
        }
      }
    ],
    "sec_term_re-election": [
      {
        "title": "7. Term of Office & Eligibility for Re-election (Article 67)",
        "points": {
          "en": [
            "5-Year Term: Holds office for a term of 5 years from the date on which he enters upon his office.",
            "Continuation Until Successor Enters: Continues in office, notwithstanding the expiration of his term, until his successor enters upon his office (Article 67(c)).",
            "Re-election Eligibility: Eligible for re-election for any number of terms. Two Vice-Presidents have served two full terms: Dr. S. Radhakrishnan (1952–1962) and Mohammad Hamid Ansari (2007–2017).",
            "Resignation Letter: May resign his office by writing under his hand addressed to the PRESIDENT OF INDIA."
          ],
          "ta": [
            "5 ஆண்டுகள் பதவிக் காலம்: பதவியேற்ற நாளிலிருந்து 5 ஆண்டுகள் பதவியில் இருப்பார்.",
            "வாரிசு வரும் வரை தொடருதல்: 5 ஆண்டுகள் முடிந்தாலும், புதிய துணைக் குடியரசுத் தலைவர் பதவியேற்கும் வரை பதவியில் தொடருவார் (உறுப்பு 67(c)).",
            "மீண்டும் தேர்ந்தெடுக்கப்படும் தகுதி: எத்தனை முறை வேண்டுமானாலும் மீண்டும் தேர்ந்தெடுக்கப்படலாம். இருவர் இருமுறை பதவி வகித்துள்ளனர்: டாக்டர் எஸ். ராதாகிருஷ்ணன் (1952-1962) மற்றும் முகமது ஹமீத் அன்சாரி (2007-2017).",
            "ராஜினாமாக் கடிதம்: தனது கையொப்பமிட்ட ராஜினாமாக் கடிதத்தை இந்தியக் குடியரசுத் தலைவரிடம் வழங்க வேண்டும்."
          ]
        }
      }
    ],
    "sec_resignation_oath": [
      {
        "title": "8. Resignation & Oath of Office (Articles 67 & 69)",
        "points": {
          "en": [
            "Resignation Addressee: Resignation letter must be addressed to the President of India (Article 67(a)).",
            "Oath Administration (Article 69): Oath or affirmation is administered by the President of India, or some person appointed in that behalf by him.",
            "Text of Oath: Swears to bear true faith and allegiance to the Constitution of India as by law established and to faithfully discharge the duty upon which he is about to enter."
          ],
          "ta": [
            "ராஜினாமா பெறுநர்: ராஜினாமாக் கடிதம் இந்தியக் குடியரசுத் தலைவரிடம் வழங்கப்பட வேண்டும் (உறுப்பு 67(a)).",
            "பதவிப் பிரமாணம் (உறுப்பு 69): இந்தியக் குடியரசுத் தலைவர் அல்லது அவரால் நியமிக்கப்பட்ட நபரால் பதவிப் பிரமாணம் செய்து வைக்கப்படுகிறது.",
            "உறுதிமொழி உள்ளடக்கம்: இந்திய அரசியலமைப்பிற்கு உண்மையாகவும் விசுவாசமாகவும் இருப்பேன் என்றும் தனது கடமையைச் செவ்வனே செய்வேன் என்றும் உறுதிமொழி ஏற்கிறார்."
          ]
        }
      }
    ],
    "sec_removal_foundation": [
      {
        "title": "9. Removal Procedure Foundation (Article 67(b))",
        "points": {
          "en": [
            "No Formal Impeachment: The Vice-President is NOT removed by formal impeachment under Article 61 (which applies ONLY to the President).",
            "Rajya Sabha Resolution: Removal can be initiated ONLY in the Rajya Sabha by a resolution passed by an effective majority (majority of all the then members of the Rajya Sabha).",
            "Lok Sabha Agreement: Must be agreed to by the Lok Sabha by a simple majority.",
            "14 Days' Notice: No such resolution can be moved unless at least 14 days' advance notice has been given.",
            "No Specific Ground: The Constitution specifies NO GROUND for the removal of the Vice-President."
          ],
          "ta": [
            "அரசியலமைப்பு பதவி நீக்கம் (Impeachment) இல்லை: உறுப்பு 61-ன் கீழ் குடியரசுத் தலைவருக்குரிய பதவி நீக்க நடைமுறை துணைக் குடியரசுத் தலைவருக்குப் பொருந்தாது.",
            "மாநிலங்களவைத் தீர்மானம்: பதவி நீக்கத் தீர்மானம் மாநிலங்களவையில் மட்டுமே தொடங்கப்பட்டு, அன்றைய மொத்த உறுப்பினர்களின் பெரும்பான்மையால் (Effective Majority) நிறைவேற்றப்பட வேண்டும்.",
            "மக்களவை ஒப்புதல்: மக்களவையில் சாதாரண பெரும்பான்மையால் ஒப்புதல் பெறப்பட வேண்டும்.",
            "14 நாட்கள் முன்னறிவிப்பு: குறைந்தபட்சம் 14 நாட்களுக்கு முன் அறிவிப்பு வழங்கப்பட வேண்டும்.",
            "காரணம் குறிப்பிடப்படவில்லை: துணைக் குடியரசுத் தலைவரைப் பதவி நீக்கம் செய்வதற்கான எந்தவொரு காரணமும் அரசியலமைப்பில் குறிப்பிடப்படவில்லை."
          ]
        }
      }
    ],
    "sec_vacancy_foundation": [
      {
        "title": "10. Vacancy in Office Foundation (Articles 68 & 71)",
        "points": {
          "en": [
            "Causes of Vacancy: Expiration of 5-year term, resignation, removal by Parliament, death, or election declared void by Supreme Court.",
            "Regular Vacancy Election: Election to fill vacancy caused by expiration of term must be completed BEFORE the expiration of the term.",
            "Casual Vacancy Election: Election to fill a casual vacancy (death, resignation, removal) must be held 'as soon as possible' (no fixed 6-month limit specified in Art 68, unlike Art 62 for President).",
            "Full Term for Newly Elected: The newly elected Vice-President holds office for a full term of 5 years.",
            "Article 71 Disputes: Supreme Court has exclusive jurisdiction over all election disputes."
          ],
          "ta": [
            "காலியிடத்திற்கான காரணங்கள்: 5 ஆண்டுகள் பதவிக் காலம் முடிவடைதல், ராஜினாமா, பதவி நீக்கம், மரணம் அல்லது உச்ச நீதிமன்றத்தால் தேர்தல் செல்லாது என அறிவிக்கப்படுதல்.",
            "வழக்கமான காலியிடத் தேர்தல்: பதவிக் காலம் முடிவதற்கு முன்பே அடுத்த தேர்தலை நடத்தி முடிக்க வேண்டும்.",
            "அவசரக் காலியிடத் தேர்தல்: மரணம் அல்லது ராஜினாமாவால் ஏற்படும் காலியிடத்திற்கு 'যত விரைவில் சாத்தியமோ' தேர்தல் நடத்தப்பட வேண்டும் (குடியரசுத் தலைவரைப் போல 6 மாத வரம்பு உறுப்பு 68-ல் குறிப்பிடப்படவில்லை).",
            "புதிய உறுப்பினரின் பதவிக் காலம்: புதிதாகத் தேர்ந்தெடுக்கப்படும் துணைக் குடியரசுத் தலைவர் முழுமையாக 5 ஆண்டுகள் பதவி வகிப்பார்.",
            "உறுப்பு 71 தகராறுகள்: அனைத்துத் தேர்தல் தகராறுகளையும் உச்ச நீதிமன்றம் மட்டுமே விசாரிக்கும்."
          ]
        }
      }
    ],
    "comparison_tables": [
      {
        "id": "tbl_pres_vs_vp_electoral_college",
        "title_en": "1. President vs Vice-President Electoral College Comparison",
        "title_ta": "1. குடியரசுத் தலைவர் vs துணைக் குடியரசுத் தலைவர் வாக்காளர் குழு ஒப்பீடு",
        "headers_en": ["Dimension", "President's Electoral College (Article 54)", "Vice-President's Electoral College (Article 66)"],
        "headers_ta": ["அம்சம்", "குடியரசுத் தலைவர் வாக்காளர் குழு (உறுப்பு 54)", "துணைக் குடியரசுத் தலைவர் வாக்காளர் குழு (உறுப்பு 66)"],
        "rows_en": [
          ["Parliament Elected MPs", "Included (Lok Sabha + Rajya Sabha elected MPs)", "Included (Lok Sabha + Rajya Sabha elected MPs)"],
          ["Parliament Nominated MPs", "EXCLUDED (Cannot vote in election)", "INCLUDED (Elected + Nominated MPs can vote)"],
          ["State MLAs", "INCLUDED (Elected MLAs of all States)", "EXCLUDED (State MLAs do not participate)"],
          ["UT MLAs", "INCLUDED (Elected MLAs of Delhi, Puducherry & J&K)", "EXCLUDED (UT MLAs do not participate)"],
          ["State MLCs", "EXCLUDED (Legislative Council members excluded)", "EXCLUDED (Legislative Council members excluded)"]
        ],
        "rows_ta": [
          ["தேர்ந்தெடுக்கப்பட்ட எம்பிக்கள்", "சேர்க்கப்பட்டுள்ளனர் (மக்களவை + மாநிலங்களவை)", "சேர்க்கப்பட்டுள்ளனர் (மக்களவை + மாநிலங்களவை)"],
          ["நியமன எம்பிக்கள்", "விலக்கப்பட்டுள்ளனர் (வாக்களிக்க முடியாது)", "சேர்க்கப்பட்டுள்ளனர் (தேர்ந்தெடுக்கப்பட்ட + நியமன எம்பிக்கள்)"],
          ["மாநில எம்.எல்.ஏக்கள்", "சேர்க்கப்பட்டுள்ளனர் (அனைத்து மாநில எம்.எல்.ஏக்கள்)", "விலக்கப்பட்டுள்ளனர் (மாநில எம்.எல்.ஏக்கள் பங்கேற்பதில்லை)"],
          ["யூனியன் பிரதேச எம்.எல்.ஏக்கள்", "சேர்க்கப்பட்டுள்ளனர் (டெல்லி, புதுச்சேரி, ஜே&கே)", "விலக்கப்பட்டுள்ளனர் (பங்கேற்பதில்லை)"],
          ["மாநில மேலவை உறுப்பினர்கள்", "விலக்கப்பட்டுள்ளனர் (மேலவை உறுப்பினர்கள் இல்லை)", "விலக்கப்பட்டுள்ளனர் (மேலவை உறுப்பினர்கள் இல்லை)"]
        ]
      },
      {
        "id": "tbl_pres_vs_vp_qualification",
        "title_en": "2. President vs Vice-President Qualification Comparison",
        "title_ta": "2. குடியரசுத் தலைவர் vs துணைக் குடியரசுத் தலைவர் தகுதிகள் ஒப்பீடு",
        "headers_en": ["Qualification Parameter", "President of India (Article 58)", "Vice-President of India (Article 66(3))"],
        "headers_ta": ["தகுதிப் காரணி", "இந்தியக் குடியரசுத் தலைவர் (உறுப்பு 58)", "இந்தியத் துணைக் குடியரசுத் தலைவர் (உறுப்பு 66(3))"],
        "rows_en": [
          ["Citizenship", "Citizen of India", "Citizen of India"],
          ["Minimum Age", "35 Years", "35 Years"],
          ["Legislative House Eligibility", "Must be qualified for election to LOK SABHA", "Must be qualified for election to RAJYA SABHA"],
          ["Office of Profit", "Must not hold office of profit", "Must not hold office of profit"],
          ["Exempted Offices", "Sitting President, VP, Governor, Union/State Minister", "Sitting President, VP, Governor, Union/State Minister"]
        ],
        "rows_ta": [
          ["குடியுரிமை", "இந்தியக் குடிமகன்", "இந்தியக் குடிமகன்"],
          ["குறைந்தபட்ச வயது", "35 ஆண்டுகள்", "35 ஆண்டுகள்"],
          ["சட்டமன்ற அவைத் தகுதி", "மக்களவைக்கு (Lok Sabha) தேர்வாகும் தகுதி", "மாநிலங்களவைக்கு (Rajya Sabha) தேர்வாகும் தகுதி"],
          ["ஆதாயம் தரும் பதவி", "ஆதாயம் தரும் பதவி வகிக்கக் கூடாது", "ஆதாயம் தரும் பதவி வகிக்கக் கூடாது"],
          ["விலக்களிக்கப்பட்ட பதவிகள்", "குடியரசுத் தலைவர், VP, ஆளுநர், அமைச்சர்", "குடியரசுத் தலைவர், VP, ஆளுநர், அமைச்சர்"]
        ]
      },
      {
        "id": "tbl_pres_vs_vp_vote_value",
        "title_en": "3. President vs Vice-President Vote Value Comparison",
        "title_ta": "3. குடியரசுத் தலைவர் vs துணைக் குடியரசுத் தலைவர் வாக்கு மதிப்பு ஒப்பீடு",
        "headers_en": ["Vote Feature", "Presidential Election", "Vice-Presidential Election"],
        "headers_ta": ["வாக்கு அம்சம்", "குடியரசுத் தலைவர் தேர்தல்", "துணைக் குடியரசுத் தலைவர் தேர்தல்"],
        "rows_en": [
          ["MP Vote Value", "Weighted Value (Calculated based on total MLA vote values)", "EQUAL Vote Value (Every MP vote = 1)"],
          ["MLA Vote Value", "Weighted Value (Based on State 1971 Population / SLAs)", "NO MLA Vote (MLAs do not participate)"],
          ["Census Base Year", "1971 Census (Fixed until post-2026 census)", "Not Applicable (No population weighting used)"],
          ["Ballot System", "Secret Ballot with STV", "Secret Ballot with STV"]
        ],
        "rows_ta": [
          ["எம்பி வாக்கு மதிப்பு", "எடையுள்ள மதிப்பு (மொத்த எம்எல்ஏ வாக்குகள் அடிப்படையில்)", "சமமான வாக்கு மதிப்பு (ஒவ்வொரு எம்பி வாக்கு = 1)"],
          ["எம்எல்ஏ வாக்கு மதிப்பு", "எடையுள்ள மதிப்பு (1971 மக்கள் தொகை அடிப்படையில்)", "எம்எல்ஏ வாக்கு இல்லை (எம்எல்ஏக்கள் பங்கேற்பதில்லை)"],
          ["மக்கள் தொகை கணக்கெடுப்பு ஆண்டு", "1971 கணக்கெடுப்பு (2026 வரை நிலைநிறுத்தப்பட்டது)", "பொருந்தாது (மக்கள் தொகை எடை பயன்படுத்தப்படவில்லை)"],
          ["வாக்கெடுப்பு முறை", "ஒற்றை மாற்று வாக்கு ரகசிய வாக்கெடுப்பு", "ஒற்றை மாற்று வாக்கு ரகசிய வாக்கெடுப்பு"]
        ]
      },
      {
        "id": "tbl_pres_vs_vp_resignation",
        "title_en": "4. Resignation & Oath Administration Comparison",
        "title_ta": "4. ராஜினாமா & பதவிப் பிரமாண நிர்வாக ஒப்பீடு",
        "headers_en": ["Administrative Function", "President of India", "Vice-President of India"],
        "headers_ta": ["நிர்வாகப் பணி", "இந்தியக் குடியரசுத் தலைவர்", "இந்தியத் துணைக் குடியரசுத் தலைவர்"],
        "rows_en": [
          ["Resignation Addressed To", "VICE-PRESIDENT OF INDIA (Article 56)", "PRESIDENT OF INDIA (Article 67)"],
          ["Resignation Communication", "VP communicates it immediately to Speaker of LS", "President receives and accepts it"],
          ["Oath Administered By", "CHIEF JUSTICE OF INDIA (or Senior SC Judge) (Art 60)", "PRESIDENT OF INDIA (or person appointed) (Art 69)"],
          ["Oath Core Wording", "Preserve, Protect and Defend the Constitution", "Bear true faith and allegiance to the Constitution"]
        ],
        "rows_ta": [
          ["ராஜினாமாக் கடிதம் பெறுநர்", "இந்தியத் துணைக் குடியரசுத் தலைவர் (உறுப்பு 56)", "இந்தியக் குடியரசுத் தலைவர் (உறுப்பு 67)"],
          ["ராஜினாமா தகவல் பரிமாற்றம்", "VP உடனடியாக மக்களவை சபாநாயகருக்குத் தெரிவிப்பார்", "குடியரசுத் தலைவர் பெற்று ஏற்பார்"],
          ["பதவிப் பிரமாணம் வழங்குபவர்", "இந்திய தலைமை நீதிபதி (CJI) (உறுப்பு 60)", "இந்தியக் குடியரசுத் தலைவர் (உறுப்பு 69)"],
          ["உறுதிமொழி முக்கிய வார்த்தை", "அரசியலமைப்பைப் பேணிப் பாதுகாத்து அரணாக நிற்பேன்", "அரசியலமைப்பிற்கு உண்மையாகவும் விசுவாசமாகவும் இருப்பேன்"]
        ]
      },
      {
        "id": "tbl_pres_impeachment_vs_vp_removal_foundation",
        "title_en": "5. President Impeachment (Art 61) vs Vice-President Removal (Art 67b)",
        "title_ta": "5. குடியரசுத் தலைவர் பதவி நீக்கம் vs துணைக் குடியரசுத் தலைவர் பதவி நீக்கம்",
        "headers_en": ["Feature", "President Impeachment (Article 61)", "Vice-President Removal (Article 67(b))"],
        "headers_ta": ["அம்சம்", "குடியரசுத் தலைவர் பதவி நீக்கம் (உறுப்பு 61)", "துணைக் குடியரசுத் தலைவர் பதவி நீக்கம் (உறுப்பு 67(b))"],
        "rows_en": [
          ["Initiating House", "EITHER House of Parliament (Lok Sabha or Rajya Sabha)", "RAJYA SABHA ONLY (Must originate in RS)"],
          ["Ground Specified", "Violation of the Constitution (Only ground)", "NO Ground specified in the Constitution"],
          ["Notice Period", "14 Days' Notice in writing (1/4th members signed)", "14 Days' Notice in writing"],
          ["Passing Majority", "2/3rd TOTAL MEMBERSHIP of initiating & 2nd House", "Effective Majority in RS + Simple Majority in LS"],
          ["Participation of Nominated MPs", "Nominated MPs CAN vote", "Nominated MPs CAN vote"],
          ["Participation of State MLAs", "State MLAs DO NOT vote", "State MLAs DO NOT vote"]
        ],
        "rows_ta": [
          ["தொடங்கும் அவை", "நாடாளுமன்றத்தின் ஏதேனும் ஒரு அவை (LS அல்லது RS)", "மாநிலங்களவை மட்டுமே (Rajya Sabha)"],
          ["காரணம்", "அரசியலமைப்பை மீறுதல் (மட்டுமே)", "எந்தவொரு காரணமும் குறிப்பிடப்படவில்லை"],
          ["அறிவிப்பு காலம்", "14 நாட்கள் முன்னறிவிப்பு (1/4 எம்பிக்கள் கையொப்பம்)", "14 நாட்கள் முன்னறிவிப்பு"],
          ["நிறைவேற்றும் பெரும்பான்மை", "இரு அவைகளிலும் 2/3 பங்கு மொத்த உறுப்பினர் பெரும்பான்மை", "மாநிலங்களவையில் Effective Majority + மக்களவையில் Simple Majority"],
          ["நியமன எம்பிக்கள் பங்கேற்பு", "நியமன எம்பிக்கள் வாக்களிக்கலாம்", "நியமன எம்பிக்கள் வாக்களிக்கலாம்"],
          ["மாநில எம்எல்ஏக்கள் பங்கேற்பு", "மாநில எம்எல்ஏக்கள் வாக்களிக்க முடியாது", "மாநில எம்எல்ஏக்கள் வாக்களிக்க முடியாது"]
        ]
      },
      {
        "id": "tbl_indian_vp_vs_american_vp",
        "title_en": "6. Indian Vice-President vs American Vice-President Comparison",
        "title_ta": "6. இந்தியத் துணைக் குடியரசுத் தலைவர் vs அமெரிக்கத் துணைக் குடியரசுத் தலைவர் ஒப்பீடு",
        "headers_en": ["Comparison Dimension", "Indian Vice-President", "American Vice-President"],
        "headers_ta": ["ஒப்பீட்டுப் பரிமாணம்", "இந்தியத் துணைக் குடியரசுத் தலைவர்", "அமெரிக்கத் துணைக் குடியரசுத் தலைவர்"],
        "rows_en": [
          ["Succession to Vacant Presidency", "Acts as President ONLY until new President elected (Max 6 months)", "Becomes President for FULL REMAINING TERM of predecessor"],
          ["Presiding Officer Role", "Ex-Officio Chairman of Rajya Sabha", "Ex-Officio President of US Senate"],
          ["Casting Vote Power", "Possesses Casting Vote in Rajya Sabha", "Possesses Casting Vote in US Senate"],
          ["Constitutional Weight", "Described as 'His Superfluous Highness' due to lack of independent executive functions", "Significant political office with direct presidential succession power"]
        ],
        "rows_ta": [
          ["குடியரசுத் தலைவர் காலியிட வாரிசுரிமை", "புதிய தலைவர் தேர்வாகும் வரை மட்டுமே செயல் தலைவர் (அதிகபட்சம் 6 மாதங்கள்)", "முந்தைய தலைவரின் மீதமுள்ள முழு பதவிக் காலத்திற்கும் தலைவராகிறார்"],
          ["அவைத் தலைவர் பொறுப்பு", "மாநிலங்களவையின் பதவிவழித் தலைவர்", "அமெரிக்க செனட் அவையின் பதவிவழித் தலைவர்"],
          ["முடிவு வாக்கு (Casting Vote)", "மாநிலங்களவையில் முடிவு வாக்கு அளிக்கும் அதிகாரம் உண்டு", "அமெரிக்க செனட்டில் முடிவு வாக்கு அளிக்கும் அதிகாரம் உண்டு"],
          ["அரசியலமைப்பு எடை", "சுயாதீன நிர்வாக அதிகாரங்கள் இல்லாததால் 'அவசியமற்ற மேன்மைப் பதவி' எனக் குறிப்பிடப்படுகிறது", "நேரடி வாரிசுரிமை அதிகாரத்துடன் கூடிய சக்திவாய்ந்த பதவி"]
        ]
      }
    ],
    "comparison": [
      {
        "id": "tbl_pres_vs_vp_electoral_college",
        "title_en": "1. President vs Vice-President Electoral College Comparison",
        "title_ta": "1. குடியரசுத் தலைவர் vs துணைக் குடியரசுத் தலைவர் வாக்காளர் குழு ஒப்பீடு",
        "headers_en": ["Dimension", "President's Electoral College (Article 54)", "Vice-President's Electoral College (Article 66)"],
        "headers_ta": ["அம்சம்", "குடியரசுத் தலைவர் வாக்காளர் குழு (உறுப்பு 54)", "துணைக் குடியரசுத் தலைவர் வாக்காளர் குழு (உறுப்பு 66)"],
        "rows_en": [
          ["Parliament Elected MPs", "Included (Lok Sabha + Rajya Sabha elected MPs)", "Included (Lok Sabha + Rajya Sabha elected MPs)"],
          ["Parliament Nominated MPs", "EXCLUDED (Cannot vote in election)", "INCLUDED (Elected + Nominated MPs can vote)"],
          ["State MLAs", "INCLUDED (Elected MLAs of all States)", "EXCLUDED (State MLAs do not participate)"],
          ["UT MLAs", "INCLUDED (Elected MLAs of Delhi, Puducherry & J&K)", "EXCLUDED (UT MLAs do not participate)"],
          ["State MLCs", "EXCLUDED (Legislative Council members excluded)", "EXCLUDED (Legislative Council members excluded)"]
        ],
        "rows_ta": [
          ["தேர்ந்தெடுக்கப்பட்ட எம்பிக்கள்", "சேர்க்கப்பட்டுள்ளனர் (மக்களவை + மாநிலங்களவை)", "சேர்க்கப்பட்டுள்ளனர் (மக்களவை + மாநிலங்களவை)"],
          ["நியமன எம்பிக்கள்", "விலக்கப்பட்டுள்ளனர் (வாக்களிக்க முடியாது)", "சேர்க்கப்பட்டுள்ளனர் (தேர்ந்தெடுக்கப்பட்ட + நியமன எம்பிக்கள்)"],
          ["மாநில எம்.எல்.ஏக்கள்", "சேர்க்கப்பட்டுள்ளனர் (அனைத்து மாநில எம்.எல்.ஏக்கள்)", "விலக்கப்பட்டுள்ளனர் (மாநில எம்.எல்.ஏக்கள் பங்கேற்பதில்லை)"],
          ["யூனியன் பிரதேச எம்.எல்.ஏக்கள்", "சேர்க்கப்பட்டுள்ளனர் (டெல்லி, புதுச்சேரி, ஜே&கே)", "விலக்கப்பட்டுள்ளனர் (பங்கேற்பதில்லை)"],
          ["மாநில மேலவை உறுப்பினர்கள்", "விலக்கப்பட்டுள்ளனர் (மேலவை உறுப்பினர்கள் இல்லை)", "விலக்கப்பட்டுள்ளனர் (மேலவை உறுப்பினர்கள் இல்லை)"]
        ]
      },
      {
        "id": "tbl_pres_vs_vp_qualification",
        "title_en": "2. President vs Vice-President Qualification Comparison",
        "title_ta": "2. குடியரசுத் தலைவர் vs துணைக் குடியரசுத் தலைவர் தகுதிகள் ஒப்பீடு",
        "headers_en": ["Qualification Parameter", "President of India (Article 58)", "Vice-President of India (Article 66(3))"],
        "headers_ta": ["தகுதிப் காரணி", "இந்தியக் குடியரசுத் தலைவர் (உறுப்பு 58)", "இந்தியத் துணைக் குடியரசுத் தலைவர் (உறுப்பு 66(3))"],
        "rows_en": [
          ["Citizenship", "Citizen of India", "Citizen of India"],
          ["Minimum Age", "35 Years", "35 Years"],
          ["Legislative House Eligibility", "Must be qualified for election to LOK SABHA", "Must be qualified for election to RAJYA SABHA"],
          ["Office of Profit", "Must not hold office of profit", "Must not hold office of profit"],
          ["Exempted Offices", "Sitting President, VP, Governor, Union/State Minister", "Sitting President, VP, Governor, Union/State Minister"]
        ],
        "rows_ta": [
          ["குடியுரிமை", "இந்தியக் குடிமகன்", "இந்தியக் குடிமகன்"],
          ["குறைந்தபட்ச வயது", "35 ஆண்டுகள்", "35 ஆண்டுகள்"],
          ["சட்டமன்ற அவைத் தகுதி", "மக்களவைக்கு (Lok Sabha) தேர்வாகும் தகுதி", "மாநிலங்களவைக்கு (Rajya Sabha) தேர்வாகும் தகுதி"],
          ["ஆதாயம் தரும் பதவி", "ஆதாயம் தரும் பதவி வகிக்கக் கூடாது", "ஆதாயம் தரும் பதவி வகிக்கக் கூடாது"],
          ["விலக்களிக்கப்பட்ட பதவிகள்", "குடியரசுத் தலைவர், VP, ஆளுநர், அமைச்சர்", "குடியரசுத் தலைவர், VP, ஆளுநர், அமைச்சர்"]
        ]
      },
      {
        "id": "tbl_pres_vs_vp_vote_value",
        "title_en": "3. President vs Vice-President Vote Value Comparison",
        "title_ta": "3. குடியரசுத் தலைவர் vs துணைக் குடியரசுத் தலைவர் வாக்கு மதிப்பு ஒப்பீடு",
        "headers_en": ["Vote Feature", "Presidential Election", "Vice-Presidential Election"],
        "headers_ta": ["வாக்கு அம்சம்", "குடியரசுத் தலைவர் தேர்தல்", "துணைக் குடியரசுத் தலைவர் தேர்தல்"],
        "rows_en": [
          ["MP Vote Value", "Weighted Value (Calculated based on total MLA vote values)", "EQUAL Vote Value (Every MP vote = 1)"],
          ["MLA Vote Value", "Weighted Value (Based on State 1971 Population / SLAs)", "NO MLA Vote (MLAs do not participate)"],
          ["Census Base Year", "1971 Census (Fixed until post-2026 census)", "Not Applicable (No population weighting used)"],
          ["Ballot System", "Secret Ballot with STV", "Secret Ballot with STV"]
        ],
        "rows_ta": [
          ["எம்பி வாக்கு மதிப்பு", "எடையுள்ள மதிப்பு (மொத்த எம்எல்ஏ வாக்குகள் அடிப்படையில்)", "சமமான வாக்கு மதிப்பு (ஒவ்வொரு எம்பி வாக்கு = 1)"],
          ["எம்எல்ஏ வாக்கு மதிப்பு", "எடையுள்ள மதிப்பு (1971 மக்கள் தொகை அடிப்படையில்)", "எம்எல்ஏ வாக்கு இல்லை (எம்எல்ஏக்கள் பங்கேற்பதில்லை)"],
          ["மக்கள் தொகை கணக்கெடுப்பு ஆண்டு", "1971 கணக்கெடுப்பு (2026 வரை நிலைநிறுத்தப்பட்டது)", "பொருந்தாது (மக்கள் தொகை எடை பயன்படுத்தப்படவில்லை)"],
          ["வாக்கெடுப்பு முறை", "ஒற்றை மாற்று வாக்கு ரகசிய வாக்கெடுப்பு", "ஒற்றை மாற்று வாக்கு ரகசிய வாக்கெடுப்பு"]
        ]
      },
      {
        "id": "tbl_pres_vs_vp_resignation",
        "title_en": "4. Resignation & Oath Administration Comparison",
        "title_ta": "4. ராஜினாமா & பதவிப் பிரமாண நிர்வாக ஒப்பீடு",
        "headers_en": ["Administrative Function", "President of India", "Vice-President of India"],
        "headers_ta": ["நிர்வாகப் பணி", "இந்தியக் குடியரசுத் தலைவர்", "இந்தியத் துணைக் குடியரசுத் தலைவர்"],
        "rows_en": [
          ["Resignation Addressed To", "VICE-PRESIDENT OF INDIA (Article 56)", "PRESIDENT OF INDIA (Article 67)"],
          ["Resignation Communication", "VP communicates it immediately to Speaker of LS", "President receives and accepts it"],
          ["Oath Administered By", "CHIEF JUSTICE OF INDIA (or Senior SC Judge) (Art 60)", "PRESIDENT OF INDIA (or person appointed) (Art 69)"],
          ["Oath Core Wording", "Preserve, Protect and Defend the Constitution", "Bear true faith and allegiance to the Constitution"]
        ],
        "rows_ta": [
          ["ராஜினாமாக் கடிதம் பெறுநர்", "இந்தியத் துணைக் குடியரசுத் தலைவர் (உறுப்பு 56)", "இந்தியக் குடியரசுத் தலைவர் (உறுப்பு 67)"],
          ["ராஜினாமா தகவல் பரிமாற்றம்", "VP உடனடியாக மக்களவை சபாநாயகருக்குத் தெரிவிப்பார்", "குடியரசுத் தலைவர் பெற்று ஏற்பார்"],
          ["பதவிப் பிரமாணம் வழங்குபவர்", "இந்திய தலைமை நீதிபதி (CJI) (உறுப்பு 60)", "இந்தியக் குடியரசுத் தலைவர் (உறுப்பு 69)"],
          ["உறுதிமொழி முக்கிய வார்த்தை", "அரசியலமைப்பைப் பேணிப் பாதுகாத்து அரணாக நிற்பேன்", "அரசியலமைப்பிற்கு உண்மையாகவும் விசுவாசமாகவும் இருப்பேன்"]
        ]
      },
      {
        "id": "tbl_pres_impeachment_vs_vp_removal_foundation",
        "title_en": "5. President Impeachment (Art 61) vs Vice-President Removal (Art 67b)",
        "title_ta": "5. குடியரசுத் தலைவர் பதவி நீக்கம் vs துணைக் குடியரசுத் தலைவர் பதவி நீக்கம்",
        "headers_en": ["Feature", "President Impeachment (Article 61)", "Vice-President Removal (Article 67(b))"],
        "headers_ta": ["அம்சம்", "குடியரசுத் தலைவர் பதவி நீக்கம் (உறுப்பு 61)", "துணைக் குடியரசுத் தலைவர் பதவி நீக்கம் (உறுப்பு 67(b))"],
        "rows_en": [
          ["Initiating House", "EITHER House of Parliament (Lok Sabha or Rajya Sabha)", "RAJYA SABHA ONLY (Must originate in RS)"],
          ["Ground Specified", "Violation of the Constitution (Only ground)", "NO Ground specified in the Constitution"],
          ["Notice Period", "14 Days' Notice in writing (1/4th members signed)", "14 Days' Notice in writing"],
          ["Passing Majority", "2/3rd TOTAL MEMBERSHIP of initiating & 2nd House", "Effective Majority in RS + Simple Majority in LS"],
          ["Participation of Nominated MPs", "Nominated MPs CAN vote", "Nominated MPs CAN vote"],
          ["Participation of State MLAs", "State MLAs DO NOT vote", "State MLAs DO NOT vote"]
        ],
        "rows_ta": [
          ["தொடங்கும் அவை", "நாடாளுமன்றத்தின் ஏதேனும் ஒரு அவை (LS அல்லது RS)", "மாநிலங்களவை மட்டுமே (Rajya Sabha)"],
          ["காரணம்", "அரசியலமைப்பை மீறுதல் (மட்டுமே)", "எந்தவொரு காரணமும் குறிப்பிடப்படவில்லை"],
          ["அறிவிப்பு காலம்", "14 நாட்கள் முன்னறிவிப்பு (1/4 எம்பிக்கள் கையொப்பம்)", "14 நாட்கள் முன்னறிவிப்பு"],
          ["நிறைவேற்றும் பெரும்பான்மை", "இரு அவைகளிலும் 2/3 பங்கு மொத்த உறுப்பினர் பெரும்பான்மை", "மாநிலங்களவையில் Effective Majority + மக்களவையில் Simple Majority"],
          ["நியமன எம்பிக்கள் பங்கேற்பு", "நியமன எம்பிக்கள் வாக்களிக்கலாம்", "நியமன எம்பிக்கள் வாக்களிக்கலாம்"],
          ["மாநில எம்எல்ஏக்கள் பங்கேற்பு", "மாநில எம்எல்ஏக்கள் வாக்களிக்க முடியாது", "மாநில எம்எல்ஏக்கள் வாக்களிக்க முடியாது"]
        ]
      },
      {
        "id": "tbl_indian_vp_vs_american_vp",
        "title_en": "6. Indian Vice-President vs American Vice-President Comparison",
        "title_ta": "6. இந்தியத் துணைக் குடியரசுத் தலைவர் vs அமெரிக்கத் துணைக் குடியரசுத் தலைவர் ஒப்பீடு",
        "headers_en": ["Comparison Dimension", "Indian Vice-President", "American Vice-President"],
        "headers_ta": ["ஒப்பீட்டுப் பரிமாணம்", "இந்தியத் துணைக் குடியரசுத் தலைவர்", "அமெரிக்கத் துணைக் குடியரசுத் தலைவர்"],
        "rows_en": [
          ["Succession to Vacant Presidency", "Acts as President ONLY until new President elected (Max 6 months)", "Becomes President for FULL REMAINING TERM of predecessor"],
          ["Presiding Officer Role", "Ex-Officio Chairman of Rajya Sabha", "Ex-Officio President of US Senate"],
          ["Casting Vote Power", "Possesses Casting Vote in Rajya Sabha", "Possesses Casting Vote in US Senate"],
          ["Constitutional Weight", "Described as 'His Superfluous Highness' due to lack of independent executive functions", "Significant political office with direct presidential succession power"]
        ],
        "rows_ta": [
          ["குடியரசுத் தலைவர் காலியிட வாரிசுரிமை", "புதிய தலைவர் தேர்வாகும் வரை மட்டுமே செயல் தலைவர் (அதிகபட்சம் 6 மாதங்கள்)", "முந்தைய தலைவரின் மீதமுள்ள முழு பதவிக் காலத்திற்கும் தலைவராகிறார்"],
          ["அவைத் தலைவர் பொறுப்பு", "மாநிலங்களவையின் பதவிவழித் தலைவர்", "அமெரிக்க செனட் அவையின் பதவிவழித் தலைவர்"],
          ["முடிவு வாக்கு (Casting Vote)", "மாநிலங்களவையில் முடிவு வாக்கு அளிக்கும் அதிகாரம் உண்டு", "அமெரிக்க செனட்டில் முடிவு வாக்கு அளிக்கும் அதிகாரம் உண்டு"],
          ["அரசியலமைப்பு எடை", "சுயாதீன நிர்வாக அதிகாரங்கள் இல்லாததால் 'அவசியமற்ற மேன்மைப் பதவி' எனக் குறிப்பிடப்படுகிறது", "நேரடி வாரிசுரிமை அதிகாரத்துடன் கூடிய சக்திவாய்ந்த பதவி"]
        ]
      }
    ],
    "mind_map": [
      {
        "title": "Vice-President of India (Part V - Articles 63 to 71)",
        "short_label": "Vice-President Part 1",
        "children": [
          {
            "title": "1. Constitutional Position",
            "short_label": "Position",
            "children": [
              {
                "title": "Article 63: Office of Vice-President (2nd Highest Office)",
                "short_label": "Art 63 Office"
              },
              {
                "title": "Article 64: Ex-Officio Chairman of Rajya Sabha",
                "short_label": "Art 64 Ex-Officio"
              }
            ]
          },
          {
            "title": "2. Election & Electoral College",
            "short_label": "Election",
            "children": [
              {
                "title": "Article 66(1): Both Houses of Parliament (Elected + Nominated MPs)",
                "short_label": "Electoral College"
              },
              {
                "title": "No State MLAs / MLCs (Unlike Presidential Election)",
                "short_label": "No States"
              },
              {
                "title": "Method: Proportional Representation by STV (Secret Ballot)",
                "short_label": "STV Method"
              },
              {
                "title": "Vote Value: Equal MP vote value (= 1) (No weighted value)",
                "short_label": "Equal Vote"
              }
            ]
          },
          {
            "title": "3. Qualifications & Oath",
            "short_label": "Qualifications",
            "children": [
              {
                "title": "Article 66(3): Citizen, 35 Years Age, RS Election Eligibility",
                "short_label": "Qualifications"
              },
              {
                "title": "Article 69: Oath administered by President of India",
                "short_label": "Art 69 Oath"
              }
            ]
          },
          {
            "title": "4. Term, Resignation & Removal",
            "short_label": "Term & Removal",
            "children": [
              {
                "title": "Article 67: 5-Year Term (Eligible for Re-election)",
                "short_label": "Art 67 Term"
              },
              {
                "title": "Resignation: Addressed to President of India",
                "short_label": "Resignation"
              },
              {
                "title": "Article 67(b): Removal by RS Effective Majority + LS Simple Majority (14 days notice)",
                "short_label": "Removal Art 67b"
              }
            ]
          }
        ]
      }
    ],
    "tnpsc_traps": [
      {
        "title": "1. Nominated MPs Voting Rights Trap (நியமன எம்பிக்கள் வாக்குரிமைப் பொறி)",
        "points": {
          "en": [
            "TRAP: Believing nominated MPs cannot vote in any constitutional election.",
            "FACT: Nominated MPs CANNOT vote in the President's election (Article 54), BUT they CAN vote in the Vice-President's election (Article 66)!"
          ],
          "ta": [
            "பொறி: நியமன எம்பிக்கள் எந்தவொரு அரசியலமைப்புத் தேர்தலிலும் வாக்களிக்க முடியாது என நம்புவது.",
            "உண்மை: நியமன எம்பிக்கள் குடியரசுத் தலைவர் தேர்தலில் வாக்களிக்க முடியாது (உறுப்பு 54), ஆனால் துணைக் குடியரசுத் தலைவர் தேர்தலில் வாக்களிக்கலாம் (உறுப்பு 66)!"
          ]
        }
      },
      {
        "title": "2. State MLAs Participation Trap (மாநில எம்.எல்.ஏக்கள் பங்கேற்புப் பொறி)",
        "points": {
          "en": [
            "TRAP: Assuming State MLAs vote in both President and Vice-President elections.",
            "FACT: State MLAs vote ONLY in the President's election. They have ZERO role in the Vice-President's election!"
          ],
          "ta": [
            "பொறி: மாநில எம்.எல்.ஏக்கள் குடியரசுத் தலைவர் மற்றும் துணைக் குடியரசுத் தலைவர் இரு தேர்தல்களிலும் வாக்களிப்பார்கள் என நினைப்பது.",
            "உண்மை: மாநில எம்.எல்.ஏக்கள் குடியரசுத் தலைவர் தேர்தலில் மட்டுமே வாக்களிப்பார்கள். துணைக் குடியரசுத் தலைவர் தேர்தலில் அவர்களுக்கு எவ்விதப்ங்கும் இல்லை!"
          ]
        }
      },
      {
        "title": "3. House Eligibility Qualification Trap (சட்டமன்ற அவை தகுதிப் பொறி)",
        "points": {
          "en": [
            "TRAP: Confusing Lok Sabha vs Rajya Sabha qualification for President and Vice-President.",
            "FACT: President candidate must be qualified for LOK SABHA. Vice-President candidate must be qualified for RAJYA SABHA!"
          ],
          "ta": [
            "பொறி: குடியரசுத் தலைவர் மற்றும் துணைக் குடியரசுத் தலைவருக்கான அவை தகுதியைக் குழப்பிக் கொள்ளுதல்.",
            "உண்மை: குடியரசுத் தலைவர் வேட்பாளர் மக்களவைக்குத் (Lok Sabha) தேர்வாகும் தகுதி பெற வேண்டும். துணைக் குடியரசுத் தலைவர் வேட்பாளர் மாநிலங்களவைக்குத் (Rajya Sabha) தேர்வாகும் தகுதி பெற வேண்டும்!"
          ]
        }
      },
      {
        "title": "4. Resignation Address Trap (ராஜினாமாக் கடிதம் பெறுநர் பொறி)",
        "points": {
          "en": [
            "TRAP: Believing Vice-President resigns to the Speaker of Lok Sabha or Chief Justice.",
            "FACT: Vice-President resigns to the PRESIDENT OF INDIA. (And President resigns to the Vice-President)."
          ],
          "ta": [
            "பொறி: துணைக் குடியரசுத் தலைவர் தனது ராஜினாமாக் கடிதத்தை மக்களவை சபாநாயகர் அல்லது தலைமை நீதிபதியிடம் வழங்குவார் என நினைப்பது.",
            "உண்மை: துணைக் குடியரசுத் தலைவர் தனது ராஜினாமாக் கடிதத்தை இந்தியக் குடியரசுத் தலைவரிடம் வழங்குகிறார். (குடியரசுத் தலைவர் துணைக் குடியரசுத் தலைவரிடம் வழங்குகிறார்)."
          ]
        }
      },
      {
        "title": "5. Equal Vote Value vs Weighted Vote Trap (சமமான வாக்கு மதிப்பு பொறி)",
        "points": {
          "en": [
            "TRAP: Applying President's weighted vote-value formula to Vice-President's election.",
            "FACT: In Presidential election, MP and MLA votes are weighted based on population. In Vice-Presidential election, EVERY MP HAS AN EQUAL VOTE VALUE OF 1!"
          ],
          "ta": [
            "பொறி: குடியரசுத் தலைவர் தேர்தலின் எடையுள்ள வாக்கு சூத்திரத்தைத் துணைக் குடியரசுத் தலைவர் தேர்தலுக்குப் பயன்படுத்துவது.",
            "உண்மை: குடியரசுத் தலைவர் தேர்தலில் மக்கள் தொகை அடிப்படையில் வாக்கு மதிப்பு கணக்கிடப்படும். துணைக் குடியரசுத் தலைவர் தேர்தலில் ஒவ்வொரு எம்பியின் வாக்கு மதிப்பும் சமமாக 1 ஆகும்!"
          ]
        }
      },
      {
        "title": "6. Oath Administration Trap (பதவிப் பிரமாண நிர்வாகப் பொறி)",
        "points": {
          "en": [
            "TRAP: Assuming Chief Justice of India administers oath to the Vice-President.",
            "FACT: Chief Justice of India administers oath to the PRESIDENT (Art 60). The PRESIDENT OF INDIA administers oath to the VICE-PRESIDENT (Art 69)!"
          ],
          "ta": [
            "பொறி: இந்திய தலைமை நீதிபதி துணைக் குடியரசுத் தலைவருக்குப் பதவிப் பிரமாணம் செய்து வைப்பார் எனக் கருதுவது.",
            "உண்மை: தலைமை நீதிபதி குடியரசுத் தலைவருக்குப் பதவிப் பிரமாணம் செய்து வைக்கிறார் (உறுப்பு 60). குடியரசுத் தலைவர் துணைக் குடியரசுத் தலைவருக்குப் பதவிப் பிரமாணம் செய்து வைக்கிறார் (உறுப்பு 69)!"
          ]
        }
      },
      {
        "title": "7. Impeachment vs Removal Terminology Trap (பதவி நீக்கச் சொல் பொறி)",
        "points": {
          "en": [
            "TRAP: Using the term 'Impeachment' for Vice-President removal.",
            "FACT: The Constitution uses 'Impeachment' ONLY for the President (Article 61). Vice-President removal is called 'Removal by Resolution' (Article 67(b))."
          ],
          "ta": [
            "பொறி: துணைக் குடியரசுத் தலைவர் பதவி நீக்கத்திற்கு 'Impeachment' என்ற சொல்லைப் பயன்படுத்துவது.",
            "உண்மை: அரசியலமைப்பு 'Impeachment' என்ற சொல்லைக் குடியரசுத் தலைவருக்கு மட்டுமே பயன்படுத்துகிறது (உறுப்பு 61). துணைக் குடியரசுத் தலைவருக்கு 'தீர்மானம் மூலம் பதவி நீக்கம்' (Article 67(b)) என்றே குறிப்பிடப்படுகிறது."
          ]
        }
      },
      {
        "title": "8. Removal Initiation House Trap (பதவி நீக்கம் தொடங்கும் அவை பொறி)",
        "points": {
          "en": [
            "TRAP: Believing Vice-President removal resolution can originate in Lok Sabha.",
            "FACT: Vice-President removal resolution CAN ORIGINATE ONLY IN RAJYA SABHA (Article 67(b)). Lok Sabha only needs to agree by simple majority."
          ],
          "ta": [
            "பொறி: துணைக் குடியரசுத் தலைவர் பதவி நீக்கத் தீர்மானம் மக்களவையில் தொடங்கப்படலாம் என நம்புவது.",
            "உண்மை: துணைக் குடியரசுத் தலைவர் பதவி நீக்கத் தீர்மானம் மாநிலங்களவையில் (Rajya Sabha) மட்டுமே தொடங்கப்பட முடியும் (உறுப்பு 67(b))."
          ]
        }
      },
      {
        "title": "9. Maximum Acting Presidency Duration Trap (செயல் தலைவர் கால வரம்பு பொறி)",
        "points": {
          "en": [
            "TRAP: Believing Indian Vice-President becomes President for the remaining unexpired term.",
            "FACT: In US, Vice-President becomes President for the full remaining term. In India, Vice-President acts as President ONLY until a new President is elected (MAXIMUM 6 MONTHS)!"
          ],
          "ta": [
            "பொறி: இந்தியத் துணைக் குடியரசுத் தலைவர் மீதமுள்ள முழு பதவிக் காலத்திற்கும் குடியரசுத் தலைவராக மாறிவிடுவார் என நம்புவது.",
            "உண்மை: அமெரிக்காவில் மீதமுள்ள முழு காலத்திற்கும் தலைவராவார். இந்தியாவில் புதிய தலைவர் தேர்வாகும் வரை அதிகபட்சம் 6 மாதங்கள் மட்டுமே செயல் தலைவராக இருக்க முடியும்!"
          ]
        }
      },
      {
        "title": "10. Article 71 Election Disputes Trap (தேர்தல் தகராறுகள் பொறி)",
        "points": {
          "en": [
            "TRAP: Believing Election Commission of India decides Presidential/Vice-Presidential election disputes.",
            "FACT: Election Commission conducts the election, BUT all election DISPUTES are inquired into and decided EXCLUSIVELY BY THE SUPREME COURT under Article 71!"
          ],
          "ta": [
            "பொறி: குடியரசுத் தலைவர் / துணைக் குடியரசுத் தலைவர் தேர்தல் தகராறுகளை இந்தியத் தேர்தல் ஆணையம் தீர்க்கும் என நினைப்பது.",
            "உண்மை: தேர்தல் ஆணையம் தேர்தலை மட்டுமே நடத்துகிறது; ஆனால் அனைத்துத் தேர்தல் தகராறுகளையும் உறுப்பு 71-ன் கீழ் உச்ச நீதிமன்றம் மட்டுமே விசாரித்துத் தீர்க்கும்!"
          ]
        }
      }
    ],
    "important_facts": {
      "en": [
        "Article 63 establishes the office of the Vice-President of India as the 2nd highest constitutional office.",
        "The Vice-President is elected by an Electoral College consisting of ALL MPs of Parliament (Elected + Nominated).",
        "State Legislative Assemblies (MLAs) and Legislative Councils (MLCs) do NOT participate in Vice-President elections.",
        "Every MP vote in the Vice-Presidential election has an equal vote value of 1.",
        "Minimum age for eligibility is 35 years, and the candidate must be qualified for election to Rajya Sabha.",
        "Oath is administered by the President of India under Article 69.",
        "Resignation letter is addressed to the President of India.",
        "Under Article 64, the Vice-President serves as the Ex-officio Chairman of the Rajya Sabha."
      ],
      "ta": [
        "உறுப்பு 63 துணைக் குடியரசுத் தலைவர் பதவியை நாட்டின் 2-வது மிக உயர்ந்த அரசியலமைப்புப் பதவியாக உருவாக்குகிறது.",
        "நாடாளுமன்றத்தின் அனைத்து எம்பிக்களையும் (தேர்ந்தெடுக்கப்பட்ட + நியமன) கொண்ட வாக்காளர் குழுவால் தேர்ந்தெடுக்கப்படுகிறார்.",
        "மாநில சட்டமன்ற உறுப்பினர்கள் (MLAs) மற்றும் மேலவை உறுப்பினர்கள் (MLCs) இத்தேர்தலில் பங்கேற்பதில்லை.",
        "துணைக் குடியரசுத் தலைவர் தேர்தலில் ஒவ்வொரு எம்பியின் வாக்கு மதிப்பும் சமமாக 1 ஆகும்.",
        "குறைந்தபட்ச வயது வரம்பு 35 ஆண்டுகள் மற்றும் மாநிலங்களவை உறுப்பினராவதற்கான தகுதி பெற்றிருக்க வேண்டும்.",
        "பதவிப் பிரமாணம் உறுப்பு 69-ன் கீழ் இந்தியக் குடியரசுத் தலைவரால் செய்து வைக்கப்படுகிறது.",
        "ராஜினாமாக் கடிதம் இந்தியக் குடியரசுத் தலைவரிடம் சமர்ப்பிக்கப்பட வேண்டும்.",
        "உறுப்பு 64-ன் கீழ் துணைக் குடியரசுத் தலைவர் மாநிலங்களவையின் பதவிவழித் தலைவராகப் பணியாற்றுகிறார்."
      ]
    },
    "quick_revision": {
      "en": [
        "Office: Article 63 (2nd Highest Constitutional Office in India).",
        "Electoral College: Article 66(1) — Both Houses of Parliament (Elected + Nominated MPs). No State MLAs.",
        "Method: Proportional Representation by Single Transferable Vote (Secret Ballot). Equal MP vote value = 1.",
        "Qualifications: Article 66(3) — Indian Citizen, 35 Years Age, Qualified for Rajya Sabha election.",
        "Term & Resignation: Article 67 — 5 Years term; Resignation addressed to President of India.",
        "Oath: Article 69 — Administered by the President of India.",
        "Removal Foundation: Article 67(b) — Resolution initiated ONLY in Rajya Sabha (Effective Majority) + Lok Sabha agreement (Simple Majority)."
      ],
      "ta": [
        "பதவி: உறுப்பு 63 (இந்தியாவின் 2-வது மிக உயர்ந்த அரசியலமைப்புப் பதவி).",
        "வாக்காளர் குழு: உறுப்பு 66(1) — நாடாளுமன்ற இரு அவைகளும் (தேர்ந்தெடுக்கப்பட்ட + நியமன எம்பிக்கள்). மாநில எம்.எல்.ஏக்கள் இல்லை.",
        "தேர்தல் முறை: ஒற்றை மாற்று வாக்கு விகிதாச்சார பிரதிநிதித்துவம் (ரகசிய வாக்கெடுப்பு). எம்பி வாக்கு மதிப்பு = 1.",
        "தகுதிகள்: உறுப்பு 66(3) — இந்தியக் குடிமகன், 35 வயது, மாநிலங்களவை உறுப்பினர் தகுதி.",
        "பதவிக் காலம் & ராஜினாமா: உறுப்பு 67 — 5 ஆண்டுகள்; ராஜினாமா குடியரசுத் தலைவரிடம் வழங்கப்பட வேண்டும்.",
        "பதவிப் பிரமாணம்: உறுப்பு 69 — இந்தியக் குடியரசுத் தலைவரால் செய்து வைக்கப்படுகிறது.",
        "பதவி நீக்க அடிப்படை: உறுப்பு 67(b) — மாநிலங்களவையில் மட்டுமே தொடங்கும் தீர்மானம் (Effective Majority) + மக்களவை ஒப்புதல் (Simple Majority)."
      ]
    },
    "revision_cards": [
      {
        "title": "Article 63",
        "content_en": "Establishes that 'There shall be a Vice-President of India' (2nd highest office).",
        "content_ta": "'இந்தியாவிற்கு ஒரு துணைக் குடியரசுத் தலைவர் இருக்க வேண்டும்' எனப் பதவியை நிறுவுகிறது (2-வது உயர்ந்த பதவி)."
      },
      {
        "title": "Article 64",
        "content_en": "Vice-President is the Ex-Officio Chairman of Rajya Sabha (Council of States).",
        "content_ta": "துணைக் குடியரசுத் தலைவர் மாநிலங்களவையின் பதவிவழித் தலைவராவார்."
      },
      {
        "title": "Article 65",
        "content_en": "Vice-President acts as President during casual vacancies or absence (Max 6 months).",
        "content_ta": "குடியரசுத் தலைவர் பதவிக் காலியிடங்களின் போது செயல் தலைவராகப் பணியாற்றுகிறார் (அதிகபட்சம் 6 மாதங்கள்)."
      },
      {
        "title": "Article 66(1) Electoral College",
        "content_en": "Electoral College = All MPs of Parliament (Elected + Nominated). No State MLAs.",
        "content_ta": "வாக்காளர் குழு = நாடாளுமன்றத்தின் அனைத்து எம்பிக்களும் (தேர்ந்தெடுக்கப்பட்ட + நியமன). மாநில எம்.எல்.ஏக்கள் இல்லை."
      },
      {
        "title": "Article 66(3) Qualifications",
        "content_en": "Citizen of India, Completed 35 Years, Qualified for Rajya Sabha election.",
        "content_ta": "இந்தியக் குடிமகன், 35 வயது பூர்த்தி, மாநிலங்களவை உறுப்பினர் தகுதி."
      },
      {
        "title": "Article 67 Term",
        "content_en": "5-Year Term; Resigns to President; Re-election permitted for any number of terms.",
        "content_ta": "5 ஆண்டுகள் பதவிக் காலம்; குடியரசுத் தலைவரிடம் ராஜினாமா; எத்தனை முறை வேண்டுமானாலும் மீண்டும் போட்டியிடலாம்."
      },
      {
        "title": "Article 67(b) Removal",
        "content_en": "Resolution initiated ONLY in Rajya Sabha (Effective Majority) + Lok Sabha Simple Majority.",
        "content_ta": "மாநிலங்களவையில் மட்டுமே தொடங்கும் தீர்மானம் (Effective Majority) + மக்களவையில் சாதாரண பெரும்பான்மை."
      },
      {
        "title": "Article 68 Vacancy",
        "content_en": "Regular election before term expiry; Casual vacancy election held 'as soon as possible'.",
        "content_ta": "காலம் முடிவதற்குள் அடுத்த தேர்தல்; அவசரக் காலியிடத்திற்கு 'যত விரைவில் சாத்தியமோ' தேர்தல்."
      },
      {
        "title": "Article 69 Oath",
        "content_en": "Oath administered by the President of India or a person appointed by him.",
        "content_ta": "பதவிப் பிரமாணம் இந்தியக் குடியரசுத் தலைவரால் செய்து வைக்கப்படுகிறது."
      },
      {
        "title": "Article 71 Disputes",
        "content_en": "Supreme Court has exclusive and final jurisdiction over President/VP election disputes.",
        "content_ta": "குடியரசுத் தலைவர் / துணைக் குடியரசுத் தலைவர் தேர்தல் தகராறுகளை உச்ச நீதிமன்றம் மட்டுமே விசாரிக்கும்."
      },
      {
        "title": "Equal Vote Value",
        "content_en": "Every MP in Vice-President election has equal vote value of 1 (No population weighting).",
        "content_ta": "துணைக் குடியரசுத் தலைவர் தேர்தலில் ஒவ்வொரு எம்பியின் வாக்கு மதிப்பும் சமமாக 1 ஆகும்."
      },
      {
        "title": "US vs Indian VP Succession",
        "content_en": "US VP becomes President for full unexpired term; Indian VP acts as President max 6 months.",
        "content_ta": "அமெரிக்க VP மீதமுள்ள முழு காலத்திற்கும் தலைவராவார்; இந்திய VP அதிகபட்சம் 6 மாதங்கள் மட்டுமே செயல் தலைவராவார்."
      }
    ]
  }
}

target_path = 'data/notes/polity/vice_president_part_1.json'
with open(target_path, 'w', encoding='utf-8') as f:
    json.dump(part1_data, f, ensure_ascii=False, indent=2)

print(f"✅ Vice-President Part 1 JSON built successfully: {target_path}")
