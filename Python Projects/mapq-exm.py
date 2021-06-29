import urllib.parse
import requests
import json


def user_input():
    start = input("Please enter your starting location: ")
    stop = input("Please enter your destination location: ")
    return start,stop

def create_url (type,source,destination):
    api_url = "http://www.mapquestapi.com/directions/v2/"+type+"?"
    key = "AjzeQ5qduyDGgcIO32V6bL6BPKqkBqO3"
    url = api_url + urllib.parse.urlencode({"key":key,"from":source,"to":destination})
    return url

def mapquest_reply(url):

    reply = requests.get(url)
    reply_in_json=reply.json()
    return reply_in_json


def main():
   source,destination= user_input()
   types = ["routematrix"]
   for type in types:
       if type == "optimizedroute":
           way = "optimized route"
       elif type == "alternateroutes":
           way = "alternate route"
       else: 
           way = "route"
       url=create_url(type,source,destination)    
       map_reply = mapquest_reply(url)

       print(json.dumps(map_reply,indent=4))
       '''
       distance = map_reply["route"]["distance"]
       
       print("your distance for your {} is {}km".format(way,int(distance*1.61)))

    
       detail_man = input("do you want to see detiled instruction?\n(yes/no)>")
       if detail_man == "yes":
           maneuvers = map_reply["route"]["legs"][0]["maneuvers"]
           for maneuver in maneuvers:
               print("{}({:.2f}km)".format(maneuver["narrative"],(maneuver["distance"]*1.61)))
            
'''

if __name__== main():
    main()
