#!/usr/bin/python3
"""
Making Change
"""


def makeChange(coins, total):
    """" Create a list to store the minimum number of coins
    needed for each total from 0 to 'total_amount'
    """
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0  # 0 coins are needed to make a total of 0

    # Iterate through each coin value
    for coin_value in coins:
        """ Update min_coins[total] for all
        values of total where total >= coin_value"""
        for total in range(coin_value, total + 1):
            min_coins[total] = min(min_coins[total],
                                   min_coins[total - coin_value] + 1)

    # If min_coins[total_amount] is still float('inf'),
    # it means the total cannot be met by any number of coins
    if min_coins[total] == float('inf'):
        return -1
    else:
        return min_coins[total]
