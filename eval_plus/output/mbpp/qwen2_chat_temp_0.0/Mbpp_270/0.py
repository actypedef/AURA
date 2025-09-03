"""
Write a python function to find the sum of even numbers at even positions of a list.
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
"""
def sum_even_and_even_index(lst):
    # Initialize the sum variable to zero
    s = 0
    
    # Iterate over the list using enumerate to get both index and value
    for i, x in enumerate(lst):
        # Check if the index is even and the value is even
        if i % 2 == 0 and x % 2 == 0:
            # Add the value to the sum
            s += x
            
    # Return the computed sum
    return s

# Test the function with the provided test case
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30