"""
Write a python function that takes in an integer n and returns the sum of the squares of the first n odd natural numbers.
assert square_Sum(2) == 10
"""
def square_Sum(n):
    # Initialize sum to 0
    sum = 0
    # Iterate through the first n odd numbers
    for i in range(0, n):
        # Calculate the i-th odd number and add its square to the sum
        sum += (2 * i + 1) ** 2
    return sum

# Test the function with the provided test case
assert square_Sum(2) == 10
