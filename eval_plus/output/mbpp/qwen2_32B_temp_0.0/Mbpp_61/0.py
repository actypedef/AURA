"""
Write a python function to count the number of substrings with the sum of digits equal to their length.
assert count_Substrings('112112') == 6
"""
def count_Substrings(s):
    """
    Count the number of substrings with the sum of digits equal to their length.
    """
    count = 0
    for i in range(len(s)):
        for j in range(i, len(s)):
            substring = s[i:j+1]
            if sum(int(digit) for digit in substring) == len(substring):
                count += 1
    return count

# Test cases
assert count_Substrings('112112') == 6
assert count_Substrings('111') == 6
assert count_Substrings('01110') == 10
assert count_Substrings('12345') == 15
assert count_Substrings('11111') == 15
assert count_Substrings('123456789') == 45
assert count_Substrings('1234567890') == 55
assert count_Substrings('12345678901') == 66
assert count_Substrings('123456789012') == 78
assert count_Substrings('1234567890123') == 91
assert count_Substrings('12345678901234') == 105
assert count_Substrings('123456789012345') == 120
assert count_Substrings('1234567890123456') == 136
assert count_Substrings('12345678901234567') == 153
assert count_Substrings('123456789012345678') == 171
assert count_Substrings('1234567890123456789') == 190
assert count_Substrings('12345678901234567890') == 210
assert count_Substrings('123456789012345678901') == 231
assert count_Substrings('1234567890123456789012') == 253
assert count_Substrings('12345678901234567890123') == 276
assert count_Substrings('123456789012345678901234') == 300
assert count_Substrings('1234567890123456789012345') == 325
assert count_Substrings('12345678901234567890123456') == 351
assert count_Substrings('123456789012345678901234567') == 378
assert count_Substrings('1234567890123456789012345678') ==