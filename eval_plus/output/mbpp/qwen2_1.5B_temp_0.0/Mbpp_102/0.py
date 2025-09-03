"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""
def snake_to_camel(snake_str):
    # Split the snake case string into words using underscore as the delimiter
    words = snake_str.split('_')
    
    # Capitalize the first letter of each word except the first one and join them together
    camel_str = words[0].lower() + ''.join(word.capitalize() for word in words[1:])
    
    return camel_str

# Test cases to verify the correctness of the solution
assert snake_to_camel('python_program') == 'PythonProgram'
assert snake_to_camel('this_is_a_test_string') == 'ThisIsATestString'
assert snake_to_camel('convert_this_to_camel_case') == 'ConvertThisToCamelCase'