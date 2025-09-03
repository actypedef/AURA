"""
Write a function to remove characters from the first string which are present in the second string.
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
"""
def remove_dirty_chars(str1, str2):
    # Create a set of characters from the second string for quick lookup
    dirty_chars = set(str2)
    
    # Use list comprehension to filter out characters present in the second string
    result = ''.join([char for char in str1 if char not in dirty_chars])
    
    return result

# Test the function with the provided test case
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
