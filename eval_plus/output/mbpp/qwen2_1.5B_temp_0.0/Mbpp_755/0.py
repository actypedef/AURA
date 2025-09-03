"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""
def second_smallest(numbers):
    # Remove duplicates from the list
    unique_numbers = set(numbers)
    
    # Check if there are at least two unique numbers
    if len(unique_numbers) < 2:
        return None
    
    # Sort the unique numbers in ascending order
    sorted_unique_numbers = sorted(unique_numbers)
    
    # Return the second smallest number
    return sorted_unique_numbers[1]

# Test cases
assert second_smallest([1, 2, -8, -2, 0, -2]) == -2
assert second_smallest([3, 5, 7, 9, 11]) == 3
assert second_smallest([-1, -2, -3, -4, -5]) == -2
assert second_smallest([]) == None
assert second_smallest([10]) == None