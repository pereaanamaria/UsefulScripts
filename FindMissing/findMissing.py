import os

#file_inter = open("FullList.txt")
#file_inter = open("IntermediarList.txt")

file_inputs = open("inputs.txt")

extension = file_inputs.readline().strip("\n")
full_path = file_inputs.readline().strip("\n")
inter_path = file_inputs.readline().strip("\n")

file_inputs.close()

interList = []

'''
for line in file_inter:
    interList.append(line.strip('\n'))

file_inter.close()
'''

for r, d, f in os.walk(inter_path):
    for file in f:
        if extension in file:
            name = file[:42]
            interList.append(name)
                
no_dupl_list = []

#file_full = open("IntermediarList.txt")
#file_full = open("FullList.txt")
file_missing = open("MissingList.txt",'w+')

empty = True

'''
for line in file_full:
    line = line.strip('\n')
    if line not in no_dupl_list:
        if line not in interList:
            file_missing.write(line + '\n')
            empty = False
        no_dupl_list.append(line)

file_full.close()
'''

for r, d, f in os.walk(inter_path):
    for file in f:
        if extension in file:
            name = file[:42]
            if name not in no_dupl_list:
                if name not in interList:
                    file_missing.write(name + '\n')
                    empty = False
                no_dupl_list.append(name)

file_missing.close()

no_dupl_list.sort()
interList.sort()

print("")

if no_dupl_list == interList:
    print("##### Identical lists. \n")
else:
    print("##### The lists are not identical!\n")

if empty:
    print("##### All good!! -> MissingList file is empty!\n")
else: print("##### Not good!! -> MissingList file is not empty!\n")

print("##### Job done. #####")