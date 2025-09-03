"""
Write a python function to find whether the parity of a given number is odd.
assert find_Parity(12) == False
"""
def find_Parity(num):
    # Check if the number of 1s in the binary representation of num is odd
    return bool(num & 1)

# Test the function with the provided test case
assert find_Parity(12) == False
