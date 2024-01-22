import shutil, os
from pathlib import Path

# to move the file from folder to other folder
# shutil.move(Path.home()/Path("OneDrive","سطح المكتب", "folders", "test.txt"),
#             Path.home()/Path("OneDrive","سطح المكتب", "files"))

# shutil.move(Path.home()/Path("OneDrive","سطح المكتب", "folders", "test1.txt"),
#             Path.home()/Path("OneDrive","سطح المكتب", "files", "test_final"))

# if not have the folder in the path this instruction ceate file using this name
# shutil.move(Path.home()/Path("OneDrive","سطح المكتب", "folders", "myfile.txt"),
#             Path.home()/Path("OneDrive","سطح المكتب", "test_desktop"))

# ========================================================================
# for rename file using to methods
# shutil.move(Path.home()/Path("OneDrive","سطح المكتب", "folders", "New Text.txt"),
#             Path.home()/Path("OneDrive","سطح المكتب", "folders", "MyFile.txt"))

os.rename("file_one.txt", "First_File.txt")