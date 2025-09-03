

def count_distinct_characters(string: str) -> int:
    """ Given a string, find out how many distinct characters (regardless of case) does it consist of
    >>> count_distinct_characters('xyzXYZ')
    3
    >>> count_distinct_characters('Jerry')
    4
    """
def count_distinct_characters(string: str) -> int:
    # Convert the string to lowercase to ensure case insensitivity
    lower_string = string.lower()
    # Use set to store unique characters and convert back to list to get the count
    distinct_chars = list(set(lower_string))
    return len(distinct_chars)

# Test cases
assert count_distinct_characters('xyzXYZ') == 3
assert count_distinct_characters('Jerry') == 4
