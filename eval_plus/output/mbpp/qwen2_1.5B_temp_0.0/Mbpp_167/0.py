"""
Write a python function to find the smallest power of 2 greater than or equal to n.
assert next_power_of_2(0) == 1
"""
def next_power_of_2(n):
    """
    Find the smallest power of 2 greater than or equal to n.

    Args:
    n (int): The number to find the next power of 2 for.

    Returns:
    int: The smallest power of 2 greater than or equal to n.
    """
    if n <= 0:
        return 1
    else:
        return 2 ** (n - 1).bit_length()

# Test cases
assert next_power_of_2(0) == 1
assert next_power_of_2(1) == 1
assert next_power_of_2(2) == 2
assert next_power_of_2(3) == 4
assert next_power_of_2(4) == 4
assert next_power_of_2(5) == 8
assert next_power_of_2(6) == 8
assert next_power_of_2(7) == 8
assert next_power_of_2(8) == 8
assert next_power_of_2(9) == 16
assert next_power_of_2(10) == 16
assert next_power_of_2(11) == 16
assert next_power_of_2(12) == 16
assert next_power_of_2(13) == 16
assert next_power_of_2(14) == 16
assert next_power_of_2(15) == 16
assert next_power_of_2(16) == 16
assert next_power_of_2(17) == 32
assert next_power_of_2(18) == 32
assert next_power_of_2(19) == 32
assert next_power_of_2(20) == 32
assert next_power_of_2(21) == 32
assert next_power_of_2(22) == 32
assert next_power_of_2(23) == 32
assert next_power_of_2(24) == 32
assert next_power_of_2(25) == 32
assert next_power_of_2(26) == 32
assert next_power_of_2(27) == 32
assert next_power_of_2(28) == 32
assert next_power_of_2(29) == 32
assert next_power_of_2(30) == 32
assert next_power_of_2(31) == 32
assert next_power_of_2(32) == 32
assert next_power_of_2(33) == 64
assert next_power_of_2(34) == 64
assert next_power_of_2(35) == 64
assert next_power_of_2(36) == 64
assert next_power_of_2(37) == 64
assert next_power_of_2(38) == 64
assert next_power_of_2(39) == 64
assert next_power_of_2(40) == 64
assert next_power_of_2(41) == 64
assert next_power_of_2(42) == 64
assert next_power_of_2(43) == 64
assert next_power_of_2(44) == 64
assert next_power_of_2(45) == 6