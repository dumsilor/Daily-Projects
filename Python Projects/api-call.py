from librouteros import connect
import json


ip = "163.53.150.254"
user ="admin"
passw = "pr0b3sh-B@r0n"

api = connect(username=user,password=passw,host=ip)
stdout = api(cmd="/interface/print")

for out in stdout:
    print(json.dumps(out,indent=4))
