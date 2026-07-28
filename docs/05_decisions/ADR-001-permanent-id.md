# ADR-001: Permanent Identifiers for Topics and Repositories

- **Status**: Accepted & Implemented
- **Date**: 2026-07-22
- **Deciders**: Architecture Team, Core Engineering

---

## 1. Context & Problem Statement

Historically, TNPSC Nova AI mapped syllabus topics, revision notes, and question repositories using human-readable string combinations (e.g. `subject="polity"`, `topic="Historical Background"`). This created key fragile points:
1. Slight string formatting differences (spaces vs underscores, capitalization) led to path mismatch failures.
2. Renaming a topic title broke database progress lookups and session state.
3. Lack of unified repository identifiers prevented seamless cross-linking between Notes, Practice Sets, and Grand Tests.

---

## 2. Decision Outcome

We decided to introduce immutable, normalized **Permanent Identifiers** across all data schemas and session states:
- **`topic_id`**: Canonical topic identifier (e.g., `polity_historical_background`).
- **`repository_id`**: Canonical question payload identifier (e.g., `polity_historical_background_easy`).

### Key Principles:
1. **Zero Downtime & Backward Compatibility**: Legacy method calls using subject/topic strings automatically convert internally via `normalize_topic_id()`.
2. **Deterministic File Resolution**: Disk paths are derived systematically from permanent IDs (e.g., `data/notes/polity/historical_background_part_1.json`).

---

## 3. Consequences

### Positive:
- 🟢 100% robust topic resolution regardless of UI label capitalization.
- 🟢 Unlocks instant topic-level analytics and cross-module navigation.
- 🟢 Database records maintain consistency even if UI display names are localized or updated.

### Negative / Trade-offs:
- Requires internal mapping table (`TOPIC_ID_MAP`) in `core/` to resolve legacy routes seamlessly.
