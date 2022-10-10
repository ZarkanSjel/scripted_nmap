#!/usr/bin/env python3

import time
import os 
from datetime import datetime

def execute_nmap(source_file, output_file):
    # ONLY VALID FOR UNIX
    base, filename = os.path.split(output_file)
    print(base)
    assert os.path.isfile(source_file), f"The InputFile: {source_file}, Does Not Exist"
    assert os.path.isdir(base), f"The Path: {base}, Doesn't Exist."

    command = f"nmap -sV -T4 -A -v --script vulners.nse -iL {source_file} -oN {output_file}"
    nmap_exec_code = os.system(command) # For Windows it will be the output of the command
    return nmap_exec_code

def main() -> int:
    now = datetime.now()
    pwd = os.getcwd()
    scan_date = now.strftime("%Y-%m-%d")

    INPUT_FILE_NAME = "ip_list.txt"
    OUTPUT_FILE_NAME = f"scan_{scan_date}.txt"
    OUTPUT_FOLDER_NAME = "scan"

    dest_path = os.path.join(pwd, OUTPUT_FOLDER_NAME)
    source_file = os.path.join(pwd, INPUT_FILE_NAME)
    output_file = os.path.join(dest_path, OUTPUT_FILE_NAME)

    status_code = execute_nmap(source_file, output_file)
    return status_code

if __name__ == '__main__':
    start_time = time.time()
    main()
    print(f"{(time.time() - start_time)} seconds")