"""
Write a function to find the combinations of sums with tuples in the given tuple list. https://www.geeksforgeeks.org/python-combinations-of-sum-with-tuples-in-tuple-list/
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]
"""
from itertools import combinations

def find_combinations(tuples_list):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over each tuple in the list
    for tup in tuples_list:
        # Generate all possible combinations of the current tuple
        for combo in combinations(tup, len(tup)):
            # Calculate the sum of the combination
            total_sum = sum(combo)
            # Append the tuple and its sum to the result list
            result.append((tup, total_sum))
    
    return result

# Test the function with the provided data point
assert find_combinations([(2, 4), (6, 7), (5, 1), (6, 10)]) == [(8, 11), (7, 5), (8, 14), (11, 8), (12, 17), (11, 11)]