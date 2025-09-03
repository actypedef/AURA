"""
Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
assert find_length("11000010001") == 6
"""
def find_length(s):
    # Initialize variables to store the maximum length and current sum
    max_len = 0
    curr_sum = 0
    
    # Iterate through each character in the string
    for i in range(len(s)):
        # Increment current sum if '0' is found, decrement otherwise
        curr_sum += (1 if s[i] == '0' else -1)
        
        # If current sum becomes negative, reset it to zero
        if curr_sum < 0:
            curr_sum = 0
        
        # Update maximum length if current sum is greater than the previous maximum
        max_len = max(max_len, curr_sum)
    
    return max_len

# Test the function with the provided test case
assert find_length("11000010001") == 6