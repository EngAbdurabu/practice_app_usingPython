import os, send2trash, shutil
from pathlib import Path

# this method is permanent remove
# revome files using unlink()
# os.unlink(Path.home()/Path("OneDrive", "سطح المكتب", "folders", "file1.txt"))
# for remove empty folder using rmdir()
# os.rmdir(Path.home()/Path("OneDrive", "سطح المكتب", "folders", "empty"))
# for remove folder content files
# shutil.rmtree(Path.home()/Path("OneDrive", "سطح المكتب", "folders", "files"))

# for send the remove file or folder to trash temporary revome
send2trash.send2trash(Path.home()/Path("OneDrive", "سطح المكتب", "folders", "file2.txt"))
send2trash.send2trash(Path.home()/Path("OneDrive", "سطح المكتب", "folders", "venv"))
