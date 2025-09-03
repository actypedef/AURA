"""
Write a function that takes in a list of tuples and returns a dictionary mapping each unique tuple to the number of times it occurs in the list.
assert check_occurences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)] ) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}
"""
def check_occurrences(tuples_list):
    # Create an empty dictionary to store the occurrences
    occurrence_dict = {}
    
    # Iterate over each tuple in the list
    for tup in tuples_list:
        # If the tuple is already in the dictionary, increment its count
        if tup in occurrence_dict:
            occurrence_dict[tup] += 1
        # Otherwise, add the tuple to the dictionary with a count of 1
        else:
            occurrence_dict[tup] = 1
    
    return occurrence_dict

# Test the function with the provided data point
assert check_occurrences([(3, 1), (1, 3), (2, 5), (5, 2), (6, 3)]) == {(1, 3): 2, (2, 5): 2, (3, 6): 1}