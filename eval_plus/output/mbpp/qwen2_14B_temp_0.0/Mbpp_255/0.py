"""
Write a function that takes in a list and length n, and generates all combinations (with repetition) of the elements of the list and returns a list with a tuple for each combination.
assert combinations_colors( ["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
"""
from itertools import combinations_with_replacement

def combinations_colors(colors, n):
    # Generate all combinations with repetition of the given list of colors
    return list(combinations_with_replacement(colors, n))

# Test the function with the provided test case
assert combinations_colors(["Red", "Green", "Blue"], 1) == [('Red',), ('Green',), ('Blue',)]
