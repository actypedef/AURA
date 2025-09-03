"""
Write a python function that takes in an integer n and finds the sum of the first n even natural numbers that are raised to the fifth power.
assert even_Power_Sum(2) == 1056
"""
def even_Power_Sum(n):
    # Initialize the sum variable
    sum = 0
    
    # Loop through the first n even natural numbers
    for i in range(1, n + 1):
        # Calculate the fifth power of the current even number and add it to the sum
        sum += (2 * i) ** 5
    
    return sum

# Test the function with the provided test case
assert even_Power_Sum(2) == 1056
