"""
Write a function to find the maximum difference between the number of 0s and number of 1s in any sub-string of the given binary string.
assert find_length("11000010001") == 6
"""
def find_length(s):
    # Initialize variables to store the maximum difference, current sum, and a dictionary to track sums
    max_diff = -float('inf')
    cur_sum = 0
    sum_dict = {}
    
    # Iterate through the string, treating '0' as -1 and '1' as 1
    for i in range(len(s)):
        cur_sum += (-1 if s[i] == '0' else 1)
        
        # If the current sum is negative, update the maximum difference
        if cur_sum < 0:
            max_diff = max(max_diff, i + 1)
        else:
            # If the current sum has been seen before, calculate the difference
            if cur_sum in sum_dict:
                max_diff = max(max_diff, i - sum_dict[cur_sum])
            else:
                # Store the first occurrence of the current sum
                sum_dict[cur_sum] = i
    
    return max_diff

# Test the function with the provided test case
assert find_length("11000010001") == 6
