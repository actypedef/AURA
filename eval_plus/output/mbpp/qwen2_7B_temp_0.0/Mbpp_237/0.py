"""
Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
"""
def check_occurrences(test_list):
    # Initialize an empty dictionary to store the occurrences of each tuple
    res = {}
    
    # Iterate over each tuple in the test list
    for ele in test_list:
        # If the tuple is already in the dictionary, increment its count
        if ele in res:
            res[ele] += 1
        # If the tuple is not in the dictionary, add it with a count of 1
        else:
            res[ele] = 1
    
    # Return the resulting dictionary containing tuple counts
    return res

# Test the function with the provided data point
assert check_occurrences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
