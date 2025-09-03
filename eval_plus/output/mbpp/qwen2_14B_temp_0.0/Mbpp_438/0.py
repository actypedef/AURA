"""
Write a function to count bidirectional tuple pairs.
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
"""
def count_bidirectional(test_list):
    # Initialize the result counter
    res = 0
    
    # Create a set of tuples where the elements are sorted
    temp = set([tuple(sorted(sub)) for sub in test_list])
    
    # Iterate through the original list
    for ele in test_list:
        # Check if the reverse tuple exists in the set
        if (ele[1], ele[0]) in temp:
            res += 1
    
    # Return half the count since each pair is counted twice
    return res // 2

# Test the function with the provided test case
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]) == 3
