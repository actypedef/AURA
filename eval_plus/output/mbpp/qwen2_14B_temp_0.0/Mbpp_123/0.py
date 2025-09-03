"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""
def amicable_numbers_sum(limit):
    # Dictionary to store the sum of proper divisors for each number
    divisorsum = [0] * (limit + 1)
    
    # Calculate the sum of proper divisors for each number
    for i in range(1, limit + 1):
        for j in range(i * 2, limit + 1, i):
            divisorsum[j] += i
    
    # Sum all amicable numbers
    total_amicable_sum = 0
    for i in range(2, limit + 1):
        if divisorsum[i] != i and divisorsum[i] <= limit and divisorsum[divisorsum[i]] == i:
            total_amicable_sum += i
    
    return total_amicable_sum

# Test the function with the provided test case
assert amicable_numbers_sum(999) == 504
