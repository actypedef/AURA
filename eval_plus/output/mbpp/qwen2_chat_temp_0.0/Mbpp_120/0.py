"""
Write a function to find the maximum absolute product between numbers in pairs of tuples within a given list.
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==36
"""
def max_product_tuple(test_list):
    # Calculate the maximum product of pairs using a generator expression
    res = max(a * b for a, b in test_list)
    return res

# Test the function with the provided test case
assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
