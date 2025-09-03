"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""
def tuple_str_int(test_str):
    # Remove parentheses from the input string
    test_str = test_str.replace("(", "")
    test_str = test_str.replace(")", "")
    
    # Split the string into individual elements based on comma delimiter
    res = list(map(int, test_str.split(", ")))
    
    # Convert the list of integers back to a tuple
    return tuple(res)

# Test the function with the provided test case
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
