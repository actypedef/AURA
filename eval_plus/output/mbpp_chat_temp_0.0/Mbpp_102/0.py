"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""
def snake_to_camel(snake_str):
    # Split the snake_case string into words based on underscores
    words = snake_str.split('_')
    
    # Capitalize each word and join them together without any separators
    return ''.join(word.capitalize() for word in words)

# Test the function with the provided test case
assert snake_to_camel('python_program') == 'PythonProgram'
