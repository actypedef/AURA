"""
Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.
assert min_Swaps("1101","1110") == 1
"""
def min_Swaps(str1, str2):
    # Initialize variables to store the counts of '0' and '1'
    cnt0 = 0
    cnt1 = 0
    
    # Iterate through both strings simultaneously
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            # If characters at the same position differ, check which character is different
            if str1[i] == '0':
                cnt0 += 1
            else:
                cnt1 += 1
    
    # Calculate the minimum number of swaps required
    return (cnt0 + cnt1) // 2

# Test the function with the provided test case
assert min_Swaps("1101", "1110") == 1