"""
Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
assert find_Rotations("aaaa") == 1
"""
def find_Rotations(s):
    # Check if the input string is empty or has only one character
    if len(s) <= 1:
        return 0
    
    # Initialize variables to store the length of the string and the result
    n = len(s)
    res = n
    
    # Iterate through the string to find the minimum rotation
    for i in range(1, n):
        rotated = s[i:] + s[:i]
        if rotated < s:
            res = min(res, i)
    
    return res

# Test the function with the provided test case
assert find_Rotations("aaaa") == 1