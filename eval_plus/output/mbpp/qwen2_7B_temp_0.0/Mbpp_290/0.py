"""
Write a function to find the list of maximum length in a list of lists.
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]])==(3, [13, 15, 17])
"""
def max_length(lst):
    # Initialize variables to store the maximum length and the longest sublist
    max_len = 0
    longest_sublist = []
    
    # Iterate through each sublist in the input list
    for sublist in lst:
        # Check if the current sublist is longer than the previously found longest sublist
        if len(sublist) > max_len:
            max_len = len(sublist)
            longest_sublist = sublist
    
    # Return the maximum length and the longest sublist as a tuple
    return (max_len, longest_sublist)

# Test the function with the provided test case
assert max_length([[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]) == (3, [13, 15, 17])
