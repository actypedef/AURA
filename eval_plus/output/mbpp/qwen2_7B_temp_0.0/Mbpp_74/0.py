"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""
def is_samepatterns(patterns, colors):
    # Check if the length of patterns and colors arrays are equal
    if len(colors) != len(patterns):
        return False
    
    # Create a dictionary to map each pattern to its corresponding color
    pattern_to_color = {}
    
    # Iterate over the patterns and colors arrays
    for i in range(len(patterns)):
        pattern = patterns[i]
        color = colors[i]
        
        # If the pattern is already in the dictionary, check if the corresponding color is the same
        if pattern in pattern_to_color:
            if pattern_to_color[pattern] != color:
                return False
        
        # Otherwise, add the pattern-color pair to the dictionary
        else:
            pattern_to_color[pattern] = color
    
    # If all patterns match their corresponding colors, return True
    return True

# Test the function with the provided test case
assert is_samepatterns(["red", "green", "green"], ["a", "b", "b"]) == True