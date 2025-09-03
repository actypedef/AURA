"""
Write a function that returns the perimeter of a square given its side length as input.
assert square_perimeter(10)==40
"""
def square_perimeter(side_length):
    # Calculate the perimeter of the square
    perimeter = 4 * side_length
    return perimeter

# Test the function with the provided test case
assert square_perimeter(10) == 40
