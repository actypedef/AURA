"""
Write a function to replace all occurrences of spaces, commas, or dots with a colon.
assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
"""
def replace_specialchar(text):
    # Replace spaces, commas, or dots with a colon
    return text.replace(" ", ":").replace(",", ":").replace(".", ":")

# Test cases to verify the correctness of the solution
assert replace_specialchar('Python language, Programming language.') == ('Python:language::Programming:language:')
assert replace_specialchar('Hello, World!') == 'Hello:World:'
assert replace_specialchar('Data analysis, Machine learning.') == ('Data:analysis::Machine:learning:')