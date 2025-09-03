"""
Write a function to calculate the maximum aggregate from the list of tuples.
assert max_aggregate([('Juan Whelan',90),('Sabah Colley',88),('Peter Nichols',7),('Juan Whelan',122),('Sabah Colley',84)])==('Juan Whelan', 212)
"""
def max_aggregate(test_list):
    # Initialize an empty dictionary to store the sum of values for each key
    res_dict = {}
    
    # Iterate through each tuple in the test list
    for key, val in test_list:
        # If the key is already in the dictionary, add the value to its current total
        if key in res_dict:
            res_dict[key] += val
        else:
            # Otherwise, set the initial value for this key
            res_dict[key] = val
    
    # Find the key with the maximum value in the dictionary
    res_key = max(res_dict, key=res_dict.get)
    
    # Return the key-value pair with the maximum value
    return (res_key, res_dict[res_key])

# Test the function with the provided test case
assert max_aggregate([('Juan Whelan', 90), ('Sabah Colley', 88), ('Peter Nichols', 7), ('Juan Whelan', 122), ('Sabah Colley', 84)]) == ('Juan Whelan', 212)