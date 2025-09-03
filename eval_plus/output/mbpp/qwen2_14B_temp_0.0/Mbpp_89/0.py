"""
Write a function to find the closest smaller number than n.
assert closest_num(11) == 10
"""
def closest_num(n):
    # Iterate from n-1 down to 0
    for i in range(n-1, -1, -1):
        # Return the first number found, which is the closest smaller number
        return i

# Test the function with the provided test case
assert closest_num(11) == 10
