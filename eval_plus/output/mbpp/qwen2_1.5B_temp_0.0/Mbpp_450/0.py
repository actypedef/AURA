"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
"""
def extract_string(string_list, size):
    # Use list comprehension to filter strings based on their length
    return [s for s in string_list if len(s) == size]

# Test the function with provided data points
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8) == ['practice', 'solution']