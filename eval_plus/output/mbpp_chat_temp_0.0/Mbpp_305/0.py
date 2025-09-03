"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
def start_withp(words):
    # Use list comprehension to filter words starting with 'P' or 'p'
    p_words = [word for word in words if word[0] == 'P' or word[0] == 'p']
    
    # Return the first two words found that match the criteria
    return (p_words[0], p_words[1])

# Test the function with the provided test case
assert start_withp(["Python PHP", "Java JavaScript", "c c++"]) == ('Python', 'PHP')
