# TNPSC Nova AI — Progress Calculation & Mastery Analysis

---

## 1. Current Progress Engine Evaluation

### Code-Level Implementation Analysis

Progress is currently handled by `core/progress_ai.py` and `core/dashboard_stats_ai.py`.

```python
# How average accuracy is currently calculated:
def get_average_accuracy(user, progress=None):
    scores = [float(row.get("accuracy", 0)) for row in progress]
    return round(sum(scores) / len(scores), 1)
```

### Critical Flaws in Current Formula

1. **Unweighted Average**:
   A 5-question easy quiz has the exact same weight as a 100-question full-length Grand Test!
   - Quiz 1 (5 Qs): 100%
   - Grand Test (100 Qs): 50%
   - Current System Accuracy: $\frac{100 + 50}{2} = 75\%$
   - **Real Student Accuracy**: $\frac{5 + 50}{105} = 52.3\%$ (The current app overestimates accuracy by 22.7%!).

2. **No Time-Decay / Exponential Weighting**:
   If a student scored 20% on a topic 3 months ago, that score continuously drags down their average today, even if they have scored 100% on the last 5 tests.

3. **Fake Topic Mastery Calculation**:
   In `ui/navigation_v2/topic_hub.py`:
   $$\text{Mastery \%} = \frac{\text{Available Payload Files}}{\text{Total Repositories (10)}} \times 100$$
   This measures **developer file creation**, NOT student learning achievement!

---

## 2. Multi-Dimensional Progress Evaluation Matrix

| Progress Dimension | Currently Tracked? | Formula / Metric Used | Reflects True Learning? | Required Enhancement |
|---|---|---|---|---|
| **Reading Progress** | ❌ NO | None | ❌ NO | Log note completion status (`notes_read = True`) & engaged reading time |
| **Practice Coverage** | ⚠️ Partial | Row count in `users_progress` | ❌ NO | Syllabus topic coverage % ($\frac{\text{Topics Practiced}}{\text{Total Syllabus Topics}}$) |
| **Question Accuracy** | 🟢 YES | Arithmetic Mean of attempt % | ⚠️ Flawed | Weighted accuracy by total questions answered ($\sum \text{Correct} / \sum \text{Attempted}$) |
| **Spaced Revision** | ⚠️ Partial | `user_revisions.level` (1-5) | ❌ Disconnected | Retention Index based on revision level stability over time |
| **Grand Test Mastery**| ⚠️ Partial | Averaged with standard quizzes | ❌ NO | Separate "Exam Readiness Score" derived from Grand Tests |
| **Weakness Removal** | ⚠️ Partial | `users_weakness.error_count` | ❌ NO | Weakness Reduction Rate (% of red topics converted to green) |
| **Overall Readiness** | ❌ NO | None | ❌ NO | Integrated **TNPSC Readiness Score (0 - 1000)** |

---

## 3. Recommended Multi-Dimensional Progress Architecture

To provide an accurate, motivating representation of student readiness, TNPSC Nova AI should calculate 4 distinct sub-scores:

```
┌────────────────────────────────────────────────────────────────────────┐
│                   INTEGRATED TNPSC READINESS SCORE                     │
│                    Score Range: 0 ───► 1000 Points                      │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
      ┌────────────────────────────┼────────────────────────────┐
      ▼                            ▼                            ▼
┌───────────┐                ┌───────────┐                ┌───────────┐
│ SYLLABUS  │                │ ACCURACY  │                │ RETENTION │
│ COVERAGE  │                │  MASTERY  │                │   INDEX   │
│ (300 Pts) │                │ (400 Pts) │                │ (200 Pts) │
└─────┬─────┘                └─────┬─────┘                └─────┬─────┘
      │                            │                            │
      │ % of Note Parts            │ Question-weighted          │ Spaced Revision
      │ & Topics Practiced         │ Accuracy Across            │ Level 3+ Passed
      │                            │ Easy/Medium/Hard           │ Topics
      └────────────────────────────┼────────────────────────────┘
                                   │
                                   ▼
                             ┌───────────┐
                             │ EXAM HALL │
                             │  STAMINA  │
                             │ (100 Pts) │
                             └───────────┘
                               Grand Test
                               Simulations
                               Passed
```

### Detailed Sub-Score Breakdown:

1. **Syllabus Coverage Score (0 - 300 Pts)**:
   $$S_{\text{coverage}} = 300 \times \left( \frac{\text{Completed Note Parts}}{\text{Total Note Parts in Syllabus}} \right)$$

2. **Accuracy Mastery Score (0 - 400 Pts)**:
   $$S_{\text{accuracy}} = 400 \times \left( \frac{\text{Total Correct Answers (Last 30 Days)}}{\text{Total Questions Attempted (Last 30 Days)}} \right)$$

3. **Retention Index (0 - 200 Pts)**:
   $$S_{\text{retention}} = 200 \times \left( \frac{\text{Topics with Revision Level } \ge 3}{\text{Total Practiced Topics}} \right)$$

4. **Exam Hall Stamina (0 - 100 Pts)**:
   $$S_{\text{stamina}} = 100 \times \left( \text{Average Grand Test Score \%} \right)$$

---

## 4. Visual Progress Dashboard Redesign

The Progress Page (`ui/pages/progress.py`) should be upgraded from raw static tables to an interactive visual dashboard displaying:
1. **TNPSC Readiness Gauge**: 0 to 1000 overall score indicator.
2. **Syllabus Heatmap Tree**: Interactive tree map of Polity, History, Economy showing green (mastered), yellow (practiced), and gray (unstudied) topic nodes.
3. **Accuracy Trend Line**: 30-day moving average chart of student performance.
