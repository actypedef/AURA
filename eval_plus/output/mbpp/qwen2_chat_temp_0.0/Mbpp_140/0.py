"""
Write a function to flatten the list of lists into a single set of numbers.
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
"""
def extract_singly(test_list):
    # Flatten the list of lists using list comprehension
    res = [ele for sub in test_list for ele in sub]
    return res

# Test the function with the provided test case
assert set(extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])) == set([3, 4, 5, 7, 1])
