import os
import winreg as reg

# Get path of current working directory and python.exe
cwd = os.getcwd()

# Set the path of the context menu (right-click menu)
key_path = r'Directory\\Background\\shell\\Unzipper\\'

# Create outer key
key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
reg.SetValue(key, '', reg.REG_SZ, '&Unzip all zip files')

# create inner key
key1 = reg.CreateKey(key, r"command")
reg.SetValue(key1, '', reg.REG_SZ, f'{cwd}\\Unzipper.exe')
reg.SetValue(key1, '', reg.REG_SZ, f'{cwd}\\Unzipper.exe')  # hides terminal
