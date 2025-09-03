"""
Write a function to remove characters from the first string which are present in the second string.
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
"""
def remove_dirty_chars(main_str, dirty_str):
    # Create a set of characters in the dirty string for faster lookup
    dirty_set = set(dirty_str)
    
    # Use list comprehension to filter out characters from main_str that are present in dirty_set
    result = ''.join([char for char in main_str if char not in dirty_set])
    
    return result

# Test cases to verify the correctness of the solution
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
assert remove_dirty_chars("hello", "world") == "helo"
assert remove_dirty_chars("pythonprogramming", "pyth") == "onpragmming"