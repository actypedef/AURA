"""
Write a function to find the number of elements that occurs before the tuple element in the given tuple.
assert count_first_elements((1, 5, 7, (4, 6), 10) ) == 3
"""
def count_first_elements(test_tup):
    # Count the number of elements before the first tuple element
    res = len([ele for ele in test_tup if not isinstance(ele, tuple)])
    return res

# Test the function with the provided test case
assert count_first_elements((1, 5, 7, (4, 6), 10)) == 3
