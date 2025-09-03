"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""
def extract_rear(strings):
    """
    Extracts the last character from each string in the provided tuple.

    Args:
    strings (tuple): A tuple containing strings.

    Returns:
    list: A list containing the last characters of each string in the input tuple.
    """
    return [string[-1] for string in strings]

# Test cases to verify the correctness of the solution
assert extract_rear(('Mers', 'for', 'Vers')) == ['s', 'r', 's']
assert extract_rear(('Python', 'Programming', 'Language')) == ['n', 'g', 'a']
assert extract_rear(('Hello', 'World', 'Python')) == ['o', 'd', 'n']