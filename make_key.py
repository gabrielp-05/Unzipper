import os
import winreg as reg
import glob

# Get path of current working directory and python.exe
cwd = os.getcwd()

# Get path of main exe to be added to context menu (prioritises the first in alphabetical order)
exe = glob.glob(f"{cwd}\\Unzipper*.exe")[0]
filename = os.path.splitext(os.path.basename(exe))[0]

# Set the path of the context menu (right-click menu)
key_path = f'Directory\\Background\\shell\\{filename}\\'

# Create outer key
key = reg.CreateKey(reg.HKEY_CLASSES_ROOT, key_path)
reg.SetValue(key, '', reg.REG_SZ, '&Uncompress all compressed files')

# create inner key
key1 = reg.CreateKey(key, r"command")
reg.SetValue(key1, '', reg.REG_SZ, exe)
reg.SetValue(key1, '', reg.REG_SZ, exe)  # hides terminal
