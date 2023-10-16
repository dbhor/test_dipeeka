import time
from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetmikoTimeoutException
from netmiko.ssh_exception import NetmikoAuthenticationException




def enable_netconf(net_device):
    print("{} Connecting to {}".format(time.asctime(),net_device['ip']))
    junos_device = ConnectHandler(**net_device)
    configure= junos_device.config_mode()
    print("{} Applying config to {}".format(time.asctime(), net_device['ip']))
    sendcommand= junos_device.send_command("set system services netconf ssh")
    print("{} Committing the config of netconf on {}".format(time.asctime(),net_device['ip']))
    junos_device.commit(comment='enable netconf ssh on device', and_quit=True)
    print("{} Closing the connection to device {}".format(time.asctime(), net_device['ip']))
    junos_device.disconnect()

def main():
    user_login = input("enter username:")
    user_pass = getpass("Enter password")
    with open("inventory.txt")as f:
        device_list=f.read().splitlines()
        for device in device_list:
             net_device = {'device_type':'juniper', 'ip': device, 'username':user_login ,'password':user_pass}
        enable_netconf(net_device)

if __name__=='__main__':
    main()