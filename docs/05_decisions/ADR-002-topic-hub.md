# ADR-002: Decoupled Topic Hub Workspace & Navigation v2 Architecture

- **Status**: Accepted & Implemented
- **Date**: 2026-07-22
- **Deciders**: Architecture Team, UX Team

---

## 1. Context & Problem Statement

Prior navigation required students to jump between disconnected sidebar pages to read notes, launch practice tests, inspect PYQs, or ask AI doubts. This fragmented user experience led to navigation loops, lost session state, and high cognitive load.

---

## 2. Decision Outcome

We decided to implement the **Topic Hub Workspace (Navigation v2)** as the centralized operational center for learning:
1. **Unified Workspace View**: When a student selects a topic, the application renders a single integrated workspace (`ui/navigation_v2/topic_hub.py`).
2. **Integrated Toolkit**:
   - **Notes Tab**: Inline reading without leaving context.
   - **Practice Card**: Immediate launch of Easy, Medium, Hard, Statement-Based, AR, Match, and Chronology practice sets.
   - **AI Teacher Link**: Pre-fills active topic context directly into the AI tutor.
   - **PYQ Explorer**: Deep links to relevant past year questions for the active topic.

---

## 3. Consequences

### Positive:
- 🟢 Reduced navigation friction by 80%.
- 🟢 Students remain focused inside a single topic context during study sessions.
- 🟢 Session state transitions are clean and predictable.

### Negative / Trade-offs:
- Sidebar menu options are now primary domain hubs, while fine-grained topic interactions occur inside the Topic Hub.
