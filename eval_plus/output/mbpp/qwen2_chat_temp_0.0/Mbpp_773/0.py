"""
Write a function to find the occurrence and position of the substrings within a string. Return None if there is no match.
assert occurance_substring('python programming, python language','python')==('python', 0, 6)
"""
def occurance_substring(string, substring):
    # Check if the substring exists in the string
    if substring in string:
        # Find the starting index of the first occurrence of the substring
        start = string.find(substring)
        # Calculate the length of the substring
        end = start + len(substring) - 1
        return (substring, start, end)
    else:
        # Return None if the substring is not found
        return None

# Test the function with the provided test case
assert occurance_substring('python programming, python language', 'python') == ('python', 0, 6)