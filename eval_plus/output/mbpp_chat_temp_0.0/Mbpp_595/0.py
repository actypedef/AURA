"""
Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.
assert min_Swaps("1101","1110") == 1
"""
def min_Swaps(str1, str2):
    # Initialize swap count to zero
    swap = 0
    
    # Iterate over each character in the strings
    for i in range(len(str1)):
        # If characters at the same position are different
        if (str1[i] != str2[i]):
            # Increment swap count
            swap += 1
    
    # Return half of the swap count since each swap fixes two positions
    return int(swap / 2)

# Test the function with the provided test case
assert min_Swaps("1101", "1110") == 1