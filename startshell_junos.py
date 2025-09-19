from jnpr.junos import Device
from jnpr.junos.utils.fs import FS
from jnpr.junos.utils.start_shell import StartShell
from jnpr.junos.utils.scp import SCP
dev = Device(host="10.6.3.2", user="", password= "")
dev.open()
ss= StartShell(dev)
ss.open()
ss.run('cli -c "show route summary | no-more"')
ss.close()



