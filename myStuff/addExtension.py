f = open('_FileList.txt')
fNew = open('new.txt','w+')

path = r'"D:\FalsePositivesDataBase'
extension = r'.dat'

for line in f:
    line = line.strip('\n')
    fNew.write(path + '\\' + line + extension + '"\n')

f.close()
fNew.close()

print("##### Job done! #####")