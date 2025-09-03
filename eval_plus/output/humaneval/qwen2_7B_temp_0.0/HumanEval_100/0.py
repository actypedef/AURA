
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
def make_a_pile(n):
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).
    
    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """
    # Initialize the list with the first level's stone count
    pile = [n]
    
    # Determine the next number based on whether n is odd or even
    next_number = n + 2 if n % 2 == 0 else n + 1
    
    # Add the next numbers for each subsequent level up to n levels
    for _ in range(1, n):
        pile.append(next_number)
        next_number += 2
    
    return pile

# Example usage