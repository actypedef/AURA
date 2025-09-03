"""
Write a python function to find the element of a list having maximum length.
assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
"""
def Find_Max(list1):
    # Use the max function with key=len to find the sublist with the maximum length
    return max(list1, key=len)

# Test the function with the provided test case
assert Find_Max([['A'], ['A', 'B'], ['A', 'B', 'C']]) == ['A', 'B', 'C']
