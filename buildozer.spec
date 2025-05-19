[app]
title = SlideshowApp
package.name = slideshowapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,jpeg,gif
version = 1.0
source.exclude_exts = spec
source.exclude_dirs = tests,bin,venv,__pycache__
source.exclude_patterns = LICENSE,README.md,*.md,*.pyc,*.pyo
requirements = python3,kivy==2.1.0,requests
android.permissions = INTERNET
android.api = 31
android.minapi = 21
android.ndk = 23.1.7779620
android.archs = arm64-v8a
android.allow_backup = True
android.accept_sdk_license = True
android.enable_androidx = False
orientation = landscape
fullscreen = 1
android.logcat_filters = *:S python:D
icon.filename = %(source.dir)s/assets/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
p4a.bootstrap = sdl2
p4a.branch = stable
android.gradle_debug = True
android.gradle_version = 7.5
