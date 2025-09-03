"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""
def odd_Equivalent(binary_str, rotations):
    # Calculate the length of the binary string
    length = len(binary_str)
    
    # Initialize count of odd decimal values
    odd_count = 0
    
    # Iterate through each possible rotation
    for i in range(rotations + 1):
        # Convert the binary string to a decimal number
        decimal_value = int(binary_str, 2)
        
        # Check if the decimal value is odd
        if decimal_value % 2 != 0:
            odd_count += 1
        
        # Perform the rotation: move the last character to the front
        binary_str = binary_str[-1] + binary_str[:-1]
    
    return odd_count

# Test the function with the provided test case
assert odd_Equivalent("011001", 6) == 3