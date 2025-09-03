"""
Write a function that takes in a list of tuples and returns a list containing the rear element of each tuple.
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
"""
def rear_extract(test_list):
    # Using list comprehension to extract the last element from each tuple in the list
    res = [tup[-1] for tup in test_list]
    return res

# Test case to verify the correctness of the function
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
