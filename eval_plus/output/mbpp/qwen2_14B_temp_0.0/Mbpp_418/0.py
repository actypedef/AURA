"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""
def Find_Max(lst):
    # Initialize the maximum length and the result list
    maxLength = 0
    res = []
    
    # Iterate through each sublist in the list
    for i in lst:
        # Check if the current sublist's length is greater than maxLength
        if len(i) > maxLength:
            maxLength = len(i)
            res = i
    
    return res

# Test the function with the provided test case
assert Find_Max([['A'], ['A', 'B'], ['A', 'B', 'C']]) == ['A', 'B', 'C']
