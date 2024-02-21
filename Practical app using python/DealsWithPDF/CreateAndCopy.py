from PyPDF2 import PdfFileWriter as w
from pathlib import Path
import PyPDF2

# create
pdf = w()
file = open(Path.home()/Path("OneDrive", "سطح المكتب", "python_practical",
                              "pdf_file.pdf"), "wb")

for i in range(4):
	pdf.addBlankPage(219, 297) # A4 dimension

pdf.write(file)

# copy
pdffile = open(Path.home()/Path("OneDrive", "سطح المكتب", "python_practical",
                              "pdf_test.pdf"), "rb")
pdfReader = PyPDF2.PdfFileReader(pdffile)

for numpage in range(pdfReader.numPages):
	ObjFile = pdfReader.getPage(numpage)
	pdf.addPage(ObjFile)

pdf.write(file)

file.close()