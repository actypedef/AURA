"""
Write a function to convert tuple string to integer tuple.
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)
"""
def tuple_str_int(tuple_str):
    # Remove parentheses from the input string
    tuple_str = tuple_str[1:-1]
    
    # Split the string into individual elements
    elements = tuple_str.split(',')
    
    # Convert each element to an integer
    int_elements = [int(element) for element in elements]
    
    # Return the resulting integer tuple
    return tuple(int_elements)

# Test the function with the provided test case
assert tuple_str_int("(7, 8, 9)") == (7, 8, 9)