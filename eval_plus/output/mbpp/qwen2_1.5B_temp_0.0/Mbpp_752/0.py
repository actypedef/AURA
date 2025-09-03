"""
Write a function to find the nth jacobsthal number. https://www.geeksforgeeks.org/jacobsthal-and-jacobsthal-lucas-numbers/ 0, 1, 1, 3, 5, 11, 21, 43, 85, 171, 341, 683, 1365, 2731, ...
assert jacobsthal_num(5) == 11
"""
def jacobsthal_num(n):
    if n == 0 or n == 1:
        return n
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            c = a + 2 * b
            a = b
            b = c
        return b

# Test cases
assert jacobsthal_num(5) == 11
assert jacobsthal_num(6) == 21
assert jacobsthal_num(7) == 43
assert jacobsthal_num(8) == 85
assert jacobsthal_num(9) == 171
assert jacobsthal_num(10) == 341
assert jacobsthal_num(11) == 683
assert jacobsthal_num(12) == 1365
assert jacobsthal_num(13) == 2731
assert jacobsthal_num(14) == 5463
assert jacobsthal_num(15) == 10925
assert jacobsthal_num(16) == 21851
assert jacobsthal_num(17) == 43703
assert jacobsthal_num(18) == 87407
assert jacobsthal_num(19) == 174815
assert jacobsthal_num(20) == 349631