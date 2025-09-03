"""
Write a function to remove odd characters in a string.
assert remove_odd("python")==("yhn")
"""
def remove_odd(s):
    # Initialize an empty string to store even-indexed characters
    s1 = ''
    # Iterate over the string, considering only even indices
    for i in range(len(s)):
        if i % 2 != 0:
            s1 = s1 + s[i]
    return s1

# Test the function with the provided test case
assert remove_odd("python") == "yhn"
