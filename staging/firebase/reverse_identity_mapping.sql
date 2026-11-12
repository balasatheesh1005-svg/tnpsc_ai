-- Review-only reverse migration for nova-ai-staging (fcuykyzgmnwoevmvibbu).
-- Applies only after the forward Firebase migration has been committed.
-- Before rehearsal: export the staging schema, exact ACLs and private links to
-- protected storage; verify the backup and preserve the link audit records.
-- Before actual rollback: disable preview Google Login, remove staging Firebase
-- trust, and verify that previously issued Firebase JWTs are denied at the API.
-- Use a single connection and stop on any SQL error. Confirm the project ref
-- out of band; the catalog guards do not identify a hosted project.
BEGIN;
SET LOCAL lock_timeout = '5s';
SET LOCAL search_path = pg_catalog;

DO $$
DECLARE
    policy record;
    owner_column text;
    installed_expression text;
    previous_expression text;
    clauses text;
BEGIN
    IF to_regclass('nova_firebase_private.identity_links') IS NULL
       OR to_regprocedure('nova_firebase_private.current_profile_id()') IS NULL
       OR to_regprocedure('public.get_linked_firebase_profile_id()') IS NULL
       OR (SELECT count(*) FROM pg_policies WHERE schemaname = 'public') <> 23 THEN
        RAISE EXCEPTION 'Expected installed Firebase migration; refusing rollback';
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
        installed_expression := format('((SELECTnova_firebase_private.current_profile_id())=%I)', owner_column);
        previous_expression := format('(auth.uid() = %I)', owner_column);

        IF NOT EXISTS (
            SELECT 1 FROM pg_policies AS p
            WHERE p.schemaname = 'public' AND p.tablename = policy.table_name
              AND p.policyname = policy.policy_name AND p.cmd = policy.action
              AND p.permissive = 'PERMISSIVE' AND p.roles = ARRAY['authenticated']::name[]
              AND regexp_replace(replace(p.qual, ' AS current_profile_id', ''), '[[:space:]]', '', 'g')
                  IS NOT DISTINCT FROM CASE WHEN policy.action <> 'INSERT' THEN installed_expression END
              AND regexp_replace(replace(p.with_check, ' AS current_profile_id', ''), '[[:space:]]', '', 'g')
                  IS NOT DISTINCT FROM CASE WHEN policy.action <> 'SELECT' THEN installed_expression END
        ) THEN
            RAISE EXCEPTION 'Unexpected installed policy: %', policy.policy_name;
        END IF;

        clauses := CASE WHEN policy.action <> 'INSERT' THEN format(' USING (%s)', previous_expression) ELSE '' END
            || CASE WHEN policy.action <> 'SELECT' THEN format(' WITH CHECK (%s)', previous_expression) ELSE '' END;
        EXECUTE format('ALTER POLICY %I ON public.%I%s', policy.policy_name, policy.table_name, clauses);
    END LOOP;
END;
$$;

-- Restore the staging catalog definition and grants. CREATE OR REPLACE
-- retains the function owner. The signup function and trigger are untouched.
CREATE OR REPLACE FUNCTION public.get_global_leaderboard()
 RETURNS TABLE(username text, accuracy numeric)
 LANGUAGE sql
 STABLE SECURITY DEFINER
 SET search_path TO 'public', 'pg_temp'
AS $function$
    SELECT
        up.username,
        ROUND(AVG(up.accuracy)::numeric, 2) AS accuracy
    FROM public.users_progress AS up
    WHERE auth.uid() IS NOT NULL AND up.username IS NOT NULL
      AND up.username <> ''
    GROUP BY up.username
    ORDER BY accuracy DESC
    LIMIT 10;
$function$
;
REVOKE ALL ON FUNCTION public.get_global_leaderboard() FROM PUBLIC, anon, authenticated, service_role;
GRANT EXECUTE ON FUNCTION public.get_global_leaderboard() TO authenticated, service_role;

-- RESTRICT makes unexpected dependencies abort the whole transaction.
DROP FUNCTION public.get_linked_firebase_profile_id() RESTRICT;
DROP FUNCTION nova_firebase_private.current_profile_id() RESTRICT;
DROP TABLE nova_firebase_private.identity_links RESTRICT;
DROP SCHEMA nova_firebase_private RESTRICT;

-- Rehearsal: compare the resulting catalog to the captured baseline before
-- ending the transaction. Verify policy names/commands/roles/USING/WITH CHECK,
-- RLS flags, function owner/body/ACL and signup trigger. Use a disposable
-- database to test the committed forward/reverse pair and Data API.
-- With two isolated test users and publishable key + user tokens, verify own
-- UUID/read/write and deny cross-user reads/writes. Test Email/Password,
-- signup trigger, Remember Me, reset and leaderboard before/after each
-- migration. With Firebase trust enabled only after the forward migration,
-- test linked Google sign-in, unlinked denial, and session isolation.
-- After reverse, recheck legacy auth and denial of previously issued Firebase
-- tokens. Only an explicitly approved execution copy may end in COMMIT.
ROLLBACK;
