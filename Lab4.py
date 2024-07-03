#Name: Dennis Dam #
#School fleming College#
#Course: Scripting Applications# 
#Assignment: 4#

##filepath=(/Users/dennidam/Desktop/Lab-assignment-3-scrpiting-applications-/lab-4-gateway-/gateway.log)##

##### project: writing a python script that process a gateway log file line by line #####



import re
import sys
import os
import pandas as pd


def main():
    log_file = get_log_file_path_from_cmd_line()
    # ...


#step 3
def get_log_file_path_from_cmd_line():
    if len(sys.argv) != 2:
        print("error: log file not provided.")
        sys.exit(1)

    log_file_path = sys.argv[1]
    if not os.path.isfile(log_file_path):
        print(f"error: error file not found at {log_file_path}") 
        sys.exit(1)

    return log_file_path


#step 4-7 combined 
def filter_log_by_regex(log_file, regex, ignore_case=True, print_summary=False, print_records=False):
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

    if print_summary:
        if ignore_case:
            print(f"The log file contains {len(records)} records that case-insensitive match the regex \"{regex}\".")    
        else:
            print(f"The log file contains {len(records)} records that match the regex \"{regex}\".")

    return records, captured_data



### step 8 ##
def tally_port_traffic(log_file):
    port_counts = {}
    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(r'DPT=(\d+)', line)
            if match:
                port = match.group(1)
                if port in port_counts:
                    port_counts[port] += 1
                else:
                    port_counts[port] = 1
    return port_counts



##### step 9 #####
def generate_port_traffic_report(log_file, port_number):
    records, _ = []
    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(r'DPT={port_number}', line)
            if match:
                date, time, src, dst, spt, dpt = re.findall(r'(Jan \d+ \d+: d+:\d+) |SRC= (.*?)|DST= (.*?)|SPT= (.*?)|DPT= (.*?)', line)
                records.append([date, time, src, dst, spt, dpt])

    df = pd.DataFrame(records, colums=['Date', 'Sorce IP', 'Destination IP', 'Source Port', 'Destination Port'])
    df.to_csv(f"destination_port_{port_number}_report.csv", index=False)


                

####Step 11### generating invalid user report 
def generate_invalid_user_report(log_file):
    records = []
    with open(log_file, 'r') as f:
        for line in f:
            match = re.search(r'Invalid user (.*?) from (.*?)', line)
            if match:
                date, time, user, ip = re.findall(r'(Jan \d+ \d+: d+:\d+) |Invalid user (.*?) from(.*?)', line)
                records.append([date, time, user, ip])

    df = pd.Dataframe(records, columns=['Date', 'Time', 'Username' 'IP Address'])
    df.to_csv('invalid_user.csv', index=False)




####Step 12### to generate source ip log 
def generate_source_ip_log(log_file, ip_address):
    records, _ = filter_log_by_regex(log_file, f'SRC={ip_address}') 
    with open('source_ip_log.csv', 'w') as f:
        for record in records:
            f.write(record + '\n')
if __name__ == '__main__':
    main()
