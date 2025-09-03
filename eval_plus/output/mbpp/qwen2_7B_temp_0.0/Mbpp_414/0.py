"""
Write a python function to check whether any value in a sequence exists in a sequence or not.
assert overlapping([1,2,3,4,5],[6,7,8,9]) == False
"""
def overlapping(list1, list2):
    # Check if there is any common element between list1 and list2
    return bool(set(list1) & set(list2))

# Test the function with the provided test case
assert overlapping([1, 2, 3, 4, 5], [6, 7, 8, 9]) == False
