"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""
def Find_Max(lst):
    # Initialize max_length to 0 and max_element to None
    max_length = 0
    max_element = None
    
    # Iterate through each sublist in the list
    for sublist in lst:
        # Update max_length if current sublist's length is greater than max_length
        if len(sublist) > max_length:
            max_length = len(sublist)
            max_element = sublist
    
    return max_element

# Test the function with the provided test case
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']