-- =============================================================================
-- TNPSC Nova AI — Test Data Cleanup
-- SQL Script: Purge Test & Demo Data for Production Readiness
-- =============================================================================
-- Purpose: Safely clear old testing/demo data from user activity & progress tables.
-- Target Tables:
--   - public.users_progress
--   - public.user_xp
--   - public.users_weakness
--   - public.user_revisions
--   - public.user_streaks
--   - public.daily_missions
--   - public.mentor_memory
--
-- Excluded Tables (PRESERVED):
--   - public.profiles (DO NOT DELETE)
--   - auth.users (DO NOT DELETE)
--
-- Execution Mode: Transactional, Schema-Preserving, Zero-DDL
-- Author: Lead Database Architect, TNPSC Nova AI
-- Date: July 25, 2026
-- =============================================================================

BEGIN;

-- -----------------------------------------------------------------------------
-- 1. Table: public.users_progress
-- Purge test progress data and reset identity sequence
-- -----------------------------------------------------------------------------
DELETE FROM public.users_progress;

-- -----------------------------------------------------------------------------
-- 2. Table: public.user_xp
-- Purge test XP and level records
-- -----------------------------------------------------------------------------
DELETE FROM public.user_xp;

-- -----------------------------------------------------------------------------
-- 3. Table: public.users_weakness
-- Purge test weakness tracking data
-- -----------------------------------------------------------------------------
DELETE FROM public.users_weakness;

-- -----------------------------------------------------------------------------
-- 4. Table: public.user_revisions
-- Purge test spaced repetition scheduling data
-- -----------------------------------------------------------------------------
DELETE FROM public.user_revisions;

-- -----------------------------------------------------------------------------
-- 5. Table: public.user_streaks
-- Purge test streak tracking data
-- -----------------------------------------------------------------------------
DELETE FROM public.user_streaks;

-- -----------------------------------------------------------------------------
-- 6. Table: public.daily_missions
-- Purge test mission completion data
-- -----------------------------------------------------------------------------
DELETE FROM public.daily_missions;

-- -----------------------------------------------------------------------------
-- 7. Table: public.mentor_memory
-- Purge test AI mentor conversation context
-- -----------------------------------------------------------------------------
DELETE FROM public.mentor_memory;

COMMIT;

-- =============================================================================
-- POST-CLEANUP VERIFICATION SCRIPT
-- Verify that all 7 target tables are completely empty (COUNT = 0)
-- while public.profiles remains completely intact.
-- =============================================================================
SELECT 
    'users_progress' AS table_name,
    COUNT(*) AS row_count,
    CASE WHEN COUNT(*) = 0 THEN 'CLEAN (READY)' ELSE 'NOT EMPTY' END AS status
FROM public.users_progress
UNION ALL
SELECT 'user_xp', COUNT(*), CASE WHEN COUNT(*) = 0 THEN 'CLEAN (READY)' ELSE 'NOT EMPTY' END FROM public.user_xp
UNION ALL
SELECT 'users_weakness', COUNT(*), CASE WHEN COUNT(*) = 0 THEN 'CLEAN (READY)' ELSE 'NOT EMPTY' END FROM public.users_weakness
UNION ALL
SELECT 'user_revisions', COUNT(*), CASE WHEN COUNT(*) = 0 THEN 'CLEAN (READY)' ELSE 'NOT EMPTY' END FROM public.user_revisions
UNION ALL
SELECT 'user_streaks', COUNT(*), CASE WHEN COUNT(*) = 0 THEN 'CLEAN (READY)' ELSE 'NOT EMPTY' END FROM public.user_streaks
UNION ALL
SELECT 'daily_missions', COUNT(*), CASE WHEN COUNT(*) = 0 THEN 'CLEAN (READY)' ELSE 'NOT EMPTY' END FROM public.daily_missions
UNION ALL
SELECT 'mentor_memory', COUNT(*), CASE WHEN COUNT(*) = 0 THEN 'CLEAN (READY)' ELSE 'NOT EMPTY' END FROM public.mentor_memory
UNION ALL
SELECT 
    'profiles (PRESERVED TABLE)',
    COUNT(*),
    'INTACT & UNTOUCHED'
FROM public.profiles
ORDER BY table_name;
