"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""
def is_samepatterns(strs, patterns):
    # Create a dictionary to map each string to its pattern
    d = {}
    
    # Iterate over both lists simultaneously
    for i, j in zip(strs, patterns):
        # Check if the string is already in the dictionary
        if i not in d:
            # If the pattern is also not in the dictionary, add both mappings
            if j not in d.values():
                d[i] = j
            else:
                return False
        # If the string is in the dictionary but maps to a different pattern, return False
        elif d[i] != j:
            return False
    
    # If all checks pass, return True
    return True

# Test the function with the provided test case
assert is_samepatterns(["red","green","green"], ["a", "b", "b"]) == True
