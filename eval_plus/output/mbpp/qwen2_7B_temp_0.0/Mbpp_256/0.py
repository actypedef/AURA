"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""
def count_Primes_nums(n):
    # Check if n is less than 3, as there are no primes less than 2
    if n < 3:
        return 0
    
    # Initialize a list to keep track of prime status for each number up to n
    primes = [True] * n
    primes[0], primes[1] = False, False  # 0 and 1 are not prime numbers
    
    # Implement the Sieve of Eratosthenes algorithm to mark non-prime numbers
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            for j in range(i*i, n, i):
                primes[j] = False
    
    # Count the number of prime numbers
    prime_count = sum(primes)
    
    return prime_count

# Test the function with the provided test case
assert count_Primes_nums(5) == 2