# TNPSC Nova AI 🚀
**Enterprise AI-Powered Competitive Exam Preparation Platform**

---

## 🌟 Overview

**TNPSC Nova AI** is a state-of-the-art learning platform designed for students preparing for Tamil Nadu Public Service Commission (TNPSC Group 1, Group 2, Group 4) examinations.

Built with Python and Streamlit, the platform features:
- **Decoupled Practice Engine**: High-performance practice workflows supporting 7 distinct question formats (Easy, Medium, Hard, Statement-Based, Assertion & Reason, Match the Following, Chronology).
- **Navigation v2 & Topic Hub**: Topic-centric workspace integrating syllabus revision notes, practice sets, past year question (PYQ) explorer, and AI teacher doubt resolution.
- **Adaptive Testing & Progress Analytics**: Real-time accuracy scoring, subject mastery tracking, weakness heatmaps, XP rewards, and streak tracking.

---

## 📚 Project Documentation System

TNPSC Nova AI follows a **Hybrid Documentation Strategy** governed by the official [Documentation Governance Policy v1.0](file:///c:/Users/Home/Desktop/tnpsc_ai/docs/documentation_policy.md).

For complete technical documentation, architecture blueprints, schemas, and developer roadmaps, consult the [Master Documentation Index](file:///c:/Users/Home/Desktop/tnpsc_ai/docs/DOCUMENTATION_INDEX.md).

### Documentation Quick Links

| Category | Description | Primary Document |
| :--- | :--- | :--- |
| 📖 **Governance** | Hybrid Documentation Policy & Guidelines | [docs/documentation_policy.md](file:///c:/Users/Home/Desktop/tnpsc_ai/docs/documentation_policy.md) |
| 🏛️ **Architecture** | System Blueprints, Layout Engines & Schemas | [docs/01_architecture/](file:///c:/Users/Home/Desktop/tnpsc_ai/docs/01_architecture/practice_engine_architecture.md) |
| 📊 **Audits** | Product Analysis & Gamification Audits | [docs/02_audit/](file:///c:/Users/Home/Desktop/tnpsc_ai/docs/02_audit/product_audit_report.md) |
| 🧪 **QA & Validation** | Quality Gate Checklist & Release Verdicts | [docs/03_qa/](file:///c:/Users/Home/Desktop/tnpsc_ai/docs/03_qa/practice_engine_final_verdict.md) |
| 🔄 **Migration** | Zero-Downtime Refactoring & Compatibility | [docs/04_migration/](file:///c:/Users/Home/Desktop/tnpsc_ai/docs/04_migration/migration_report.md) |
| 📝 **ADRs** | Architecture Decision Records | [docs/05_decisions/](file:///c:/Users/Home/Desktop/tnpsc_ai/docs/05_decisions/ADR-001-permanent-id.md) |
| 🚀 **Roadmaps** | Product & Learning Engine Pipelines | [docs/06_roadmap/](file:///c:/Users/Home/Desktop/tnpsc_ai/docs/06_roadmap/future_roadmap.md) |

---

## ⚡ Quick Start

### 1. Requirements
- Python 3.9 or higher

### 2. Environment Setup
```bash
# Clone the repository
git clone https://github.com/balasatheesh1005-svg/tnpsc_ai.git
cd tnpsc_ai

# Install dependencies
pip install -r requirements.txt
```

### 3. Launch Application
```bash
streamlit run app.py
```

---

## 📁 Repository Directory Layout

```text
tnpsc_ai/
├── app.py                         # Application entry point
├── README.md                      # Project documentation (this file)
├── requirements.txt               # Dependencies
├── .gitignore                     # Git ignore rules
├── core/                          # Backend engines (question loader, practice session, db)
├── ui/                            # Streamlit layout renderers & Topic Hub components
├── data/                          # Question repositories & subject revision notes
├── docs/                          # Master Documentation Tree (Adheres to Hybrid Policy)
├── tools/                         # Ingestion pipelines & data utilities
└── assets/                        # Static UI assets & branding
```

---

## 🛡️ License & Governance

Managed under enterprise development standards. See [Documentation Governance Policy v1.0](file:///c:/Users/Home/Desktop/tnpsc_ai/docs/documentation_policy.md) for contribution rules.
