#Name: Dennis Dam #
#School fleming College#
#Course: Scripting Applications# 
#Assignment: 4#

##filepath=(/Users/dennidam/Desktop/Lab-assignment-3-scrpiting-applications-/lab-4-gateway-/gateway.log)##

##### project: writing a python script that process a text file line by line #####



import re
import sys
import os
import pandas as pd


def main():
    log_file = get_log_file_path_from_cmd_line()
    # ...


#step 3
def get_log_file_path_from_cmd_line():
    """get_log_file_path_from_cmd_line parameters

    args:
        None
    
    returns:
        str: path of the log file

    Raises:
        SystemExit: If no command line parameter is provided, or if the
            command line paraeter is not the path of an existing file.
    """ 
    if len(sys.argv) != 2:
        print("error: log file not provided.")
        sys.exit(1)

    log_file_path = sys.argv[1]
    if not os.path.isfile(log_file_path):
        print(f"error: error file not found at {log_file_path}") 
        sys.exit(1)

    return get_log_file_path


#step 4-7
def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False):
    """Gets a list of records in a log file that match a specified regex.

    Args:
        log_file (str): Path of the log file.
        regex (str): Regex filter
        ignore_case (bool, optional): Enable case insensitive regex matching. Defaults to True.
        print_summary (bool, optional): Enable printing summary of results. Defaults to False.
        print_records (bool, optional): Enable printing all records that match the regex. Defaults to False.
    Returns:
            (list, list): List of records that match regex, List of tuples of captured data
    """
    records = []
    captured_data = []
    with open(log_file, 'r') as f:
        for line in f:
            if ignore_case:
                match = re.search(regex, line, re. IGNORECASE)
            else:
                match = re.search(regex, line)
            if match:
                records.append(line.strip())
                if match.groups():
                    captured_data.append(match.groups())
                if print_records:
                    print(line.strip())

if print_summmury:
    if ignore_case:
        print(f"The log file contains {len(records)} records that case-insensitive match the regex \"{regex}\".")    
    else:
        print(f"The log file contains {len(records)} records that match the regex \"{regex}\".")
return records, captured_data



### step 8 ##
def tally_port_traffic(log_file):
    """Tallies traffic by a log file:
    
    Args:
        log_file (str): Path of the log file.
    
    Returns:
        dict: Dictionary of destination ports and the number records counts.
    """
    port_traffic = {}
    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(r'DPT=(\d+)', line)
            if match:
                port = match.group(1)
                if port in port_counts:
                    port_counts[port] += 1
            else:
                port_traffic[port] = 1
    return port_counts



##### step 9 #####
def generate_port_traffic_report(log_file, port_number):
    """Generates a CSV report for a specified destination port number.

    Args:
        log_file (str): Path of the log file.
        port_number (str): Destination port number
    
    returns:
        None
    """
    records, _ = []
    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(r'DPT={port_number}', line)
            if match:
                date, time, src, dst, spt, dpt = re.findall(r'(Jan \d+ \d+: d+:\d+) |SRC= (.*?)|DST= (.*?)|SPT= (.*?)|DPT= (.*?)', line)
                records.append([date, time, src, dst, spt, dpt])

    df = pd.DataFrame(records, colums=['Date', 'Sorce IP', 'Destination IP', 'Source Port', 'Destination Port'])
    df.to_csv(f"destination_port_{port_number}_report.csv", index=False)


                

####Step 11###
def generate invalid user report(log_file):
    """Generates a CSV report of invalid user login attempts.

    Args:
        log_file (str): Path of the log file.
    
    Returns:
        None
    """
    records, _ = []
    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(r'Invalid user', (.*?) from (.*?)', line)
            if match:
                date, time, src, dst = re.findall(r'(Jan \d+ \d+: d+:\d+) |Invalid user (.*?) from(.*?)', line)
                records.append([date, time, user, ip])

df = pd.Dataframes(records, columns=['Date', Time', 'Username' IP Address'])
df.to_csv('invalid_user_report.csv', index=False)




