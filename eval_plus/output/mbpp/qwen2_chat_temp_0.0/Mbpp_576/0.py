"""
Write a python function to check whether a list is sublist of another or not.
assert is_Sub_Array([1,4,3,5],[1,2]) == False
"""
def is_Sub_Array(list1, list2):
    # Check if all elements of list2 are present in list1
    return set(list2).issubset(set(list1))

# Test the function with the provided test case
assert is_Sub_Array([1, 4, 3, 5], [1, 2]) == False
