import pexpect
import re
import json
import time
import requests
from threading import Thread
import matplotlib.pyplot as plt
import datetime
import urllib3
import coloredlogs, logging
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def dev_handle(nxt_srv, **input):
    if "yes" in input['jump_server'].lower():
        js_ip = input['js_ip']
        js_user = input['js_user']
        js_passwd = input['js_password']
        ssh = pexpect.spawn('ssh {}@{}'.format(js_user, js_ip), env = {"TERM": "dumb"})
        ret = ssh.expect(['\?','assword:'])
        if ret == 0:
            ssh.sendline('yes')
            ret = ssh.expect('assword:')
            if ret == 0:
                ssh.sendline(js_passwd)
                ret = ssh.expect('%')
                ssh.sendline('\n')
        elif ret == 1:
            ssh.sendline(js_passwd)
            ret = ssh.expect('%')
            ssh.sendline('\n')
    if nxt_srv == 0:
        var = "dev"
    else:
        var = "nxt_srv"
    dev_ip = input['{}_ip'.format(var)]
    dev_user = input['{}_user'.format(var)]
    dev_password = input['{}_password'.format(var)]
    print("getting device ssh handle for {}, {}".format(dev_user, dev_ip))
    ssh.sendline('ssh {}@{}'.format(dev_user, dev_ip))
    ret = ssh.expect(['/?', 'assword:'])
    if ret == 0:
        ssh.sendline('yes')
        ret = ssh.expect('assword:')
        if ret == 0:
            ssh.sendline(dev_password)
            ssh.expect('%')
            ssh.sendline('cli')
            ret = ssh.expect('>')
            if ret == 0:
                return ssh
    elif ret == 1:
        ssh.sendline(dev_password)
        ssh.expect('%')
        ssh.sendline('cli')
        ret = ssh.expect('>')
        if ret == 0:
            return ssh

def dev_monitoring_type(server):
    agent_type = 'Event_Script'
    ssh = dev_handle(nxt_srv=0, **server)
    ssh.sendline('show configuration | grep daemon | display set')
    ssh.expect('>')
    ping_res = ssh.before
    print(ping_res)
    out = ping_res.decode('utf-8')
    print(out)
    ssh.sendline('show chassis routing-engine | match idle')
    ssh.expect('>')
    ping_res = ssh.before
    print("this is ", ping_res)
    out1 = ping_res.decode('utf-8')
    print("this",out1)
    ping_after= ssh.after
    print("this is after", ping_after)
    ssh.sendline('file show /var/tmp/mxoc_agentd.conf')
    ssh.expect('>')
    ping_res = ssh.before
    out2 = ping_res.decode('utf-8')
    if re.search("daemonize", out):
        if re.search("mxoc_agentd", out1) and re.search("outbound_ssh", out2):
            agent_type = 'PyAgent'
        elif re.search("mxoc_agentd", out1) and re.search("mxoc_notifier", out1) and re.search("netconf", out2):
            agent_type = 'PyAgent_V2'
    return agent_type


def read_input(file_name= 'Server_Details.json'):
    with open(file_name)as input_file:
        input_json = json.load(input_file)
        return(input_json)

if __name__ == '__main__':
    start = time.time()
    input = read_input()
    print("Received input : {}".format(input))

    for x in input['server_details']:
        server = input['server_details'][x]
        event_int = int(server['event_time_interval'])
        dev_name = server['mist_dev_name']
        mon_method = dev_monitoring_type(server)
        print(mon_method)
