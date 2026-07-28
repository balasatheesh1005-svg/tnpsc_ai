# TNPSC Nova AI — Production Repository Structure

This document presents the complete visual file tree of the organized TNPSC Nova AI project repository and external working workspace.

---

## 1. Production Repository Layout (`tnpsc_ai`)

```text
tnpsc_ai/
│
├── README.md                      # High-level enterprise README & Quick Start
├── .gitignore                     # Git exclusion rules for Python & Streamlit
├── requirements.txt               # Python package dependencies
├── app.py                         # Main Streamlit application entry point
├── documentation_cleanup_report.md# Final cleanup & governance execution log
├── repository_structure.md        # This visual repository structure document
├── documentation_index.md         # Root hyperlinked documentation index
│
├── docs/                          # Master Permanent Documentation Tree
│   ├── DOCUMENTATION_INDEX.md     # Master hyperlinked catalog
│   ├── documentation_policy.md    # Official Hybrid Documentation Governance Policy v1.0
│   │
│   ├── 01_architecture/           # Architectural Specifications & Schemas
│   │   ├── architecture_freeze_v1.md
│   │   ├── architecture_review.md
│   │   ├── content_standards_v1.md
│   │   ├── mcq_schema_specification_v1.md
│   │   ├── module_dependency_map.md
│   │   ├── navigation_analysis.md
│   │   ├── notes_schema_specification_v1.md
│   │   ├── practice_engine_architecture.md
│   │   ├── repository_topic_architecture.md
│   │   └── topic_mapping_design.md
│   │
│   ├── 02_audit/                  # System & Gamification Audits
│   │   ├── gamification_analysis.md
│   │   ├── improvement_backlog.md
│   │   ├── learning_cycle_analysis.md
│   │   ├── product_audit_report.md
│   │   └── progress_analysis.md
│   │
│   ├── 03_qa/                     # Production Quality Gate & QA Verdicts
│   │   ├── practice_engine_final_verdict.md
│   │   └── validation_checklist_v1.md
│   │
│   ├── 04_migration/              # Refactoring Reports & Navigation Flows
│   │   ├── current_user_flow.md
│   │   ├── migration_notes.md
│   │   ├── migration_report.md
│   │   └── practice_flow.md
│   │
│   ├── 05_decisions/              # Architecture Decision Records (ADRs)
│   │   ├── ADR-001-permanent-id.md
│   │   ├── ADR-002-topic-hub.md
│   │   └── ADR-003-practice-engine.md
│   │
│   ├── 06_roadmap/                # Project Roadmaps & Horizon Plans
│   │   ├── feature_roadmap.md
│   │   ├── future_roadmap.md
│   │   └── learning_engine_roadmap.md
│   │
│   └── 99_archive/                # Superseded Documents & Legacy Notes
│       ├── docs_readme_v1.md
│       └── ideal_user_flow.md
│
├── core/                          # Backend Engines & Utilities
│   ├── db.py                      # Supabase / SQLite database interface
│   ├── auth.py                    # User authentication handler
│   ├── xp_ai.py                   # XP & Gamification rewards system
│   ├── question_engine/           # Decoupled question loading & practice session
│   │   ├── loader.py              # Repository JSON loader
│   │   ├── practice_session.py    # Dedicated practice session state manager
│   │   ├── daily_test.py          # Daily test session manager
│   │   ├── schema_validator.py    # MCQ JSON schema validator
│   │   └── bookmark.py            # Question bookmark manager
│   └── topic_hub/                 # Topic mapping & metadata registry
│       ├── mapper.py              # Permanent topic ID mapping
│       ├── topic_service.py       # Topic retrieval service
│       └── stats_engine.py        # Progress & analytics calculator
│
├── ui/                            # Streamlit Components & Layout Engines
│   ├── layout.py                  # Page wrapper & navigation sidebar
│   ├── navigation_v2/             # Topic Hub Workspace implementation
│   │   └── topic_hub.py           # Integrated topic reading & practice hub
│   ├── question_engine/           # Universal question rendering components
│   │   ├── practice_renderer.py   # Dedicated practice renderer
│   │   ├── renderer.py            # UniversalQuestionAdapter & UI layouts
│   │   ├── header_component.py    # Progress bar & timer header
│   │   └── palette_component.py   # Interactive question jump palette
│   └── pages/                     # Application views & dashboards
│       ├── home.py                # Dashboard & subject selector
│       ├── notes.py               # Revision notes reader
│       ├── weakness.py            # Weakness heatmap & dynamic practice link
│       ├── progress.py            # Accuracy & repository progress analytics
│       ├── leaderboard.py         # Global student rankings
│       ├── teacher.py             # AI doubt resolution tutor
│       ├── mentor.py              # Personal mentor chat view
│       └── pyq.py                 # Past Year Questions explorer
│
├── data/                          # Core Content Repositories
│   ├── notes/                     # Subject revision notes JSON files
│   │   ├── polity/
│   │   └── economy/
│   └── questions/                 # Question payload JSON repositories
│       ├── polity/
│       └── economy/
│
├── tools/                         # Maintenance & Import Pipelines
│   ├── pyq_importer.py            # PDF & JSON question ingestion tool
│   └── import_pipeline_v2/        # Ingestion pipeline scripts
│
└── assets/                        # Static UI Media & Styling
    └── custom.css                 # Premium custom Glassmorphism CSS
```

---

## 2. External Workspace Layout (`TNPSC_Nova_AI_Workspace`)

```text
TNPSC_Nova_AI_Workspace/
├── README.md                      # Workspace purpose & folder usage guide
├── 01_Gemini_Reports/             # Raw AI-generated reviews & code analysis
│   ├── practice_engine_bug_report.md
│   ├── practice_engine_performance_review.md
│   └── practice_engine_ux_review.md
├── 02_Implementation_Plans/       # Feature & migration implementation plan drafts
├── 03_Brainstorm/                 # Product concepts & feature ideas
├── 04_QA_Drafts/                  # Test execution logs & pass/fail matrices
│   ├── practice_engine_pass_fail_matrix.md
│   └── practice_engine_qa_report.md
├── 05_Research/                   # Benchmark findings & technology research
└── 06_Archive/                    # Obsolete working notes & closed feature drafts
```
