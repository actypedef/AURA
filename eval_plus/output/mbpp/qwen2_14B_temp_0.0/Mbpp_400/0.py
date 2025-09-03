"""
Write a function to extract the number of unique tuples in the given list.
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)] ) == 3
"""
def extract_freq(test_list):
    # Use a set to store unique tuples
    res = set()
    
    # Iterate through each tuple in the list
    for sub in test_list:
        # Sort the tuple to handle tuples with the same elements in different orders
        sub = tuple(sorted(sub))
        # Add the sorted tuple to the set
        res.add(sub)
    
    # Return the number of unique tuples
    return len(res)

# Test the function with the provided test case
assert extract_freq([(3, 4), (1, 2), (4, 3), (5, 6)]) == 3
