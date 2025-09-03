

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
# Define the function to find the maximum element in a list
def max_element(l: list):
    # Initialize the maximum value as negative infinity
    max_val = float('-inf')
    
    # Iterate through each element in the list
    for num in l:
        # Update the maximum value if the current number is greater than the previous maximum
        if num > max_val:
            max_val = num
    
    # Return the maximum value found
    return max_val

# Test cases to verify the correctness of the function
assert max_element([1, 2, 3]) == 3
assert max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) == 123