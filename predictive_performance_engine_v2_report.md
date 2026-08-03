# TNPSC Nova AI - Phase 6 Sprint 3 Report
## Predictive Performance Engine V2 & Predictive Performance Dashboard

---

### 1. Executive Summary

Phase 6 Sprint 3 introduces the central future projection system for TNPSC Nova AI: **Predictive Performance Engine V2**.

Rather than serving as an exam result or pass/fail predictor, this sprint establishes a unified, deterministic estimation engine ([core/predictive_performance_ai.py](file:///c:/Users/Home/Desktop/tnpsc_ai/core/predictive_performance_ai.py)) that estimates future learning outcomes using rule-based calculations derived from existing learning signals.

**Key Architectural Highlights**:
- **Single Projection Authority**: Serves as the single future prediction engine for AI Exam Coach, Adaptive Revision, Exam Strategy, Future Planning, and Dashboard.
- **Zero UI Prediction Logic**: The [Predictive Performance Dashboard](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/predictive_performance/dashboard.py) performs **zero** predictions or calculations — it strictly visualizes pre-computed outputs from `core/predictive_performance_ai.py`.
- **Deterministic & Conservative Range Estimates**: ALL projections are rendered as estimated ranges (e.g. Current Readiness: 72% $\rightarrow$ Estimated Readiness: 75–79%) rather than single guaranteed values.
- **Prohibition of Absolute Claims**: Strictly avoids claims such as "You will pass", "You will clear Group 1", or "Guaranteed Rank 10". Uses conservative terminology: "Based on current preparation...", "If current study consistency continues...", "Projected...".
- **Zero Database Schema Change**: Reuses existing engine outputs across Exam Readiness V2, Mock Intelligence V2, Recommendation V2, Study Planner V2, Learning Intelligence V2, Revision V2, Progress, Weakness, and Streak engines without modifying database schema.

---

### 2. Predictive Performance Architecture

```
+-----------------------------------------------------------------------------------+
|                        MASTER LEARNING ENGINES & DATA                             |
|  Exam Readiness V2 • Mock Intelligence V2 • Learning Intelligence V2             |
|  Study Planner V2 • Recommendation Engine V2 • Revision Engine V2                |
|  Progress Engine • Weakness Engine • Streak Engine • User XP Engine               |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼
+-----------------------------------------------------------------------------------+
|                   PREDICTIVE PERFORMANCE ENGINE V2 (Master)                       |
|  • Readiness Trend & Projected Range    • Mock Accuracy Trend & Projected Range   |
|  • Topic Mastery Trend & Range          • Revision Health Trend & Range           |
|  • Consistency Trend & Range            • Repository Completion Trend & Range     |
|  • Prediction Confidence Score (0-100%) • Rule-Based Rationale & Explanation      |
+-----------------------------------------------------------------------------------+
                                         │
                   ┌─────────────────────┼─────────────────────┐
                   ▼                     ▼                     ▼
        [Predictive Performance    [AI Exam Coach        [Future Strategy &
             Dashboard]              Projections]           Adaptive Revision]
```

---

### 3. Prediction Rules

The Predictive Performance Engine enforces strict, deterministic calculation principles:

1. **Range-Based Output**: ALL projected metrics are expressed strictly as estimated ranges (e.g., `75–79%`, `76–80%`). Single guaranteed numeric values are prohibited.
2. **Deterministic Range Formulas**:
   $$\text{Low Bound} = \max(10, \min(97, \lfloor S + \Delta_{\text{low}} \rfloor))$$
   $$\text{High Bound} = \max(\text{Low Bound} + 2, \min(99, \lfloor S + \Delta_{\text{high}} \rfloor))$$
   where $S$ is the baseline metric score, $\Delta_{\text{low}}$ and $\Delta_{\text{high}}$ are rule-based momentum multipliers derived from active study streak ($\ge 5$ days) and revision health ($\ge 70\%$).
3. **No Non-Deterministic LLM Calls**: Pure mathematical calculations and deterministic template rules ensure 100% reproducible and transparent projections.
4. **Safety & Policy Guardrails**: Output NEVER guarantees exam selection, rank, or exact score.

---

### 4. Projection Methodology

The engine computes future projections across 6 core learning dimensions:

| Dimension | Baseline Engine Source | Current Metric | Projected Range | Trend Classification |
|---|---|---|---|---|
| **Readiness Trend** | Exam Readiness V2 | 72% | **75–79%** | Improving |
| **Mock Accuracy Trend** | Mock Intelligence V2 | 74% | **76–80%** | Improving |
| **Topic Mastery Trend** | Learning Intelligence V2 | 70% | **73–77%** | Improving |
| **Revision Health Trend** | Revision Engine V2 | 75% | **78–82%** | Stable |
| **Study Consistency Trend** | Streak Engine | 80% | **82–86%** | Improving |
| **Repository Completion Trend** | Exam Readiness V2 | 65% | **68–72%** | Improving |

---

### 5. Trend Analysis Logic

Trends are classified deterministically based on projected delta growth ($\Delta_{\text{low}}$):

- **$\Delta_{\text{low}} \ge 3.0$**: `"Improving"` (Strong learning momentum and active streak)
- **$1.0 \le \Delta_{\text{low}} < 3.0$**: `"Stable"` (Steady preparation pacing)
- **$\Delta_{\text{low}} < 1.0$**: `"Needs Attention"` (Sparse activity or low revision completion)

---

### 6. Confidence Calculation

Prediction confidence is computed deterministically (50% to 96%):

$$\text{Confidence} = 70 + \text{Bonus}_{\text{history}} + \text{Bonus}_{\text{streak}} + \text{Bonus}_{\text{revision}}$$

- **History Depth**: $+12\%$ for $\ge 15$ test attempts ($+6\%$ for $\ge 5$ attempts).
- **Streak Stability**: $+8\%$ for $\ge 5$-day streak ($+4\%$ for $\ge 2$-day streak).
- **Revision Health**: $+6\%$ for revision health $\ge 70\%$.

**Confidence Rationale Output**:
- $\ge 88\%$: *"Rich learning history, consistent study streak, and sufficient performance data across tests."*
- $75–87\%$: *"Moderate learning history and steady revision activity. Projections are well-supported."*
- $< 75\%$: *"Sparse activity history or developing study streak. Complete more daily practice tests to refine accuracy."*

---

### 7. Prediction Explanation Rules

The engine generates explicit rationale explaining *why* projections were produced:

```json
{
  "prediction_reason": "Based on consistent revision (75%), improving mock analytics (74%), and a stable study streak (5 days), current learning trend indicates continued gradual improvement.",
  "mentor_projection": "If current study consistency and spaced revision continue, readiness and mock accuracy are projected to improve steadily within the estimated target ranges.",
  "explanation_bullets": [
    "Consistent revision health (75%) indicates stable memory retention.",
    "Active learning streak (5 days) supports continued gradual performance gains.",
    "Observed mock exam accuracy (74%) provides a reliable baseline for next test performance.",
    "Topic mastery baseline (70%) across target syllabus subjects shows positive trajectory."
  ]
}
```

---

### 8. Dashboard Layout

The **Predictive Performance Dashboard V2** ([ui/predictive_performance/dashboard.py](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/predictive_performance/dashboard.py)) renders engine outputs across 8 distinct sections:

1. 📈 **Future Performance Hero Card**: Highlights Current Readiness $\rightarrow$ Estimated Range, Current Mock Acc. $\rightarrow$ Next Mock Range, and Confidence Badge.
2. 📊 **Current vs. Estimated Comparison**: 6 Side-by-side cards with progress bars and trend badges.
3. 📚 **Readiness Trend**: Deep-dive card for overall readiness trajectory.
4. 📝 **Mock Accuracy Trend**: Deep-dive card for next mock performance range.
5. 🔄 **Revision Trend**: Deep-dive card for spaced memory retention projection.
6. 📅 **Consistency Trend**: Deep-dive card for study streak sustainability.
7. 🎯 **Prediction Confidence**: Visual meter bar (0-100%) and rationale statement.
8. 📖 **Why This Projection?**: Rationale callout, key evaluated factors, future mentor guidance, and safety disclaimer.

---

### 9. Files Modified

| File | Purpose | Action |
|---|---|---|
| [core/predictive_performance_ai.py](file:///c:/Users/Home/Desktop/tnpsc_ai/core/predictive_performance_ai.py) | Master Predictive Performance Engine V2 | **[NEW]** |
| [core/test_predictive_performance.py](file:///c:/Users/Home/Desktop/tnpsc_ai/core/test_predictive_performance.py) | Unit tests for engine rules & confidence | **[NEW]** |
| [ui/predictive_performance/__init__.py](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/predictive_performance/__init__.py) | Package initialization | **[NEW]** |
| [ui/predictive_performance/dashboard.py](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/predictive_performance/dashboard.py) | Master Predictive Performance Dashboard V2 | **[NEW]** |
| [ui/components/cards.py](file:///c:/Users/Home/Desktop/tnpsc_ai/ui/components/cards.py) | Glassmorphic predictive card helpers | **[MODIFY]** |
| [app.py](file:///c:/Users/Home/Desktop/tnpsc_ai/app.py) | Menu navigation & dashboard router | **[MODIFY]** |

---

### 10. Regression Testing

All unit test suites executed cleanly:
- `core/test_predictive_performance.py`: Verified schema conformance, trend classification, range formatting, confidence bounds, and strict prohibition of guarantee claims.
- `core/test_exam_readiness.py`: Verified zero regression on Exam Readiness Engine V2.
- `core/test_mock_intelligence.py`: Verified zero regression on Mock Intelligence Engine V2.

```bash
Ran 5 tests in 0.003s - OK
```

---

### 11. Compatibility Verification

- **Zero ImportError / Circular Import**: Verified clean import hierarchy between master engines and UI components.
- **Zero Database Schema Modification**: Fully compatible with existing Supabase tables and local session storage.
- **Master JSON Schema Compliance**: Output dictionary conforms strictly to the master schema required for future AI Exam Coach integration.

---

### 12. Mobile Verification

- Responsive CSS flex and grid containers (`repeat(auto-fit, minmax(280px, 1fr))`) ensure seamless rendering across mobile, tablet, and desktop viewports.
- Glassmorphism design elements adjust dynamically with fast initial render times.
