"""
Write a python function which takes a list of integers and counts the number of possible unordered pairs where both elements are unequal.
assert count_Pairs([1,2,1],3) == 2
"""
from itertools import combinations

def count_Pairs(arr, n):
    # Generate all possible pairs using combinations
    comb = combinations(arr, 2)
    count = 0
    
    # Iterate through each pair and count if they are unequal
    for i in comb:
        if i[0] != i[1]:
            count += 1
            
    return count

# Test the function with the provided test case
assert count_Pairs([1, 2, 1], 3) == 2
