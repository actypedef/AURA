"""
Write a function to check if the given number is woodball or not.
assert is_woodall(383) == True
"""
def is_woodall(n):
    """
    Check if the given number is a Woodall number or not.
    A Woodall number is of the form n * 2^n + 1 for some integer n.
    """
    n = 1
    while True:
        woodall = n * 2**n + 1
        if woodall == n:
            return True
        elif woodall > n:
            return False
        n += 1

# Test cases
assert is_woodall(383) == True
assert is_woodall(15) == True
assert is_woodall(10) == False