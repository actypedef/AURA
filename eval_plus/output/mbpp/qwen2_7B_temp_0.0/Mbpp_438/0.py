"""
Write a function to count bidirectional tuple pairs.
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
"""
def count_bidirectional(test_list):
    # Initialize a set to store unique tuples
    res = set()
    
    # Iterate through each tuple in the list
    for sub in test_list:
        # Check if the reverse of the current tuple exists in the set
        if (sub[1], sub[0]) in res:
            # If found, add the original tuple to the result set
            res.add(sub)
        else:
            # Otherwise, add the reverse tuple to the set
            res.add((sub[1], sub[0]))
    
    # Return the number of unique bidirectional pairs
    return len(res)

# Test the function with the provided test case
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]) == 3
