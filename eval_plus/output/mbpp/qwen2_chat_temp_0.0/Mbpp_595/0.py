"""
Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.
assert min_Swaps("1101","1110") == 1
"""
def min_Swaps(str1, str2):
    # Initialize swap count to zero
    swap_count = 0
    
    # Iterate through each character in the strings
    for i in range(len(str1)):
        # If characters at the current position are different
        if str1[i] != str2[i]:
            # Find the first '1' in str2 from the current position to the end
            j = i + 1
            while j < len(str2) and str2[j] != '1':
                j += 1
            
            # If no '1' found, return -1 (impossible to make them equal)
            if j == len(str2):
                return -1
            
            # Swap the found '1' with the current position
            str2 = str2[:j] + '0' + str2[j+1:]
            str2 = str2[:i] + '1' + str2[i+1:]
            
            # Increment swap count
            swap_count += 1
    
    # Return the total number of swaps
    return swap_count

# Test the function with the provided test case
assert min_Swaps("1101", "1110") == 1