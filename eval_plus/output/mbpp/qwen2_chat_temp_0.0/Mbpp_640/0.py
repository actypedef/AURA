"""
Write a function to remove the parenthesis and what is inbetween them from a string.
assert remove_parenthesis(["python (chrome)"])==("python")
"""
def remove_parenthesis(text):
    # Iterate through each character in the input text
    for i in text:
        # Check if the current character is an opening parenthesis '('
        if i == "(":
            # If it is, slice the string from the beginning up to but not including the current index
            return text[:i]
    # If no parentheses are found, return the original text
    return text

# Test the function with the provided test case
assert remove_parenthesis(["python (chrome)"]) == "python"
