"""
Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
assert square_Sum(2) == 20
"""
def square_Sum(n):
    # Initialize the result variable to store the sum of squares
    res = 0
    
    # Iterate through the first n even numbers
    for i in range(1, n + 1):
        # Square each even number and add it to the result
        res += (2 * i) ** 2
    
    # Return the computed sum of squares
    return res

# Test the function with the provided test case
assert square_Sum(2) == 20
