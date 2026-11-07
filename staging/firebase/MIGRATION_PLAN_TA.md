# பழைய பயனர் முன்னேற்றத்தைப் பாதுகாக்கும் migration திட்டம்

**இது திட்டம் மட்டுமே. Production migration பரிந்துரைக்கப்படவில்லை; எந்த production தரவும் நகலெடுக்கப்படவில்லை அல்லது மாற்றப்படவில்லை.** Firebase deployment மற்றும் உண்மையான browser/RLS சோதனைகள் முடியும் வரை production cutover செய்யக்கூடாது.

1. Production-க்கு வெளியே synthetic test accounts/progress-ஐப் பயன்படுத்தி dual-provider schema உருவாக்கவும். தற்போதைய Supabase UUID-யை canonical UUID ஆகவே வைத்திருக்கவும்; progress, revision, XP, streak, weakness, mentor, mission owner IDs மாறக்கூடாது.
2. Firebase UID-க்கு அதே canonical UUID-யை இணைப்பதற்கு ஒரே browser session-ல் பழைய Supabase கணக்கின் சமீபத்திய reauthentication மற்றும் புதிய Google/Firebase கணக்கின் verified/recent authentication ஆகிய இரண்டும் தேவை. Email பொருந்துவது, username, mobile அல்லது user_metadata மட்டும் உரிமைக்குச் சான்றல்ல.
3. Session-bound nonce/CSRF state, குறுகிய கால one-use linking ticket மற்றும் immutable unique `(issuer, subject)` mapping வேண்டும். வேறொருவருடன் இணைக்கப்பட்ட Firebase identity-ஐ overwrite/reassign செய்யக்கூடாது. Concurrent linking transaction-safe ஆக வேண்டும். Audit-ல் token/key/கடவுச்சொல் பதிவு செய்யக்கூடாது.
4. Legacy Supabase accounts-ஐ நீக்கவோ, progress rows-ஐ Firebase UID-க்கு மறுபதிவு செய்யவோ வேண்டாம். புதிய Firebase-only users-க்கு புதிய canonical UUID; பழைய email collision-க்கு account linking flow; automatic merge இல்லை.
5. இரண்டு providers-ல் வரும் ஒரே user தனது அதே progress-ஐ மட்டுமே காண வேண்டும். தொடர்பில்லாத identity, UUID போலத் தோன்றும் Firebase UID, வேறு issuer/project, forged/expired/unverified/revoked token அனைத்தும் மறுக்கப்பட வேண்டும். Supabase பழைய session-களும் பாதுகாப்பாகத் தொடர்ந்து இயங்க வேண்டும்.
6. Google popup cancellation, expired callback, token refresh failure, logout, இரு browser contexts, shared device, account switching, network failure, duplicate email/link conflict மற்றும் deployment rollback ஆகியவற்றைச் சோதிக்கவும். தனியான test inbox-களில் மட்டுமே email flow சோதனை செய்யவும்.
7. Browser மற்றும் live Data API tests வெற்றியடைந்தபின் மட்டும் தனியான production review/approval பெறவும். முதலில் schema backup/restore drill, rollback plan மற்றும் குறைந்த அளவிலான opt-in linking வேண்டும். Production தரவை staging-க்கு நகலெடுப்பது இந்தத் திட்டத்தில் இல்லை.
8. Rollback-க்கு Firebase UI-ஐ நிறுத்தி legacy Login தொடரக்கூடிய வடிவம் தேவை. இருந்த UUID/progress/link audit-ஐ அழிக்கக்கூடாது. Users-ஐ logout செய்ய வேண்டிய நிலை மற்றும் token expiry/revocation விளைவுகளை முன்கூட்டியே ஆவணப்படுத்தவும்.

## நிலுவைச் சோதனை அட்டவணை

| பகுதி | தற்போதைய ஆதாரம் | மீதமுள்ளது |
|---|---|---|
| Firebase token cryptography | Synthetic RSA keys-உடன் உண்மையான Google verifier unit tests | உண்மையான Test Firebase token, revocation/disabled user |
| பழைய Login/Logout/Remember Me | Existing unit suite தொடர்கிறது | Hosted regression |
| Firebase Login/Logout | இன்னும் App-ல் இணைக்கப்படவில்லை | Google chooser + client/server cleanup |
| Firebase session isolation | Namespace/project validation unit tests மட்டும் | இரண்டு browser contexts மற்றும் token refresh |
| User data isolation | தற்போதைய UUID/RLS schema read-only ஆய்வு | புதிய mapping/helper மீது live cross-provider CRUD |
| Progress continuity | UUID-ஐ மாற்றாத வடிவமைப்பு | Synthetic old-account + Google linking end-to-end |
