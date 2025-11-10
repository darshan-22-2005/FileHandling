# Check if a file is empty

import os

file_path = r"D:\Professional Course on Python\Assignments\File handling packages\Content.txt"

if os.path.exists(file_path):
    if os.path.getsize(file_path) == 0:
        print("The file is empty.")
    else:
        print("The file is not empty.")
else:
    print("File does not exist.")