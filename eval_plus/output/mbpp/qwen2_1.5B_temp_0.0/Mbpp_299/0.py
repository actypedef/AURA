"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""
def max_aggregate(tuples_list):
    # Initialize variables to store the maximum aggregate and its associated name
    max_aggregate = (None, 0)
    
    # Iterate through each tuple in the list
    for name, score in tuples_list:
        # Update the maximum aggregate if the current score is higher
        if score > max_aggregate[1]:
            max_aggregate = (name, score)
    
    return max_aggregate

# Test the function with the provided data point
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)]) == ('Juan Whelan', 212)