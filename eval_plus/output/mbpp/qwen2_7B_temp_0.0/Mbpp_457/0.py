"""
Write a python function to find the sublist having minimum length.
assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
"""
def Find_Min(test_list):
    # Initialize min_len with a large value to ensure any list will be shorter initially
    min_len = float('inf')
    
    # Iterate through each sublist in the test_list
    for sub in test_list:
        # Update min_len if the current sublist's length is less than min_len
        min_len = min(min_len, len(sub))
    
    # Filter and return the sublist(s) that have the minimum length found
    res = [sub for sub in test_list if len(sub) == min_len]
    return res

# Test the function with the provided test case
assert Find_Min([[1], [1, 2], [1, 2, 3]]) == [1]
