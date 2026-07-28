# TNPSC Nova AI — Current User Flow Audit

---

## 1. Complete Current User Flow Diagram

```
[ LOGIN / SIGNUP SCREEN ]
         │
         ▼
  [ AUTHENTICATED ]
         │
         ├────────────────────────────────────────────────────────────────────────┐
         │                                                                        │
         ▼                                                                        ▼
┌──────────────────┐                                                    ┌──────────────────┐
│ SIDEBAR MAIN MENU│                                                    │ HOME PAGE VIEW   │
└────────┬─────────┘                                                    └────────┬─────────┘
         │                                                                       │
         ├─► 🏠 Home ────────────────────────────────────────────────────────────┘
         │
         ├─► 📘 Daily Test ────────► [Daily Test Setup]
         │                                │
         │                                ├─► Start Daily Test ──► [Question Renderer] ──► [Answer Submit] ──► [Explanation]
         │                                │                                                                         │
         │                                │                                                                         ▼
         │                                │                                                                [Last Question Submitted]
         │                                │                                                                         │
         │                                │                                                                         ▼
         │                                │                                                                  [DEAD END 🛑]
         │                                │                                                         (Reruns to Daily Test Setup,
         │                                │                                                          no Result Screen shown)
         │                                │
         │                                ├─► Practice Weak Topics ──► [Loads 5 Weak Qs] ──► (Same loop)
         │                                └─► Start Revision Test ──► [Loads 5 Rev Qs]  ──► (Same loop)
         │
         ├─► PYQ ──────────────────► [PYQ Dashboard] ──► [BROKEN FLOW ⚠️] (Select Year/Subject, hardcoded viewer)
         │
         ├─► 📚 Notes ─────────────► [Topic Notes Viewer] ──► Read Notes ──► [Practice Questions Button]
         │                                                                             │
         │                                                                             ▼
         │                                                                  [Switches to Daily Test]
         │
         ├─► 🧠 Weakness ──────────► [Weakness Heatmap] ──► [DEAD END 🛑] (View static dataframe; no practice button)
         │
         ├─► 📊 Progress ──────────► [Progress Dashboard] ─► [DEAD END 🛑] (View static dataframes; no topic link)
         │
         ├─► 🏆 Leaderboard ───────► [Leaderboard View] ──► [DEAD END 🛑] (View top 10; no social interaction)
         │
         ├─► 🤖 AI Teacher ────────► [AI Doubt Box] ──────► Type query ──► Click Ask ──► [View Keyword Match Text]
         │
         ├─► 👨‍🏫 Personal Mentor ──► [Mentor Chat View] ─► View static advice text & chat history
         │
         ├─► ℹ️ About ─────────────► [About Page View]
         │
         └─► 📞 Contact ───────────► [Contact Page View]

───────────────────────────────────────────────────────────────────────────────────────────
[ HOME TAB NAVIGATION V2 FLOW ]

  [ 🏠 Home Page ]
         │
         ├─► nav_view == "subject_select" ──► [Subject Selector] ──► Click Subject ──► nav_view = "topic_select"
         │                                                                                  │
         ├─► nav_view == "topic_select"   ──► [Topic Selector]   ──► Click Topic   ──► nav_view = "topic_hub"
         │                                                                                  │
         └─► nav_view == "topic_hub"      ──► [ TOPIC HUB WORKSPACE ]                       │
                                                      │                                     │
                                                      ├─► Read Notes ──► Switches menu to 📚 Notes
                                                      ├─► Start GT   ──► Switches menu to 📘 Daily Test (GT Repo)
                                                      ├─► AI Teacher ──► Pre-fills prompt & switches to 🤖 AI Teacher
                                                      │
                                                      ├─► Practice Repositories (Easy/Medium/Hard/Statements/AR/Match/Chrono)
                                                      │        │
                                                      │        ├─► Easy ──► [Practice Setup Card] ──► Start Practice
                                                      │        │                                           │
                                                      │        │                                           ▼
                                                      │        │                                  Switches to 📘 Daily Test
                                                      │        │
                                                      │        └─► Other ──► Directly switches to 📘 Daily Test
                                                      │
                                                      └─► Topic Toolkit:
                                                               ├─► Smart Revision ──► Switches menu to 🧠 Weakness
                                                               ├─► Topic Analytics──► Switches menu to 📊 Progress
                                                               └─► PYQ Explorer   ──► Switches menu to PYQ
```

---

## 2. Screen-by-Screen Audit Findings

### 1. Daily Test Completion Screen `[DEAD END 🛑]`
- **Location**: `app.py` line 785-830
- **Issue**: After completing the last question of a test, `complete_test()` runs, updates database tables, and sets `test_active = False`. The user is immediately dropped back to the top of the Daily Test page with the 3 start buttons.
- **User Impact**: Anti-climactic. The student gets no detailed breakdown of right vs wrong answers, no list of topics to review, and no button to return to the Topic Hub.

### 2. Practice Repository Launch `[DUPLICATE & CONFUSING FLOW ⚠️]`
- **Location**: `ui/navigation_v2/topic_hub.py` lines 277-330
- **Issue**: Clicking "Easy" opens an in-page "Practice Setup" card with question count and instructions. But clicking "Medium", "Hard", or "Statement Based" completely bypasses the setup card and forcibly switches the active sidebar menu to `📘 Daily Test`!
- **User Impact**: Disorienting. The student was working inside the Topic Hub and suddenly finds themselves navigated to a totally different sidebar page.

### 3. Weakness Dashboard `[DEAD END 🛑]`
- **Location**: `ui/pages/weakness.py`
- **Issue**: Displays a styled pandas table highlighting weak topics in red (`Weakness >= 4`). However, none of the rows are interactive. There is no "Practice This Topic Now" button next to red items.
- **User Impact**: Frustration. The student sees that they are weak in "Polity - Preamble", but must manually navigate to Home -> Subject -> Polity -> Preamble to fix it.

### 4. Progress Dashboard `[DEAD END 🛑]`
- **Location**: `ui/pages/progress.py`
- **Issue**: Displays part-level and repository-level accuracy tables. Like the Weakness page, it is entirely read-only with no direct links to study notes or practice sets.

### 5. Bookmark System `[MISSING FLOW ❌]`
- **Location**: `core/question_engine/bookmark.py` & `ui/question_engine/header_component.py`
- **Issue**: Question Header allows clicking a Bookmark button during a test. However, there is no page in the sidebar menu or profile to view bookmarked questions. Furthermore, bookmarks are saved only in session state!

### 6. Achievement & Badge System `[MISSING FLOW ❌]`
- **Location**: `core/xp_ai.py`
- **Issue**: Backend logic awards XP for perfection and 7-day streaks, but there is no screen in the app that displays unlocked badges, trophies, or milestone progress.

### 7. PYQ Dashboard `[BROKEN FLOW ⚠️]`
- **Location**: `ui/pyq/dashboard.py`
- **Issue**: Renders hardcoded paper selectors (`Group 1 2021`, `Group 1 2022`). Selecting a paper loads raw JSON questions into a static scroll view without interactive timer, scoring, or progress saving.

### 8. AI Teacher Interface `[DISCONNECTED FLOW ⚠️]`
- **Location**: `ui/pages/teacher.py`
- **Issue**: Located as a standalone sidebar menu option. When launched from Topic Hub, it prepends prompt text in session state, but the text box does not automatically lock to the active topic context or maintain past chat history.
