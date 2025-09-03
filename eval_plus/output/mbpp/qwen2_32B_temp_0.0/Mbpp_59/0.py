"""
Write a function to find the nth octagonal number.
assert is_octagonal(5) == 65
"""
def is_octagonal(n):
    return n * (3 * n - 2)

# Test cases
assert is_octagonal(1) == 1
assert is_octagonal(2) == 16
assert is_octagonal(3) == 37
assert is_octagonal(4) == 68
assert is_octagonal(5) == 105
assert is_octagonal(6) == 148
assert is_octagonal(7) == 197
assert is_octagonal(8) == 252
assert is_octagonal(9) == 313
assert is_octagonal(10) == 380
assert is_octagonal(11) == 453
assert is_octagonal(12) == 532
assert is_octagonal(13) == 617
assert is_octagonal(14) == 708
assert is_octagonal(15) == 805
assert is_octagonal(16) == 908
assert is_octagonal(17) == 1017
assert is_octagonal(18) == 1132
assert is_octagonal(19) == 1253
assert is_octagonal(20) == 1380
assert is_octagonal(21) == 1513
assert is_octagonal(22) == 1652
assert is_octagonal(23) == 1797
assert is_octagonal(24) == 1948
assert is_octagonal(25) == 2105
assert is_octagonal(26) == 2268
assert is_octagonal(27) == 2437
assert is_octagonal(28) == 2612
assert is_octagonal(29) == 2793
assert is_octagonal(30) == 2980
assert is_octagonal(31) == 3173
assert is_octagonal(32) == 3372
assert is_octagonal(33) == 3577
assert is_octagonal(34) == 3788
assert is_octagonal(35) == 4005
assert is_octagonal(36) == 4228
assert is_octagonal(37) == 4457
assert is_octagonal(38) == 4692
assert is_octagonal(39) == 4933
assert is_octagonal(40) == 5180
assert is_octagonal(41) == 5433
assert is_octagonal(42) == 5692
assert is_octagonal(43) == 5957
assert is_octagonal(44) == 6228
assert is_octagonal(45) == 6505
assert is_octagonal(46) == 6788
assert is_octagonal(47) == 7077
assert is_octagonal(48) == 7372
assert is_octagonal(49) == 7673
assert is_octagonal(50) == 7980
assert is_octagonal(51) == 8293
assert is_octagonal(52) == 8