"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""
def count_Substrings(s):
    # Initialize variables to store the result and the cumulative sum
    res = 0
    cum_sum = 0
    
    # Create a dictionary to store the frequency of (cumulative sum - index)
    freq = {0: 1}
    
    # Iterate over the string with index
    for i in range(len(s)):
        # Update the cumulative sum by adding the current digit
        cum_sum += int(s[i])
        
        # Calculate the required value for the substring condition
        req_val = cum_sum - (i + 1)
        
        # Add the frequency of the required value to the result
        if req_val in freq:
            res += freq[req_val]
        
        # Update the frequency dictionary
        if req_val in freq:
            freq[req_val] += 1
        else:
            freq[req_val] = 1
    
    return res

# Test the function with the provided test case
assert count_Substrings('112112') == 6