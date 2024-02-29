#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    """Determines fewest coins needed to meet given total with a pile of coins.

    Args:
    - coins (list of int): Available coin denominations.
    - total (int): Total amount to make change for.

    Returns:
    - int: Fewest number of coins needed. If not possible, return -1.
    """
    if total <= 0:
        return 0

    remaining_amount = total
    coins_count = 0
    coin_index = 0
    sorted_coins = sorted(coins, reverse=True)
    num_coins = len(coins)

    while remaining_amount > 0:
        if coin_index >= num_coins:
            return -1

        if remaining_amount - sorted_coins[coin_index] >= 0:
            remaining_amount -= sorted_coins[coin_index]
            coins_count += 1
        else:
            coin_index += 1

    return coins_count
