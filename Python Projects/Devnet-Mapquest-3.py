import urllib.parse
import requests

url_main = "https://www.mapquestapi.com/directions/v2/route?"

origin = input("Please enter your starting Location: ")
destination = input("Please enter your destination Location: ")
key = "AjzeQ5qduyDGgcIO32V6bL6BPKqkBqO3"

url = url_main + urllib.parse.urlencode({"key":key,"from":origin,"to": destination})
json_data = requests.get(url).json()
json_status = json_data["info"]["statuscode"]

print("URL:" + url+"\n")

if json_status == 0:
    print("Status Code: " + str(json_status) + " = a successful route call\n")


print("======================================================")
print("Destination from " + origin + " to " + destination )
print("Trip Duration: " + str(json_data["route"]["distance"]))
print("======================================================")
