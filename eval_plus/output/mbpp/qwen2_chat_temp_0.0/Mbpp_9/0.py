"""
Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
assert find_Rotations("aaaa") == 1
"""
def find_Rotations(str):
    # Concatenate the string with itself to handle rotations
    str = str + str
    
    # Initialize the result as the length of the original string
    res = len(str)
    
    # Iterate through the string to check for repeating patterns
    for i in range(1, len(str)):
        if str[i] == str[0]:
            j = i
            while j < len(str) and str[j] == str[j - i]:
                j += 1
            
            # If a full cycle is found, update the result
            if j == len(str):
                res = min(res, i)
    
    return res

# Test the function with the provided test case
assert find_Rotations("aaaa") == 1