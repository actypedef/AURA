
def histogram(test):
    """Given a string representing a space separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}

    """
from collections import Counter

def histogram(test):
    """Given a string representing a space-separated lowercase letters, return a dictionary
    of the letter with the most repetition and containing the corresponding count.
    If several letters have the same occurrence, return all of them.
    
    Example:
    histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    histogram('a b b a') == {'a': 2, 'b': 2}
    histogram('a b c a b') == {'a': 2, 'b': 2}
    histogram('b b b b a') == {'b': 4}
    histogram('') == {}
    """
    if not test:  # Check if the input string is empty
        return {}
    
    # Split the input string into individual characters and count their occurrences
    char_counts = Counter(test.split())
    
    # Find the maximum occurrence value
    max_occurrence = max(char_counts.values())
    
    # Create a dictionary to hold the letters with the maximum occurrence
    result = {letter: count for letter, count in char_counts.items() if count == max_occurrence}
    
    return result

# Test cases
assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
assert histogram('a b b a') == {'a': 2, 'b': 2}
assert histogram('a b c a b') == {'a': 2, 'b': 2}
assert histogram('b b b b a') == {'b': 4}
assert histogram('') == {}