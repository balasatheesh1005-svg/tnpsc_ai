# TNPSC Nova AI — Adaptive Learning Engine Roadmap

---

## Overview

The Learning Engine forms the core intelligence of TNPSC Nova AI, analyzing student response patterns, memory decay, and topic mastery to guide efficient exam preparation.

---

## Technical Pipeline Evolution

```text
┌────────────────────────┐      ┌────────────────────────┐      ┌────────────────────────┐
│  Current: Rule-Based   │ ───► │   Phase 1: Dynamic     │ ───► │ Phase 2: Predictive    │
│  Difficulty Routing    │      │ Spaced Repetition (SR) │      │ Mastery & AI Tutor     │
└────────────────────────┘      └────────────────────────┘      └────────────────────────┘
```

---

## Planned Core Upgrades

### 1. Item Response Theory (IRT) Scoring
- Implement 2-Parameter IRT model to calculate item difficulty ($b$) and student ability ($\theta$).
- Replace static XP rewards with difficulty-adjusted mastery growth indices.

### 2. Micro-Knowledge Graph Mapping
- Map prerequisite concepts (e.g. `Preamble` -> `Fundamental Rights` -> `Directive Principles`).
- Automatically recommend foundation reading when accuracy drops below 50% in dependent topics.

### 3. Smart Error Analysis AI
- Categorize student mistakes into:
  - **Factual Memory Gap** (Incorrect recall of dates/articles)
  - **Conceptual Misunderstanding** (Distractor choice alignment)
  - **Careless Error** (Rapid submission latency < 5s)
