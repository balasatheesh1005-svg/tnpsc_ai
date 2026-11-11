# Firebase Google Login — Staging பாதுகாப்பு வடிவமைப்பு


இந்த ஆவணம் ஆரம்ப வடிவமைப்பைப் பதிவு செய்கிறது. தற்போதைய நிலைக்கு [STATUS_TA.md](STATUS_TA.md) பார்க்கவும்.
## தற்போதைய நிலை

இது `feature/firebase-google-auth-staging` branch-க்கான வடிவமைப்பும் token-validation அடித்தளமும் மட்டுமே. Firebase project உருவாக்கப்படவில்லை; Console இணைப்பு/அனுமதி நிலுவை. Google Login button, browser callback, Supabase trust integration, UUID mapping மற்றும் புதிய RLS helper இன்னும் செயல்படுத்தப்படவில்லை. எந்த schema/RLS மாற்றமும் இயக்கப்படவில்லை. தற்போதைய Supabase Login/Remember Me/Logout மாற்றப்படவில்லை. இந்த branch-ஐ Google Login தயாராகிவிட்டதாக deploy செய்யக்கூடாது.

## உறுதிப்படுத்தப்பட்ட அமைப்பு

- Staging base commit: `6b2d963`; தனி Supabase Test Project: `nova-ai-staging`.
- ஒவ்வொரு Streamlit அமர்விற்கும் தனி Supabase client; URL token persistence இல்லை. Remember Me opaque cookie-யின் Supabase tokens server memory-ல் மட்டுமே உள்ளன. Cookie HttpOnly இல்லை; restart-ல் நினைவில் வைத்த அமர்வு செல்லாது.
- 23 ownership policies `auth.uid()` மூலம் UUID `id`/`user_id`-ஐச் சோதிக்கின்றன. `profiles.id` என்பது `auth.users.id`-ஐச் சார்ந்த UUID. பிற முன்னேற்றத் தரவு `profiles.id`-ஐச் சார்ந்துள்ளது.
- Firebase `sub` text UID-ஐ `auth.uid()` UUID என நேரடியாகப் பயன்படுத்த முடியாது. Firebase token-ஐ தற்போதைய `supabase.auth.set_session()`-க்கு அளிப்பதும் சரியான native third-party integration அல்ல.
- `bookmarks`, `user_analytics` RLS இயங்குகிறது; policies இல்லை என்பதால் client operations மறுக்கப்படுகின்றன. Username Login-ன் pre-login profile lookup-க்கும் தற்போதைய RLS அனுமதி இல்லை. இவற்றை இந்தப் பணியில் தளர்த்தவில்லை.

## தேர்ந்தெடுக்கப்பட்ட ஒருங்கிணைப்பு

| அடுக்கு | பொறுப்பு |
|---|---|
| Firebase Web SDK | Google provider account chooser; OAuth state/redirect கையாளுதல்; ஆரம்பத்தில் in-memory persistence |
| Streamlit callback | Session-bound nonce, ஒருமுறை பயன்படுத்தும் callback, Google ID token server-க்கு component channel வழியாக மட்டும்; URL/cookie/log-ல் token இல்லை |
| Token verifier | Google certificate மூலம் RS256 signature, pinned Firebase project audience/issuer, exp/iat/auth_time, Google provider, verified email, authenticated role |
| Supabase hosted Third-Party Auth | அதே Test Firebase project-ஐ trust செய்ய வேண்டும்; தெரியாத project JWT-களை gateway மறுக்க வேண்டும் |
| Private identity mapping + RLS | `(issuer, subject)` → canonical app UUID; client அனுப்பும் UUID/email மூலம் owner தீர்மானிக்கக்கூடாது |

Firebase SDK Google `signInWithPopup` பயன்படுத்தலாம்; mobile iframe/popup restrictions ஏற்பட்டால் top-level redirect/broker தேவைப்படலாம். இந்த user flow உண்மையான hosted browser-ல் சோதிக்கப்படாதது. Token expiry/refresh component-ல் கையாளப்பட்டு, server மற்றும் Supabase request-களில் மீண்டும் சரிபார்க்கப்பட வேண்டும். Google OAuth token மற்றும் Firebase ID token வெவ்வேறு; இங்கு native integration-க்கு Firebase ID token தேவை.

Supabase third-party auth-க்கு signed `role = authenticated` custom claim தேவை. அதை client அல்லது editable user_metadata-இலிருந்து அமைக்கக்கூடாது. முதல் verified Google sign-in-க்குப் பிறகு server-only Firebase Admin SDK மூலம் நிரந்தர `authenticated` claim மட்டும் ஒதுக்கி, SDK token force-refresh செய்து, அதன் பிறகே strict authorization verifier மற்றும் profile bootstrap இயங்க வேண்டும். இந்த privileged bootstrap இன்னும் எழுதப்படவில்லை. Existing custom claims-ஐ அழிக்கக்கூடாது.

Firebase Cloud Functions / Identity Platform / Blaze billing தானாக இயக்கப்படாது. Admin SDK credentials தேவைப்பட்டால் அவை Test Project-க்கான server Secrets-ல் மட்டும் இருக்க வேண்டும்; browser/component அல்லது GitHub-க்கு செல்லக்கூடாது. Supabase queries-க்கு service-role key பயன்படுத்தக் கூடாது; Firebase bearer + Test publishable key + RLS மட்டுமே.

## UUID-ஐப் பாதுகாக்கும் proposed database மாற்றம் — இன்னும் பயன்படுத்தப்படவில்லை

1. Private schema-வில் canonical `app_users(id UUID)` மற்றும் `external_identities(issuer TEXT, subject TEXT, app_user_id UUID)` உருவாக்க வேண்டும். `(issuer, subject)` unique, linkage immutable; client direct writes இல்லை. RLS/permissions defense-in-depth வேண்டும்.
2. தற்போதைய staging profile UUID-களை அதே UUID-களாக canonical app_users-ல் backfill செய்ய வேண்டும். Progress `user_id`-களை மாற்ற வேண்டாம். Production பதிவுகளை Test Project-க்கு எடுத்துவரக் கூடாது.
3. `profiles.id` foreign key-ஐ `auth.users`-இலிருந்து canonical app_users-க்கு மாற்ற வேண்டும். Supabase Auth user trigger அதே UUID-யில் canonical row மற்றும் profile உருவாக்க வேண்டும்; பழைய Login தொடர வேண்டும்.
4. Firebase profile bootstrap ஒரு குறுகிய, transaction-safe server RPC ஆக இருக்க வேண்டும். Supabase-verified JWT-ன் pinned issuer, audience, subject, Google provider/verified email/role-ஐச் சரிபார்த்து canonical UUID-யை database-ல் உருவாக்க வேண்டும். Client UUID, username அல்லது email mapping தேர்ந்தெடுக்க அனுமதி இல்லை. Existing email collision வந்தால் auto-link செய்யாமல் dual-login linking தேவை என மறுக்க வேண்டும்.
5. `current_app_user_id()` private helper, trusted Supabase issuer + UUID subject-க்கு பழைய app UUID-யையும், pinned Firebase issuer + text subject-க்கு private mapping UUID-யையும் மட்டுமே வழங்க வேண்டும். Firebase UID UUID போலத் தோன்றினாலும் பழைய Supabase UUID-க்கு நேரடியாக cast செய்யக்கூடாது.
6. தற்போதைய ownership policies-ல் UUID resolver மட்டும் மாற்றப்படும்; owner `USING`/`WITH CHECK` சோதனைகள் தொடரும். Trusted issuer/audience restrictive guard இரு வழிகளுக்கும் வேண்டும். Unknown/unlinked/disabled mappings மறுக்கப்பட வேண்டும். SECURITY DEFINER lookup அவசியமானால் private schema, empty search_path, மிகக் குறுகிய privileges, arbitrary lookup arguments இல்லாத வடிவம், anon/PUBLIC EXECUTE மறுப்பு தேவை.
7. `bookmarks`/`user_analytics` புதிய policies மற்றும் username resolution தனிப் பரிசீலனை; Firebase integration காரணமாக பொதுவான SELECT அல்லது `true` policies சேர்க்கக்கூடாது.

## இந்த commit-ல் செயல்படுத்தப்பட்ட வரம்பு

`core/firebase_token_validation.py` Google-ன் `verify_firebase_token` library-ஐ உண்மையாகப் பயன்படுத்துகிறது. Public certificate URL pin, 5-second timeout, RS256/kid கட்டுப்பாடு, untrusted jku/jwk/x5u மறுப்பு, project issuer/audience, Google provider, verified email, authenticated claim, recent auth_time ஆகியவை சோதிக்கப்படுகின்றன. Return value-ல் raw token இல்லை; token logs இல்லை. இது Streamlit authenticated state-ஐ உருவாக்குவதில்லை; Supabase RLS-ஐ மாற்றுவதில்லை.

Public-certificate validation மட்டும் online revocation அல்லது disabled-user நிலையை நிரூபிக்காது. முழு login bootstrap-க்கு Firebase Admin SDK check_revoked/disabled check அல்லது சமமான session validation தேவை. Logout-ல் browser Firebase signOut + server token/client/cache cleanup இரண்டும் வேண்டும். Issued JWT expiry வரை செல்லுபடியாகலாம்; local logout-ஐ global revocation எனக் குறிப்பிடக்கூடாது.

## செயல்படுத்துவதற்கு முன் தேவை

- Firebase இணைப்பு/Console உள்நுழைவு; தனி Test Project, plan/billing சரிபார்ப்பு; ஏதேனும் nonzero charge இருந்தால் user அனுமதி.
- Google provider enable, authorized domains/actual Test App URL, Google consent/support-email மற்றும் callback flow ஆய்வு.
- Test Supabase-ல் Firebase trust integration உறுதி; provider IDs/credentials Secrets-ல் மட்டும்.
- மேலுள்ள database மாற்றத்தின் staging-only migration மற்றும் dual-provider RLS tests முடிந்த பிறகே Login button enable செய்ய வேண்டும். பழைய Login-ஐ அகற்றக்கூடாது.
- Live Google chooser, Login/Logout, token refresh/expiry, cross-browser session isolation மற்றும் Data API RLS சோதனைகள் இன்னும் நிலுவை.

## அதிகாரப்பூர்வ ஆதாரங்கள்

- [Supabase Firebase third-party authentication](https://supabase.com/docs/guides/auth/third-party/firebase-auth)
- [Firebase ID token validation](https://firebase.google.com/docs/auth/admin/verify-id-tokens)
- [Google Python Firebase verifier](https://google-auth.readthedocs.io/en/latest/reference/google.oauth2.id_token.html)
- [Firebase Google Web Login](https://firebase.google.com/docs/auth/web/google-signin)

## Offline சரிபார்ப்பு

Google verifier-ன் உண்மையான RSA signature code path-ஐ synthetic keys/certificates-உடன் பயன்படுத்திய 35 புதிய token tests வெற்றி. மொத்தம் 279 unit tests வெற்றி; pip dependency check மற்றும் git diff whitespace check வெற்றி. Live Firebase project/token, Google browser Login, Firebase Logout/revocation, UUID mapping மற்றும் live cross-provider RLS tests நடத்தப்படவில்லை. இந்த முடிவுகளை Firebase Login வெற்றியாகக் கருதக்கூடாது.
