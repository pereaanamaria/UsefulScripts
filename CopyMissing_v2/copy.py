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
    destination_folder = f.readline().replace('\"','').strip('\n')
    f.close()
    
    destination_folder_FileInfo = os.path.join(destination_folder,'FileInfo')
    search_dir1 = r"V:\RO01\DataLake\DCS01\NV4REFB16D22D7C1\SE-JGJ105\2019"
    search_dir2 = r"V:\RO01\DataLake\DCS01\NV4REFB271507BF4\SE-JGJ105\2019"
    search_FileInto = r"V:\RO01\Common\Engineering & Development\Vision-NightVision (10)\99_ALGO\08_Feature_Test\FileInfoDataBaseNV4"
    # open .txt file, 'r'ead mode is default
    # each line in search_list.txt includes file name
    f = open('listOfNames.txt')

    while True:
    # begin while loop

        # read each line from .txt file + cut off line break char
        file_name = f.readline().strip('\n')
        if file_name:
            if '_FileInfo.txt' in file_name:
                file_path = find_file(file_name, search_FileInto)
                if file_path:
                    copy_file(file_path, destination_folder_FileInfo)
                    print (str(datetime.datetime.now().time())+" --> "+file_name)
                else:
                    print (str(datetime.datetime.now().time())+" --> "+file_name+" --> file not found")
            else:
                # try to find file in search_dir
                file_path1 = find_file(file_name, search_dir1)
                file_path2 = find_file(file_name, search_dir2)
                
                # if file is found, copy it to [out_files] folder
                if file_path1:
                    copy_file(file_path1, destination_folder)
                    print (str(datetime.datetime.now().time())+" --> "+file_name)
                elif file_path2:
                    copy_file(file_path2, destination_folder)
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