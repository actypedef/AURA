"""
Write a python function to find the length of the smallest list in a list of lists.
assert Find_Min_Length([[1],[1,2]]) == 1
"""
def Find_Min_Length(list_of_lists):
    # Initialize min_length to infinity
    min_length = float('inf')
    
    # Iterate through each sublist in the list of lists
    for sublist in list_of_lists:
        # Update min_length if current sublist's length is smaller
        if len(sublist) < min_length:
            min_length = len(sublist)
    
    return min_length

# Test cases to verify the correctness of the function
assert Find_Min_Length([[1],[1,2]]) == 1
assert Find_Min_Length([[3,4,5],[6,7,8,9],[10]]) == 1
assert Find_Min_Length([[],[1,2,3],[],[4,5]]) == 1
assert Find_Min_Length([[100],[200],[300]]) == 1
assert Find_Min_Length([[1,2,3,4,5],[6,7,8,9,10,11]]) == 2