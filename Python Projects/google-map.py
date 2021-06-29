#Google Map API use kore distance and direction
#Docker e integrate korte hobe
#manirul@aiub.edu
'''
1. Direction API
2. Develop a python application
3. Deploy the configuration in docker container
submit:
1. py file submit
2. Dockerfile submit
3. Screen shot of the application running in Docker Container
4. DevNet B1 Skill Exam
'''

import urllib.parse
import json
import requests
import xml.dom.minidom


api_key="AIzaSyCu-fZZl-qUzEUvtSyQKSL-iVv4uJwCsWE"

api_url = "https://maps.googleapis.com/maps/api/directions/json?"


origin = "mirpur"
destination="gulshan-1"

url = api_url + urllib.parse.urlencode({"origin":origin,"destination":destination,"key":api_key})

reply = requests.get(url).json()
print(json.dumps(reply))
