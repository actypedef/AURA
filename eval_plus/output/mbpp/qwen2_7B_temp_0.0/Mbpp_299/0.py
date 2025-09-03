"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""
def max_aggregate(test_list):
    # Initialize an empty dictionary to store the aggregated scores for each person
    res = {}
    
    # Iterate through each tuple in the test list
    for key, val in test_list:
        # If the person's name already exists in the dictionary, add the score to their total
        if key in res:
            res[key] += val
        else:
            # Otherwise, create a new entry in the dictionary with the current score
            res[key] = val
    
    # Convert the dictionary back into a list of tuples and return it
    return list(res.items())

# Test the function with the provided test case
assert max_aggregate([('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), ('Juan Whelan', 122), ('Sabah Colley', 84)]) == [('Juan Whelan', 212), ('Sabah Colley', 172), ('Peter Nichols', 7)]
