"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""
def extract_rear(test_tup):
    # Extracting the last character from each string in the tuple
    res = [sub[-1] for sub in test_tup]
    return res

# Test cases to validate the solution
assert extract_rear(('Mers', 'for', 'Vers')) == ['s', 'r', 's']
