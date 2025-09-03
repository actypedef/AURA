"""
Write a python function to split a string into characters.
assert split('python') == ['p','y','t','h','o','n']
"""
def split(string):
    # Splitting the string into a list of characters using list comprehension
    return [char for char in string]

# Test the function with the provided test case
assert split('python') == ['p', 'y', 't', 'h', 'o', 'n']
