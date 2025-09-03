"""
Write a function to return a list of all pairs of consecutive items in a given list.
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
"""
def pair_wise(lst):
    # Use list comprehension to create pairs of consecutive elements
    return [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]

# Test the function with the provided test case
assert pair_wise([1, 1, 2, 3, 3, 4, 4, 5]) == [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
