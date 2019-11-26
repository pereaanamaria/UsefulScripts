import os
import datetime
import sys 

#read from _details.txt
f = open('_details.txt')
extension = f.readline().strip('\n')
path = f.readline().strip('\n')
f.close()

acceptedExtensions = ['.dat','_FileInfo.txt','_AdtfInfo.txt','_parameters.txt']

if extension not in acceptedExtensions:
    print(str(datetime.datetime.now().time()) +" --> Error! Unknown extension "+ extension + " !!!")
    print("\n##### Job NOT done! #####")
    sys.exit()

#get existing files with the same extenstionas required from destination path
interList = []

for r, d, f in os.walk(path):
    for file in f:
        if extension in file:
            interList.append(file)

#check existing with _FileList.txt and prepare for copy
no_dupl_list = []

file_full = open("_FileList.txt")

file_missing = open("listOfNames.txt",'w+')

count = 0

for line in file_full:
    nr = line.find("NV4")
    line = line[nr:nr+42] + extension
    #print(line)
    if line not in no_dupl_list:
        if line not in interList:
            file_missing.write(line + '\n')
            count = count + 1
        no_dupl_list.append(line)
file_full.close()
file_missing.close()

print("")
print(str(datetime.datetime.now().time()) + " --> Missing " + str(count) + " files!")

#start copying at destination the missing files
if count:
    print("\n" + str(datetime.datetime.now().time()) +" --> Start copying missing files!\n")
    #os.system('python -3 copy.py')
    os.system('copy.py')

print("\n##### Job done! #####")