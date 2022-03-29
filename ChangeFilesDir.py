import os
from shutil import move

targetDirs = ["Des", "Pre", "Prod"]
directory = os.getcwd()
subfolders = [os.path.abspath(name) for name in os.listdir(".") if os.path.isdir(name)]
for subfolder in subfolders:
    os.chdir(subfolder)
    files = [os.path.relpath(name) for name in os.listdir(".") if not os.path.isdir(name)]
    for targetDir in targetDirs:
        try:
            os.mkdir(targetDir)
        except:
            pass
        for fileDir in files:
            if fileDir.find(targetDir) != -1:
                #print(str(fileDir.find(targetDir))+ fileDir)
                move(fileDir, os.path.abspath(targetDir))
