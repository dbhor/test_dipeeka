from jnpr.junos import Device
import re
import argparse
import datetime
from pprint import pprint


def get(fname):
    show_command = "show chassis hardware detail"


    with open(fname)as f:
        for line in f:
            content = f.readlines()
            print(content)
            print(len(content))
            for i in range(len(content)):
                if show_command in content[i]:
                    print("inside")
                    print(content[i])
                    print(i)
                    i = i+2
                    print(content[i])
                    cli_pattern = "root@re0.HYWRWIIO1CW>"
                    if cli_pattern in content[i]:
                        """print(content[i:len(content)])"""
                        """output=''.join(content[i:len(content)])"""
                        """print(output)"""
                        print("you are in last if")
                        break




                    """
                    if cli_pattern in content[i]:
                        continue

                    while cli_pattern not in content[i]:
                        print(content[i:len(content)])"""








get("rsi.text")