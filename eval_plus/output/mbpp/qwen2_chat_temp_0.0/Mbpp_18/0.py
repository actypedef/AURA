"""
Write a function to remove characters from the first string which are present in the second string.
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
"""
def remove_dirty_chars(str1, str2):
    # Create a set of characters from str2 for quick lookup
    char_set = set(str2)
    
    # Use list comprehension to filter out characters in str1 that are not in char_set
    result = [char for char in str1 if char not in char_set]
    
    # Join the list back into a string and return it
    return ''.join(result)

# Test the function with the provided test case
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'