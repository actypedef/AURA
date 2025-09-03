

def strlen(string: str) -> int:
    """ Return length of given string
    >>> strlen('')
    0
    >>> strlen('abc')
    3
    """
# Define the function to calculate the length of a string
def strlen(string: str) -> int:
    # Use built-in len() function to get the length of the string
    return len(string)

# Test cases to verify the correctness of the function
def test_strlen():
    assert strlen("") == 0, "Test case for empty string failed"
    assert strlen("abc") == 3, "Test case for 'abc' failed"
    assert strlen("1234567890") == 10, "Test case for '1234567890' failed"
    print("All test cases passed!")

# Run the test function
test_strlen()