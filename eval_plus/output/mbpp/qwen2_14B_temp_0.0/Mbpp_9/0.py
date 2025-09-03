"""
Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
assert find_Rotations("aaaa") == 1
"""
def find_Rotations(s):
    # Concatenate the string with itself
    tmp = s + s
    n = len(s)
    
    # Iterate through possible rotations
    for i in range(1, n + 1):
        # Check if the substring matches the original string
        if tmp[i: i + n] == s:
            return i
    
    # If no rotation matches, return the length of the string
    return n

# Test the function with the provided test case
assert find_Rotations("aaaa") == 1
