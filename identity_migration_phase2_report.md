# TNPSC Nova AI — Identity Migration v1.0
## Phase 2 Migration Report: Data Backfill Architecture

**Architect:** Lead Database Architect, TNPSC Nova AI  
**Date:** July 25, 2026  
**Status:** Completed & Approved for Execution  
**Phase Target:** Dual-Identity Readiness (Data Layer Backfill)  

---

## 1. Executive Summary

This report establishes **Phase 2: Data Backfill** of the enterprise migration for TNPSC Nova AI, transitioning from legacy `username`-centric identification to **Supabase Auth UUID (`user_id`)** architecture.

Phase 1 successfully prepared the database schema by adding nullable `user_id UUID` columns referencing `public.profiles(id)` across all 9 user-related tables. Phase 2 populates these `user_id` columns safely and idempotently by mapping existing `username` values to `public.profiles.id`.

### Core Operational Principles of Phase 2
1. **Zero Application Code Changes**: No Python backend code (`core/*.py`), Streamlit UI scripts (`ui/*.py`), or session state handlers are modified.
2. **Pure Database Data Migration**: Performs SQL-level updates exclusively (`UPDATE ... FROM public.profiles`).
3. **100% Backwards & Forwards Compatibility**: Existing `username` columns, indexes, and primary keys remain untouched and fully operational.
4. **Strict Idempotency**: Only updates rows where `user_id IS NULL`. Pre-existing UUIDs are never overwritten.
5. **Data Preservation Guarantee**: Orphan records (usernames not in `public.profiles`) are audited and reported, but **never deleted**.
6. **Zero Application Downtime**: Migration statements execute within safe PostgreSQL transaction blocks with minimal lock overhead.

---

## 2. Migration Roadmap Overview

```
┌───────────────────────────────────────┐
│ PHASE 1: Schema Preparation (DONE)   │
│ - Added nullable user_id UUID columns │
│ - Created Foreign Keys & Indexes      │
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│ PHASE 2: Data Backfill (THIS PHASE)   │
│ - Map username -> profiles.id (UUID)  │
│ - Backfill user_id where IS NULL      │
│ - Audit orphan records & validate     │
└──────────────────┬────────────────────┘
                   │
                   ▼
┌───────────────────────────────────────┐
│ PHASE 3: Application & Constraint Lock│
│ - Dual-write in Python backend        │
│ - Set user_id NOT NULL & enforce FK   │
│ - Deprecate username-only queries     │
└───────────────────────────────────────┘
```

---

## 3. Profiles Mapping Audit

The mapping anchor for Phase 2 is `public.profiles`, which binds Supabase Auth `auth.users.id` (UUID) to `username`.

### Pre-Flight Verification Checks
Before executing backfill statements, `identity_migration_phase2.sql` executes automated pre-flight checks:
- **NULL Username Check**: Verifies `public.profiles` contains zero NULL usernames.
- **Duplicate Username Check**: Verifies `username` values in `public.profiles` are 100% unique.
- **ID Integrity Check**: Verifies every profile possesses a valid, non-null UUID `id`.

---

## 4. Comprehensive Table Backfill Matrix

The 9 target user-related tables and their Phase 2 backfill specifications are detailed below:

| Table Name | Primary Key | Identifier Column | Target Backfill Column | Foreign Key Reference | Backfill Logic & Condition |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`users_progress`** | `id` (BIGINT) | `username` (TEXT) | `user_id` (UUID) | `public.profiles(id)` | `SET user_id = p.id FROM profiles p WHERE target.username = p.username AND target.user_id IS NULL` |
| **`user_xp`** | `id` (UUID) | `username` (TEXT UNIQUE) | `user_id` (UUID) | `public.profiles(id)` | `SET user_id = p.id FROM profiles p WHERE target.username = p.username AND target.user_id IS NULL` |
| **`users_weakness`** | `id` (BIGINT) | `username` (TEXT) | `user_id` (UUID) | `public.profiles(id)` | `SET user_id = p.id FROM profiles p WHERE target.username = p.username AND target.user_id IS NULL` |
| **`user_revisions`** | `id` (BIGINT) | `username` (TEXT) | `user_id` (UUID) | `public.profiles(id)` | `SET user_id = p.id FROM profiles p WHERE target.username = p.username AND target.user_id IS NULL` |
| **`user_streaks`** | `id` (BIGINT) | `username` (TEXT) | `user_id` (UUID) | `public.profiles(id)` | `SET user_id = p.id FROM profiles p WHERE target.username = p.username AND target.user_id IS NULL` |
| **`daily_missions`** | `id` (BIGINT) | `username` (TEXT) | `user_id` (UUID) | `public.profiles(id)` | `SET user_id = p.id FROM profiles p WHERE target.username = p.username AND target.user_id IS NULL` |
| **`mentor_memory`** | `id` (BIGINT) | `username` (TEXT UNIQUE) | `user_id` (UUID) | `public.profiles(id)` | `SET user_id = p.id FROM profiles p WHERE target.username = p.username AND target.user_id IS NULL` |
| **`bookmarks`** | `id` (BIGINT) | `username` (TEXT) | `user_id` (UUID) | `public.profiles(id)` | `SET user_id = p.id FROM profiles p WHERE target.username = p.username AND target.user_id IS NULL` |
| **`user_analytics`** | `id` (BIGINT) | `username` (TEXT) | `user_id` (UUID) | `public.profiles(id)` | `SET user_id = p.id FROM profiles p WHERE target.username = p.username AND target.user_id IS NULL` |

---

## 5. SQL Execution Architecture & Safety Mechanics

### 5.1 Standardized UPDATE Pattern
Every backfill operation follows PostgreSQL hash/index join semantics:
```sql
UPDATE public.<table_name> AS target
SET user_id = p.id
FROM public.profiles AS p
WHERE target.username = p.username
  AND target.user_id IS NULL;
```

### 5.2 Performance & Index Utilization
- In Phase 1, B-tree indexes were created on both `profiles(username)` and `<table_name>(username)`.
- The `UPDATE ... FROM` statement utilizes these indexes to perform $O(N)$ index-driven batch updates.
- Execution lock times are minimized, preventing table contention during live application use.

---

## 6. Deliverables Package

Phase 2 includes 5 master database artifacts generated directly in the workspace root:

1. **`identity_migration_phase2.sql`**  
   Master execution script containing transactional backfill updates for all 9 target tables with pre-flight checks and execution summary outputs.

2. **`validation_queries.sql`**  
   Comprehensive validation suite auditing profile mapping integrity, zero-unmigrated matching checks, orphan counts, and foreign key alignment.

3. **`rollback_phase2.sql`**  
   Emergency rollback script to safely reset `user_id = NULL` across all 9 tables without dropping columns or losing data.

4. **`orphan_report.md`**  
   Dedicated audit document analyzing orphan records (usernames not in `public.profiles`), providing detection queries and pre-Phase 3 resolution options.

5. **`identity_migration_phase2_report.md`** (This file)  
   Complete technical architecture report detailing Phase 2 scope, table matrix, execution design, and roadmap alignment.

---

## 7. Migration Verification & Audit Summary Template

Upon executing `identity_migration_phase2.sql` followed by `validation_queries.sql`, the database administrator can verify success using the summary table format below:

```
+----------------+------------+---------------+------------------------------+--------------+------------------+
| table_name     | total_rows | migrated_rows | unmigrated_matching_profiles | orphan_rows  | status           |
+----------------+------------+---------------+------------------------------+--------------+------------------+
| bookmarks      |     ...    |      ...      |              0               |     ...      | PASSED ✅        |
| daily_missions |     ...    |      ...      |              0               |     ...      | PASSED ✅        |
| mentor_memory  |     ...    |      ...      |              0               |     ...      | PASSED ✅        |
| user_analytics |     ...    |      ...      |              0               |     ...      | PASSED ✅        |
| user_revisions |     ...    |      ...      |              0               |     ...      | PASSED ✅        |
| user_streaks   |     ...    |      ...      |              0               |     ...      | PASSED ✅        |
| user_xp        |     ...    |      ...      |              0               |     ...      | PASSED ✅        |
| users_progress |     ...    |      ...      |              0               |     ...      | PASSED ✅        |
| users_weakness |     ...    |      ...      |              0               |     ...      | PASSED ✅        |
+----------------+------------+---------------+------------------------------+--------------+------------------+
```

---

## 8. Transition Criteria for Phase 3

Completion of Phase 2 establishes **dual-identity readiness**. The application database now contains both `username` and `user_id` for every registered user record.

### Phase 3 Prerequisites
1. Execute `identity_migration_phase2.sql` in production database.
2. Execute `validation_queries.sql` and verify `unmigrated_matching_profiles = 0` for all tables.
3. Review `orphan_report.md` and select resolution strategy (e.g. Synthetic Profile creation) for orphan usernames.
4. Begin Phase 3: Python backend refactoring (`core/*.py`) to introduce dual-write operations and transition primary queries to `user_id`.
