# TNPSC Nova AI — Product Improvement Backlog & Implementation Blueprint
**(No Code Modifications — Strategic Product Backlog)**

---

## Executive Overview

This improvement backlog categorizes, prioritizes, and defines actionable product specifications to evolve TNPSC Nova AI from a disconnected feature set into a seamless, high-engagement TNPSC learning platform.

The backlog is organized across **5 strategic implementation phases**, ordered by impact and dependency prerequisites.

---

## Phase 1: Critical UX & Navigation Refactoring (High Priority)

### EPIC-1: Dead End Elimination & Dedicated Result Screen
- **ID**: `UX-001`
- **Priority**: P0 (Blocker)
- **Description**: Build a dedicated post-test Result Screen view (`ui/question_engine/result_component.py`) that executes immediately upon answering the final question of any test.
- **Key Deliverables**:
  - Score percentage radial chart, total time spent, average speed per question.
  - Diagnostic mistake review list with hyperlinked explanations.
  - 3 Primary Call-to-Action buttons: `[ 🔄 Revise Mistakes ]`, `[ 🤖 Ask AI Teacher ]`, `[ 🎯 Next Topic Activity ]`.

### EPIC-2: Standardize on Universal Question Renderer
- **ID**: `ARCH-001`
- **Priority**: P0 (Blocker)
- **Description**: Deprecate legacy radio-button rendering in `app.py` and `daily_test_renderer.py`. Standardize all practice modes (Daily Test, Weakness Test, Revision Test, Repository Practice, Grand Test) on `ui/question_engine/universal_renderer.py`.
- **Key Deliverables**:
  - Unified bilingual toggle (`EN` / `TA` / `BOTH`).
  - Unified Question Palette & Jump Navigation.
  - Dynamic timer and confidence rating selector across all tests.

### EPIC-3: Persistent Topic Navigation Context
- **ID**: `NAV-001`
- **Priority**: P1 (High)
- **Description**: Refactor `navigation_state.py` and `app.py` to ensure `selected_subject` and `selected_topic_id` remain active when switching between sidebar menu tabs (Notes, Practice, AI Teacher).
- **Key Deliverables**:
  - Top breadcrumb navigation bar: `Home / Polity / Preamble / Easy Practice`.
  - Prevent menu switching from clearing current topic state.

---

## Phase 2: Closed-Loop Learning Integration & Topic Mastery

### EPIC-4: Empirical Topic Completion Engine
- **ID**: `LRN-001`
- **Priority**: P1 (High)
- **Description**: Replace payload file-count mastery with actual student performance criteria.
- **Mastery Criteria**:
  $$\text{Topic Completed} = \text{Read Notes} \land (\text{Easy Acc} \ge 80\%) \land (\text{Medium Acc} \ge 70\%) \land (\text{Revision L1 Passed})$$
- **Key Deliverables**:
  - Create Supabase table `user_topic_mastery`.
  - Update Topic Hub card to render interactive 4-stage locked/unlocked progress roadmap.

### EPIC-5: Next-Activity Recommendation Engine
- **ID**: `LRN-002`
- **Priority**: P1 (High)
- **Description**: Automatically prompt the optimal next learning activity at the bottom of Notes, Practice Result screens, and Topic Hub.
- **Key Deliverables**:
  - Dynamic recommendation banner: *"You passed Easy Practice (90%). Click to launch Medium Practice."*
  - Auto-routing upon topic completion to the next syllabus topic.

---

## Phase 3: Gamification & Motivation Overhaul

### EPIC-6: TNPSC Cadre Titles & Level Progression
- **ID**: `GAM-001`
- **Priority**: P2 (Medium)
- **Description**: Transform raw level numbers (Level 1 - 10) into authentic TNPSC Cadre Designation Titles.
- **Cadre Title Map**:
  - L1 (0 XP): *Junior Assistant Aspirant*
  - L3 (250 XP): *Revenue Inspector Aspirant*
  - L5 (1,000 XP): *Sub-Registrar Aspirant*
  - L7 (3,500 XP): *Assistant Commissioner Aspirant*
  - L10 (10,000 XP): *Deputy Collector Aspirant*
- **Key Deliverables**:
  - Render Cadre Titles on Profile, Sidebar Header, and Level-Up Alerts.

### EPIC-7: Persistent "Trophy Vault" & Badge Gallery
- **ID**: `GAM-002`
- **Priority**: P2 (Medium)
- **Description**: Create a dedicated UI view (`ui/pages/achievements.py`) featuring 15+ unlockable TNPSC achievement badges.
- **Key Deliverables**:
  - Visual grid of locked vs unlocked badge cards (e.g. "Preamble Scholar", "7-Day Streak Warrior", "Centum Club").
  - Animated badge unlock toast notification during test completion.

### EPIC-8: Leaderboard Metric Refactor & League Tiers
- **ID**: `GAM-003`
- **Priority**: P2 (Medium)
- **Description**: Update leaderboard ranking formula to incorporate Total XP, test volume, and accuracy, eliminating the unweighted average flaw.
- **Key Deliverables**:
  - Weekly resetting competitive tiers: Gold League, Silver League, Bronze League.

---

## Phase 4: AI Teacher & Contextual Memory Upgrade

### EPIC-9: Context-Aware AI Tutor Engine
- **ID**: `AI-001`
- **Priority**: P2 (Medium)
- **Description**: Upgrade `ai_teacher.py` from raw string matching to an active context-aware tutor.
- **Key Deliverables**:
  - Automatically inject active subject, topic, and last missed question metadata into query context.
  - Multi-turn conversation memory (`st.session_state["teacher_chat_history"]`).
  - Slide-out inline tutor drawer available inside Notes and Question Explanations.

---

## Phase 5: Multi-Dimensional Progress & Analytics

### EPIC-10: Integrated TNPSC Readiness Score (0 - 1000 Pts)
- **ID**: `ANA-001`
- **Priority**: P3 (Future Enhancement)
- **Description**: Build a unified Readiness Score algorithm combining Syllabus Coverage (300 Pts), Accuracy Mastery (400 Pts), Retention Index (200 Pts), and Exam Hall Stamina (100 Pts).
- **Key Deliverables**:
  - Visual radial gauge on Dashboard and Progress page.
  - Interactive 30-day accuracy trend graph and subject strength radar chart.

---

## Summary Backlog Roadmap

```
┌────────────────────────────────────────────────────────────────────────┐
│                        IMPLEMENTATION ROADMAP                          │
└────────────────────────────────────────────────────────────────────────┘

[ PHASE 1: UX & ROUTING ] ──► Fix Result Screen Dead Ends, Standardize Universal
                              Renderer, Fix Sidebar Menu Topic Context Loss.

[ PHASE 2: CLOSED LOOP  ] ──► Implement True Performance Topic Mastery & Next-
                              Step Recommendation Engine.

[ PHASE 3: GAMIFICATION ] ──► Add TNPSC Cadre Titles, Trophy Vault Badge Gallery,
                              XP Micro-Animations & League Leaderboards.

[ PHASE 4: AI TUTORING  ] ──► Contextual Memory AI Teacher & Slide-out Inline
                              Doubt Drawer.

[ PHASE 5: ANALYTICS    ] ──► Integrated TNPSC Readiness Score (0-1000 Pts) &
                              Interactive Time-Series Progress Charts.
```
