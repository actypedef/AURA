"""
Write a python function to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers.
assert difference(3) == 30
"""
def difference(n):
    # Calculate the sum of cubes of the first n natural numbers using the formula (n*(n+1)/2)^2
    sum_of_cubes = (n * (n + 1) // 2) ** 2
    
    # Calculate the sum of the first n natural numbers using the formula n*(n+1)/2
    sum_of_natural_numbers = n * (n + 1) // 2
    
    # Return the difference between the two sums
    return sum_of_cubes - sum_of_natural_numbers

# Test cases to verify the correctness of the solution
assert difference(3) == 30
assert difference(4) == 70
assert difference(5) == 165