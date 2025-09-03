"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
def start_withp(words):
    # Use a generator expression to filter words starting with 'P'
    p_words = (word for word in words if word.startswith('P'))
    # Convert the generator to a tuple and return it
    return tuple(p_words)

# Test the function with the provided test case
assert start_withp(["Python PHP", "Java JavaScript", "c c++"]) == ('Python', 'PHP')
