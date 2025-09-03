"""
Write a function to find the median of three numbers.
assert median_numbers(25,55,65)==55.0
"""
def median_numbers(x, y, z):
    # Check if x is not between y and z
    if (x > y and x < z) or (x > z and x < y):
        return x
    # Check if y is not between x and z
    elif (y > x and y < z) or (y > z and y < x):
        return y
    else:
        return z

# Test the function with the provided test case
assert median_numbers(25, 55, 65) == 55.0