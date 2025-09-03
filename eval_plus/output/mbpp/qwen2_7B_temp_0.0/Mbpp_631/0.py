"""
Write a function to replace whitespaces with an underscore and vice versa in a given string.
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
"""
def replace_spaces(input_string):
    # Check if the input string contains spaces
    if " " in input_string:
        # Replace spaces with underscores
        return input_string.replace(" ", "_")
    else:
        # Replace underscores with spaces
        return input_string.replace("_", " ")

# Test the function with the provided test case
assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'