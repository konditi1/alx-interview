#!/usr/bin/env python3

import sys
from collections import defaultdict

# Initialize variables to store metrics
total_file_size = 0
status_code_counts = defaultdict(int)
lines_processed = 0

try:
    # Read input line by line from stdin
    for line in sys.stdin:
        # Strip the newline character and split the line by spaces
        parts = line.strip().split()

        # Check if the line follows the expected format
        if len(parts) != 7:
            continue

        # Extract relevant information
        status_code = parts[-2]
        file_size = int(parts[-1])

        # Update metrics
        total_file_size += file_size
        status_code_counts[status_code] += 1
        lines_processed += 1

        # Print statistics after every 10 lines
        if lines_processed % 10 == 0:
            print(f"Total file size: {total_file_size}")
            for code in sorted(status_code_counts.keys(), key=int):
                print(f"{code}: {status_code_counts[code]}")
            print()

except KeyboardInterrupt:
    # Handle keyboard interruption
    print(f"Total file size: {total_file_size}")
    for code in sorted(status_code_counts.keys(), key=int):
        print(f"{code}: {status_code_counts[code]}")
