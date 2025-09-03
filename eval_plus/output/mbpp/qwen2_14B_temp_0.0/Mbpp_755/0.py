"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""
def second_smallest(numbers):
    # Remove duplicate elements by converting the list to a set, then convert back to a list
    unique_numbers = list(set(numbers))
    
    # Check if there are at least 2 unique numbers
    if len(unique_numbers) < 2:
        return None
    
    # Sort the unique numbers
    unique_numbers.sort()
    
    # Return the second smallest number
    return unique_numbers[1]

# Test the function with the provided test case
assert second_smallest([1, 2, -8, -2, 0, -2]) == -2
