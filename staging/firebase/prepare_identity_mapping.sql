-- Review-only migration for nova-ai-staging. Do not run on Production.
BEGIN;

CREATE SCHEMA nova_firebase_private;
REVOKE ALL ON SCHEMA nova_firebase_private FROM PUBLIC, anon, authenticated;

-- Provision only after independently verifying both accounts. No app/API writes.
CREATE TABLE nova_firebase_private.identity_links (
    firebase_subject text PRIMARY KEY CHECK (length(firebase_subject) BETWEEN 1 AND 128),
    profile_id uuid NOT NULL UNIQUE REFERENCES public.profiles(id) ON DELETE CASCADE
);
ALTER TABLE nova_firebase_private.identity_links ENABLE ROW LEVEL SECURITY;
REVOKE ALL ON nova_firebase_private.identity_links FROM PUBLIC, anon, authenticated;

CREATE FUNCTION nova_firebase_private.current_profile_id()
RETURNS uuid
LANGUAGE plpgsql
STABLE
SECURITY DEFINER
SET search_path = ''
AS $$
DECLARE
    claims jsonb := auth.jwt();
    linked_id uuid;
BEGIN
    IF claims->>'role' IS DISTINCT FROM 'authenticated' THEN
        RETURN NULL;
    END IF;

    IF claims->>'iss' = 'https://fcuykyzgmnwoevmvibbu.supabase.co/auth/v1'
       AND claims->>'aud' = 'authenticated'
       AND claims->>'sub' ~ '^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$' THEN
        RETURN (claims->>'sub')::uuid;
    END IF;

    IF claims->>'iss' = 'https://securetoken.google.com/tnpsc-nova-ai-auth-test'
       AND claims->>'aud' = 'tnpsc-nova-ai-auth-test'
       AND claims->'firebase'->>'sign_in_provider' = 'google.com'
       AND claims->'email_verified' = 'true'::jsonb THEN
        SELECT profile_id INTO linked_id
        FROM nova_firebase_private.identity_links
        WHERE firebase_subject = claims->>'sub';
        RETURN linked_id;
    END IF;

    RETURN NULL;
END;
$$;

REVOKE ALL ON FUNCTION nova_firebase_private.current_profile_id() FROM PUBLIC, anon, authenticated;
GRANT EXECUTE ON FUNCTION nova_firebase_private.current_profile_id() TO authenticated;

DO $$
DECLARE
    policy record;
    old_expression text;
    new_expression text;
    owner_column text;
    clauses text;
BEGIN
    IF (SELECT count(*) FROM pg_catalog.pg_policies WHERE schemaname = 'public') <> 23 THEN
        RAISE EXCEPTION 'Unexpected staging policy count';
    END IF;

    FOR policy IN SELECT * FROM (VALUES
            ('profiles', 'profiles_insert', 'INSERT'),
            ('profiles', 'profiles_update', 'UPDATE'),
            ('profiles', 'profiles_select_own', 'SELECT'),
            ('users_weakness', 'users_weakness_insert_own', 'INSERT'),
            ('users_weakness', 'users_weakness_select_own', 'SELECT'),
            ('users_weakness', 'users_weakness_update_own', 'UPDATE'),
            ('user_streaks', 'user_streaks_insert_own', 'INSERT'),
            ('user_streaks', 'user_streaks_select_own', 'SELECT'),
            ('user_streaks', 'user_streaks_update_own', 'UPDATE'),
            ('users_progress', 'users_progress_insert_own', 'INSERT'),
            ('users_progress', 'users_progress_select_own', 'SELECT'),
            ('user_revisions', 'user_revisions_insert_own', 'INSERT'),
            ('user_revisions', 'user_revisions_select_own', 'SELECT'),
            ('user_revisions', 'user_revisions_update_own', 'UPDATE'),
            ('mentor_memory', 'mentor_memory_insert_own', 'INSERT'),
            ('mentor_memory', 'mentor_memory_select_own', 'SELECT'),
            ('mentor_memory', 'mentor_memory_update_own', 'UPDATE'),
            ('user_xp', 'user_xp_insert_own', 'INSERT'),
            ('user_xp', 'user_xp_select_own', 'SELECT'),
            ('user_xp', 'user_xp_update_own', 'UPDATE'),
            ('daily_missions', 'daily_missions_insert_own', 'INSERT'),
            ('daily_missions', 'daily_missions_select_own', 'SELECT'),
            ('daily_missions', 'daily_missions_update_own', 'UPDATE')
    ) AS expected(table_name, policy_name, action)
    LOOP
        owner_column := CASE WHEN policy.table_name = 'profiles' THEN 'id' ELSE 'user_id' END;
        old_expression := format('(auth.uid() = %I)', owner_column);
        new_expression := format('(SELECT nova_firebase_private.current_profile_id()) = %I', owner_column);

        IF NOT EXISTS (
            SELECT 1 FROM pg_catalog.pg_policies
            WHERE schemaname = 'public' AND tablename = policy.table_name
              AND policyname = policy.policy_name AND cmd = policy.action
              AND permissive = 'PERMISSIVE' AND roles = ARRAY['authenticated']::name[]
              AND qual IS NOT DISTINCT FROM CASE WHEN policy.action <> 'INSERT' THEN old_expression END
              AND with_check IS NOT DISTINCT FROM CASE WHEN policy.action <> 'SELECT' THEN old_expression END
        ) THEN
            RAISE EXCEPTION 'Unexpected policy: %', policy.policy_name;
        END IF;

        clauses := CASE WHEN policy.action <> 'INSERT' THEN format(' USING (%s)', new_expression) ELSE '' END
            || CASE WHEN policy.action <> 'SELECT' THEN format(' WITH CHECK (%s)', new_expression) ELSE '' END;
        EXECUTE format('ALTER POLICY %I ON public.%I%s', policy.policy_name, policy.table_name, clauses);
    END LOOP;
END;
$$;

-- Retain the existing public ranking behavior for authorized profiles only.
CREATE OR REPLACE FUNCTION public.get_global_leaderboard()
RETURNS TABLE(username text, accuracy numeric)
LANGUAGE sql
STABLE SECURITY DEFINER
SET search_path = ''
AS $$
    SELECT up.username, round(avg(up.accuracy)::numeric, 2)
    FROM public.users_progress AS up
    WHERE (SELECT nova_firebase_private.current_profile_id()) IS NOT NULL
      AND up.username IS NOT NULL AND up.username <> ''
    GROUP BY up.username
    ORDER BY 2 DESC
    LIMIT 10;
$$;
REVOKE ALL ON FUNCTION public.get_global_leaderboard() FROM PUBLIC, anon, authenticated;
GRANT EXECUTE ON FUNCTION public.get_global_leaderboard() TO authenticated;

-- This RPC also acts as a fail-closed check that the reviewed migration exists.
CREATE FUNCTION public.get_linked_firebase_profile_id()
RETURNS uuid
LANGUAGE sql
STABLE SECURITY DEFINER
SET search_path = ''
AS $$
    SELECT nova_firebase_private.current_profile_id()
    WHERE auth.jwt()->>'iss' = 'https://securetoken.google.com/tnpsc-nova-ai-auth-test';
$$;
REVOKE ALL ON FUNCTION public.get_linked_firebase_profile_id() FROM PUBLIC, anon, authenticated;
GRANT EXECUTE ON FUNCTION public.get_linked_firebase_profile_id() TO authenticated;

-- Deliberately roll back this review artifact.
ROLLBACK;
