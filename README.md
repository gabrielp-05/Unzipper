# Unzipper

# This branch is experimenting with a new library called pyunpack, which utilises the patoolib library, for decompressing multiple file types (rar, zip, possibly 7z though this doesn't currently work with PyInstaller)

A small Python program which allows users to extract all .zip files in any given folder using the right-click context menu.

Goals: 
  - Compile both scripts into an executable to be installed on a users computer ✔
  - Add support for more file types (e.g. .rar, .7z) 🔨

# Issues: 
- I have yet to find a library in Python which allows me to extract from an archive of the .rar .zip and .7z formats, so this is being worked on.

# Notes:
  - When uninstalling or updating, remove the key in "Computer\HKEY_CLASSES_ROOT\Directory\Background\shell\Unzipper"
