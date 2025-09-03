"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""
def max_aggregate(test_list):
    # Initialize an empty dictionary to store the sum of values for each key
    res = {}
    
    # Iterate through each tuple in the list
    for key, val in test_list:
        # If the key already exists in the dictionary, add the value to it
        if key in res:
            res[key] += val
        else:
            # Otherwise, initialize the key with the current value
            res[key] = val
    
    # Return the key-value pair with the maximum value
    return max(res.items(), key=lambda x: x[1])

# Test the function with the provided test case
assert max_aggregate([('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), ('Juan Whelan', 122), ('Sabah Colley', 84)]) == ('Juan Whelan', 212)