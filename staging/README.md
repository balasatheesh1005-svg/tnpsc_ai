# TNPSC Nova AI — தனிமைப்படுத்தப்பட்ட சோதனைச் சூழல்

இந்த branch `fix/p0-auth-isolation`-ன் `0f581ff` commit-இலிருந்து உருவாக்கப்பட்டது. Production மற்றும் PR #1 branch-களை மாற்ற வேண்டாம். App entrypoint: `app.py`. இரண்டு கணக்குகள் மட்டுமே அனுமதிக்கும் கட்டுப்பாடு இல்லை.

## தற்போதைய நிலை

- Staging code, read-only metadata ஆய்வு SQL, schema-only அமைப்பு SQL மற்றும் rollback சோதனை SQL தயாரிக்கப்பட்டுள்ளன.
- Supabase இணைப்பு உறுதிப்படுத்தப்பட்டது. தற்போதைய organization-ல் `nova-ai-staging` உருவாக்கப்பட்டது. உருவாக்குவதற்கு முன் பெறப்பட்ட quotation: மாதத்திற்கு $0 (₹0). Paid addon அல்லது upgrade தேர்ந்தெடுக்கப்படவில்லை. Streamlit உள்நுழைவு இன்னும் நிலுவை.
- Production system catalogs-ஐ READ ONLY transaction-ல் ஆய்வு செய்து 10 tables, 23 policies, தேவையான 2 functions மற்றும் 1 trigger புதிய Test Project-ல் அமைக்கப்பட்டன. Production table rows அல்லது auth users வாசிக்கப்படவோ நகலெடுக்கப்படவோ இல்லை.
- Test App deploy செய்யப்படவில்லை. இங்குள்ள URL எடுத்துக்காட்டுகள் செயல்படும் deployment இணைப்புகள் அல்ல.

## Project உருவாக்கமும் schema ஆய்வும்

1. Supabase-ல் தனியான `tnpsc-nova-ai-p0-test` project உருவாக்கவும். தேர்ந்தெடுத்த organization-ல் கட்டணம்/upgrade தேவைப்பட்டால் நிறுத்தி உரிமையாளரின் அனுமதி பெறவும். Free quota கிடைப்பதாக ஊகிக்க வேண்டாம்.
2. Production-ல் `production_catalog_readonly.sql`-ஐ வாசிப்பு அனுமதியுடன் மட்டும் இயக்கவும். இது system catalogs-இல் table/column/constraint/index, function, trigger, RLS, grant மற்றும் enum/extension விவரங்களை மட்டும் வாசிக்கிறது. Auth/users அல்லது app பயனர் பதிவுகளை வாசிப்பதில்லை.
3. Function definitions-ல் credentials இருக்கலாம். ஆய்வு முடிவுகளைப் பொதுவான GitHub branch, logs அல்லது உரையாடலில் வெளியிட வேண்டாம். Functions-ன் dependencies, SECURITY DEFINER/search_path மற்றும் grants-ஐ ஆய்வு செய்யவும்.
4. App பயன்படுத்தும் public objects மற்றும் அவற்றின் dependencies மட்டும் புதிய Test Project-க்கு எடுத்துச் செல்லவும். Supabase-managed auth/storage/internal schemas, Auth users, table rows, production backups, Vault secrets, FDW இணைப்புகள், cron jobs, webhooks ஆகியவற்றை நகலெடுக்க வேண்டாம். Auth user-created trigger-ன் தேவையான public function/custom trigger மட்டும் புதிய auth.users-க்கு பொருத்தவும்.
5. Production URL/key அல்லது external production services-ஐ அழைக்கும் function/trigger இருப்பின் நகலெடுப்பதை நிறுத்தி தனியாக மாற்றத்தை ஆய்வு செய்யவும். இப்போதைய SQL ஒரு inventory மட்டுமே; இயங்கத் தயாரான clone migration அல்ல.
6. RLS இருப்பது மட்டுமே போதாது. Permissive policies, owner checks, INSERT/UPDATE WITH CHECK, table/sequence/function grants, மற்றும் public profile lookup தேவையை ஆய்வு செய்யவும். App-க்கு தேவையான SELECT/INSERT/UPDATE/DELETE-ஐ Test Project-ல் சரிபார்க்கவும்.

## Test App Secrets

- `secrets.example.toml` ஒரு placeholder template மட்டுமே. புதிய Streamlit Test App-ன் Advanced settings → Secrets பகுதியில் உண்மையான Test Project மதிப்புகளை வைக்கவும். Production App Secrets-ஐத் தொட வேண்டாம்.
- `staging.mode = "staging"`, `staging.expected_project_ref`, `staging.app_url`, `supabase.url`, `supabase.publishable_key` அனைத்தும் தேவை.
- Project URL துல்லியமாக `https://<TEST_REF>.supabase.co` வடிவில் இருக்க வேண்டும். Project ref 20 சிறிய எழுத்துகள்/எண்கள். Key புதிய project-ன் publishable key அல்லது anon JWT ஆக மட்டுமே இருக்க வேண்டும். Service-role/secret key பயன்படுத்த வேண்டாம்.
- App URL துல்லியமான HTTPS Community Cloud root URL ஆக இருக்க வேண்டும்; hostname-ல் `test` தனி hyphen label தேவை. Path, query, fragment, username/password, trailing slash அனுமதிக்கப்படுவதில்லை.
- Production project identifier fingerprint தடுப்பில் உள்ளது; production URL-ஐ தவறாகக் கொடுத்தாலும் staging இயங்காது. Missing/invalid Secrets-க்கு fallback இல்லை; App நிறுத்தப்படும்.
- Opaque publishable key-ன் project உரிமையை வடிவச் சோதனை மட்டும் நிரூபிக்காது. Dashboard-ல் project/ref மற்றும் key இணையை உறுதிப்படுத்தவும். Secrets மாற்றினால் Test App-ஐ மறுதொடக்கம் செய்யவும்.
- Runtime production config மற்றும் பழைய production diagnostic notebook staging-இலிருந்து அகற்றப்பட்டுள்ளன. Git வரலாறு மாற்றப்படவில்லை.

## Password Reset / Email Confirmation

1. புதிய Test Project-ன் Authentication URL Configuration-ல் Site URL மற்றும் Redirect URLs ஆகியவற்றை **உண்மையில் ஒதுக்கப்பட்ட Test App root URL**-க்கு மட்டும் அமைக்கவும். Production project-ன் settings-ஐ மாற்ற வேண்டாம். Wildcard redirect சேர்க்க வேண்டாம்.
2. அதே URL-ஐ புதிய Test App-ன் `staging.app_url` Secret-ல் வைக்கவும். இந்த code password-reset `redirect_to` மற்றும் signup `email_redirect_to`-வை இதிலிருந்தே எடுக்கிறது; query input-ல் இருந்து எடுக்காது. Redirect இல்லாத legacy fallback இல்லை.
3. Test Project email templates-ல் production URL/hardcoded production project இருப்பதில்லை என்று சரிபார்க்கவும். Recovery இணைப்பிற்கு token_hash recovery callback வழியை முன்னுரிமைப்படுத்தவும்; தற்போதைய legacy fragment callback code-ல் transient URL token அபாயம் மீதமுள்ளது.
4. Email verification/rate limits-ஐ சோதனை வெற்றிக்காக முடக்க வேண்டாம். தனக்குச் சொந்தமான சோதனை inbox-களில் மட்டும் உண்மையான reset email சோதனை செய்யவும். Test account மாற்றங்கள் Test Project-ஐ மட்டுமே பாதிக்க வேண்டும்.

## Deployment முன் தடைச் சோதனைகள்

- புதிய project/ref உறுதியாக இருக்க வேண்டும்; schema migration Test Project-ல் மட்டும் review செய்யப்பட்டிருக்க வேண்டும்.
- RLS/grants, functions/triggers-ன் external side effects, Test App Secrets மற்றும் email redirects ஆகியவற்றின் live ஆய்வு முடிந்திருக்க வேண்டும்.
- புதிய Streamlit App உருவாக்கும்போது இந்த staging branch, `app.py`, சோதித்த Python/requirements பயன்படுத்தவும். பெயர் கிடைப்பதைக் Dashboard-ல் சரிபார்க்கவும்; production deployment-ஐ edit செய்ய வேண்டாம்.
- Remember Me அதிகபட்சம் 7 நாள்; server restart-ல் செல்லாது. JavaScript cookie என்பதால் HttpOnly இல்லை; XSS அபாயம் உள்ளது. இது production security certification அல்ல.
- இந்த prerequisites முடியும் வரை deployment முடிந்ததாகவோ பாதுகாப்பு உறுதிசெய்யப்பட்டதாகவோ குறிப்பிட வேண்டாம்.

## நேரடி சோதனைத் திட்டம் — அனைத்தும் நிலுவை

| சோதனை | எதிர்பார்ப்பு |
|---|---|
| Signup / Login | Test Project-ல் மட்டும் புதிய user/profile; email/username Login சரியாக இயங்க வேண்டும் |
| Remember Me | தேர்வுடன்/இல்லாமல் reload; token URL/cookie-ல் Supabase credential இருக்கக்கூடாது |
| Logout | cookie handle/session நீங்க வேண்டும்; reload-ல் பழைய அமர்வு மீளக்கூடாது |
| Password Reset | புதிய project மின்னஞ்சல் Test App-க்கு வர வேண்டும்; expired/invalid link மறுக்கப்பட வேண்டும் |
| Session Isolation | தனித்த browser contexts A/B-ல் auth/profile/progress கலக்கக்கூடாது; A logout B-ஐ பாதிக்கக்கூடாது |
| RLS | anon மற்றும் வேறொரு test user மூலம் மற்றவரின் owner data CRUD மறுக்கப்பட வேண்டும் |
| Production பிரிப்பு | அனைத்து SDK request destinations-மும் புதிய Test Project; production rows/settings மாறக்கூடாது |

Mock HTTP சோதனைகள் மற்றும் உண்மையான SDK constructor சோதனைகள் live Supabase/browser சோதனைகளுக்கு மாற்றாகாது.


## 2026-11-06 நேரடி database சரிபார்ப்பு

- புதிய Test Project-ல் மட்டுமே synthetic auth users/profile/progress பதிவுகள் உருவாக்கப்பட்டு transaction rollback செய்யப்பட்டது. Profile trigger, owner SELECT/INSERT, cross-owner SELECT/INSERT/UPDATE மறுப்பு, anon profile மறுப்பு, trigger/leaderboard RPC-க்கு anon EXECUTE மறுப்பு மற்றும் TRUNCATE grant இல்லாதது ஆகிய சோதனைகள் வெற்றி.
- Rollback-க்குப் பிறகு தனியான read-only query மூலம் 10 public tables-லும் 0 பதிவுகள், auth.users-ல் 0 பதிவுகள், 10 RLS-enabled tables மற்றும் 23 policies இருப்பது உறுதிப்படுத்தப்பட்டது.
- Production-ன் பயன்படுத்தப்படாத `handle_new_user_profile` function நகலெடுக்கப்படவில்லை. பயன்படுத்தப்படும் profile trigger-க்கு search_path ஏற்கெனவே பாதுகாப்பாக உள்ளது; அதன் நேரடி RPC EXECUTE அனுமதி நீக்கப்பட்டது. Leaderboard aggregate function authenticated பயனருக்கு மட்டும் அனுமதிக்கப்பட்டு auth.uid() guard சேர்க்கப்பட்டது. தேவையற்ற TRUNCATE/REFERENCES/TRIGGER grants நகலெடுக்கப்படவில்லை. இவை Test Project-ல் மட்டும் செய்யப்பட்ட பாதுகாப்பு வேறுபாடுகள்.
- `bookmarks`, `user_analytics`-ல் production போலவே RLS உள்ளது; policy இல்லை. அதனால் client access மறுக்கப்படுகிறது. Feature வேலை செய்கிறது எனக் கருதக்கூடாது. [Policy ஆய்வு வழிகாட்டி](https://supabase.com/docs/guides/database/database-linter?lint=0008_rls_enabled_no_policy).
- Authenticated leaderboard function SECURITY DEFINER ஆக இருப்பதை advisor இன்னும் எச்சரிக்கிறது. இது aggregate leaderboard-க்கு மட்டும், நிலையான query, 10 rows limit, authenticated EXECUTE மற்றும் auth.uid() guard உடன் உள்ளது. [ஆய்வு வழிகாட்டி](https://supabase.com/docs/guides/database/database-linter?lint=0029_authenticated_security_definer_function_executable).
- தற்போதைய profiles RLS pre-login anonymous username lookup-ஐ அனுமதிக்காது. Username Login-ஐ உறுதிப்படுத்தவில்லை; அதை இயங்கச் செய்ய RLS-ஐத் தளர்த்த வேண்டாம். தனியான பாதுகாப்பான username-resolution திருத்தம் தேவைப்படலாம். Email Login, உண்மையான மின்னஞ்சல் Password Reset மற்றும் browser cookie/session சோதனைகள் இன்னும் நிலுவை.
- Schema SQL புதிய public schema காலியாக இல்லாவிட்டால் செயல்படாமல் நிற்கும். Production-ல் இதை இயக்க வேண்டாம். App startup அல்லது CI இதை இயக்குவதில்லை.

இறுதி code சரிபார்ப்பு: `python -m pytest tests/unit -q --tb=short` — **244 வெற்றி**; `python -m pip check` மற்றும் `git diff --check` வெற்றி. SDK timeout/verify deprecation warnings உள்ளன. இவை தனியான browser/Auth API சோதனை முடிவுகள் அல்ல.
