#Name: Dennis Dam #
#School fleming College#
#Course: Scripting Applications# 
#Assignment: 4#



##(/Users/dennidam/Desktop/Lab-assignment-3-scrpiting-applications-/lab-4-gateway-/gateway.log)##

##### project: writing a python script that process a text file line by line #####



import re
import sys
import os
import csv

def main():
    log_file = get_log_file_path_from_cmd_line()

    # TODO: Step 10 - generate destination port reports provded #
    port_traffic_counts = tally_port_traffic(log_file)
    for port, count in port_traffic_counts.items():
        if count >= 100:
            generate_port_traffic_report(log_file, port)

    # TODO: Step 11 - generate invalid user report
    generate_invalid_user_report(log_file)

    # TODO: Step 12 - generate source IP log
    generate_source_ip_log(log_file, '220.195.35.40')


# TODO: Step 3
def get_log_file_path_from_cmd_line():
    if len(sys.argv) < 2:
        print("Error: Log file path not provided.")
        sys.exit(1)

    log_file = sys.argv[1]
    if not os.path.isfile(log_file):
        print("Error: Log file not found:", log_file)
        sys.exit(1)

    return log_file

# TODO: Steps 4-7
def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False):
    """Gets a list of records in a log file that match a specified regex.

    Args:
        log_file (str): Path of the log file
        regex (str): Regex filter
        ignore_case (bool, optional): Enable case insensitive regex matching. Defaults to True.
        print_summary (bool, optional): Enable printing summary of results. Defaults to False.
        print_records (bool, optional): Enable printing all records that match the regex. Defaults to False.

    Returns:
        (list, list): List of records that match regex, List of tuples of captured data
    """
    matching_records = []
    captured_data = []
    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(regex, line, re.IGNORECASE if ignore_case else 0)
            if match:
                matching_records.append(line.strip())
                if match.groups():
                    captured_data.append(match.groups())
                if print_records:
                    print(line.strip())

    if print_summary:
        print(f"The log file contains {len(matching_records)} records that {'case-insensitive' if ignore_case else 'case-sensitive'} match the regex \"{regex}\".")

    return matching_records, captured_data

# TODO: Step 8
def tally_port_traffic(log_file):
    """Processes a log file to create a dictionary of record tallies for each destination port.

    Args:
        log_file (str): Path of the log file

    Returns:
        dict: Dictionary of destination port number records counts
    """
    port_counts = {}
    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(r'DPT=(\d+)', line)
            if match:
                port_number = int(match.group(1))
                if port_number in port_counts:
                    port_counts[port_number] += 1
                else:
                    port_counts[port_number] = 1
    return port_counts

# TODO: Step 9
def generate_port_traffic_report(log_file, port_number):
    """Generates a CSV file containing port traffic information for a specified port.

    Args:
        log_file (str): Path of the log file
        port_number (int): Destination port number
    """
    report_data = []
    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(r'DPT=(\d+)', line)
            if match and int(match.group(1)) == port_number:
                date_time = re.search(r'(\w+ \d+ \d+:\d+:\d+)', line).group(1)
                src_ip = re.search(r'SRC=(\d+\.\d+\.\d+\.\d+)', line).group(1)
                dst_ip = re.search(r'DST=(\d+\.\d+\.\d+\.\d+)', line).group(1)
                src_port = re.search(r'SPORT=(\d+)', line).group(1) if re.search(r'SPORT=(\d+)', line) else ''
                report_data.append([date_time, src_ip, dst_ip, src_port, port_number])

    with open(f"destination_port_{port_number}_report.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date", "Time", "Source IP", "Destination IP", "Source Port", "Destination Port"])
        writer.writerows(report_data)

# TODO: Step 11
def generate_invalid_user_report(log_file):
    """Generates a CSV file containing information about invalid user login attempts.

    Args:
        log_file (str): Path of the log file
    """
    report_data = []
    with open(log_file, 'r') as file:
        for line in file:
            match = re.search(r'Invalid user (\w+) from (\d+\.\d+\.\d+\.\d+)', line)
            if match:
                username, ip_address = match.groups()
                date_time = re.search(r'(\w+ \d+ \d+:\d+:\d+)', line).group(1)
                report_data.append([date_time, username, ip_address])

    with open(f"invalid_users.csv", 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Date", "Time", "Username", "IP Address"])
        writer.writerows(report_data)

# TODO: Step 12
def generate_source_ip_log(log_file, ip_address):
    """Generates a plain text log file containing records with the specified source IP address.

    Args:
        log_file (str): Path of the log file
        ip_address (str): Source IP address
    """
    matching_records, _ = filter_log_by_regex(log_file, f'SRC={ip_address}')
    with open(f"source_ip_{ip_address.replace('.', '_')}.log", 'w') as outfile:
        for record in matching_records:
            outfile.write(record + "\n")

if __name__ == '__main__':
    main()

   
    
   