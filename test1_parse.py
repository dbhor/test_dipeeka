from jnpr.junos import Device
import re
import argparse
import datetime
from pprint import pprint
def get_show(fname):
    x = False
    show_command = "show chassis hardware detail no-forwarding"
    with open(fname)as f:
        for line in f:
            if show_command in line:
                x = True
                print(line)
            if(x == True):
                cli_pattern = "root@re0.HYWRWIIO1CW>"
                if cli_pattern not in line:
                    print("we are in if")
                    print(line)
                else:
                    print("we are in else")
                    x = False



get_show("rsi.text")

