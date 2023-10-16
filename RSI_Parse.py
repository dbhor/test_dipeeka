from jnpr.junos import Device
import re
import argparse
import datetime
from pprint import pprint


def get(fname):
    show_command = "show chassis hardware detail"
    cli_pattern = "root@re0.HYWRWIIO1CW>"

    with open(fname)as f:
        for line in f:
            content = f.readlines()
            print(content)


            for i in range(len(content)):
                if show_command in content[i]:
                    print("hi")
                    print(content[i])
                    i = i +1

                    while cli_pattern not in content[i]:
                        print(content[i])
                        i = i+1















get("rsi.text")