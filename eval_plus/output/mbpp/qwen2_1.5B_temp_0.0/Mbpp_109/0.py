"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""
def odd_Equivalent(binary_string, rotations):
    # Convert the binary string to an integer
    num = int(binary_string, 2)
    
    # Initialize count for odd equivalent numbers
    odd_count = 0
    
    # Iterate through each rotation
    for _ in range(rotations):
        # Rotate the binary string to the left by one position
        rotated_string = binary_string[1:] + binary_string[0]
        
        # Convert the rotated string back to an integer
        rotated_num = int(rotated_string, 2)
        
        # Check if the rotated number has an odd value
        if rotated_num % 2 != 0:
            odd_count += 1
    
    return odd_count

# Test cases
assert odd_Equivalent("011001",6) == 3
assert odd_Equivalent("101010",5) == 4
assert odd_Equivalent("111111",7) == 8