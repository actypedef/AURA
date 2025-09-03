"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""
import re

def remove_parenthesis(items):
    # Loop through each item in the list
    for item in items:
        # Use regex to remove parenthesis and their contents
        return re.sub(r" ?\([^)]+\)", "", item)

# Test the function with the provided test case
assert remove_parenthesis(["python (chrome)"]) == "python"
