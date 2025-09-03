"""
Write function to find the sum of all items in the given dictionary.
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
"""
def return_sum(dict):
    # Initialize sum to zero
    sums = 0
    
    # Iterate through each value in the dictionary and add it to the sum
    for i in dict.values():
        sums += i
    
    # Return the total sum of all values
    return sums

# Test the function with the provided test case
assert return_sum({'a': 100, 'b': 200, 'c': 300}) == 600
