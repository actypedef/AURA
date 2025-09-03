"""
Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
assert find_Rotations("aaaa") == 1
"""
def find_Rotations(str):
    # Concatenate the string with itself to handle rotations
    temp = str + str
    
    # Initialize the result as the length of the original string
    res = len(str)
    
    # Iterate through the concatenated string to find the minimum rotations
    for i in range(1, len(str)):
        count = 0
        
        # Compare characters from the current position to the end of the original string
        for j in range(len(str)):
            if temp[i + j] != str[j]:
                count += 1
        
        # Update the result if a smaller rotation count is found
        res = min(res, count)
    
    return res

# Test the function with the provided test case
assert find_Rotations("aaaa") == 1