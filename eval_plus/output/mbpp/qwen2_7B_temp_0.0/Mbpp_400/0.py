"""
Write a function to extract the number of unique tuples in the given list.
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
"""
def extract_freq(test_list):
    # Use set comprehension to convert each tuple into a frozenset for immutability,
    # then convert the set of frozensets back into a list to count unique tuples
    res = len(list(set(frozenset(sub) for sub in test_list)))
    return res

# Test the function with the provided data point
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]) == 3
