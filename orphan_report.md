# TNPSC Nova AI — Identity Migration v1.0
## Orphan Record Audit & Management Report

**Architect:** Lead Database Architect, TNPSC Nova AI  
**Date:** July 25, 2026  
**Status:** Complete Audit & Strategy Formulation  
**Phase Target:** Phase 2 Data Backfill & Phase 3 Readiness  

---

## 1. Executive Summary

This report establishes the **Orphan Record Audit & Management Strategy** for Phase 2 of the TNPSC Nova AI identity migration.

In the database context of TNPSC Nova AI, an **orphan record** is defined as any database row in a user-related application table (`users_progress`, `user_xp`, `users_weakness`, `user_revisions`, `user_streaks`, `daily_missions`, `mentor_memory`, `bookmarks`, `user_analytics`) whose `username` string does **NOT** match any existing record in `public.profiles.username`.

### Core Safety Directives
> [!IMPORTANT]
> **Data Retention Policy**: Orphan records must **NEVER** be deleted during Phase 2.
> All historical user data, analytics, test progress, and revision states must be preserved without data loss.

> [!NOTE]
> In Phase 2, orphan rows will simply maintain `user_id = NULL`. Their existing `username` functionality remains 100% operational in the application layer.

---

## 2. Root Cause Analysis

Orphan records in TNPSC Nova AI typically originate from three distinct scenarios:

1. **Legacy User Registration**: Historical records created before standard Supabase Auth trigger integration (`handle_new_user`), where activity was logged under a raw `username` without inserting a corresponding row into `public.profiles`.
2. **Account Deletions**: Scenarios where a user profile was removed from `auth.users` / `public.profiles`, but transactional data (e.g., `user_analytics`, `user_revisions`) was preserved for auditing or reporting purposes.
3. **Development & Synthetic Testing**: Test runs, benchmarking scripts, or seed routines executed under placeholder usernames (e.g., `test_user`, `admin_demo`, `benchmark_runner`).

---

## 3. SQL Detection Queries by Table

To audit and identify all orphan records across the database, execute the following targeted SQL queries:

### 3.1 `users_progress` Orphans
```sql
SELECT username, COUNT(*) AS orphan_row_count
FROM public.users_progress
WHERE username NOT IN (SELECT username FROM public.profiles)
GROUP BY username
ORDER BY orphan_row_count DESC;
```

### 3.2 `user_xp` Orphans
```sql
SELECT username, xp, level
FROM public.user_xp
WHERE username NOT IN (SELECT username FROM public.profiles);
```

### 3.3 `users_weakness` Orphans
```sql
SELECT username, COUNT(*) AS orphan_row_count
FROM public.users_weakness
WHERE username NOT IN (SELECT username FROM public.profiles)
GROUP BY username
ORDER BY orphan_row_count DESC;
```

### 3.4 `user_revisions` Orphans
```sql
SELECT username, COUNT(*) AS orphan_row_count
FROM public.user_revisions
WHERE username NOT IN (SELECT username FROM public.profiles)
GROUP BY username
ORDER BY orphan_row_count DESC;
```

### 3.5 `user_streaks` Orphans
```sql
SELECT username, current_streak, max_streak
FROM public.user_streaks
WHERE username NOT IN (SELECT username FROM public.profiles);
```

### 3.6 `daily_missions` Orphans
```sql
SELECT username, COUNT(*) AS orphan_row_count
FROM public.daily_missions
WHERE username NOT IN (SELECT username FROM public.profiles)
GROUP BY username
ORDER BY orphan_row_count DESC;
```

### 3.7 `mentor_memory` Orphans
```sql
SELECT username, updated_at
FROM public.mentor_memory
WHERE username NOT IN (SELECT username FROM public.profiles);
```

### 3.8 `bookmarks` Orphans
```sql
SELECT username, COUNT(*) AS orphan_row_count
FROM public.bookmarks
WHERE username NOT IN (SELECT username FROM public.profiles)
GROUP BY username
ORDER BY orphan_row_count DESC;
```

### 3.9 `user_analytics` Orphans
```sql
SELECT username, COUNT(*) AS orphan_row_count
FROM public.user_analytics
WHERE username NOT IN (SELECT username FROM public.profiles)
GROUP BY username
ORDER BY orphan_row_count DESC;
```

---

## 4. Master Consolidated Orphan Identification Query

Run this single SQL statement to generate a complete inventory of all distinct orphan usernames across all 9 user tables:

```sql
WITH all_usernames AS (
    SELECT username, 'users_progress' AS source_table FROM public.users_progress
    UNION ALL
    SELECT username, 'user_xp' FROM public.user_xp
    UNION ALL
    SELECT username, 'users_weakness' FROM public.users_weakness
    UNION ALL
    SELECT username, 'user_revisions' FROM public.user_revisions
    UNION ALL
    SELECT username, 'user_streaks' FROM public.user_streaks
    UNION ALL
    SELECT username, 'daily_missions' FROM public.daily_missions
    UNION ALL
    SELECT username, 'mentor_memory' FROM public.mentor_memory
    UNION ALL
    SELECT username, 'bookmarks' FROM public.bookmarks
    UNION ALL
    SELECT username, 'user_analytics' FROM public.user_analytics
)
SELECT 
    u.username AS orphan_username,
    COUNT(DISTINCT u.source_table) AS affected_table_count,
    COUNT(*) AS total_orphan_rows,
    ARRAY_AGG(DISTINCT u.source_table) AS affected_tables
FROM all_usernames AS u
LEFT JOIN public.profiles AS p ON u.username = p.username
WHERE p.username IS NULL
GROUP BY u.username
ORDER BY total_orphan_rows DESC;
```

---

## 5. Impact Analysis on Phase 3

In Phase 3 of the Identity Migration, the database schema will enforce strict constraints:
- `user_id` columns will be transitioned to `NOT NULL`.
- Foreign Key relationships referencing `public.profiles(id)` will be strictly enforced.

If orphan records remain unhandled with `user_id IS NULL` when Phase 3 executes, the DDL command `ALTER TABLE ... ALTER COLUMN user_id SET NOT NULL;` will **fail** with a constraint violation error.

---

## 6. Recommended Resolution Options Prior to Phase 3

Before executing Phase 3 constraint enforcement, Database Administrators should select one of the following resolution pathways:

### Option A: Synthetic Profile Backfill (Recommended)
For valid historical users who lack a Supabase Auth entry, generate placeholder profiles in `public.profiles`:
```sql
INSERT INTO public.profiles (id, username, email, full_name)
SELECT 
    gen_random_uuid(),
    orphan_username,
    orphan_username || '@legacy.tnpscnova.ai',
    'Legacy User (' || orphan_username || ')'
FROM (
    -- Subquery of orphan usernames from Master Orphan Query
) AS orphans
ON CONFLICT (username) DO NOTHING;
```
*Outcome*: Converts orphan records into valid profile-backed records, enabling 100% successful Phase 2 backfill and Phase 3 constraint application.

### Option B: Account Reconciliation & User Linking
Provide an administrative UI or CLI script allowing users with legacy usernames to link their historical data to their new Supabase Auth account.

### Option C: Historical Data Archival
Move orphan rows into dedicated archive tables (e.g., `archive.user_analytics_legacy`) before Phase 3 enforcement if the data is purely historical and no longer associated with active accounts.

---

## 7. Phase 2 Verification Protocol

During Phase 2 execution:
1. Verify that orphan records are accurately counted and reported in `validation_queries.sql`.
2. Confirm that orphan records remain completely unaffected in their `username` functionality.
3. Sign off on the orphan record inventory prior to approving Phase 3 schema lockdown.
