[app]
title = Jarvis
package.name = jarvis
package.domain = org.jarvis
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,txt,json
version = 0.1

requirements = python3,kivy==2.3.0,pyjnius,android,requests,urllib3,chardet,idna

orientation = portrait
fullscreen = 0

android.permissions = INTERNET,ACCESS_NETWORK_STATE,BATTERY_STATS,WAKE_LOCK,FOREGROUND_SERVICE,RECEIVE_BOOT_COMPLETED,SET_ALARM,VIBRATE

android.api = 33
android.minapi = 24
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
