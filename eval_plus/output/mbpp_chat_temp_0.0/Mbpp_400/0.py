"""
Write a function to extract the number of unique tuples in the given list.
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
"""
def extract_freq(test_list):
    # Convert each tuple in the list to a sorted tuple to ensure uniqueness
    res = len(set(tuple(sorted(sub)) for sub in test_list))
    return res

# Test the function with the provided test case
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]) == 3
