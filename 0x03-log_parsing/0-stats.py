#!/usr/bin/python3
import sys
import signal
import re

# Initialize the counters and variables
total_size = 0
status_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
line_count = 0

# Regular expression to parse the log lines
log_pattern = re.compile(r'(\S+) - \[\S+ \S+\] "GET /projects/260 HTTP/1.1" (\d{3}) (\d+)')

def print_stats():
    """Prints the accumulated statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print("{}: {}".format(code, status_counts[code]))

def signal_handler(sig, frame):
    """Handles the keyboard interruption signal."""
    print_stats()
    sys.exit(0)

# Set up the signal handler for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

# Read and process each line from standard input
try:
    for line in sys.stdin:
        match = log_pattern.match(line)
        if match:
            status_code = match.group(2)
            file_size = int(match.group(3))
            
            # Accumulate the total file size
            total_size += file_size
            
            # Count the status code occurrence
            if status_code in status_counts:
                status_counts[status_code] += 1

            line_count += 1

            # Print statistics after every 10 lines
            if line_count % 10 == 0:
                print_stats()
except KeyboardInterrupt:
    # Handle the keyboard interruption if not caught by the signal handler
    print_stats()
    sys.exit(0)

# Print the final statistics after reading all lines
print_stats()
