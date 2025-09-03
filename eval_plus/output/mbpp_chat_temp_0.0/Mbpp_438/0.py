"""
Write a function to count bidirectional tuple pairs.
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)] ) == 3
"""
def count_bidirectional(test_list):
    # Initialize a counter for bidirectional tuples
    res = 0
    
    # Iterate through each tuple in the list
    for ele in test_list:
        # Check if the reverse of the current tuple exists in the list
        if (ele[1], ele[0]) in test_list:
            # Increment the counter if a bidirectional pair is found
            res += 1
    
    # Return half the result since each pair is counted twice
    return res // 2

# Test the function with the provided test case
assert count_bidirectional([(5, 6), (1, 2), (6, 5), (9, 1), (6, 5), (2, 1)]) == 3