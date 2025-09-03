
def split_words(txt):
    '''
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    split_words("Hello world!") ➞ ["Hello", "world!"]
    split_words("Hello,world!") ➞ ["Hello", "world!"]
    split_words("abcdef") == 3 
    '''
def split_words(txt):
    # Check for whitespace and split if present
    if ' ' in txt:
        return txt.split()
    # Check for commas and split if present
    elif ',' in txt:
        return txt.split(',')
    else:
        # Count lowercase letters with odd positions in the alphabet
        count = sum(1 for char in txt if char.islower() and (ord(char) - ord('a')) % 2 == 0)
        return count

# Test cases to verify the correctness of the function