"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
"""
def extract_string(str1, size):
    # Use list comprehension to filter strings with length equal to the specified size
    result = [x for x in str1 if len(x) == size]
    return result

# Test the function with the provided test case
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8) == ['practice', 'solution']
