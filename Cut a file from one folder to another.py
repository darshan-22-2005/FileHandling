# Cut a file from one folder to another

import os
import shutil           
source_path = r"D:\Professional Course on Python\Assignments\File handling packages\questionnarie.txt"
destination_path = r"D:\Professional Course on Python\Assignments\File handling packages\Files\questionnarie.txt"
os.makedirs(destination_path, exist_ok=True)
shutil.move(source_path, destination_path)
print("File moved successfully!")
