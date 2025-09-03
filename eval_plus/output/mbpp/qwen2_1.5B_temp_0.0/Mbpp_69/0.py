"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""
def is_sublist(main_list, sub_list):
    # Check if the main list is empty
    if not main_list:
        return False
    
    # Iterate through the main list to find the first occurrence of the sub_list's first element
    for i in range(len(main_list)):
        if main_list[i] == sub_list[0]:
            # If found, check if the remaining elements match the sub_list
            if main_list[i:i+len(sub_list)] == sub_list:
                return True
    
    # If no match is found, return False
    return False

# Test cases
assert is_sublist([2,4,3,5,7],[3,7])==False
assert is_sublist([1,2,3,4,5],[1,2])==True
assert is_sublist([1,2,3,4,5],[6,7])==False
assert is_sublist([], [1,2])==False
assert is_sublist([1,2,3,4,5], [])==True