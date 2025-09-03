"""
Write a python function to check if a given number is one less than twice its reverse.
assert check(70) == False
"""
def check(n):
    """
    Check if a given number is one less than twice its reverse.
    """
    # Convert the number to a string to reverse it
    n_str = str(n)
    # Reverse the string
    n_rev_str = n_str[::-1]
    # Convert the reversed string back to an integer
    n_rev = int(n_rev_str)
    # Check if the number is one less than twice its reverse
    return n == 2 * n_rev - 1

# Test cases
assert check(70) == False
assert check(13) == True
assert check(25) == False
assert check(37) == True
assert check(49) == False
assert check(61) == True
assert check(73) == False
assert check(85) == True
assert check(97) == False
assert check(109) == True
assert check(121) == False
assert check(133) == True
assert check(145) == False
assert check(157) == True
assert check(169) == False
assert check(181) == True
assert check(193) == False
assert check(205) == True
assert check(217) == False
assert check(229) == True
assert check(241) == False
assert check(253) == True
assert check(265) == False
assert check(277) == True
assert check(289) == False
assert check(301) == True
assert check(313) == False
assert check(325) == True
assert check(337) == False
assert check(349) == True
assert check(361) == False
assert check(373) == True
assert check(385) == False
assert check(397) == True
assert check(409) == False
assert check(421) == True
assert check(433) == False
assert check(445) == True
assert check(457) == False
assert check(469) == True
assert check(481) == False
assert check(493) == True
assert check(505) == False
assert check(517) == True
assert check(529) == False
assert check(541) == True
assert check(553) == False
assert check(565) == True
assert check(577) == False
assert check(589) == True
assert check(601) == False
assert check(613) == True
assert check(625) == False
assert check(637) == True
assert check(649) == False
assert check(661) == True
assert check(673) == False
assert check(685) == True
assert check(697) == False
assert check(709) == True
assert check(721) == False
assert check(733) == True
assert check(745) == False
assert check(757) == True
assert check(769) == False
assert check(781) == True
assert check(793) == False