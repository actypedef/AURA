"""
Write a python function to find the cube sum of first n even natural numbers.
assert cube_Sum(2) == 72
"""
def cube_Sum(n):
    # Initialize the sum variable
    sum = 0
    
    # Loop through the first n even natural numbers
    for i in range(1, n + 1):
        # Calculate the cube of each even number and add it to the sum
        sum += (2 * i) ** 3
    
    return sum

# Test the function with the provided test case
assert cube_Sum(2) == 72
