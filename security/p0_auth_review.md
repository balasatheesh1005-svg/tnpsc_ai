# P0 பாதுகாப்புத் திருத்தம் — ஆய்வுக் குறிப்பு

## திருத்தங்கள்

- `tnpsc_at`, `tnpsc_rt` URL மதிப்புகள் நீக்கப்படுகின்றன; அவை உள்நுழைவுக்காக ஏற்கப்படுவதில்லை. பழைய bookmark இணைப்பைப் பயன்படுத்துவோர் மீண்டும் உள்நுழைய வேண்டும்.
- ஒவ்வொரு Streamlit அமர்விற்கும் தனி Supabase client. பொதுவான proxy ஒவ்வொரு அழைப்பிலும் தற்போதைய அமர்வின் client-ஐத் தேர்ந்தெடுக்கிறது. Auth மற்றும் database கோரிக்கைகள் அதே client-ஐப் பயன்படுத்துகின்றன.
- SDK பின்னணி refresh மற்றும் SDK persistence முடக்கப்பட்டுள்ளன. காலாவதியாகும் செயலில் உள்ள அமர்வு அடுத்த rerun-ல் புதுப்பிக்கப்படுகிறது. தோல்வியில் அமர்வு நீக்கப்படுகிறது.
- Remember Me தேர்வில் 7 நாள் காலவரையறையுள்ள சீரற்ற cookie அடையாளம் மட்டும் உலாவியில் வைக்கப்படுகிறது. Supabase token-கள் server நினைவகத்தில் மட்டுமே இருக்கும். Logout, தோல்வியுற்ற மீட்பு, காலாவதி ஆகியவை அடையாளத்தைச் செல்லாததாக்குகின்றன.
- சேவையக மறுதொடக்கம் Remember Me-ஐ முடிக்கும். பல worker அமைப்பிற்கு பகிரப்பட்ட பாதுகாப்பான session store தேவை. தற்போதைய செயலாக்கம் ஒரே process அமைப்பிற்கானது.
- Cookie-க்கு Secure மற்றும் SameSite=Strict அமைக்கப்பட்டுள்ளது. JavaScript component பயன்படுத்துவதால் HttpOnly இல்லை; XSS ஏற்பட்டால் opaque cookie-யும் திருடப்படலாம். முழுமையான நீண்டகாலத் தீர்விற்கு HttpOnly cookie வழங்கும் server authentication gateway தேவை. HTTPS அவசியம்.
- Password reset OTP, PKCE மற்றும் பழைய token callback வழிகள் பாதுகாக்கப்பட்டுள்ளன. புதிய callback பழைய recovery நிலையை நீக்குகிறது. ஏற்கனவே உள்ள implicit recovery fragment → query bridge மாற்றப்படவில்லை; callback token-கள் கிடைத்தவுடன் URL நீக்கப்படுகிறது. Inbound query callback-கள் hosting/access logs-ல் செல்லும் அபாயம் மீதமுள்ளது; deployment-ல் token_hash recovery email template-ஐ முன்னுரிமைப்படுத்த வேண்டும். இந்த PR hosting அல்லது email template-ஐ மாற்றவில்லை.

## bookmarks மற்றும் user_analytics RLS தேவைகள்

Repository phase1 SQL-ல் `user_id UUID` உள்ளது; இந்த இரு அட்டவணைகளுக்கும் RLS policies சேர்க்கப்படவில்லை. Production grants இருப்பது மட்டுமே பாதுகாப்பை நிரூபிக்காது.

| செயல்பாடு | authenticated policy தேவை |
|---|---|
| SELECT | USING (`auth.uid() = user_id`) |
| INSERT | WITH CHECK (`auth.uid() = user_id`) |
| UPDATE | USING மற்றும் WITH CHECK இரண்டிலும் (`auth.uid() = user_id`) |
| DELETE | USING (`auth.uid() = user_id`) |

- இரு அட்டவணைகளிலும் RLS இயக்கப்பட்டிருக்க வேண்டும்; anon-க்கு உரிமையாளர் தரவு அனுமதிக்கும் policy இருக்கக்கூடாது.
- ஏற்கனவே `true` அல்லது username அடிப்படையில் அனுமதிக்கும் permissive policy இருந்தால் அதை ஆய்வு செய்து மாற்ற வேண்டும். புதிய owner policy மட்டும் சேர்ப்பது பழைய permissive அனுமதியைத் தடுக்காது.
- NULL `user_id` பதிவுகளை username அடிப்படையில் அனைவருக்கும் திறக்கக்கூடாது. தனியாக ஆய்வு செய்து உரிமையாளரை உறுதிப்படுத்த வேண்டும்.
- `security/p0_rls_audit.sql` வாசிப்பு மட்டுமே செய்யும் ஆய்வு query-கள். இங்கு இயக்கப்படவில்லை. Database மாற்றம் செய்யும் migration திட்டமிட்டு சேர்க்கப்படவில்லை.
- Repository bookmark engine தற்போது local JSON-ஐயும் பயன்படுத்துகிறது; Supabase RLS அதைக் கட்டுப்படுத்தாது. அதன் தனிப் பாதுகாப்பு ஆய்வு இந்த மாற்றத்தின் வரம்பிற்கு வெளியே உள்ளது.

## சரிபார்ப்பு வரம்புகள்

Mock சோதனைகள் நேரடி Supabase பாதுகாப்பை நிரூபிப்பதில்லை. Production secrets, தரவு, policies எதுவும் மாற்றப்படவில்லை. Merge/deploy முன் தனி staging சூழலில் கீழ்கண்டவை இன்னும் அவசியம்:

1. இரண்டு கணக்குகள் மற்றும் anon மூலம் இரு அட்டவணைகளிலும் SELECT/INSERT/UPDATE/DELETE சோதனை; மற்றவரின் user_id-க்கு மாற்ற முயற்சியும் மறுக்கப்பட வேண்டும்.
2. இரண்டு தனி உலாவிகளில் Login, Remember Me உடன்/இல்லாமல் reload, logout, token refresh சோதனை.
3. உண்மையான மின்னஞ்சல் recovery இணைப்பு, காலாவதியான இணைப்பு, OTP/PKCE verifier மற்றும் password update சோதனை.
4. Hosted browser-ல் cookie component செயல்பாடு மற்றும் HTTPS cookie சேமிப்பு சரிபார்ப்பு. இவை முடிந்ததாகக் கருதக்கூடாது.


## SDK initialization திருத்தம் — 2026-11-06

முந்தைய import `supabase.lib.client_options.ClientOptions` அடிப்படை options வகையைத் தேர்ந்தெடுத்தது. Synchronous SDK-க்கு அவசியமான `storage` இதில் இல்லை. பொதுவான `from supabase import ClientOptions` import, சரியான `SyncClientOptions` வகையை வழங்குகிறது. ஒவ்வொரு பயனர் அமர்வுக்கும் புதிதாக options மற்றும் memory storage உருவாகின்றன; `auto_refresh_token=False`, `persist_session=False` அமைப்புகள் தொடர்கின்றன.

`requirements.txt`-ல் `supabase==2.34.0` உறுதிப்படுத்தப்பட்டுள்ளது. இந்த SDK தன் துணைப் பொதிகளையும் அதே பதிப்பில் கோருகிறது. தனியான Work சோதனைச் சூழலில் Python 3.12.14 பயன்படுத்தப்பட்டது; பயனரின் Windows கணினியில் நிறுவப்பட்ட பதிப்புகளை நேரடியாகப் பெறவில்லை.

| நிறுவப்பட்ட பொதி | சரிபார்த்த பதிப்பு |
|---|---|
| supabase | 2.34.0 |
| supabase-auth | 2.34.0 |
| supabase-functions | 2.34.0 |
| postgrest | 2.34.0 |
| storage3 | 2.34.0 |
| realtime | 2.34.0 |
| httpx | 0.28.1 |

- `python -m pip check` வெற்றி. CI-யிலும் dependency பொருத்தமும் SDK பதிப்புகளும் பதிவு செய்யப்படுகின்றன.
- புதிய `test_supabase_sdk.py` உண்மையான SDK constructor, auth state, தனித்த storage, Login, Remember Me மீட்பு, Logout மற்றும் password recovery/update வழிகளைச் சோதிக்கிறது. SDK factory mock செய்யப்படுவதில்லை; HTTP பதில்கள் மட்டும் செயற்கையாக வழங்கப்படுகின்றன. Production URL/key பயன்படுத்தப்படுவதில்லை; unit சோதனைகளில் socket இணைப்புகள் தடுக்கப்படுகின்றன.
- பழைய import-ஐச் சோதனையில் மட்டும் மீண்டும் செலுத்தியபோது புதிய initialization சோதனை அதே `AttributeError: 'ClientOptions' object has no attribute 'storage'` பிழையுடன் தோல்வியடைந்தது. சரியான import-உடன் அது வெற்றியடைந்தது.
- SDK proxy-ஐ ஆய்வு செய்யும் `__func__` போன்ற metadata கோரிக்கைகள் இனி client உருவாக்கத்தைத் தூண்டுவதில்லை.
- SDK-இன் `timeout`/`verify` deprecation warnings உள்ளன; அவை இந்த initialization பிழையல்ல.
- இவை நேரடி Supabase அல்லது browser சோதனைகள் அல்ல. RLS, உண்மையான recovery மின்னஞ்சல், hosted browser cookie ஆகியவற்றின் நிலுவைச் சரிபார்ப்புகள் மேலே உள்ளபடியே தொடர்கின்றன.

இறுதி unit சரிபார்ப்பு: `python -m pytest tests/unit -q --tb=short --durations=5` — **220 சோதனைகள் வெற்றி**. இதில் authentication/SDK தொடர்பான 59 சோதனைகள் அடங்கும். `git diff --check` மற்றும் `python -m pip check` வெற்றி. இது Work சோதனைச் சூழலின் முடிவு; Windows localhost அல்லது நேரடி சேவையின் முடிவல்ல.
