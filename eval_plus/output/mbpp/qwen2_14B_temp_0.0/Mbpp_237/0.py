"""
Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
"""
from collections import defaultdict

def check_occurences(test_list):
    # Initialize a defaultdict to store the occurrences of each tuple
    res = defaultdict(int)
    
    # Iterate through each tuple in the list
    for sub in test_list:
        # Increment the count for the tuple
        res[sub] += 1
    
    # Convert defaultdict to a dictionary before returning
    return dict(res)

# Test the function with the provided test case
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
