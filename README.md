# Articulate APK

## Quick test build
1. Create a PRIVATE GitHub repo (important: keeps your source hidden). Upload all files, including .github.
2. Actions > Build APK > Run workflow > download Articulate-APK.

## Protected release build (for Play Store)
1. Make a keystore once (keep it safe, never lose it):
   keytool -genkeypair -v -keystore ks.jks -alias articulate -keyalg RSA -keysize 2048 -validity 10000
2. Convert it: base64 -w0 ks.jks   (Mac: base64 -i ks.jks)
3. Repo > Settings > Secrets and variables > Actions > add:
   KEYSTORE_B64 (the base64 text), KEYSTORE_PASSWORD, KEY_ALIAS (articulate)
4. Run Build APK again > download Articulate-RELEASE (signed APK + AAB).

## Before earning
Real AdMob IDs: www/index.html (ADS) and App ID in scripts/patch-android.py. Set TEST:false.
