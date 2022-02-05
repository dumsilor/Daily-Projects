from genericpath import isfile
import os
import string
import re
import sqlite3

available_drives = []
files = {}
folders = {}
file_list = []
folder_list = []
total_path= {}

connection = sqlite3.connect("list.db")
print(connection)
cur = connection.cursor()



for d in string.ascii_uppercase:
    if os.path.exists('%s:' % d):
     available_drives.append('%s:' % d)

# cur.execute(''' CREATE TABLE drive (serial INTEGER NOT NULL PRIMARY KEY, drive_name); ''')

drive_sr = 1

for drive in available_drives:
    cur.execute("INSERT INTO drive VALUES ('"+str(drive_sr)+"','"+drive+"');")
    drive_sr += 1
    os.chdir(drive+"\\")
    files[drive] = None
    elements = os.listdir(drive)
    for element in elements:
        # print(drive)
        # print(element)
        if isfile(element):
            # print(drive + "\\" + element + " is a file")
            file_list.append(element)
            files[drive] = file_list
        # print(drive + "\\" + element)
        else:
            # print(drive + "\\" + element + " is not a file")
            match = re.search(r"^\$", element)
            msi_match = re.search(r"\b\.Msi\b", element)
            tmp_match = re.search(r"\b\.tmp\b", element)
            sys_match = re.search(r"^System Volume Information$", element)
            rec_match = re.search(r"^Recovery$", element)
                # print(folders)
            if match or msi_match or tmp_match or sys_match or rec_match:
                continue
            else:
                folder_list.append(element)
                folders[drive] = folder_list
    file_list = []
    folder_list= []




for drive in available_drives:
    if drive == "C:":
        continue
    else:
        selected_folder_list = folders[drive]
        for folder in selected_folder_list:
            path = drive+"\\"+folder
            os.chdir(path)
            elements = os.listdir(path)
            # print(elements)
            var_name = folder.split(" ")
            globals()[f"folder_%s" % var_name[0]] = {}
            for element in elements:
                print(element)   
    break

for row in cur.execute('SELECT * FROM drive'):
    print(row)

connection.commit()
connection.close()