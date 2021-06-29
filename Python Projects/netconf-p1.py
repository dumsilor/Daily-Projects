import re
from ncclient import manager
import xml.dom.minidom


header = manager.connect(
    host = "192.168.1.13",
    port=830,
    username = "cisco",
    password = "cisco123!",
    hostkey_verify = False
)

reply = header.get_config(source="running")
pretty_xml = xml.dom.minidom.parseString(reply.xml).toprettyxml()

from ncclient import manager
import xml.dom.minidom

header = manager.connect(
    port = 830,
    host="192.168.1.13",
    username = "cisco",
    password = "cisco123!",
    hostkey_verify = False
)


interface_filter = '''
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
        </interface>
    </native>
</filter>
'''

router_response = header.get_config(source="running",filter=interface_filter)
pretty_xml = xml.dom.minidom.parseString(router_response.xml).toprettyxml()

print(pretty_xml)



import ncclient
import xml.dom.minidom

head = ncclient.manager.connect (
    port=830,
    host = "192.168.1.13",
    username = "cisco",
    password = "cisco123!",
    hostkey_verify = False
)

create_lo = '''
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>1</name>
                <description>Test</description>
                
                <ip>
                <address>
                <primary>
                    <address>10.10.10.10</address>
                    <mask>
                    255.255.255.255
                    </mask>
                </primary>
                </address>
                </ip>
                
                
            </Loopback>
        </interface>
    </native>
</config>
'''


rotuer_conf_ch = head.edit_config(target="running",config=create_lo)
check_config = header.get_config(source="running",filter=interface_filter)

print(xml.dom.minidom.parseString(check_config.xml).toprettyxml())
