# TNPSC Nova AI — Ideal End-to-End User Flow Architecture

---

## 1. Vision Statement

The ideal TNPSC Nova AI experience is an **intelligent, self-guiding, closed-loop learning journey**. 

An aspirant should never ask *"What should I do next?"*. The system should seamlessly guide them from concept reading to difficulty-based practice, instant diagnostic evaluation, automated remediation, spaced revision, and official topic mastery.

---

## 2. Ideal Master User Flow Diagram

```
┌────────────────────────────────────────────────────────────────────────┐
│                        1. DASHBOARD ENTRY POINT                        │
│  • Daily Action Plan Widget: "Today's Target: Master Preamble Part 1" │
│  • 1-Click Button: "🚀 Continue Active Learning Journey"              │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                     2. UNIFIED TOPIC HUB WORKSPACE                     │
│  • Visual Stage Progress Map:                                         │
│    [📖 Read Notes] ──► [🟢 Easy Repo] ──► [🟡 Medium Repo] ──► [🏆 GT] │
│  • Primary Glowing Action: "Step 1: Read Topic Notes"                  │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                        3. INTERACTIVE STUDY NOTES                      │
│  • Bilingual structured notes with collapsible Tamil translation        │
│  • In-note Article Bookmarking & AI Tutor slide-out helper             │
│  • Bottom Sticky Button: "✅ Mark Notes Read & Start Easy Practice"    │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│              4. IN-LINE PRACTICE (UNIVERSAL QUESTION RENDERER)          │
│  • Renders directly inside Topic Hub tab (No disorienting menu jump)   │
│  • Bilingual toggle, timer, question palette, distractor explanations  │
│  • Instant feedback on answer submission                              │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                       5. DEDICATED RESULT SCREEN                       │
│  • Score percentage, time taken per question, XP earned (+100 XP)      │
│  • Diagnostic Breakdown: "2 Mistakes in Article 19 (Freedom of Speech)"│
│  • 3 Primary Call-to-Actions:                                          │
│    [1. Revise 2 Mistakes]  [2. Retry Practice]  [3. Move to Medium]  │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│                    6. AUTOMATED MASTERY & PROGRESS UPDATE              │
│  • System saves accuracy to `users_progress`                           │
│  • Evaluates Topic Completion: Easy Passed (>=80%)                     │
│  • Enqueues Topic in `user_revisions` for Spaced Revision Day 1        │
│  • Awards Badges/XP: "Preamble Foundation Unlocked!"                   │
└──────────────────────────────────┬─────────────────────────────────────┘
                                   │
                                   ▼
┌────────────────────────────────────────────────────────────────────────┐
│               7. DYNAMIC NEXT-STEP RECOMMENDATION ENGINE               │
│  • Automatically updates Topic Hub Stage Map                           │
│  • Unlocks "Step 2: Medium Practice Repository"                        │
│  • Proposes Next Syllabus Topic when Topic Mastery reaching 100%       │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 3. Step-by-Step Experience Blueprint

### Step 1: Smart Dashboard Entry
- **User View**: When the student logs in, top card displays:
  > **🎯 Today's Mission**: You are 60% done with *Polity — Preamble*.  
  > **Recommended Next Step**: Complete 10 Medium Practice Questions.  
  > `[ 🚀 Launch Session (Estimated 8 Mins) ]`

### Step 2: Unified Topic Hub
- **User View**: Topic Hub displays a sequential 4-step progress tracker:
  1. `[✅ Completed]` Step 1: Read Notes
  2. `[✅ Passed 90%]` Step 2: Easy Question Repository
  3. `[👉 ACTIVE]` Step 3: Medium Question Repository
  4. `[🔒 Locked]` Step 4: Grand Test Simulator

### Step 3: Seamless Inline Practice
- Practice set executes inside the Topic Hub workspace.
- Header shows live countdown timer, language switcher, and question palette.
- Sidebar menu remains highlighted on "🏠 Home" so user never loses context.

### Step 4: Diagnostic Result Screen
Upon answering the final question, the UI transitions to a beautiful Result Screen:
- **Radial Score Wheel**: 80% (8 / 10 Correct)
- **Performance Breakdown**:
  - 🟢 Speed: Average 32 seconds per question (Target: 45s)
  - 🔴 Weak Sub-Concept: *Preamble Amendments (42nd Amendment 1976)*
- **Interactive Action Buttons**:
  - `[ 🤖 Ask AI Teacher to Explain Amendments ]`
  - `[ 📝 Proceed to Statement-Based Questions ]`
  - `[ 🏠 Back to Topic Hub ]`

### Step 5: Automatic Spaced Revision Scheduling
- The system checks if this topic needs revision.
- If accuracy >= 80%, the system automatically adds the topic to the student's `user_revisions` table with `next_due = tomorrow`.
- A notification toast confirms: `📅 Added 'Preamble' to your Revision Queue for tomorrow!`.

### Step 6: Topic Mastery & Next Syllabus Topic Unlocking
- When all 4 stages of a topic are complete, a confetti animation fires:
  > **🏆 TOPIC MASTERED: Historical Background & Preamble**  
  > **Reward**: +150 XP • Unlocked Title: "Constitutional Architect"  
  > **Next Syllabus Topic**: *Salient Features of the Indian Constitution Part 1*  
  > `[ ➡️ Start Next Topic ]`
