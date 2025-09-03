"""
Write a function to convert a snake case string to camel case string.
assert snake_to_camel('python_program')=='PythonProgram'
"""
import re

def snake_to_camel(snake_str):
    # Split the snake case string by underscore and capitalize each segment
    components = snake_str.split('_')
    # Capitalize the first letter of each component and join them together
    return ''.join(x.capitalize() or '_' for x in components)

# Test the function with the provided test case
assert snake_to_camel('python_program') == 'PythonProgram'
