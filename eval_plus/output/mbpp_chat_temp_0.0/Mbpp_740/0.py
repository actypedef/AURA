"""
Write a function to convert the given tuple to a key-value dictionary using adjacent elements. https://www.geeksforgeeks.org/python-convert-tuple-to-adjacent-pair-dictionary/
assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
"""
def tuple_to_dict(test_tup):
    # Using dictionary comprehension to pair adjacent elements
    res = dict(test_tup[idx : idx + 2] for idx in range(0, len(test_tup), 2))
    return res

# Test the function with the provided test case
assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
