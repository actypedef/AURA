"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""
def remove_parenthesis(items):
    # Iterate through each item in the list
    for i in items:
        # Find the index of the first opening parenthesis '('
        start = i.find('(')
        # Find the index of the closing parenthesis ')'
        end = i.find(')')
        # If both parentheses are found, slice the string to exclude them
        if start != -1 and end != -1:
            return i[:start] + i[end+1:]

# Test the function with the provided test case
assert remove_parenthesis(["python (chrome)"]) == "python"
