[app]
# General app metadata
title = SlideshowApp
package.name = slideshowapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,jpeg,gif
version = 1.0

# Files and directories to exclude to reduce APK size
source.exclude_exts = spec
source.exclude_dirs = tests,bin,venv,__pycache__
source.exclude_patterns = LICENSE,README.md,*.md,*.pyc,*.pyo

# Python and Kivy dependencies
requirements = python3,kivy==2.1.0,requests

# Android-specific settings
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.ndk = 23.1.7779620
android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True
android.accept_sdk_license = True
android.enable_androidx = False

# Lock to landscape for slideshow UI
orientation = landscape
fullscreen = 1

# Logging and debugging
android.logcat_filters = *:S python:D

# Specify icon
icon.filename = %(source.dir)s/assets/icon.png

[buildozer]
# Verbose logging for debugging
log_level = 2
warn_on_root = 1

# Use SDL2 bootstrap for Kivy
p4a.bootstrap = sdl2

# Ensure compatibility with Python-for-Android
p4a.branch = stable
