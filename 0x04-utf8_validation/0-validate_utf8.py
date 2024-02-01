#!/usr/bin/python3

"""
function that determines if a given data set represents a
valid UTF-8 encoding
"""


def validUTF8(data):
    """
    function that determines if a given data set represents a
    valid UTF-8 encoding

    """
    # Variable to track the number of remaining bytes to validate
    remaining_bytes = 0

    # Iterate through each integer in the data list
    for num in data:
        # If no bytes remaining to validate, check the current byte
        if remaining_bytes == 0:
            if (num >> 3) == 0b11110:
                remaining_bytes = 3
            elif (num >> 4) == 0b1110:
                remaining_bytes = 2
            elif (num >> 5) == 0b110:
                remaining_bytes = 1
            elif (num >> 7) == 0b0:
                continue
            else:
                return False
        else:
            # If remaining bytes are still expected, check if the current byte is valid
            if (num >> 6) != 0b10:
                return False
            remaining_bytes -= 1

    # If there are remaining bytes after iterating through the data list, it's invalid
    return remaining_bytes == 0
