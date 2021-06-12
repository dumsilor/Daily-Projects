import urllib.parse
import requests

url_main = "https://www.mapquestapi.com/directions/v2/route?"

origin = "mirpur"
destination = "shahjadpur"
key = "AjzeQ5qduyDGgcIO32V6bL6BPKqkBqO3"


url = url_main + urllib.parse.urlencode({"key":key, "from":origin, "to":destination})

json_data = requests.get(url).json()

print ("URL: " + url)

json_status = json_data["info"]["statuscode"]

if json_status == 0:
    print("API Status: " + str(json_status)+ " = A successfull route call.\n")