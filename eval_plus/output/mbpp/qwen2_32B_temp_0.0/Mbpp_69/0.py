"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""
def is_sublist(list1, list2):
    """
    Check whether list1 contains list2 as a sublist.
    """
    if not list2:
        return True
    if len(list2) > len(list1):
        return False
    for i in range(len(list1) - len(list2) + 1):
        if list1[i:i+len(list2)] == list2:
            return True
    return False

# Test cases
assert is_sublist([2,4,3,5,7],[3,7])==False
assert is_sublist([2,4,3,5,7],[4,3])==True
assert is_sublist([2,4,3,5,7],[2,4,3,5,7])==True
assert is_sublist([2,4,3,5,7],[2,4,3,5,7,8])==False
assert is_sublist([2,4,3,5,7],[2,4,3,5,7,8,9])==False
assert is_sublist([2,4,3,5,7],[2,4,3,5,7,8,9,10])==False
assert is_sublist([2,4,3,5,7],[2,4,3,5,7,8,9,10,11])==False
assert is_sublist([2,4,3,5,7],[2,4,3,5,7,8,9,10,11,12])==False
assert is_sublist([2,4,3,5,7],[2,4,3,5,7,8,9,10,11,12,13])==False
assert is_sublist([2,4,3,5,7],[2,4,3,5,7,8,9,10,11,12,13,14])==False
assert is_sublist([2,4,3,5,7],[2,4,3,5,7,8,9,10,11,12,13,14,15])==False
assert is_sublist([2,4,3,5,7],[2,4,3,5,7,8,9,10,11,12,13,14,15,16])==False
assert is_sublist([2,4,3,5,7],[2,4,3,5,7,8,9,10,11,12,13,14,15,16,17])==False
assert is_sublist([2,4,3,5,7],[2,4,3,5,7,8,9,10,11,12,13,14,15,16,17,18])==False
assert is_sublist([2,4,3,5,7],[2,4,3,5,7,8,9,10,11,12,13,14,15,16,17,18,19])==False
assert is_sublist([2,4,3,5,7],[2,4,3,5,7,8,9,10,11,12,13,14,15,16,17,18,19,20])==False
assert is_sublist([