from docx import Document

questions = ["What is Python?", "Define data types.", "Explain file handling."]
doc = Document()
doc.add_paragraph("\n".join(questions))
doc.save("questionnaire.docx")