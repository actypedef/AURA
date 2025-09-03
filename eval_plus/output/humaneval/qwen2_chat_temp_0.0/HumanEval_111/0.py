
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
    if not test:
        return {}
    
    # Split the input string into individual letters and count occurrences
    letter_counts = Counter(test.split())
    
    # Find the maximum count
    max_count = max(letter_counts.values(), default=0)
    
    # Filter letters that have the maximum count
    result = {letter: count for letter, count in letter_counts.items() if count == max_count}
    
    return result

# Check function to verify the correctness of the solution
def check():
    assert histogram('a b c') == {'a': 1, 'b': 1, 'c': 1}
    assert histogram('a b b a') == {'a': 2, 'b': 2}
    assert histogram('a b c a b') == {'a': 2, 'b': 2}
    assert histogram('b b b b a') == {'b': 4}
    assert histogram('') == {}
    print("All tests passed!")

check()