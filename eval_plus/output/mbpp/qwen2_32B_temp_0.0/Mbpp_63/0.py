"""
Write a function to find the maximum difference between available pairs in the given tuple list.
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""
def max_difference(pairs):
    """
    Write a function to find the maximum difference between available pairs in the given tuple list.
    assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
    """
    max_diff = 0
    for pair in pairs:
        diff = abs(pair[0] - pair[1])
        if diff > max_diff:
            max_diff = diff
    return max_diff

# Test cases
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
assert max_difference([(1, 1), (2, 2), (3, 3)]) == 0
assert max_difference([(10, 5), (8, 3), (6, 1)]) == 5