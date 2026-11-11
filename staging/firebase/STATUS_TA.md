# Firebase Google Login — Feature branch நிலை

Firebase Test Project, Google provider, Web App மற்றும் authorized domain அமைக்கப்பட்டதாகத் திட்ட உரிமையாளர் தெரிவித்துள்ளார். தற்போதைய Streamlit deployment மற்றும் இரு Supabase சூழல்களிலும் மாற்றங்கள் செய்யப்படவில்லை.

## அடையாள இணைப்பு

ஆரம்ப staging சோதனைக்கு ஏற்கெனவே உள்ள staging profile UUID-ஐத் தனிப்பட்ட schema-வில் Firebase UID உடன் இணைக்கும் முறையைத் தேர்வு செய்துள்ளோம். நிர்வாகி இரு கணக்குகளின் உரிமையையும் சரிபார்த்த பிறகே இணைப்பைப் பதிவு செய்ய வேண்டும். மின்னஞ்சலை வைத்து தானாக இணைப்பதும், புதிய profile உருவாக்குவதும் இந்தக் கட்டத்தில் கிடையாது. தற்போதைய profile மற்றும் முன்னேற்ற UUID-கள் தொடரும். இந்த முறை DESIGN_TA.md-ல் உள்ள புதிய canonical user அட்டவணை யோசனைக்கு முன் சோதிக்க வேண்டிய குறுகிய staging வழி.

`prepare_identity_mapping.sql` staging snapshot-ல் உள்ள 23 கொள்கைகளின் பெயர், operation, role மற்றும் owner checks ஆகியவற்றைச் சரிபார்க்கிறது. Firebase பயனருக்கு mapping கிடைத்தால் மட்டுமே அதே owner check செயல்படும். SQL கோப்பு ROLLBACK-ல் முடிகிறது. Hosted PostgreSQL-ல் இயக்கப்படவில்லை. Bookmarks, analytics மற்றும் Username Login சிக்கல்கள் இந்த மாற்றத்தின் வரம்பில் தீர்க்கப்படவில்லை.

`bind_firebase_profile()` சரிபார்க்கப்பட்ட Firebase token-ஐ தனி Supabase SDK client-ன் PostgREST bearer ஆகப் பயன்படுத்துகிறது. Staging URL pin, publishable/anon configuration, mapping RPC, RLS வழியாகப் பார்க்கக்கூடிய ஒரே UUID ஆகியவை தேவை. Streamlit அமர்வை `core/firebase_session.py` உருவாக்குகிறது.

## Deployment முன் நிலுவை

- மாற்றமில்லாத தற்போதைய test app-இலிருந்து தனியாக ஒரு preview deployment பயன்படுத்த வேண்டும். அதற்கான hostname-ஐ Firebase Authorized Domains-ல் சேர்க்க வேண்டும்.
- Browser popup, callback, expiry மற்றும் Logout ஆகியவற்றை desktop/mobile-ல் நேரடியாகச் சோதிக்க வேண்டும். உடனடி Firebase revocation சரிபார்ப்பு இன்னும் சேர்க்கப்படவில்லை.
- Test Supabase Third-Party Auth trust, Firebase Admin வழியாக authenticated claim வழங்குதல், rollback SQL சரிபார்ப்பு மற்றும் உண்மையான இரு synthetic test identities-ன் RLS சோதனை தேவை.
- Email/Password மற்றும் Password Reset உள்ளிட்ட browser regression சோதனைகள் நிலுவை.

## Google Login UI

Feature preview-ல் Google account chooser, நினைவகத்தில் மட்டும் Firebase browser auth, ஐந்து நிமிட ஒருமுறை nonce, தனி server client மற்றும் JWT expiry சோதனை சேர்க்கப்பட்டுள்ளன. Google token URL, browser storage, Remember Me அல்லது Supabase Auth session-க்கு எழுதப்படாது. Firebase browser sign-out token callback-க்கு முன்பே நடக்கும். App Logout server state/client-ஐ அகற்றும். இது வழங்கப்பட்ட JWT-ஐ Firebase-ல் உடனடியாக revoke செய்யாது. Expiry அடுத்த app rerun-ல் அமலாகும். Hosted browser மற்றும் live RLS இன்னும் சோதிக்கப்படவில்லை.

தனி preview அமைக்கும் நேரத்தில் மட்டும் Streamlit Secrets-ல் `[firebase_google]` பிரிவில் `enabled = true`, `web_api_key`, `web_app_id` வழங்கவும். தற்போதைய staging URL-க்கு இந்த பொத்தான் இயக்கப்படாது. Firebase Authentication → Settings → Authorized domains-ல் preview hostname சேர்க்கவும். Firebase Project settings → Your apps-ல் Web configuration கிடைக்கும். Private key தேவையில்லை.

Test Supabase-ல் SQL-ஐ முதலில் rollback முறையில் சரிபார்க்கவும். பின்னர் தனி ஒப்புதலுடன் SQL-ஐ நிறுவிய பிறகே Authentication → Third-Party Auth-ல் `tnpsc-nova-ai-auth-test` சேர்க்கவும். அங்கீகரிக்கப்பட்ட Firebase நிர்வாகி சோதனைப் பயனருக்கு `role: authenticated` custom claim சேர்த்து, ஏற்கெனவே உள்ள claims-ஐப் பாதுகாக்க வேண்டும். சோதனைப் பயனர் புதிதாக உள்நுழைந்து புதிய token பெற வேண்டும்.

ஒவ்வொரு இணைப்புக்கும் ஒரே நபர் Google கணக்கிலும் பழைய staging Email/Password கணக்கிலும் புதிதாக உள்நுழைந்து கட்டுப்பாட்டை நிரூபிக்க வேண்டும். நிர்வாகி அந்த அமர்வுகளில் இருந்து Firebase UID மற்றும் Supabase UUID-ஐச் சரிபார்த்து, இரு நேரங்களையும் ஆய்வுப் பதிவின் குறியீட்டையும் private mapping-ல் பதிவு செய்ய வேண்டும். SQL அந்தப் பதிவுகள் கட்டாயம் எனச் சரிபார்க்கிறது. உரிமை நிரூபிப்பை நிர்வாகியே சரிபார்க்க வேண்டும். மின்னஞ்சல் பொருத்தம் மற்றும் பயனர் தட்டச்சு செய்த ID மட்டும் போதாது.
