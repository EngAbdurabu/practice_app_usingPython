import docx

def GetText(filename):
	doc = docx.Document(filename)
	fulltext = []
	for para in doc.paragraphs:
		fulltext.append(para.text)

	return "\n".join(fulltext)
