"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""
def find_tuples(tuples_list, k):
    """
    This function finds tuples which have all elements divisible by k from the given list of tuples.
    """
    result = []
    for tup in tuples_list:
        if all(element % k == 0 for element in tup):
            result.append(tup)
    return result

# Test cases
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 3) == [(6, 24, 12), (12, 18, 21)]
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 2) == [(6, 24, 12), (12, 18, 21)]
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 1) == [(6, 24, 12), (7, 9, 6), (12, 18, 21)]
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 0) == []
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], -1) == []
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], -2) == []
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], -3) == []
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], -6) == []
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], -12) == []
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], -24) == []
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], -12) == []
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], -24) == []
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], -12) == []
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], -24) == []
assert find_tuples([(6,