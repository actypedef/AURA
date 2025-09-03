"""
Write a function to find words that are longer than n characters from a given list of words.
assert long_words(3,"python is a programming language")==['python','programming','language']
"""
def long_words(n, str):
    # Split the string into words using space as a delimiter
    words = str.split(" ")
    
    # Use list comprehension to filter out words longer than 'n' characters
    result = [word for word in words if len(word) > n]
    
    return result

# Test the function with the provided test case
assert long_words(3, "python is a programming language") == ['python', 'programming', 'language']
