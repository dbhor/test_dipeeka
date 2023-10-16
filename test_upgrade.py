>>> from jnpr.junos import Device
>>> from pprint import pprint
>>> devices_ip = ["10.85.173.182", "10.85.173.152"]
>>> for dev_ip in devices_ip:
...     dev = Device(host=dev_ip, user="labroot",password="lab123",gather_facts=True)
...     dev.open()
...     dev.timeout = 60
...     facts = dev.facts
...     print("collecting version from device {}".format(dev_ip))
...     pprint(dev.facts['version'])
... 
Device(10.85.173.182)
collecting version from device 10.85.173.182
'16.1R6-S3.1'
Device(10.85.173.152)
collecting version from device 10.85.173.152
'16.1X8'
