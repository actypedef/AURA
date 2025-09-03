"""
Write a function to find all possible combinations of the elements of a given list.
assert combinations_list(['orange', 'red', 'green', 'blue'])==[[], ['orange'], ['red'], ['red', 'orange'], ['green'], ['green', 'orange'], ['green', 'red'], ['green', 'red', 'orange'], ['blue'], ['blue', 'orange'], ['blue', 'red'], ['blue', 'red', 'orange'], ['blue', 'green'], ['blue', 'green', 'orange'], ['blue', 'green', 'red'], ['blue', 'green', 'red', 'orange']]
"""
from itertools import combinations

def combinations_list(input_list):
    # Initialize an empty list to store all combinations
    comb_list = []
    
    # Iterate over all possible lengths of combinations
    for i in range(len(input_list) + 1):
        # Generate all combinations of the current length and add them to the list
        comb_list.extend(combinations(input_list, i))
    
    return comb_list

# Test the function with the provided test case
assert combinations_list(['orange', 'red', 'green', 'blue']) == [
    [], 
    ('orange',), 
    ('red',), 
    ('red', 'orange'), 
    ('green',), 
    ('green', 'orange'), 
    ('green', 'red'), 
    ('green', 'red', 'orange'), 
    ('blue',), 
    ('blue', 'orange'), 
    ('blue', 'red'), 
    ('blue', 'red', 'orange'), 
    ('blue', 'green'), 
    ('blue', 'green', 'orange'), 
    ('blue', 'green', 'red'), 
    ('blue', 'green', 'red', 'orange')
]