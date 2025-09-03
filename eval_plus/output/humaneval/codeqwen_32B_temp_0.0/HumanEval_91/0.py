
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
    sentences = S.split('.')
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()]
    count = 0
    for sentence in sentences:
        if sentence.startswith('I'):
            count += 1
    return count

# Test cases
assert is_bored("Hello world") == 0
assert is_bored("The sky is blue. The sun is shining. I love this weather") == 1
assert is_bored("I am bored. I am tired. I am hungry.") == 3
assert is_bored("I am not bored. I am not tired. I am not hungry.") == 0
assert is_bored("I am bored. I am tired. I am hungry. I am happy.") == 4
assert is_bored("I am not bored. I am not tired. I am not hungry. I am not happy.") == 0
assert is_bored("I am bored. I am tired. I am hungry. I am happy. I am sad.") == 5
assert is_bored("I am not bored. I am not tired. I am not hungry. I am not happy. I am not sad.") == 0
assert is_bored("I am bored. I am tired. I am hungry. I am happy. I am sad. I am angry.") == 6
assert is_bored("I am not bored. I am not tired. I am not hungry. I am not happy. I am not sad. I am not angry.") == 0
assert is_bored("I am bored. I am tired. I am hungry. I am happy. I am sad. I am angry. I am confused.") == 7
assert is_bored("I am not bored. I am not tired. I am not hungry. I am not happy. I am not sad. I am not angry. I am not confused.") == 0
assert is_bored("I am bored. I am tired. I am hungry. I am happy. I am sad. I am angry. I am confused. I am frustrated.") == 8
assert is_bored("I am not bored. I am not tired. I am not hungry. I am not happy. I am not sad. I am not angry. I am not confused. I am not frustrated.") == 0
assert is_bored("I am bored. I am tired. I am hungry. I am happy. I am sad. I am angry. I am confused. I am frustrated. I am overwhelmed.") == 9
assert is_bored("I am not bored. I am not tired. I am not hungry. I am not happy. I am not sad. I am not angry. I am not confused. I am not frustrated. I am not overwhelmed.") == 0
assert is_bored("I am bored. I am tired. I am hungry. I am happy. I am sad. I am angry. I am confused. I am frustrated. I am overwhelmed. I am exhausted.") == 10
assert is_bored("I am not bored. I am not tired. I am not hungry. I am not