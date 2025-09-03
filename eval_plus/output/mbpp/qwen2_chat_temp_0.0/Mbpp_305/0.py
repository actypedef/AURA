"""
Write a function to return two words from a list of words starting with letter 'p'.
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
"""
def start_withp(words):
    # Split each word in the list by spaces and filter those starting with 'P'
    p_words = [word.split()[0] for word in words if word.split()[0][0].lower() == 'p']
    
    # Return the first two words found that start with 'P' as a tuple
    return (p_words[0], p_words[1])

# Test the function with the provided test case
assert start_withp(["Python PHP", "Java JavaScript", "c c++"]) == ('Python', 'PHP')
