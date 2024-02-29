#!/usr/bin/python3
"""
Main file for testing
"""

makeChange = __import__('0-making_change').makeChange

# Test cases with non-empty coins list and non-zero total
print(makeChange([1, 2, 25], 37))           # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))   # Output: -1

# Additional edge cases
print(makeChange([], 0))                    # Output: 0 (No coins, total 0)
print(makeChange([1, 2, 3], 0))             # Output: 0 (Empty total)
print(makeChange([], 10))                    # Output: -1 (No coins, non-zero total)
print(makeChange([2, 4, 6], 3))             # Output: -1 (Impossible to make total)
print(makeChange([1, 2, 5], 11))            # Output: 3 (11 = 5 + 5 + 1)
print(makeChange([1, 2, 5, 10], 14))        # Output: 2 (14 = 10 + 2 + 2)
