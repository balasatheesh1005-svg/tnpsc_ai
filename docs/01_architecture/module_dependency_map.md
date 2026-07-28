# TNPSC Nova AI — Module Dependency & Architecture Map

---

## 1. System Architecture Layers

TNPSC Nova AI is structured across 4 functional layers:

```
┌────────────────────────────────────────────────────────────────────────┐
│                        1. PRESENTATION LAYER (UI)                     │
│  app.py • dashboard.py • topic_hub.py • notes.py • daily_test_renderer │
│  universal_renderer.py • progress.py • weakness.py • leaderboard.py    │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        2. NAVIGATION & ROUTING                         │
│  navigation_state.py • topic_selector.py • subject_selector.py        │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                      3. BUSINESS & AI LOGIC (CORE)                     │
│  test_completion.py • test_evaluator.py • xp_ai.py • streak_ai.py    │
│  weakness_ai.py • progress_ai.py • revision_ai.py • ai_teacher.py     │
│  mentor_ai.py • question_loader.py • topics_loader.py                  │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                   4. DATA & PERSISTENCE LAYER (SUPABASE)              │
│  users_progress • user_xp • users_streak • user_revisions              │
│  users_weakness • mentor_memory • JSON Files (Notes & Questions)       │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Core Service Dependency Matrix

Below is the comprehensive interaction matrix mapping which core modules depend on each other:

| Module | Consumes (Inputs From) | Feeds (Outputs To) | Database Tables |
|---|---|---|---|
| `app.py` | `auth.py`, `session.py`, `dashboard_stats_ai`, `navigation_state`, `question_loader`, `test_evaluator`, `test_completion` | UI Rendering Loop | `users_progress`, `user_xp`, `users_streak` |
| `navigation_state.py` | `topics_loader.py`, `st.session_state` | `topic_hub.py`, `notes.py`, `universal_renderer.py` | N/A (State) |
| `test_completion.py` | `ai_coach.py`, `mentor_memory.py`, `progress_ai.py`, `streak_ai.py`, `weakness_ai.py`, `xp_ai.py` | `app.py`, Result Component | `users_progress`, `user_xp`, `users_streak` |
| `test_evaluator.py` | Raw option choice, correct key | `test_weakness.py`, `test_revision.py` | N/A (Evaluation) |
| `xp_ai.py` | `supabase_client.py` | `test_completion.py`, `dashboard_stats_ai.py`, UI Headers | `user_xp` |
| `streak_ai.py` | `supabase_client.py`, `datetime` | `test_completion.py`, `dashboard_stats_ai.py` | `users_streak` |
| `weakness_ai.py` | `supabase_client.py` | `ai_teacher.py`, `mentor_ai.py`, `weakness.py` (UI) | `users_weakness` |
| `progress_ai.py` | `supabase_client.py`, `topics_loader.py` | `dashboard_stats_ai.py`, `progress.py` (UI) | `users_progress` |
| `revision_ai.py` | `supabase_client.py`, `datetime` | `daily_mission_ai.py`, `app.py` | `user_revisions` |
| `ai_teacher.py` | `topics_loader.py`, Static JSON Notes, `weakness_ai.py` | `teacher.py` (UI), Explanation Component | Static JSON Files |
| `universal_renderer.py`| `parser.py`, `body_component`, `option_component`, `footer_component`, `explanation_component` | `topic_hub.py` (Practice Setup) | N/A (UI Component) |

---

## 3. Data Flow & Call Stack Diagrams

### Test Execution & Completion Call Stack

```
[User Clicks Option & Submit]
          │
          ▼
   app.py / universal_renderer
          │
          ├──────────────────────────► evaluate_answer()
          │                                  │
          │                                  ├─► handle_correct_answer() / handle_wrong_answer()
          │                                  │        │
          │                                  │        └─► Supabase: users_weakness
          │                                  │
          │                                  └─► handle_correct_revision() / handle_wrong_revision()
          │                                           │
          │                                           └─► Supabase: user_revisions
          │
[Last Question Completed]
          │
          ▼
   complete_test()
          │
          ├─► ai_coach() ────────────► Generates feedback string
          ├─► update_memory() ───────► Supabase: mentor_memory
          ├─► update_streak() ───────► Supabase: users_streak
          ├─► add_xp() ──────────────► Supabase: user_xp (+50 completion, +50 bonus)
          ├─► save_progress() ───────► Supabase: users_progress
          └─► get_dashboard_stats() ─► Refreshes st.session_state stats
```

---

## 4. Architectural Bottlenecks & Risk Points

1. **Tight Coupling in `app.py`**:
   `app.py` directly handles routing, login CSS, dashboard stats fetching, test execution logic, score evaluation, level up checks, and menu rendering. This violates single responsibility principles.

2. **Dual Question Engines**:
   - `ui/pages/daily_test_renderer.py` operates independently from `ui/question_engine/universal_renderer.py`.
   - `daily_test_renderer.py` uses legacy radio button lists, whereas `universal_renderer.py` uses modular sub-components (`header_component`, `body_component`, `option_component`, `footer_component`).

3. **Orphaned Persistence Tables**:
   - `user_revisions` is updated by `revision_ai.py` but has no dedicated UI view.
   - `mentor_memory` stores AI mentor logs, but `ui/pages/mentor.py` reads from `st.session_state.mentor_chat` instead of reading from `mentor_memory` on initial load!
