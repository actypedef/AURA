"""
Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
assert find_Rotations("aaaa") == 1
"""
def find_Rotations(s):
    """
    Write a python function to find the minimum number of rotations (greater than 0) required to get the same string.
    """
    n = len(s)
    for i in range(1, n):
        if s[i:] + s[:i] == s:
            return i
    return n

# Test cases
assert find_Rotations("aaaa") == 1
assert find_Rotations("abc") == 3
assert find_Rotations("abab") == 2
assert find_Rotations("abcd") == 4
assert find_Rotations("ababab") == 2
assert find_Rotations("abababab") == 2
assert find_Rotations("ababababab") == 2
assert find_Rotations("abababababab") == 2
assert find_Rotations("ababababababab") == 2
assert find_Rotations("abababababababab") == 2
assert find_Rotations("ababababababababab") == 2
assert find_Rotations("abababababababababab") == 2
assert find_Rotations("ababababababababababab") == 2
assert find_Rotations("abababababababababababab") == 2
assert find_Rotations("ababababababababababababab") == 2
assert find_Rotations("abababababababababababababab") == 2
assert find_Rotations("ababababababababababababababab") == 2
assert find_Rotations("abababababababababababababababab") == 2
assert find_Rotations("ababababababababababababababababab") == 2
assert find_Rotations("abababababababababababababababababab") == 2
assert find_Rotations("ababababababababababababababababababab") == 2
assert find_Rotations("abababababababababababababababababababab") == 2
assert find_Rotations("ababababababababababababababababababababab") == 2
assert find_Rotations("abababababababababababababababababababababab") == 2
assert find_Rotations("ababababababababababababababababababababababab") == 2
assert find_Rotations("abababababababababababababababababababababababab") == 2
assert find_Rotations("ababababababababababababababababababababababababab") == 2
assert find_Rotations("abababababababababababababababababababababababababab") == 2
assert find_Rotations("abababababababababababababababababababababababab