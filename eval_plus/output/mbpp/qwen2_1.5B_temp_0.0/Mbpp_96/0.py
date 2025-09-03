"""
Write a python function to find the number of divisors of a given integer.
assert divisor(15) == 4
"""
def divisor(n):
    count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            count += 1
    return count

# Test cases
assert divisor(15) == 4
assert divisor(28) == 6
assert divisor(37) == 2
assert divisor(100) == 9