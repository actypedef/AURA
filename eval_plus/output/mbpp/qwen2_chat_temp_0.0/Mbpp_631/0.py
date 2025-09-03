"""
Write a function to replace whitespaces with an underscore and vice versa in a given string.
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
"""
def replace_spaces(input_string):
    # Replace underscores with spaces if they exist
    if '_' in input_string:
        return input_string.replace('_', ' ')
    # Replace spaces with underscores if no underscores are present
    else:
        return input_string.replace(' ', '_')

# Test the function with the provided test case
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
