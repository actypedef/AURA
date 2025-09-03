"""
Write a function to find tuples which have all elements divisible by k from the given list of tuples.
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
"""
def find_tuples(tuples_list, k):
    # Filter tuples where all elements are divisible by k
    result = [tup for tup in tuples_list if all(x % k == 0 for x in tup)]
    return result

# Test cases
assert find_tuples([(6, 24, 12), (7, 9, 6), (12, 18, 21)], 6) == [(6, 24, 12)]
assert find_tuples([(3, 6, 9), (10, 20, 30), (5, 10, 15)], 5) == [(5, 10, 15)]
assert find_tuples([(1, 2, 3), (4, 5, 6), (7, 8, 9)], 10) == []