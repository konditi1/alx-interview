#!/usr/bin/python3

import re
import sys


def extract_input(input_line):
    """Extracts sections of a line of an HTTP request log."""
    match = re.match(
        r'\S+ - \[(\d+-\d+-\d+ \d+:\d+:\d+\.\d+)\]'
        r'"GET /projects/260 HTTP/1.1" (\d+) (\d+)', input_line)
    if match:
        return int(match.group(2)), int(match.group(3))
    return 0, 0


def print_statistics(total_file_size, status_codes_stats):
    '''Prints the accumulated statistics of the HTTP request log.'''
    print('File size:', total_file_size)
    for code, count in sorted(status_codes_stats.items()):
        if count:
            print(f'{code}: {count}')


def update_metrics(line, total_file_size, status_codes_stats):
    """Updates the metrics from a given HTTP request log."""
    status_code, file_size = extract_input(line)
    if status_code in status_codes_stats:
        status_codes_stats[status_code] += 1
    return total_file_size + file_size


def run():
    """Starts the log parser."""
    total_file_size = 0
    status_codes_stats = {str(code): 0 for code in range(200, 600, 100)}
    try:
        for line_num, line in enumerate(sys.stdin, 1):
            file1 = total_file_size
            file2 = status_codes_stats
            total_file_size = update_metrics(line.strip(), file1, file2)
            if line_num % 10 == 0:
                print_statistics(total_file_size, status_codes_stats)
    except KeyboardInterrupt:
        print_statistics(total_file_size, status_codes_stats)


if __name__ == '__main__':
    run()
