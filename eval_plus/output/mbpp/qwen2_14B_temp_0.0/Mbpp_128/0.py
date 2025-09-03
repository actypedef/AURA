"""
Write a function to find words that are longer than n characters from a given list of words.
assert long_words(3,"python is a programming language")==['python','programming','language']
"""
def long_words(n, sentence):
    # Split the sentence into words
    words = sentence.split(" ")
    # Filter words longer than n characters
    long_words_list = [word for word in words if len(word) > n]
    return long_words_list

# Test the function with the provided test case
assert long_words(3, "python is a programming language") == ['python', 'programming', 'language']
