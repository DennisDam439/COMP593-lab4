#Name: Dennis Dam #
#School fleming College#
#Course: Scripting Applications# 
#Assignment: 4#



##filepath=(/Users/dennidam/Desktop/Lab-assignment-3-scrpiting-applications-/lab-4-gateway-/gateway.log)##

##### project: writing a python script that process a text file line by line #####



import re
import sys
import os
import csv


def main():
    log_file = get_log_file_path_from_cmd_line()

#step 3
    def_get_log_files_path_from_cmd_line ():
    if len(sys.argv) < 2:
        print("error")
        sys.exit(1)
    log_file = sys.argv[1]
    if not os.path.isfile(log_file);
        print("error")
        sys.exit(1)
    return log_file

#step 4
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
        returns:
        (list, list): List of records that match regex, List of tuples of captured data
        """
matching_records = []
captured_data = []
with open(log_file, 'r') as f:
    for line in f:
        if ignore case:
            match = re.search(regex, line, re. IGNORECASE)
        else:
            match = re.search(regex, line)
        if match:
            matching_records.append(line)
            if match.groups()
                captured_data.append(match.groups())
if print_records:
    for record in matching_records:
        print(record)
if print_summmury:
    if ignore_case:
        print(f"Found {len(matching_records)} matching records") records that case-sensitive match the regex \"{regex}\".")    
    else:
        print(f"Found {len(matching_records)} matching records") records that match the regex \"{regex}\".")
return matching_records, captured_data



### step 8

