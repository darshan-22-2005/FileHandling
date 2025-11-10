# Copy all text files from one folder to another folder
import os
import shutil

source_folder = r"D:\Professional Course on Python\Assignments\File handling packages\Files"
destination_folder = r"D:\Professional Course on Python\Assignments\File handling packages\Files\TextFiles"

os.makedirs(destination_folder, exist_ok=True)

for filename in os.listdir(source_folder):
    if filename.endswith(".txt"):
        shutil.copy(os.path.join(source_folder, filename), destination_folder)  
        print(f"Copied: {filename} to {destination_folder}")

print("File transfer completed.")



