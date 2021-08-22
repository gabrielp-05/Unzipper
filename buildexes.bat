pip install pyinstaller
pyinstaller --clean --onefile --noconsole Unzipper.py
pyinstaller --clean --onefile --noconsole --uac-admin make_key.py