"""
Write a function to find whether all the given tuples have equal length or not.
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
"""
def get_equal(test_list):
    # Check if all tuples in the list have the same length
    res = all(len(sub) == len(test_list[0]) for sub in test_list)
    return res

# Test the function with the provided test case
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
