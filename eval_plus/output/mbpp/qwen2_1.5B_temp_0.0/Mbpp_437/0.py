"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""
def remove_odd(s):
    return ''.join([char for char in s if ord(char) % 2 == 0])

# Test cases
assert remove_odd("python") == "yhn"
assert remove_odd("hello world") == "el ol"
assert remove_odd("123456789") == "2468"
assert remove_odd("") == ""
assert remove_odd("a") == ""