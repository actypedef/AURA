"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""
def amicable_numbers_sum(n):
    # Initialize a list to store the sum of divisors for each number up to n
    sums = [0] * (n + 1)
    
    # Calculate the sum of divisors for each number
    for i in range(1, n + 1):
        for j in range(i * 2, n + 1, i):
            sums[j] += i
    
    # Find and sum all amicable pairs
    return sum(i for i in range(2, n) if sums[i] != i and sums[sums[i]] == i)

# Test the function with the provided test case
assert amicable_numbers_sum(999) == 504