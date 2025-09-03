"""
Write a function to convert the given tuple to a key-value dictionary using adjacent elements. https://www.geeksforgeeks.org/python-convert-tuple-to-adjacent-pair-dictionary/
assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
"""
def tuple_to_dict(test_tup):
    # Initialize an empty dictionary
    res = {}
    
    # Iterate over the tuple in steps of 2 to form key-value pairs
    for i in range(0, len(test_tup), 2):
        # Assign each pair to the dictionary
        res[test_tup[i]] = test_tup[i + 1]
    
    return res

# Test the function with the provided test case
assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
