"""
Write a function to return a list of all pairs of consecutive items in a given list.
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
"""
def pair_wise(test_list):
    # Use list comprehension to iterate through the list and create tuples of consecutive elements
    res = [(test_list[idx], test_list[idx + 1]) for idx in range(len(test_list) - 1)]
    return res

# Test the function with the provided test case
assert pair_wise([1, 1, 2, 3, 3, 4, 4, 5]) == [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]