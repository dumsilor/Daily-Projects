import os
import shutil

target = input("Enter your path: ")
dst = input("Enter your destination: ")
extention  = input("enter file extension: ")
searchWord = input("enter keyword: ")
# os.chdir("C:\\Users\\rashi\Downloads\\")
os.chdir(target)
cwd = os.getcwd()
files = os.listdir(cwd)

for file in files:
    if (searchWord.upper()) in file or (searchWord.lower()) in file or (searchWord.capitalize()) in file and ("."+extention) in file:
        current_path = cwd + "\\" + file
        dest_path =  dst + "\\" + file
        #print()
        shutil.move(current_path,dest_path)
        print("Moved= " + file)

