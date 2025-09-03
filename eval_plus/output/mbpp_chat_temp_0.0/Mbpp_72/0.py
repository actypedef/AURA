"""
Write a python function to check whether the given number can be represented as the difference of two squares or not.
assert dif_Square(5) == True
"""
def dif_Square(n):
    # Check if n is even or 1
    if (n % 2 == 0) or (n == 1):
        return True
    else:
        return False

# Test the function with the provided test case
assert dif_Square(5) == True