import os
import datetime


#read from _details.txt
f = open('_details.txt')
path = f.readline().strip('\n')
path_FileInfo = f.readline().strip('\n')
f.close()

extensions = ['.dat','_FileInfo.txt','_AdtfInfo.txt']

#get existing files with the same extenstionas required from destination path
interList = []

for r, d, f in os.walk(path):
    for file in f:
        if '.dat' in file or '_AdtfInfo.txt' in file:
            interList.append(file)
            
for r, d, f in os.walk(path_FileInfo):
    for file in f:
        if '_FileInfo.txt' in file:
            interList.append(file)

#check existing with _FileList.txt and prepare for copy
no_dupl_list = []

file_full = open("_FileList.txt")
file_missing = open("listOfNames.txt",'w+')

count = 0

for line in file_full:
    line = line.replace('\"','').strip('\n')
    nr = line.find("NV4")
    line_dat = line[nr:nr+42] + r'.dat'
    line_AdtfInfo = line_dat.replace('.dat','_AdtfInfo.txt')
    line_FileInfo = line_dat.replace('.dat','_FileInfo.txt')
    #print(line)
    if line_dat not in no_dupl_list:
        if line_dat not in interList:
            file_missing.write(line_dat + '\n')
            count = count + 1
        no_dupl_list.append(line_dat)
    if line_AdtfInfo not in no_dupl_list:
        if line_AdtfInfo not in interList:
            file_missing.write(line_AdtfInfo + '\n')
            count = count + 1
        no_dupl_list.append(line_AdtfInfo)
    if line_FileInfo not in no_dupl_list:
        if line_FileInfo not in interList:
            file_missing.write(line_FileInfo + '\n')
            count = count + 1
        no_dupl_list.append(line_FileInfo)

file_full.close()
file_missing.close()

print("")
print(str(datetime.datetime.now().time()) + ": Missing " + str(count) + " files!\n")

#start copying at destination the missing files
if count:
    print("\n" + str(datetime.datetime.now().time()) +": Start copying missing files!\n")
    #os.system('python -3 copy.py')
    os.system('copy.py')

#print("\n##### Job done! #####")