"""
Write a function to check if all the elements in tuple have same data type or not.
assert check_type((5, 6, 7, 3, 5, 6) ) == True
"""
def check_type(test_tup):
    # Check if all elements in the tuple have the same data type
    res = all(isinstance(ele, type(test_tup[0])) for ele in test_tup)
    return res

# Test the function with the provided test case
assert check_type((5, 6, 7, 3, 5, 6)) == True
