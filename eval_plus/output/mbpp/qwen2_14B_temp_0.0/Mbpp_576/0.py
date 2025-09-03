"""
Write a python function to check whether a list is sublist of another or not.
assert is_Sub_Array([1,4,3,5],[1,2]) == False
"""
def is_Sub_Array(arr1, arr2):
    # Initialize pointers for arr1 and arr2
    i = 0
    j = 0
    
    # Traverse both arrays
    while i < len(arr1) and j < len(arr2):
        # If elements match, move the pointer of arr2
        if arr1[i] == arr2[j]:
            j += 1
        # Move the pointer of arr1
        i += 1
    
    # If all elements of arr2 were found in arr1
    return j == len(arr2)

# Test the function with the provided test case
assert is_Sub_Array([1, 4, 3, 5], [1, 2]) == False
