"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""
def second_smallest(numbers):
    # Initialize the first and second minimum values as infinity
    first = second = float('inf')
    
    # Iterate through each number in the list
    for num in numbers:
        if num <= first:
            # Update first and second if current number is smaller or equal
            second = first
            first = num
        elif num < second:
            # Update second only if current number is between first and second
            second = num
    
    # Return the second smallest number found
    return second

# Test the function with the provided test case
assert second_smallest([1, 2, -8, -2, 0, -2]) == -2