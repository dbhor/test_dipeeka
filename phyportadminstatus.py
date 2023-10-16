from jnpr.junos.op.phyport import *
from jnpr.junos import Device

dev= Device(host="10.85.173.182", user="labroot", password="lab123")
dev.open()
ports = PhyPortTable(dev).get()
print(ports.key)
print(ports.values())
#for item in ports:
#if item.oper == "down":
#print("the port " + item.key + " is down")