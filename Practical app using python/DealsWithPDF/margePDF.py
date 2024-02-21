import PyPDF2, os
from pathlib import Path

path = Path.home() / Path("OneDrive", "سطح المكتب", "python_practical",
                              "article")
pdffiles = []
for filename in os.listdir(path):
	if filename.endswith(".pdf"):
		pdffiles.append(filename)

pdffiles.sort(key=str.lower)

pdfWriter = PyPDF2.PdfFileWriter()

for filename in pdffiles:
	PdfFileObj = open(Path.home() / Path("OneDrive", "سطح المكتب", "python_practical",
                              "article", filename), 'rb')
	pdfReader = PyPDF2.PdfFileReader(PdfFileObj)

	for pageNum in range(1, pdfReader.numPages):
		pageObj = pdfReader.getPage(pageNum)
		pdfWriter.addPage(pageObj)



pdfOutPut = open(Path.home() / Path("OneDrive", "سطح المكتب", "python_practical",
                              "article", "article.pdf"), 'wb')
pdfWriter.write(pdfOutPut)
pdfOutPut.close()

