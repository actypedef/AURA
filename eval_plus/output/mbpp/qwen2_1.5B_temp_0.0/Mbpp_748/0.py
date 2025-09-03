"""
Write a function to put spaces between words starting with capital letters in a given string.
assert capital_words_spaces("Python") == 'Python'
"""
def capital_words_spaces(s):
    # Split the string into words based on spaces
    words = s.split()
    
    # Iterate over each word
    for i in range(len(words)):
        # Check if the first character of the word is uppercase
        if words[i][0].isupper():
            # Add a space before the word
            words[i] = ' ' + words[i]
    
    # Join the words back into a single string
    return ''.join(words)

# Test cases to verify the correctness of the function
assert capital_words_spaces("Python") == 'Python'
assert capital_words_spaces("HelloWorld") == 'Hello World'
assert capital_words_spaces("ThisIsAString") == 'This Is A String'
assert capital_words_spaces("12345") == '12345'