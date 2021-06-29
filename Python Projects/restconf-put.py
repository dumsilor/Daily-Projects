import requests
import json
requests.packages.urllib3.disable_warnings()


header={
    "Content-type":"application/yang-data+json",
    "Accept":"application/yang-data+json"
}


url = "https://192.168.1.7/restconf/data/ietf-interfaces:interfaces/interface=Loopback100"

basic_auth = ("cisco","cisco123!")

yangConfig = {
    "ietf-interfaces:interface": {
        "name": "Loopback100",
        "description": "Loopback using RestConf",
        "type":"iana-if-type:softwareLoopback",
        "enabled":True,
        "ietf-ip:ipv4":{
            "address": [
                {
                "ip": "10.10.10.2",
                "netmask":"255.255.255.0"
                }
            ]
        },
        "ietf-ip:ipv6": {}
    }

}

resp = requests.put(url, data=json.dumps(yangConfig),
                    auth=basic_auth, headers=header, verify=False)


if (resp.status_code>=200 and resp.status_code<=299):
    print("STATUS OK: {}".format(resp.status_code))
else:
    print('Error. Staus Code : {} \nErrormessage: {}'.format(resp.status_code,resp.json()))


api_url = "https://192.168.1.7/restconf/data/ietf-interfaces:interfaces"

resp = requests.get(api_url,auth=basic_auth,headers=header,verify=False)

json_data = resp.json()

print(json.dumps(json_data,indent=4))
