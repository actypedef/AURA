"""
Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.
assert count_Primes_nums(5) == 2
"""
def count_Primes_nums(num):
    # Initialize a list to mark prime numbers
    prime = [True] * (num)
    p = 2
    
    # Sieve of Eratosthenes algorithm to mark non-prime numbers
    while (p * p < num):
        if (prime[p] == True):
            for i in range(p * p, num, p):
                prime[i] = False
        p += 1
    
    # Count prime numbers
    prime[0], prime[1] = False, False
    count = 0
    for i in range(num):
        if prime[i]:
            count += 1
    
    return count

# Test the function with the provided test case
assert count_Primes_nums(5) == 2
