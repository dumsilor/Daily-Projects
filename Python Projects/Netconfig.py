from ncclient import manager
import xml.dom.minidom

m = manager.connect(
    host="192.168.1.188",
    port=830,
    username="cisco",
    password="cisco123!",
    hostkey_verify = False
)

"""
print("#Supported Capabilites (YANG Model): ")
for capability in m.server_capabilities:
    print(capability)
"""
netconf_hostname = """
<config>
<native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
 <interface>
 <Loopback>
 <name>1</name>
 <description>Loopback for exam</description>
 <ip>
 <address>
 <primary>
 <address>10.1.1.1</address>
 <mask>255.255.255.0</mask>
 </primary>
 </address>
 </ip>
 </Loopback>
 </interface>
</native>
</config>
"""


reply_filter = '''
<filter>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname></hostname>
    </native>
</filter>
'''



ch_hostname = '''
<config>
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>Rashik</hostname>
    </native>
</config>
'''



#reply = m.edit_config(target="running", config=netconf_hostname)
reply  = m.edit_config(target="running", config=netconf_hostname)
print(xml.dom.minidom.parseString(reply.xml).toprettyxml())
reply = m.get_config(source="running",filter=reply_filter)
print(xml.dom.minidom.parseString(reply.xml).toprettyxml())
