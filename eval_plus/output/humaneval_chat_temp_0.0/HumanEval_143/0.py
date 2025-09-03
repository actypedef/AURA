
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
from typing import *
from collections import *

def is_prime(n):
    """Check if a number is a prime number."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def words_in_sentence(sentence):
    """
    Return a string containing words from the original sentence whose lengths are prime numbers.
    
    :param sentence: A string representing a sentence with words separated by spaces.
    :return: A string with words of prime length, maintaining their original order.
    """
    # Split the sentence into words
    words = sentence.split()
    # Filter words where their length is a prime number
    prime_length_words = [word for word in words if is_prime(len(word))]
    # Join and return the filtered words
    return ' '.join(prime_length_words)

# Check function to verify the correctness of the solution
def check():
    assert words_in_sentence("This is a test") == "is", "Test case 1 failed"
    assert words_in_sentence("lets go for swimming") == "go for", "Test case 2 failed"
    print("All test cases passed!")

check()