"""
Write a python function to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers.
assert difference(3) == 30
"""
def difference(n):
    # Calculate the sum of the cubes of the first n natural numbers
    sum_of_cubes = sum(i ** 3 for i in range(1, n + 1))
    
    # Calculate the sum of the first n natural numbers
    sum_of_naturals = sum(range(1, n + 1))
    
    # Return the difference between the sum of cubes and the sum of natural numbers
    return sum_of_cubes - sum_of_naturals

# Test the function with the provided test case
assert difference(3) == 30
