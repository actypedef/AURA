"""
Write a function to find the n'th lucas number.
assert find_lucas(9) == 76
"""
def find_lucas(n):
    # Base cases for the first two Lucas numbers
    if n == 0:
        return 2
    elif n == 1:
        return 1
    
    # Initialize the first two Lucas numbers
    lucas_0 = 2
    lucas_1 = 1
    
    # Calculate the nth Lucas number iteratively
    for _ in range(2, n + 1):
        next_lucas = lucas_0 + lucas_1
        lucas_0 = lucas_1
        lucas_1 = next_lucas
    
    return lucas_1

# Test the function with the provided test case
assert find_lucas(9) == 76