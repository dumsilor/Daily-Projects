import urllib.parse
import requests
import json

def route_matrix(key):
    url = "http://www.mapquestapi.com/directions/v2/routematrix?"
    api_url = url + urllib.parse.urlencode({"key":key})
    locations='{"locations":["new york","jersey city","dallas"]}'
    api_body = json.loads(locations)
    reply = requests.get(api_url,data=locations).json()
    pretty_reply = json.dumps(reply,indent=4)
    return pretty_reply

def normal_route(key):
    source = "new york"
    dest = "jersey city"
    url = "http://www.mapquestapi.com/directions/v2/route?"
    api_url = url + \
        urllib.parse.urlencode({"key": key, "from": source, "to": dest})
    reply = requests.get(api_url).json()
    session = reply["route"]["sessionId"]
    pretty_reply = json.dumps(reply, indent=4)
    return session,pretty_reply

def route_shape(key,session):
    url = "http://www.mapquestapi.com/directions/v2/routeshape?"
    shapes= ["mapState", "fullShape"]
    for shape in shapes: 
      api_url = url + urllib.parse.urlencode({"key": key, "sessionId": session, shape:True})
      reply = requests.get(api_url).json()
      pretty_reply = json.dumps(reply, indent=4)
      return pretty_reply


def main():
    key = "AjzeQ5qduyDGgcIO32V6bL6BPKqkBqO3"
    matrix = route_matrix(key)
    sessionId = normal_route(key)[0]
    route = normal_route(key)[1]
    shape = route_shape(key, sessionId)
    outputs = {"rotue matrix":matrix,"Normal route": route,"Route Shape":shape}
    for k, value in outputs.items():
        print ("######################################################################################################################")
        print("Output of" + k + " is: ")
        print(value)
        print("#######################################################################################################################")

if __name__== main():
    main()
