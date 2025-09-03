"""
Write a python function to find the cube sum of first n even natural numbers.
assert cube_Sum(2) == 72
"""
def cube_Sum(n):
    # Initialize sum to 0
    sum = 0
    
    # Iterate through the first n even natural numbers
    for i in range(1, n + 1):
        # Calculate the i-th even number and add its cube to the sum
        sum += (2 * i) ** 3
    
    return sum

# Test the function with the provided test case
assert cube_Sum(2) == 72
