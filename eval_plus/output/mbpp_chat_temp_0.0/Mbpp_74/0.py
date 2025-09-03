"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""
def is_samepatterns(strs, patterns):
    # Create dictionaries to map strings to patterns and patterns to strings
    str_to_pattern = {}
    pattern_to_str = {}
    
    # Iterate through each string and its corresponding pattern
    for s, p in zip(strs, patterns):
        # Check if the string is already mapped to a different pattern
        if s in str_to_pattern and str_to_pattern[s] != p:
            return False
        # Check if the pattern is already mapped to a different string
        if p in pattern_to_str and pattern_to_str[p] != s:
            return False
        
        # Map the string to the pattern and vice versa
        str_to_pattern[s] = p
        pattern_to_str[p] = s
    
    # If all mappings are consistent, return True
    return True

# Test the function with the provided test case
assert is_samepatterns(["red", "green", "green"], ["a", "b", "b"]) == True