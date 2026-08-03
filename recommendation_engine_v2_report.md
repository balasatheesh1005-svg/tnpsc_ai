# TNPSC Nova AI - Phase 5 Sprint 5 Report
## AI Recommendation Engine V2 & AI Recommendation Dashboard

---

### 1. Executive Summary

Phase 5 Sprint 5 introduces the central recommendation authority for TNPSC Nova AI: **AI Recommendation Engine V2**.

Rather than serving as a basic recommendation widget, this sprint establishes a reusable recommendation engine ([core/recommendation_ai.py](file:///c:/Users/Home/Desktop/tnpsc_ai/core/recommendation_ai.py)) that acts as the single recommendation brain for AI Mentor, Study Planner, Dashboards, Topic Completion, Repository Completion, and all future AI modules.

**Key Architectural Highlights**:
- **Central Recommendation System**: Serves as the single recommendation engine for AI Mentor, Study Planner, Dashboards, and Future AI.
- **Zero UI Recommendation Logic**: The [AI Recommendation Dashboard](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/recommendation/dashboard.py) performs **zero** business or recommendation calculations — it strictly visualizes the JSON output produced by `core/recommendation_ai.py`.
- **Single Primary Recommendation Cascade**: Applies a strict priority cascade to generate **ONE** unambiguous primary recommendation (*Overdue Revision → Critical Bottleneck → Recovery Plan → Study Plan → Grand Test → Topic Completion → Next Topic*).
- **Automated Risk Detection**: Detects learning risks (*Overdue Revision Risk, Low Revision Habit, Weak Hard Repository, Broken Streak*) with risk level ratings (*Low, Medium, High, Critical*).
- **Rule-Based Confidence & Benefit**: Calculates recommendation confidence scores (70%–98%) and estimated benefits (+10% Mastery, +40 XP, High Confidence) using deterministic rules.
- **Zero Database Schema Change**: Synthesizes existing user data and engine states without modifying Supabase schemas.

---

### 2. Recommendation Engine Architecture

```
+-----------------------------------------------------------------------------------+
|                        RAW DATA ENGINES & REPOSITORIES                            |
|  Learning Intelligence V2 • Study Planner V2 • Smart Revision V2 • Progress       |
|  Weakness Engine • Streak Engine • XP Engine • Mission Engine • Memory            |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼
+-----------------------------------------------------------------------------------+
|                     AI RECOMMENDATION ENGINE V2 (Master)                          |
|  • Single Primary Recommendation      • Priority Order Cascade                    |
|  • Risk Detection System (Low-Crit)   • Rule-Based Confidence (70-98%)            |
|  • Estimated Mastery & XP Gain        • Recommendation Explanation Generator      |
+-----------------------------------------------------------------------------------+
                                         │
                   ┌─────────────────────┼─────────────────────┐
                   ▼                     ▼                     ▼
        [AI Recommendation        [AI Mentor            [Future AI
               Dashboard]           Coaching]            Modules]
```

---

### 3. Recommendation Rules

The AI Recommendation Engine adheres to strict platform rules:

1. **Single Recommendation Authority**: Engine generates exactly **ONE** primary recommendation per evaluation run. No competing or ambiguous options.
2. **Deterministic Processing**: Zero LLM call or non-deterministic code. Recommendation text, risk flags, and confidence scores are calculated via pure rule-based logic.
3. **Master Output JSON Conformance**: Conforms strictly to the master schema consumed by UI components, mentor subagents, and future planner modules.

---

### 4. Priority Logic

Recommendations are evaluated using a strict priority cascade:

| Priority | Level | Trigger / Category | Recommendation Type | Example Primary Recommendation |
|---|---|---|---|---|
| **1** | Critical | Overdue Revision | Revise Today | Revise Overdue Topic: History → Modern India |
| **2** | High | Critical Learning Bottleneck | Continue Recovery | Revise History Modern India (Assertion & Reason) |
| **3** | Medium-High | Ongoing Recovery Cycle | Complete Hard Repo | Execute Recovery Step: Revise Notes & Target Set |
| **4** | Medium | Today's Study Plan | Maintain Streak | Complete Today's Study Plan (3 Tasks) |
| **5** | Standard | High Accuracy ($\ge 75\%$) | Start Grand Test | Take Full Grand Mock Test in History |
| **6** | Standard | Topic Mastery ($\ge 85\%$) | Start Next Topic | Mastery Achieved (86%) • Proceed to Next Topic |

---

### 5. Risk Detection Logic

The Risk Detection System identifies active learning obstacles and assigns a Risk Level:

- **Overdue Revision Risk** (*Critical / High*): Active overdue revision topics experiencing memory decay.
- **Low Revision Habit** (*High*): Spaced revision completion rate $< 50\%$.
- **Weak Hard Repository** (*High*): Hard Repository accuracy $< 50\%$ in current subject.
- **Low PYQ Performance** (*Medium*): Previous Year Question accuracy $< 55\%$.
- **Broken Study Streak** (*Medium*): Streak reset to 0 after previous active days.
- **Optimal Progress** (*Low*): No critical risks detected.

---

### 6. Benefit Estimation Rules

Estimated learning benefits are calculated deterministically:

- **Mastery Gain**: Calculated dynamically based on remaining bottleneck gap:
  $$\text{Mastery Gain} = \min\left(20.0, \max\left(5.0, (100.0 - \text{Current Mastery}) \times 0.25\right)\right)$$
- **XP Reward**: `+50 XP` for Critical priority recommendations; `+40 XP` for Standard/High recommendations.
- **Confidence Rating**: `High Confidence` (when risk level is Low/Medium) or `Medium Confidence` (when risk level is High/Critical).

---

### 7. Confidence Rules

Recommendation confidence scores (70% to 98%) are calculated using deterministic data weighting:

- **Base Confidence**: 90%
- **Risk Level Bonus/Penalty**: $+4\%$ for Low Risk; $-6\%$ for Critical Risk.
- **Data Depth Adjustments**:
  - $\ge 10$ test attempt rows: $+2\%$ (High confidence from rich dataset).
  - $< 3$ test attempt rows: $-14\%$ (78% confidence due to sparse data).

---

### 8. Dashboard Layout

The AI Recommendation Dashboard ([ui/recommendation/dashboard.py](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/recommendation/dashboard.py)) includes:

1. **🧠 Mentor Directives Banner**: Expressing high-level mentor advice.
2. **⭐ Primary Recommendation Hero Card**: Prominent glass card showcasing the single primary recommendation, priority badge, confidence score, and topic context.
3. **⚠ Risk Alert Card**: Color-coded risk level badge (*Critical/High/Medium/Low*) and risk mitigation description.
4. **📈 Estimated Learning Benefit Grid**: Metrics showing Mastery Gain, XP Reward, and Confidence rating.
5. **🎯 Current Action & ➡ Next Action Cards**: Clear 2-step chronological action flow.
6. **📖 Why This Recommendation? Card**: Rule-based explanation card detailing identified bottlenecks and learning rationale.

---

### 9. Files Modified

- **[NEW]** [core/recommendation_ai.py](file:///c:/Users/Home/Desktop/tnpsc_ai/core/recommendation_ai.py) – Master AI Recommendation Engine V2.
- **[NEW]** [ui/recommendation/__init__.py](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/recommendation/__init__.py) & [ui/recommendation/dashboard.py](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/recommendation/dashboard.py) – Recommendation Dashboard UI.
- **[NEW]** [core/test_recommendation.py](file:///c:/Users/Home/Desktop/tnpsc_ai/core/test_recommendation.py) – Comprehensive unit tests for recommendation engine.
- **[MODIFY]** [ui/components/cards.py](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/components/cards.py) – Added `recommendation_hero_card_html` and `recommendation_risk_alert_html`.
- **[MODIFY]** [app.py](file:///c:/Users/Home/Desktop/tnpsc_ai/app.py) – Added `"💡 AI Recommendations"` menu option, icon (`lightbulb`), and page routing.

---

### 10. Regression Testing

- **Compilation Check**: Executed `python -m py_compile` across all created and modified files. Zero syntax or import errors.
- **Unit Test Execution**: Executed `python -m unittest core/test_recommendation.py`. All 6 unit tests passed (`OK`).
- **Engine Conformance**: Verified master JSON schema completeness across `recommendation`, `priority`, `risk`, `risk_level`, `confidence`, `current_action`, `next_action`, and `explanation`.

---

### 11. Compatibility Verification

- Reused existing engine functions cleanly without modifying upstream APIs:
  - `get_learning_intelligence` from `core.learning_intelligence_ai`
  - `get_personal_study_plan` from `core.study_planner_ai`
  - `get_intelligent_revision_plan` & `get_revision_analytics_v2` from `core.revision_engine`
  - `get_progress` from `core.progress_ai`
  - `get_weakness` from `core.weakness_ai`
  - `get_streak` from `core.streak_ai`
  - `get_user_xp` from `core.xp_ai`
  - `get_today_mission` from `core.daily_mission_ai`
  - `get_memory` from `core.mentor_memory`
- Handled empty database states and unauthenticated test runs gracefully with zero unhandled exceptions.

---

### 12. Mobile Verification

- Implemented responsive glass cards with fluid typography (`clamp()`) and flex wrapping (`flex-wrap: wrap`).
- Applied single-column layout auto-reflow for viewports $\le 768\text{px}$.
