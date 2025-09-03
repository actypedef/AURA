"""
Write a python function to split a string into characters.
assert split('python') == ['p','y','t','h','o','n']
"""
def split(s):
    return list(s)

# Test cases
assert split('python') == ['p', 'y', 't', 'h', 'o', 'n']
assert split('hello world') == ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
assert split('1234567890') == ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
assert split('') == []