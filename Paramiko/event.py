###### event script is on springdawn.ultralab.juniper.net. 
% cat
LACP_FLAP.py
# !/usr/bin/python
#
# Copyright (c) 2019, Juniper Networks Inc.
#
# All rights reserved.
#

# Based on receiving an event configured for an event policy, following
# script will be triggered.

"""
Since this is a Python event Script.
The Following config needs to be loaded on the system prior to triggering
save file under /var/db/scripts/event/
set event-options max-policies 2
set event-options policy LACP_FLAP events lacpd_timeout
set event-options policy LACP_FLAP then event-script LACP_FLAP.py output-filename LACP_FLAP_OUTPUT
set event-options policy LACP_FLAP then event-script LACP_FLAP.py destination local-flash
set event-options policy LACP_FLAP then event-script LACP_FLAP.py output-format text
set event-options event-script file LACP_FLAP.py python-script-user remote
set event-options destinations local-flash archive-sites /var/tmp/
set event-options event-script file LACP_FLAP.py python-script-user remote
set system scripts language python

set system scripts op file LACP_FLAP.py
save file under /var/db/scripts/op/

"""

from jnpr.junos import Device
from jnpr.junos.utils.start_shell import StartShell
from junos import Junos_Trigger_Event
from datetime import datetime, timedelta
# from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import os
import re
import time

Debug_Mode = True

try:
    os.mkdir("/var/tmp/script_outputs")
except:
    pass
    if (Debug_Mode): print('Script Directory already existed')

Date = datetime.today().strftime("%Y%m%d%H%M%S")
# Path = os.getcwd() + "/{}/".format(Date)
Path = "/var/tmp/script_outputs/{}/".format(Date)
if (Debug_Mode): print(Path)
# os.mkdir(Path)

try:
    os.mkdir(Path)
except:
    if (Debug_Mode): print('Directory already existed')
    pass


def document_InTextfile(command, Data):
    try:
        with open(Path + 'LACP_FLAP_OUTPUT' + Date + '.txt', 'a') as file:
            file.write('\n' + datetime.now().strftime("%b %d %H:%M:%S") + '\n')
            file.write(" :----->" + command + '\n' + Data + '\n\n\n')
    except:
        print('LACP_FLAP_OUTPUT' + ": " + " :----->\n" + Data)
        # print('**Failed to create text file output for {}'.format(ERO))


if __name__ == '__main__':

    for Iteration in range(0, 240):
        command = 'cprod -A fpc0 -c "show pechip trapstats"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show shim jnh reject stats"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show shim jnh discard stats"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show shim pfe statistics traffic"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show pfe statistics notification"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show shim jnh discard dev 0"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show shim jnh discard dev 1"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show shim jnh discard dev 2"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show shim jnh discard dev 3"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show shim jnh discard dev 4"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show shim jnh discard dev 5"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show mtip-xgmac 0 statistics"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show mtip-xgmac 1 statistics"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show mtip-xgmac 2 statistics"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show mtip-xgmac 3 statistics"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show mtip-xgmac 4 statistics"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show mtip-xgmac 5 statistics"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show lacp timeouts'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show lacp statistics interfaces'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show lacp interfaces extensive'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show ppm connection-queue'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show ppm connections'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show ppm distribution-statistics'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show ppm event-statistics'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show ppm ifl-statistics'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show ppm mem-statistics'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show ppm packet-statistics'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show ppm packet-statistics packet recv'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show ppm packet-snapshot'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show ppm request-queue detail'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show ppm rpc-statistics'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show ppm rules'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show ppm transmissions'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show system processes extensive'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show chassis fpc'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cli show ddos-protection protocols'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show ppm statistics"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show ppm statistics detail"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show ppm statistics protocol lacp"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show ppm adjacencies protocol lacp"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show ppm transmits protocol lacp"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show ttp statistics"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show ukern_trace <>"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show sched"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show threads"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show threads cpu"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show expr-if host stats"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show pechip interrupt"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show pechip trapstats"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        command = 'cprod -A fpc0 -c "show ddos policer all stats"'
        output = os.popen(command).read()
        document_InTextfile(command, output)

        time.sleep(5) %