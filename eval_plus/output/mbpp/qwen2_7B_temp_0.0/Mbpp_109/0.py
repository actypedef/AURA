"""
Write a python function to find the number of numbers with an odd value when rotating a binary string the given number of times.
assert odd_Equivalent("011001",6) == 3
"""
def odd_Equivalent(s, n):
    # Initialize count of odd equivalent strings
    count = 0
    
    # Iterate over each character in the string
    for i in range(len(s)):
        # Check if the current character is '1'
        if s[i] == '1':
            # Increment the count as it contributes to odd equivalence
            count += 1
    
    # Return the total count of odd equivalent strings
    return count

# Test the function with the provided test case
assert odd_Equivalent("011001", 6) == 3