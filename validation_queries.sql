-- =============================================================================
-- TNPSC Nova AI — Identity Migration v1.0
-- PHASE 2: Validation & Audit Queries (SQL Script)
-- =============================================================================
-- Purpose: Rigorously verify Phase 2 data backfill accuracy, check for zero
--          unmigrated matching rows, identify orphan records, and validate FK integrity.
-- Scope: Read-only verification queries.
-- Author: Lead Database Architect, TNPSC Nova AI
-- Date: July 25, 2026
-- =============================================================================

-- -----------------------------------------------------------------------------
-- SECTION 1: PROFILES TABLE INTEGRITY AUDIT
-- -----------------------------------------------------------------------------

-- 1.1 Check for NULL usernames in profiles (Target: 0)
SELECT 
    'profiles_null_username_check' AS audit_name,
    COUNT(*) AS issue_count,
    CASE WHEN COUNT(*) = 0 THEN 'PASSED' ELSE 'FAILED' END AS audit_status
FROM public.profiles
WHERE username IS NULL;

-- 1.2 Check for duplicate usernames in profiles (Target: 0)
SELECT 
    'profiles_duplicate_username_check' AS audit_name,
    COUNT(username) - COUNT(DISTINCT username) AS issue_count,
    CASE WHEN COUNT(username) - COUNT(DISTINCT username) = 0 THEN 'PASSED' ELSE 'FAILED' END AS audit_status
FROM public.profiles;

-- 1.3 Check for NULL IDs in profiles (Target: 0)
SELECT 
    'profiles_null_id_check' AS audit_name,
    COUNT(*) AS issue_count,
    CASE WHEN COUNT(*) = 0 THEN 'PASSED' ELSE 'FAILED' END AS audit_status
FROM public.profiles
WHERE id IS NULL;


-- -----------------------------------------------------------------------------
-- SECTION 2: INDIVIDUAL TABLE VALIDATION QUERIES
-- Target for unmigrated_matching_profiles: ALWAYS 0
-- Target for fk_mismatches: ALWAYS 0
-- -----------------------------------------------------------------------------

-- 2.1 Table: users_progress
SELECT 
    'users_progress' AS table_name,
    COUNT(*) AS total_rows,
    COUNT(user_id) AS migrated_rows,
    SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS unmigrated_matching_profiles,
    SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS orphan_rows,
    SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) AS fk_mismatches,
    CASE 
        WHEN SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) = 0 
         AND SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) = 0 
        THEN 'PASSED' 
        ELSE 'FAILED' 
    END AS validation_status
FROM public.users_progress AS target
LEFT JOIN public.profiles AS p ON target.username = p.username;

-- 2.2 Table: user_xp
SELECT 
    'user_xp' AS table_name,
    COUNT(*) AS total_rows,
    COUNT(user_id) AS migrated_rows,
    SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS unmigrated_matching_profiles,
    SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS orphan_rows,
    SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) AS fk_mismatches,
    CASE 
        WHEN SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) = 0 
         AND SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) = 0 
        THEN 'PASSED' 
        ELSE 'FAILED' 
    END AS validation_status
FROM public.user_xp AS target
LEFT JOIN public.profiles AS p ON target.username = p.username;

-- 2.3 Table: users_weakness
SELECT 
    'users_weakness' AS table_name,
    COUNT(*) AS total_rows,
    COUNT(user_id) AS migrated_rows,
    SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS unmigrated_matching_profiles,
    SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS orphan_rows,
    SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) AS fk_mismatches,
    CASE 
        WHEN SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) = 0 
         AND SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) = 0 
        THEN 'PASSED' 
        ELSE 'FAILED' 
    END AS validation_status
FROM public.users_weakness AS target
LEFT JOIN public.profiles AS p ON target.username = p.username;

-- 2.4 Table: user_revisions
SELECT 
    'user_revisions' AS table_name,
    COUNT(*) AS total_rows,
    COUNT(user_id) AS migrated_rows,
    SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS unmigrated_matching_profiles,
    SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS orphan_rows,
    SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) AS fk_mismatches,
    CASE 
        WHEN SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) = 0 
         AND SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) = 0 
        THEN 'PASSED' 
        ELSE 'FAILED' 
    END AS validation_status
FROM public.user_revisions AS target
LEFT JOIN public.profiles AS p ON target.username = p.username;

-- 2.5 Table: user_streaks
SELECT 
    'user_streaks' AS table_name,
    COUNT(*) AS total_rows,
    COUNT(user_id) AS migrated_rows,
    SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS unmigrated_matching_profiles,
    SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS orphan_rows,
    SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) AS fk_mismatches,
    CASE 
        WHEN SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) = 0 
         AND SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) = 0 
        THEN 'PASSED' 
        ELSE 'FAILED' 
    END AS validation_status
FROM public.user_streaks AS target
LEFT JOIN public.profiles AS p ON target.username = p.username;

-- 2.6 Table: daily_missions
SELECT 
    'daily_missions' AS table_name,
    COUNT(*) AS total_rows,
    COUNT(user_id) AS migrated_rows,
    SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS unmigrated_matching_profiles,
    SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS orphan_rows,
    SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) AS fk_mismatches,
    CASE 
        WHEN SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) = 0 
         AND SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) = 0 
        THEN 'PASSED' 
        ELSE 'FAILED' 
    END AS validation_status
FROM public.daily_missions AS target
LEFT JOIN public.profiles AS p ON target.username = p.username;

-- 2.7 Table: mentor_memory
SELECT 
    'mentor_memory' AS table_name,
    COUNT(*) AS total_rows,
    COUNT(user_id) AS migrated_rows,
    SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS unmigrated_matching_profiles,
    SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS orphan_rows,
    SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) AS fk_mismatches,
    CASE 
        WHEN SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) = 0 
         AND SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) = 0 
        THEN 'PASSED' 
        ELSE 'FAILED' 
    END AS validation_status
FROM public.mentor_memory AS target
LEFT JOIN public.profiles AS p ON target.username = p.username;

-- 2.8 Table: bookmarks
SELECT 
    'bookmarks' AS table_name,
    COUNT(*) AS total_rows,
    COUNT(user_id) AS migrated_rows,
    SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS unmigrated_matching_profiles,
    SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS orphan_rows,
    SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) AS fk_mismatches,
    CASE 
        WHEN SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) = 0 
         AND SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) = 0 
        THEN 'PASSED' 
        ELSE 'FAILED' 
    END AS validation_status
FROM public.bookmarks AS target
LEFT JOIN public.profiles AS p ON target.username = p.username;

-- 2.9 Table: user_analytics
SELECT 
    'user_analytics' AS table_name,
    COUNT(*) AS total_rows,
    COUNT(user_id) AS migrated_rows,
    SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS unmigrated_matching_profiles,
    SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS orphan_rows,
    SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) AS fk_mismatches,
    CASE 
        WHEN SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) = 0 
         AND SUM(CASE WHEN target.user_id IS NOT NULL AND target.user_id <> p.id THEN 1 ELSE 0 END) = 0 
        THEN 'PASSED' 
        ELSE 'FAILED' 
    END AS validation_status
FROM public.user_analytics AS target
LEFT JOIN public.profiles AS p ON target.username = p.username;


-- -----------------------------------------------------------------------------
-- SECTION 3: MASTER SYSTEM-WIDE AUDIT REPORT QUERY
-- Single consolidated query returning full validation status across all tables
-- -----------------------------------------------------------------------------
WITH summary_data AS (
    SELECT 'users_progress' AS table_name, COUNT(*) AS total_rows, COUNT(user_id) AS migrated_rows, SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS unmigrated_matching, SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) AS orphans FROM public.users_progress
    UNION ALL
    SELECT 'user_xp', COUNT(*), COUNT(user_id), SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END), SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) FROM public.user_xp
    UNION ALL
    SELECT 'users_weakness', COUNT(*), COUNT(user_id), SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END), SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) FROM public.users_weakness
    UNION ALL
    SELECT 'user_revisions', COUNT(*), COUNT(user_id), SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END), SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) FROM public.user_revisions
    UNION ALL
    SELECT 'user_streaks', COUNT(*), COUNT(user_id), SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END), SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) FROM public.user_streaks
    UNION ALL
    SELECT 'daily_missions', COUNT(*), COUNT(user_id), SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END), SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) FROM public.daily_missions
    UNION ALL
    SELECT 'mentor_memory', COUNT(*), COUNT(user_id), SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END), SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) FROM public.mentor_memory
    UNION ALL
    SELECT 'bookmarks', COUNT(*), COUNT(user_id), SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END), SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) FROM public.bookmarks
    UNION ALL
    SELECT 'user_analytics', COUNT(*), COUNT(user_id), SUM(CASE WHEN user_id IS NULL AND username IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END), SUM(CASE WHEN user_id IS NULL AND username NOT IN (SELECT username FROM public.profiles) THEN 1 ELSE 0 END) FROM public.user_analytics
)
SELECT 
    table_name,
    total_rows,
    migrated_rows,
    unmigrated_matching AS unmigrated_matching_profiles,
    orphans AS orphan_rows,
    CASE 
        WHEN unmigrated_matching = 0 THEN 'PASSED ✅' 
        ELSE 'ACTION REQUIRED ❌' 
    END AS status
FROM summary_data
ORDER BY table_name;
