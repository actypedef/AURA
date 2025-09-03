"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""
def is_sublist(list1, list2):
    # Check if list2 is empty, which is always a sublist
    if not list2:
        return True
    
    # Check if list1 is empty but list2 is not, which means list2 cannot be a sublist
    if not list1:
        return False
    
    # Get the length of list2
    len_list2 = len(list2)
    
    # Iterate through list1 to find a matching sublist
    for i in range(len(list1) - len_list2 + 1):
        # Check if the sublist starting at index i matches list2
        if list1[i:i + len_list2] == list2:
            return True
    
    # If no matching sublist is found, return False
    return False

# Test the function with the provided test case
assert is_sublist([2, 4, 3, 5, 7], [3, 7]) == False
