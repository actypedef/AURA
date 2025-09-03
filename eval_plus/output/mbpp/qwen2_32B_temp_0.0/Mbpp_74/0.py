"""
Write a function to check whether it follows the sequence given in the patterns array.
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
"""
def is_samepatterns(patterns, words):
    if len(patterns) != len(words):
        return False
    pattern_to_word = {}
    word_to_pattern = {}
    for pattern, word in zip(patterns, words):
        if pattern in pattern_to_word and pattern_to_word[pattern] != word:
            return False
        if word in word_to_pattern and word_to_pattern[word] != pattern:
            return False
        pattern_to_word[pattern] = word
        word_to_pattern[word] = pattern
    return True

assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True
assert is_samepatterns(["red","green","green"], ["a", "b", "c"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "a"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "b", "c"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "b", "b"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "b", "b", "c"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "b", "b", "b"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "b", "b", "b", "c"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "b", "b", "b", "b"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "b", "b", "b", "b", "c"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "b", "b", "b", "b", "b"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "b", "b", "b", "b", "b", "c"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "b", "b", "b", "b", "b", "b"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "b", "b", "b", "b", "b", "b", "c"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "b", "b", "b", "b", "b", "b", "b"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "b", "b", "b", "b", "b", "b", "b", "c"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "c"])==False
assert is_samepatterns(["red","green","green"], ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"])==False
assert is_samepatterns