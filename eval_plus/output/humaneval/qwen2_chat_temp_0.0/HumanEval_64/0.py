
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
# Define the function to count vowels in a given word
def vowels_count(s):
    # Convert the string to lowercase to handle both uppercase and lowercase inputs
    s = s.lower()
    # Initialize a counter for vowels
    count = 0
    # Iterate through each character in the string
    for char in s:
        # Check if the character is a vowel (including 'y' at the end)
        if char in "aeiou" or (char == 'y' and s[-1] == 'y'):
            # Increment the counter if the character is a vowel
            count += 1
    # Return the total count of vowels
    return count

# Test cases to verify the correctness of the function
assert vowels_count("abcde") == 2, "Test case 1 failed"
assert vowels_count("ACEDY") == 3, "Test case 2 failed"
assert vowels_count("rhythm") == 0, "Test case 3 failed"
assert vowels_count("SYZYGY") == 1, "Test case 4 failed"
assert vowels_count("quickly") == 2, "Test case 5 failed"