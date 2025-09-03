"""
Write a function to find the median length of a trapezium.
assert median_trapezium(15,25,35)==20
"""
def median_trapezium(base_a, base_b, height):
    # Calculate the median length of the trapezium using the formula
    median = 0.5 * (base_a + base_b)
    return median

# Test the function with the provided test case
assert median_trapezium(15, 25, 35) == 20
