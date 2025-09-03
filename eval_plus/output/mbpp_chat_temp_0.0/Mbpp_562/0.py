"""
Write a python function to find the length of the longest sublists.
assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4
"""
def Find_Max_Length(lst):
    # Initialize max_length to store the maximum length found
    max_length = 0
    
    # Iterate through each sublist in the list
    for i in lst:
        # Update max_length if the current sublist's length is greater
        if len(i) > max_length:
            max_length = len(i)
    
    # Return the maximum length found
    return max_length

# Test the function with the provided test case
assert Find_Max_Length([[1], [1, 4], [5, 6, 7, 8]]) == 4
