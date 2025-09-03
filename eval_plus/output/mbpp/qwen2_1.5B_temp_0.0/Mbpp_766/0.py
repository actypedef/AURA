"""
Write a function to return a list of all pairs of consecutive items in a given list.
assert pair_wise([1,1,2,3,3,4,4,5])==[(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]
"""
def pair_wise(lst):
    # Initialize an empty list to store the pairs
    result = []
    # Iterate through the list using range(len(lst) - 1)
    for i in range(len(lst) - 1):
        # Append each pair of consecutive elements to the result list
        result.append((lst[i], lst[i + 1]))
    # Return the resulting list of pairs
    return result

# Test the function with the provided test case
assert pair_wise([1,1,2,3,3,4,4,5]) == [(1, 1), (1, 2), (2, 3), (3, 3), (3, 4), (4, 4), (4, 5)]