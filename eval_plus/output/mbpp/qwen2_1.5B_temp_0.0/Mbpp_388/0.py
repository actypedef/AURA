"""
Write a python function to find the highest power of 2 that is less than or equal to n.
assert highest_Power_of_2(10) == 8
"""
def highest_Power_of_2(n):
    """
    Write a python function to find the highest power of 2 that is less than or equal to n.
    
    :param n: Integer
    :return: Integer
    """
    # Initialize the result variable
    result = 1
    
    # Loop until the current result is greater than n
    while result * 2 <= n:
        result *= 2
    
    return result

# Test cases to verify the correctness of the function
assert highest_Power_of_2(10) == 8
assert highest_Power_of_2(16) == 16
assert highest_Power_of_2(31) == 32
assert highest_Power_of_2(0) == 1
assert highest_Power_of_2(1) == 1