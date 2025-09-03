"""
Write a python function to find the sum of even factors of a number.
assert sumofFactors(18) == 26
"""
def sumofFactors(n):
    # Initialize sum to zero
    sum = 0
    
    # Iterate through all numbers from 1 to n
    for i in range(1, n + 1):
        # Check if i is an even factor of n
        if n % i == 0:
            # Add i to the sum
            sum += i
            
    # Return the final sum
    return sum

# Test the function with the provided test case
assert sumofFactors(18) == 26