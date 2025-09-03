"""
Write a function to find the n'th lucas number.
assert find_lucas(9) == 76
"""
def find_lucas(n):
    # Base case: return 2 if n is 0
    if n == 0:
        return 2
    # Base case: return 1 if n is 1
    elif n == 1:
        return 1
    # Recursive case: return the sum of the two preceding Lucas numbers
    else:
        return find_lucas(n - 1) + find_lucas(n - 2)

# Test the function with the provided test case
assert find_lucas(9) == 76
