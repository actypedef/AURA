"""
Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.
assert min_Swaps("1101","1110") == 1
"""
def min_Swaps(str1, str2):
    # Initialize the count of mismatches
    count = 0
    
    # Iterate through both strings to find mismatches
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            count += 1
    
    # If the count of mismatches is even, return half of it
    if count % 2 == 0:
        return count // 2
    else:
        # If the count of mismatches is odd, return "Not Possible"
        return "Not Possible"

# Test the function with the provided test case
assert min_Swaps("1101", "1110") == 1