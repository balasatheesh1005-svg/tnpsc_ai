# Firebase Google Login — Feature branch நிலை

Firebase Test Project, Google provider, Web App மற்றும் authorized domain அமைக்கப்பட்டதாகத் திட்ட உரிமையாளர் தெரிவித்துள்ளார். தற்போதைய Streamlit deployment மற்றும் இரு Supabase சூழல்களிலும் மாற்றங்கள் செய்யப்படவில்லை.

## அடையாள இணைப்பு

ஆரம்ப staging சோதனைக்கு ஏற்கெனவே உள்ள staging profile UUID-ஐத் தனிப்பட்ட schema-வில் Firebase UID உடன் இணைக்கும் முறையைத் தேர்வு செய்துள்ளோம். நிர்வாகி இரு கணக்குகளின் உரிமையையும் சரிபார்த்த பிறகே இணைப்பைப் பதிவு செய்ய வேண்டும். மின்னஞ்சலை வைத்து தானாக இணைப்பதும், புதிய profile உருவாக்குவதும் இந்தக் கட்டத்தில் கிடையாது. தற்போதைய profile மற்றும் முன்னேற்ற UUID-கள் தொடரும். இந்த முறை DESIGN_TA.md-ல் உள்ள புதிய canonical user அட்டவணை யோசனைக்கு முன் சோதிக்க வேண்டிய குறுகிய staging வழி.

`prepare_identity_mapping.sql` staging snapshot-ல் உள்ள 23 கொள்கைகளின் பெயர், operation, role மற்றும் owner checks ஆகியவற்றைச் சரிபார்க்கிறது. Firebase பயனருக்கு mapping கிடைத்தால் மட்டுமே அதே owner check செயல்படும். SQL கோப்பு ROLLBACK-ல் முடிகிறது. Hosted PostgreSQL-ல் இயக்கப்படவில்லை. Bookmarks, analytics மற்றும் Username Login சிக்கல்கள் இந்த மாற்றத்தின் வரம்பில் தீர்க்கப்படவில்லை.

`bind_firebase_profile()` சரிபார்க்கப்பட்ட Firebase token-ஐ தனி Supabase SDK client-ன் PostgREST bearer ஆகப் பயன்படுத்துகிறது. Staging URL pin, publishable/anon configuration, mapping RPC, RLS வழியாகப் பார்க்கக்கூடிய ஒரே UUID ஆகியவை தேவை. இது Streamlit அமர்வைத் தொடங்காது. Google Login பொத்தான் மற்றும் callback இன்னும் சேர்க்கப்படவில்லை.

## Deployment முன் நிலுவை

- மாற்றமில்லாத தற்போதைய test app-இலிருந்து தனியாக ஒரு preview deployment பயன்படுத்த வேண்டும். அதற்கான hostname-ஐ Firebase Authorized Domains-ல் சேர்க்க வேண்டும்.
- Firebase browser SDK callback, replay தடுப்பு, session cleanup, token expiry மற்றும் revocation கையாளுதல் தேவை.
- Test Supabase Third-Party Auth trust, Firebase Admin வழியாக authenticated claim வழங்குதல், rollback SQL சரிபார்ப்பு மற்றும் உண்மையான இரு synthetic test identities-ன் RLS சோதனை தேவை.
- Email/Password மற்றும் Password Reset உள்ளிட்ட browser regression சோதனைகள் நிலுவை.
