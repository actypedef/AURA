"""
Write a function to extract specified size of strings from a given list of string values.
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
"""
def extract_string(list1, n):
    # Use list comprehension to filter strings with length equal to n
    result = [x for x in list1 if len(x) == n]
    return result

# Test the function with the provided test case
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8) == ['practice', 'solution']
