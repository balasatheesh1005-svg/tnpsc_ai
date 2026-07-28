-- =============================================================================
-- TNPSC Nova AI — Identity Migration v1.0
-- PHASE 2: Data Backfill (SQL Script)
-- =============================================================================
-- Purpose: Safely populate user_id UUID columns across all user-related tables
--          by mapping username to public.profiles.id.
-- Scope: Data backfill ONLY. No DDL alterations, no Python changes, no RLS, no auth changes.
-- Execution Mode: Transactional, Idempotent, Non-blocking
-- Author: Lead Database Architect, TNPSC Nova AI
-- Date: July 25, 2026
-- =============================================================================

BEGIN;

-- -----------------------------------------------------------------------------
-- 0. PRE-FLIGHT AUDIT: Validate profiles table integrity
-- -----------------------------------------------------------------------------
-- Verify profiles table exists and has zero duplicate usernames or NULL values.
DO $$
DECLARE
    null_username_count INTEGER;
    duplicate_username_count INTEGER;
    total_profiles_count INTEGER;
BEGIN
    SELECT COUNT(*) INTO null_username_count 
    FROM public.profiles 
    WHERE username IS NULL;

    SELECT COUNT(*) - COUNT(DISTINCT username) INTO duplicate_username_count 
    FROM public.profiles 
    WHERE username IS NOT NULL;

    SELECT COUNT(*) INTO total_profiles_count 
    FROM public.profiles;

    IF null_username_count > 0 THEN
        RAISE EXCEPTION 'Pre-flight check failed: Found % NULL usernames in public.profiles', null_username_count;
    END IF;

    IF duplicate_username_count > 0 THEN
        RAISE EXCEPTION 'Pre-flight check failed: Found % duplicate usernames in public.profiles', duplicate_username_count;
    END IF;

    RAISE NOTICE 'Pre-flight check passed. Total active profiles: %', total_profiles_count;
END $$;

-- -----------------------------------------------------------------------------
-- 1. Table: public.users_progress
-- Backfill user_id where username matches profiles.username and user_id IS NULL
-- -----------------------------------------------------------------------------
UPDATE public.users_progress AS target
SET user_id = p.id
FROM public.profiles AS p
WHERE target.username = p.username
  AND target.user_id IS NULL;

-- -----------------------------------------------------------------------------
-- 2. Table: public.user_xp
-- Backfill user_id where username matches profiles.username and user_id IS NULL
-- -----------------------------------------------------------------------------
UPDATE public.user_xp AS target
SET user_id = p.id
FROM public.profiles AS p
WHERE target.username = p.username
  AND target.user_id IS NULL;

-- -----------------------------------------------------------------------------
-- 3. Table: public.users_weakness
-- Backfill user_id where username matches profiles.username and user_id IS NULL
-- -----------------------------------------------------------------------------
UPDATE public.users_weakness AS target
SET user_id = p.id
FROM public.profiles AS p
WHERE target.username = p.username
  AND target.user_id IS NULL;

-- -----------------------------------------------------------------------------
-- 4. Table: public.user_revisions
-- Backfill user_id where username matches profiles.username and user_id IS NULL
-- -----------------------------------------------------------------------------
UPDATE public.user_revisions AS target
SET user_id = p.id
FROM public.profiles AS p
WHERE target.username = p.username
  AND target.user_id IS NULL;

-- -----------------------------------------------------------------------------
-- 5. Table: public.user_streaks
-- Backfill user_id where username matches profiles.username and user_id IS NULL
-- -----------------------------------------------------------------------------
UPDATE public.user_streaks AS target
SET user_id = p.id
FROM public.profiles AS p
WHERE target.username = p.username
  AND target.user_id IS NULL;

-- -----------------------------------------------------------------------------
-- 6. Table: public.daily_missions
-- Backfill user_id where username matches profiles.username and user_id IS NULL
-- -----------------------------------------------------------------------------
UPDATE public.daily_missions AS target
SET user_id = p.id
FROM public.profiles AS p
WHERE target.username = p.username
  AND target.user_id IS NULL;

-- -----------------------------------------------------------------------------
-- 7. Table: public.mentor_memory
-- Backfill user_id where username matches profiles.username and user_id IS NULL
-- -----------------------------------------------------------------------------
UPDATE public.mentor_memory AS target
SET user_id = p.id
FROM public.profiles AS p
WHERE target.username = p.username
  AND target.user_id IS NULL;

-- -----------------------------------------------------------------------------
-- 8. Table: public.bookmarks
-- Backfill user_id where username matches profiles.username and user_id IS NULL
-- -----------------------------------------------------------------------------
UPDATE public.bookmarks AS target
SET user_id = p.id
FROM public.profiles AS p
WHERE target.username = p.username
  AND target.user_id IS NULL;

-- -----------------------------------------------------------------------------
-- 9. Table: public.user_analytics
-- Backfill user_id where username matches profiles.username and user_id IS NULL
-- -----------------------------------------------------------------------------
UPDATE public.user_analytics AS target
SET user_id = p.id
FROM public.profiles AS p
WHERE target.username = p.username
  AND target.user_id IS NULL;

COMMIT;

-- =============================================================================
-- POST-MIGRATION EXECUTION SUMMARY QUERY
-- Run this query to view backfill results across all user-related tables.
-- =============================================================================
SELECT 
    'users_progress' AS table_name,
    COUNT(*) AS total_rows,
    COUNT(user_id) AS migrated_rows,
    COUNT(*) - COUNT(user_id) AS unmigrated_or_orphan_rows
FROM public.users_progress
UNION ALL
SELECT 
    'user_xp',
    COUNT(*),
    COUNT(user_id),
    COUNT(*) - COUNT(user_id)
FROM public.user_xp
UNION ALL
SELECT 
    'users_weakness',
    COUNT(*),
    COUNT(user_id),
    COUNT(*) - COUNT(user_id)
FROM public.users_weakness
UNION ALL
SELECT 
    'user_revisions',
    COUNT(*),
    COUNT(user_id),
    COUNT(*) - COUNT(user_id)
FROM public.user_revisions
UNION ALL
SELECT 
    'user_streaks',
    COUNT(*),
    COUNT(user_id),
    COUNT(*) - COUNT(user_id)
FROM public.user_streaks
UNION ALL
SELECT 
    'daily_missions',
    COUNT(*),
    COUNT(user_id),
    COUNT(*) - COUNT(user_id)
FROM public.daily_missions
UNION ALL
SELECT 
    'mentor_memory',
    COUNT(*),
    COUNT(user_id),
    COUNT(*) - COUNT(user_id)
FROM public.mentor_memory
UNION ALL
SELECT 
    'bookmarks',
    COUNT(*),
    COUNT(user_id),
    COUNT(*) - COUNT(user_id)
FROM public.bookmarks
UNION ALL
SELECT 
    'user_analytics',
    COUNT(*),
    COUNT(user_id),
    COUNT(*) - COUNT(user_id)
FROM public.user_analytics
ORDER BY table_name;
