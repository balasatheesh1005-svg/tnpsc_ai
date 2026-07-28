# TNPSC Nova AI — Identity Migration v1.0
## Phase 1 Migration Report: Database Schema Preparation

**Architect:** Lead Database Architect, TNPSC Nova AI  
**Date:** July 23, 2026  
**Status:** Approved for Schema Execution (Phase 1 Database Preparation Only)  

---

## 1. Executive Summary

This report establishes **Phase 1: Database Schema Preparation** for the enterprise migration of TNPSC Nova AI from legacy `username`-centric identification to standard **Supabase Auth UUID (`user_id`)** architecture.

### Key Principles of Phase 1
1. **Zero Code Disruption**: No Python backend code (`core/*.py`), Streamlit UI components (`ui/*.py`), or session state managers are modified.
2. **Schema Preparation Only**: Adds a nullable `user_id UUID` column and Foreign Key relationship referencing `public.profiles(id)` across all user-related tables.
3. **100% Backwards Compatibility**: Existing `username` columns, unique keys, and primary keys remain active. Current read/write operations continue without disruption.
4. **Non-Blocking Schema Adjustments**: No `NOT NULL` constraints, trigger enforcement, or mandatory column drops are applied in this phase.

---

## 2. Comprehensive User-Related Table Audit

Every user-related database table in the TNPSC Nova AI workspace has been inspected. The complete list of target tables and their migration specifications are detailed below.

### Table Migration Summary Matrix

| Table Name | Current Primary Key | Current User Identifier | Recommended Phase 1 Change | Foreign Key Reference |
| :--- | :--- | :--- | :--- | :--- |
| **`profiles`** | `id` (UUID) | `id` (UUID), `username`, `email` | Retain schema; verify PK references `auth.users(id)` | `auth.users(id)` |
| **`users_progress`** | `id` (BIGINT / IDENTITY) | `username` (TEXT) | Add `user_id UUID` (NULLABLE) + Index | `public.profiles(id)` |
| **`user_xp`** | `id` (UUID) | `username` (TEXT UNIQUE) | Add `user_id UUID` (NULLABLE) + Index | `public.profiles(id)` |
| **`users_weakness`** | `id` (BIGINT / IDENTITY) | `username` (TEXT) | Add `user_id UUID` (NULLABLE) + Index | `public.profiles(id)` |
| **`user_revisions`** | `id` (BIGINT / IDENTITY) | `username` (TEXT) | Add `user_id UUID` (NULLABLE) + Index | `public.profiles(id)` |
| **`user_streaks`** | `id` (BIGINT / IDENTITY) | `username` (TEXT) | Add `user_id UUID` (NULLABLE) + Index | `public.profiles(id)` |
| **`daily_missions`** | `id` (BIGINT / IDENTITY) | `username` (TEXT) | Add `user_id UUID` (NULLABLE) + Index | `public.profiles(id)` |
| **`mentor_memory`** | `id` (BIGINT / IDENTITY) | `username` (TEXT UNIQUE) | Add `user_id UUID` (NULLABLE) + Index | `public.profiles(id)` |
| **`bookmarks`** | `id` (BIGINT / IDENTITY) | `username` (TEXT) | Add `user_id UUID` (NULLABLE) + Index | `public.profiles(id)` |
| **`user_analytics`** | `id` (BIGINT / IDENTITY) | `username` (TEXT) | Add `user_id UUID` (NULLABLE) + Index | `public.profiles(id)` |

---

## 3. Individual Table Specifications

### 3.1. Table: `profiles`
- **Role**: Primary user metadata table created upon Supabase Auth signup.
- **Current PK**: `id` (UUID).
- **Current Identifiers**: `id` (UUID), `username` (TEXT UNIQUE), `email` (TEXT UNIQUE).
- **Phase 1 Action**: No structural alteration required. Acts as the root lookup table where `profiles.id = auth.users.id`. Ensure index `idx_profiles_id` and `idx_profiles_username` are verified.

### 3.2. Table: `users_progress`
- **Role**: Stores subject/topic question accuracy, total attempted, correct count.
- **Current PK**: `id` (BIGINT / IDENTITY).
- **Current Identifier**: `username` (TEXT).
- **Phase 1 Action**: `ALTER TABLE public.users_progress ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;`
- **Index**: `CREATE INDEX IF NOT EXISTS idx_users_progress_user_id ON public.users_progress(user_id);`

### 3.3. Table: `user_xp`
- **Role**: Gamification system tracking user XP points and current user level.
- **Current PK**: `id` (UUID).
- **Current Identifier**: `username` (TEXT UNIQUE).
- **Phase 1 Action**: `ALTER TABLE public.user_xp ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;`
- **Index**: `CREATE INDEX IF NOT EXISTS idx_user_xp_user_id ON public.user_xp(user_id);`

### 3.4. Table: `users_weakness`
- **Role**: Tracks user subtopic error rates and weakness heatmaps.
- **Current PK**: `id` (BIGINT / IDENTITY).
- **Current Identifier**: `username` (TEXT).
- **Phase 1 Action**: `ALTER TABLE public.users_weakness ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;`
- **Index**: `CREATE INDEX IF NOT EXISTS idx_users_weakness_user_id ON public.users_weakness(user_id);`

### 3.5. Table: `user_revisions`
- **Role**: Spaced repetition engine tracking review dates, interval, ease factor, repetitions.
- **Current PK**: `id` (BIGINT / IDENTITY).
- **Current Identifier**: `username` (TEXT).
- **Phase 1 Action**: `ALTER TABLE public.user_revisions ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;`
- **Index**: `CREATE INDEX IF NOT EXISTS idx_user_revisions_user_id ON public.user_revisions(user_id);`

### 3.6. Table: `user_streaks`
- **Role**: Daily learning streak tracking (current streak, max streak, last active date).
- **Current PK**: `id` (BIGINT / IDENTITY).
- **Current Identifier**: `username` (TEXT).
- **Phase 1 Action**: `ALTER TABLE public.user_streaks ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;`
- **Index**: `CREATE INDEX IF NOT EXISTS idx_user_streaks_user_id ON public.user_streaks(user_id);`

### 3.7. Table: `daily_missions`
- **Role**: Daily task completions and streak milestone tracking.
- **Current PK**: `id` (BIGINT / IDENTITY).
- **Current Identifier**: `username` (TEXT).
- **Phase 1 Action**: `ALTER TABLE public.daily_missions ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;`
- **Index**: `CREATE INDEX IF NOT EXISTS idx_daily_missions_user_id ON public.daily_missions(user_id);`

### 3.8. Table: `mentor_memory`
- **Role**: Context memory and summary store for AI Personal Mentor.
- **Current PK**: `id` (BIGINT / IDENTITY).
- **Current Identifier**: `username` (TEXT UNIQUE).
- **Phase 1 Action**: `ALTER TABLE public.mentor_memory ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;`
- **Index**: `CREATE INDEX IF NOT EXISTS idx_mentor_memory_user_id ON public.mentor_memory(user_id);`

### 3.9. Table: `bookmarks`
- **Role**: Saved question bookmarks and study quick-savers.
- **Current PK**: `id` (BIGINT / IDENTITY).
- **Current Identifier**: `username` (TEXT).
- **Phase 1 Action**: `ALTER TABLE public.bookmarks ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;`
- **Index**: `CREATE INDEX IF NOT EXISTS idx_bookmarks_user_id ON public.bookmarks(user_id);`

### 3.10. Table: `user_analytics`
- **Role**: Event tracking logs for user app interaction analysis.
- **Current PK**: `id` (BIGINT / IDENTITY).
- **Current Identifier**: `username` (TEXT).
- **Phase 1 Action**: `ALTER TABLE public.user_analytics ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;`
- **Index**: `CREATE INDEX IF NOT EXISTS idx_user_analytics_user_id ON public.user_analytics(user_id);`

---

## 4. Code Compatibility & Safety Verification

| Component / Subsystem | Verification Status | Explanation |
| :--- | :--- | :--- |
| **`core/auth.py`** | ✅ 100% Compatible | Login, signup, and session functions continue reading/writing `profiles` by `id` or `username`. |
| **`core/progress_ai.py`** | ✅ 100% Compatible | `users_progress` queries continue using `username`. Nullable `user_id` column does not conflict. |
| **`core/xp_ai.py`** | ✅ 100% Compatible | `user_xp` upserts match on `username`. Nullable `user_id` column remains unused by current code. |
| **`core/revision_ai.py`** | ✅ 100% Compatible | `user_revisions` upserts match on `username, subject, topic`. Schema addition is fully transparent. |
| **`core/weakness_ai.py`** | ✅ 100% Compatible | `users_weakness` updates match on `username`. No query changes needed in Phase 1. |
| **`core/streak_ai.py`** | ✅ 100% Compatible | `user_streaks` checks match on `username`. Operations remain unchanged. |
| **`core/daily_mission_ai.py`**| ✅ 100% Compatible | `daily_missions` lookups operate by `username`. |
| **`core/mentor_memory.py`** | ✅ 100% Compatible | `mentor_memory` queries filter by `username`. |
| **Streamlit UI (`ui/*`)** | ✅ 100% Compatible | Zero UI files modified. All rendering components function identically. |

---

## 5. Next Steps — Preparation for Phase 2

Phase 1 establishes the database structure for **Phase 2 (Data Backfill & Dual-Write Engine)**.  
When Phase 2 is triggered, the following sequential steps will be executed:
1. **Backfill Script**: Populate `user_id` in all 10 tables by joining existing rows with `profiles` on `username`.
2. **Dual-Write Updates in Python**: Update `core/*.py` modules to write both `username` and `user_id`.
3. **Validation & Audit**: Verify 100% of rows have non-null `user_id` matching `profiles.id`.
4. **Constraint Enforcement (Phase 3)**: Enable `NOT NULL` on `user_id` and transition primary lookups to `user_id`.
