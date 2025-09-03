"""
Write a python function takes in an integer n and returns the sum of squares of first n even natural numbers.
assert square_Sum(2) == 20
"""
def square_Sum(n):
    # Initialize sum to 0
    sm = 0
    # Iterate through the first n even numbers
    for i in range(1, n + 1):
        # Calculate the i-th even number and add its square to the sum
        sm = sm + (2 * i) * (2 * i)
    return sm

# Test the function with the provided test case
assert square_Sum(2) == 20
