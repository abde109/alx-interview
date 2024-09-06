#!/usr/bin/python3
"""this is last alx python code"""

def is_prime(n):
    """ Helper function to determine if n is prime using the Sieve"""
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for start in range(2, int(n ** 0.5) + 1):
        if sieve[start]:
            for i in range(start * start, n + 1, start):
                sieve[i] = False
    return sieve


def isWinner(x, nums):
    """ Determine the winner after x rounds of the prime game """
    if x < 1 or not nums:
        return None

    # Precompute primes up to the maximum number in nums using sieve
    max_n = max(nums)
    sieve = is_prime(max_n)

    # Maria wins if the count of primes is odd, Ben wins if it's even
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        primes_count = sum(sieve[:n + 1])
        if primes_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
