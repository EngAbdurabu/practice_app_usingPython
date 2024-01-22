import shutil
from pathlib import Path
import os
# for copy the files using the following instruction
# shutil.copy(copied from path, copied  to path)
shutil.copy("file_one.txt", Path.home() / Path("OneDrive","سطح المكتب", "files",
                                               "copied_file.txt"))

# for copy the folders with the content of the folder
shutil.copytree(Path(os.getcwd()), Path.home() / Path("OneDrive", "سطح المكتب"
                                                , "foders"))
