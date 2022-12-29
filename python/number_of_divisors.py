"""
Count the number of divisors of a positive integer n.

Random tests go up to n = 500000.
"""

def divisors(n):
    count = 1               #every number has at least 2 divisors (the number 1 and itself)
    for i in range(1, n):
        if n % i == 0:
            count += 1
    return count