import zipfile, os, shutil
from pathlib import Path

# compression = zipfile.ZipFile(Path.home() / Path("OneDrive", "سطح المكتب",
#                                                  "folders.zip"))
# print(compression.namelist()) # tell you want file in this folder
#
# info = compression.getinfo("folders/writing.py")
# print(info.file_size)
# print(info.compress_size)
#
# # extract
os.chdir(Path.home() / Path("OneDrive", "سطح المكتب"))
# # to extract all file in folder
# compression.extractall()
# # to extract special file from folder
# compression.extract("folders/reading.py", Path.home() / Path("OneDrive",
#                                                             "سطح المكتب" , "newfile"))
#
#
# # compression file
# new_zip = zipfile.ZipFile("new.zip", 'w')
# # create new file it's name folder and in it create file name myfile.txt
# new_zip.write("folders/MyFile.txt")
#
# # compression folder
# # not practical method
# new_folder_zip = zipfile.ZipFile("new_folder.zip", 'w')
# new_folder_zip.write(Path.home()/Path("OneDrive", "سطح المكتب", "newfile"))

# practical method
shutil.make_archive("compression_folder", "zip", Path.home()/Path("OneDrive",
                                                    "سطح المكتب", "folders"))