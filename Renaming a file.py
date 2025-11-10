import os

folder =r"D:\Professional Course on Python\Assignments\File handling packages\Files"
prefix = "updated_"
for i, filename in enumerate(os.listdir(folder)):
    old = os.path.join(folder, filename)
    new = os.path.join(folder, f"{prefix}{i+1}_{filename}")
    os.rename(old, new)