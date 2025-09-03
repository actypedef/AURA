"""
Write a python function to check whether a list is sublist of another or not.
assert is_Sub_Array([1,4,3,5],[1,2]) == False
"""
def is_Sub_Array(arr1, arr2):
    # Check if both lists are empty
    if len(arr1) == 0 and len(arr2) == 0:
        return True
    # If second list is empty but first list is not
    elif len(arr2) == 0:
        return True
    # If first list is empty but second list is not
    elif len(arr1) < len(arr2):
        return False
    # If elements of both lists are equal
    elif arr1[0] == arr2[0]:
        # Recursively check the rest of the elements
        return is_Sub_Array(arr1[1:], arr2[1:])
    else:
        # Move one element from the start of the first list and check again
        return is_Sub_Array(arr1[1:], arr2)

# Test the function with the provided test case
assert is_Sub_Array([1, 4, 3, 5], [1, 2]) == False