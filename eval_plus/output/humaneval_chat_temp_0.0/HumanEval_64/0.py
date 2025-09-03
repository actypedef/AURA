
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
# Define the function vowels_count to count vowels in a given word
def vowels_count(s):
    # Convert the input string to lowercase to handle both uppercase and lowercase inputs
    s = s.lower()
    # Initialize a counter for vowels
    count = 0
    # Iterate through each character in the string
    for char in s:
        # Check if the character is a vowel ('a', 'e', 'i', 'o', 'u')
        if char in "aeiou":
            count += 1
    # Check if the last character is 'y'
    if s.endswith('y'):
        count += 1
    # Return the total count of vowels
    return count

# Test cases to verify the correctness of the function