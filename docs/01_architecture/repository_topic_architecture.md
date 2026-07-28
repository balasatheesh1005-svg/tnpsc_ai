# TNPSC Nova AI — Permanent Repository Topic Architecture

## Executive Summary

This document specifies the permanent identifier architecture for TNPSC Nova AI, decoupling Notes Topic navigation (`topic_id`) from Practice Repository navigation (`repository_id`).

---

## Architectural Problem Addressed

Prior to this architecture, UI display titles (e.g. `Historical Background Part 1`) were improperly used as keys to search practice repositories. Because Notes are split into sequential parts while question repositories are built for the complete topic (`historical_background`), practice repository lookups failed, resulting in erroneous **"Repository Not Available"** warnings.

---

## Core Principles

1. **Permanent Identifiers over String Titles**:
   - `topic_id`: Unique identifier of a specific note payload / part (e.g. `polity_historical_background_part1`).
   - `repository_id`: Identifier of the parent full-topic practice repository (e.g. `polity_historical_background`).
   - `display_title`: Human-readable title used **exclusively** in the UI (e.g. `Historical Background Part 1`). Never used for repository resolution.

2. **Decoupled Navigation**:
   - **Notes Module**: Guided by `topic_id` to load specific note part files (`data/notes/{subject}/{topic_id}.json`).
   - **Practice Repositories & Grand Test**: Guided by `repository_id` to load complete question repositories (`data/questions/{subject}/{repository_id}_{type}.json`).

3. **Dual-Level Progress Tracking**:
   - **Repository Level**: Aggregated accuracy across the entire topic area.
   - **Part Level**: Granular completion and performance breakdown per note part.

---

## Component Interaction Overview

```
                          ┌───────────────────────────┐
                          │   Topic Selection UI      │
                          └─────────────┬─────────────┘
                                        │
                         Selects topic_id & repository_id
                                        │
           ┌────────────────────────────┴────────────────────────────┐
           ▼                                                         ▼
┌───────────────────────┐                               ┌───────────────────────┐
│     Notes Engine      │                               │   Question Loader     │
│ (Uses topic_id)       │                               │ (Uses repository_id)  │
└──────────┬────────────┘                               └───────────┬───────────┘
           │                                                        │
           ▼                                                        ▼
data/notes/polity/                                      data/questions/polity/
historical_background_part_1.json                       historical_background_easy.json
                                                        historical_background_grand_test.json
```
