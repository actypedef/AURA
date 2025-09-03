
def select_words(s, n):
    """Given a string s and a natural number n, you have been tasked to implement 
    a function that returns a list of all words from string s that contain exactly 
    n consonants, in order these words appear in the string s.
    If the string s is empty then the function should return an empty list.
    Note: you may assume the input string contains only letters and spaces.
    Examples:
    select_words("Mary had a little lamb", 4) ==> ["little"]
    select_words("Mary had a little lamb", 3) ==> ["Mary", "lamb"]
    select_words("simple white space", 2) ==> []
    select_words("Hello world", 4) ==> ["world"]
    select_words("Uncle sam", 3) ==> ["Uncle"]
    """
def select_words(s, n):
    # Define vowels for comparison
    vowels = 'aeiouAEIOU'
    # Split the string into words
    words = s.split()
    # Initialize an empty list to store the result
    result = []

    # Iterate over each word in the list
    for word in words:
        # Count the number of consonants in the current word
        consonant_count = sum(1 for char in word if char.isalpha() and char not in vowels)
        
        # Check if the count matches the given number n
        if consonant_count == n:
            result.append(word)

    return result

# Test cases