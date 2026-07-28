# TNPSC Nova AI — Architectural Review & Technical Assessment

---

## 1. Executive Summary

This document presents a technical architectural evaluation of the TNPSC Nova AI codebase. 

The application demonstrates strong domain modeling in its content schema specifications, permanent ID conventions, and multi-format question parsing. However, architectural flaws exist in state management coupling, duplicated UI rendering engines, primitive keyword-based AI logic, and missing closed-loop user flows.

---

## 2. Core Architectural Subsystems Review

### 1. Permanent ID Architecture
- **Description**: Topic metadata and files are mapped using deterministic permanent IDs (e.g. `polity_historical_background_part1`).
- **Strengths**: 
  - Resolves file name discrepancies between note files (`polity_historical_background_part1.json`) and question repositories (`polity_historical_background_easy.json`).
  - Helper functions in `core/topics_loader.py` provide reliable fallback lookups using `get_topic_metadata_by_id()`.
- **Weaknesses**:
  - String manipulation code (`if note_basename.startswith(f"{subj}_"): note_basename = note_basename[len(subj) + 1:]`) is repeated across 5 separate files (`navigation_state.py`, `notes.py`, `progress.py`, `ai_teacher.py`, `topic_hub.py`).

### 2. Universal Renderer System
- **Description**: Universal Question Engine located in `ui/question_engine/` featuring `UniversalQuestionAdapter`, `NormalizedQuestion`, `body_component`, `option_component`, `footer_component`, `explanation_component`, `palette_component`, `result_component`.
- **Strengths**:
  - Highly modular GFM-compliant architecture.
  - Normalizes heterogeneous question JSON formats into a single strongly-typed dataclass.
  - Multi-type rendering support for MCQs, Multi-Statement accuracy, Assertion & Reason, Match the Following, and Chronology.
- **Weaknesses**:
  - **Not fully adopted!** `app.py` and `ui/pages/daily_test_renderer.py` still use an older, hardcoded inline radio loop for Daily Tests instead of delegating to `universal_renderer.py`.

### 3. Repository System
- **Description**: Data directory structure organizing content into `data/notes/<subject>/` and `data/questions/<subject>/`.
- **Strengths**:
  - Clean separation of content files from code logic.
  - File-naming standards allow checking payload availability via `check_repository_availability()`.
- **Weaknesses**:
  - Payload existence checks (`os.path.exists`) are performed synchronously on every Streamlit rerun, causing disk I/O overhead on large directories.

### 4. Topic Hub Architecture
- **Description**: Central workspace (`ui/navigation_v2/topic_hub.py`) unifying Notes, Practice Repos, Grand Tests, and AI Teacher.
- **Strengths**:
  - Modern glassmorphism UI layout using custom HTML/CSS card components.
  - Displays payload availability status badges ("Ready" vs "Coming Soon").
- **Weaknesses**:
  - Mastery calculation formula is fake (measures JSON file count on disk rather than student performance).
  - Practice buttons switch top-level menu tabs forcibly, losing Topic Hub context.

### 5. Daily Test & Grand Test Engines
- **Description**: Test execution loops in `app.py` and `ui/pages/daily_test_renderer.py`.
- **Strengths**:
  - Handles score tracking, time elapsed formatting, and database progress logging.
- **Weaknesses**:
  - Code duplication: Daily test rendering logic is duplicated in `app.py` lines 614-830.
  - Missing dedicated Result Screen view at completion.

---

## 3. Comprehensive Strengths vs Weaknesses Matrix

| Architecture Component | Strengths | Weaknesses & Technical Debt |
|---|---|---|
| **Data Schema & Spec** | Strict JSON schemas defined in `docs/` specs for Notes and MCQs. | Some legacy JSON payloads lack Tamil translation keys or distractor explanation fields. |
| **Authentication & Auth** | Supabase auth integration with session restoration. | Session expiration leaves user in half-logged state; requires manual logout rerun. |
| **Database Resilience** | Custom `_RetryQuery` client in `supabase_client.py` handling network retries. | Errors silently return empty namespaces without informing user of database downtime. |
| **Gamification Engine** | Backend functions for XP, levels, and streaks exist in `core/`. | Disconnected from frontend; missing badge UI, trophy room, and level cadre titles. |
| **AI Tutoring Engine** | Rule-based string matcher in `ai_teacher.py`. | Primitive keyword matching (no LLM, no RAG, no conversational state memory). |
| **State Management** | Centralized session defaults in `app.py`. | State keys mutated haphazardly across components; duplicate writes (`test_mode`). |

---

## 4. Architectural Target State Diagram

To eliminate technical debt and ensure scalability, the architecture should evolve into a clean 3-tier modular system:

```
┌────────────────────────────────────────────────────────────────────────┐
│                          PRESENTATION TIER                             │
│                                                                        │
│   ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐   │
│   │ Unified Workspace│   │Universal Renderer│   │ Result & Summary │   │
│   │   (Topic Hub)    │   │ (Question Engine)│   │  (Diagnostic UI) │   │
│   └─────────┬────────┘   └─────────┬────────┘   └─────────┬────────┘   │
└─────────────┼──────────────────────┼──────────────────────┼────────────┘
              │                      │                      │
              ▼                      ▼                      ▼
┌────────────────────────────────────────────────────────────────────────┐
│                           APPLICATION TIER                             │
│                                                                        │
│   ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐   │
│   │ Unified Router   │   │  Mastery Engine  │   │  AI Mentor & RAG │   │
│   │ (core/router.py) │   │(core/mastery.py) │   │ (core/ai_tutor)  │   │
│   └─────────┬────────┘   └─────────┬────────┘   └─────────┬────────┘   │
└─────────────┼──────────────────────┼──────────────────────┼────────────┘
              │                      │                      │
              ▼                      ▼                      ▼
┌────────────────────────────────────────────────────────────────────────┐
│                             DATA TIER                                  │
│                                                                        │
│   ┌──────────────────┐   ┌──────────────────┐   ┌──────────────────┐   │
│   │ Supabase Tables  │   │ JSON Repositories│   │ Local Memory Cache│   │
│   │ (Progress/XP/Rev)│   │ (Notes/Questions)│   │  (st.cache_data) │   │
│   └──────────────────┘   └──────────────────┘   └──────────────────┘   │
└────────────────────────────────────────────────────────────────────────┘
```
