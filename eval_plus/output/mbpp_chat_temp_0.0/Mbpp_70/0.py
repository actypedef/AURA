"""
Write a function to find whether all the given tuples have equal length or not.
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
"""
def get_equal(test_list):
    # Check if all tuples in the list have the same length as the first tuple
    res = len(set(len(sub) for sub in test_list)) == 1
    return res

# Test the function with the provided test case
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
