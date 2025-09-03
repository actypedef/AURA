"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""
def is_sublist(l1, l2):
    # Check if all elements of l2 are in l1
    return set(l2).issubset(set(l1))

# Test the function with the provided test case
assert is_sublist([2, 4, 3, 5, 7], [3, 7]) == False
