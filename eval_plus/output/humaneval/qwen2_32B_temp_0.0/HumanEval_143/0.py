
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
def words_in_sentence(sentence):
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
        Input: sentence = "This is a test"
        Output: "is"

    Example 2:
        Input: sentence = "lets go for swimming"
        Output: "go for"

    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    words = sentence.split()
    prime_length_words = [word for word in words if is_prime(len(word))]
    return ' '.join(prime_length_words)

# Test cases
assert words_in_sentence("This is a test") == "is"
assert words_in_sentence("lets go for swimming") == "go for"
assert words_in_sentence("I love programming") == "love"
assert words_in_sentence("Python is fun") == "is"
assert words_in_sentence("Hello world") == ""
assert words_in_sentence("The quick brown fox jumps over the lazy dog") == "The quick brown fox jumps over the lazy dog"
assert words_in_sentence("This is a test sentence with some words") == "is a test sentence with some words"
assert words_in_sentence("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z") == "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
assert words_in_sentence("This is a test sentence with some words and some more words") == "is a test sentence with some words and some more words"
assert words_in_sentence("This is a test sentence with some words and some more words and some more words") == "is a test sentence with some words and some more words and some more words"
assert words_in_sentence("This is a test sentence with some words and some more words and some more words and some more words") == "is a test sentence with some words and some more words and some more words and some more words"
assert words_in_sentence("This is a test sentence with some words and some more words and some more words and some more words and some more words") == "is a test sentence with some words and some more words and some more words and some more words and some more words"
assert words_in_sentence("This is a test sentence with some words and some more words and some more words and some more words and some more words and some more words") == "is a test sentence with some words and some more words and some more words and some more words and some more words and some more words"
assert words_in_sentence("This is a test sentence with some words and some more words and some more words and some more words and some more words and some more words and some more words") == "is a test sentence with some words and some more words and some more words and some more words and some more words and some more words and some more words"
assert words_in_sentence("This is a test sentence with some words and some more words and some more words and some more words and some more words and some more words and some more words and some more words") == "is a