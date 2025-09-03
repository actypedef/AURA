"""
Write a python function to check whether all the characters are same or not.
assert all_Characters_Same("python") == False
"""
def all_Characters_Same(s):
    # Check if all characters in the string are the same
    return len(set(s)) == 1

# Test the function with the provided test case
assert all_Characters_Same("python") == False