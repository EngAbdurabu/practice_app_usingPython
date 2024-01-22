import os, shutil, re
from pathlib import Path

pattern = "^(.*?)((0|1)?\d)-((0|1|2|3)?\d)-((19|20)\d\d)(.*?)$"

for filename in os.listdir(Path.home()/Path("OneDrive", "سطح المكتب", "files")):
	search = re.search(pattern, filename)

	if search == None:
		continue


	beforedate = search.group(1)
	month = search.group(2)
	day = search.group(4)
	year = search.group(6)
	afterdate = search.group(8)

	newfilename = beforedate + day + '-' + month + '-' + year + afterdate
	print(f'Renaming the "{filename}" to "{newfilename}"')

	oldName = Path.home()/Path("OneDrive", "سطح المكتب", "files")/filename
	newName = Path.home()/Path("OneDrive", "سطح المكتب", "files")/newfilename

	shutil.move(oldName, newName)


