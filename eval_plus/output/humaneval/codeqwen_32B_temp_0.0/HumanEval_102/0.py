
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
def choose_num(x, y):
    """This function takes two positive numbers x and y and returns the
    biggest even integer number that is in the range [x, y] inclusive. If 
    there's no such number, then the function should return -1.

    For example:
    choose_num(12, 15) = 14
    choose_num(13, 12) = -1
    """
    if x > y:
        return -1
    if y % 2 == 0:
        return y
    if (y - 1) >= x:
        return y - 1
    return -1

def check(candidate):
    assert candidate(12, 15) == 14
    assert candidate(13, 12) == -1
    assert candidate(11, 11) == -1
    assert candidate(1, 1) == -1
    assert candidate(1, 100) == 100
    assert candidate(100, 1) == -1
    assert candidate(7, 19) == 18
    assert candidate(21, 29) == 28
    assert candidate(5, 5) == -1
    assert candidate(80, 80) == 80
    assert candidate(99, 99) == -1
    assert candidate(100, 100) == 100
    assert candidate(63, 63) == -1
    assert candidate(63, 64) == 64
    assert candidate(63, 65) == 64
    assert candidate(63, 66) == 66
    assert candidate(63, 67) == 66
    assert candidate(63, 68) == 68
    assert candidate(63, 69) == 68
    assert candidate(63, 70) == 70
    assert candidate(63, 71) == 70
    assert candidate(63, 72) == 72
    assert candidate(63, 73) == 72
    assert candidate(63, 74) == 74
    assert candidate(63, 75) == 74
    assert candidate(63, 76) == 76
    assert candidate(63, 77) == 76
    assert candidate(63, 78) == 78
    assert candidate(63, 79) == 78
    assert candidate(63, 80) == 80
    assert candidate(63, 81) == 80
    assert candidate(63, 82) == 82
    assert candidate(63, 83) == 82
    assert candidate(63, 84) == 84
    assert candidate(63, 85) == 84
    assert candidate(63, 86) == 86
    assert candidate(63, 87) == 86
    assert candidate(63, 88) == 88
    assert candidate(63, 89) == 88
    assert candidate(63,