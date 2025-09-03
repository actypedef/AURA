"""
Write a function to remove characters from the first string which are present in the second string.
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
"""
def remove_dirty_chars(s1, s2):
    """
    Remove characters from the first string which are present in the second string.
    """
    # Convert the second string to a set for faster lookups
    s2_set = set(s2)
    
    # Use a list comprehension to filter out characters from the first string
    # that are present in the second string
    result = ''.join([char for char in s1 if char not in s2_set])
    
    return result

# Test cases
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
assert remove_dirty_chars("hello", "world") == 'he'
assert remove_dirty_chars("python", "python") == ''
assert remove_dirty_chars("python", "") == 'python'
assert remove_dirty_chars("", "python") == ''
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "python") == ''
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java") == 'python'
assert remove_dirty_chars("python", "java