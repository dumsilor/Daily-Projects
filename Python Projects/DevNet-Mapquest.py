import urllib.parse
import requests

url_main = "https://www.mapquestapi.com/directions/v2/route?"
orgin = "Gulshan-1"
destinatio = "Mirpur"
key="AjzeQ5qduyDGgcIO32V6bL6BPKqkBqO3"


url = url_main + urllib.parse.urlencode({"key":key, "from":orgin, "to":destinatio})

json_data = requests.get(url).json()
print(json_data)

