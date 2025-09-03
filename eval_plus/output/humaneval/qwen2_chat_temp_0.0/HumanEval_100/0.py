
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
    pile = []
    current_stones = n
    for _ in range(n):
        pile.append(current_stones)
        if n % 2 == 0:  # If n is even
            current_stones += 2  # Next even number
        else:  # If n is odd
            current_stones += 2  # Next odd number
    return pile

# Check function to verify the correctness of the solution
def check_solution():
    assert make_a_pile(3) == [3, 5, 7], "Test case 1 failed"
    assert make_a_pile(4) == [4, 6, 8, 10], "Test case 2 failed"
    assert make_a_pile(1) == [1], "Test case 3 failed"
    assert make_a_pile(2) == [2, 4], "Test case 4 failed"
    print("All test cases passed!")

check_solution()