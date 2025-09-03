"""
Write a function to replace whitespaces with an underscore and vice versa in a given string.
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
"""
def replace_spaces(input_string):
    # Replace spaces with underscores
    result = input_string.replace(" ", "_")
    # Replace underscores back to spaces
    return result.replace("_", " ")

# Test cases to verify the correctness of the solution
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
assert replace_spaces('Hello World') == 'Hello_World'
assert replace_spaces('Python Programming') == 'Python_Programming'