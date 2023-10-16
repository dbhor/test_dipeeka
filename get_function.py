def get_pfe_traffic_stats(rsi):
    traffic_stats = {}
    traffic_stats_command = re.compile(r"^(.+) show pfe statistics traffic$")
    drop_counters = ['Software input control plane drops']
    with open(rsi) as input_file:
        for line in input_file:
            if traffic_stats_command.match(line):
                cli_prompt_pattern = re.compile(str(traffic_stats_command.search(line).group(1)))
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


def compare_pfe_traffic_stats(previous, current):
    print("\nPFE Traffic Statistics comparison:\n")
    counters = previous.keys()
    difference_seen = False
    for counter in counters:
        if int(previous[counter]) < int(current[counter]):
            print_red(
                f"Value of counter \"{counter}\" has increased. Current: {current[counter]} Previous:{previous[counter]}")
            difference_seen = True
        elif int(previous[counter]) > int(current[counter]):
            print_red(
                f"Value of counter \"{counter}\" has decreased. Current: {current[counter]} Previous:{previous[counter]}")
            difference_seen = True
    if not difference_seen:
        print_green("No difference seen in previous and current PFE traffic stats.")
