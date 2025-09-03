
def cycpattern_check(a , b):
    """You are given 2 words. You need to return True if the second word or any of its rotations is a substring in the first word
    cycpattern_check("abcd","abd") => False
    cycpattern_check("hello","ell") => True
    cycpattern_check("whassup","psus") => False
    cycpattern_check("abab","baa") => True
    cycpattern_check("efef","eeff") => False
    cycpattern_check("himenss","simen") => True

    """
def cycpattern_check(a, b):
    # Check if the second word or any of its rotations is a substring in the first word
    for i in range(len(b)):
        rotated_b = b[i:] + b[:i]  # Rotate the string b by i positions
        if rotated_b in a:  # Check if the rotated string is a substring of a
            return True
    return False

# Test cases