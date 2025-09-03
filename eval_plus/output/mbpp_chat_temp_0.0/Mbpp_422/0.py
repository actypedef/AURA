"""
Write a python function to find the average of cubes of first n natural numbers.
assert find_Average_Of_Cube(2) == 4.5
"""
def find_Average_Of_Cube(n):
    # Calculate the sum of cubes of the first n natural numbers
    sum = (n * (n + 1)) // 2
    # Calculate the cube of the sum
    cube_sum = sum ** 3
    # Return the average of the cubes
    return cube_sum / n

# Test the function with the provided test case
assert find_Average_Of_Cube(2) == 4.5
