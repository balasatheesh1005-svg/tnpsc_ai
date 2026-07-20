# TNPSC Nova AI - Validation Checklist (Version 1.0)

This document is the official **Validation Checklist** and Quality Gate specification for the **TNPSC Nova AI** project. It serves as the mandatory checklist for merging any study notes, practice questions (MCQs), previous year questions (PYQs), and AI-generated contents into the production repository.

---

## 1. Validation Overview
The purpose of the validation system is to prevent errors from reaching the production app.
* **Why Validation is Required**: Streams-based database structures and dynamic UI templates depend on absolute JSON schema consistency. Typos or missing translation keys will trigger runtime exceptions in the Streamlit interface.
* **Production Workflow**: Content progresses through automated checks, academic evaluations, translation review, and technical validation.
* **Approval Stages**: All content must pass the automated validator checks, earn a minimum score, pass manual quality reviews, and receive QA signoff.

---

## 2. Notes Validation
Every notes JSON file must be evaluated against the following criteria:

* **Syntax & Schema**:
  * [ ] File parses successfully as valid UTF-8 JSON.
  * [ ] Matches the Notes JSON schema definition exactly.
  * [ ] Mandatory fields (`subject`, `topic`, `language`, `ui_type`, `content`) are present at the root.
* **Language & Translation**:
  * [ ] No empty values in English (`en`) keys.
  * [ ] No empty values in Tamil (`ta`) keys.
  * [ ] Technical terms are consistently translated (e.g. *Sovereign* $\rightarrow$ *இறையாண்மை*).
* **Topic & Layout Routing**:
  * [ ] Topic is registered in `data/structure/{subject}_structure.json`.
  * [ ] Suffix and path match: `data/notes/{subject}/{topic_key}.json`.
  * [ ] The `ui_type` string is exactly `"polity"`, `"economy"`, `"history"`, `"aptitude"`, or `"reasoning"`.
* **Component-Specific Checks**:
  * [ ] Polity notes match polity sub-item requirements.
  * [ ] History notes verify dates, events, and timeline lists.
  * [ ] Economy notes verify key policies, indicators, and fact boxes.
  * [ ] Aptitude notes verify code blocks, shortcut boxes, and expanders.
  * [ ] Reasoning notes verify rule lists, shortcut methods, and warning boxes.

---

## 3. MCQ Validation
Practice question database files (`data/questions/`) must satisfy these criteria:

* **Syntax & Schema**:
  * [ ] File parses successfully as valid UTF-8 JSON.
  * [ ] Meets the MCQ JSON schema structure.
  * [ ] Parent folders are correct (`data/questions/{subject}/`).
* **Question Content**:
  * [ ] Question statements (`question_en`, `question_ta`) are complete and clear.
  * [ ] Options lists (`options_en`, `options_ta`) contain exactly four unique choices.
  * [ ] Correct choice `"answer"` is a lowercase letter (`"a"`, `"b"`, `"c"`, `"d"`).
* **Verification & Rationale**:
  * [ ] Only one option is correct.
  * [ ] Explanations (`explanation_en`, `explanation_ta`) are clear and state *why* the option is correct.
  * [ ] Difficulty tags match their folder and file structure (`_easy.json`, `_medium.json`, `_hard.json`).

---

## 4. PYQ Validation
Verified Previous Year Questions (PYQs) must pass the following audits:

* **Source Authenticity**:
  * [ ] Source matched with official TNPSC final answer keys.
  * [ ] Answer options list matches the verified final key.
* **Integrity & References**:
  * [ ] Multi-answers lists conform to schema specifications (e.g. `["A", "C"]`).
  * [ ] Question is mapped to its matching topic key.
  * [ ] Previous year tag (`🏆 PYQ YYYY`) is formatted correctly.

---

## 5. AI Output Validation
AI-generated content must be audited to verify:

* **Architecture Alignment**:
  * [ ] Conforms to the frozen database structure and key naming conventions.
  * [ ] No new root properties or unsupported sections are generated.
* **Content Delivery**:
  * [ ] No truncated JSON blocks or placeholders.
  * [ ] Both English and Tamil translation blocks are complete.

---

## 6. Language Validation
* **English Grammar**: Check for correct grammar, punctuation, and capitalization.
* **Tamil Grammar**: Verify that formal academic Tamil is used. Avoid colloquial expressions.
* **Translation Alignment**: Ensure terminology matches across languages.
* **Bilingual Consistency**: Parallel lists must have matching counts to avoid layout misalignment.

---

## 7. Content Quality Validation
* **Academic Rigor**: Content must match the TNPSC Group 1 syllabus standards.
* **Fact Verification**: Historical dates, case names, and constitutional articles must be verified.
* **Clarity**: Explanations must be easy to follow and support student revision.

---

## 8. Technical Validation
* **Encoding**: Files must be saved in `UTF-8` encoding.
* **Formatting**: Validate that the JSON contains no syntax errors, missing commas, or mismatched brackets.
* **Directory Paths**: Verify that directories use standard casing (e.g. `data/notes/polity/`).

---

## 9. Scoring System
Every new content block is scored out of 100 points:

| Quality Dimension | Weight | Scoring Criteria |
| :--- | :---: | :--- |
| **Factual Accuracy** | 25% | Rejects content if any factual errors exist. |
| **Bilingual Completeness** | 20% | Rejects content if any translation is missing. |
| **Schema Compliance** | 15% | Rejects content if any required fields are missing. |
| **UI Compatibility** | 15% | Evaluates rendering quality in the Streamlit UI. |
| **Explanation Rigor** | 15% | Evaluates the clarity and detail of explanation notes. |
| **MCQ Distractors Quality** | 10% | Verifies that all options are unique and plausible. |

* **Validation Quality Gate**: Content must score **$\ge 90$ points** to be merged into production.

---

## 10. Failure Conditions
Content must be rejected if it triggers any of the following critical failures:
1. **Broken JSON Syntax**: Malformed JSON files.
2. **Schema Mismatch**: Missing or renamed required fields.
3. **Incomplete Translations**: Missing English or Tamil sections.
4. **Factual Errors**: Mapped incorrect constitutional articles, historical dates, or answer keys.
5. **UI Rendering Failures**: Content triggers rendering errors in the UI.

---

## 11. Production Workflow
The final approval pipeline follows this flow:

```text
  Content Draft ──► Schema Audit ──► Academic Audit ──► Technical Signoff ──► QA Merge
```

1. **Draft Stage**: Author writes or AI generates content JSON.
2. **Schema Audit**: Automated script validates JSON formatting and key schemas.
3. **Academic Audit**: Subject Matter Expert reviews translation accuracy and facts.
4. **Technical Signoff**: Developer verifies UI layout rendering.
5. **QA Merge**: QA team merges verified content into the production repository.

---

## 12. Review Responsibilities
* **Content Writer**: Drafts bilingual notes and question sheets.
* **AI Model**: Generates content conforming to the schema guidelines.
* **Academic Reviewer**: Verifies factual correctness and translation quality.
* **Technical Developer**: Checks code integrations and UI rendering performance.
* **QA Lead**: Grants final approval and merges content into production.

---

## 13. Best Practices
1. **Validate JSON First**: Always run automated syntax and schema checks first.
2. **Verify Bilingual Completeness**: Never merge content with missing translations.
3. **Test UI Rendering**: Check that all dynamic sections render correctly in Streamlit.
4. **Enforce Strict Schema Rules**: Never bypass validators to speed up a release.

---

## 14. Validation Templates
Below are the ready-to-use review checklists:

### Notes Validation Card
```text
Subject: ___________ | Topic: ___________

[ ] JSON parses without syntax errors (UTF-8 encoding).
[ ] Matches Notes JSON schema structure (required root fields present).
[ ] Subject matches the structure registry.
[ ] Topic is registered in structure JSON.
[ ] Folder path is correct: data/notes/{subject}/{topic_key}.json.
[ ] English translation blocks are complete.
[ ] Tamil translation blocks are complete.
[ ] All nested sub-sections are bilingual.
[ ] Displays correctly in the Streamlit UI.
```

### MCQ Validation Card
```text
Subject: ___________ | Topic: ___________ | Level: ___________

[ ] JSON parses without syntax errors (UTF-8 encoding).
[ ] Matches MCQ JSON schema structure.
[ ] Question text is complete in English and Tamil.
[ ] Contains exactly four unique options.
[ ] Tamil options match the order of English options.
[ ] Correct answer key matches a lowercase choice letter ("a", "b", "c", "d").
[ ] English explanation details why the answer is correct.
[ ] Tamil explanation details why the answer is correct.
[ ] No duplicate questions are present in the collection.
```

### PYQ Validation Card
```text
Question ID: ___________ | Exam / Year: ___________

[ ] Source is matched with official TNPSC final answer keys.
[ ] Answer options list matches the verified final key.
[ ] Multi-answers lists conform to schema specifications (e.g. ["A", "C"]).
[ ] Previous year tag (🏆 PYQ YYYY) is formatted correctly.
```

---

## 15. Final Validation Freeze
The **TNPSC Nova AI Validation Checklist (Version 1.0)** is hereby frozen. All future content updates, ingestion pipelines, and QA reviews must comply with these guidelines.
