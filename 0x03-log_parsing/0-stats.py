#!/usr/bin/python3

import sys
import signal

def print_msg(dict_sc, total_file_size):
    """
    Method to print the accumulated statistics
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))

# Initialize variables to hold the total file size and status code counts
total_file_size = 0
counter = 0
dict_sc = {"200": 0, "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}

def signal_handler(sig, frame):
    """
    Handles the keyboard interruption signal (CTRL + C)
    """
    print_msg(dict_sc, total_file_size)
    sys.exit(0)

# Set up the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parsed_line = line.split()  # Split the line into components
        parsed_line = parsed_line[::-1]  # Reverse the components

        if len(parsed_line) > 2:
            counter += 1

            total_file_size += int(parsed_line[0])  # Update total file size
            code = parsed_line[1]  # Extract status code

            if code in dict_sc.keys():
                dict_sc[code] += 1  # Increment the count for the status code

            if counter == 10:
                print_msg(dict_sc, total_file_size)  # Print stats every 10 lines
                counter = 0

finally:
    print_msg(dict_sc, total_file_size)  # Print final stats on termination
