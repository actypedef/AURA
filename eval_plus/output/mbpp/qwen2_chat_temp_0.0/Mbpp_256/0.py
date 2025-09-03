"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""
def count_Primes_nums(n):
    # Initialize a list to keep track of prime status for each number up to n-1
    primes = [True] * (n)
    
    # Set the first two elements as False since they are not prime
    primes[0], primes[1] = False, False
    
    # Iterate over each number starting from 2
    for i in range(2, int(n**0.5) + 1):
        if primes[i]:
            # Mark multiples of i as False (not prime)
            for j in range(i*i, n, i):
                primes[j] = False
                
    # Count the number of True values in the primes list, which represent prime numbers
    return sum(primes)

# Test the function with the provided test case
assert count_Primes_nums(5) == 2