"""
Write a function to find the median of three numbers.
assert median_numbers(25,55,65)==55.0
"""
def median_numbers(x, y, z):
    # Sort the numbers and return the middle one as the median
    if x < y:
        if y < z:
            return y
        elif x < z:
            return z
        else:
            return x
    else:
        if x < z:
            return x
        elif y < z:
            return z
        else:
            return y

# Test the function with the provided test case
assert median_numbers(25, 55, 65) == 55.0
