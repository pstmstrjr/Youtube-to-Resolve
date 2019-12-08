
import os

#NEW PATHS


yr_p3 = r'C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Comp\y_to_r_part_3.py'


testing_folder = r'C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Comp\4. test folder'


user_folder_cacher = r'C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Comp\3. text files\user_folder_cacher.txt'
    



bat_cacher = r'C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Comp\2. bat files\bat_cacher.bat'

url = input("enter the url : ") 
print (url)

with open(user_folder_cacher, 'r') as f:
    user_folder = f.read()

with open (bat_cacher, 'w') as f:
    f.writelines('cd ' + '"' + testing_folder + '"')
    f.writelines('\nyoutube-dl -f bestvideo[ext=mp4]+bestaudio[ext=m4a]/mp4  '+ '"' + url + '"')
    f.writelines ('\n"' + yr_p3 + '"')
    f.writelines('\nif errorlevel 1 echo Unsuccessful')
    f.writelines('\npause')
    
    
    



print(user_folder)



import subprocess

subprocess.call([bat_cacher])
