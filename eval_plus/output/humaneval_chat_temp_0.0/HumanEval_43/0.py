

def pairs_sum_to_zero(l):
    """
    pairs_sum_to_zero takes a list of integers as an input.
    it returns True if there are two distinct elements in the list that
    sum to zero, and False otherwise.
    >>> pairs_sum_to_zero([1, 3, 5, 0])
    False
    >>> pairs_sum_to_zero([1, 3, -2, 1])
    False
    >>> pairs_sum_to_zero([1, 2, 3, 7])
    False
    >>> pairs_sum_to_zero([2, 4, -5, 3, 5, 7])
    True
    >>> pairs_sum_to_zero([1])
    False
    """
def pairs_sum_to_zero(l):
    # Create a set to store seen numbers
    seen = set()
    
    # Iterate through each number in the list
    for num in l:
        # Check if the negation of the current number exists in the set
        if -num in seen:
            return True
        # Add the current number to the set
        seen.add(num)
    
    # Return False if no pair sums to zero
    return False

# Test cases