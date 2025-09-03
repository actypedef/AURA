
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
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if s[i] == s[i + 1] or s[i] == s[i + 2] or s[i + 1] == s[i + 2]:
            return False
    return True


def test():
    assert is_happy("a") == False
    assert is_happy("aa") == False
    assert is_happy("abcd") == True
    assert is_happy("aabb") == False
    assert is_happy("adb") == True
    assert is_happy("xyy") == False
    assert is_happy("xyz") == True
    assert is_happy("xyzz") == False
    assert is_happy("xyzzy") == False
    assert is_happy("xyzzyx") == False
    assert is_happy("xyzzyxy") == False
    assert is_happy("xyzzyxyx") == False
    assert is_happy("xyzzyxyxy") == False
    assert is_happy("xyzzyxyxyx") == False
    assert is_happy("xyzzyxyxyxy") == False
    assert is_happy("xyzzyxyxyxyx") == False
    assert is_happy("xyzzyxyxyxyxy") == False
    assert is_happy("xyzzyxyxyxyxyx") == False
    assert is_happy("xyzzyxyxyxyxyxy") == False
    assert is_happy("xyzzyxyxyxyxyxyx") == False
    assert is_happy("xyzzyxyxyxyxyxyxy") == False
    assert is_happy("xyzzyxyxyxyxyxyxyx") == False
    assert is_happy("xyzzyxyxyxyxyxyxyxy") == False
    assert is_happy("xyzzyxyxyxyxyxyxyxyx") == False
    assert is_happy("xyzzyxyxyxyxyxyxyxyxy") == False
    assert is_happy("xyzzyxyxyxyxyxyxyxyxyx") == False
    assert is_happy("xyzzyxyxyxyxyxyxyxyxyxy") == False
    assert is_happy("xyzzyxyxyxyxyxyxyxyxyxyx") == False
    assert is_happy("xyzzyxyxyxyxyxyxyxyxyxyxy") == False
    assert is_happy("xyzzyxyxyxyxyxyxyxyxyxyxyx") == False
    assert is_happy("xyzzyxyxyxyxyxyxyxyxyxyxyxy") == False
    assert is_happy("xyzzyxyxyxyxyxyxyxyxyxyxyxyx") == False
    assert is_happy("xyzzyxyxyxyxyxyxyxyxyxyxyxyxy") == False
    assert is_happy("xyzzyxyxyxyxyxyxyxyxyxyxyxyxyx") == False
    assert is_happy("xyzzy