import PyPDF2
from pathlib import Path
from PyPDF2 import PdfFileWriter as w

caver = w()
file = open(Path.home() / Path("OneDrive", "سطح المكتب", "python_practical",
                         "article", "caver.pdf"), 'wb')

for i in range(0,1):
	caver.addBlankPage(219, 297)

caver.write(file)

# caver copy

pdffile = open(Path.home() / Path("OneDrive", "سطح المكتب", "python_practical",
                              "article", "academy_1.pdf"), 'rb')

pdfReader = PyPDF2.PdfFileReader(pdffile)

Caver = pdfReader.getPage(0)
caver.addPage(Caver)

caver.write(file)

file.close()