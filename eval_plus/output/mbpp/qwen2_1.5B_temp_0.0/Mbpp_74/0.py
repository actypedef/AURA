"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""
def is_samepatterns(patterns, sequences):
    # Check if the lengths of patterns and sequences are equal
    if len(patterns) != len(sequences):
        return False
    
    # Iterate through each pattern and sequence pair
    for pattern, sequence in zip(patterns, sequences):
        # Check if the current pattern matches the current sequence
        if pattern != sequence:
            return False
    
    # If all patterns match the sequences, return True
    return True

# Test cases
assert is_samepatterns(["red","green","green"], ["a", "b", "b"]) == True
assert is_samepatterns(["red","green","blue"], ["a", "b", "c"]) == False
assert is_samepatterns([], []) == True
assert is_samepatterns(["a", "b", "a"], ["a", "b", "a"]) == True
assert is_samepatterns(["a", "b", "c"], ["a", "b", "d"]) == False