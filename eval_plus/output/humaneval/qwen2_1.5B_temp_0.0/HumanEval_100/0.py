
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
# Importing necessary packages
from typing import List

def make_a_pile(n: int) -> List[int]:
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
    # Initialize an empty list to store the number of stones in each level
    result = []
    # Start from the first level with n stones
    current_stones = n
    
    # Loop through each level up to n
    for _ in range(n):
        # Append the current number of stones to the result list
        result.append(current_stones)
        
        # Determine the next number of stones based on whether the current number is odd or even
        if current_stones % 2 == 0:
            # If even, add the next even number
            current_stones += 2
        else:
            # If odd, add the next odd number
            current_stones += 1
    
    return result

# Function to check the correctness of the make_a_pile function
def check_function():
    assert make_a_pile(3) == [3, 5, 7], "Test case 1 failed"
    assert make_a_pile(4) == [4, 6, 8, 10], "Test case 2 failed"
    assert make_a_pile(1) == [1], "Test case 3 failed"
    print("All test cases passed!")

# Run the check function to verify the solution
check_function()