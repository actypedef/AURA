"""
Write a function to find the median of three numbers.
assert median_numbers(25,55,65)==55.0
"""
def median_numbers(x, y, z):
    # Check if x is the median
    if (x >= y and x <= z) or (x <= y and x >= z):
        return x
    # Check if y is the median
    elif (y >= x and y <= z) or (y <= x and y >= z):
        return y
    # Otherwise, z is the median
    else:
        return z

# Test the function with the provided test case
assert median_numbers(25, 55, 65) == 55.0
