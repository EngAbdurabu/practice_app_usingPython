from pathlib import Path
from docx2pdf import convert
#
# file = Path.home()/Path("OneDrive", "سطح المكتب", "python_practical",
#                                      "academy_1.docx")
# convert(file)

# # to convert with change file name
# docx_file = Path.home()/Path("OneDrive", "سطح المكتب", "python_practical",
#                                      "write.docx")
# pdf_file = Path.home()/Path("OneDrive", "سطح المكتب", "python_practical",
#                                      "Pdf_write.pdf")
# convert(docx_file, pdf_file)

# to convert multiple file
multifile = Path.home()/Path("OneDrive", "سطح المكتب", "python_practical",
                                     "word file/")
# folder name / : means all file in folder
convert(multifile)