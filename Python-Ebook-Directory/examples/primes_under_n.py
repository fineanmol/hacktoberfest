"""Example: primes_under_n.py

Provides `list_primes(n)` which is testable and an interactive CLI guard.
"""
import math
from typing import List


def is_prime(candidate: int) -> bool:
    if candidate < 2:
        return False
    if candidate == 2:
        return True
    if candidate % 2 == 0:
        return False
    limit = int(math.sqrt(candidate)) + 1
    for i in range(3, limit, 2):
        if candidate % i == 0:
            return False
    return True


def list_primes(n: int) -> List[int]:
    return [i for i in range(2, n + 1) if is_prime(i)]


if __name__ == "__main__":
    n = int(input("List primes up to: "))
    print(list_primes(n))
