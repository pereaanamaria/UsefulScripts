import os
import shutil
import datetime

def copy_file(src, dest):
    try:
        shutil.copy(src, dest)
    except shutil.Error as e:
        print('Error: {0}'.format(e))
    except IOError as e:
        print('Error: {0}'.format(e.strerror))

file_paths = open('_paths.txt')
path_out = file_paths.readline().replace('\"','').strip('\n')
file_paths.close()

path_in = r'V:\RO01\Common\Engineering & Development\Vision-NightVision (10)\99_ALGO\08_Feature_Test\FileInfoDataBaseNV4'

for r, d, f in os.walk(path_in):
    for file in f:
        if '_FileInfo.txt' in file:
            path_to_file = os.path.join(r, file)
            copy_file(path_to_file, path_out)
            print (str(datetime.datetime.now().time())+": "+ path_to_file)