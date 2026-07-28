# TNPSC Nova AI - MCQ Schema Specification (Version 1.0)

This document is the official schema specification for **TNPSC Nova AI** multiple-choice practice and test questions (MCQs) JSON files. It serves as the single source of truth for the MCQ database structure, answer verification, and difficulty progression.

---

## 1. Overview
The MCQ System dynamically generates practice tests, registers student test attempts, calculates XP, and adjusts the question difficulty level in real-time.
* Question files are divided by topic and difficulty level.
* They are loaded via [question_loader.py](file:///c:/Users/Home/Desktop/tnpsc_ai/core/question_loader.py) and evaluated in [test_evaluator.py](file:///c:/Users/Home/Desktop/tnpsc_ai/core/test_evaluator.py).
* Level scaling is handled adaptively after each question attempt using [difficulty_ai.py](file:///c:/Users/Home/Desktop/tnpsc_ai/core/difficulty_ai.py).

---

## 2. Existing MCQ Analysis
The practice question database files are stored inside `data/questions/{subject}/` and partitioned by difficulty levels. Each JSON file contains an array of question dictionaries matching this structure:
```json
[
  {
    "question_en": "English question text",
    "question_ta": "தமிழ் கேள்வி உரை",
    "options_en": ["Option A", "Option B", "Option C", "Option D"],
    "options_ta": ["விடை A", "விடை B", "விடை C", "விடை D"],
    "answer": "a | b | c | d",
    "explanation_en": "English explanation note",
    "explanation_ta": "தமிழ் விளக்கக் குறிப்பு",
    "subject": "SUBJECT",
    "topic": "topic_key"
  }
]
```

---

## 3. Common Fields
Every question object in the JSON database contains these mandatory fields:

### `subject`
* **Purpose**: Identifies the primary curriculum subject.
* **Description**: Matches the uppercase subject category tag.
* **Required / Optional**: Required.
* **Data Type**: String.
* **Allowed Values**: `"POLITY"`, `"ECONOMY"`, `"HISTORY"`, `"GEOGRAPHY"`, `"SCIENCE"`, `"APTITUDE"`, `"REASONING"`.
* **Example**: `"POLITY"`

### `topic`
* **Purpose**: Specifies the curriculum topic identifier.
* **Description**: Matches the lowercased snake_case topic key.
* **Required / Optional**: Required.
* **Data Type**: String.
* **Allowed Values**: Topic keys registered in the curriculum structure.
* **Example**: `"preamble"`

---

## 4. Question Structure
The fields representing the question statements are structured as follows:

### `question_en`
* **Purpose**: The question statement text shown in English.
* **Description**: Holds plain text, assertion-reason pairings, or statement selections.
* **Required / Optional**: Required.
* **Data Type**: String.
* **Example**: `"Which words were added by the 42nd Amendment?"`

### `question_ta`
* **Purpose**: The question statement text shown in Tamil.
* **Description**: Direct, contextually accurate Tamil translation of `question_en`.
* **Required / Optional**: Required.
* **Data Type**: String.
* **Example**: `"42வது திருத்தத்தில் சேர்க்கப்பட்ட சொற்கள்?"`

---

## 5. Option Structure
The multiple-choice options are stored in parallel bilingual lists:

### `options_en`
* **Purpose**: The list of choices displayed in English.
* **Description**: An array containing exactly four choice strings.
* **Required / Optional**: Required.
* **Data Type**: Array of strings.
* **Allowed Count**: Exactly 4 items.
* **Example**: `["Socialist, Secular, Integrity", "Liberty, Equality", "Justice, Fraternity", "Republic, Democratic"]`

### `options_ta`
* **Purpose**: The list of choices displayed in Tamil.
* **Description**: Direct Tamil translations matching the index positioning of `options_en`.
* **Required / Optional**: Required.
* **Data Type**: Array of strings.
* **Allowed Count**: Exactly 4 items.
* **Example**: `["சோசலிஸ்ட், மதச்சார்பின்மை, ஒருமை", "சுதந்திரம், சமத்துவம்", "நீதி, சகோதரத்துவம்", "குடியரசு, ஜனநாயகம்"]`

### Option Order and Indices
* Option indices (`0`, `1`, `2`, `3`) translate to the choice letters `"a"`, `"b"`, `"c"`, `"d"` respectively.
* Options must be unique; duplicate choices within the same list are not allowed.

---

## 6. Explanation Structure
The explanation blocks detail the rationale behind the correct answer:

### `explanation_en`
* **Purpose**: Clarifies why the answer is correct in English.
* **Description**: Details legal references, dates, math workings, or historical contexts.
* **Required / Optional**: Required.
* **Data Type**: String.
* **Example**: `"The 42nd Amendment of 1976 added three words: Socialist, Secular, and Integrity."`

### `explanation_ta`
* **Purpose**: Clarifies why the answer is correct in Tamil.
* **Description**: Tamil translation of `explanation_en`.
* **Required / Optional**: Required.
* **Data Type**: String.
* **Example**: `"1976 ஆம் ஆண்டின் 42வது திருத்தம் சோசலிஸ்ட், மதச்சார்பின்மை மற்றும் ஒருமைப்பாடு ஆகிய மூன்று சொற்களைச் சேர்த்தது."`

---

## 7. Difficulty System
Questions are partitioned into three distinct difficulty levels:

* **Easy (`"easy"`)**: Direct facts, simple formulas, single-clause statements.
* **Medium (`"medium"`)**: Short statement selections, multi-step math questions, key case laws.
* **Hard (`"hard"`)**: Assertion-Reason pairings, chronology ordering tables, complex statement matrices.

### Adaptive Difficulty State Machine
During a test session, the system evaluates student streaks to adjust difficulty for the next question (implemented in [difficulty_ai.py](file:///c:/Users/Home/Desktop/tnpsc_ai/core/difficulty_ai.py)):

```text
                  ┌──────────────────────┐
                  │      EASY LEVEL      │
                  └──────────┬───────────┘
                             │ (Streak >= 2)
                             ▼
                  ┌──────────────────────┐
                  │     MEDIUM LEVEL     │
                  └──────────┬───────────┘
               ▲             │             │
  (Streak >= 2)│             │             │(Wrong >= 2)
               │             ▼             ▼
         ┌─────┴────────┐            ┌─────┴────────┐
         │  HARD LEVEL  │            │  EASY LEVEL  │
         └──────────────┘            └──────────────┘
```

* **Upgrade Promotion**: A correct answer streak $\ge 2$ upgrades difficulty:
  * `"easy"` $\rightarrow$ `"medium"`
  * `"medium"` $\rightarrow$ `"hard"`
* **Downgrade Demotion**: A consecutive wrong answer count $\ge 2$ downgrades difficulty:
  * `"hard"` $\rightarrow$ `"medium"`
  * `"medium"` $\rightarrow$ `"easy"`
* **Loader Suffixes**: JSON files are named by appending difficulty suffixes:
  * `{topic_key}_easy.json`
  * `{topic_key}_medium.json`
  * `{topic_key}_hard.json`

---

## 8. Evaluation Flow
When a user submits an answer, the evaluation logic is executed sequentially:

1. **Option Index Lookup**: Maps the selected bilingual option string back to its index positioning:
   `selected_letter = ["a", "b", "c", "d"][options.index(selected)]`
2. **Comparison Check**: Compares `selected_letter` with the correct `"answer"` value (case-sensitive lowercase check).
3. **Streak Logging**: Increments correct/wrong streak trackers based on the comparison check result.
4. **Adaptive Progression**: Invokes `get_next_level()` to adjust the difficulty level (`st.session_state.level`) for the next question.
5. **Session Scoring**: Adds score points and awards `+10 XP` for correct choices.

---

## 9. UI Mapping
Every question attribute maps to a Streamlit UI component inside [daily_test_renderer.py](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/pages/daily_test_renderer.py):

* **`question_en` & `question_ta`** $\rightarrow$ **Question Glass Card**: Displays both statements sequentially in a glassmorphic container.
* **`options_en` & `options_ta`** $\rightarrow$ **st.radio Option Buttons**: Renders options as combined bilingual rows:
  `"English Option / Tamil Option"`
* **`explanation_en` & `explanation_ta`** $\rightarrow$ **Explanation Card panels**: Displays both English and Tamil explanation text below the correct answer block.
* **`answer`** $\rightarrow$ **Correct Option Header**: Shows the correct answer status (`Correct Answer: [Letter]`) inside a feedback card.

---

## 10. Validation Rules
All MCQ files must pass the following validation checks:
1. **List Integrity**: `options_en` and `options_ta` must contain exactly four non-empty strings.
2. **Key Validity**: Root `"answer"` value must be one of `"a"`, `"b"`, `"c"`, or `"d"` (must be lowercase).
3. **Subject and Topic Matching**: Root `"subject"` must be uppercase, and `"topic"` must match the lowercase snake_case key registered in curriculum structures.
4. **Completeness check**: Empty strings (`""`) or missing option translations are treated as validation errors.

---

## 11. Naming Conventions

* **Folder Naming**:
  * Root questions directory: `data/questions/`
  * Subjects subdirectories: lowercase matching the subject key (e.g. `polity`, `economy`, `history`).
* **JSON File Naming**:
  * Filenames must be structured as `{topic_key}_{level}.json`.
  * Suffixes must be strictly `_easy.json`, `_medium.json`, or `_hard.json`.
  * Example: `preamble_easy.json`

---

## 12. Backward Compatibility
1. **Lower-Case Key Enforcements**: The lowercase answer keys (`"a"`, `"b"`, `"c"`, `"d"`) must never be changed, as this would break index-mapping calculations.
2. **Optional Parameters**: Metadata details (e.g., `pyq_year`, `source_reference`) can be safely appended as optional root parameters without breaking core question loading logic.

---

## 13. Best Practices
1. **Translation Accuracy**: Ensure translations capture the correct context of legal and historical terms.
2. **Standardized Counts**: Every question must contain exactly 4 options.
3. **Standalone Explanations**: Explanations must be clear and explain *why* the option is correct, providing additional context where possible.

---

## 14. Quality Standards
* **Question Clarity**: Questions must be clear and avoid ambiguous wording.
* **Bilingual Alignment**: Terms must match across both English and Tamil statements.
* **Fact Accuracy**: Historical dates, case names, and constitution articles must be verified against official references.

---

## 15. Example JSON
Here is a sample MCQ question item ([preamble_easy.json](file:///c:/Users/Home/Desktop/tnpsc_ai/data/questions/polity/preamble_easy.json)):

```json
[
  {
    "question_en": "Consider the following statements:\n1. Preamble is part of the Constitution.\n2. It is enforceable in courts.\nWhich is correct?",
    "question_ta": "கூற்றுகள்:\n1. முன்னுரை அரசியலமைப்பின் பகுதி.\n2. இது நீதிமன்றத்தில் அமல்படுத்தலாம்.\nசரி எது?",
    "options_en": ["1 only", "2 only", "Both", "None"],
    "options_ta": ["1 மட்டும்", "2 மட்டும்", "இரண்டும்", "இல்லை"],
    "answer": "a",
    "explanation_en": "Preamble is part of the Constitution but not enforceable in courts.",
    "explanation_ta": "முன்னுரை அரசியலமைப்பின் பகுதி ஆனால் நீதிமன்றத்தில் அமல்படுத்த முடியாது.",
    "subject": "POLITY",
    "topic": "preamble"
  }
]
```

---

## 16. Schema Diagrams

### Question Data Schema
```text
 MCQ JSON Question
  ├── question_en (String)
  ├── question_ta (String)
  ├── options_en (Array of 4 Strings)
  ├── options_ta (Array of 4 Strings)
  ├── answer ("a" | "b" | "c" | "d")
  ├── explanation_en (String)
  ├── explanation_ta (String)
  ├── subject (String - UPPERCASE)
  └── topic (String - lowercase snake_case)
```

### Ingestion & Evaluation Flow
```text
  Get Topic & Level ──► Load JSON ──► Render Card ──► Radio Input ──► Evaluate
                                                                         │
                                                                         ▼
                                                             Update Streak & Level
```

---

## 17. Final Schema Freeze
The **TNPSC Nova AI MCQ Schema Specification (Version 1.0)** is hereby frozen. All future question collections, translation pipelines, and system validators must conform to the structures, indices, and validation rules specified in this document.
