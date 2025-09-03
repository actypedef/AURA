"""
Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
assert find_Rotations("aaaa") == 1
"""
def find_Rotations(s):
    # Initialize the count of rotations to zero
    rotation_count = 0
    
    # Iterate through each character in the string
    for i in range(len(s)):
        # Check if the current character is not the first one
        if s[i] != s[0]:
            # Increment the rotation count
            rotation_count += 1
    
    # Return the total rotation count
    return rotation_count

# Test cases to verify the correctness of the function
assert find_Rotations("aaaa") == 1
assert find_Rotations("abab") == 1
assert find_Rotations("abcabc") == 2
assert find_Rotations("abcdedcba") == 4
assert find_Rotations("abcdefg") == 3