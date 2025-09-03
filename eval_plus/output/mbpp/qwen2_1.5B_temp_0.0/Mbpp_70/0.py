"""
Write a function to find whether all the given tuples have equal length or not.
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
"""
def get_equal(tuples_list):
    # Check if the list of tuples is empty
    if not tuples_list:
        return True
    
    # Get the length of the first tuple
    first_tuple_length = len(tuples_list[0])
    
    # Compare the length of each tuple in the list with the length of the first tuple
    for tup in tuples_list:
        if len(tup) != first_tuple_length:
            return False
    
    return True

# Test cases
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
assert get_equal([(11, 22), (33, 44, 55, 66)]) == False
assert get_equal([]) == True