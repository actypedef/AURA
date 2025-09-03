"""
Write a function to find words that are longer than n characters from a given list of words.
assert long_words(3,"python is a programming language")==['python','programming','language']
"""
def long_words(n, word_list):
    # Use list comprehension to filter out words longer than n characters
    return [word for word in word_list if len(word) > n]

# Test cases to verify the correctness of the function
assert long_words(3,"python is a programming language")==['python','programming','language']
assert long_words(4,"hello world this is a test")==['world','this','test']
assert long_words(1,"a b c d e f g h i j k l m n o p q r s t u v w x y z')==[]