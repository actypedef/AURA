"""
Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
"""
def check_occurences(test_list):
    # Initialize an empty dictionary to store the count of each tuple
    res = {}
    
    # Iterate over each tuple in the test list
    for ele in test_list:
        # If the tuple is already in the dictionary, increment its count
        if ele in res:
            res[ele] += 1
        # Otherwise, add the tuple to the dictionary with a count of 1
        else:
            res[ele] = 1
    
    # Return the dictionary containing the counts of each tuple
    return res

# Test the function with the provided test case
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}