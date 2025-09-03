"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""
def extract_rear(test_tup):
    # Using list comprehension to iterate through each string in the tuple
    # and extracting the last character using negative indexing [-1]
    res = [sub[-1] for sub in test_tup]
    return res

# Test the function with the provided test case
assert extract_rear(('Mers', 'for', 'Vers')) == ['s', 'r', 's']
