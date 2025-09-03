"""
Write a python function to find the sum of even numbers at even positions of a list.
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
"""
def sum_even_and_even_index(arr):
    # Initialize sum to 0
    summation = 0
    
    # Iterate through the list with index and value
    for index, value in enumerate(arr):
        # Check if both index and value are even
        if index % 2 == 0 and value % 2 == 0:
            # Add the value to the sum
            summation += value
    
    return summation

# Test the function with the provided test case
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
