
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
    # Split the input string into a list of letters
    letters = test.split()
    
    # Count the occurrences of each letter using Counter from collections
    letter_counts = Counter(letters)
    
    # Find the maximum count of any letter
    max_count = max(letter_counts.values(), default=0)
    
    # Filter the letters that have the maximum count
    result = {letter: count for letter, count in letter_counts.items() if count == max_count}
    
    return result

# Test cases to verify the correctness of the function
assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
assert histogram('a b b a') == {'a': 2, 'b': 2}
assert histogram('a b c a b') == {'a': 2, 'b': 2}
assert histogram('b b b b a') == {'b': 4}
assert histogram('') == {}
