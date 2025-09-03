"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""
def find_tuples(test_list, K):
    # Use list comprehension to filter tuples where all elements are divisible by K
    res = [tup for tup in test_list if all(x % K == 0 for x in tup)]
    return res

# Test the function with the provided test case
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]