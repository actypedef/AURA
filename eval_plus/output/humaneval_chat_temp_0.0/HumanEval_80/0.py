
def is_happy(s):
    """You are given a string s.
    Your task is to check if the string is happy or not.
    A string is happy if its length is at least 3 and every 3 consecutive letters are distinct
    For example:
    is_happy(a) => False
    is_happy(aa) => False
    is_happy(abcd) => True
    is_happy(aabb) => False
    is_happy(adb) => True
    is_happy(xyy) => False
    """
def is_happy(s):
    # Check if the length of the string is less than 3
    if len(s) < 3:
        return False
    
    # Iterate through the string up to the third last character
    for i in range(len(s) - 2):
        # Check if any three consecutive characters are the same
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False
    
    # If no three consecutive characters are the same, the string is happy
    return True

# Test cases