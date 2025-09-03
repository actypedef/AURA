"""
Write a function to find the combinations of sums with tuples in the given tuple list. https://www.geeksforgeeks.org/python-combinations-of-sum-with-tuples-in-tuple-list/
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
"""
from itertools import combinations

def find_combinations(test_list):
    # Generate all possible pairs of tuples from the list
    temp = list(combinations(test_list, 2))
    
    # Calculate the sum of corresponding elements in each pair of tuples
    res = [(b1 + b2, a1 + a2) for (a1, b1), (a2, b2) in temp]
    
    return res

# Test the function with the provided test case
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
