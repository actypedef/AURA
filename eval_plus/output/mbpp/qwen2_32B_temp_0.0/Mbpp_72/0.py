"""
Write a python function to check whether the given number can be represented as the difference of two squares or not.
assert dif_Square(5) == True
"""
def dif_Square(n):
    """
    Check whether the given number can be represented as the difference of two squares or not.
    """
    # A number can be represented as the difference of two squares if and only if it is not of the form 4k+2
    return n % 4 != 2

# Test cases
assert dif_Square(5) == True
assert dif_Square(10) == False
assert dif_Square(15) == True
assert dif_Square(20) == False
assert dif_Square(25) == True
assert dif_Square(30) == False
assert dif_Square(35) == True
assert dif_Square(40) == False
assert dif_Square(45) == True
assert dif_Square(50) == False
assert dif_Square(55) == True
assert dif_Square(60) == False
assert dif_Square(65) == True
assert dif_Square(70) == False
assert dif_Square(75) == True
assert dif_Square(80) == False
assert dif_Square(85) == True
assert dif_Square(90) == False
assert dif_Square(95) == True
assert dif_Square(100) == False
assert dif_Square(105) == True
assert dif_Square(110) == False
assert dif_Square(115) == True
assert dif_Square(120) == False
assert dif_Square(125) == True
assert dif_Square(130) == False
assert dif_Square(135) == True
assert dif_Square(140) == False
assert dif_Square(145) == True
assert dif_Square(150) == False
assert dif_Square(155) == True
assert dif_Square(160) == False
assert dif_Square(165) == True
assert dif_Square(170) == False
assert dif_Square(175) == True
assert dif_Square(180) == False
assert dif_Square(185) == True
assert dif_Square(190) == False
assert dif_Square(195) == True
assert dif_Square(200) == False
assert dif_Square(205) == True
assert dif_Square(210) == False
assert dif_Square(215) == True
assert dif_Square(220) == False
assert dif_Square(225) == True
assert dif_Square(230) == False
assert dif_Square(235) == True
assert dif_Square(240) == False
assert dif_Square(245) == True
assert dif_Square(250) == False
assert dif_Square(255) == True
assert dif_Square(260) == False
assert dif_Square(265) == True
assert dif_Square(270) == False
assert dif_Square(275) == True
assert dif_Square(280) == False
assert dif_Square(285) == True
assert dif_Square(290) == False
assert dif_Square(295) == True
assert dif_Square(300)