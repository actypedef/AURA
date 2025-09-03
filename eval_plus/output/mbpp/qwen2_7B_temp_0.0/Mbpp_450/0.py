"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
"""
def extract_string(string_list, size):
    # Filter the list to include only strings of the specified size
    result = [string for string in string_list if len(string) == size]
    return result

# Test the function with the provided test case
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8) == ['practice', 'solution']
