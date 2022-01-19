from genericpath import isfile
import os
import string
import re

available_drives = []
files = {}
folders = {}
file_list = []
folder_list = []

for d in string.ascii_uppercase:
    if os.path.exists('%s:' % d):
     available_drives.append('%s:' % d)


for drive in available_drives:
    os.chdir(drive+"\\")
    files[drive] = None
    elements = os.listdir(drive)
    # print(elements)
    for element in elements:
        if isfile(element):
            # print(drive + "\\" + element + " is a file")
            file_list.append(element)
            files[drive] = file_list
        # print(drive + "\\" + element)
        else:
            # print(drive + "\\" + element + " is not a file")
            match = re.search(r"^\$", element)
            msi_match = re.search(r"[A-Za-z]*[\.Msi]$", element)
            tmp_match = re.search(r"[A-Za-z]*[\.tmp]$", element)
            sys_match = re.search(r"^System Volume Information$",element)
            rec_match = re.search(r"^Recovery$", element)
            if match or msi_match or tmp_match or sys_match or rec_match:
                continue
            else:
                folder_list.append(element)
                folders[drive] = folder_list
 

print(files)

