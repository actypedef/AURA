"""
Write a python function to find the sum of even numbers at even positions of a list.
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
"""
def sum_even_and_even_index(lst):
    # Initialize sum to zero
    total = 0
    
    # Iterate over the list using enumerate to get both index and value
    for i, num in enumerate(lst):
        # Check if the index is even and the number is even
        if i % 2 == 0 and num % 2 == 0:
            # Add the number to the total
            total += num
            
    return total

# Test the function with the provided test case
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30