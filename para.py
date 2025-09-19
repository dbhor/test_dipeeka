import paramiko
from pprint import pprint
import time
ssh_client = paramiko.SSHClient()
print('Connecting to 10.5.73.12')
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#next line is connecting to Junos device, with plain text password.
ssh_client.connect(hostname = '10.5.73.12', port = 22 , username='' , password= '', look_for_keys=False, allow_agent=False)
shell = ssh_client.invoke_shell()
shell.send('show ospf neighbor\n')
time.sleep(1)
output = shell.recv(10000)
pprint(output.decode())

with open('backup.txt', 'wb')as f:
    f.write(output)

if ssh_client.get_transport().is_active() == True:
    print('closing connection')

