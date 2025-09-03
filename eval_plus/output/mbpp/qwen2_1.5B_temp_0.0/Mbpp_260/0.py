"""
Write a function to find the nth newman–shanks–williams prime number.
assert newman_prime(3) == 7
"""
def newman_prime(n):
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    count = 0
    num = 2
    while True:
        if is_prime(num):
            count += 1
            if count == n:
                return num
        num += 1

# Test cases
assert newman_prime(3) == 7
assert newman_prime(4) == 11
assert newman_prime(5) == 13
assert newman_prime(6) == 17
assert newman_prime(7) == 19
assert newman_prime(8) == 23
assert newman_prime(9) == 29
assert newman_prime(10) == 31
assert newman_prime(11) == 37
assert newman_prime(12) == 41
assert newman_prime(13) == 43
assert newman_prime(14) == 47
assert newman_prime(15) == 53
assert newman_prime(16) == 59
assert newman_prime(17) == 61
assert newman_prime(18) == 67
assert newman_prime(19) == 71
assert newman_prime(20) == 73
assert newman_prime(21) == 79
assert newman_prime(22) == 83
assert newman_prime(23) == 89
assert newman_prime(24) == 97
assert newman_prime(25) == 101
assert newman_prime(26) == 103
assert newman_prime(27) == 107
assert newman_prime(28) == 109
assert newman_prime(29) == 113
assert newman_prime(30) == 127
assert newman_prime(31) == 131
assert newman_prime(32) == 137
assert newman_prime(33) == 139
assert newman_prime(34) == 149
assert newman_prime(35) == 151
assert newman_prime(36) == 157
assert newman_prime(37) == 163
assert newman_prime(38) == 167
assert newman_prime(39) == 173
assert newman_prime(40) == 179
assert newman_prime(41) == 181
assert newman_prime(42) == 191
assert newman_prime(43) == 193
assert newman_prime(44) == 197
assert newman_prime(45) == 199
assert newman_prime(46) == 211
assert newman_prime(47) == 223
assert newman_prime(48) == 227
assert newman_prime(49) == 229
assert newman_prime(50) == 233
assert newman_prime(51) == 239
assert newman_prime(