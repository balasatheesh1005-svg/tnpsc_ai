# TNPSC Nova AI — Learning Cycle & Topic Completion Analysis

---

## 1. The Broken Learning Journey

### Current Reality (Linear & Dead-Ended)

The existing user flow follows a strictly linear path that abruptly terminates:

```
Dashboard
   ↓
Subject Selection
   ↓
Topic Selection
   ↓
Topic Hub
   ↓
Study Notes
   ↓
Practice Repository (Easy/Medium)
   ↓
Evaluation & Test Completion
   ↓
??? [DEAD END]
```

### Why Does the Learning Stop?

1. **Missing Result & Next-Action Screen**:
   When a student completes the final question of a test in `app.py`, the backend runs `complete_test()`, clears `test_qs = []`, sets `test_active = False`, and reruns the page. The user is left looking at the generic "Start Daily Test" setup menu. There is no feedback loop saying:
   - *"You scored 80% on Preamble (Easy). Ready for Preamble (Medium)?"*
   - *"You missed Question 3 on Article 19. Tap here to review notes or ask AI Teacher."*

2. **No Automatic State Handshake**:
   Completing a practice session for a topic does not update the state of that topic in the Topic Hub. The student has to manually navigate back to Home -> Topic Hub -> click another button.

3. **No Syllabus Continuity Vector**:
   The application treats every test as an isolated event. It does not calculate where the student sits in the overall TNPSC Group 1 syllabus graph or propose the logical next topic (e.g. *Historical Background Part 1 → Historical Background Part 2 → Preamble*).

---

## 2. Where Should the Student Naturally Continue?

After completing any learning activity, the student should be presented with a **Dynamic Recommendation Engine** that routes them based on their performance:

```
                      [ PRACTICE COMPLETED ]
                                │
                 ┌──────────────┴──────────────┐
                 ▼                             ▼
         Score < 70%                     Score >= 70%
                 │                             │
    ┌────────────┴────────────┐       ┌────────┴────────┐
    ▼                         ▼       ▼                 ▼
[Remedial Notes]     [AI Tutor Doubt] [Next Level Repo] [Topic Completion]
   (Re-read)          (Clear Trap)    (Easy → Medium)    (Mark Completed)
                                                        └───────┬────────┘
                                                                ▼
                                                        [Next Syllabus Topic]
```

---

## 3. Topic Completion Criteria Analysis

### Current Implementation (Flawed)
- In `ui/navigation_v2/topic_hub.py`, topic mastery is calculated as:
  $$\text{Mastery \%} = \frac{\text{Count of existing payload files for topic}}{\text{Total repository types (10)}} \times 100$$
- **Flaw**: A topic is marked 80% "Mastered" simply because developers placed 8 JSON files in `data/questions/`! The student hasn't answered a single question, yet the app tells them they have 80% Mastery!

### Ideal Implementation (Pedagogically Sound)
A topic should only be marked as **Completed / Mastered** when the student achieves empirical performance milestones across 4 distinct learning phases:

$$\text{Topic Completion} = \text{Read Notes} \land (\text{Easy Acc} \ge 80\%) \land (\text{Medium Acc} \ge 70\%) \land (\text{Spaced Revision L1 Done})$$

```
[ Phase 1: STUDY ]    ──►  Read Topic Notes payload (Min 2 mins engaged time)
[ Phase 2: FOUNDATION] ──►  Score >= 80% on Easy Question Repository (10 Qs)
[ Phase 3: MASTERY ]   ──►  Score >= 70% on Medium or Statement-Based Repository
[ Phase 4: RETENTION ] ──►  Pass 1 Spaced Revision test after 24 hours
```

### Missing Implementation Required
1. **`user_topic_mastery` Table**: To store `(username, subject, topic_id, notes_read, easy_passed, medium_passed, revision_passed, completion_status)`.
2. **Visual Topic Progress Badges**: Locked/Unlocked badges on Topic Cards showing stage progression (📖 Read -> 🟢 Easy -> 🟡 Medium -> 🏆 Mastered).
3. **Automatic Progression Triggers**: Automatically launching the next stage upon completing the prerequisite.

---

## 4. Comprehensive Progress Analysis

### How Progress is Currently Calculated
In `core/progress_ai.py` and `core/dashboard_stats_ai.py`:
- `accuracy` = Simple unweighted mean of all percentage scores in `users_progress`.
- `tests_attempted` = Total count of rows in `users_progress`.
- `weak_subject` = Topic key with maximum error count in `users_weakness`.

### Gap Analysis Across Learning Dimensions

| Dimension | Tracked in Code? | Displayed in UI? | Impact on Mastery? | Assessment & Gaps |
|---|---|---|---|---|
| **Reading Notes** | ❌ No | ❌ No | ❌ No | Reading notes is completely ignored by progress engine. |
| **Practice Repositories** | ⚠️ Partial | ⚠️ Partial | ❌ No | Saves test accuracy % to DB, but doesn't distinguish between Easy vs Hard repos. |
| **Revision Cycles** | ⚠️ Partial | ❌ No | ❌ No | Updates `level` in `user_revisions`, but revision completion is disconnected from overall topic progress. |
| **Grand Tests** | ⚠️ Partial | ❌ No | ❌ No | Treated identically to a 5-question quick quiz in accuracy averaging. |
| **Weakness Remediation** | ⚠️ Partial | ⚠️ Partial | ❌ No | Increments error score on wrong answers, but resolving errors doesn't lower the weakness score! |
| **Mastery Calculation** | ❌ No | ❌ Fake | N/A | UI shows fake percentage based on file system existence. |

---

## 5. Ideal Closed-Loop Learning Cycle Architecture

To transform TNPSC Nova AI into a self-reinforcing learning system, every student interaction must flow through 6 closed-loop stages:

```
┌────────────────────────────────────────────────────────────────────────┐
│                      THE Closed-Loop LEARNING CYCLE                   │
└────────────────────────────────────────────────────────────────────────┘

     1. DIAGNOSE & RECOMMEND
     ┌──────────────────────┐
     │ Dashboard / Hub      │ ◄──────────────────────────────────┐
     │ Identifies Next Step │                                    │
     └──────────┬───────────┘                                    │
                │                                                │
                ▼                                                │
     2. CONCEPT ACQUISITION                                      │
     ┌──────────────────────┐                                    │
     │ Study Notes          │                                    │
     │ Interactive Reading  │                                    │
     └──────────┬───────────┘                                    │
                │                                                │
                ▼                                                │
     3. FORMAT PRACTICE                                          │
     ┌──────────────────────┐                                    │
     │ Universal Renderer   │                                    │
     │ Easy/Medium/Hard/PYQ │                                    │
     └──────────┬───────────┘                                    │
                │                                                │
                ▼                                                │
     4. EVALUATE & FEEDBACK                                      │
     ┌──────────────────────┐                                    │
     │ Result Screen        │                                    │
     │ Diagnostic Analytics │                                    │
     └──────────┬───────────┘                                    │
                │                                                │
                ▼                                                │
     5. REMEDIATE & TWEAK                                        │
     ┌──────────────────────┐                                    │
     │ AI Teacher & Weakness│                                    │
     │ Targeted Re-test     │                                    │
     └──────────┬───────────┘                                    │
                │                                                │
                ▼                                                │
     6. SPACED RETENTION                                         │
     ┌──────────────────────┐                                    │
     │ Revision Queue       │────────────────────────────────────┘
     │ Day 1, 3, 7, 15, 30  │ (Topic Mastered & Next Syllabus Topic Unlocked)
     └──────────────────────┘
```
