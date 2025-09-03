"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""
def count_Substrings(s):
    # Initialize variables to store the count of valid substrings and the current sum
    count = 0
    curr_sum = 0
    
    # Iterate through each character in the string
    for i in range(len(s)):
        # Subtract the ASCII value of '0' from the current character to get its numeric value
        curr_sum += ord(s[i]) - ord('0')
        
        # If the current sum equals the index (i+1), increment the count
        if curr_sum == i + 1:
            count += 1
    
    return count

# Test the function with the provided test case
assert count_Substrings('112112') == 6