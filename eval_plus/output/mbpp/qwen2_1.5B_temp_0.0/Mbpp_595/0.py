"""
Write a python function to count minimum number of swaps required to convert one binary number represented as a string to another.
assert min_Swaps("1101","1110") == 1
"""
def min_Swaps(str1, str2):
    # Count the number of differing bits between the two strings
    diff_count = sum(1 for bit1, bit2 in zip(str1, str2) if bit1 != bit2)
    
    # The minimum number of swaps required is half the difference in the number of ones in both strings
    return diff_count // 2

# Test cases
assert min_Swaps("1101", "1110") == 1
assert min_Swaps("1010", "0000") == 3
assert min_Swaps("1111", "1111") == 0
assert min_Swaps("0000", "1111") == 4