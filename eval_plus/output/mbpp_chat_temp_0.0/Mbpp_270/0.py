"""
Write a python function to find the sum of even numbers at even positions of a list.
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30
"""
def sum_even_and_even_index(lst):
    # Initialize the sum variable to store the result
    total_sum = 0
    
    # Iterate over the list using enumerate to get both index and value
    for i, num in enumerate(lst):
        # Check if the index is even and the number is even
        if i % 2 == 0 and num % 2 == 0:
            # Add the number to the total sum
            total_sum += num
    
    # Return the computed sum
    return total_sum

# Test the function with the provided test case
assert sum_even_and_even_index([5, 6, 12, 1, 18, 8]) == 30