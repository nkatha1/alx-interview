#!/usr/bin/python3
"""
Prime Game - Determines the winner of a prime number removal game.
"""


def isWinner(x, nums):
    """
    Determine the winner of x rounds of a game where two players take turns
    choosing a prime number from a set of consecutive integers starting from 1
    up to and including n. The player that cannot make a move loses the game.
    
    Args:
        x (int): Number of rounds.
        nums (list of int): List containing the maximum integer (n) for each round.

    Returns:
        str: Name of the player that won the most rounds ("Maria" or "Ben").
             If there's no clear winner, return None.
    """
    if x < 1 or not nums:
        return None
    
    marias_wins, bens_wins = 0, 0

    # Generate primes using Sieve of Eratosthenes up to the maximum number in nums
    n = max(nums)
    primes = [True for _ in range(n + 1)]
    primes[0] = primes[1] = False  # 0 and 1 are not prime numbers
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i * i, n + 1, i):
                primes[j] = False

    # Precompute the number of primes up to each index
    prime_count = [0] * (n + 1)
    for i in range(1, n + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Simulate each game round
    for _, n in zip(range(x), nums):
        # Count the total primes up to n
        primes_up_to_n = prime_count[n]
        if primes_up_to_n % 2 == 0:
            bens_wins += 1
        else:
            marias_wins += 1

    # Determine the overall winner
    if marias_wins > bens_wins:
        return "Maria"
    elif bens_wins > marias_wins:
        return "Ben"
    return None

