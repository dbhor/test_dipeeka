


from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell
dev = Device(host="10.85.173.182", user="labroot", password="lab123")
ss = StartShell(dev)
ss.open()
#ss.run('cli -c "request support information | save /var/tmp/information.txt"')
ver = ss.run('cli -c "show version"')
ss.close()
print(ver)