"""
Write a function to check whether a list contains the given sublist or not.
assert is_sublist([2,4,3,5,7],[3,7])==False
"""
def is_sublist(a, b):
    # Check if all elements of 'b' are present in 'a'
    return set(b).issubset(set(a))

# Test the function with the provided test case
assert is_sublist([2, 4, 3, 5, 7], [3, 7]) == False
