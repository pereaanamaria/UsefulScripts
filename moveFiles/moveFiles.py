import os
import datetime

def getFileName(path):
    path = path.replace('\"','').strip('\n')
    x = path.rfind('\\') + 1
    filename = path[x:]
    return filename

list_filesToMove = []

f = open("_FileList.txt")

for line in f:
    line = getFileName(line)
    list_filesToMove.append(line)

f.close()

path_original = r"C:\Users\ana-maria.perea\Desktop\testingStuff\AutoCheck"
path_newLocation = r"C:\Users\ana-maria.perea\Desktop\testingStuff\AutoCheck\output_HIL"

for r, d, f in os.walk(path_original):
    for file in f:
        if ".dat" in file and file in list_filesToMove:
            old = path_original + '\\' + file
            new = path_newLocation + '\\' + file
            os.rename(old, new)
            print(str(datetime.datetime.now().time()) + " --> " + file)
            
print('\n' + str(len(list_filesToMove)) + " files have been moved")
print("\n##### JOB DONE! #####")