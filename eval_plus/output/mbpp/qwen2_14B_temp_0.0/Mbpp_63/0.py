"""
Write a function to find the maximum difference between available pairs in the given tuple list.
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""
def max_difference(test_list):
    # Calculate the absolute difference for each pair in the list
    temp = [abs(b - a) for a, b in test_list]
    # Find and return the maximum difference
    return max(temp)

# Test the function with the provided test case
assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
