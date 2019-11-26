import os
import shutil
import datetime

def find_file(name, path):
    # find file in given path (the first match)
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)


def copy_file(src, dest):
    # copy file from source to destination
    try:
        shutil.copy(src, dest)
    # eg. source and destination are the same file
    except shutil.Error as e:
        print('Error: {0}'.format(e))
        # eg. source or destination doesn't exist
    except IOError as e:
        print('Error: {0}'.format(e.strerror))


def main():
    # main begin
    f = open("_details.txt")
    for i, line in enumerate(f):
        if i == 1: 
            destination_folder = line.strip('\n')
        if i == 2:
            search_dir = line.strip('\n')
    f.close()
    
    # open .txt file, 'r'ead mode is default
    # each line in search_list.txt includes file name
    f = open('listOfNames.txt')

    while True:
    # begin while loop

        # read each line from .txt file + cut off line break char
        file_name = f.readline().strip('\n')
        if file_name:
            # try to find file in search_dir
            file_path = find_file(file_name, search_dir)
   
            # if file is found, copy it to [out_files] folder
            if file_path:
                copy_file(file_path, destination_folder)
                print (str(datetime.datetime.now().time())+" --> "+file_name)
            else:
                print (str(datetime.datetime.now().time())+" --> "+file_name+" --> file not found")

        # Zero length indicates EOF
        if len(file_name) == 0:
            break
        
        

    # end of while loop

    # close the file
    f.close()

# main end

if __name__ == "__main__": main()