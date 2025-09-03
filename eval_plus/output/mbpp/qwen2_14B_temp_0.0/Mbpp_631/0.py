"""
Write a function to replace whitespaces with an underscore and vice versa in a given string.
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
"""
def replace_spaces(text):
    # Replace spaces with underscores
    result = text.replace(' ', '_')
    
    # Replace underscores with spaces
    result = result.replace('_', ' ')
    
    return result

# Test the function with the provided test case
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
