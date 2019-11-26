f = open("list.txt")
fo = open("unique.txt","w+")
unique = []

for line in f:
    line = line.strip('\n')
    if line not in unique:
        unique.append(line)
        fo.write(line + "\n")

print(len(unique))

f.close()
fo.close()