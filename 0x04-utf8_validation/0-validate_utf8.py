#!/usr/bin/python3
"""validUTF8 method module"""


def validUTF8(data):
    """determines if a given data set represents a valid UTF-8 encoding"""

    # Variable to keep track of the number of remaining bytes
    # to read for a character
    remaining_byte = 0

    for value in data:

        # Check if this byte is a continuation byte
        if remaining_byte:

            # If it's not of the form 10xxxxxx, then it's an
            # invalid continuation byte
            if value >> 6 == 0b10:
                remaining_byte -= 1
                continue
            return False

        # If the byte starts with 0, it's a single-byte character
        if value >> 7 == 0:
            continue
        else:
            # Count the number of leading 1s to determine the number
            # of bytes in this character
            if value >> 3 == 0b11110:
                remaining_byte = 3
            elif value >> 4 == 0b1110:
                remaining_byte = 2
            elif value >> 5 == 0b110:
                remaining_byte = 1
            else:
                return False
    return True
