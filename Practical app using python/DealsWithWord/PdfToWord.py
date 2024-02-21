from pdf2docx import Converter
from pathlib import Path

pdf_file = Path.home()/Path("OneDrive", "سطح المكتب", "python_practical",
                                     "desktop_instruction.pdf")
docx_file = Path.home()/Path("OneDrive", "سطح المكتب", "python_practical",
                                     "instruction_convert.docx")

# convert pdf to docx
cv = Converter(pdf_file)
cv.convert(docx_file)      # all pages by default
cv.close()