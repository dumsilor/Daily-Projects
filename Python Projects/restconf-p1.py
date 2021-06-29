import requests
import json
requests.packages.urllib3.disable_warnings()

header = {
    "content-type":"application/yang-data+json",
    "Accept":"application/yang-data+json"
}

url = "https://sandbox-iosxe-latest-1.cisco.com/restconf/data/Cisco-IOS-XE-native:native/"
basic_auth = ("developer", "C1sco12345")
print(url)

router_reply = requests.get(url,auth=basic_auth,headers=header,verify=False).json()
print(router_reply)
print(json.dumps(router_reply,indent=4))
