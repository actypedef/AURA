"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""
def Find_Min(lists):
    # Initialize min_len with the length of the first sublist
    min_len = len(lists[0])
    
    # Iterate through each sublist in the list
    for i in range(1, len(lists)):
        # Update min_len if a shorter sublist is found
        if len(lists[i]) < min_len:
            min_len = len(lists[i])
    
    # Return the first sublist with the minimum length
    return lists[min_len - 1]

# Test the function with the provided test case
assert Find_Min([[1], [1, 2], [1, 2, 3]]) == [1]
