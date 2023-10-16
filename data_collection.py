
from pprint import pprint
from lxml import etree
from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import *
import argparse
from jnpr.junos.utils.start_shell import StartShell
import time
import getpass


start_time = time.time()

#hostname=input("Enter router name:  ")
#username=input("Enter your SSH username:  ")
#password=getpass.getpass()

fpc_numbers=[0,1]

time_start = time.time()

DEV = Device(host="10.85.173.182", user="labroot", password="lab123")
ss = StartShell(DEV)
ss.open()
DEV.open()
pprint(ss.run('cli -c "set cli timestamp"'))
for fpc_number in fpc_numbers:
    pprint(ss.run('cprod -A fpc{} -c "show route summary"'.format(fpc_number)))
    pprint(ss.run('cprod -A fpc{} -c "show pfe statistics traffic"'.format(fpc_number)))
    pprint(ss.run('cprod -A fpc{} -c "show nhdb summary"'.format(fpc_number)))
    pprint(ss.run('cprod -A fpc{} -c "show sched"'.format(fpc_number)))
    pprint(ss.run('cprod -A fpc{} -c "show nvram"'.format(fpc_number)))
    pprint(ss.run('cprod -A fpc{} -c "show syslog messages"'.format(fpc_number)))

print("Completed data collection in %f sec." % (time.time() - time_start))

ss.close()
DEV.close()
