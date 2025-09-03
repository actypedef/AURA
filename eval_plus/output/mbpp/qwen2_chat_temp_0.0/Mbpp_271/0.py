"""
Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.
assert even_Power_Sum(2) == 1056
"""
def even_Power_Sum(n):
    # Initialize the result variable to store the sum
    res = 0
    
    # Iterate through the first n even numbers
    for i in range(1, n + 1):
        # Calculate the fifth power of the current even number (2 * i)
        # and add it to the result
        res += (2 * i) ** 5
    
    # Return the final calculated sum
    return res

# Test the function with the provided test case
assert even_Power_Sum(2) == 1056