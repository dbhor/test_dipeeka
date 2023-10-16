from jnpr.junos import Device
import xml.etree.ElementTree as ET
dev= Device(host="10.85.173.182", user="labroot", password="lab123")
dev.open()
port_output= dev.rpc.get_interface_information()
print(ET.tostring(port_output, encoding = "utf8", method= 'text'))
dev.close()

