"""
Write a python function to find whether the parity of a given number is odd.
assert find_Parity(12) == False
"""
def find_Parity(n):
    # Check if the number is even using bitwise AND operation
    if (n & 1) == 0:
        return False
    else:
        return True

# Test the function with the provided test case
assert find_Parity(12) == False
