# Check whether the path exists

import os
path = r"D:\Professional Course on Python\Assignments\File handling packages"
if os.path.exists(path):
    print("The path exists.")
else:
    print("The path does not exist.")
