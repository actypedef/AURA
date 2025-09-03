"""
Write a function to find the closest smaller number than n.
assert closest_num(11) == 10
"""
def closest_num(n):
    # Subtract 1 from the given number to get the closest smaller number
    return (n - 1)

# Test the function with the provided test case
assert closest_num(11) == 10
