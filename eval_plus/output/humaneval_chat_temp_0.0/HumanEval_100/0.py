
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
    # Initialize the list to store the number of stones per level
    stone_levels = []
    
    # Start with the given number of stones for the first level
    current_stones = n
    
    # Loop through each level up to n
    for _ in range(n):
        # Append the current number of stones to the list
        stone_levels.append(current_stones)
        
        # Determine the next number of stones based on whether n is odd or even
        if n % 2 == 0:  # If n is even
            current_stones += 2  # Next even number
        else:  # If n is odd
            current_stones += 2  # Next odd number

    return stone_levels

# Example usage