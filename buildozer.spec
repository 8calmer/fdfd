[app]
title = SlideshowApp
package.name = slideshowapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,jpeg,gif
source.exclude_dirs = tests,bin,venv,pycache 
source.exclude_patterns = .pyc,.pyo
version = 1.0

requirements = python3,kivy,requests

android.permissions = INTERNET

android.api = 33
android.minapi = 21
android.arch = armeabi-v7a,arm64-v8a

orientation = landscape
fullscreen = 1

[buildozer] 
log_level = 2
warn_on_root = 1
