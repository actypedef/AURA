

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to ignore case differences
    lower_string = string.lower()
    # Use a set to store unique characters
    unique_chars = set(lower_string)
    # Return the number of unique characters
    return len(unique_chars)

# Test cases