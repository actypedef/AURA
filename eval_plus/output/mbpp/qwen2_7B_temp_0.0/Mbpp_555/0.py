"""
Write a python function to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers.
assert difference(3) == 30
"""
def difference(n):
    # Calculate the sum of cubes of the first n natural numbers
    cube_sum = (n * (n + 1) // 2) ** 3
    
    # Calculate the sum of the first n natural numbers
    linear_sum = n * (n + 1) // 2
    
    # Return the difference between the cube sum and the linear sum
    return cube_sum - linear_sum

# Test the function with the provided test case
assert difference(3) == 30
