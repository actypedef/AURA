"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""
def odd_Equivalent(s, n):
    # Check if the length of the string is even or odd
    if len(s) % 2 == 0:
        # If even, all rotations will have the same number of 1s
        return (n + 1) // 2
    else:
        # If odd, count the number of 1s in the original string
        ones = s.count('1')
        # Calculate the number of rotations with an odd number of 1s
        return ((ones * (n + 1)) + 1) // 2

# Test the function with the provided test case
assert odd_Equivalent("011001", 6) == 3