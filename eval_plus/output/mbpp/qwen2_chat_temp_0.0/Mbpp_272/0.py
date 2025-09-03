"""
Write a function that takes in a list of tuples and returns a list containing the rear element of each tuple.
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
"""
def rear_extract(test_list):
    # Extracting the last element from each tuple using list comprehension
    res = [sub[-1] for sub in test_list]
    return res

# Test the function with the provided test case
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
