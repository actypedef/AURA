"""
Write a function to return the sum of all divisors of a number.
assert sum_div(8)==7
"""
def sum_div(n):
    # Initialize sum to 0
    total_sum = 0
    
    # Loop through all numbers from 1 to n (inclusive)
    for i in range(1, n + 1):
        # If i divides n without leaving a remainder, add it to total_sum
        if n % i == 0:
            total_sum += i
            
    # Return the total sum of divisors
    return total_sum

# Test the function with the provided test case
assert sum_div(8) == 7