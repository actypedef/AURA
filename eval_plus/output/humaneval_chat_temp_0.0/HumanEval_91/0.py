
def is_bored(S):
    """
    You'll be given a string of words, and your task is to count the number
    of boredoms. A boredom is a sentence that starts with the word "I".
    Sentences are delimited by '.', '?' or '!'.
   
    For example:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
import re

def is_bored(S):
    """
    Counts the number of sentences starting with 'I' as a measure of boredom.
    
    Args:
    S (str): A string containing multiple sentences.

    Returns:
    int: The number of sentences starting with 'I'.

    Example usage:
    >>> is_bored("Hello world")
    0
    >>> is_bored("The sky is blue. The sun is shining. I love this weather")
    1
    """
    # Split the text into sentences using regex to match '.', '?' or '!'
    sentences = re.split(r'[.?!]\s*', S)
    # Count sentences starting with 'I'
    boredom_count = sum(sentence.startswith('I') for sentence in sentences if sentence)
    return boredom_count

# Check function to verify the correctness of the solution
def check():
    assert is_bored("Hello world") == 0
    assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1
    assert is_bored("I am happy. Are you? Yes, I am!") == 2
    print("All tests passed!")

check()