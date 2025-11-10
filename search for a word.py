
file_path = r"D:\Professional Course on Python\Assignments\File handling packages\Content.txt"
search_word = "Data"   # 🔍 Word you want to search

found = False

with open(file_path, "r", encoding="utf-8") as file:
    for line_number, line in enumerate(file, start=1):
        if search_word.lower() in line.lower():  # case-insensitive search
            print(f"✅ Found '{search_word}' in line {line_number}: {line.strip()}")
            found = True

if not found:
    print(f"❌ The word '{search_word}' was not found in the file.")