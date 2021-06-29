import webbrowser

url_lines= []

with open("ulrs.txt","r") as urls:
    lines=urls.read()
    url_lines=lines.split("\n")


for line in url_lines:
    url = line
    chrome_path = "C:/Program Files (x86)/Google//Chrome/Application/chrome.exe %s"
    webbrowser.get(chrome_path).open(url)
    


