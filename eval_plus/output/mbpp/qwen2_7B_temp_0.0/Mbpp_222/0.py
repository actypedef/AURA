"""
Write a function to check if all the elements in tuple have same data type or not.
assert check_type((5, 6, 7, 3, 5, 6) ) == True
"""
def check_type(test_tup):
    # Check if all elements in the tuple have the same data type
    res = len(set(map(type, test_tup))) == 1
    return res

# Test the function with the provided test case
assert check_type((5, 6, 7, 3, 5, 6)) == True
