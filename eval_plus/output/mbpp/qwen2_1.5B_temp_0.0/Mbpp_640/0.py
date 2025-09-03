"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""
def remove_parenthesis(strings):
    # Use regular expression to find all substrings enclosed in parentheses
    result = ''.join([s for s in strings if '(' not in s and ')' not in s])
    return result

# Test cases
assert remove_parenthesis(["python (chrome)"]) == "python"
assert remove_parenthesis(["hello (world)", "(python)", "test"]) == "helloworld test"
assert remove_parenthesis(["(nested (parentheses))", "no parentheses here"]) == "no parentheses here"