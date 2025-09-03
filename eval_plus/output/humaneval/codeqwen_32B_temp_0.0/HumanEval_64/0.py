
FIX = """
Add more test cases.
"""

def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
def vowels_count(s):
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count("abcde")
    2
    >>> vowels_count("ACEDY")
    3
    """
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for char in s.lower():
        if char in vowels:
            count += 1
    if s[-1].lower() == 'y':
        count += 1
    return count

# Test cases
assert vowels_count("abcde") == 2
assert vowels_count("ACEDY") == 3
assert vowels_count("hello") == 2
assert vowels_count("HELLO") == 2
assert vowels_count("python") == 1
assert vowels_count("PYTHON") == 1
assert vowels_count("y") == 1
assert vowels_count("Y") == 1
assert vowels_count("aeiouy") == 6
assert vowels_count("AEIOUY") == 6