# Exam Strategy Engine V2 & Exam Strategy Dashboard Report

## 1. Executive Summary
Sprint 5 introduces the **Exam Strategy Engine V2** and **Exam Strategy Dashboard** to TNPSC Nova AI. The engine serves as the single pre-exam execution strategy authority across the entire platform. Crucially, the engine is **not** a live exam assistant, answer generator, or cheating tool. Instead, it acts as a central strategic planner that synthesizes existing learning signals—Exam Readiness V2, Mock Intelligence V2, Predictive Performance V2, Adaptive Revision V2, Learning Intelligence V2, Recommendation Engine V2, Progress, and Weakness engines—to produce a personalized, deterministic pre-exam execution blueprint tailored to each aspirant's unique strengths and behavioral history.

## 2. Exam Strategy Architecture
The Exam Strategy Engine V2 establishes a central authority model for execution planning:

```
[ Exam Readiness V2 ]      ──┐
[ Mock Intelligence V2 ]   ──┼─► [ Exam Strategy Engine V2 ] ─► [ Exam Strategy Dashboard ]
[ Predictive Engine V2 ]   ──┼─►   (Single Execution Authority)   (Renders ONLY Engine Output)
[ Adaptive Revision V2 ]   ──┼─►
[ Learning Intel V2 ]      ──┘
```

The engine serves as the single execution strategy authority for:
- AI Exam Coach
- Pre-Exam Dashboard
- Final Revision Alignment
- Exam Preparation Modules

The UI Dashboard contains **zero evaluation or strategy creation logic** and renders output exclusively received from `get_exam_strategy()`.

## 3. Strategy Generation Rules
The execution strategy is generated deterministically based on:
1. **Student Strengths & Topic Mastery** (from Learning Intelligence V2 & Progress)
2. **Weak Subjects & Penalty Counts** (from Weakness Engine)
3. **Mock Exam Behaviour & Mistake Patterns** (from Mock Exam Intelligence V2)
4. **Time Management & Question Speed Metrics** (from Mock Intelligence V2)
5. **Prediction Trajectories** (from Predictive Performance Engine V2)
6. **Revision Completion Status** (from Adaptive Final Revision Engine V2)
7. **Overall Preparation Readiness** (from Exam Readiness Engine V2)

All strategies generated are **explainable, deterministic, and personalized**.

## 4. Subject Ordering Logic
The engine calculates a personalized subject attempt sequence using a momentum-first algorithm:

$$\text{Subject Strength Score} = (\text{Mock Accuracy} \times 1.5) - (\text{Weak Penalty} \times 10.0) + (\text{TNPSC Weightage} \times 0.2)$$

Subjects are sorted in descending order of strength score. Aspirants attempt their strongest, most accurate, and fastest subjects first (e.g. History → Polity → Science → Economy → Current Affairs) to build early confidence and exam momentum. Fixed or hardcoded subject ordering is **never** used.

## 5. Time Allocation Methodology
Section-wise recommended time allocations are generated to fit strictly within the configured total exam duration (e.g., 180 minutes for standard 200-question TNPSC exams, or custom 120/150 minute formats):
1. **Review & Buffer Reserve**: 10% to 15% of total exam time is reserved exclusively for a final review buffer (e.g., 22 minutes in a 180-minute exam).
2. **Sectional Proportional Allocation**: Remaining minutes are distributed across active sections proportional to TNPSC question weightages and student speed metrics.
3. **Exact Summation Guarantee**: The sum of section minutes plus review buffer minutes equals `total_exam_minutes` strictly ($35 + 35 + 25 + 25 + 20 + 20 + 20 = 180\text{ min}$).

## 6. Question Decision Framework
Questions are categorized into a 4-tier decision framework with strategy guidance (zero answer keys generated):
- **Easy**: Answer immediately on Pass 1 (direct factual MCQs in strength subjects).
- **Medium**: Think briefly (max 45 seconds) on moderate statement-based questions.
- **Hard**: Mark for review in Pass 2 (complex Assertion & Reason or multi-statement items).
- **Unknown**: Skip immediately on Pass 1 and continue without lingering.

## 7. Risk Analysis Rules
The risk analysis engine detects key exam execution hazards:
- **Overthinking Risk**: Advises against second-guessing initial answers on direct factual questions.
- **Time Pressure Risk**: Enforces strict section time limits to preserve final review buffer.
- **Weak Subject Risk**: Warns against lingering on low-mastery subjects early in the exam.
- **Guessing & Fatigue Risk**: Recommends 5-second mental resets between section transitions.

All risk alerts use **constructive, empowering language** and strictly avoid fear-based or discouraging phrasing.

## 8. Dashboard Layout
The Exam Strategy Dashboard (`ui/exam_strategy/dashboard.py`) presents 9 visual strategy sections:
1. 🎯 **Overall Strategy Hero Banner**: Executive execution theme and strategy confidence meter.
2. 📚 **Subject Attempt Order Timeline**: Flow view of strength-first subject sequence.
3. ⏱ **Section-wise Time Allocation Progress**: Visual time allocation bars per subject section.
4. 📝 **Question Decision Strategy Cards**: 4-tier question handling rules.
5. ⏭ **Skip & Return Strategy Box**: Specific time-trap prevention rules.
6. 🔄 **Review Strategy Sequence**: Prioritized order for reviewing marked questions.
7. ⚠ **Risk Awareness Callouts**: Actionable risk prevention guidance.
8. 📊 **Strategy Confidence Score**: Confidence meter (0-100) and rationale.
9. 🧠 **AI Mentor Strategy Advice**: Personalized pre-exam advice from AI Mentor.

## 9. Files Modified
- **`core/exam_strategy_ai.py`** [NEW]: Master Exam Strategy Engine V2 implementation.
- **`core/test_exam_strategy.py`** [NEW]: Unit test suite for exam strategy engine.
- **`ui/exam_strategy/__init__.py`** [NEW]: UI package initializer.
- **`ui/exam_strategy/dashboard.py`** [NEW]: Dashboard implementation rendering engine output.
- **`ui/components/cards.py`** [MODIFY]: Added 6 reusable HTML glassmorphic card helpers.
- **`app.py`** [MODIFY]: Integrated "🎯 Exam Execution Strategy" menu option and routing branch.

## 10. Regression Testing
- Executed full test suite via `python -m unittest core/test_exam_strategy.py core/test_adaptive_revision.py core/test_predictive_performance.py core/test_mock_intelligence.py core/test_exam_readiness.py core/test_recommendation.py core/test_study_planner.py`.
- Verified deterministic schema conformance, exact time summation ($180 = 180\text{ min}$), and non-fear language.

## 11. Compatibility Verification
- Zero modifications to existing engines (Learning Intelligence, Study Planner, Recommendation, Exam Readiness, Mock Intelligence, Predictive Performance, Adaptive Revision, Question Engine).
- Zero database schema changes or duplicate calculation modules created.
- All imports verified; no circular imports or `ImportError` exceptions.

## 12. Mobile Verification
- All UI components utilize standard glassmorphic containers with responsive flexbox and CSS grid layouts (`minmax(0, 1fr)`).
- Tested layout scaling across standard desktop, tablet, and mobile device screen widths.
