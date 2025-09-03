
def can_arrange(arr):
    """Create a function which returns the largest index of an element which
    is not greater than or equal to the element immediately preceding it. If
    no such element exists then return -1. The given array will not contain
    duplicate values.

    Examples:
    can_arrange([1,2,4,3,5]) = 3
    can_arrange([1,2,3]) = -1
    """
def can_arrange(arr):
    # Iterate through the array starting from the second element
    for i in range(1, len(arr)):
        # Check if the current element is less than the previous one
        if arr[i] <= arr[i-1]:
            # Return the current index if it's not greater than or equal to the previous one
            return i
    # Return -1 if no such element exists
    return -1

# Test cases