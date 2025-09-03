"""
Write function to find the sum of all items in the given dictionary.
assert return_sum({'a': 100, 'b':200, 'c':300}) == 600
"""
def return_sum(dict):
    # Initialize sum to zero
    sum = 0
    
    # Iterate through each item in the dictionary
    for i in dict.values():
        # Add the value of each item to the sum
        sum += i
    
    # Return the total sum of all values
    return sum

# Test the function with the provided test case
assert return_sum({'a': 100, 'b': 200, 'c': 300}) == 600
