-- READ ONLY: production-இல் தானாக இயக்கப்படவில்லை.
-- RLS enabled மட்டும் போதாது; permissive policies OR மூலம் இணைகின்றன.
SELECT c.relname, c.relrowsecurity, c.relforcerowsecurity
FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'public' AND c.relname IN ('bookmarks', 'user_analytics');
SELECT tablename, policyname, permissive, roles, cmd, qual, with_check
FROM pg_policies WHERE schemaname = 'public'
AND tablename IN ('bookmarks', 'user_analytics');
SELECT table_name, grantee, privilege_type FROM information_schema.role_table_grants
WHERE table_schema = 'public' AND table_name IN ('bookmarks', 'user_analytics');
SELECT 'bookmarks' AS table_name, count(*) FILTER (WHERE user_id IS NULL) AS missing_owner
FROM public.bookmarks
UNION ALL SELECT 'user_analytics', count(*) FILTER (WHERE user_id IS NULL)
FROM public.user_analytics;
