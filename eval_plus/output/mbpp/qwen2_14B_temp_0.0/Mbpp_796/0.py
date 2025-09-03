"""
Write function to find the sum of all items in the given dictionary.
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
"""
def return_sum(dict):
    # Calculate the sum of all values in the dictionary
    sum = 0
    for i in dict.values():
        sum += i
    return sum

# Test the function with the provided test case
assert return_sum({'a': 100, 'b': 200, 'c': 300}) == 600
