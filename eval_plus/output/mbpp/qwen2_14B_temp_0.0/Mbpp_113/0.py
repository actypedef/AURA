"""
Write a function to check if a string represents an integer or not.
assert check_integer("python")==False
"""
def check_integer(s):
    # Check if the string is equal to its integer representation as a string
    s = s.strip()
    try:
        int(s)
        return True
    except ValueError:
        return False

# Test the function with the provided test case
assert check_integer("python") == False
