import re
m='android/app/src/main/AndroidManifest.xml'
s=open(m).read()
perms='''    <uses-permission android:name="android.permission.INTERNET" />
    <uses-permission android:name="android.permission.RECORD_AUDIO" />
    <uses-permission android:name="android.permission.MODIFY_AUDIO_SETTINGS" />
    <uses-permission android:name="android.permission.ACCESS_NETWORK_STATE" />
    <queries>
        <intent><action android:name="android.speech.RecognitionService" /></intent>
    </queries>
'''
# AdMob APP ID: Google TEST id. Replace with your real App ID before publishing.
meta='''        <meta-data android:name="com.google.android.gms.ads.APPLICATION_ID" android:value="ca-app-pub-3940256099942544~3347511713"/>
'''
s=s.replace('</manifest>',perms+'</manifest>') if 'RECORD_AUDIO' not in s else s
s=re.sub(r'(<application[^>]*>)',r'\1\n'+meta,s,count=1) if 'APPLICATION_ID' not in s else s
open(m,'w').write(s)
v='android/variables.gradle'
t=open(v).read()
t=re.sub(r'minSdkVersion\s*=\s*\d+','minSdkVersion = 23',t)
open(v,'w').write(t)
print('patched')
g='android/app/build.gradle'
b=open(g).read()
b=re.sub(r'minifyEnabled\s+false','minifyEnabled true\n            shrinkResources true',b)
open(g,'w').write(b)
print('release minify on')
