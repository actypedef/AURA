"""
Write a function that returns the perimeter of a square given its side length as input.
assert square_perimeter(10)==40
"""
def square_perimeter(side_length):
    # Calculate the perimeter of a square
    return 4 * side_length

# Test cases to verify the correctness of the function
assert square_perimeter(10) == 40
assert square_perimeter(5) == 20
assert square_perimeter(7) == 28