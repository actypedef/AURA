"""
Write a python function to identify non-prime numbers.
assert is_not_prime(2) == False
"""
def is_not_prime(n):
    if n <= 1:
        return True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False

# Test cases
assert is_not_prime(2) == False
assert is_not_prime(3) == False
assert is_not_prime(4) == True
assert is_not_prime(5) == False
assert is_not_prime(6) == True
assert is_not_prime(7) == False
assert is_not_prime(8) == True
assert is_not_prime(9) == True
assert is_not_prime(10) == True
assert is_not_prime(11) == False
assert is_not_prime(12) == True
assert is_not_prime(13) == False
assert is_not_prime(14) == True
assert is_not_prime(15) == True
assert is_not_prime(16) == True
assert is_not_prime(17) == False
assert is_not_prime(18) == True
assert is_not_prime(19) == False
assert is_not_prime(20) == True
assert is_not_prime(21) == True
assert is_not_prime(22) == True
assert is_not_prime(23) == False
assert is_not_prime(24) == True
assert is_not_prime(25) == True
assert is_not_prime(26) == True
assert is_not_prime(27) == True
assert is_not_prime(28) == True
assert is_not_prime(29) == False
assert is_not_prime(30) == True
assert is_not_prime(31) == False
assert is_not_prime(32) == True
assert is_not_prime(33) == True
assert is_not_prime(34) == True
assert is_not_prime(35) == True
assert is_not_prime(36) == True
assert is_not_prime(37) == False
assert is_not_prime(38) == True
assert is_not_prime(39) == True
assert is_not_prime(40) == True
assert is_not_prime(41) == False
assert is_not_prime(42) == True
assert is_not_prime(43) == False
assert is_not_prime(44) == True
assert is_not_prime(45) == True
assert is_not_prime(46) == True
assert is_not_prime(47) == False
assert is_not_prime(48) == True
assert is_not_prime(49) == True
assert is_not_prime(50) == True
assert is_not_prime(51) == True
assert is_not_prime(52) == True
assert is_not_prime(53) == False
assert is_not_prime(54) == True
assert is_not_prime(55) == True
assert is_not_prime(56) == True
assert is_not_prime(57) == True
assert is_not_prime(58) == True
assert is_not_prime(59) == False
assert is_not_prime(60) == True
assert is_not_prime(61) == False
assert is_not_prime(62) == True
assert is_not_prime(63) == True
assert is_not_prime(64) == True
assert is_not_prime(65) == True
assert is_not_prime(66) == True
assert is_not_prime