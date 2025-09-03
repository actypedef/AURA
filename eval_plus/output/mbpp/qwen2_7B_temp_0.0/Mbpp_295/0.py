"""
Write a function to return the sum of all divisors of a number.
assert sum_div(8)==7
"""
def sum_div(n):
    # Initialize the sum of divisors to 0
    sum = 0
    
    # Iterate through numbers from 1 to n-1
    for i in range(1, n):
        # Check if i is a divisor of n
        if n % i == 0:
            # Add the divisor to the sum
            sum += i
    
    # Return the total sum of divisors
    return sum

# Test the function with the provided test case
assert sum_div(8) == 7