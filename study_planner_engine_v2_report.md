# TNPSC Nova AI - Phase 5 Sprint 4 Report
## Personal Study Planner Engine V2 & Personal Study Planner Dashboard

---

### 1. Executive Summary

Phase 5 Sprint 4 introduces the central planning engine of TNPSC Nova AI: **Personal Study Planner Engine V2**.

Unlike static timetables or basic schedules, this sprint establishes a reusable, deterministic study planning engine ([core/study_planner_ai.py](file:///c:/Users/Home/Desktop/tnpsc_ai/core/study_planner_ai.py)) that synthesizes output from Learning Intelligence Engine V2, Revision Engine V2, Mission Engine, Progress Engine, Weakness Engine, Streak, and XP Engines into personalized daily study plans.

**Key Architectural Highlights**:
- **Central Master Planning Engine**: Acts as the single planning brain for Today's Plan, Weekly Plan, Daily Mission, AI Mentor Directives, and Future AI Modules.
- **Zero UI Calculation**: The [Personal Study Planner Dashboard](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/planner/dashboard.py) performs **zero** business or planning logic — it strictly visualizes the JSON output produced by `core/study_planner_ai.py`.
- **Deterministic Prioritization Rules**: Tasks are prioritized strictly based on learning needs: *Overdue Revision → Current Bottleneck → Recovery Plan → Daily Mission → Topic Progress → Optional Practice*.
- **Dynamic Available Time Adaptation**: Automatically scales and caps candidate study tasks based on user-selected time slots (20 Min, 45 Min, 90 Min, 120 Min, or custom duration).
- **Zero Database Schema Change**: Synthesizes existing user data and engine states without modifying Supabase schemas.

---

### 2. Study Planner Architecture

```
+-----------------------------------------------------------------------------------+
|                        RAW DATA ENGINES & REPOSITORIES                            |
|  Learning Intelligence V2 • Smart Revision V2 • Daily Mission • Progress Engine   |
|  Weakness Engine • Spaced Revision Queue • Streak Engine • XP Engine • Memory     |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼
+-----------------------------------------------------------------------------------+
|                       STUDY PLANNER ENGINE V2 (Master)                            |
|  • Overdue Revision Priority      • Bottleneck Practice Selection                 |
|  • Deterministic Time Adaptation   • Study Sequence Timeline Generator             |
|  • Expected Mastery Gain          • Next Recommended Action                       |
+-----------------------------------------------------------------------------------+
                                         │
                   ┌─────────────────────┼─────────────────────┐
                   ▼                     ▼                     ▼
        [Personal Study Planner   [AI Mentor            [Future AI
               Dashboard]           Directives]          Planner]
```

---

### 3. Planning Rules

The Study Planner Engine never creates random tasks. Every task is generated deterministically from existing engine intelligence:

1. **Task Selection Source**: Tasks originate strictly from Learning Intelligence gaps, Revision Queue due items, Weakness records, and Mission targets.
2. **Deterministic Rules Only**: Zero AI/LLM generation for task selection or duration calculation.
3. **Master Output JSON Conformance**: Output adheres strictly to the unified JSON schema consumed by all UI components and subagents.

---

### 4. Priority Logic

Tasks are ranked according to standard pedagogical rules:

| Priority | Level | Category | Reason / Trigger | Example Action |
|---|---|---|---|---|
| **1** | Critical | Overdue Revision | Memory decay prevention from Revision Engine | Revise History → Modern India (Spaced Recall) |
| **2** | High | Learning Bottleneck | Primary obstacle identified by Learning Intelligence V2 | Practice Assertion & Reason in Hard Repo (18 min) |
| **3** | Medium-High | Recovery Plan | Rule-based recovery plan step | Guided Notes & Key Concepts Review (15 min) |
| **4** | Medium | Daily Mission | Uncompleted daily test / streak maintenance | Daily Mission Mixed Set (20 min) |
| **5** | Standard | Topic Progress | Official PYQ repository readiness | Attempt History PYQ Set (25 min) |
| **6** | Optional | Grand Practice | Full length exam simulation | Grand Mock Test (30 min) |

---

### 5. Study Sequence Rules

The planner arranges selected tasks into the optimal chronological study order:

1. **Step 1 - Spaced Revision**: Address overdue or memory-decay items while the mind is fresh.
2. **Step 2 - Weakness Recovery**: Focus heavy cognitive load on the primary learning bottleneck.
3. **Step 3 - Practice & Application**: Apply concepts in targeted question types (Assertion & Reason, Statement Based).
4. **Step 4 - PYQ & Verification**: Validate readiness using official previous year questions or grand tests.

---

### 6. Expected Outcome Rules

Topic Mastery gain and confidence boosts are calculated using deterministic formulas:

$$\text{Mastery Gain} = \min\left(25.0, 4.0 \times N_{\text{tasks}} + 0.15 \times T_{\text{duration}}\right)$$

$$\text{Expected Mastery} = \min\left(98.0, \text{Current Mastery} + \text{Mastery Gain}\right)$$

- **Confidence Progression**: Low $\rightarrow$ Medium $\rightarrow$ High $\rightarrow$ Mastery / Expert based on mastery thresholds ($<50\% \rightarrow 50\text{–}75\% \rightarrow >75\%$).

---

### 7. Dashboard Layout

The Personal Study Planner Dashboard ([ui/planner/dashboard.py](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/planner/dashboard.py)) features:

1. **⏱️ Interactive Available Time Selector Bar**: Quick-select chips (20 Min, 45 Min, 90 Min, 120 Min) + custom number input.
2. **🧠 Mentor Banner**: Highlighting today's AI directive and focus area.
3. **📊 Daily Summary Metrics Grid**: Showing Today's Goal, Estimated Time, Potential XP, and Expected Mastery Gain.
4. **🎯 Today's Study Plan**: Glass cards displaying Priority Badge, Task Name, Subject/Topic, Repository/Pattern, Time, Reason, Benefit, and XP Reward.
5. **📈 Expected Learning Outcome Card**: Visualizing current vs expected mastery & confidence boost.
6. **📅 Study Sequence Timeline**: Step-by-step visual timeline flow.
7. **➡ Next Recommended Action**: Prominent directive guiding the student post-session.

---

### 8. Files Modified

- **[NEW]** [core/study_planner_ai.py](file:///c:/Users/Home/Desktop/tnpsc_ai/core/study_planner_ai.py) – Master Personal Study Planner Engine V2.
- **[NEW]** [ui/planner/__init__.py](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/planner/__init__.py) & [ui/planner/dashboard.py](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/planner/dashboard.py) – Personal Study Planner Dashboard UI.
- **[NEW]** [core/test_study_planner.py](file:///c:/Users/Home/Desktop/tnpsc_ai/core/test_study_planner.py) – Unit tests for planner logic and time adaptation.
- **[MODIFY]** [core/study_planner.py](file:///c:/Users/Home/Desktop/tnpsc_ai/core/study_planner.py) – Updated legacy adapter to delegate to `study_planner_ai.py`.
- **[MODIFY]** [ui/components/cards.py](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/components/cards.py) – Added `planner_task_card_html` and `planner_sequence_timeline_html`.
- **[MODIFY]** [app.py](file:///c:/Users/Home/Desktop/tnpsc_ai/app.py) – Added `📅 Study Planner` menu option, icon (`calendar-event`), and page route.

---

### 9. Regression Testing

- **Compilation Check**: Executed `python -m py_compile` across all created and modified files. Zero syntax or import errors.
- **Unit Test Execution**: Executed `python -m unittest core/test_study_planner.py`. All 6 unit tests passed (`OK`).
- **Engine Conformance**: Verified output JSON schema completeness across `today_plan`, `estimated_time`, `expected_outcome`, `study_sequence`, and `daily_summary`.

---

### 10. Compatibility Verification

- Reused existing engine functions cleanly without modifying upstream APIs:
  - `get_learning_intelligence` from `core.learning_intelligence_ai`
  - `get_intelligent_revision_plan` & `get_revision_analytics_v2` from `core.revision_engine`
  - `get_today_mission` from `core.daily_mission_ai`
  - `get_progress` from `core.progress_ai`
  - `get_weakness` from `core.weakness_ai`
  - `get_streak` from `core.streak_ai`
  - `get_user_xp` from `core.xp_ai`
  - `get_memory` from `core.mentor_memory`
- Handled empty database states and unauthenticated test runs gracefully with zero unhandled exceptions.

---

### 11. Mobile Verification

- Implemented CSS grid layouts with `grid-template-columns: repeat(auto-fit, minmax(180px, 1fr))`.
- Applied flex wrapping (`flex-wrap: wrap`) and fluid typography (`clamp()`) for glass cards.
- Ensured single-column stacking on mobile viewports ($\le 768\text{px}$).
