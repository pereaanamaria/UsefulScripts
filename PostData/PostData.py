import os
import shutil
current_path = os.getcwd()

#------------------------------------------------------
#extract data
shutil.copy('_paths.txt', 'ExtractData\_ExcelList.txt')
os.chdir('ExtractData')
os.system('ExtractData.py')
os.chdir(current_path)

#------------------------------------------------------
#generate the table for Confluence
path_html = r"genetatedHTML.html" 
file_out = open(path_html,"w")
file_in = open('ExtractData\Data.txt','r')
data = file_in.readlines()

table = "<table>\n"

folder_list = []
category_list = ['Classification','Clustering','Tracker Pedestrian','Warning Decision']
color_list = ['red','green','blue','yellow']

table += """  <tr>
    <th rowspan=\"2\">              </th>
    <th class="highlight-red" colspan="3" data-highlight-colour="red" style="text-align: center;width: 180.0px;">Classification</th>
    <th class="highlight-green" colspan="3" data-highlight-colour="green" style="text-align: center;width: 180.0px;">Clustering</th>
    <th class="highlight-blue" colspan="3" data-highlight-colour="blue" style="text-align: center;width: 180.0px;">Tracker Pedestrian</th>
    <th class="highlight-yellow" colspan="3" data-highlight-colour="yellow" style="text-align: center;width: 180.0px;">Warning Decision</th>
  </tr>\n    
"""

# Create the table's column headers
header = data[0].split(",")

table += "  <tr>\n"
for times in range(0,4):
    for column in range(1,len(header)-1):
        table += "    <th class=\"highlight-{0}\" data-highlight-colour=\"{0}\" style=\"width: 60.0px;\">{1}</th>\n".format(color_list[times],header[column].strip())
table += "  </tr>\n"

classification = []
clustering = []
tracker = []
warning = []


firstRow = True
# Create the table's row data
for line in data[1:]:
    row = line.split(",")
    if row[0] not in folder_list:
        if firstRow:
            table += "  <tr>\n"
            firstRow = False
        else:
            if classification:
                for elem in classification:
                    table += "    <td class=\"highlight-red\" data-highlight-colour=\"red\" style=\"text-align: center;width: 60.0px;\">{0}</td>\n".format(elem.strip())
            else:
                for x in range(0,3):
                    table += "    <td class=\"highlight-red\" data-highlight-colour=\"red\" style=\"text-align: center;width: 60.0px;\">-</td>\n"
            if clustering:
                for elem in clustering:
                    table += "    <td class=\"highlight-green\" data-highlight-colour=\"green\" style=\"text-align: center;width: 60.0px;\">{0}</td>\n".format(elem.strip())
            else:
                for x in range(0,3):
                    table += "    <td class=\"highlight-green\" data-highlight-colour=\"green\" style=\"text-align: center;width: 60.0px;\">-</td>\n"
            if tracker:
                for elem in tracker:
                    table += "    <td class=\"highlight-blue\" data-highlight-colour=\"blue\" style=\"text-align: center;width: 60.0px;\">{0}</td>\n".format(elem.strip())
            else:
                for x in range(0,3):
                    table += "    <td class=\"highlight-blue\" data-highlight-colour=\"blue\" style=\"text-align: center;width: 60.0px;\">-</td>\n"
            if warning:
                for elem in warning:
                    table += "    <td class=\"highlight-yellow\" data-highlight-colour=\"yellow\" style=\"text-align: center;width: 60.0px;\">{0}</td>\n".format(elem.strip())
            else:
                for x in range(0,3):
                    table += "    <td class=\"highlight-yellow\" data-highlight-colour=\"yellow\" style=\"text-align: center;width: 60.0px;\">-</td>\n"
            classification = []
            clustering = []
            tracker = []
            warning = []
            table += "  </tr>\n"
            table += "  <tr>\n"
        folder_list.append(row[0])
        table += "    <th style=\"width: 110.0px;\">{0}</th>\n".format(row[0].strip())
            
    if 'Classification\n' in row:
        classification.append(row[1])
        classification.append(row[2])
        classification.append(row[3])
    if 'Cluster\n' in row:
        clustering.append(row[1])
        clustering.append(row[2])
        clustering.append(row[3])
    if 'Tracker Pedestrian\n' in row:
        tracker.append(row[1])
        tracker.append(row[2])
        tracker.append(row[3])
    if 'Warning Decision\n' in row:
        warning.append(row[1])
        warning.append(row[2])
        warning.append(row[3])
            
if classification:
    for elem in classification:
        table += "    <td class=\"highlight-red\" data-highlight-colour=\"red\" style=\"text-align: center;width: 60.0px;\">{0}</td>\n".format(elem.strip())
else:
    for x in range(0,3):
        table += "    <td class=\"highlight-red\" data-highlight-colour=\"red\" style=\"text-align: center;width: 60.0px;\">-</td>\n"
if clustering:
    for elem in clustering:
        table += "    <td class=\"highlight-green\" data-highlight-colour=\"green\" style=\"text-align: center;width: 60.0px;\">{0}</td>\n".format(elem.strip())
else:
    for x in range(0,3):
        table += "    <td class=\"highlight-green\" data-highlight-colour=\"green\" style=\"text-align: center;width: 60.0px;\">-</td>\n"
if tracker:
    for elem in tracker:
        table += "    <td class=\"highlight-blue\" data-highlight-colour=\"blue\" style=\"text-align: center;width: 60.0px;\">{0}</td>\n".format(elem.strip())
else:
    for x in range(0,3):
        table += "    <td class=\"highlight-blue\" data-highlight-colour=\"blue\" style=\"text-align: center;width: 60.0px;\">-</td>\n"
if warning:
    for elem in warning:
        table += "    <td class=\"highlight-yellow\" data-highlight-colour=\"yellow\" style=\"text-align: center;width: 60.0px;\">{0}</td>\n".format(elem.strip())
else:
    for x in range(0,3):
        table += "    <td class=\"highlight-yellow\" data-highlight-colour=\"yellow\" style=\"text-align: center;width: 60.0px;\">-</td>\n"
classification = []
clustering = []
tracker = []
warning = []
table += "  </tr>\n"
table += "</table>"

file_out.writelines(table)

file_out.close()
file_in.close()

print("\n##### HTML table for Confluence was generated. #####")
