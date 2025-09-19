from jnpr.junos import Device
import xml.etree.ElementTree as ET
dev= Device(host="10.5.3.2", user="", password="")
dev.open()
port_output= dev.rpc.get_interface_information()
print(ET.tostring(port_output, encoding = "utf8", method= 'text'))
dev.close()

