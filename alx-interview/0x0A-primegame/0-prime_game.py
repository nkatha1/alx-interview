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

    # Step 1: Generate primes using Sieve of Eratosthenes
    max_num = max(nums)
    primes = [True] * (max_num + 1)
    primes[0] = primes[1] = False  # 0 and 1 are not primes
    for i in range(2, int(max_num ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, max_num + 1, i):
                primes[j] = False

    # Step 2: Precompute the number of primes up to each number
    prime_count = [0] * (max_num + 1)
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    # Step 3: Simulate the game for each round
    marias_wins = 0
    bens_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 0:
            bens_wins += 1
        else:
            marias_wins += 1

    # Step 4: Determine the overall winner
    if marias_wins > bens_wins:
        return "Maria"
    elif bens_wins > marias_wins:
        return "Ben"
    return None

