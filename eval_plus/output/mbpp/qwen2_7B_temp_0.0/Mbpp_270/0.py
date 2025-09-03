"""
Write a python function to find the sum of even numbers at even positions of a list.
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
"""
def sum_even_and_even_index(lst):
    # Initialize the sum variable to zero
    total = 0
    
    # Iterate over the list using index and value
    for i, x in enumerate(lst):
        # Check if the index is even and the value is even
        if i % 2 == 0 and x % 2 == 0:
            # Add the value to the total sum
            total += x
    
    # Return the computed sum
    return total

# Test the function with the provided test case
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
