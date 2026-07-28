# ADR-003: Decoupled Independent Practice Engine

- **Status**: Accepted & Implemented
- **Date**: 2026-07-22
- **Deciders**: Core Engineering, QA Team

---

## 1. Context & Problem Statement

In initial versions, Practice sessions shared session state flags with the Daily Test module (`test_active`, `test_qs`, `q_index`). This resulted in severe bugs:
- Practice tests were artificially capped at 10 questions.
- Completing a practice set triggered daily test streak and mission logic.
- Practice submission redirected users to a blank screen or sidebar `📘 Daily Test` tab.

---

## 2. Decision Outcome

We decided to build a completely independent, decoupled **Practice Engine**:
1. **Isolated Session Namespace**: All practice states operate strictly under `st.session_state["practice_*"]` (`practice_active`, `practice_questions`, `practice_current_index`, `practice_score`).
2. **Full Payload Loading**: Practice sessions load full repository payloads without 10-question truncation.
3. **Dedicated Result & Review Screen**: Replaced blank screen redirects with an interactive Result Screen featuring score breakdown, XP reward (+10/correct answer), full answer review, practice again, and direct return to Topic Hub.

---

## 3. Consequences

### Positive:
- 🟢 100% decoupling between Practice and Daily Test routines.
- 🟢 No state leakage or accidental daily mission credit during casual practice.
- 🟢 Supports unlimited question counts (15, 25, 50 Qs) and specialized formats (Statement, Match, Chronology).

### Negative / Trade-offs:
- Requires maintaining dual renderer state abstractions (`practice_session.py` vs `daily_test.py`), though both leverage the `UniversalQuestionAdapter`.
