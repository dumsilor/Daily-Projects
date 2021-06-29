import time
import os

t=0
while (t < 120):

    time.sleep(15)
    browserExe = "chrome.exe"
    os.system("taskkill /f /im "+browserExe)
    t+=1
