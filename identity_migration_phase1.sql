-- =============================================================================
-- TNPSC Nova AI — Identity Migration v1.0
-- PHASE 1: Database Schema Preparation (SQL Script)
-- =============================================================================
-- Purpose: Add nullable user_id UUID columns and FK references to profiles(id)
--          across all user-related tables without breaking existing username logic.
-- Execution Mode: Idempotent / Safe / Non-blocking DDL
-- Author: Lead Database Architect, TNPSC Nova AI
-- Date: July 23, 2026
-- =============================================================================

BEGIN;

-- -----------------------------------------------------------------------------
-- 1. Table: public.profiles
-- Ensure profiles table has proper UUID primary key referencing auth.users(id)
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS public.profiles (
    id UUID PRIMARY KEY REFERENCES auth.users(id) ON DELETE CASCADE,
    username TEXT UNIQUE NOT NULL,
    email TEXT UNIQUE NOT NULL,
    full_name TEXT,
    avatar_url TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_profiles_username ON public.profiles(username);
CREATE INDEX IF NOT EXISTS idx_profiles_email ON public.profiles(email);

-- -----------------------------------------------------------------------------
-- 2. Table: public.users_progress
-- -----------------------------------------------------------------------------
ALTER TABLE public.users_progress 
    ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;

CREATE INDEX IF NOT EXISTS idx_users_progress_user_id ON public.users_progress(user_id);
CREATE INDEX IF NOT EXISTS idx_users_progress_username ON public.users_progress(username);

-- -----------------------------------------------------------------------------
-- 3. Table: public.user_xp
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS public.user_xp (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    username TEXT UNIQUE NOT NULL,
    xp INTEGER NOT NULL DEFAULT 0,
    level INTEGER NOT NULL DEFAULT 1,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

ALTER TABLE public.user_xp 
    ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;

CREATE INDEX IF NOT EXISTS idx_user_xp_user_id ON public.user_xp(user_id);
CREATE INDEX IF NOT EXISTS idx_user_xp_username ON public.user_xp(username);

-- -----------------------------------------------------------------------------
-- 4. Table: public.users_weakness
-- -----------------------------------------------------------------------------
ALTER TABLE public.users_weakness 
    ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;

CREATE INDEX IF NOT EXISTS idx_users_weakness_user_id ON public.users_weakness(user_id);
CREATE INDEX IF NOT EXISTS idx_users_weakness_username ON public.users_weakness(username);

-- -----------------------------------------------------------------------------
-- 5. Table: public.user_revisions
-- -----------------------------------------------------------------------------
ALTER TABLE public.user_revisions 
    ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;

CREATE INDEX IF NOT EXISTS idx_user_revisions_user_id ON public.user_revisions(user_id);
CREATE INDEX IF NOT EXISTS idx_user_revisions_username ON public.user_revisions(username);

-- -----------------------------------------------------------------------------
-- 6. Table: public.user_streaks
-- -----------------------------------------------------------------------------
ALTER TABLE public.user_streaks 
    ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;

CREATE INDEX IF NOT EXISTS idx_user_streaks_user_id ON public.user_streaks(user_id);
CREATE INDEX IF NOT EXISTS idx_user_streaks_username ON public.user_streaks(username);

-- -----------------------------------------------------------------------------
-- 7. Table: public.daily_missions
-- -----------------------------------------------------------------------------
ALTER TABLE public.daily_missions 
    ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;

CREATE INDEX IF NOT EXISTS idx_daily_missions_user_id ON public.daily_missions(user_id);
CREATE INDEX IF NOT EXISTS idx_daily_missions_username ON public.daily_missions(username);

-- -----------------------------------------------------------------------------
-- 8. Table: public.mentor_memory
-- -----------------------------------------------------------------------------
ALTER TABLE public.mentor_memory 
    ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;

CREATE INDEX IF NOT EXISTS idx_mentor_memory_user_id ON public.mentor_memory(user_id);
CREATE INDEX IF NOT EXISTS idx_mentor_memory_username ON public.mentor_memory(username);

-- -----------------------------------------------------------------------------
-- 9. Table: public.bookmarks
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS public.bookmarks (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    question_id TEXT NOT NULL,
    topic TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

ALTER TABLE public.bookmarks 
    ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;

CREATE INDEX IF NOT EXISTS idx_bookmarks_user_id ON public.bookmarks(user_id);
CREATE INDEX IF NOT EXISTS idx_bookmarks_username ON public.bookmarks(username);

-- -----------------------------------------------------------------------------
-- 10. Table: public.user_analytics
-- -----------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS public.user_analytics (
    id BIGINT GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
    username TEXT NOT NULL,
    action TEXT NOT NULL,
    payload JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

ALTER TABLE public.user_analytics 
    ADD COLUMN IF NOT EXISTS user_id UUID REFERENCES public.profiles(id) ON DELETE CASCADE;

CREATE INDEX IF NOT EXISTS idx_user_analytics_user_id ON public.user_analytics(user_id);
CREATE INDEX IF NOT EXISTS idx_user_analytics_username ON public.user_analytics(username);

COMMIT;

-- =============================================================================
-- POST-MIGRATION VERIFICATION SCRIPT (Run to verify schema setup)
-- =============================================================================
SELECT 
    table_name, 
    column_name, 
    data_type, 
    is_nullable 
FROM 
    information_schema.columns 
WHERE 
    table_schema = 'public' 
    AND column_name = 'user_id'
ORDER BY 
    table_name;
