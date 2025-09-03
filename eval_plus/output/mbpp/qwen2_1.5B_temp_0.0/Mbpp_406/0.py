"""
Write a python function to find whether the parity of a given number is odd.
assert find_Parity(12) == False
"""
def find_Parity(n):
    """
    Write a python function to find whether the parity of a given number is odd.
    
    Parameters:
    n (int): The number whose parity needs to be checked.
    
    Returns:
    bool: True if the number has an odd parity, False otherwise.
    """
    return n % 2 != 0

# Test cases
assert find_Parity(12) == False
assert find_Parity(7) == True
assert find_Parity(0) == False
assert find_Parity(3) == True
assert find_Parity(8) == False
assert find_Parity(5) == True
assert find_Parity(9) == True
assert find_Parity(4) == False
assert find_Parity(6) == False
assert find_Parity(2) == False
assert find_Parity(1) == True
assert find_Parity(10) == False
assert find_Parity(15) == True
assert find_Parity(20) == False
assert find_Parity(25) == True
assert find_Parity(30) == False
assert find_Parity(35) == True
assert find_Parity(40) == False
assert find_Parity(45) == True
assert find_Parity(50) == False
assert find_Parity(55) == True
assert find_Parity(60) == False
assert find_Parity(65) == True
assert find_Parity(70) == False
assert find_Parity(75) == True
assert find_Parity(80) == False
assert find_Parity(85) == True
assert find_Parity(90) == False
assert find_Parity(95) == True
assert find_Parity(100) == False
assert find_Parity(105) == True
assert find_Parity(110) == False
assert find_Parity(115) == True
assert find_Parity(120) == False
assert find_Parity(125) == True
assert find_Parity(130) == False
assert find_Parity(135) == True
assert find_Parity(140) == False
assert find_Parity(145) == True
assert find_Parity(150) == False
assert find_Parity(155) == True
assert find_Parity(160) == False
assert find_Parity(165) == True
assert find_Parity(170) == False
assert find_Parity(175) == True
assert find_Parity(180) == False
assert find_Parity(185) == True
assert find_Parity(190) == False
assert find_Parity(195) == True
assert find_Parity(200) == False
assert find_Parity(205) == True
assert find_Parity(210) == False
assert find_Parity(215) == True
assert find_Parity(220) == False
assert find_Parity(225) == True
assert find_Parity(230) == False
assert find_Parity(235) == True
assert find_Parity(240) == False
assert find_Parity(245) == True
assert find_Parity(250) == False
assert find_Parity(255)