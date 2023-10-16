def get_re_info(rsi):
    re_info = {}
    re_info_command = re.compile(r"^(.+) show chassis routing-engine no-forwarding$")
    slot_pattern = re.compile(r"^\s+Slot (\d):$")
    current_state = re.compile(r"^\s+Current state\s+(\S+)$")
    temp = re.compile(r"^\s+Temperature\s+(\d+) degrees.*$")
    cpu_temp = re.compile(r"^\s+CPU temperature\s+(\d+) degrees.*$")
    mem_util = re.compile(r"^\s+Memory utilization\s+(\d+) percent$")
    start_time = re.compile(r"^\s+Start time\s+(.*)$")
    with open(rsi) as input_file:
        for line in input_file:
            if re_info_command.match(line):
                cli_prompt_pattern = re.compile(str(re_info_command.search(line).group(1)))
                line = input_file.readline()
                slot = '0'
                while not (cli_prompt_pattern.match(line)):
                    if slot_pattern.match(line):
                        slot = slot_pattern.search(line).group(1)
                        if not (slot in re_info.keys()):
                            re_info[slot] = {}
                    if current_state.match(line):
                        re_info[slot]['current_state'] = current_state.search(line).group(1)
                    if temp.match(line):
                        re_info[slot]['temp'] = temp.search(line).group(1)
                    if cpu_temp.match(line):
                        re_info[slot]['cpu_temp'] = cpu_temp.search(line).group(1)
                    if mem_util.match(line):
                        re_info[slot]['mem_util'] = mem_util.search(line).group(1)
                    if start_time.match(line):
                        re_info[slot]['start_time'] = start_time.search(line).group(1)
                    line = input_file.readline()
                break
    return re_info
