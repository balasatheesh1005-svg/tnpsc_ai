-- =============================================================================
-- TNPSC Nova AI — Identity Migration v1.0
-- PHASE 2: Emergency Rollback Script (SQL Script)
-- =============================================================================
-- Purpose: Safely revert Phase 2 data backfill by resetting user_id to NULL
--          across all 9 user-related tables without dropping columns or altering username.
-- Safety Guarantees:
--   - 100% Data Retention: Zero rows deleted.
--   - Zero DDL Alterations: user_id columns, indexes, and FKs remain intact.
--   - Application Continuity: Application continues using username without disruption.
-- Author: Lead Database Architect, TNPSC Nova AI
-- Date: July 25, 2026
-- =============================================================================

BEGIN;

-- -----------------------------------------------------------------------------
-- 1. Table: public.users_progress
-- Reset user_id to NULL
-- -----------------------------------------------------------------------------
UPDATE public.users_progress
SET user_id = NULL
WHERE user_id IS NOT NULL;

-- -----------------------------------------------------------------------------
-- 2. Table: public.user_xp
-- Reset user_id to NULL
-- -----------------------------------------------------------------------------
UPDATE public.user_xp
SET user_id = NULL
WHERE user_id IS NOT NULL;

-- -----------------------------------------------------------------------------
-- 3. Table: public.users_weakness
-- Reset user_id to NULL
-- -----------------------------------------------------------------------------
UPDATE public.users_weakness
SET user_id = NULL
WHERE user_id IS NOT NULL;

-- -----------------------------------------------------------------------------
-- 4. Table: public.user_revisions
-- Reset user_id to NULL
-- -----------------------------------------------------------------------------
UPDATE public.user_revisions
SET user_id = NULL
WHERE user_id IS NOT NULL;

-- -----------------------------------------------------------------------------
-- 5. Table: public.user_streaks
-- Reset user_id to NULL
-- -----------------------------------------------------------------------------
UPDATE public.user_streaks
SET user_id = NULL
WHERE user_id IS NOT NULL;

-- -----------------------------------------------------------------------------
-- 6. Table: public.daily_missions
-- Reset user_id to NULL
-- -----------------------------------------------------------------------------
UPDATE public.daily_missions
SET user_id = NULL
WHERE user_id IS NOT NULL;

-- -----------------------------------------------------------------------------
-- 7. Table: public.mentor_memory
-- Reset user_id to NULL
-- -----------------------------------------------------------------------------
UPDATE public.mentor_memory
SET user_id = NULL
WHERE user_id IS NOT NULL;

-- -----------------------------------------------------------------------------
-- 8. Table: public.bookmarks
-- Reset user_id to NULL
-- -----------------------------------------------------------------------------
UPDATE public.bookmarks
SET user_id = NULL
WHERE user_id IS NOT NULL;

-- -----------------------------------------------------------------------------
-- 9. Table: public.user_analytics
-- Reset user_id to NULL
-- -----------------------------------------------------------------------------
UPDATE public.user_analytics
SET user_id = NULL
WHERE user_id IS NOT NULL;

COMMIT;

-- =============================================================================
-- POST-ROLLBACK VERIFICATION SCRIPT
-- Confirm that all user_id values are reset to NULL while total rows remain intact.
-- =============================================================================
SELECT 
    'users_progress' AS table_name,
    COUNT(*) AS total_rows,
    COUNT(user_id) AS active_user_id_count,
    CASE WHEN COUNT(user_id) = 0 THEN 'ROLLBACK SUCCESSFUL ✅' ELSE 'ROLLBACK INCOMPLETE ❌' END AS status
FROM public.users_progress
UNION ALL
SELECT 'user_xp', COUNT(*), COUNT(user_id), CASE WHEN COUNT(user_id) = 0 THEN 'ROLLBACK SUCCESSFUL ✅' ELSE 'ROLLBACK INCOMPLETE ❌' END FROM public.user_xp
UNION ALL
SELECT 'users_weakness', COUNT(*), COUNT(user_id), CASE WHEN COUNT(user_id) = 0 THEN 'ROLLBACK SUCCESSFUL ✅' ELSE 'ROLLBACK INCOMPLETE ❌' END FROM public.users_weakness
UNION ALL
SELECT 'user_revisions', COUNT(*), COUNT(user_id), CASE WHEN COUNT(user_id) = 0 THEN 'ROLLBACK SUCCESSFUL ✅' ELSE 'ROLLBACK INCOMPLETE ❌' END FROM public.user_revisions
UNION ALL
SELECT 'user_streaks', COUNT(*), COUNT(user_id), CASE WHEN COUNT(user_id) = 0 THEN 'ROLLBACK SUCCESSFUL ✅' ELSE 'ROLLBACK INCOMPLETE ❌' END FROM public.user_streaks
UNION ALL
SELECT 'daily_missions', COUNT(*), COUNT(user_id), CASE WHEN COUNT(user_id) = 0 THEN 'ROLLBACK SUCCESSFUL ✅' ELSE 'ROLLBACK INCOMPLETE ❌' END FROM public.daily_missions
UNION ALL
SELECT 'mentor_memory', COUNT(*), COUNT(user_id), CASE WHEN COUNT(user_id) = 0 THEN 'ROLLBACK SUCCESSFUL ✅' ELSE 'ROLLBACK INCOMPLETE ❌' END FROM public.mentor_memory
UNION ALL
SELECT 'bookmarks', COUNT(*), COUNT(user_id), CASE WHEN COUNT(user_id) = 0 THEN 'ROLLBACK SUCCESSFUL ✅' ELSE 'ROLLBACK INCOMPLETE ❌' END FROM public.bookmarks
UNION ALL
SELECT 'user_analytics', COUNT(*), COUNT(user_id), CASE WHEN COUNT(user_id) = 0 THEN 'ROLLBACK SUCCESSFUL ✅' ELSE 'ROLLBACK INCOMPLETE ❌' END FROM public.user_analytics
ORDER BY table_name;
