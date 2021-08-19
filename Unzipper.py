import os, logging, ctypes
from zipfile import ZipFile
from glob import glob

logging.basicConfig(filename=f'C:\\Users\\{os.getlogin()}\\AppData\\Local\\Unzipper\\errorlog.log', level=logging.ERROR, force=True, format='%(asctime)s %(levelname)s %(name)s %(message)s')

def main():
    """
    Gets the current dir, and unzips all .zip files inside, placing them in a folder.
    """

    cwd = os.getcwd()
    fileTypes = ['.zip'] # will later include support for '.rar','.7z' filetypes
    zipFiles = list()
    for fileType in fileTypes:
        zipFiles.extend(glob(cwd+r'\\*{}'.format(fileType)))

    error = False
    filesExtracted = 0

    for file in zipFiles:
        fileName = os.path.basename(file)
        try:
            with ZipFile(file,'r') as zipObj:
                zipObj.extractall(cwd+r'\\Unzipped\\'+os.path.splitext(fileName)[0])
                filesExtracted += 1
        except Exception as e:
            logging.error(e)
            error = True

    if error:
        ctypes.windll.user32.MessageBoxW(0, "One or multiple exceptions occured, this could be due to files being corrupted or a file requiring a password", "An error has occured", 16)
    if filesExtracted >= 1:
        ctypes.windll.user32.MessageBoxW(0, f"{filesExtracted} File extraction(s) completed.", "Completed", 0)


if __name__ == "__main__":
    main()
