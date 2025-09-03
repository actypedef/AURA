"""
Write a function to find the perimeter of a regular pentagon from the length of its sides.
assert perimeter_pentagon(5) == 25
"""
def perimeter_pentagon(side):
    # Calculate the perimeter of a regular pentagon by multiplying the side length by 5
    return 5 * side

# Test the function with the provided test case
assert perimeter_pentagon(5) == 25
