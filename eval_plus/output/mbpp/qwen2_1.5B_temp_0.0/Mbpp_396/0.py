"""
Write a function to check whether the given string starts and ends with the same character or not.
assert check_char("abba") == "Valid"
"""
def check_char(s):
    # Check if the first and last characters of the string are the same
    return "Valid" if s[0] == s[-1] else "Invalid"

# Test cases to verify the correctness of the function
assert check_char("abba") == "Valid"
assert check_char("abc") == "Invalid"
assert check_char("a") == "Valid"
assert check_char("") == "Invalid"