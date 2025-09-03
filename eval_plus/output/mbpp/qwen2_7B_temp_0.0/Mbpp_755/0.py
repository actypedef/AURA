"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""
def second_smallest(numbers):
    # Initialize the minimum and second minimum values
    min_val = float('inf')
    sec_min = float('inf')
    
    for num in numbers:
        # Update the minimum value if the current number is smaller
        if num < min_val:
            sec_min = min_val
            min_val = num
        # Update the second minimum value if the current number is between min_val and sec_min
        elif min_val < num < sec_min:
            sec_min = num
    
    return sec_min

# Test the function with the provided test case
assert second_smallest([1, 2, -8, -2, 0, -2]) == -2
