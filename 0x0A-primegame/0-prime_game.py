#!/usr/bin/python3
"""
Maria and Ben are playing a game
"""


def isWinner(rounds, numbers):
    """Determines the winner of the game.

    Args:
        rounds (int): Number of rounds.
        numbers (list of int): List of numbers.

    Returns:
        str/None: Name of winner ("Ben"/"Maria") orNone if inputs are invalid.
    """
    if rounds <= 0 or numbers is None or rounds != len(numbers):
        return None

    ben_score = 0
    maria_score = 0

    # Sieve of Eratosthenes to generate primes
    primes = generate_primes(max(numbers))

    for num in numbers:
        if sum(primes[:num + 1]) % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if ben_score > maria_score:
        return "Ben"
    elif maria_score > ben_score:
        return "Maria"
    else:
        return None


def generate_primes(limit):
    """Generates prime numbers using Sieve of Eratosthenes.

    Args:
        limit (int): Upper limit for generating primes.

    Returns:
        list of int: List contain 1 at prime indices and 0 at composite indices
    """
    primes = [1] * (limit + 1)
    primes[0], primes[1] = 0, 0

    for i in range(2, len(primes)):
        for j in range(2 * i, len(primes), i):
            primes[j] = 0

    return primes
