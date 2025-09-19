


from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell
dev = Device(host="10.5.13.12", user="", password="")
ss = StartShell(dev)
ss.open()
#ss.run('cli -c "request support information | save /var/tmp/information.txt"')
ver = ss.run('cli -c "show version"')
ss.close()
print(ver)
