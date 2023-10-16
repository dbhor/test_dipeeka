from jnpr.junos import Device
import re
import argparse
import datetime


def get_pfe_traffic_stats(fname):
    traffic_stats = {}
    traffic_stats_command = re.compile(r"^(.+) show pfe statistics traffic$")
    drop_counters = ['Software input control plane drops']
    with open(fname) as input_file:
        for line in input_file:
            if traffic_stats_command.match(line):
                cli_prompt_pattern = re.compile(traffic_stats_command.search(line))
                print(cli_prompt_pattern)
                line = input_file.readline()
                while not (cli_prompt_pattern.match(line)):
                    for counter in drop_counters:
                        if re.match("\s+" + counter + "\s+:\s+(\d+)", line):
                            traffic_stats[counter] = re.search("\s+" + counter + "\s+:\s+(\d+)", line).group(1)
                            drop_counters.remove(counter)
                            break
                    line = input_file.readline()
                break
    return traffic_stats



