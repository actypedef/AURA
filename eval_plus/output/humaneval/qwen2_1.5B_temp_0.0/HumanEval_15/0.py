

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
# Define the function to generate a string of space-separated numbers
def string_sequence(n: int) -> str:
    # Use list comprehension to create a list of numbers from 0 to n
    number_list = [str(i) for i in range(n + 1)]
    # Join the list elements into a single string separated by spaces
    return " ".join(number_list)

# Test cases to verify the correctness of the function
def test_string_sequence():
    assert string_sequence(0) == '0', "Test case 1 failed"
    assert string_sequence(5) == '0 1 2 3 4 5', "Test case 2 failed"
    print("All test cases passed!")

# Run the test function
test_string_sequence()