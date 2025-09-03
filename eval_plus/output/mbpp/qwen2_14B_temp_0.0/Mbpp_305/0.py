"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
def start_withp(text1):
    # Filter words that start with 'p' or 'P'
    result = [word for word in text1 if word.lower().startswith('p')]
    
    # Return the first two words that start with 'p'
    return result[:2]

# Test the function with the provided test case
assert start_withp(["Python PHP", "Java JavaScript", "c c++"]) == ('Python', 'PHP')
