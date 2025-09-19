import jnpr.junos
from jnpr.junos import Device
from lxml import etree
dev = Device(host="10.85.173.182", user="", password="")
dev.open()
rsp = dev.rpc.get_interface_information(terse=True,interface_name='ae201')
print(etree.tostring(rsp))
