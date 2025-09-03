"""
Write a function to check whether the given string starts and ends with the same character or not.
assert check_char("abba") == "Valid"
"""
def check_char(s):
    # Check if the first and last characters of the string are the same
    if s[0] == s[-1]:
        return "Valid"
    else:
        return "Invalid"

# Test the function with the provided test case
assert check_char("abba") == "Valid"
