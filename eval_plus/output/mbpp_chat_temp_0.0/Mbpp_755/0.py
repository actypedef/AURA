"""
Write a function to find the second smallest number in a list.
assert second_smallest([1, 2, -8, -2, 0, -2])==-2
"""
def second_smallest(numbers):
    # Initialize the first and second minimum values to positive infinity
    x = y = float('inf')
    
    for i in numbers:
        # Update the first minimum value if the current number is smaller
        if i < x:
            x, y = i, x
        # Update the second minimum value if the current number is between x and y
        elif x < i < y:
            y = i
    
    return y

# Test the function with the provided test case
assert second_smallest([1, 2, -8, -2, 0, -2]) == -2