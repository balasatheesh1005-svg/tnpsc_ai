# TNPSC Nova AI - Notes Schema Specification (Version 1.0)

This document is the official schema specification for **TNPSC Nova AI** revision notes JSON files. It serves as the single source of truth for the notes database structure and layout mappings.

---

## 1. Overview
The Notes System uses structured JSON configuration files to store bilingual revision sheets for students.
* Notes are parsed, dynamically loaded, and rendered inside the Streamlit user interface.
* Layouts are determined by the `"ui_type"` parameter inside the JSON file.
* Redirection triggers (`notes_practice_trigger`) allow seamless transition from a specific note sheet to topic-based adaptive practice questions.

---

## 2. Existing Schema Analysis
Every Notes JSON file has a top-level dictionary containing metadata and a nested `"content"` dictionary:
```json
{
  "subject": "SubjectName",
  "topic": "Human Readable Topic Name",
  "language": "bilingual",
  "ui_type": "polity | economy | history | aptitude | reasoning",
  "content": {
    "definition": {
      "en": "English definition",
      "ta": "தமிழ் வரையறை"
    },
    "...": "Subject-specific dynamic sections"
  }
}
```

---

## 3. Common Fields
These metadata fields are **required** at the root of every Notes JSON file:

### `subject`
* **Purpose**: Identifies the parent syllabus category.
* **Description**: Matches folder and curriculum tags.
* **Required / Optional**: Required.
* **Data Type**: String.
* **Allowed Values**: `"Polity"`, `"Economy"`, `"History"`, `"Aptitude"`, `"Reasoning"`, `"Geography"`, `"INM"`.
* **Example**: `"Polity"`
* **UI Component**: Main Selectbox header label.
* **Render Function**: [render_notes_page](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/pages/notes.py#L28-L65).

### `topic`
* **Purpose**: Human-readable title of the topic sheet.
* **Description**: Shown as the page title and alert context.
* **Required / Optional**: Required.
* **Data Type**: String.
* **Allowed Values**: Non-empty string.
* **Example**: `"Preamble of Indian Constitution"`
* **UI Component**: Page title header alert.
* **Render Function**: [render_notes](file:///c:/Users/Home/Desktop/tnpsc_ai/core/streamlit_ui_engine.py#L10-L11).

### `language`
* **Purpose**: Specifies language format.
* **Description**: Flags bilingual tab layout.
* **Required / Optional**: Required.
* **Data Type**: String.
* **Allowed Values**: `"bilingual"`.
* **Example**: `"bilingual"`
* **UI Component**: Implicitly triggers tab panels rendering.

### `ui_type`
* **Purpose**: Dictates layout templates and component grouping.
* **Description**: Directs routing inside the UI engine.
* **Required / Optional**: Required.
* **Data Type**: String.
* **Allowed Values**: `"polity"`, `"economy"`, `"history"`, `"aptitude"`, `"reasoning"`.
* **Example**: `"polity"`
* **UI Component**: Layout template selector.
* **Render Function**: [render_notes](file:///c:/Users/Home/Desktop/tnpsc_ai/core/streamlit_ui_engine.py#L17-L30).

---

## 4. Subject Specific Fields
The sub-structures inside `"content"` are routed dynamically according to `"ui_type"`:

### 🏛 Polity UI Layout (`ui_type == "polity"`)
* **`definition`** *(Object)*: Required. Bilingual core definition.
* **`acts` / `objectives`** *(Array of Objects)*: Optional. Sequential dynamic arrays.
* **`importance`** *(Object)*: Optional. Points list in English and Tamil.
* **Render Function**: `render_polity()`

### 💰 Economy & History Layouts (`ui_type == "economy" | "history"`)
* **`definition`** *(Object)*: Required. Bilingual core definition.
* **Dynamic Sections** *(Array of Objects)*: Optional. Loop-rendered collections (e.g. `origin_of_guptas`).
* **`timeline`** *(Array of Objects, History only)*: Optional. List of `year` and `event` keys.
* **`important_facts`** *(Object)*: Optional. List of fact alerts.
* **`current_affairs`** *(Array of Objects)*: Optional. Current connection points.
* **`mind_map`** *(Array of Strings)*: Optional. Simple tags arrays.
* **Render Function**: `render_economy()`, `render_history()`

### 🔢 Aptitude Layout (`ui_type == "aptitude"`)
* **`definition` / `exam_importance`** *(Object)*: Optional. Intro summaries.
* **`formula_sheet`** *(Array of Objects)*: Optional. Formulas in code blocks with explanation notes.
* **`core_concepts`** *(Array of Objects)*: Optional. Core syllabus concepts.
* **`shortcut_tricks`** *(Array of Objects)*: Optional. Dynamic shortcut calculations.
* **`exam_traps`** *(Array of Objects)*: Optional. Pitfalls highlighted in warning panels.
* **`solved_examples`** *(Array of Objects)*: Optional. Workouts inside Streamlit expanders.
* **`important_facts`** *(Object)*: Optional. Bilingual fact cards.
* **`quick_revision`** *(Object)*: Optional. Revision notes summaries.
* **`tnpsc_focus`** *(Object)*: Optional. Syllabus hotspots.
* **`mcqs` / `practice_mcqs`** *(Array of Objects)*: Optional. Practice question cards.
* **`expected_questions`** *(Array of Objects)*: Optional. Expected exam questions.
* **`mind_map`** *(Array of Objects/Strings)*: Optional. Summary tag hierarchies.
* **Render Function**: `render_aptitude()` (line 989 active)

### 🧠 Reasoning Layout (`ui_type == "reasoning"`)
* **`definition`** *(Object)*: Required. Intro definition.
* **`concept_rules`** *(Array of Objects)*: Optional. Rule lists.
* **`shortcut_methods`** *(Array of Objects)*: Optional. Trick steps in success boxes.
* **`common_mistakes`** *(Array of Objects)*: Optional. Pitfalls inside error boxes.
* **`solved_examples`** *(Array of Objects)*: Optional. Step-by-step example expanders.
* **`important_facts`** *(Object)*: Optional. Bilingual fact cards.
* **Render Function**: `render_reasoning()`

---

## 5. Nested Objects
Below is a detail of standard nested objects used in note files:

### `definition` & `exam_importance` & `important_facts`
Bilingual maps containing strings or lists:
```json
"definition": {
  "en": "Plaintext string or [\"Array of strings\"]",
  "ta": "Plaintext string or [\"Array of strings\"]"
}
```

### Dynamic Section Object
Used inside list keys inside Polity, Economy, and History:
```json
{
  "title": "Concept Subtitle Title",
  "points": {
    "en": [
      "Point description 1",
      "Point description 2"
    ],
    "ta": [
      "விளக்கம் 1",
      "விளக்கம் 2"
    ]
  }
}
```

### `timeline` Item
Used in History timelines:
```json
{
  "year": "320 CE",
  "event": "Event explanation string"
}
```

### `formula_sheet` Item
Used in Aptitude formulas:
```json
{
  "title": "Formula Name",
  "formula": "plaintext equation / LaTeX",
  "explanation": {
    "en": ["Explanation points"],
    "ta": ["விளக்கப் புள்ளிகள்"]
  }
}
```

### `solved_examples` Item
Used in Aptitude and Reasoning worked examples:
```json
{
  "title": "Example Title",
  "pyq": true,
  "year": 2019,
  "question": {
    "en": "Question text",
    "ta": "கேள்வி உரை"
  },
  "step1": { "en": "Step description", "ta": "படி விளக்கம்" },
  "step2": { "en": "Step description", "ta": "படி விளக்கம்" },
  "solution": { "en": "Solution working out", "ta": "தீர்வு விளக்கம்" },
  "answer": { "en": "Final answer value", "ta": "இறுதி விடை மதிப்பு" }
}
```

---

## 6. Data Types
* **Subject metadata (`subject`, `topic`, `ui_type`, `language`)**: String. Must not be null or empty.
* **Bilingual strings**: Dictionary containing `"en"` (string) and `"ta"` (string).
* **Bilingual arrays**: Dictionary containing `"en"` (array of strings) and `"ta"` (array of strings).
* **`timeline` year**: String or Integer.
* **`pyq`**: Boolean. Indicates that a section represents an official Previous Year Question.

---

## 7. UI Mapping

* **`definition`** $\rightarrow$ **st.info Card**: Bilingual info box with EN/TA tabs.
* **`timeline`** $\rightarrow$ **Markdown Timetable List**: Year formatted in bold alongside its event details.
* **`important_facts`** $\rightarrow$ **st.success Alert**: Success alert card containing bulleted statements.
* **`exam_traps` / `common_mistakes`** $\rightarrow$ **st.error / st.warning Panel**: Warning alert layout for traps.
* **`solved_examples`** $\rightarrow$ **st.expander Block**: Accordion panel detailing step-by-step solutions.
* **`formula_sheet`** $\rightarrow$ **st.code Block**: Math formula formatted inside code tags.
* **`mind_map`** $\rightarrow$ **Bulleted Lists**: Bullet-point lists compiling core keywords.

---

## 8. Validation Rules
Every Notes JSON file must comply with the following structural rules:
1. **Root Verification**: Dict structure must contain `subject`, `topic`, `language`, `ui_type`, and `content`.
2. **Translation Key Integrity**: All bilingual objects must have *both* `"en"` and `"ta"` keys. If a translation is missing, it must not be omitted (must write `""` or `[]` to prevent runtime dictionary `KeyError` crashes).
3. **Option list length**: Any list containing points (e.g. `points["en"]`) must have the exact same length as its translation counterpart (`points["ta"]`) for parallel list rendering.
4. **Valid UI Types**: The `ui_type` string must strictly match one of the active layout keys: `"polity"`, `"economy"`, `"history"`, `"aptitude"`, `"reasoning"`.

---

## 9. Naming Conventions

* **Folder Naming**:
  * Root notes directory: `data/notes/`
  * Subjects subdirectories: lowercase matching the subject key (e.g. `polity`, `economy`, `history`, `aptitude`, `geography`, `inm`).
* **JSON File Naming**:
  * The file name must match the formatted topic key (lowercase, removes special characters, replaces spaces with underscores).
  * Example: `"Historical Background"` $\rightarrow$ `historical_background.json`.
* **Syllabus Register**:
  * Topic list must be registered in the matching structure file `data/structure/{subject}_structure.json` under `"topics"`.

---

## 10. Backward Compatibility
1. **Preserved UI Types**: The core layout types (`"polity"`, `"economy"`, `"history"`, `"aptitude"`, `"reasoning"`) must never be renamed or deleted, as they are hardcoded in the [streamlit_ui_engine.py](file:///c:/Users/Home/Desktop/tnpsc_ai/core/streamlit_ui_engine.py) router.
2. **Extensible Sections**: New sections can be safely added to the `"content"` dictionary in Polity, Economy, and History notes. The loops will dynamically render them as subheaders without requiring UI code modifications.
3. **Optional Parameters**: All sections under `"content"` (other than `"definition"`) are optional. If a key is missing or set to `null`/`[]`, the UI engine skips rendering it without failing.

---

## 11. Best Practices
1. **Bilingual Completeness**: Always compile complete translations for both English and Tamil.
2. **Double-Newline Safety**: Ensure no single newlines are inside notes content blocks where double-newlines (`\n\n`) are used as section dividers.
3. **Clean Code Blocks**: Keep formulas clean (either plaintext or standard LaTeX formatting).
4. **Sampler Constraints**: Keep the topic names registered in `polity_structure.json` consistent with notes folders to prevent broken file paths.

---

## 12. Example JSON
Here is an example notes sheet conforming to the **Polity** layout structure ([preamble.json](file:///c:/Users/Home/Desktop/tnpsc_ai/data/notes/polity/preamble.json)):

```json
{
  "subject": "Polity",
  "topic": "Preamble of Indian Constitution",
  "language": "bilingual",
  "ui_type": "polity",
  "content": {
    "definition": {
      "en": "The Preamble is the introductory statement of the Constitution that contains its philosophy, objectives and ideals.",
      "ta": "முன்னுரை என்பது அரசியலமைப்பின் அறிமுகப் பகுதி ஆகும். இது அதன் இலக்குகள், தத்துவம் மற்றும் அடிப்படை மதிப்புகளை விளக்குகிறது."
    },
    "acts": [
      {
        "title": "Sovereign",
        "points": {
          "en": [
            "India is free from external control",
            "No foreign authority can control India"
          ],
          "ta": [
            "இந்தியா வெளிநாட்டு கட்டுப்பாட்டிலிருந்து சுதந்திரமானது",
            "வேறு நாடு கட்டுப்படுத்த முடியாது"
          ]
        }
      }
    ],
    "importance": {
      "en": [
        "Reflects philosophy of Constitution",
        "Guides interpretation of laws"
      ],
      "ta": [
        "அரசியலமைப்பின் தத்துவத்தை காட்டுகிறது",
        "சட்ட விளக்கத்திற்கு உதவும்"
      ]
    }
  }
}
```

---

## 13. Schema Diagram
```text
  Notes JSON File
   ├── subject (String)
   ├── topic (String)
   ├── language ("bilingual")
   ├── ui_type ("polity" | "economy" | "history" | "aptitude" | "reasoning")
   └── content (Object)
        ├── definition (Bilingual String/Array)
        └── [Subject Specific Elements]
             ├── acts/objectives/timeline (Arrays of bilingual objects)
             ├── formula_sheet/solved_examples (Arrays of mathematical schemas)
             └── important_facts/exam_traps (Bilingual arrays/warnings alerts)
```

---

## 14. Recommendations
1. **Clean Redundant Codes**: Delete lines 382–495 and lines 497–987 inside `core/streamlit_ui_engine.py` (duplicate `render_aptitude` declarations) to keep code clean.
2. **Refactor Renderers**: Split the monolithic `streamlit_ui_engine.py` into separate layouts (e.g. `polity.py`, `economy.py`, `aptitude.py`) inside a new package `core/notes_renderers/` for ease of maintenance.
3. **Automate Notes Ingestion Audits**: Write a schema auditing tool verifying bilingual alignment keys inside `data/notes/` before merging new note additions.

---

## 15. Final Schema Freeze
The **TNPSC Nova AI Notes Schema Specification (Version 1.0)** is hereby frozen. All future content ingestion and formatting pipelines must conform to the structures, field namings, and validation rules specified in this document.
