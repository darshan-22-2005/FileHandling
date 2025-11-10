import os


"""
1. Doc Help 
2. File Extension Handling 
3. What happen prefix is not given.. Make the prefix as optional argument 
4. What happens when single slash is given in folder? 
5. 
"""
def renaming_file(prefix :str, folder :str): 
    for i, filename in enumerate(os.listdir(folder)):
        old = os.path.join(folder, filename)
        new = os.path.join(folder, f"{prefix}{i+1}_{filename}")
        os.rename(old, new)
