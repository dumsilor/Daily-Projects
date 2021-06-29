import urllib.parse
import requests
import json

url = "http://www.mapquestapi.com/directions/v2/route?"

starting_point = "dhaka"
ending_point = "Shihezi"
key = "AjzeQ5qduyDGgcIO32V6bL6BPKqkBqO3"

api_url = url + urllib.parse.urlencode({"key":key,"from":starting_point,"to":ending_point})

resp = requests.get(api_url).json()

total_distance = resp["route"]["distance"]

print("You start from: " + starting_point)
print("Your destination: " + ending_point)
print("Total distnace: " , total_distance , "miles (" , float(total_distance)*1.60934 , "km)")
