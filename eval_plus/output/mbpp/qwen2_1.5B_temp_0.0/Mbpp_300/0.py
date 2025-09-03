"""
Write a function to find the count of all binary sequences of length 2n such that sum of first n bits is same as sum of last n bits.
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)
"""
import math

def count_binary_seq(n):
    """
    Calculate the number of binary sequences of length 2n where the sum of the first n bits equals the sum of the last n bits.

    Args:
    n (int): The length of the binary sequence.

    Returns:
    float: The count of valid binary sequences.
    """
    # Initialize the result variable
    result = 0
    
    # Iterate over possible values for the sum of the first n bits
    for i in range(n + 1):
        # Calculate the number of ways to choose i bits out of n to be '1'
        ways_to_choose_ones = math.comb(n, i)
        
        # Since the sum of the first n bits must equal the sum of the last n bits,
        # the remaining n-i bits must also be '1'. Therefore, there are no other choices.
        # Thus, the total number of valid sequences is simply the number of ways to choose i bits out of n.
        result += ways_to_choose_ones
    
    return result

# Test the function with the provided test case
assert math.isclose(count_binary_seq(1), 2.0, rel_tol=0.001)