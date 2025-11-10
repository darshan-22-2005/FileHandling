# Count the words and lines in a text file


from docx import Document
import os       
file_path = r"D:\Professional Course on Python\Assignments\File handling packages\Content.docx"

if os.path.exists(file_path):
    line_count = 0
    word_count = 0
    doc = Document(file_path)
    for paragraph in doc.paragraphs:
        line_count += 1
        words = paragraph.text.split()
        word_count += len(words)
    print(" Total Lines:", line_count)
    print(" Total Words:", word_count)
else:
    print("File not found at:", file_path)