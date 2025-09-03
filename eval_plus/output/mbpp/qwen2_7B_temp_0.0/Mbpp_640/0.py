"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""
import re

def remove_parenthesis(items):
    # Iterate over each item in the list
    for i in range(len(items)):
        # Use regular expression to find and replace text within parentheses
        items[i] = re.sub(r'\s*\([^)]+\)', '', items[i])
    return items

# Test the function with the provided test case
assert remove_parenthesis(["python (chrome)"]) == ("python")
