
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
    Count the number of sentences starting with the word 'I' in a given string.
    Sentences are delimited by '.', '?' or '!'.
    
    Args:
    S (str): The input string containing sentences.
    
    Returns:
    int: The number of sentences starting with 'I'.
    """
    # Split the string into sentences using regex to match '.', '?', or '!'
    sentences = re.split(r'[.?!]\s*', S)
    # Count sentences starting with 'I'
    boredom_count = sum(sentence.startswith('I') for sentence in sentences if sentence)
    return boredom_count

# Test cases