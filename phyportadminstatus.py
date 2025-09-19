from jnpr.junos.op.phyport import *
from jnpr.junos import Device

dev= Device(host="10.85.1.82", user="", password="")
dev.open()
ports = PhyPortTable(dev).get()
print(ports.key)
print(ports.values())
#for item in ports:
#if item.oper == "down":
#print("the port " + item.key + " is down")
