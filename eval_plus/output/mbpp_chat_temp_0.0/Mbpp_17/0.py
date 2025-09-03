"""
Write a function that returns the perimeter of a square given its side length as input.
assert square_perimeter(10)==40
"""
def square_perimeter(side):
    # Calculate the perimeter of the square using the formula: 4 * side length
    return 4 * side

# Test the function with the provided test case
assert square_perimeter(10) == 40
