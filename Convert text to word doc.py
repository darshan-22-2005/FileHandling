# Convert text content to a Word document

from docx import Document           
text="""This is a sample text that will be converted into a Word document."""
doc = Document()
doc.add_paragraph(text)
doc.save("Content.docx")
print("Text has been converted to Word document successfully.")