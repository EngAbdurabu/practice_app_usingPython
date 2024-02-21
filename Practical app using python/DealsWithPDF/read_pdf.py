import PyPDF2
from pathlib import Path

PdfFileObj = open(Path.home()/Path("OneDrive", "سطح المكتب", "python_practical",
                              "pdf_test.pdf"), "rb")
# PdfFileObj = open(Path.home()/Path("OneDrive", "سطح المكتب", "python_practical",
#                               "desktop_instruction.pdf"), "rb", encoding='utf-8')

PdfReader = PyPDF2.PdfFileReader(PdfFileObj)

# page number
print(PdfReader.numPages)

# Read
text = PdfReader.getPage(0)
print(text.extractText())

PdfFileObj.close()