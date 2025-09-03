"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""
def is_samepatterns(arr1, arr2):
    # Check if both arrays have the same length
    if len(arr1) != len(arr2):
        return False
    
    # Create dictionaries to map elements from arr1 to arr2 and vice versa
    dict1 = {}
    dict2 = {}
    
    for i in range(len(arr1)):
        # If the element in arr1 is already in dict1, check if it matches the corresponding element in arr2
        if arr1[i] in dict1:
            if dict1[arr1[i]] != arr2[i]:
                return False
        else:
            dict1[arr1[i]] = arr2[i]
        
        # If the element in arr2 is already in dict2, check if it matches the corresponding element in arr1
        if arr2[i] in dict2:
            if dict2[arr2[i]] != arr1[i]:
                return False
        else:
            dict2[arr2[i]] = arr1[i]
    
    # If all checks pass, return True
    return True

# Test the function with the provided test case
assert is_samepatterns(["red", "green", "green"], ["a", "b", "b"]) == True