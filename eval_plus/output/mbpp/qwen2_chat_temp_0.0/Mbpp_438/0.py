"""
Write a function to count bidirectional tuple pairs.
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
"""
def count_bidirectional(test_list):
    # Initialize a counter for bidirectional pairs
    res = 0
    
    # Iterate through each pair in the list
    for ele in test_list:
        # Check if there exists a reverse pair in the list
        if (ele[1], ele[0]) in test_list:
            res += 1
    
    return res

# Test the function with the provided test case
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]) == 3