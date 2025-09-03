"""
Write a function to remove characters from the first string which are present in the second string.
assert remove_dirty_chars("probasscurve", "pros") == 'bacuve'
"""
def removeDirtyChars(str1, str2):
    # Create an array to mark the presence of characters in str2
    marked = [0] * 256
    
    # Mark the characters in str2
    for char in str2:
        marked[ord(char)] = 1
    
    # Reconstruct str1 by excluding characters marked in str2
    result = []
    for char in str1:
        if marked[ord(char)] == 0:
            result.append(char)
    
    return ''.join(result)

# Test the function with the provided test case
assert removeDirtyChars("probasscurve", "pros") == 'bacuve'