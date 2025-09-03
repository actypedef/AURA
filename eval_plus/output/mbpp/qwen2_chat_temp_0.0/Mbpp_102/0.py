"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""
def snake_to_camel(snake_str):
    # Split the string by underscores and capitalize each segment
    return ''.join(word.capitalize() or '_' for word in snake_str.split('_'))

# Test the function with the provided test case
assert snake_to_camel('python_program') == 'PythonProgram'
