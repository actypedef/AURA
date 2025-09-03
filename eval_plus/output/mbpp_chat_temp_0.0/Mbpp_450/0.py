"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
"""
def extract_string(string_list, n):
    # Use list comprehension to filter strings longer than or equal to length n
    result = [string for string in string_list if len(string) >= n]
    return result

# Test the function with the provided test case
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8) == ['practice', 'solution']
