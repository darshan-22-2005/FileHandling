# Check whether a file exists   

import os       
file_path = r"D:\Professional Course on Python\Assignments\File handling packages\Content.docx" 
if os.path.exists(file_path):
    print(" File exists ")    
else:
    print(" File does not exist at:", file_path)
