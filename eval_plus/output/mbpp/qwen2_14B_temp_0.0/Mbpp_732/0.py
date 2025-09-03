"""
Write a function to replace all occurrences of spaces, commas, or dots with a colon.
assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
"""
import re

def replace_specialchar(text):
    # Replace spaces, commas, and dots with a colon
    return (re.sub("[ ,.]", ":", text))

# Test the function with the provided test case
assert replace_specialchar('Python language, Programming language.') == 'Python:language::Programming:language:'
