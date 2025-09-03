"""
Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
assert square_Sum(2) == 20
"""
def square_Sum(n):
    # Initialize the sum to zero
    sum = 0
    
    # Loop through the first n even numbers
    for i in range(1, n + 1):
        # Calculate the square of each even number and add it to the sum
        sum += (2 * i) ** 2
    
    # Return the final sum
    return sum

# Test the function with the provided test case
assert square_Sum(2) == 20
