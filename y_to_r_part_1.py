import os
from tkinter import Tk
from tkinter.filedialog import askdirectory

 
user_folder = askdirectory(title='Select Folder') # shows dialog box and return the path

print (user_folder)





user_folder_cacher = r'C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Comp\3. text files\user_folder_cacher.txt'

print(user_folder_cacher, 'user folder selected!')

with open (user_folder_cacher, 'w') as f:

    f.writelines(user_folder)

    

