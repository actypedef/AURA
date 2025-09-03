"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""
def count_Substrings(s):
    # Initialize result and prefix sum array
    res = 0
    prefixSum = [0] * (len(s) + 1)
    
    # Compute prefix sums
    for i in range(len(s)):
        prefixSum[i + 1] = prefixSum[i] + (ord(s[i]) - ord('0'))
    
    # Dictionary to store frequency of prefix sums
    mp = {}
    
    # Iterate through prefix sums
    for i in range(len(prefixSum)):
        # If prefix sum difference is zero, increment result
        if prefixSum[i] - i in mp:
            res += mp[prefixSum[i] - i]
        # Update frequency dictionary
        if prefixSum[i] - i in mp:
            mp[prefixSum[i] - i] += 1
        else:
            mp[prefixSum[i] - i] = 1
    
    return res

# Test the function with the provided test case
assert count_Substrings('112112') == 6
