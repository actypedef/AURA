"""
Write function to find the sum of all items in the given dictionary.
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
"""
def return_sum(dictionary):
    """
    Write function to find the sum of all items in the given dictionary.
    
    assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
    """
    total = 0
    for value in dictionary.values():
        total += value
    return total

# Test cases
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
assert return_sum({'x': 50, 'y': 75, 'z': 100}) == 225
assert return_sum({}) == 0