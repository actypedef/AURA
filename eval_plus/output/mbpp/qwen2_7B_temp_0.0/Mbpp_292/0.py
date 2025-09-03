"""
Write a python function to find quotient of two numbers (rounded down to the nearest integer).
assert find(10,3) == 3
"""
# Function to calculate the quotient of two numbers, rounded down to the nearest integer
def find(x, y):
    # Calculate the quotient using floor division
    return x // y

# Test cases to verify the correctness of the function
assert find(10, 3) == 3
