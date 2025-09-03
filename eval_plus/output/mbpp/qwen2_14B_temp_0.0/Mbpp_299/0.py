"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""
def max_aggregate(test_list):
    # Create a dictionary to store the aggregate scores for each name
    res = {}
    
    # Iterate through each tuple in the list
    for sub in test_list:
        # If the name is already in the dictionary, add the score to the existing total
        if sub[0] in res:
            res[sub[0]] += sub[1]
        # If the name is not in the dictionary, initialize the total with the current score
        else:
            res[sub[0]] = sub[1]
    
    # Find the name with the maximum aggregate score
    max_name = max(res, key=res.get)
    
    # Return the name and the maximum aggregate score as a tuple
    return (max_name, res[max_name])

# Test the function with the provided test case
assert max_aggregate([('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), ('Juan Whelan', 122), ('Sabah Colley', 84)]) == ('Juan Whelan', 212)
