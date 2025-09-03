"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""
def count_Primes_nums(n):
    if n <= 1:
        return 0
    primes = [True] * (n+1)
    p = 2
    while (p * p <= n):
        if primes[p]:
            for i in range(p * p, n+1, p):
                primes[i] = False
        p += 1
    return sum(primes[2:])

# Test cases to verify the correctness of the function
assert count_Primes_nums(5) == 2
assert count_Primes_nums(11) == 4
assert count_Primes_nums(0) == 0
assert count_Primes_nums(20) == 8
assert count_Primes_nums(1) == 0
assert count_Primes_nums(18) == 6