import xlrd
import os

fld_list = []

def getFolderName(file_path):
    findX = file_path.rfind('\\')
    fname = file_path[:findX]
    findX2 = fname.rfind('\\')
    fname1 = file_path[:findX2]
    findX1 = fname1.rfind('\\') + 1
    fld_name = file_path[findX1:findX2]
    if fld_name not in fld_list:
        fld_list.append(fld_name)
        line_print = "---------------------->>  Found in folder  <==>  " + fld_name + '  <<----------------------\n' 
        print(line_print)
    return fld_name

file = open('_ExcelList.txt')
path_Excel = file.readline().strip('\n')
file.close()

excel_lists = []

for r, d, f in os.walk(path_Excel):
    for dir_name in d:
        for file_name in f:
            if '.xlsm' in file_name and not '~$' in file_name:
                file_path = os.path.join(r,file_name)
                if file_path not in excel_lists:
                    excel_lists.append(file_path)

print("")

file = open('Data.txt','w+')

file.write("Folder name,Frame Based TP-Rate,Track Based TP-Rate,FP Track/h,Excel\n")

for file_excel in excel_lists:
    fld_name = getFolderName(file_excel)
    
    file.write(fld_name + ', ')
    print(file_excel)
    
    #creat a workbook and add a worksheet
    workbook = xlrd.open_workbook(file_excel)

    #open TP-Rates sheet
    sheet = workbook.sheet_by_name("TP-Rates")
    
    frameBasedTPRate = 0
    trackBasedTPRate = 0
    count = 0
    
    if 'Animal' in file_excel:
        category = 'Animal'
    else:
        category = 'Pedestrian'

    for row in range(sheet.nrows):
        if sheet.cell(row,1).value == category:
            if count == 0:
                frameBasedTPRate = round(sheet.cell(row,4).value * 100, 1)
                count += 1
            elif count == 1:
                trackBasedTPRate = round(sheet.cell(row,4).value * 100, 1)
                count += 1
                break
    
    file.write(str(frameBasedTPRate) + "%,")
    print("Frame Based TP-Rate = " + str(frameBasedTPRate) + "%")
    file.write(str(trackBasedTPRate) + "%,")
    print("Track Based TP-Rate = " + str(trackBasedTPRate) + "%")

    #open TP-Rates sheet
    sheet = workbook.sheet_by_name("FP-FW-Rates")
    
    FPRatePerH = 0
    foundTrack = False
    
    for row in range(sheet.nrows):
        if sheet.cell(row,1).value == 'FPTrack-Rate by - ObjectType' and not foundTrack:
            foundTrack = True
            
        if sheet.cell(row,1).value == category and foundTrack:
            FPRatePerH = round(sheet.cell(row,3).value)
            break

    file.write(str(FPRatePerH) + ",")
    print("FP Track/h = " + str(FPRatePerH))  
    
    workbook.release_resources()
    
    if '_Classification' in file_excel:
        file.write('Classification\n')
    elif '_Cluster' in file_excel:
        file.write('Cluster\n')
    elif '_TrackerPedestrian' in file_excel:
        file.write('Tracker Pedestrian\n')
    elif '_TrackerAnimal' in file_excel:
        file.write('Tracker Animal\n')
    elif '_WarningDecision' in file_excel:
        file.write('Warning Decision\n')
        
    print("")

file.close()

print("\n##### Data has been extracted #####")