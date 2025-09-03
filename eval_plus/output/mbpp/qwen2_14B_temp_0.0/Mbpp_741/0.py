"""
Write a python function to check whether all the characters are same or not.
assert all_Characters_Same("python") == False
"""
def all_Characters_Same(s):
    # Check if the length of the set of characters in the string is 1
    return len(set(s)) == 1

# Test the function with the provided test case
assert all_Characters_Same("python") == False
