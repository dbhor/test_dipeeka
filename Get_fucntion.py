import re
def get_interface_stats(rsi):
    interface_stats = {}
    interface_stats_seen = False
    interface_stats_command = re.compile(r"^(.+) show interfaces extensive no-forwarding$")
    cli_prompt = ""
    interface_header_pattern = re.compile(r"Physical interface: ((\D{2})-\d{1,2}\/\d{1,2}\/\d{1,2}),\s*(.*),\s*(.*)")
    interface_header_generic = re.compile(r"Physical interface:.*")
    last_flap_pattern = re.compile(r"\s+Last flapped\s+:\s+(.*)\s+\(.*ago\)")
    input_error_pattern = re.compile(r"\s*Errors: (\d*), Drops: (\d*), Framing errors: (\d*), Runts: (\d*), Policed discards: (\d*), L3 incompletes: (\d*), L2 channel errors: (\d*), L2 mismatch timeouts: (\d*), FIFO errors: (\d*), Resource errors: (\d*)")
    output_error_pattern = re.compile(r"\s*Carrier transitions: (\d*), Errors: (\d*), Drops: (\d*), Collisions: (\d*), Aged packets: (\d*), FIFO errors: (\d*), HS link CRC errors: (\d*), MTU errors: (\d*), Resource errors: (\d*)")
    queue_drops_pattern = re.compile(r"^\s+(\d)\s+\d+\s+\d+\s+(\d+)$")
    bit_errors_pattern = re.compile(r"^\s+Bit errors\s+(\d+)$")
    errored_blocks_pattern = re.compile(r"^\s+Errored blocks\s+(\d+)$")
    input_bps = re.compile(r"\s+Input\s+bytes\s+\:\s+\d+\s+(\d+)\s+bps")
    output_bps = re.compile(r"\s+Output\s+bytes\s+\:\s+\d+\s+(\d+)\s+bps")
    with open(rsi) as input_file:
        line = input_file.readline()
        while line:
            if interface_stats_command.match(line):
                interface_stats_seen = True
                cli_prompt = str(interface_stats_command.search(line).group(1))
                break
            line = input_file.readline()
        cli_prompt_pattern = re.compile(cli_prompt)
    if interface_stats_seen:
            line = input_file.readline()
            while line:
                if cli_prompt_pattern.match(line):
                    break
                if interface_header_pattern.match(line):
                    if str(interface_header_pattern.search(line).group(2)) in interface_types:
                        current_interface = str(interface_header_pattern.search(line).group(1))
                        interface_stats[current_interface] = {}
                        if 'Enabled' in str(interface_header_pattern.search(line).group(3)):
                            interface_stats[current_interface]['admin_status'] = True
                        else:
                            interface_stats[current_interface]['admin_status'] = False
                        if 'Up' in str(interface_header_pattern.search(line).group(4)):
                            interface_stats[current_interface]['link_status'] = True
                        else:
                            interface_stats[current_interface]['link_status'] = False
                        line = input_file.readline()
                        file_pointer = 0
                        while not (interface_header_generic.match(line)):
                            if last_flap_pattern.match(line):
                                interface_stats[current_interface]['last_flap'] = str(last_flap_pattern.search(line).group(1))
                                if input_error_pattern.match(line):
                                    interface_stats[current_interface]['input_errors'] = {}
                                interface_stats[current_interface]['input_errors']['total_errors'] = str(input_error_pattern.search(line).group(1))
                                interface_stats[current_interface]['input_errors']['drops'] = str(input_error_pattern.search(line).group(2))
                                interface_stats[current_interface]['input_errors']['framing_errors'] = str(
                                    input_error_pattern.search(line).group(3))
                                interface_stats[current_interface]['input_errors']['runts'] = str(
                                    input_error_pattern.search(line).group(4))
                                interface_stats[current_interface]['input_errors']['policed_discards'] = str(
                                    input_error_pattern.search(line).group(5))
                                interface_stats[current_interface]['input_errors']['l3_incompletes'] = str(
                                    input_error_pattern.search(line).group(6))
                                interface_stats[current_interface]['input_errors']['l2_channel_errors'] = str(
                                    input_error_pattern.search(line).group(7))
                                interface_stats[current_interface]['input_errors']['l2_mismatch_timeouts'] = str(
                                    input_error_pattern.search(line).group(8))
                                interface_stats[current_interface]['input_errors']['fifo_errors'] = str(
                                    input_error_pattern.search(line).group(9))
                                interface_stats[current_interface]['input_errors']['resource_errors'] = str(
                                    input_error_pattern.search(line).group(10))
                            if output_error_pattern.match(line):
                                interface_stats[current_interface]['output_errors'] = {}
                                interface_stats[current_interface]['output_errors']['carrier_transitions'] = str(
                                    output_error_pattern.search(line).group(1))
                                interface_stats[current_interface]['output_errors']['errors'] = str(
                                    output_error_pattern.search(line).group(2))
                                interface_stats[current_interface]['output_errors']['drops'] = str(
                                    output_error_pattern.search(line).group(3))
                                interface_stats[current_interface]['output_errors']['collisions'] = str(
                                    output_error_pattern.search(line).group(4))
                                interface_stats[current_interface]['output_errors']['aged_packets'] = str(
                                    output_error_pattern.search(line).group(5))
                                interface_stats[current_interface]['output_errors']['fifo_errors'] = str(
                                    output_error_pattern.search(line).group(6))
                                interface_stats[current_interface]['output_errors']['crc_errors'] = str(
                                    output_error_pattern.search(line).group(7))
                                interface_stats[current_interface]['output_errors']['mtu_errors'] = str(
                                    output_error_pattern.search(line).group(8))
                                interface_stats[current_interface]['output_errors']['resource_errors'] = str(
                                    output_error_pattern.search(line).group(9))
                            if queue_drops_pattern.match(line):
                                if not ('queue_drops' in interface_stats[current_interface].keys()):
                                    interface_stats[current_interface]['queue_drops'] = {}
                                interface_stats[current_interface]['queue_drops'][
                                    queue_drops_pattern.search(line).group(1)] = queue_drops_pattern.search(line).group(
                                    2)
                            if bit_errors_pattern.match(line):
                                interface_stats[current_interface]['bit_errors'] = bit_errors_pattern.search(
                                    line).group(1)
                            if errored_blocks_pattern.match(line):
                                interface_stats[current_interface]['errored_blocks'] = errored_blocks_pattern.search(
                                    line).group(1)
                            if input_bps.match(line):
                                if not ('traffic_rate' in interface_stats[current_interface].keys()):
                                    interface_stats[current_interface]['traffic_rate'] = {}
                                input_gbps = round(float(int(input_bps.search(line).group(1)) / (1024 * 1024 * 1024)),
                                                   3)
                                interface_stats[current_interface]['traffic_rate']['input'] = str(input_gbps)
                            if output_bps.match(line):
                                if not ('traffic_rate' in interface_stats[current_interface].keys()):
                                    interface_stats[current_interface]['traffic_rate'] = {}
                                output_gbps = round(float(int(output_bps.search(line).group(1)) / (1024 * 1024 * 1024)),
                                                    3)
                                interface_stats[current_interface]['traffic_rate']['output'] = str(output_gbps)
                            file_pointer = input_file.tell()
                    line = input_file.readline()
                    if file_pointer != 0:
                            input_file.seek(file_pointer)
                line = input_file.readline()
    return interface_stats