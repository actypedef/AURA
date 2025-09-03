"""
Write a function to find the median length of a trapezium.
assert median_trapezium(15,25,35)==20
"""
def median_trapezium(base1, base2, height):
    # Calculate the median length of the trapezium using the formula
    return (base1 + base2) / 2

# Test the function with the provided test case
assert median_trapezium(15, 25, 35) == 20
