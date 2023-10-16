import paramiko
import time
import getpass
client = paramiko.SSHClient()
print('Connecting to 10.85.173.197')
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
password = getpass.getpass("Enter a password:")
router = {hostname = '10.85.173.197', port = 22 , username='labroot' , password= password} // created a dictionary object router, which has keys and values.
client.connect( **router, look_for_keys=False, allow_agent=False)
shell = client.invoke_shell()
shell.send('edit')
shell.send('set protocols ospf area 0 interface xe-8/3/3.0\n')
shell.send('commit')
time.sleep(2)
output = shell.recv(10000).decode()
print(output)

if client.get_transport().is_active() == True:
    print('closing connection')
    client.close()
