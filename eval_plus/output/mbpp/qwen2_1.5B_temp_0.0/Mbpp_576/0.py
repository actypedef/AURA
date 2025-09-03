"""
Write a python function to check whether a list is sublist of another or not.
assert is_Sub_Array([1,4,3,5],[1,2]) == False
"""
def is_Sub_Array(arr1, arr2):
    # Check if arr2 is empty
    if len(arr2) == 0:
        return True
    
    # Iterate through arr1 to find the first element of arr2
    for i in range(len(arr1)):
        if arr1[i] == arr2[0]:
            # If found, check if the rest of arr2 matches arr1 from the same index
            if arr1[i:i+len(arr2)] == arr2:
                return True
            
    # If no match is found, return False
    return False

# Test cases
assert is_Sub_Array([1,4,3,5],[1,2]) == False
assert is_Sub_Array([1,2,3,4,5], [2,3]) == True
assert is_Sub_Array([1,2,3,4,5], [1,2,3,4,5]) == True
assert is_Sub_Array([1,2,3,4,5], []) == True
assert is_Sub_Array([], [1,2,3,4,5]) == False