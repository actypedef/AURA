"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""
def Find_Min(lst):
    # Initialize min_length as the length of the first sublist
    min_length = len(lst[0])
    
    # Iterate through each sublist in the list
    for sublist in lst:
        # Update min_length if the current sublist's length is smaller
        if len(sublist) < min_length:
            min_length = len(sublist)
    
    # Return the sublist with the minimum length
    return [sublist for sublist in lst if len(sublist) == min_length][0]

# Test the function with the provided test case
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]