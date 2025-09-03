"""
Write a python function to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers.
assert difference(3) == 30
"""
def difference(n):
    # Calculate the sum of the first n natural numbers
    sum_natural = (n * (n + 1)) // 2
    
    # Calculate the sum of cubes of the first n natural numbers
    sum_cubes = ((n * (n + 1)) // 2) ** 2
    
    # Return the difference between the sum of cubes and the sum of natural numbers
    return sum_cubes - sum_natural

# Test the function with the provided test case
assert difference(3) == 30
