# TNPSC Nova AI — Practice Engine Architecture v1.0
**Architectural Specification & Decoupled Learning Engine Design**

---

## 1. Overview

The Practice Engine v1.0 establishes **Practice as an independent learning workflow** completely decoupled from the Daily Test session.

Prior to this refactor, Practice sessions incorrectly reused Daily Test session variables (`test_active`, `test_qs`, `q_index`, `test_mode`), causing Daily Test state pollution, artificial 10-question truncation, execution of daily mission logic on practice sets, and abrupt blank screens after submission.

The refactored Practice Engine operates under a dedicated session state namespace (`practice_*`), loads complete repository payloads, exclusively uses the `UniversalRenderer` system, and presents a dedicated Practice Result Screen with closed-loop navigation back to the Topic Hub.

---

## 2. Decoupled Architecture Blueprint

```
┌────────────────────────────────────────────────────────────────────────┐
│                        TOPIC HUB WORKSPACE                             │
│  • Rendered under 🏠 Home -> 🎯 Topic Hub Workspace                    │
│  • Monitors st.session_state["practice_active"]                        │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                    DEDICATED PRACTICE SESSION                          │
│                    (core/question_engine/practice_session.py)          │
│  • practice_active = True                                              │
│  • Loads complete repository via load_questions(repo_id, repo_type)    │
│  • Manages practice_questions, practice_current_index, practice_score  │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                      UNIVERSAL QUESTION RENDERER                       │
│                     (ui/question_engine/practice_renderer.py)          │
│  • UniversalQuestionAdapter & NormalizedQuestion                       │
│  • Bilingual Toggle (EN / TA / BOTH)                                   │
│  • Live elapsed timer & Question Palette jump navigation               │
│  • Option cards & Distractor explanations                             │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        PRACTICE RESULT SCREEN                          │
│  • Calculates: Correct, Wrong, Accuracy %, Time Taken, XP Earned       │
│  • Saves progress via save_progress() & awards Practice XP (+10/correct)│
│  • Actions:                                                            │
│    [ 📖 Review Answers ]  [ 🔄 Practice Again ]                        │
│    [ ➡️ Next Repository ] [ ⬅️ Return to Topic Hub ]                  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Session State Isolation Specification

To guarantee 100% decoupling, Practice and Daily Test utilize completely separated state keys:

| State Variable | Practice Engine Namespace | Daily Test Namespace | Isolation Status |
|---|---|---|---|
| Active Flag | `st.session_state["practice_active"]` | `st.session_state["test_active"]` | 🟢 100% Isolated |
| Subject | `st.session_state["practice_subject"]` | `st.session_state["test_subject"]` | 🟢 100% Isolated |
| Topic ID | `st.session_state["practice_topic_id"]` | `st.session_state["test_topic_id"]` | 🟢 100% Isolated |
| Repo ID | `st.session_state["practice_repository_id"]` | `st.session_state["test_repository_id"]` | 🟢 100% Isolated |
| Repo Type | `st.session_state["practice_repository_type"]` | `st.session_state["test_mode"]` | 🟢 100% Isolated |
| Question Stack | `st.session_state["practice_questions"]` | `st.session_state["test_qs"]` | 🟢 100% Isolated (Full repo loaded) |
| Current Index | `st.session_state["practice_current_index"]` | `st.session_state["q_index"]` | 🟢 100% Isolated |
| Score | `st.session_state["practice_score"]` | `st.session_state["score"]` | 🟢 100% Isolated |
| Answers Map | `st.session_state["practice_answers"]` | `st.session_state["answered"]` | 🟢 100% Isolated |
| Timestamps | `st.session_state["practice_start_time"]` | `st.session_state["start_time"]` | 🟢 100% Isolated |
| Completed Flag | `st.session_state["practice_completed"]` | `st.session_state["test_results_processed"]` | 🟢 100% Isolated |

---

## 4. Key Component Specifications

### 1. `core/question_engine/practice_session.py`
- `start_practice_session(subject, topic_id, repository_id, display_title, repository_type)`: Initializes practice state, loads question JSON file without capping at 10.
- `record_practice_answer(question_index, selected_option, is_correct, question_id)`: Logs user choice for the active index and updates score.
- `next_practice_question()`: Advances index or sets `practice_completed = True` when all questions are answered.
- `complete_practice_session(user)`: Saves accuracy to `users_progress` DB table and awards practice XP (`+10 XP per correct answer`). Does NOT call `update_daily_test` or daily mission handlers.
- `clear_practice_session()`: Clears all `practice_*` session keys cleanly.

### 2. `ui/question_engine/practice_renderer.py`
- `render_practice_workspace(user)`: Top-level workspace router switching between Question View, Result Screen, and Review Mode.
- `render_practice_result_screen(user)`: Glass card result screen displaying summary metrics, feedback banners, and action buttons.
- `render_practice_review(user)`: Interactive review mode allowing students to inspect all questions with chosen vs correct options and explanations.
