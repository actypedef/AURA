"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""
def amicable_numbers_sum(n):
    # Initialize a list to store amicable numbers
    amicables = []
    
    # Loop through each number up to n
    for i in range(2, n + 1):
        # Calculate the sum of divisors of i (excluding i itself)
        sum_i = sum([j for j in range(1, i) if i % j == 0])
        
        # Check if the sum of divisors of sum_i equals i and i is not already in the list
        if sum_i > i and sum([j for j in range(1, sum_i) if sum_i % j == 0]) == i and i not in amicables:
            # Add both numbers to the list of amicable numbers
            amicables.extend([i, sum_i])
    
    # Return the sum of all unique amicable numbers found
    return sum(set(amicables))

# Test the function with the provided test case
assert amicable_numbers_sum(999) == 504