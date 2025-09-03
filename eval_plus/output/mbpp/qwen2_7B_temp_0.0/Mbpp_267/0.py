"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""
def square_Sum(n):
    # Initialize the sum variable to store the result
    sum = 0
    
    # Loop through the first n odd numbers
    for i in range(1, 2 * n + 1, 2):
        # Square each odd number and add it to the sum
        sum += i * i
    
    # Return the final sum of squares
    return sum

# Test the function with the provided test case
assert square_Sum(2) == 10
