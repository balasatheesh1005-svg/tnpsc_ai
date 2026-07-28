# TNPSC Nova AI — Documentation Governance Policy v1.0
**(Hybrid Documentation Strategy)**

---

## 1. Overview & Purpose

The **TNPSC Nova AI Documentation Governance Policy** defines the mandatory standards for organizing, maintaining, and archiving documentation across the project lifecycle. 

As TNPSC Nova AI evolves into an enterprise-grade AI exam preparation system, maintaining a clean, clutter-free production repository while preserving full historical context and architectural decisions is paramount.

This policy establishes a **Hybrid Documentation Strategy**:
1. **Permanent Documentation**: Strictly curated, production-grade blueprints, architecture decision records, roadmaps, setup guides, and documentation indexes stored inside the GitHub repository (`docs/`).
2. **Temporary Working Documentation**: AI-generated working drafts, pass/fail matrices, bug logs, feature ideas, and raw scratchpads stored outside the GitHub repository in an **External Workspace** (`TNPSC_Nova_AI_Workspace/`).

---

## 2. In-Repository Documentation Structure

All permanent documentation inside the repository must be placed in `docs/` adhering to the standard folder hierarchy:

```text
docs/
├── DOCUMENTATION_INDEX.md         # Master hyperlinked documentation catalog
├── documentation_policy.md        # This governance standard
├── 01_architecture/               # System architecture, schemas, and design specs
├── 02_audit/                      # Product audits, progress & learning analysis
├── 03_qa/                         # Latest production-ready QA verdicts & checklists
├── 04_migration/                  # Refactoring reports, migration notes, user flows
├── 05_decisions/                  # Architecture Decision Records (ADR-xxx)
├── 06_roadmap/                    # Future milestones, feature & learning engine roadmaps
└── 99_archive/                    # Superseded architectural notes & legacy flows
```

### Classification Rules for In-Repository Docs:
- **`01_architecture/`**: Holds immutable blueprints, schema specifications (`MCQ`, `Notes`), component module maps, and frozen design specs.
- **`02_audit/`**: Holds high-level product evaluations, gamification reviews, and strategic backlog audits.
- **`03_qa/`**: Holds **only the single latest production-ready QA report** and active validation checklists. Draft QA logs belong in the External Workspace.
- **`04_migration/`**: Holds zero-downtime refactoring notes, backward compatibility guides, and user navigation maps.
- **`05_decisions/`**: Holds Architecture Decision Records (ADRs) formatted according to standard enterprise ADR templates.
- **`06_roadmap/`**: Holds core product, UI feature, and AI learning engine evolution roadmaps.
- **`99_archive/`**: Holds legacy documentation replaced by newer versions. Files must never be deleted; they are archived here.

---

## 3. External Workspace Policy

To prevent repository clutter, temporary and working documents created during active development cycles must be placed outside the GitHub repository in `TNPSC_Nova_AI_Workspace/`.

```text
TNPSC_Nova_AI_Workspace/
├── README.md                      # External workspace overview & usage guide
├── 01_Gemini_Reports/             # Raw AI reviews, code analysis & comparisons
├── 02_Implementation_Plans/       # Active & past feature implementation plans
├── 03_Brainstorm/                 # Product concepts, feature ideas & UX sketches
├── 04_QA_Drafts/                  # Test execution logs, pass/fail matrices & bug reports
├── 05_Research/                   # Benchmark findings, competitor analysis & AI research
└── 06_Archive/                    # Obsolete drafts and closed feature working notes
```

---

## 4. Root Directory Governance Policy

The project root (`c:\Users\Home\Desktop\tnpsc_ai`) must remain strictly minimal and professional.

### Permitted Root Items:
- `app.py` (Main Streamlit entry point)
- `README.md` (High-level project introduction pointing to `docs/`)
- `requirements.txt` (Python dependencies)
- `.gitignore` (Git ignore patterns)
- `core/` (Backend modules)
- `ui/` (Frontend & layout modules)
- `data/` (Question & notes JSON payloads)
- `docs/` (Permanent documentation tree)
- `tools/` (Utility & ingestion scripts)
- `assets/` (Static visual assets & images)

### Prohibited Root Items:
- ❌ **No `.md` files in root** except `README.md`
- ❌ **No temporary AI scratchpads** or working drafts
- ❌ **No unused placeholder files** (such as empty `tests/` directories, dummy `Dockerfile`s, unfinalized `LICENSE` files, or unneeded `pyproject.toml` files)

---

## 5. Monthly Cleanup & Maintenance Workflow

On the **1st business day of each month**, the repository maintainer must execute the following cleanup checklist:

1. **Review Root Directory**: Verify that no new `.md` files or scratch scripts were committed to root.
2. **Classify Working Files**: Move completed working drafts from the repository into the External Workspace (`TNPSC_Nova_AI_Workspace/`).
3. **Archive Obsolete Docs**: Move superseded architecture notes or old QA reports to `docs/99_archive/`.
4. **Update `DOCUMENTATION_INDEX.md`**: Synchronize links for any newly added permanent docs or ADRs.
5. **Review Roadmaps & ADRs**: Ensure roadmaps reflect recent feature completions and new architectural decisions are logged.
6. **Link Health Check**: Run a link check across markdown files to ensure no broken relative file links exist.

---

## 6. Guidelines for AI Coding Assistants

All AI agents (Gemini, ChatGPT, Claude, Cursor, Copilot, Codex) interacting with this codebase must enforce these guidelines:

1. **Never pollute project root**: Output temporary working plans or analysis directly into artifacts or the External Workspace.
2. **Never modify application logic during documentation tasks**: Maintain strict separation between code execution and documentation organization.
3. **Respect folder hierarchy**: Place all permanent technical documentation under the designated `docs/0x_...` directory.
4. **Maintain Hyperlinks**: When referencing code symbols or documentation files, use Markdown file links (`file:///...`).
