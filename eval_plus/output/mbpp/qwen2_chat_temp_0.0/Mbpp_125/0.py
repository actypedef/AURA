"""
Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
assert find_length("11000010001") == 6
"""
def find_length(s):
    # Initialize variables to store the current sum and maximum sum
    curr_sum = max_sum = 0
    
    # Iterate through each character in the string
    for i in range(len(s)):
        # If '1' is encountered, add 1 to curr_sum; if '0' is encountered, subtract 1 from curr_sum
        curr_sum += (1 if s[i] == '1' else -1)
        
        # Reset curr_sum to 0 if it becomes negative
        if curr_sum < 0:
            curr_sum = 0
        
        # Update max_sum if curr_sum is greater than max_sum
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

# Test the function with the provided test case
assert find_length("11000010001") == 6