"""
Write a function to remove uneven elements in the nested mixed tuple.
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)
"""
def extract_even(mixed_tuple):
    # Initialize an empty list to store even numbers
    even_numbers = []
    
    # Iterate through each element in the mixed tuple
    for item in mixed_tuple:
        # Check if the item is a tuple itself
        if isinstance(item, tuple):
            # Recursively call the function on the nested tuple
            even_numbers.extend(extract_even(item))
        else:
            # Check if the item is an integer and even
            if isinstance(item, int) and item % 2 == 0:
                even_numbers.append(item)
    
    # Return the list of even numbers
    return tuple(even_numbers)

# Test the function with the provided data point
assert extract_even((4, 5, (7, 6, (2, 4)), 6, 8)) == (4, (6, (2, 4)), 6, 8)