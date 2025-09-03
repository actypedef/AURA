"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""
def square_Sum(n):
    # Initialize the sum to zero
    sum = 0
    
    # Iterate through the first n odd numbers
    for i in range(1, 2 * n, 2):
        # Add the square of each odd number to the sum
        sum += i ** 2
    
    # Return the computed sum
    return sum

# Test the function with the provided test case
assert square_Sum(2) == 10