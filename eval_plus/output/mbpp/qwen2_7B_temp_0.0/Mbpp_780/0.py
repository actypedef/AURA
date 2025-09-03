"""
Write a function to find the combinations of sums with tuples in the given tuple list. https://www.geeksforgeeks.org/python-combinations-of-sum-with-tuples-in-tuple-list/
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
"""
from itertools import product

def find_combinations(test_list):
    # Initialize an empty set to store unique combinations
    res = set()
    
    # Iterate through each pair of tuples in the list
    for x, y in product(test_list, repeat=2):
        # Calculate the sum of elements from both tuples
        res.add((x[0] + y[0], x[1] + y[1]))
    
    # Convert the set back to a sorted list and return it
    return sorted(list(res))

# Test the function with the provided test case
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]