BEGIN;
INSERT INTO auth.users (id, email, aud, role, raw_user_meta_data, created_at, updated_at)
VALUES
 ('00000000-0000-0000-0000-000000000001','staging-a@nova.invalid','authenticated','authenticated','{"username":"staging_a","full_name":"Synthetic A"}',now(),now()),
 ('00000000-0000-0000-0000-000000000002','staging-b@nova.invalid','authenticated','authenticated','{"username":"staging_b","full_name":"Synthetic B"}',now(),now());
DO $$ BEGIN IF (SELECT count(*) FROM public.profiles) <> 2 THEN RAISE EXCEPTION 'Profile trigger failed'; END IF; END $$;
SELECT set_config('request.jwt.claims','{"sub":"00000000-0000-0000-0000-000000000001","role":"authenticated"}',true);
SET LOCAL ROLE authenticated;
DO $$
DECLARE n integer;
BEGIN
 IF (SELECT count(*) FROM public.profiles) <> 1 THEN RAISE EXCEPTION 'Owner profile SELECT failed'; END IF;
 IF (SELECT count(*) FROM public.profiles WHERE username='staging_b') <> 0 THEN RAISE EXCEPTION 'Cross-owner SELECT leaked'; END IF;
 INSERT INTO public.users_progress(username, user_id, subject, topic, accuracy)
 VALUES ('staging_a','00000000-0000-0000-0000-000000000001','test','synthetic',50);
 IF (SELECT count(*) FROM public.users_progress) <> 1 THEN RAISE EXCEPTION 'Owner progress failed'; END IF;
 BEGIN
   INSERT INTO public.users_progress(username,user_id) VALUES ('staging_b','00000000-0000-0000-0000-000000000002');
   RAISE EXCEPTION 'Cross-owner INSERT was allowed';
 EXCEPTION WHEN insufficient_privilege THEN NULL;
 END;
 UPDATE public.profiles SET full_name='forbidden' WHERE username='staging_b';
 GET DIAGNOSTICS n=ROW_COUNT;
 IF n <> 0 THEN RAISE EXCEPTION 'Cross-owner UPDATE was allowed'; END IF;
 BEGIN
   INSERT INTO public.bookmarks(username,user_id,question_id) VALUES ('staging_a','00000000-0000-0000-0000-000000000001','synthetic');
   RAISE EXCEPTION 'Missing bookmark policy did not fail closed';
 EXCEPTION WHEN insufficient_privilege THEN NULL;
 END;
 IF has_table_privilege(current_user,'public.profiles','TRUNCATE') THEN RAISE EXCEPTION 'Unsafe truncate grant'; END IF;
END $$;
SELECT set_config('request.jwt.claims','{"sub":"00000000-0000-0000-0000-000000000002","role":"authenticated"}',true);
DO $$ BEGIN
 IF (SELECT count(*) FROM public.users_progress) <> 0 THEN RAISE EXCEPTION 'User B read A progress'; END IF;
 IF (SELECT count(*) FROM public.profiles) <> 1 THEN RAISE EXCEPTION 'User B own profile failed'; END IF;
END $$;
RESET ROLE;
SELECT set_config('request.jwt.claims','{"role":"anon"}',true);
SET LOCAL ROLE anon;
DO $$ BEGIN
 IF (SELECT count(*) FROM public.profiles) <> 0 THEN RAISE EXCEPTION 'Anon profile read leaked'; END IF;
 IF has_function_privilege(current_user,'public.handle_new_user()','EXECUTE') THEN RAISE EXCEPTION 'Trigger function exposed'; END IF;
 IF has_function_privilege(current_user,'public.get_global_leaderboard()','EXECUTE') THEN RAISE EXCEPTION 'Leaderboard exposed to anon'; END IF;
END $$;
RESET ROLE;
SELECT 'passed' AS isolated_staging_rls_and_trigger_checks, 'all synthetic rows will be rolled back' AS retention;
ROLLBACK;
