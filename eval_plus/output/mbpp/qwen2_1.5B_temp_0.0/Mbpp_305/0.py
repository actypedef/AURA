"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
def start_withp(words):
    # Filter the list to include only those words that start with 'p'
    filtered_words = [word for word in words if word.startswith('p')]
    
    # Check if there are at least two words that start with 'p'
    if len(filtered_words) < 2:
        raise ValueError("The list must contain at least two words starting with 'p'")
    
    # Return the first two words from the filtered list
    return tuple(filtered_words[:2])

# Test the function with the provided test case
assert start_withp(["Python PHP", "Java JavaScript", "c c++"]) == ('Python', 'PHP')