

def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """
    for i in range(n - 1, 0, -1):
        if n % i == 0:
            return i
    return 1

# Test cases
assert largest_divisor(15) == 5
assert largest_divisor(25) == 5
assert largest_divisor(100) == 50
assert largest_divisor(1) == 1
assert largest_divisor(2) == 1
assert largest_divisor(3) == 1
assert largest_divisor(4) == 2
assert largest_divisor(5) == 1
assert largest_divisor(6) == 3
assert largest_divisor(7) == 1
assert largest_divisor(8) == 4
assert largest_divisor(9) == 3
assert largest_divisor(10) == 5
assert largest_divisor(11) == 1
assert largest_divisor(12) == 6
assert largest_divisor(13) == 1
assert largest_divisor(14) == 7
assert largest_divisor(15) == 5
assert largest_divisor(16) == 8
assert largest_divisor(17) == 1
assert largest_divisor(18) == 9
assert largest_divisor(19) == 1
assert largest_divisor(20) == 10
assert largest_divisor(21) == 7
assert largest_divisor(22) == 11
assert largest_divisor(23) == 1
assert largest_divisor(24) == 12
assert largest_divisor(25) == 5
assert largest_divisor(26) == 13
assert largest_divisor(27) == 9
assert largest_divisor(28) == 14
assert largest_divisor(29) == 1
assert largest_divisor(30) == 15
assert largest_divisor(31) == 1
assert largest_divisor(32) == 16
assert largest_divisor(33) == 11
assert largest_divisor(34) == 17
assert largest_divisor(35) == 7
assert largest_divisor(36) == 18
assert largest_divisor(37) == 1
assert largest_divisor(38) == 19
assert largest_divisor(39) == 13
assert largest_divisor(40) == 20
assert largest_divisor(41) == 1
assert largest_divisor(42) == 21
assert largest_divisor(43) == 1
assert largest_divisor(44) == 22
assert largest_divisor(45) == 15
assert largest_divisor(46) == 23
assert largest_divisor(47) == 1
assert largest_divisor(48) == 24
assert largest_divisor(49) == 7
assert largest_divisor(50) == 25
assert largest_divisor(51) == 17
assert largest_divisor(52) == 26
assert largest_divisor(53) ==