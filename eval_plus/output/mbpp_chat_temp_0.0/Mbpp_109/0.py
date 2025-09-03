"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""
def odd_Equivalent(binary_string, rotations):
    # Initialize count of odd equivalent strings
    odd_count = 0
    
    # Iterate through each possible rotation
    for i in range(rotations):
        # Check if the current rotation has an odd number of '1's
        if binary_string.count('1') % 2 != 0:
            odd_count += 1
        
        # Rotate the string by moving the first character to the end
        binary_string = binary_string[1:] + binary_string[0]
    
    return odd_count

# Test the function with the provided test case
assert odd_Equivalent("011001", 6) == 3