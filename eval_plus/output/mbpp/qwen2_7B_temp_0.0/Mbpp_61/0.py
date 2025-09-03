"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""
def count_Substrings(s):
    # Initialize variables to store the result and the current sum
    res = 0
    curr_sum = 0
    
    # Create a dictionary to store the frequency of prefix sums
    prefix_sum_freq = {0: 1}
    
    # Iterate through each character in the string
    for i in range(len(s)):
        # Convert the current character to an integer and add it to the current sum
        curr_sum += int(s[i])
        
        # Calculate the required prefix sum to match the current index
        req_prefix_sum = curr_sum - (i + 1)
        
        # If the required prefix sum exists in the dictionary, add its frequency to the result
        if req_prefix_sum in prefix_sum_freq:
            res += prefix_sum_freq[req_prefix_sum]
        
        # Update the frequency of the current prefix sum in the dictionary
        prefix_sum_freq[curr_sum] = prefix_sum_freq.get(curr_sum, 0) + 1
    
    return res

# Test the function with the provided test case
assert count_Substrings('112112') == 6