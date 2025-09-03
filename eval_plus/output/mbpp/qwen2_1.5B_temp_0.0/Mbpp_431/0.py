"""
Write a function that takes two lists and returns true if they have at least one common element.
assert common_element([1,2,3,4,5], [5,6,7,8,9])==True
"""
def common_element(list1, list2):
    # Check if there is any common element between the two lists
    return len(set(list1) & set(list2)) > 0

# Test cases to verify the correctness of the function
assert common_element([1,2,3,4,5], [5,6,7,8,9]) == True
assert common_element([1,2,3,4,5], [6,7,8,9,10]) == False
assert common_element([], []) == False
assert common_element(['a', 'b', 'c'], ['d', 'e', 'f']) == False
assert common_element(['x', 'y', 'z'], ['w', 'x', 'y']) == True