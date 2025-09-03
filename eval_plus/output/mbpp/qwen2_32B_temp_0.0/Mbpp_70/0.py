"""
Write a function to find whether all the given tuples have equal length or not.
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
"""
def get_equal(tuples):
    """
    Write a function to find whether all the given tuples have equal length or not.
    """
    return all(len(t) == len(tuples[0]) for t in tuples)

# Test cases
assert get_equal([(11, 22, 33), (44, 55, 66)]) == True
assert get_equal([(11, 22, 33), (44, 55)]) == False
assert get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99)]) == True
assert get_equal([(11, 22, 33), (44, 55, 66), (77, 88)]) == False
assert get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99), (100, 111, 122)]) == True
assert get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99), (100, 111)]) == False
assert get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99), (100, 111, 122), (133, 144, 155)]) == True
assert get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99), (100, 111, 122), (133, 144)]) == False
assert get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99), (100, 111, 122), (133, 144, 155), (166, 177, 188)]) == True
assert get_equal([(11, 22, 33), (44, 55, 66), (77, 88, 99), (100, 111, 122), (133, 144, 155), (166, 177)]) == False