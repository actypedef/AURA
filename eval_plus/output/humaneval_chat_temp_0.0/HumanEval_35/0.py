

def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
def max_element(l: list):
    """Return maximum element in the list.
    >>> max_element([1, 2, 3])
    3
    >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
    123
    """
    if not l:  # Check if the list is empty
        return None  # Return None for an empty list
    
    max_val = l[0]  # Initialize max_val with the first element of the list
    
    for num in l:  # Iterate through each number in the list
        if num > max_val:  # If current number is greater than max_val
            max_val = num  # Update max_val to the current number
    
    return max_val  # Return the maximum value found

# Test cases