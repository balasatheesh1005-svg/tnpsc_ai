# TNPSC Nova AI — Practice Engine User Flow Specification

---

## 1. End-to-End Practice User Flow

```
[ TOPIC HUB WORKSPACE ]
          │
          ├─► Select Repository Type (Easy / Medium / Hard / Statement / AR / Match / Chrono / PYQ)
          │
          ▼
   [ start_practice_session() ]
          │
          ├─► Loads COMPLETE question repository payload from JSON
          ├─► Initializes practice_* session state variables
          │
          ▼
   [ PRACTICE WORKSPACE ]
          │
          ├─► Universal Question Renderer Header (Progress %, Timer, Badges)
          ├─► Language Mode Toggle (EN / TA / BOTH)
          ├─► Question Palette & Jump Navigation
          ├─► Option Cards Selection
          │
          ▼
   [ Click "Submit Answer" ]
          │
          ├─► Records answer in practice_answers
          ├─► Evaluates correctness & updates practice_score
          ├─► Displays Explanation Card with article references
          │
          ▼
   [ Click "Next ➡️" / "Finish Practice 🏁" ]
          │
          ├─► If questions remain: Advances practice_current_index += 1
          └─► If final question: Sets practice_completed = True
                                        │
                                        ▼
                           [ PRACTICE RESULT SCREEN ]
                                        │
                                        ├─► Displays: Repository Name, Total Qs, Correct, Wrong,
                                        │             Accuracy %, Time Taken, XP Earned
                                        ├─► Saves progress to users_progress DB table
                                        ├─► Awards Practice XP (+10 XP per correct answer)
                                        │
                                        ├─► [ 📖 Review Answers ] ─────► [ Practice Review Mode ]
                                        │                                       │
                                        │                                       └─► Return to Performance Summary
                                        ├─► [ 🔄 Practice Again ] ─────► Re-launches same repo session
                                        ├─► [ ➡️ Next Repository ] ────► Launches next difficulty repo
                                        └─► [ ⬅️ Return to Topic Hub ]─► Calls clear_practice_session()
                                                                                │
                                                                                ▼
                                                                     [ RETURN TO TOPIC HUB ]
```

---

## 2. Screen State & Interaction Transitions

### Screen 1: Topic Hub Repository Launcher
- **Trigger**: Student clicks "Start Practice" or "Start [Repository Type]" in Topic Hub.
- **Action**: Calls `start_practice_session(subject, topic_id, repository_id, display_title, repo_type)`.
- **Navigation**: Reruns inside Topic Hub workspace without changing top menu tab.

### Screen 2: Practice Question Interface
- **Components**:
  - Top Control Bar with `⬅️ Exit Practice` button.
  - Header with live timer, progress bar (`Question X / Y`), subject, difficulty, and bloom level badges.
  - Expandable Question Palette for jump navigation.
  - Question body and bilingual option cards.
  - Submit button, Previous button, and Next/Finish button.
  - Post-submit explanation component.

### Screen 3: Practice Result Screen
- **Components**:
  - Header Glass Card showing Repository Name, Repository Type, Accuracy %, and Time Taken.
  - Metrics Grid displaying Attempted Count, Correct Count, Wrong Count, Accuracy %, Elapsed Time, and XP Earned.
  - Dynamic Feedback Callout (Excellent / Good / Practice Needed).
  - 4 Action Buttons: `[ 📖 Review Answers ]`, `[ 🔄 Practice Again ]`, `[ ➡️ Next Repository ]`, `[ ⬅️ Return to Topic Hub ]`.

### Screen 4: Practice Review Mode
- **Components**:
  - Header bar with `⬅️ Back to Performance Summary` button.
  - Complete list of questions with student choice status (🟢 Correct vs 🔴 Incorrect/Skipped) and detailed explanations.
