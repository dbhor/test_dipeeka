from jnpr.junos import Device
from pprint import pprint
devices_ip = ["10.5.3.82"]
for dev_ip in devices_ip:
    dev = Device(host=dev_ip, user="",password="",gather_facts=True)
    dev.open()
    dev.timeout = 60
    facts = dev.facts
    print("collecting version from device {}".format(dev_ip))
    pprint(dev.facts['version'])





