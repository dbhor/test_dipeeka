#this script uses paramiko to send show commands to Junos device.
import paramiko
from pprint import pprint
import time
import getpass
ssh_client = paramiko.SSHClient()
print('Connecting to 10.85.173.197')
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
password = getpass.getpass("Enter a password:")
#next line is connecting to Junos device, where it will prompt the user to enter password in secure manner.
ssh_client.connect(hostname = '10.85.173.197', port = 22 , username='labroot' , password= password, look_for_keys=False, allow_agent=False)
shell = ssh_client.invoke_shell()
shell.send('show isis adjacency\n')
time.sleep(1)
output = shell.recv(10000)
pprint(output)
mystr = output.decode(encoding='UTF8')  // decode command is to decode the bytes to string.
print(mystr)

if ssh_client.get_transport().is_active() == True:
    print('closing connection')