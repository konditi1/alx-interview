#!/usr/bin/python3
"""
Minimum Operations
"""


def minOperations(n):
    # Base case: If n is 0 or 1, no operations needed
    if n <= 1:
        return 0

    # Iterate from 2 to n (inclusive) to find factors of n
    for i in range(2, n + 1):
        # Check if i is a factor of n
        if n % i == 0:
            # Recursive call: Calculate minimum operations for remaining part
            # (n // i) and add the current factor (i) to the result
            return minOperations(n // i) + i
