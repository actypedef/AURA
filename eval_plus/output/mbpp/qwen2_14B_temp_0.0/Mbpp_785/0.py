"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""
def tuple_str_int(test_str):
    # Remove the parentheses from the string
    test_str = test_str.replace("(", "").replace(")", "")
    
    # Split the string by commas and convert each element to an integer
    res = tuple(int(num) for num in test_str.split(','))
    
    return res

# Test the function with the provided test case
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
