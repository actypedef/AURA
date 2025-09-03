"""
Write a function to find the maximum difference between available pairs in the given tuple list.
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""
def max_difference(test_list):
    # Calculate the absolute differences between each pair
    res = [abs(x - y) for x, y in test_list]
    # Return the maximum difference found
    return max(res)

# Test the function with the provided test case
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7