"""
Write a function to check if a string represents an integer or not.
assert check_integer("python")==False
"""
def check_integer(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Test cases
assert check_integer("python") == False
assert check_integer("123") == True
assert check_integer("-456") == True
assert check_integer("0") == True
assert check_integer("abc") == False
assert check_integer("123.45") == False
assert check_integer("+789") == True
assert check_integer("-12345678901234567890") == True
assert check_integer("1e+10") == True
assert check_integer("1e-10") == True
assert check_integer("1E+10") == True
assert check_integer("1E-10") == True
assert check_integer("1.23e+10") == True
assert check_integer("1.23e-10") == True
assert check_integer("1.23e+10.1") == False
assert check_integer("1.23e-10.1") == False
assert check_integer("1.23e+10.0") == True
assert check_integer("1.23e-10.0") == True
assert check_integer("1.23e+10.00") == True
assert check_integer("1.23e-10.00") == True
assert check_integer("1.23e+10.000") == True
assert check_integer("1.23e-10.000") == True
assert check_integer("1.23e+10.0000") == True
assert check_integer("1.23e-10.0000") == True
assert check_integer("1.23e+10.00000") == True
assert check_integer("1.23e-10.00000") == True
assert check_integer("1.23e+10.000000") == True
assert check_integer("1.23e-10.000000") == True
assert check_integer("1.23e+10.0000000") == True
assert check_integer("1.23e-10.0000000") == True
assert check_integer("1.23e+10.00000000") == True
assert check_integer("1.23e-10.00000000") == True
assert check_integer("1.23e+10.000000000") == True
assert check_integer("1.23e-10.000000000") == True
assert check_integer("1.23e+10.0000000000") == True
assert check_integer("1.23e-10.0000000000") == True
assert check_integer("1.23e+10.00000000000") == True
assert check_integer("1.23e-10.00000000000") == True
assert check_integer("1.23e+10