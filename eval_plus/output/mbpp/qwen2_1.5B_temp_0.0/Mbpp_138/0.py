"""
Write a python function to check whether the given number can be represented as sum of non-zero powers of 2 or not.
assert is_Sum_Of_Powers_Of_Two(10) == True
"""
def is_Sum_Of_Powers_Of_Two(n):
    # Check if n is a power of two
    return (n & (n - 1)) == 0

# Test cases
assert is_Sum_Of_Powers_Of_Two(10) == True
assert is_Sum_Of_Powers_Of_Two(7) == False
assert is_Sum_Of_Powers_Of_Two(8) == True
assert is_Sum_Of_Powers_Of_Two(31) == True
assert is_Sum_Of_Powers_Of_Two(64) == True
assert is_Sum_Of_Powers_Of_Two(65) == False