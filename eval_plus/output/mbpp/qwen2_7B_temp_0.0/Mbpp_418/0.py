"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""
def Find_Max(test_list):
    # Use the max function with key=len to find the sublist with the maximum length
    res = max(test_list, key=len)
    return res

# Test the function with the provided test case
assert Find_Max([['A'], ['A', 'B'], ['A', 'B', 'C']]) == ['A', 'B', 'C']
