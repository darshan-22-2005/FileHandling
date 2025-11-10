# Delete a specific file
import os

file_path = r"D:\Professional Course on Python\Assignments\File handling packages\questionnaire.docx"

if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted successfully!")
else:
    print(" File not found.")