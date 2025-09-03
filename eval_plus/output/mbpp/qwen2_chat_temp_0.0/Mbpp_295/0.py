"""
Write a function to return the sum of all divisors of a number.
assert sum_div(8)==7
"""
def sum_div(n):
    # Initialize the sum of divisors to 0
    s = 0
    
    # Loop through possible divisors from 1 to n-1
    for i in range(1, n):
        # If i is a divisor of n, add it to the sum
        if n % i == 0:
            s += i
            
    # Return the total sum of divisors
    return s

# Test the function with the provided test case
assert sum_div(8) == 7
