
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
    # Iterate over the array starting from the second last element
    for i in range(len(arr) - 2, -1, -1):
        # Check if the current element is less than the next one
        if arr[i] < arr[i + 1]:
            # Return the current index as it's the largest index satisfying the condition
            return i
    # If no such element is found, return -1
    return -1

# Test cases to verify the correctness of the function
assert can_arrange([1,2,4,3,5]) == 3
assert can_arrange([1,2,3]) == -1