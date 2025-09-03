
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
    # Check if the length of b is greater than a, return False immediately
    if len(b) > len(a):
        return False
    
    # Concatenate 'b' with itself to handle cyclic patterns
    doubled_b = b + b
    
    # Check if 'a' contains any rotation of 'b'
    for i in range(len(b)):
        rotated_b = doubled_b[i:i+len(b)]
        if rotated_b in a:
            return True
    
    return False

# Test cases