import os
import shutil
print('hello world')


##YOUTUBE DOWNLOADER STUFF



testing_folder = r'C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Comp\4. test folder'

user_folder_cacher = r'C:\ProgramData\Blackmagic Design\DaVinci Resolve\Fusion\Scripts\Comp\3. text files\user_folder_cacher.txt'

print(user_folder_cacher, 'is real in python')



with open(user_folder_cacher, 'r') as f:
    user_folder = f.readlines()
    
print(user_folder, 'is my user folder')



test_folder_dir = os.listdir(testing_folder)
print(test_folder_dir, ' is x' )

for i in test_folder_dir:
    print(i, 'caramba')
    #if ('mp4') in str(i) and len(x) == 1:
    print('mp4 detected, and there is only one file in this folder!!!')
    test_folder_video = str(testing_folder) + '\\'+str(i)
           
    shutil.move(test_folder_video,(user_folder[0]))


    #!/usr/bin/env python
    import DaVinciResolveScript as dvr_script
    resolve = dvr_script.scriptapp("Resolve")
    fusion = resolve.Fusion()
    #print(fusion, ' is fusion.')
    projectManager = resolve.GetProjectManager()
    proj = projectManager.GetCurrentProject()
    mediaStorage = resolve.GetMediaStorage()
    mp = proj.GetMediaPool()
    root = mp.GetRootFolder()
    root_subs = root.GetSubFolders()

    root_name = root.GetName()    

    final_user_video = user_folder[0] + '\\' + i
    
    
    mediaStorage.AddItemsToMediaPool(final_user_video)

