# Unzipper
A small Python program which allows users to extract all .zip files in any given folder using the right-click context menu.

Goals: 
  - Compile both scripts into an executable to be installed on a users computer ✔
  - Add support for more file types (e.g. .rar) 🔨

# Issues: 
- I have yet to find a library in Python which allows me to extract from an archive of the .rar .zip and .7z formats, so this is being worked on.

Note:
  - When uninstalling or updating, remove the key in "Computer\HKEY_CLASSES_ROOT\Directory\Background\shell\Unzipper"
