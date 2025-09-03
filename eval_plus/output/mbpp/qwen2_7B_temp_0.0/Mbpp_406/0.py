"""
Write a python function to find whether the parity of a given number is odd.
assert find_Parity(12) == False
"""
def find_Parity(n):
    # Check if the number is even or odd using bitwise AND operation
    return (n & 1)

# Test cases to validate the function
assert find_Parity(12) == False
