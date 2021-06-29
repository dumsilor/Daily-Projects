import json
import requests
requests.packages.urllib3.disable_warnings()

api_url = "https://192.168.1.7/restconf/d"

header ={
    "Accept": "application/yang-data+json",
    "Content-type":"application/yang-data+json"
}

basic_auth = ("cisco","cisco123!")

resp = requests.get(api_url,auth=basic_auth,headers=header,verify=False)

response_json = resp.json()
print(json.dumps(response_json,indent=4))
