"""
Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
assert find_length("11000010001") == 6
"""
def find_length(binary):
    # Initialize variables to store the maximum length and current count
    max_len = 0
    curr_count = 0
    
    # Iterate through each character in the binary string
    for char in binary:
        # If the character is '0', increment the current count
        if char == '0':
            curr_count += 1
        else:
            # If the character is '1', decrement the current count
            curr_count -= 1
        
        # Update the maximum length if the current count exceeds it
        max_len = max(max_len, curr_count)
        
        # Reset the current count if it becomes negative
        if curr_count < 0:
            curr_count = 0
    
    return max_len

# Test the function with the provided test case
assert find_length("11000010001") == 6
