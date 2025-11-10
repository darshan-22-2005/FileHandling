# Add new content to a existing file

file_path = r"D:\Professional Course on Python\Assignments\File handling packages\Content.docx"

new_lines = [
    "\nWhat is data science?",
    "Explain machine learning.",
    "Define artificial intelligence."]

with open(file_path, "a", encoding="utf-8") as file:
    for line in new_lines:
        file.write(line + "\n")

print(" Added successfully!")