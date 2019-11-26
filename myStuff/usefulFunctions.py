import os
import subprocess

def getFileName(path):
    path = path.replace('\"','').strip('\n')
    x = path.rfind('\\') + 1
    filename = path[x:]
    return filename

def MergeTool():
    filelist = open('_FileList.txt')
    os.chdir('C:\Git\AdtfMergeTool-1.1.0-x64\ADTFMergeTool')
    path_dat = r'"C:\Users\ana-maria.perea\Desktop\testingStuff\SIL_script\new_output\NV4REFB16D22D7C1_SE-JGJ105_20190122_054202.dat"'
    dat_decal = r'"C:\Users\ana-maria.perea\Desktop\testingStuff\SIL_script\NV4REFB16D22D7C1_SE-JGJ105_20190122_054202_decal.dat"'
    _command = r'AdtfMergeTool.exe ' + path_dat + ' ' + dat_decal + r' --output ' + path_dat
    print(_command + '\n')
    os.system(_command) 
    filelist.close()
    
def OpenGitBash():
    current_path = os.getcwd()
    os.chdir('C:/Git/FdMainAes')
    _path = r"C:\Program Files\Git\git-bash.exe"
    proc = subprocess.Popen(_path)
    proc.wait()
    os.chdir(current_path)
