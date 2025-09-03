"""
Write a function to replace all occurrences of spaces, commas, or dots with a colon.
assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
"""
def replace_specialchar(s):
    # Replace spaces, commas, and dots with a colon
    s = s.replace(" ", ":")
    s = s.replace(",", ":")
    s = s.replace(".", ":")
    return s

# Test the function with the provided test case
assert replace_specialchar('Python language, Programming language.') == 'Python:language::Programming:language:'
