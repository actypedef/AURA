
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
# Define the function to count vowels in a word
def vowels_count(s):
    # Initialize the count of vowels
    count = 0
    # Convert the string to lowercase for uniformity
    s = s.lower()
    # Check each character if it's a vowel
    for char in s:
        if char in "aeiou":
            count += 1
    # Check if 'y' is at the end and consider it as a vowel
    if s.endswith('y'):
        count += 1
    return count

# Test cases to verify the correctness of the function