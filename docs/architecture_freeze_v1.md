# TNPSC Nova AI - Architecture Freeze Document v1.0

This document outlines the technical specification and architecture freeze for the **TNPSC Nova AI** core platforms, including study notes, adaptive practice tests (MCQs), data routing directories, file safety guidelines, and architectural rules.

---

## 1. Project Overview
The TNPSC Nova AI platform is designed to provide bilingual study notes, Previous Year Questions (PYQs), and adaptive practice questionnaires for the TNPSC Group-I exam. It separates layout views, core business logic, and local database file content:
* **UI views** are handled by Streamlit.
* **Metadata extraction and classifications** are automated via ETL scripts.
* **Data storage** is stored in human-readable JSON files, optimizing load times with cache controls.

---

## 2. Folder Structure
The repository is organized into distinct subdirectories:

```text
c:\Users\Home\Desktop\tnpsc_ai
├── app.py                      # Application router and layout setup
├── build_2015_repo.py          # ETL builder script for the 2015 questions
├── build_2021_repo.py          # ETL builder script for the 2021 questions
├── build_2022_repo.py          # ETL builder script for the 2022 questions
├── convert_schema.py           # In-place schema converter utility
├── assets/                     # Custom graphics, CSS styles, and typography
├── core/                       # Business logic and adaptive engines
│   ├── question_engine/        # Low-level MCQ engine (bookmarks, loaders, validators)
│   │   ├── answer_key.py       # Official key loader and validator
│   │   ├── repository.py       # Data access repository layer
│   │   ├── validators.py       # JSON schema checks
│   │   └── ...
│   ├── adaptive_ai.py          # User profile adaptive learning controllers
│   ├── difficulty_ai.py        # Difficulty state progression machine
│   ├── streamlit_ui_engine.py  # Consolidated notes rendering layouts
│   ├── test_evaluator.py       # Score and answer verification engine
│   └── ...
├── data/                       # Local JSON database files
│   ├── notes/                  # Study revision sheets by subject
│   ├── official/               # Official verified answer key registers
│   ├── pyq/                    # Previous Year Question repositories
│   ├── questions/              # Practice questions by subject/topic/level
│   ├── structure/              # Subject syllabus topic registers
│   └── ...
├── tools/                      # Developer ETL classifiers and ingestion tools
│   ├── import_pipeline/
│   └── import_pipeline_v2/
└── ui/                         # Page templates and page-specific controllers
    ├── components/             # Custom widgets and UI cards
    ├── pages/                  # Streamlit page view controllers (notes, test, etc.)
    └── ...
```

---

## 3. Notes Flow
The user navigates from topic selection to rendering notes on the screen:

```text
       User Selection (Subject, Topic)
                     │
                     ▼
            notes.py (UI Page)
                     │
                     ▼
         load_note() (Cached Ingest)
                     │
                     ▼
         streamlit_ui_engine.py (Routing)
         ├── polity    ──► render_polity()
         ├── economy   ──► render_economy()
         ├── history   ──► render_history()
         ├── aptitude  ──► render_aptitude()
         └── reasoning ──► render_reasoning()
                     │
                     ▼
            Bilingual Tab Layout (EN/TA)
```

---

## 4. MCQ Flow
Adaptive testing starts from selection, loops questions, verifies correctness, and saves stats:

```text
          Test Selection (Daily/Notes Practice)
                         │
                         ▼
        question_loader.py (Cached loading)
                         │
                         ▼
        daily_test_renderer.py (Render widget)
                         │
                         ▼
           User Choice (Submit radio key)
                         │
                         ▼
        test_evaluator.py (Verify answer)
           ├── Correct ──► Award XP, increase correct_streak, reset wrong_count
           └── Wrong   ──► Reset correct_streak, increase wrong_count
                         │
                         ▼
        difficulty_ai.py (Adjust level for next question)
                         │
                         ▼
        Loop repeats (for all sample questions)
                         │
                         ▼
        complete_test() (Log progress and user stats)
```

---

## 5. JSON Locations

| Category | Storage Path | JSON Format |
| :--- | :--- | :--- |
| **Syllabus Structures** | `data/structure/{subject}_structure.json` | Subject meta-data and list of topic headings. |
| **Bilingual Study Notes** | `data/notes/{subject}/{topic_key}.json` | Multi-section strings, lists, formula codes, and timlines by `ui_type`. |
| **Practice Questions** | `data/questions/{subject}/{topic_key}_{level}.json` | Array of MCQ dictionaries (question, options, keys, explanations) by level. |
| **PYQ Repositories** | `data/pyq/{exam}/{filename}.json` | Verified official exam questions matching flat database keys. |
| **Verified Answer Keys** | `data/official/answer_keys/{exam}/{filename}.json` | Official verified key choices maps by question ID. |
| **User Progress Logs** | `data/progress.json` | Completed tests logs, dates, accuracy, and user identifiers. |
| **Revision Queues** | `data/revision.json` | Scheduling records for spaced repetition queues. |
| **User Login Streaks** | `data/streak.json` | Consecutive daily login counters. |
| **User Weakness Logs** | `data/weakness.json` | Aggregated analytics flags for weak subjects/topics. |
| **Mentor Memories** | `data/mentor_memory.json` | AI personal memory strings and chat context data. |

---

## 6. Safe Files (Content Files)
Adding or modifying content in these directories updates resources without risking core crashes:
* `data/structure/` (syllabi)
* `data/notes/` (study sheets)
* `data/questions/` (curated questions)
* `data/pyq/` (exam databases)

---

## 7. Core Files (Do Not Modify)
Modifying these modules can compromise user sessions, difficulty adjustment logic, and layout rendering templates:
* `core/streamlit_ui_engine.py` (Visual layout rendering)
* `core/test_evaluator.py` (Scoring and metrics calculator)
* `core/difficulty_ai.py` (Adaptive level state transitions)
* `core/question_engine/validators.py` (Data checker constraints)

---

## 8. Dependency Graph

### Notes Dependencies
```text
data/structure/*_structure.json ──► topics_loader.py ──┐
                                                      ▼
data/notes/**/*.json ──────────────► load_note() ──► notes.py (UI Page View)
                                                      │
                                                      ▼
                                             streamlit_ui_engine.py (render_notes)
```

### MCQ Dependencies
```text
data/questions/**/*.json ────► question_loader.py ────┐
                                                     ▼
st.session_state.level ──────► difficulty_ai.py ──► app.py (Session Controller)
                                                     │
                                                     ▼
                                            test_evaluator.py (evaluate_answer)
                                                     │
                                                     ▼
                                            daily_test_renderer.py (render_question)
```

---

## 9. Architecture Rules
1. **Curriculum Registration**: Any new topic must be added to the subject's structure JSON file in `data/structure/` before adding content notes or question sheets.
2. **Notes Layout Constraints**: Note files must match their declared `ui_type` structure:
   * `"polity"`: Requires `definition` and sub-item objects (`title` & `points`).
   * `"economy"` / `"history"`: Requires `definition`, dynamic section arrays, and optionally `important_facts`, `timeline`, and `current_affairs`.
   * `"aptitude"` / `"reasoning"`: Requires `definition`, `formula_sheet` (or `concept_rules`), `shortcut_tricks`, and `solved_examples`.
3. **Bilingual Requirement**: All content strings (questions, notes, and explanations) must be provided in both English and Tamil.
4. **Option formatting**:
   * Practice MCQs must separate English and Tamil options into `options_en` and `options_ta` lists inside the JSON schema.
   * PYQ database repositories must combine English and Tamil options using the `\n` newline character separator (e.g. `"Options English\nOptions Tamil"`).
5. **Answer Key Keys**:
   * Practice MCQs must write answer choices as a lowercase letter (`"a"`, `"b"`, `"c"`, `"d"`).
   * PYQs must map correct answer lists (`correct_answers`: array of strings) and follow multi-answers standards (`["A", "C"]` for A/C, `["A", "B", "C", "D"]` for ALL).
6. **Difficulty Transitions**: Real-time progression algorithms in `core/difficulty_ai.py` must stay decoupled from user profile database updates.

---

## 10. Improvements
1. **Redundant Function Cleanup**: Safely delete the inactive implementations of `render_aptitude` (lines 382–495 and lines 497–987) in `core/streamlit_ui_engine.py` to remove dead code.
2. **UI Monolith Modularization**: Split the layout templates in `streamlit_ui_engine.py` into separate scripts under a new folder `core/notes_renderers/` (e.g., `polity.py`, `economy.py`, `aptitude.py`) to shrink the file size.
3. **Introduce Notes and MCQ Validators**: Extend the question validator rules in `core/question_engine/validators.py` to create schema validators for notes files and practice questions, catching syntax errors before production checks.
4. **Bilingual Layout Helpers**: Extract repeating `st.tabs` block definitions inside `streamlit_ui_engine.py` into a single reusable bilingual tab helper.
