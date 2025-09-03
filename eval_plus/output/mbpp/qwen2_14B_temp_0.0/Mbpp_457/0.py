"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""
def Find_Min(lst):
    # Initialize min_len with the length of the first sublist
    min_len = len(lst[0])
    
    # Iterate through each sublist in the list
    for l in lst:
        # Update min_len if a shorter sublist is found
        if len(l) < min_len:
            min_len = len(l)
    
    # Filter and return all sublists that have the minimum length
    res = [l for l in lst if len(l) == min_len]
    return res

# Test the function with the provided test case
assert Find_Min([[1], [1, 2], [1, 2, 3]]) == [1]
