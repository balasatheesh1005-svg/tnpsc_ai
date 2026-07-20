# TNPSC Nova AI - Content Standards (Version 1.0)

This document defines the official **Content Quality Standards** and Quality Assurance (QA) guidelines for the **TNPSC Nova AI** platform. It covers bilingual revision notes, practice questions (MCQs), previous year questions (PYQs), and AI-generated contents.

---

## 1. Overview
Quality educational material is critical for students preparing for the competitive TNPSC Group-I Preliminary Exam. This document establishes rigorous benchmarks for factual accuracy, bilingual quality, and layout compatibility. All content developers, editors, and automated AI models must comply with these standards.

---

## 2. Content Philosophy
The academic design of TNPSC Nova AI is built upon six core pillars:
* **Exam-Oriented Learning**: Focuses strictly on concepts frequently tested in TNPSC Group-1 exams.
* **Concept-First Teaching**: Promotes deep understanding of facts and rules before test attempts.
* **Progressive Learning**: Uses adaptive level adjustments to guide students from basic facts to complex statement matrices.
* **Bilingual Education**: Provides parallel translations (English and Tamil) to help students master terminology in both languages.
* **Revision-First Approach**: Structures study sheets to facilitate quick, high-yield reviews.
* **Practice-Driven Preparation**: Reinforces learning through topic-based testing.

---

## 3. Notes Standards
Every Notes JSON file must conform to the following quality standards:
* **Syllabus Alignment**: Content must align with the official TNPSC Group 1 syllabus.
* **Factual Rigor**: Historical dates, case names, and constitutional articles must be cross-verified.
* **Bilingual Completeness**: English and Tamil sections must be fully translated.
* **Syllabus hot spots**: High-priority concepts must include warnings and reminders about common traps.

### Mandatory Sections by UI Type
* **Polity (`"polity"`)**:
  * `definition` (Bilingual string)
  * `acts` / `objectives` (Array of bilingual objects)
  * `importance` (Bilingual array)
* **Economy & History (`"economy" | "history"`)**:
  * `definition` (Bilingual string)
  * Dynamic sub-sections (e.g. `important_rulers`)
  * `timeline` (History only, array of date/event pairs)
  * `important_facts` (Bilingual array)
  * `mind_map` (Array of tags)
* **Aptitude & Reasoning (`"aptitude" | "reasoning"`)**:
  * `definition` (Bilingual string)
  * `formula_sheet` / `concept_rules` (Equation list or rules list)
  * `shortcut_tricks` (Alert shortcuts)
  * `solved_examples` (Worked-out expansion panels)
  * `important_facts` (Bilingual array)

---

## 4. MCQ Standards
To ensure effective practice sessions, every question object in the MCQ database must meet these standards:
* **Single Concept Focus**: Each question must evaluate one target concept at a time.
* **Single Correct Answer**: There must be exactly one correct choice. If multiple options are acceptable, the question must be restructured.
* **Distractor Plausibility**: Incorrect choices (distractors) must be realistic and reflect common student misunderstandings.
* **Bilingual Integrity**: Tamil translation terms must match the context of the English statements.
* **Explanation Completeness**: Explanations must clearly explain *why* the option is correct.

---

## 5. Question Distribution
To prepare students for all sections of the exam, topic collections should target the following question type distribution:

| Question Type | Distribution Target | Academic Purpose |
| :--- | :--- | :--- |
| **Direct Factual** | 30% | Evaluates recollection of constitutional articles, years, authors, and events. |
| **Conceptual** | 20% | Evaluates understanding of principles (e.g., judicial review, inflation). |
| **Statement-Based** | 15% | Evaluates multi-layered factual reasoning using multi-statement options. |
| **Assertion & Reason** | 10% | Tests logical connections and causal reasoning. |
| **Match the Following** | 10% | Tests association across categories (e.g., terms, leaders, events). |
| **Chronology** | 5% | Evaluates chronological sequence of historical events. |
| **Analytical** | 5% | Tests application of concepts in hypothetical scenarios. |
| **Calculation / Logic** | 5% | Evaluates quantitative and logical reasoning (Aptitude & Reasoning only). |

---

## 6. Difficulty Standards
Difficulty levels must be determined by objective design criteria rather than subjective complexity:

### Easy
* **Expected Knowledge**: Basic facts, direct articles, simple formulas.
* **Thinking Level**: Recall.
* **Time Required**: Less than 30 seconds.
* **Indicators**: Straightforward question statements; clearly incorrect distractors.

### Medium
* **Expected Knowledge**: Combined facts, multi-clause provisions, two-step equations.
* **Thinking Level**: Application and analysis.
* **Time Required**: 30 to 60 seconds.
* **Indicators**: Statement evaluations (e.g., "Which of the statements are correct?"); close distractors.

### Hard
* **Expected Knowledge**: Complex case laws, historical timelines, Assertion-Reason logic.
* **Thinking Level**: Synthesis and evaluation.
* **Time Required**: 60 to 90 seconds.
* **Indicators**: Assertion-Reason pairings; detailed chronology tables; multiple statements.

---

## 7. Explanation Standards
An effective explanation is a high-yield learning resource. Every question explanation must include:
1. **Core Rationale**: Explanation of the correct option.
2. **Distractor Analysis**: Brief notes explaining why incorrect options are wrong.
3. **Reference Citation**: Relevant articles, case laws, amendments, or textbook chapters.
4. **TNPSC Trap Warning (Optional)**: Guidance highlighting common exam traps.

---

## 8. Language Standards
* **English Standard**: Clear, formal Indian English vocabulary.
* **Tamil Standard**: Formal, standard academic Tamil. Avoid colloquial speech.
* **Translation Alignment**: Terminology must align across languages. For example:
  * *"Sovereign"* $\rightarrow$ *இறையாண்மை*
  * *"Amendment"* $\rightarrow$ *அரசியலமைப்புச் சட்டத்திருத்தம்*
* **Formatting Consistency**: Maintain matching formats, punctuation, and layouts in both versions.

---

## 9. Visual Standards
UI elements in [streamlit_ui_engine.py](file:///c:/Users/Home/Desktop/tnpsc_ai/core/streamlit_ui_engine.py) must be used consistently:

* **st.info**: Used for core definitions.
* **st.success**: Used for important facts and shortcut methods.
* **st.warning / st.error**: Used for traps and common mistakes.
* **st.expander**: Used for step-by-step solved examples.
* **st.code**: Used to format equations in formula sheets.
* **Markdown bold lists**: Used to render timeline dates.

---

## 10. Subject-Specific Standards
* **Polity**: Must cite constitutional articles, amendments, case laws, and committee recommendations.
* **History**: Must preserve accurate timelines and verify events and dynastic records.
* **Geography**: Must focus on maps, locations, resources, and meteorological patterns.
* **Economy**: Must focus on GDP metrics, inflation, tax structures, and planning policies.
* **Science**: Must focus on physics equations, chemical terms, biological systems, and scientific applications.
* **Aptitude**: Must provide step-by-step worked-out examples for all formulas.

---

## 11. PYQ Standards
* **Source Authenticity**: Use only official, final TNPSC question sheets and keys.
* **Verified Key Verification**: Crosscheck tentative keys with the final answer key list.
* **Reference Tagging**: Tag previous year questions with their exam and year (e.g. `🏆 PYQ 2019`).
* **Topic Alignment**: Map questions to their corresponding topic keys.

---

## 12. Content Review Checklist
Before any JSON file is merged into production, it must pass the following checks:

- [ ] **Schema Conformance**: Validated against the Notes and MCQ schemas.
- [ ] **Bilingual Alignment**: No missing translations in English or Tamil.
- [ ] **Factual Accuracy**: Facts, dates, and references are verified.
- [ ] **Distractor Validation**: Multiple-choice options are unique and plausible.
- [ ] **Option Sizing**: Question has exactly 4 options.
- [ ] **Key lowercase check**: Correct key matches an options letter (`"a"`, `"b"`, `"c"`, `"d"`).
- [ ] **UI Rendering Compatibility**: Layout displays cleanly without UI errors.

---

## 13. Quality Scoring System
Every new topic collection is scored out of 100 points:

| Quality Dimension | Points | Scoring Criteria |
| :--- | :---: | :--- |
| **Factual Accuracy** | 20 | Deduct 5 points for each minor error; major errors result in rejection. |
| **Bilingual Completeness** | 20 | Deduct 5 points for missing translations or unaligned terms. |
| **Syllabus Relevance** | 15 | Evaluates coverage of exam topics and past question patterns. |
| **Explanation Rigor** | 15 | Evaluates detail and clarity of rationales. |
| **MCQ Options Quality** | 15 | Checks for plausible distractors and single correct answers. |
| **Schema Compliance** | 15 | Deduct 5 points for any schema warning or missing field. |

* **Acceptance Threshold**: Content must score **$\ge 85$ points** to be accepted. Any score below 85 requires revision.

---

## 14. Content Rejection Rules
Content must be rejected if it contains any of the following critical issues:
1. **Broken JSON syntax** (syntax errors, missing commas, mismatched brackets).
2. **Missing Tamil or English translations** (partially translated content).
3. **Factual errors** (incorrect articles, years, math formulas, or answer keys).
4. **Duplicate questions** or overlapping question statements.
5. **Schema warnings** (incorrect keys, missing required fields, or wrong folder nesting).

---

## 15. AI Content Rules
Artificial intelligence models generating content for the platform must follow these rules:
1. **Schema Adherence**: Do not invent new fields or modify key names.
2. **Production-Ready Output**: Always output complete, valid JSON. Do not truncate JSON output with placeholders.
3. **Bilingual Completeness**: Generate translations for all sections.
4. **Factual Rigor**: Cross-reference dates, case names, and historical events.

---

## 16. Best Practices
* **For Content Writers**: Draft bilingual texts in parallel to keep translations aligned.
* **For Automated AI Models**: Adhere strictly to the frozen schemas and validation criteria.
* **For Developers**: Maintain clear separation between application logic and content JSON files.
* **For Reviewers**: Verify that new additions are registered in structural JSON files.

---

## 17. Versioning Policy
* **Version Format**: Uses semantic versioning (e.g. `1.0`).
* **Major Changes (X.0)**: Reserved for structural changes to the database schema.
* **Minor Changes (1.X)**: Reserved for updates to questions, explanations, or notes content.
* **Backward Compatibility**: Any updates to content files must maintain compatibility with the core rendering engine.

---

## 18. Final Content Freeze
The **TNPSC Nova AI Content Standards (Version 1.0)** are hereby frozen. All future content updates, AI models, and validation checks must comply with these guidelines.
