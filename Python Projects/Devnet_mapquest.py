import urllib.parse
import requests
import json

def create_url(req_url,key,start,to):
    url = req_url + urllib.parse.urlencode({"key":key, "from":start, "to":to}) #"unit":unit, "routeType":route_type})
    return url



def route_output(main_url, key, start, to,routing_type):
    if routing_type == "route":
        route_url = main_url+"route?"
    elif routing_type == "optimize":
        route_url = main_url + "optimizedroute?"
    elif routing_type == "alternate?":
        route_url = main_url+"alternateroutes"

    url = create_url(route_url, key, start, to)
    data = requests.get(url).json()
    return data,url
    
def parse_json (json_data):
    distance = json_data["route"]["distance"]
    pretty_json = json.dumps(json_data,indent=4,sort_keys=True)
    return distance

def main():
    main_url = "http://www.mapquestapi.com/directions/v2/"
    key = "AjzeQ5qduyDGgcIO32V6bL6BPKqkBqO3"
    start = input("Please enter a destination location: ")
    to = input("please enter starting location: ")
    routing_number = input("enter routing type:\n1.normal route\n2.optimized route\n3.Alternet route\n>")
    if routing_number == "1":
        routing_type = "route"
    elif routing_number == "2":
        routing_type = "optimize"
    elif routing_number == "3":
        routing_type="alternate"
    data = route_output(main_url, key, start, to, routing_type)
    parsed_data = parse_json(data[0])
    print(parsed_data)


if __name__ ==  "__main__":
    main()
