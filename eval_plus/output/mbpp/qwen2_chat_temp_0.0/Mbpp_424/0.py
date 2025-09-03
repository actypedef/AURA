"""
Write a function to extract only the rear index element of each string in the given tuple.
assert extract_rear(('Mers', 'for', 'Vers') ) == ['s', 'r', 's']
"""
def extract_rear(test_tup):
    # Using list comprehension to iterate through each string in the tuple
    res = [ele[-1] for ele in test_tup]
    return res

# Test the function with the provided test case
assert extract_rear(('Mers', 'for', 'Vers')) == ['s', 'r', 's']
